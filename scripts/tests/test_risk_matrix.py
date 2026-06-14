"""COMP-01 — risk_matrix.py L×S scoring engine + D-02 LOCKED default bands.

This durable contract test re-asserts, over the on-disk engine + the
fixtures/risk_matrix_cases.json golden data:

  (a) score(L, S) on the DEFAULT_5X5 returns the multiply product (1..25) mapped
      to the D-02 LOCKED bands Low 1-4 / Medium 5-9 / High 10-15 / Critical
      16-25 — every fixture cell + every band edge maps to its correct
      score + band;
  (b) the High band_action is the verbatim spec string
      "Intolerable — stop / additional controls before proceeding";
  (c) a malformed MatrixConfig (a band gap) raises MatrixConfigError — never a
      silent fallback;
  (d) likelihood/severity outside 1..len(axis) raises ValueError;
  (e) score() is deterministic — identical input yields byte-identical output.

Bare imports resolve via scripts/tests/conftest.py (puts hse_components on
sys.path). Stdlib + the engine only; the A8 quality harness (Plan 04) keys off
this durable test.
"""

import copy
import json

import pytest

from risk_matrix import (
    DEFAULT_5X5,
    DEFAULT_BANDS,
    MatrixConfigError,
    load_matrix,
    score,
)

HIGH_BAND_ACTION = "Intolerable — stop / additional controls before proceeding"


def test_every_fixture_cell_maps_to_locked_band(risk_matrix_cases):
    """Each golden (L, S) cell scores to its expected multiply product + D-02 band."""
    cases = risk_matrix_cases["cases"]
    assert cases, "fixture must contain cases"
    for case in cases:
        result = score(case["likelihood"], case["severity"])
        assert result["score"] == case["expected_score"], case
        assert result["band"] == case["expected_band"], case
        assert result["likelihood"] == case["likelihood"]
        assert result["severity"] == case["severity"]
        assert result["matrix_size"] == "5x5"


def test_locked_band_cutoffs():
    """DEFAULT_BANDS uses the exact D-02 cut-offs 1-4 / 5-9 / 10-15 / 16-25."""
    by_name = {b["name"]: b for b in DEFAULT_BANDS}
    assert (by_name["Low"]["min"], by_name["Low"]["max"]) == (1, 4)
    assert (by_name["Medium"]["min"], by_name["Medium"]["max"]) == (5, 9)
    assert (by_name["High"]["min"], by_name["High"]["max"]) == (10, 15)
    assert (by_name["Critical"]["min"], by_name["Critical"]["max"]) == (16, 25)


def test_high_band_action_is_verbatim():
    """The High band_action is byte-identical to the spec's locked string."""
    result = score(2, 5)  # product 10 -> High
    assert result["band"] == "High"
    assert result["band_action"] == HIGH_BAND_ACTION


def test_band_gap_config_raises():
    """A non-contiguous band set (gap) raises MatrixConfigError — no silent fallback."""
    bad = copy.deepcopy(DEFAULT_5X5)
    # Introduce a gap: drop Medium's coverage of 5..9 -> 6..9 leaves 5 uncovered.
    for band in bad["bands"]:
        if band["name"] == "Medium":
            band["min"] = 6
    with pytest.raises(MatrixConfigError):
        load_matrix(bad)


def test_out_of_range_raises_value_error():
    """Likelihood/severity outside 1..len(axis) raises ValueError."""
    for bad in [(0, 3), (3, 0), (6, 3), (3, 6), (-1, 2)]:
        with pytest.raises(ValueError):
            score(bad[0], bad[1])


def test_score_is_deterministic():
    """score() called twice on the same input yields byte-identical output."""
    a = json.dumps(score(4, 5), sort_keys=True)
    b = json.dumps(score(4, 5), sort_keys=True)
    assert a == b
