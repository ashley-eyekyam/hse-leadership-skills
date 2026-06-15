"""test_b5_deid_pair.py — the B5 incident-investigation de-id fixture-PAIR contract (CORE-05 / §3.12 Eval 1).

B5 is the most data-sensitive skill in the pack, and its Eval 1 is the LOAD-BEARING
de-identification auto-fail PAIR. The deterministic de-id grader (the non-waivable
privacy hard block the whole pack depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/deid-incident-pii.md): a real injured-party
    name + a witness name + a home address + a phone + an Aadhaar number + a diagnosis + an
    embedded re-identification key + a 2-person (<5) amputation cell — auto_fail is True with
    reasons (proving the gate is live), and
  - PASS every clean fixture wired into a B5 eval CASE (deid-incident-clean.md,
    rca-systemic-trace.md, hoc-reportability.md): auto_fail is False (no false-positive),
    so the per-skill eval gate is not spuriously hard-failed.

This mirrors run_evals.run_deid_selftest against the canary, scoped to B5's own pair, and
follows the B1 precedent (the eval CASE wires the CLEAN fixture; THIS test is where the
seeded negative's catch is asserted). Pure deterministic Python: no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b5_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "incident-investigation" / "evals" / "files"
LEAK = FILES / "deid-incident-pii.md"
CLEAN = FILES / "deid-incident-clean.md"


def test_b5_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B5 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b5_clean_fixture_passes():
    """The paired clean positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B5 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b5_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B5 eval CASE (all but the seeded leak) must be
    de-id clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "deid-incident-clean.md",
        "rca-systemic-trace.md",
        "hoc-reportability.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
