"""test_b7_deid_pair.py — the B7 capa-manager de-id fixture-PAIR contract (CORE-07 / §3.9 Eval 2).

B7's Eval 2 is a de-identification auto-fail PAIR with PII located IN an INGESTED CAPA
register — the B7-specific risk surface: a register lifted from an audit / investigation
crosses a trust boundary into the managed report, and may carry the producer's raw
identifiers (T-05-19). The de-id block re-checks an ingested register, never assumes it is
clean. The deterministic de-id grader (the non-waivable privacy hard block the whole pack
depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/capa-pii.md): a real technician name +
    a supervisor name + a home address + a phone + an Aadhaar + a DOB + a health condition +
    an inline re-identification key + a 2-person (<5) injury cell — auto_fail is True with
    reasons (proving the gate is live), and
  - PASS the clean positive (evals/files/capa-clean.md): a properly de-identified managed
    register — auto_fail is False (proving no false-positive).

The eval CASE itself wires the CLEAN fixture so B7's per-skill eval gate passes without a
spurious hard-fail; THIS test is where the negative's catch is asserted. It also proves
every fixture wired into a B7 eval CASE is de-id clean. Pure deterministic Python: no
network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b7_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "capa-manager" / "evals" / "files"
LEAK = FILES / "capa-pii.md"
CLEAN = FILES / "capa-clean.md"


def test_b7_seeded_leak_fixture_is_caught():
    """The seeded-leak negative (PII in an ingested CAPA register) MUST trip the de-id
    auto-fail — the gate is live across the B6→B7 trust boundary (T-05-19)."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B7 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b7_clean_fixture_passes():
    """The paired clean positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B7 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b7_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B7 eval CASE (all but the seeded leak) must be
    de-id clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "lifecycle-happy-path.md",
        "capa-clean.md",
        "corrective-preventive-effectiveness.md",
        "ingest-b6-register.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
