"""SUB-02 — arcflash.py IEEE 1584-2018 incident-energy engine + NFPA 70E PPE.

This durable contract test re-asserts, over the on-disk engine + the
fixtures/arcflash_cases.json golden data:

  (a) golden — each fixture worked example lands within the published tolerances:
      incident energy +/-0.05 cal/cm2, boundary +/-10 mm, PPE category exact.
      AF-HCB is the PDF's authoritative published worked example (8.89 cal/cm2,
      3037 mm, category 3); AF-1/AF-2 are the genuine-model VCB 400 V cases;
      AF-VCBB/AF-VOA/AF-HOA are clearly-labelled engine regression anchors;
  (b) the J->cal unit conversion: the HCB case computes ~37.217 J/cm2 internally
      before the cal/cm2 conversion, and 8.89 cal/cm2 x 4.184 ~ 37.217 J/cm2;
  (c) range-invalid (D-03): Voc below the 208 V floor, above the 15 kV ceiling, a
      negative gap, and an unknown electrode all raise ArcFlashInputError (never
      a silent clamp);
  (d) the NFPA 70E PPE-band mapping (1.2/4/8/25/40) -> {0,1,2,3,4} + >40 flag;
  (e) incident_energy is deterministic -- identical input -> byte-identical output;
  (f) to_report_blocks emits only the 12 schema block types.

Bare imports resolve via scripts/tests/conftest.py (puts hse_components on
sys.path). Stdlib + the engine only.

The engine implements the GENUINE IEEE 1584-2018 model (D-01 re-implementation,
coefficients from the owner-supplied licensed copy); it reproduces the PDF's
fully-worked HCB example and its published intermediates. This closes todo
260621-p11-arcflash-coefficients-licensed-verify.
"""

import json

import pytest

from arcflash import (
    ArcFlashInputError,
    arc_flash_boundary,
    incident_energy,
    ppe_category,
    to_report_blocks,
)

# The 12 report.json block types (report_model_schema.json definitions).
ALLOWED_BLOCK_TYPES = {
    "heading", "paragraph", "bullets", "table", "metrics", "callout",
    "findings", "hoc_table", "recommendations", "divider", "page_break", "spacer",
}


def _load_cases():
    from pathlib import Path
    p = Path(__file__).resolve().parent / "fixtures" / "arcflash_cases.json"
    return json.loads(p.read_text(encoding="utf-8"))


def test_fixture_schema():
    """The golden fixture carries the versioned schema token."""
    data = _load_cases()
    assert data["schema"] == "hse-arcflash-cases/v1"
    assert data["cases"], "fixture must contain cases"


def test_golden_worked_examples_within_tolerance():
    """Each fixture case lands within the published tolerances (incl. AF-HCB)."""
    data = _load_cases()
    for case in data["cases"]:
        result = incident_energy(
            v_oc=case["v_oc"],
            i_bf_kA=case["i_bf_kA"],
            gap_mm=case["gap_mm"],
            electrode=case["electrode"],
            working_distance_mm=case["working_distance_mm"],
            arc_time_s=case["arc_time_s"],
            enclosure_mm=case.get("enclosure_mm"),
        )
        assert abs(
            result["incident_energy_cal_cm2"]
            - case["expected_incident_energy_cal_cm2"]
        ) <= 0.05, case
        assert abs(
            result["arc_flash_boundary_mm"] - case["expected_boundary_mm"]
        ) <= 10, case
        assert result["ppe_category"] == case["expected_ppe_category"], case


def test_hcb_published_anchor():
    """AF-HCB reproduces the PDF's authoritative worked example exactly."""
    result = incident_energy(
        v_oc=13800, i_bf_kA=18.241, gap_mm=152, electrode="HCB",
        working_distance_mm=914, arc_time_s=0.191,
        enclosure_mm=(1244.6, 1244.6, 1143),
    )
    assert abs(result["incident_energy_cal_cm2"] - 8.89) <= 0.05
    assert abs(result["arc_flash_boundary_mm"] - 3037) <= 10
    assert result["ppe_category"] == 3


def test_internal_j_per_cm2_before_conversion():
    """The HCB case computes ~37.217 J/cm2 internally before the cal/cm2 conversion.

    The unit trap: the model works in J/cm2 and divides by 4.184 only at the public
    boundary. This asserts both the internal J/cm2 value and the inverse relationship
    8.89 cal/cm2 x 4.184 ~ 37.217 J/cm2, catching any 4.184-factor slip.
    """
    result = incident_energy(
        v_oc=13800, i_bf_kA=18.241, gap_mm=152, electrode="HCB",
        working_distance_mm=914, arc_time_s=0.191,
        enclosure_mm=(1244.6, 1244.6, 1143),
    )
    assert abs(result["incident_energy_j_cm2"] - 37.217) <= 0.1
    # 8.89 cal/cm2 x 4.184 ~ 37.217 J/cm2
    assert abs(8.89 * 4.184 - 37.217) <= 0.1
    # the public cal/cm2 value x 4.184 reproduces the internal J/cm2 value
    assert abs(
        result["incident_energy_cal_cm2"] * 4.184 - result["incident_energy_j_cm2"]
    ) <= 0.05


def test_range_invalid_raises():
    """D-03: out-of-range / invalid input raises ArcFlashInputError."""
    base = dict(
        i_bf_kA=7.56, gap_mm=32, electrode="VCB",
        working_distance_mm=304.8, arc_time_s=0.11,
    )
    # Voc below the 208 V floor.
    with pytest.raises(ArcFlashInputError):
        incident_energy(v_oc=50, **base)
    # Voc above the 15 kV ceiling.
    with pytest.raises(ArcFlashInputError):
        incident_energy(v_oc=20_000, **base)
    # Negative gap.
    with pytest.raises(ArcFlashInputError):
        incident_energy(
            v_oc=400, i_bf_kA=7.56, gap_mm=-5, electrode="VCB",
            working_distance_mm=304.8, arc_time_s=0.11,
        )
    # Unknown electrode configuration.
    with pytest.raises(ArcFlashInputError):
        incident_energy(
            v_oc=400, i_bf_kA=7.56, gap_mm=32, electrode="NOPE",
            working_distance_mm=304.8, arc_time_s=0.11,
        )
    # Non-positive current / arc time.
    with pytest.raises(ArcFlashInputError):
        incident_energy(
            v_oc=400, i_bf_kA=0, gap_mm=32, electrode="VCB",
            working_distance_mm=304.8, arc_time_s=0.11,
        )
    with pytest.raises(ArcFlashInputError):
        incident_energy(
            v_oc=400, i_bf_kA=7.56, gap_mm=32, electrode="VCB",
            working_distance_mm=304.8, arc_time_s=0,
        )


def test_ppe_band_mapping():
    """The NFPA 70E thresholds 1.2/4/8/25/40 map to {0,1,2,3,4} + >40 flag."""
    assert ppe_category(0.5) == 0
    assert ppe_category(1.5) == 1
    assert ppe_category(5) == 2
    assert ppe_category(10) == 3
    assert ppe_category(30) == 4
    assert ppe_category(45) == ">40 — extreme"
    # Exact threshold edges (lower-inclusive).
    assert ppe_category(1.2) == 1
    assert ppe_category(4.0) == 2
    assert ppe_category(8.0) == 3
    assert ppe_category(25.0) == 4
    assert ppe_category(40.0) == 4


def test_incident_energy_is_deterministic():
    """incident_energy called twice on the same input → byte-identical output."""
    kw = dict(
        v_oc=13800, i_bf_kA=18.241, gap_mm=152, electrode="HCB",
        working_distance_mm=914, arc_time_s=0.191,
        enclosure_mm=(1244.6, 1244.6, 1143),
    )
    a = json.dumps(incident_energy(**kw), sort_keys=True)
    b = json.dumps(incident_energy(**kw), sort_keys=True)
    assert a == b


def test_arc_flash_boundary_standalone():
    """The boundary helper returns a positive distance for a known case."""
    db = arc_flash_boundary(8.89, 914, "HCB", enclosure_mm=(1244.6, 1244.6, 1143))
    assert db > 0


def test_report_blocks_use_allowed_types_only():
    """Every block type from to_report_blocks is in the 12-type schema allowlist."""
    result = incident_energy(
        v_oc=13800, i_bf_kA=18.241, gap_mm=152, electrode="HCB",
        working_distance_mm=914, arc_time_s=0.191,
        enclosure_mm=(1244.6, 1244.6, 1143),
    )
    blocks = to_report_blocks(result)
    assert blocks, "expected at least the metrics + table blocks"
    for block in blocks:
        assert block["type"] in ALLOWED_BLOCK_TYPES, block


def test_report_blocks_extreme_adds_critical_callout():
    """A >40 cal/cm² result appends a critical callout (still an allowed type)."""
    fake = {
        "incident_energy_cal_cm2": 55.0,
        "arc_flash_boundary_mm": 3000.0,
        "ppe_category": ">40 — extreme",
        "working": {
            "v_oc": 480, "i_bf_kA": 40, "gap_mm": 32, "electrode": "VCB",
            "working_distance_mm": 304.8, "arc_time_s": 0.5,
            "arcing_current_kA": 30.0,
        },
    }
    blocks = to_report_blocks(fake)
    types = [b["type"] for b in blocks]
    assert "callout" in types
    callout = next(b for b in blocks if b["type"] == "callout")
    assert callout["box_type"] == "critical"
    for block in blocks:
        assert block["type"] in ALLOWED_BLOCK_TYPES, block
