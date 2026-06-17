"""test_gen_marketplace_bundled_in.py — D-06 cross-bundle membership (Plan 06-01, Task 3).

A facilitator skill owned by one bundle (metadata.plugin) may also appear in other
bundles via metadata.bundled_in. build_manifest must list it in ALL of them while the
manifest stays derived from frontmatter alone (no second source of truth — WR-05).

Pure deterministic Python: a minimal fixture skill is written under a tmp repo root and
driven through build_manifest; no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/<this> -> repo/scripts on sys.path for `gen_marketplace`.
SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import gen_marketplace  # noqa: E402

_FM = """---
name: {name}
description: A fixture facilitator skill.
license: Apache-2.0
metadata:
  plugin: {plugin}
{bundled_in}---

# body
"""


def _write_skill(repo: Path, name: str, plugin: str, bundled_in=None) -> None:
    bi = ""
    if bundled_in:
        bi = "  bundled_in:\n" + "".join(f"    - {b}\n" for b in bundled_in)
    d = repo / "skills" / name
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(
        _FM.format(name=name, plugin=plugin, bundled_in=bi), encoding="utf-8"
    )


def test_bundled_in_skill_appears_in_all_three_bundles(tmp_path):
    """A skill plugin=hse-process + bundled_in=[hse-chemicals,hse-mining] is listed
    under all THREE bundles by build_manifest."""
    _write_skill(
        tmp_path, "permit-to-work", "hse-process",
        bundled_in=["hse-chemicals", "hse-mining"],
    )
    manifest = gen_marketplace.build_manifest(tmp_path)
    by_name = {p["name"]: [s.rsplit("/", 1)[-1] for s in p["skills"]] for p in manifest["plugins"]}

    assert "permit-to-work" in by_name.get("hse-process", []), "missing from owning bundle"
    assert "permit-to-work" in by_name.get("hse-chemicals", []), "missing from bundled_in chemicals"
    assert "permit-to-work" in by_name.get("hse-mining", []), "missing from bundled_in mining"


def test_no_bundled_in_leaves_single_bundle(tmp_path):
    """Absence of bundled_in keeps a skill in its owning bundle only (the ~33
    non-facilitator skills are unaffected)."""
    _write_skill(tmp_path, "risk-assessment", "hse-core")
    manifest = gen_marketplace.build_manifest(tmp_path)
    by_name = {p["name"]: [s.rsplit("/", 1)[-1] for s in p["skills"]] for p in manifest["plugins"]}

    assert by_name.get("hse-core") == ["risk-assessment"]
    # No phantom *bundled_in* bundles were minted. The synthesized hse-all
    # meta-plugin (07-04, D-13/D-14) is expected: it is the union of every
    # non-hse-systems bundle, so a lone hse-core skill folds into it.
    assert set(by_name) == {"hse-core", "hse-all"}
    assert by_name["hse-all"] == ["risk-assessment"]


def test_real_repo_check_stays_clean():
    """The live repo carries no bundled_in yet → the generated manifest is identical
    to disk (gen_marketplace --check semantics stay green at Wave-0)."""
    repo = SCRIPTS.parent
    generated = gen_marketplace._serialize(gen_marketplace.build_manifest(repo))
    on_disk = (repo / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    assert generated == on_disk, "Wave-0 baseline manifest drifted unexpectedly"
