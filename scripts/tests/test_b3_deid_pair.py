"""test_b3_deid_pair.py — the B3 toolbox-talk de-id fixture-PAIR contract (CORE-03 / §3.11 Eval 2).

B3's Eval 2 is a de-identification auto-fail PAIR. B3 is the single-threaded flagship,
so this test ALSO proves the inline de-id scrub runs even on a skill that never fans out
(Decision 6). The deterministic de-id grader (the non-waivable privacy hard block the
whole pack depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/scaffold-incident-pii.md): a real worker
    name + a re-identification key + a 2-person (<5) injury cell — auto_fail is True with
    reasons (proving the gate is live), and
  - PASS the clean positive (evals/files/scaffold-incident-clean.md): a properly
    de-identified version — auto_fail is False (proving no false-positive).

This mirrors run_evals.run_deid_selftest against the canary, scoped to B3's own pair.
The eval CASE itself wires the CLEAN fixture so B3's per-skill eval gate passes without a
spurious hard-fail; THIS test is where the negative's catch is asserted. Pure
deterministic Python: no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b3_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "toolbox-talk" / "evals" / "files"
LEAK = FILES / "scaffold-incident-pii.md"
CLEAN = FILES / "scaffold-incident-clean.md"


def test_b3_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail —
    proving the inline scrub gate is live even on the single-threaded flagship."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B3 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b3_clean_fixture_passes():
    """The paired clean positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B3 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b3_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B3 eval CASE (all but the seeded leak) must be de-id
    clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "reroof-bay3-clean.md",
        "scaffold-incident-clean.md",
        "manual-handling-short.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )


def test_b3_has_no_scripts_dir():
    """B3 declares NO A7 components, so the forge creates NO scripts/ symlink — the
    deliberate B3 divergence from B1/B5. The linter expects none; assert it here so an
    accidental over-scaffold is caught."""
    skill = REPO / "skills" / "toolbox-talk"
    assert not (skill / "scripts").exists(), (
        "B3 must NOT have a scripts/ dir (no A7 components — the single-thread divergence)"
    )
