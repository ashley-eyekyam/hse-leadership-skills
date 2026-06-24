"""test_forge_sync.py — the --sync anti-drift verb (A10 D5/D-07, T-04-04).

--sync re-copies the five canonical inline regions from template/blocks/* into a
drifted skill's in-marker regions, leaving everything BELOW each :end (the roster +
kb-selection rows the author owns) untouched. Proves:

- drift-restore: a hand-edited deid region is healed back to canonical;
- unified-diff printed on a real heal;
- --dry-run prints the diff and writes NOTHING;
- below-:end roster/rows are byte-identical after a sync (author work never clobbered);
- a clean skill is an idempotent no-op.

Skills are scaffolded under the real skills/ tree (so rule-9 paths resolve) and
removed in teardown.
"""

import contextlib
import io
import json
import re
import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent.parent
FORGE_SCRIPTS = REPO / "skills" / "hse-skill-forge" / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

for p in (str(FORGE_SCRIPTS), str(REPO / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import scaffold  # noqa: E402
import validate_repo_skill as V  # noqa: E402


@pytest.fixture
def skill(tmp_path_factory):
    ans = json.loads((FIXTURES / "probe_answers.json").read_text(encoding="utf-8"))
    d = scaffold.scaffold_skill("ztest-sync", ans, force=True)
    yield d
    shutil.rmtree(d, ignore_errors=True)


def _run_sync(skill_dir, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = V.sync_skill(skill_dir, **kw)
    return rc, buf.getvalue()


def test_clean_skill_is_noop(skill):
    orig = (skill / "SKILL.md").read_text(encoding="utf-8")
    rc, out = _run_sync(skill)
    assert rc == 0
    assert "already clean" in out
    assert (skill / "SKILL.md").read_text(encoding="utf-8") == orig


def test_dry_run_writes_nothing(skill):
    md = skill / "SKILL.md"
    drifted = md.read_text(encoding="utf-8").replace(
        "Apply this BEFORE you draft anything.", "Apply this WHENEVER you feel like it.", 1
    )
    md.write_text(drifted, encoding="utf-8")
    rc, out = _run_sync(skill, dry_run=True)
    assert rc == 0
    assert "---" in out and "+++" in out, "unified diff not printed"
    assert md.read_text(encoding="utf-8") == drifted, "--dry-run must not write"


def test_drift_restored_and_below_end_untouched(skill):
    md = skill / "SKILL.md"
    before = md.read_text(encoding="utf-8")
    roster_before = before.split("hse:block:orchestration:end -->", 1)[1]
    rows_before = before.split("hse:block:kb-selection:end -->", 1)[1].split(
        "hse:block:orchestration:start", 1
    )[0]

    drifted = before.replace(
        "Apply this BEFORE you draft anything.", "Apply this WHENEVER.", 1
    )
    md.write_text(drifted, encoding="utf-8")

    rc, out = _run_sync(skill)
    assert rc == 0
    healed = md.read_text(encoding="utf-8")

    # deid region restored to canonical.
    m = re.search(r"hse:block:deid:start -->(.*?)hse:block:deid:end -->", healed, re.S)
    assert "Apply this BEFORE you draft anything." in m.group(1)

    # below-:end roster + kb rows byte-identical (author work untouched).
    assert healed.split("hse:block:orchestration:end -->", 1)[1] == roster_before
    rows_after = healed.split("hse:block:kb-selection:end -->", 1)[1].split(
        "hse:block:orchestration:start", 1
    )[0]
    assert rows_after == rows_before


def test_sync_idempotent_after_heal(skill):
    md = skill / "SKILL.md"
    md.write_text(
        md.read_text(encoding="utf-8").replace(
            "Apply this BEFORE you draft anything.", "Apply this WHENEVER.", 1
        ),
        encoding="utf-8",
    )
    _run_sync(skill)            # heal
    healed = md.read_text(encoding="utf-8")
    rc, out = _run_sync(skill)  # second run = no-op
    assert rc == 0
    assert "already clean" in out
    assert md.read_text(encoding="utf-8") == healed


# --- repo-wide idempotency (FND-08 / GATE-03) ----------------------------------
#
# The per-skill `test_sync_idempotent_after_heal` proves a single drifted skill
# heals to a no-op. GATE-03 wants the REPO-WIDE guarantee on the real tree: after
# the Phase-10 block promotion + --sync landed, re-stamping ALL in-scope skills
# introduces ZERO drift, and a second --sync reports "already clean" for every dir
# with byte-identical SKILL.md. The in-scope dirs = `skills/*` MINUS
# `hse-skill-forge` (Rules 11/12-exempt) and any `examples/` path (frozen, D-08) —
# the same enumeration the cutover --sync uses. Settled count = 93 after the
# Phase 11–16 catalog build + the Phase-16.1 router (94 skill folders − the forge);
# the six policy-sensitive health skills stay in the catalog (D-11).

def _in_scope_skill_dirs():
    dirs = sorted(
        d for d in (REPO / "skills").iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file() and d.name != "hse-skill-forge"
    )
    return dirs


def test_sync_idempotent_repo_wide():
    dirs = _in_scope_skill_dirs()
    assert len(dirs) == 93, f"expected 93 in-scope skills, found {len(dirs)}"

    # Snapshot every SKILL.md, run --sync over the whole set (re-stamp), then assert
    # NO drift was introduced (the block is already in place from the cutover).
    before = {d: (d / "SKILL.md").read_text(encoding="utf-8") for d in dirs}
    for d in dirs:
        rc, out = _run_sync(d)
        assert rc == 0, f"--sync rc != 0 for {d.name}: {out}"
        assert (d / "SKILL.md").read_text(encoding="utf-8") == before[d], (
            f"--sync introduced drift in {d.name} (block region not already canonical)"
        )

    # SECOND run over the whole set = no-op on every dir: "already clean" + identical
    # bytes (idempotency).
    for d in dirs:
        rc, out = _run_sync(d)
        assert rc == 0, f"second --sync rc != 0 for {d.name}: {out}"
        assert "already clean" in out, (
            f"second --sync did not report 'already clean' for {d.name}: {out}"
        )
        assert (d / "SKILL.md").read_text(encoding="utf-8") == before[d], (
            f"second --sync changed bytes in {d.name}"
        )
