"""test_gen_marketplace_index_check.py — the P17 router-index drift gate (QUAL-04, D-08 W3).

Today `gen_marketplace.py --check` diffs the MANIFEST only. Phase 17 extends the
`--check` branch to ALSO regenerate the router skill-index in-memory and diff it
against the committed `skills/using-hse-skills/references/skill-index.yaml`,
exiting nonzero (and printing a unified diff) on index drift. The router itself
(`using-hse-skills`) and the contributor forge (`hse-skill-forge`) stay excluded
from the index (EXCLUDE_FROM_INDEX unchanged).

Pure deterministic Python: a tmp repo root is built with fixture skills + a
committed index, then driven through main(["--check", "--repo", ...]); no
network, no model, no key.
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
description: A fixture skill. Use this skill whenever you assess a fixture hazard.
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


def _seed_repo(tmp_path: Path) -> Path:
    """A tmp repo with two routable skills + the router + the forge, fully written
    (manifest + index in sync via --write)."""
    _write_skill(tmp_path, "risk-assessment", "hse-core")
    _write_skill(tmp_path, "permit-to-work", "hse-process")
    _write_skill(tmp_path, "using-hse-skills", "hse-core")
    _write_skill(tmp_path, "hse-skill-forge", "hse-systems")
    assert gen_marketplace.main(["--write", "--repo", str(tmp_path)]) == 0
    return tmp_path


def test_check_clean_after_write(tmp_path):
    """After --write, --check exits 0: BOTH the manifest AND the router index are in sync."""
    repo = _seed_repo(tmp_path)
    assert gen_marketplace.main(["--check", "--repo", str(repo)]) == 0


def test_check_fails_on_index_drift(tmp_path, capsys):
    """A drifted committed skill-index makes --check exit nonzero and print an index diff,
    even when the manifest itself is still in sync."""
    repo = _seed_repo(tmp_path)
    index_path = repo / "skills" / "using-hse-skills" / "references" / "skill-index.yaml"
    good = index_path.read_text(encoding="utf-8")
    # Corrupt one line of the committed index without touching any SKILL.md, so the
    # manifest stays clean and ONLY the index has drifted.
    index_path.write_text(good.replace("hse-core", "hse-WRONG", 1), encoding="utf-8")

    rc = gen_marketplace.main(["--check", "--repo", str(repo)])
    assert rc != 0, "drifted committed index must make --check fail"
    err = capsys.readouterr().err
    assert "skill-index" in err.lower(), "--check must name the drifted index in its diagnostic"


def test_router_and_forge_excluded_from_index(tmp_path):
    """EXCLUDE_FROM_INDEX is preserved: the router and the forge get no index row."""
    repo = _seed_repo(tmp_path)
    rows = gen_marketplace.build_skill_index(repo)
    names = {r["name"] for r in rows}
    assert "using-hse-skills" not in names
    assert "hse-skill-forge" not in names
    assert gen_marketplace.EXCLUDE_FROM_INDEX == {"using-hse-skills", "hse-skill-forge"}
