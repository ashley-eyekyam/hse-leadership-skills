"""QA-02 — the deterministic de-id auto-fail grader (A8 §4.4.1).

The de-id grader is the non-waivable HARD BLOCK for the privacy control: it must
PASS the clean fixture and AUTO-FAIL the seeded-leak fixture. A leak overrides the
weighted mean and cannot be waived (the distinct hard-fail enforcement class — NOT
the SME-persona FLAG class, which is a different mechanism handled in Plan 06).

Promotes the 18-HIPAA-id regex + region scan idiom from tests/test_deid_contract.py
into graders/deid.py. The grader checks the four A5 §3.5 conditions; ANY one trips
auto_fail.

sys.path is wired to scripts/ so `from graders.deid import grade_deid` resolves the
package the way run_evals.py imports it at runtime, regardless of invoking cwd.
"""

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

REPO = SCRIPTS.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"
CHECKLIST = REPO / "references" / "deid-checklist.md"

CLEAN = (FIXTURES / "deid_clean.txt").read_text(encoding="utf-8")
LEAK = (FIXTURES / "deid_leak.txt").read_text(encoding="utf-8")


def _grade(text):
    from graders.deid import grade_deid
    return grade_deid(text, CHECKLIST)


# --- fixture PAIR: both directions ---------------------------------------------

def test_clean_fixture_does_not_auto_fail():
    verdict = _grade(CLEAN)
    assert verdict["auto_fail"] is False, (
        f"clean fixture must NOT auto-fail; reasons: {verdict.get('reasons')}"
    )


def test_leak_fixture_auto_fails():
    verdict = _grade(LEAK)
    assert verdict["auto_fail"] is True, "seeded-leak fixture MUST auto-fail"


# --- the four A5 §3.5 conditions are each individually trippable ---------------

def test_residual_direct_identifier_trips_auto_fail():
    # A real-looking name + phone + DOB + Aadhaar (HIPAA 18-id + HSE addendum).
    verdict = _grade("Worker John Smith, DOB 1985-04-12, phone 555-867-5309.")
    assert verdict["auto_fail"] is True
    assert any("identifier" in r.lower() for r in verdict["reasons"])


def test_small_cell_under_5_trips_auto_fail():
    text = (
        "Injury summary — Hands = 7; Eyes = 3; Back = 2. "
        "A 2-person injury cell is published directly."
    )
    verdict = _grade(text)
    assert verdict["auto_fail"] is True
    assert any("cell" in r.lower() or "small" in r.lower() for r in verdict["reasons"])


def test_reidentification_key_in_output_trips_auto_fail():
    text = "Re-identification key: Worker-A = (a stable role label maps to a person)."
    verdict = _grade(text)
    assert verdict["auto_fail"] is True
    assert any("re-id" in r.lower() or "key" in r.lower() for r in verdict["reasons"])


def test_any_single_condition_overrides_weighted_mean():
    # The clean text passes; a single injected leak flips it — proving ANY one
    # condition is sufficient (overrides the weighted mean).
    assert _grade(CLEAN)["auto_fail"] is False
    poisoned = CLEAN + "\nResidual: contact Maria Gonzalez at maria@example.com.\n"
    assert _grade(poisoned)["auto_fail"] is True
