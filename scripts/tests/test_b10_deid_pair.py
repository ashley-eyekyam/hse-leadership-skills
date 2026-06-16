"""test_b10_deid_pair.py — the B10 incident-rate-calculator de-id/AGGREGATION PAIR contract (CORE-10 / §3.8 Eval 3).

B10's Eval 3 is a small-cell de-identification/AGGREGATION auto-fail PAIR. B10 is the
single-threaded deterministic wrapper, so this test ALSO proves the inline de-id scrub
runs even on a skill that never fans out: a pasted case log must be reduced to AGGREGATE
COUNTS ONLY before the engine is called. B10's distinctive leak vector is the raw case
log behind a rate — named individuals, single-case (<5) injury categories, and an
embedded re-identification key surviving into the circulated rate report. The
deterministic de-id grader (the non-waivable privacy hard block the whole pack depends
on) MUST:

  - CATCH the seeded-leak negative (evals/files/rate-caselog-pii.md): real worker names +
    a re-identification key + single-case (<5) injury cells narrated per-case — auto_fail
    is True with reasons (proving the aggregation gate is live), and
  - PASS the clean positive (evals/files/rate-caselog-clean.md): the same period reduced to
    aggregate counts only — auto_fail is False (proving no false-positive).

The eval CASE itself wires the CLEAN fixture so B10's per-skill eval gate passes without a
spurious hard-fail; THIS test is where the negative's catch is asserted. It also proves
every fixture wired into a B10 eval CASE is de-id/aggregation clean. Pure deterministic
Python: no network, no model, no key.
"""

from __future__ import annotations

import sys
from pathlib import Path

# scripts/tests/test_b10_deid_pair.py -> repo/scripts on sys.path for `graders`.
REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid  # noqa: E402

FILES = REPO / "skills" / "incident-rate-calculator" / "evals" / "files"
LEAK = FILES / "rate-caselog-pii.md"
CLEAN = FILES / "rate-caselog-clean.md"


def test_b10_seeded_leak_fixture_is_caught():
    """The seeded-leak negative (named per-case log + <5 cells + re-id key) MUST trip the
    deterministic de-id/aggregation auto-fail — proving the inline scrub gate is live even
    on the single-threaded deterministic wrapper."""
    verdict = grade_deid(LEAK.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is True, "B10 seeded-leak fixture did NOT hard-fail"
    assert verdict["reasons"], "auto_fail with no reason is not a real catch"


def test_b10_clean_fixture_passes():
    """The paired clean, aggregate-counts-only positive must NOT false-positive."""
    verdict = grade_deid(CLEAN.read_text(encoding="utf-8"))
    assert verdict["auto_fail"] is False, (
        f"B10 clean fixture false-positived: {verdict['reasons']}"
    )


def test_b10_all_clean_eval_fixtures_pass():
    """Every fixture wired into a B10 eval CASE (all but the seeded leak) must be
    de-id/aggregation clean, so the per-skill eval gate is not spuriously hard-failed."""
    for name in (
        "rate-caselog-clean.md",
        "known-inputs-trir.md",
        "missing-denominator.md",
    ):
        verdict = grade_deid((FILES / name).read_text(encoding="utf-8"))
        assert verdict["auto_fail"] is False, (
            f"{name} unexpectedly tripped de-id: {verdict['reasons']}"
        )
