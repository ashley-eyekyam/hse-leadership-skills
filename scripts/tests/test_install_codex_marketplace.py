"""test_install_codex_marketplace.py — personal-marketplace installer contract.

Locks scripts/install_codex_marketplace.py to the safety contract in the
Codex implementation brief:

  * fresh install creates ~/.agents/plugins/marketplace.json + an ABSOLUTE
    symlink, with `source.path` RELATIVE to HOME (codex-cli 0.142.5 resolves
    the personal marketplace against HOME and silently ignores absolute
    paths — verified empirically);
  * an existing personal marketplace is never overwritten wholesale — the
    top-level name, interface, and unrelated entries are preserved;
  * a differing same-name entry / link is replaced only with --update;
  * --dry-run writes nothing; re-runs are idempotent; --remove deletes only
    this plugin's entry and link/copy; --copy makes a real tree (.git
    excluded) for symlink-less filesystems.

Everything runs against tmp_path fixtures (isolated HOME + checkout) — no
real HOME, no network, no codex CLI.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# scripts/tests/<this> -> repo/scripts on sys.path for the installer module.
SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import install_codex_marketplace as icm  # noqa: E402

PLUGIN = "fixture-plugin"  # deliberately NOT the real name: proves no hard-coding


@pytest.fixture()
def checkout(tmp_path: Path) -> Path:
    repo = tmp_path / "checkout"
    (repo / ".codex-plugin").mkdir(parents=True)
    (repo / ".codex-plugin" / "plugin.json").write_text(
        json.dumps({"name": PLUGIN, "version": "1.0.0"}) + "\n", encoding="utf-8"
    )
    (repo / "skills" / "demo").mkdir(parents=True)
    (repo / "skills" / "demo" / "SKILL.md").write_text("---\nname: demo\n---\n")
    (repo / ".git").mkdir()
    (repo / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    return repo


@pytest.fixture()
def home(tmp_path: Path) -> Path:
    h = tmp_path / "home"
    h.mkdir()
    return h


def run(home: Path, checkout: Path, *extra: str) -> int:
    return icm.main(["--home", str(home), "--repo", str(checkout), *extra])


def read_marketplace(home: Path) -> dict:
    return json.loads(
        (home / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8")
    )


def link_path(home: Path) -> Path:
    return home / ".agents" / "plugins" / "plugins" / PLUGIN


def test_fresh_install_creates_marketplace_and_absolute_symlink(home, checkout):
    assert run(home, checkout) == 0
    m = read_marketplace(home)
    assert m["name"] == "personal"
    (entry,) = m["plugins"]
    assert entry["name"] == PLUGIN
    assert entry["source"] == {
        "source": "local",
        "path": f"./.agents/plugins/plugins/{PLUGIN}",
    }, "source.path must be RELATIVE to HOME — absolute paths are ignored by codex"
    assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    assert entry["category"] == "Productivity"
    link = link_path(home)
    assert link.is_symlink()
    assert link.readlink().is_absolute()
    assert link.resolve() == checkout.resolve()


def test_prints_add_command_with_real_marketplace_name(home, checkout, capsys):
    (home / ".agents" / "plugins").mkdir(parents=True)
    (home / ".agents" / "plugins" / "marketplace.json").write_text(
        json.dumps({"name": "my-mkt", "interface": {"displayName": "Mine"}, "plugins": []})
    )
    assert run(home, checkout) == 0
    out = capsys.readouterr().out
    assert f"codex plugin add {PLUGIN}@my-mkt" in out


def test_append_preserves_existing_marketplace(home, checkout):
    foreign = {
        "name": "other-plugin",
        "source": {"source": "local", "path": "./elsewhere"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
    (home / ".agents" / "plugins").mkdir(parents=True)
    (home / ".agents" / "plugins" / "marketplace.json").write_text(
        json.dumps(
            {"name": "my-mkt", "interface": {"displayName": "Mine"}, "plugins": [foreign]}
        )
    )
    assert run(home, checkout) == 0
    m = read_marketplace(home)
    assert m["name"] == "my-mkt"
    assert m["interface"] == {"displayName": "Mine"}
    assert m["plugins"][0] == foreign, "unrelated entries must be preserved untouched"
    assert m["plugins"][1]["name"] == PLUGIN
    assert len(m["plugins"]) == 2


def test_second_run_is_idempotent(home, checkout):
    assert run(home, checkout) == 0
    before = read_marketplace(home)
    assert run(home, checkout) == 0
    after = read_marketplace(home)
    assert before == after
    assert len(after["plugins"]) == 1


def test_dry_run_writes_nothing(home, checkout):
    assert run(home, checkout, "--dry-run") == 0
    assert not (home / ".agents").exists()


def test_differing_entry_requires_update(home, checkout):
    assert run(home, checkout) == 0
    m = read_marketplace(home)
    m["plugins"][0]["source"]["path"] = "./somewhere/stale"
    (home / ".agents" / "plugins" / "marketplace.json").write_text(json.dumps(m))
    assert run(home, checkout) == 1, "differing same-name entry must demand --update"
    assert read_marketplace(home)["plugins"][0]["source"]["path"] == "./somewhere/stale"
    assert run(home, checkout, "--update") == 0
    assert (
        read_marketplace(home)["plugins"][0]["source"]["path"]
        == f"./.agents/plugins/plugins/{PLUGIN}"
    )


def test_differing_symlink_requires_update(home, checkout, tmp_path):
    assert run(home, checkout) == 0
    link = link_path(home)
    stale = tmp_path / "stale-target"
    stale.mkdir()
    link.unlink()
    link.symlink_to(stale)
    assert run(home, checkout) == 1
    assert link.readlink() == stale
    assert run(home, checkout, "--update") == 0
    assert link.resolve() == checkout.resolve()


def test_remove_deletes_only_our_entry_and_link(home, checkout):
    foreign = {
        "name": "other-plugin",
        "source": {"source": "local", "path": "./elsewhere"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
    (home / ".agents" / "plugins").mkdir(parents=True)
    (home / ".agents" / "plugins" / "marketplace.json").write_text(
        json.dumps(
            {"name": "my-mkt", "interface": {"displayName": "Mine"}, "plugins": [foreign]}
        )
    )
    assert run(home, checkout) == 0
    assert run(home, checkout, "--remove") == 0
    m = read_marketplace(home)
    assert m["plugins"] == [foreign]
    assert m["name"] == "my-mkt"
    assert not link_path(home).exists() and not link_path(home).is_symlink()


def test_remove_when_not_installed_is_noop(home, checkout):
    assert run(home, checkout, "--remove") == 0
    assert not (home / ".agents").exists()


def test_copy_fallback_makes_real_tree_without_git(home, checkout):
    assert run(home, checkout, "--copy") == 0
    link = link_path(home)
    assert link.is_dir() and not link.is_symlink()
    assert (link / ".codex-plugin" / "plugin.json").is_file()
    assert (link / "skills" / "demo" / "SKILL.md").is_file()
    assert not (link / ".git").exists(), ".git must be excluded from copies"


def test_switching_copy_to_symlink_requires_update(home, checkout):
    assert run(home, checkout, "--copy") == 0
    assert run(home, checkout) == 1
    assert run(home, checkout, "--update") == 0
    assert link_path(home).is_symlink()


def test_refuses_non_plugin_repo(home, tmp_path):
    not_repo = tmp_path / "not-a-plugin"
    not_repo.mkdir()
    assert icm.main(["--home", str(home), "--repo", str(not_repo)]) == 1
