"""test_b2_deid_pair.py — the B2 job-safety-analysis de-id fixture-PAIR contract (CORE-02 / §3.9 Eval 2).

B2's Eval 2 is a de-identification auto-fail PAIR. The deterministic de-id grader (the
non-waivable privacy hard block the whole pack depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/manual-handling-jsa-pii.md): a real worker
    name + a home address + a phone + a health condition + a re-identification key + a
    2-person (<5) injury cell, and a name fabricated into the sign-off row —
    auto_fail is True with reasons (proving the gate is live), and
  - PASS the clean positive (evals/files/manual-handling-jsa-clean.md): a properly
    de-identified version with an empty-signature-row sign-off block — auto_fail is False
    (proving no false-positive).

The eval CASE itself wires the CLEAN fixture so B2's per-skill eval gate passes without a
spurious hard-fail; THIS test is where the negative's catch is asserted. It also proves
every fixture wired into a B2 eval CASE is de-id clean. Pure deterministic Python: no
network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b2_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "job-safety-analysis" / "evals" / "files"
LEAK = FILES / "manual-handling-jsa-pii.md"
CLEAN = FILES / "manual-handling-jsa-clean.md"


def test_b2_seeded_leak_fixture_is_caught():
    """The seeded-leak negative MUST trip the deterministic de-id auto-fail."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B2 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b2_clean_fixture_passes():
    """The paired clean positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B2 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b2_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B2 eval CASE (all but the seeded leak) must be
    de-id clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "tank-clean-jsa.md",
        "manual-handling-jsa-clean.md",
        "grinding-ppe-only-step.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
