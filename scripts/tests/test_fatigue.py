"""SUB-03 — fatigue.py FMCSA HOS + EU 561/2006 compliance + advisory index.

This durable contract test re-asserts, over the on-disk engine + the
fixtures/fatigue_cases.json golden data:

  (a) FMCSA window math — FAT-1 (12 h driving) -> driving_11h FAIL; every golden
      FMCSA flag matches exactly (booleans);
  (b) EU 561 window math — FAT-2 (5 h continuous) -> break_45min_after_4.5h FAIL;
      FAT-3 / FAT-3b -> the extension-aware daily_driving result (PASS with an
      extension available, FAIL when both are spent);
  (c) clean shift — FAT-4 all flags PASS + fatigue_index in [0,1];
  (d) the fatigue index is deterministic (same input -> scores within ±0.001 AND
      byte-identical json.dumps);
  (e) the index is LABELLED advisory (result["advisory"] is True) and is NOT a
      regulatory threshold;
  (f) FAT-5 invalid (D-03) — negative hours / a >24 h day raises
      FatigueInputError (never a silent clamp);
  (g) to_report_blocks emits only the 12 schema block types.

Bare imports resolve via scripts/tests/conftest.py (puts hse_components on
sys.path). Stdlib + the engine only; no new conftest is created.
"""

import json
from pathlib import Path

import pytest

from fatigue import (
    FatigueInputError,
    eu561_compliance,
    fatigue_index,
    fmcsa_compliance,
    to_report_blocks,
)

# The 12 report.json block types (the only ones to_report_blocks may emit).
_REPORT_BLOCK_TYPES = frozenset({
    "heading", "paragraph", "bullets", "table", "metrics", "callout",
    "findings", "hoc_table", "recommendations", "divider", "page_break", "spacer",
})

_FIXTURE = Path(__file__).resolve().parent / "fixtures" / "fatigue_cases.json"


def _cases():
    data = json.loads(_FIXTURE.read_text(encoding="utf-8"))
    assert data["schema"] == "hse-fatigue-cases/v1"
    assert data["cases"], "fixture must contain cases"
    return data["cases"]


def _case(case_id):
    for c in _cases():
        if c["id"] == case_id:
            return c
    raise AssertionError(f"fixture case {case_id} not found")


# --- (a) FMCSA compliance flag goldens ---------------------------------------

def test_fmcsa_golden_flags_match_fixture():
    """Every FMCSA fixture case maps to its expected per-rule booleans exactly."""
    checked = 0
    for case in _cases():
        if "expected_fmcsa" not in case:
            continue
        result = fmcsa_compliance(case["duty_log"])
        for flag, expected in case["expected_fmcsa"].items():
            assert result[flag] == expected, (case["id"], flag, result[flag])
            assert isinstance(result[flag], bool)
        assert isinstance(result["binding_limit"], str)
        checked += 1
    assert checked, "fixture must carry at least one FMCSA case"


def test_fat1_twelve_hours_driving_fails_11h_limit():
    """FAT-1: 12 h driving in one shift -> driving_11h is exactly False."""
    case = _case("FAT-1")
    result = fmcsa_compliance(case["duty_log"])
    assert result["driving_11h"] is False
    assert result["within_14h_window"] is True


# --- (b) EU 561 compliance flag goldens --------------------------------------

def test_eu561_golden_flags_match_fixture():
    """Every EU 561 fixture case maps to its expected per-rule booleans exactly."""
    checked = 0
    for case in _cases():
        if "expected_eu561" not in case:
            continue
        result = eu561_compliance(
            case["duty_log"], extensions_used=case.get("extensions_used", 0)
        )
        for flag, expected in case["expected_eu561"].items():
            assert result[flag] == expected, (case["id"], flag, result[flag])
            assert isinstance(result[flag], bool)
        checked += 1
    assert checked, "fixture must carry at least one EU 561 case"


def test_fat2_five_hours_continuous_fails_break_rule():
    """FAT-2: 5 h continuous driving, no break -> break_45min_after_4.5h False."""
    case = _case("FAT-2")
    result = eu561_compliance(case["duty_log"])
    assert result["break_45min_after_4.5h"] is False
    assert result["daily_driving"] is True  # 5 h <= 9 h base limit


def test_fat3_daily_driving_is_extension_aware():
    """FAT-3 / FAT-3b: 9.5 h driving -> daily_driving PASS with an extension
    available, FAIL when both twice-weekly extensions are spent."""
    fat3 = _case("FAT-3")
    fat3b = _case("FAT-3b")
    r3 = eu561_compliance(fat3["duty_log"], extensions_used=fat3["extensions_used"])
    r3b = eu561_compliance(fat3b["duty_log"], extensions_used=fat3b["extensions_used"])
    assert r3["daily_driving"] is True       # extensions_used=1 -> 10 h limit
    assert r3b["daily_driving"] is False      # extensions_used=2 -> 9 h limit binds


# --- (c) clean shift: all flags pass, index in range -------------------------

def test_fat4_clean_shift_all_flags_pass_and_index_in_range():
    """FAT-4: a clean compliant shift -> all FMCSA + EU flags True; index in [0,1]."""
    case = _case("FAT-4")
    fmcsa = fmcsa_compliance(case["duty_log"])
    eu = eu561_compliance(case["duty_log"], extensions_used=case.get("extensions_used", 0))
    assert all(fmcsa[k] for k in case["expected_fmcsa"])
    assert all(eu[k] for k in case["expected_eu561"])

    idx = fatigue_index(case["duty_log"], time_of_day=case.get("time_of_day"))
    assert 0.0 <= idx["score"] <= 1.0
    assert idx["band"] in {"Low", "Moderate", "High", "Severe"}


# --- (d) index determinism (±0.001 + byte-identical) -------------------------

def test_fatigue_index_is_deterministic():
    """Same input -> scores within ±0.001 AND byte-identical json.dumps."""
    case = _case("FAT-4")
    r1 = fatigue_index(case["duty_log"], time_of_day=case.get("time_of_day"))
    r2 = fatigue_index(case["duty_log"], time_of_day=case.get("time_of_day"))
    assert abs(r1["score"] - r2["score"]) <= 0.001
    assert json.dumps(r1, sort_keys=True) == json.dumps(r2, sort_keys=True)


# --- (e) the index is labelled ADVISORY, not a regulatory threshold ----------

def test_fatigue_index_is_labelled_advisory():
    """The result dict carries advisory: True and a derived-metric note."""
    case = _case("FAT-4")
    idx = fatigue_index(case["duty_log"], time_of_day=case.get("time_of_day"))
    assert idx["advisory"] is True
    assert "advisory" in idx["note"].lower()
    assert "not a regulatory threshold" in idx["note"].lower()
    # the LOCKED weights are surfaced and sum to 1.0
    w = idx["weights"]
    assert (w["driving"], w["time_awake"], w["time_of_day"]) == (0.4, 0.3, 0.3)


# --- (f) FAT-5 invalid (D-03 fail-loud) --------------------------------------

def test_fat5_negative_hours_raises():
    """Negative segment hours raise FatigueInputError (never a silent clamp)."""
    bad = [{"status": "driving", "hours": -3.0}]
    for fn in (fmcsa_compliance, eu561_compliance, fatigue_index):
        with pytest.raises(FatigueInputError):
            fn(bad)


def test_fat5_over_24h_day_raises():
    """A single-day duty total > 24 h raises FatigueInputError (D-03)."""
    bad = [
        {"status": "driving", "hours": 11.0},
        {"status": "on_duty", "hours": 8.0},
        {"status": "off_duty", "hours": 8.0},
    ]  # 27 h total
    for fn in (fmcsa_compliance, eu561_compliance, fatigue_index):
        with pytest.raises(FatigueInputError):
            fn(bad)


def test_malformed_segment_and_status_raise():
    """A non-dict segment or an unknown status raises FatigueInputError."""
    with pytest.raises(FatigueInputError):
        fmcsa_compliance(["not-a-dict"])
    with pytest.raises(FatigueInputError):
        fmcsa_compliance([{"status": "flying", "hours": 1.0}])
    with pytest.raises(FatigueInputError):
        fmcsa_compliance([])  # empty log


# --- (g) report blocks use only the 12 schema types --------------------------

def test_to_report_blocks_uses_only_schema_types():
    """Every block type emitted by to_report_blocks is in the 12-block allowlist."""
    case = _case("FAT-1")  # FAT-1 breaches a rule -> exercises the warning callout
    result = {
        "fmcsa": fmcsa_compliance(case["duty_log"]),
        "eu561": eu561_compliance(case["duty_log"]),
        "fatigue_index": fatigue_index(case["duty_log"], time_of_day=3.0),
    }
    blocks = to_report_blocks(result)
    assert blocks, "expected at least one report block"
    for block in blocks:
        assert block["type"] in _REPORT_BLOCK_TYPES, block["type"]
    # a breach must surface a warning callout
    callouts = [b for b in blocks if b["type"] == "callout"]
    assert any(b.get("box_type") == "warning" for b in callouts)
