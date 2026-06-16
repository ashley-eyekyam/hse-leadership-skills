"""test_b4_deid_pair.py — the B4 rams-builder de-id fixture-PAIR contract (CORE-04 / §3.9 Eval 2).

B4's Eval 2 is a de-identification auto-fail PAIR layered with the named-competent-persons
exception. The deterministic de-id grader (the non-waivable privacy hard block the whole
pack depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/excavation-pii.md): a real operative
    name + DOB + phone + home address + NI number + a near-miss note naming the injured
    worker + an embedded re-identification key + a 2-person (<5) injury cell —
    auto_fail is True with reasons (proving the gate is live), and
  - PASS the clean positive (evals/files/excavation-clean.md): a properly de-identified
    version — auto_fail is False (proving no false-positive).

The named-competent-persons EXCEPTION (the user-supplied competent persons in the
sign-off record stay NAMED; the briefing table ships with EMPTY signature rows) layers
ON TOP of this gate and does not weaken it — the leak the grader catches is the
INPUT-DERIVED PII, never the deliberately-assigned duty-holders.

This mirrors run_evals.run_deid_selftest against the canary, scoped to B4's own pair.
The eval CASE itself wires the CLEAN fixture so B4's per-skill eval gate passes without
a spurious hard-fail; THIS test is where the negative's catch is asserted. Pure
deterministic Python: no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b4_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "rams-builder" / "evals" / "files"
LEAK = FILES / "excavation-pii.md"
CLEAN = FILES / "excavation-clean.md"


def test_b4_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B4 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b4_clean_fixture_passes():
    """The paired clean positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B4 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b4_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B4 eval CASE (all but the seeded leak) must be
    de-id clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "scaffold-cladding-uk.md",
        "excavation-clean.md",
        "hotwork-generic.md",
        "lifting-india-mh.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
