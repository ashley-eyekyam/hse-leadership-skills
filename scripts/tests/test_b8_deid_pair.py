"""test_b8_deid_pair.py — the B8 sop-writer de-id PAIR contract (CORE-08).

B8's Eval 1 is a de-identification auto-fail PAIR. An SOP circulates widely and is
authored at the user's literacy level, so its distinctive leak vector is a residual
DIRECT identifier carried through from the source RA/JSA or from a named author/operator
(a worker's name, Aadhaar, date of birth, email, government ID, or phone in the
procedure text) instead of a role label. The deterministic de-id grader (the
non-waivable privacy hard block the whole pack depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/confined-space-sop-pii.md): residual
    direct identifiers in the SOP body — auto_fail is True with reasons (proving the
    de-id gate is live), and
  - PASS the clean positive (evals/files/confined-space-sop-clean.md): a role-labelled,
    de-identified SOP — auto_fail is False (proving no false-positive).

The eval CASE itself wires the CLEAN fixture so B8's per-skill eval gate passes without
a spurious hard-fail; THIS test is where the negative's catch is asserted. It also
proves every fixture wired into a B8 eval CASE is de-id clean. Pure deterministic
Python: no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b8_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "sop-writer" / "evals" / "files"
LEAK = FILES / "confined-space-sop-pii.md"
CLEAN = FILES / "confined-space-sop-clean.md"


def test_b8_seeded_leak_fixture_is_caught():
    """The seeded-leak negative (residual direct identifiers in the SOP body) MUST
    trip the deterministic de-id auto-fail."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B8 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b8_clean_fixture_passes():
    """The paired clean role-labelled positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B8 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b8_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B8 eval CASE (all but the seeded leak) must be de-id
    clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "confined-space-sop-clean.md",
        "noise-task-sop-weak.md",
        "printhead-changeover-jsa.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
