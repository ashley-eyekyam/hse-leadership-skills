"""SUB-01 — ergonomics.py NIOSH + RULA + REBA engine golden contract test.

This durable contract test re-asserts, over the on-disk engine + the
fixtures/ergonomics_cases.json golden data:

  (a) NIOSH golden — for each NIOSH case the computed RWL is within +/-0.05 kg
      of the expected value (anchor 11.39 kg) and LI within +/-0.01;
  (b) RULA golden — the integer grand_score (1-7) + action_level (1-4) equal
      the fixture exactly (no float tolerance — RULA produces integers);
  (c) REBA golden — the integer final_score (1-15) + action_level (1-5) equal
      the fixture exactly;
  (d) invalid / must-raise (D-03) — out-of-range or invalid input raises
      ErgonomicsInputError (a ValueError subclass), never a silent clamp;
  (e) determinism — niosh_rwl twice on identical input yields byte-identical
      JSON;
  (f) report-blocks contract — every block from to_report_blocks() carries a
      `type` in the 12-block report.json allowlist.

Bare imports resolve via the SHARED scripts/tests/conftest.py (puts
hse_components on sys.path) — no new conftest is created here. The fixture is
loaded inline with json.loads (an existing idiom). Stdlib + the engine only.
"""

import json
from pathlib import Path

import pytest

from ergonomics import (
    ErgonomicsInputError,
    niosh_rwl,
    reba_score,
    rula_score,
    to_report_blocks,
)

CASES_PATH = Path(__file__).resolve().parent / "fixtures" / "ergonomics_cases.json"

# The 12 schema block types to_report_blocks may emit (report_model_schema.json).
ALLOWED_BLOCK_TYPES = {
    "heading", "paragraph", "bullets", "table", "metrics", "callout",
    "findings", "hoc_table", "recommendations", "divider", "page_break", "spacer",
}


def _load_cases(engine):
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    assert data["schema"] == "hse-ergonomics-cases/v1"
    return [c for c in data["cases"] if c["engine"] == engine]


def test_fixture_has_all_three_sub_engines():
    """The golden fixture carries at least one NIOSH, RULA and REBA case."""
    assert _load_cases("niosh"), "no NIOSH cases"
    assert _load_cases("rula"), "no RULA cases"
    assert _load_cases("reba"), "no REBA cases"


def test_niosh_golden_within_tolerance():
    """Each NIOSH case lands within +/-0.05 kg RWL and +/-0.01 LI of expected."""
    cases = _load_cases("niosh")
    for case in cases:
        result = niosh_rwl(**case["inputs"])
        assert abs(result["rwl"] - case["expected_rwl"]) <= 0.05, case
        assert abs(result["li"] - case["expected_li"]) <= 0.01, case


def test_niosh_anchor_is_11_39():
    """The cross-confirmed NIOSH worked example lands at RWL ~= 11.39 kg."""
    result = niosh_rwl(weight=13.0, h=30, v=2, d=150, a=0,
                       frequency=0.2, duration=1, coupling="fair")
    assert abs(result["rwl"] - 11.39) <= 0.05
    assert result["li"] > 1.0  # elevated demand


def test_rula_golden_exact_integer():
    """Each RULA case matches the integer grand_score + action_level exactly."""
    cases = _load_cases("rula")
    for case in cases:
        result = rula_score(**case["inputs"])
        assert result["grand_score"] == case["expected_grand_score"], case
        assert 1 <= result["grand_score"] <= 7
        assert result["action_level"] == case["expected_action_level"], case
        assert 1 <= result["action_level"] <= 4
        assert result["working"]["score_a"] == case["expected_score_a"], case
        assert result["working"]["score_b"] == case["expected_score_b"], case


def test_reba_golden_exact_integer():
    """Each REBA case matches the integer final_score + action_level exactly."""
    cases = _load_cases("reba")
    for case in cases:
        result = reba_score(**case["inputs"])
        assert result["final_score"] == case["expected_final_score"], case
        assert 1 <= result["final_score"] <= 15
        assert result["action_level"] == case["expected_action_level"], case
        assert 1 <= result["action_level"] <= 5
        assert result["working"]["score_a"] == case["expected_score_a"], case
        assert result["working"]["score_b"] == case["expected_score_b"], case
        assert result["working"]["score_c"] == case["expected_score_c"], case


def test_niosh_invalid_raises():
    """Negative weight / out-of-domain geometry / bad coupling raise (D-03)."""
    with pytest.raises(ErgonomicsInputError):
        niosh_rwl(weight=-1, h=30, v=2, d=150)            # negative weight
    with pytest.raises(ErgonomicsInputError):
        niosh_rwl(weight=10, h=0, v=2, d=150)             # H <= 0
    with pytest.raises(ErgonomicsInputError):
        niosh_rwl(weight=10, h=30, v=-5, d=150)           # negative V
    with pytest.raises(ErgonomicsInputError):
        niosh_rwl(weight=10, h=30, v=2, d=150, a=-10)     # negative asymmetry
    with pytest.raises(ErgonomicsInputError):
        niosh_rwl(weight=10, h=30, v=2, d=150, coupling="excellent")  # bad key


def test_niosh_invalid_is_value_error_subclass():
    """ErgonomicsInputError is a ValueError subclass (callers can catch either)."""
    assert issubclass(ErgonomicsInputError, ValueError)
    with pytest.raises(ValueError):
        niosh_rwl(weight=-1, h=30, v=2, d=150)


def test_rula_out_of_range_joint_raises():
    """An out-of-range RULA joint score raises ErgonomicsInputError."""
    with pytest.raises(ErgonomicsInputError):
        rula_score(7, 2, 2, 1, 3, 3, 1)        # upper_arm 7 (>6)
    with pytest.raises(ErgonomicsInputError):
        rula_score(3, 2, 2, 1, 3, 3, 3)        # legs 3 (>2)
    with pytest.raises(ErgonomicsInputError):
        rula_score(3, 2, 2, 1, 3, 3, 1, force_a=5)  # force modifier > 3


def test_reba_out_of_range_joint_raises():
    """An out-of-range REBA joint score raises ErgonomicsInputError."""
    with pytest.raises(ErgonomicsInputError):
        reba_score(6, 2, 2, 1, 4, 1, 2)        # trunk 6 (>5)
    with pytest.raises(ErgonomicsInputError):
        reba_score(3, 2, 2, 1, 4, 1, 2, coupling=4)  # coupling > 3


def test_niosh_is_deterministic():
    """niosh_rwl twice on the same input yields byte-identical output."""
    kw = dict(weight=13.0, h=30, v=2, d=150, a=0,
              frequency=0.2, duration=1, coupling="fair")
    a = json.dumps(niosh_rwl(**kw), sort_keys=True)
    b = json.dumps(niosh_rwl(**kw), sort_keys=True)
    assert a == b


def test_rula_reba_are_deterministic():
    """RULA/REBA twice on the same input yield byte-identical output."""
    r1 = json.dumps(rula_score(3, 2, 2, 1, 3, 3, 1, force_a=1, force_b=1), sort_keys=True)
    r2 = json.dumps(rula_score(3, 2, 2, 1, 3, 3, 1, force_a=1, force_b=1), sort_keys=True)
    assert r1 == r2
    b1 = json.dumps(reba_score(3, 2, 2, 1, 4, 1, 2, coupling=1, activity=1), sort_keys=True)
    b2 = json.dumps(reba_score(3, 2, 2, 1, 4, 1, 2, coupling=1, activity=1), sort_keys=True)
    assert b1 == b2


def test_report_blocks_use_only_allowed_types():
    """Every to_report_blocks() block has a `type` in the 12-block allowlist."""
    results = [
        niosh_rwl(weight=13.0, h=30, v=2, d=150, a=0, coupling="fair"),
        rula_score(3, 2, 2, 1, 3, 3, 1, force_a=1, force_b=1),
        reba_score(3, 2, 2, 1, 4, 1, 2, coupling=1, activity=1),
    ]
    for result in results:
        blocks = to_report_blocks(result)
        assert isinstance(blocks, list) and blocks
        for block in blocks:
            assert block["type"] in ALLOWED_BLOCK_TYPES, block


def test_report_blocks_bad_input_raises():
    """to_report_blocks on a non-result dict raises ErgonomicsInputError."""
    with pytest.raises(ErgonomicsInputError):
        to_report_blocks({"not": "a result"})
    with pytest.raises(ErgonomicsInputError):
        to_report_blocks("nope")
