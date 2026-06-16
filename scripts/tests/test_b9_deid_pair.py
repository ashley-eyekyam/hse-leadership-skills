"""test_b9_deid_pair.py — the B9 board-safety-report de-id/AGGREGATION PAIR contract (CORE-09 / §3.9 Eval 1).

B9's Eval 1 is a de-identification/AGGREGATION auto-fail PAIR. B9's distinctive leak
vector is re-identification via a VIVID SINGLE-INCIDENT ANECDOTE at board altitude (a
fatality at a named small site in a stated month re-identifies the deceased even at
"aggregate" altitude) — not merely a bare name in a record. The deterministic de-id
grader (the non-waivable privacy hard block the whole pack depends on) MUST:

  - CATCH the seeded-leak negative (evals/files/board-period-pii.md): a single named
    incident narrated with an exact date + named small site, single-incident (<5)
    injury cells, and an embedded re-identification key — auto_fail is True with
    reasons (proving the aggregation gate is live), and
  - PASS the clean positive (evals/files/board-period-clean.md): a properly aggregated,
    de-identified period — auto_fail is False (proving no false-positive).

The eval CASE itself wires the CLEAN fixture so B9's per-skill eval gate passes without
a spurious hard-fail; THIS test is where the negative's catch is asserted. It also
proves every fixture wired into a B9 eval CASE is de-id/aggregation clean. Pure
deterministic Python: no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b9_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "board-safety-report" / "evals" / "files"
LEAK = FILES / "board-period-pii.md"
CLEAN = FILES / "board-period-clean.md"


def test_b9_seeded_leak_fixture_is_caught():
    """The seeded-leak negative (a vivid single-incident anecdote + <5 cells + re-id
    key) MUST trip the deterministic de-id/aggregation auto-fail."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B9 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b9_clean_fixture_passes():
    """The paired clean aggregated positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B9 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b9_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B9 eval CASE (all but the seeded leak) must be
    de-id/aggregation clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "board-period-clean.md",
        "board-period-richdata.md",
        "board-period-benchmark.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
