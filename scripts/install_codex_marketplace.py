#!/usr/bin/env python3
"""install_codex_marketplace.py — expose this checkout as a Codex plugin.

Registers the repository in the user's PERSONAL Codex marketplace
(`~/.agents/plugins/marketplace.json`, discovered implicitly by the Codex CLI)
so the plugin can be installed with:

    codex plugin add hse-leadership-skills@<marketplace-name>

The checkout stays the single canonical plugin root — nothing is duplicated.
By default a symlink at `~/.agents/plugins/plugins/<name>` points (absolute
target) at this checkout; `--copy` copies the tree instead on filesystems
without symlink support (a copy must be refreshed with `--update` after
pulling changes).

Empirically verified against codex-cli 0.142.5: the personal marketplace's
root is the HOME directory, so `source.path` entries must be RELATIVE paths
resolved from HOME (`./.agents/plugins/plugins/<name>`). Absolute
`source.path` values are silently ignored by the CLI — never write them.

Safety contract (mirrors the implementation brief):
  * never overwrites an existing personal marketplace wholesale — the
    top-level `name`, `interface`, and every unrelated plugin entry are
    preserved byte-for-byte;
  * appends this plugin's entry only when absent; an existing same-name
    entry is replaced only with an explicit `--update`;
  * `--remove` deletes only this plugin's entry and its managed link/copy;
  * `--dry-run` prints every planned change and writes nothing;
  * idempotent — re-running a completed install is a no-op;
  * every filesystem path created, modified, or removed is reported;
  * Codex configuration files (`~/.codex/*`) are never touched.

Stdlib only. Reuses the S2 main(argv)->int contract.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent

DEFAULT_MARKETPLACE_NAME = "personal"
DEFAULT_DISPLAY_NAME = "Personal"

POLICY = {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
CATEGORY = "Productivity"


def plugin_name(repo: Path) -> str:
    """Read the canonical plugin name from the Codex manifest — never hard-coded."""
    manifest = repo / ".codex-plugin" / "plugin.json"
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERROR: cannot read {manifest}: {exc}")
    name = payload.get("name")
    if not isinstance(name, str) or not name.strip():
        raise SystemExit(f"ERROR: {manifest} has no valid `name` field")
    return name


def desired_entry(name: str) -> Dict[str, Any]:
    return {
        "name": name,
        "source": {
            "source": "local",
            # Relative to the marketplace ROOT (= HOME for the personal
            # marketplace). Absolute paths are silently ignored by codex-cli.
            "path": f"./.agents/plugins/plugins/{name}",
        },
        "policy": dict(POLICY),
        "category": CATEGORY,
    }


def load_marketplace(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(
            f"ERROR: existing marketplace file {path} is unreadable or invalid JSON"
            f" ({exc}). Refusing to touch it — repair it by hand first."
        )
    if not isinstance(payload, dict):
        raise SystemExit(f"ERROR: {path} does not contain a JSON object. Refusing to touch it.")
    return payload


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    """Atomic-ish write: temp file in the same directory, then replace."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


class Reporter:
    """Collects and prints every filesystem change (or plan, in dry-run)."""

    def __init__(self, dry_run: bool) -> None:
        self.dry_run = dry_run
        self.changed = False

    def report(self, action: str) -> None:
        self.changed = True
        prefix = "PLAN" if self.dry_run else "CHANGE"
        print(f"{prefix}: {action}")

    def note(self, message: str) -> None:
        print(f"OK: {message}")


def ensure_link(
    link: Path, target: Path, copy: bool, update: bool, rep: Reporter
) -> bool:
    """Make `link` expose `target`. Returns False on a refusal."""
    if link.is_symlink():
        current = link.readlink()
        if not copy and current == target:
            rep.note(f"symlink already correct: {link} -> {target}")
            return True
        if not update:
            print(
                f"ERROR: {link} already exists (-> {current}) and differs from the"
                f" requested install. Re-run with --update to replace it.",
                file=sys.stderr,
            )
            return False
        rep.report(f"remove existing symlink {link} (-> {current})")
        if not rep.dry_run:
            link.unlink()
    elif link.exists():
        if not update:
            print(
                f"ERROR: {link} already exists and is not a symlink (a previous --copy"
                f" install, or unrelated data). Re-run with --update to replace it.",
                file=sys.stderr,
            )
            return False
        rep.report(f"remove existing directory tree {link}")
        if not rep.dry_run:
            if link.is_dir():
                shutil.rmtree(link)
            else:
                link.unlink()

    if copy:
        rep.report(f"copy {target} -> {link} (excluding .git; refresh with --update)")
        if not rep.dry_run:
            shutil.copytree(
                target, link, ignore=shutil.ignore_patterns(".git"), symlinks=False
            )
    else:
        rep.report(f"create symlink {link} -> {target} (absolute target)")
        if not rep.dry_run:
            link.symlink_to(target)
    return True


def do_install(args: argparse.Namespace, home: Path, repo: Path) -> int:
    rep = Reporter(args.dry_run)
    name = plugin_name(repo)
    mkt_dir = home / ".agents" / "plugins"
    mkt_file = mkt_dir / "marketplace.json"
    link = mkt_dir / "plugins" / name
    entry = desired_entry(name)

    marketplace = load_marketplace(mkt_file)
    if marketplace is None:
        marketplace = {
            "name": DEFAULT_MARKETPLACE_NAME,
            "interface": {"displayName": DEFAULT_DISPLAY_NAME},
            "plugins": [],
        }
        rep.report(f"create personal marketplace file {mkt_file}")
    mkt_name = marketplace.get("name", DEFAULT_MARKETPLACE_NAME)

    plugins: List[Dict[str, Any]] = marketplace.setdefault("plugins", [])
    existing = [p for p in plugins if isinstance(p, dict) and p.get("name") == name]
    entry_action = "append"
    if existing:
        if existing[0] == entry:
            rep.note(f"marketplace entry `{name}` already present and correct in {mkt_file}")
            entry_action = "none"
        elif not args.update:
            print(
                f"ERROR: marketplace entry `{name}` already exists in {mkt_file} but"
                f" differs from the requested install. Re-run with --update to replace"
                f" it (unrelated entries are never touched).",
                file=sys.stderr,
            )
            return 1
        else:
            entry_action = "replace"

    if not link.parent.exists():
        rep.report(f"create directory {link.parent}")
        if not rep.dry_run:
            link.parent.mkdir(parents=True, exist_ok=True)

    if not ensure_link(link, repo, args.copy, args.update, rep):
        return 1

    if entry_action == "append":
        rep.report(f"append plugin entry `{name}` to {mkt_file}")
        if not rep.dry_run:
            plugins.append(entry)
            write_json(mkt_file, marketplace)
    elif entry_action == "replace":
        rep.report(f"replace plugin entry `{name}` in {mkt_file} (others preserved)")
        if not rep.dry_run:
            plugins[plugins.index(existing[0])] = entry
            write_json(mkt_file, marketplace)

    if not rep.changed:
        rep.note("nothing to do — already installed")
    print()
    print("Next steps:")
    print(f"  codex plugin add {name}@{mkt_name}")
    print("  (then open a NEW Codex thread — plugins load on thread start)")
    return 0


def do_remove(args: argparse.Namespace, home: Path, repo: Path) -> int:
    rep = Reporter(args.dry_run)
    name = plugin_name(repo)
    mkt_dir = home / ".agents" / "plugins"
    mkt_file = mkt_dir / "marketplace.json"
    link = mkt_dir / "plugins" / name

    if link.is_symlink() or link.exists():
        if link.is_symlink():
            rep.report(f"remove symlink {link}")
            if not rep.dry_run:
                link.unlink()
        elif link.is_dir():
            rep.report(f"remove copied tree {link}")
            if not rep.dry_run:
                shutil.rmtree(link)
        else:
            rep.report(f"remove file {link}")
            if not rep.dry_run:
                link.unlink()

    marketplace = load_marketplace(mkt_file)
    if marketplace is not None:
        plugins = marketplace.get("plugins", [])
        kept = [p for p in plugins if not (isinstance(p, dict) and p.get("name") == name)]
        if len(kept) != len(plugins):
            rep.report(f"remove plugin entry `{name}` from {mkt_file} (others preserved)")
            if not rep.dry_run:
                marketplace["plugins"] = kept
                write_json(mkt_file, marketplace)

    if not rep.changed:
        rep.note("nothing to remove — plugin was not installed in the personal marketplace")
    else:
        print()
        print("Note: if the plugin was added with `codex plugin add`, also run:")
        print(f"  codex plugin remove {name}")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Register (or remove) this checkout as a Codex plugin in the user's"
            " personal marketplace (~/.agents/plugins/marketplace.json)."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print every planned filesystem change without writing anything",
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="copy the checkout instead of symlinking (for filesystems without"
        " symlinks; the copy must be refreshed with --update after changes)",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="replace an existing same-name marketplace entry and link/copy"
        " (unrelated entries are never touched)",
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="remove ONLY this plugin's marketplace entry and its link/copy",
    )
    parser.add_argument(
        "--home",
        type=Path,
        default=Path.home(),
        help=argparse.SUPPRESS,  # test hook: overrides the HOME directory
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=REPO,
        help=argparse.SUPPRESS,  # test hook: overrides the checkout path
    )
    args = parser.parse_args(argv)

    home = args.home.resolve()
    repo = args.repo.resolve()
    if not (repo / ".codex-plugin" / "plugin.json").is_file():
        print(f"ERROR: {repo} is not a Codex plugin root (missing .codex-plugin/plugin.json)", file=sys.stderr)
        return 1

    if args.remove:
        return do_remove(args, home, repo)
    return do_install(args, home, repo)


if __name__ == "__main__":
    sys.exit(main())
