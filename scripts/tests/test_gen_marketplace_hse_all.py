"""test_gen_marketplace_hse_all.py — D-13/D-14 hse-all meta-plugin synthesis (Plan 07-04, Task 2).

The `hse-all` one-line "install everything" plugin is SYNTHESIZED inside
build_manifest as the sorted union of every skill in any bundle EXCEPT
EXCLUDE_FROM_META (the build-time forge, hse-systems). Synthesis is the only
source of hse-all membership — no skill declares `metadata.plugin: hse-all`, so
adding a future consultant skill auto-folds it in with zero frontmatter edits
(Pitfall 4 / WR-05). These tests lock the union/exclusion/drift invariants and
the live `--check`-stays-green guarantee.

Pure deterministic Python: fixture skills are written under a tmp repo root and
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
description: A fixture skill.
license: Apache-2.0
metadata:
  plugin: {plugin}
---

# body
"""


def _write_skill(repo: Path, name: str, plugin: str) -> None:
    d = repo / "skills" / name
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(_FM.format(name=name, plugin=plugin), encoding="utf-8")


def _by_name(manifest):
    # Each plugin's `skills` are emitted as `./skills/<name>` paths (marketplace
    # schema requires component paths, not bare names); strip back to bare names so
    # these membership assertions read against the skill names.
    return {p["name"]: [s.rsplit("/", 1)[-1] for s in p["skills"]] for p in manifest["plugins"]}


def test_hse_all_is_union_minus_forge(tmp_path):
    """hse-all == sorted union of the two consultant bundles' skills; the
    hse-systems (forge) skill is excluded (D-13)."""
    _write_skill(tmp_path, "risk-assessment", "hse-core")
    _write_skill(tmp_path, "toolbox-talk", "hse-core")
    _write_skill(tmp_path, "permit-to-work", "hse-process")
    _write_skill(tmp_path, "hse-skill-forge", "hse-systems")

    by_name = _by_name(gen_marketplace.build_manifest(tmp_path))

    assert by_name["hse-all"] == [
        "permit-to-work",
        "risk-assessment",
        "toolbox-talk",
    ], "hse-all must be the sorted union of every non-hse-systems bundle's skills"
    assert "hse-skill-forge" not in by_name["hse-all"], "the forge must stay out of hse-all (D-13)"
    # Synthesis is the only source — the forge still has its own bundle entry.
    assert by_name["hse-systems"] == ["hse-skill-forge"]


def test_hse_all_auto_includes_new_skill(tmp_path):
    """Adding a third consultant skill auto-folds it into hse-all with NO
    frontmatter naming hse-all (drift guard, Pitfall 4 / WR-05)."""
    _write_skill(tmp_path, "risk-assessment", "hse-core")
    _write_skill(tmp_path, "permit-to-work", "hse-process")
    _write_skill(tmp_path, "fall-protection", "hse-mining")
    _write_skill(tmp_path, "hse-skill-forge", "hse-systems")

    by_name = _by_name(gen_marketplace.build_manifest(tmp_path))

    assert by_name["hse-all"] == [
        "fall-protection",
        "permit-to-work",
        "risk-assessment",
    ], "a new consultant skill must auto-appear in hse-all with no manual edit"
    # No fixture declared metadata.plugin: hse-all — membership is derived only.
    for name in ("risk-assessment", "permit-to-work", "fall-protection", "hse-skill-forge"):
        fm = gen_marketplace._frontmatter(tmp_path / "skills" / name / "SKILL.md")
        assert fm["metadata"]["plugin"] != "hse-all"


def test_real_repo_hse_all_membership():
    """Live repo: hse-all lists exactly 93 skills — the 92 consultant skills PLUS
    the catalog router `using-hse-skills` (owner override 2026-06-24, supersedes
    T-17-17: a newcomer installing the one-line pack needs the navigator). The
    catalog is 94 skill folders; hse-all omits only the contributor forge
    `hse-skill-forge` (EXCLUDE_FROM_META_SKILLS). The six policy-sensitive health
    skills stay in the catalog and in hse-all (D-11)."""
    repo = SCRIPTS.parent
    by_name = _by_name(gen_marketplace.build_manifest(repo))

    assert "hse-all" in by_name, "the synthesized hse-all plugin must exist in the live manifest"
    assert len(by_name["hse-all"]) == 93, "hse-all carries the 92 consultant skills + the using-hse-skills router (owner override of T-17-17)"
    assert "hse-skill-forge" not in by_name["hse-all"], "the forge must not leak into hse-all"
    assert "using-hse-skills" in by_name["hse-all"], "the router now ships in hse-all so a newcomer installing the one-line pack gets the catalog navigator (owner override of T-17-17)"
    # The six policy-sensitive health skills remain shipped in hse-all (D-11).
    for s in (
        "lab-biosafety-assessment", "workplace-violence-prevention",
        "sharps-needlestick-management", "infection-control-plan",
        "patient-handling-assessment", "health-risk-assessment",
    ):
        assert s in by_name["hse-all"], f"{s} must stay in the catalog (D-11)"
    # hse-all is exactly the union of the non-hse-systems bundles, minus only the
    # contributor forge named in EXCLUDE_FROM_META_SKILLS (the router now stays in).
    expected = sorted({
        s
        for name, skills in by_name.items()
        if name not in gen_marketplace.EXCLUDE_FROM_META and name != "hse-all"
        for s in skills
        if s not in gen_marketplace.EXCLUDE_FROM_META_SKILLS
    })
    assert by_name["hse-all"] == expected


def test_real_repo_check_stays_clean():
    """The on-disk marketplace.json equals a fresh build — the live
    `gen_marketplace.py --check`-stays-green invariant after hse-all synthesis."""
    repo = SCRIPTS.parent
    generated = gen_marketplace._serialize(gen_marketplace.build_manifest(repo))
    on_disk = (repo / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    assert generated == on_disk, "marketplace.json drifted; run `gen_marketplace.py --write`"
