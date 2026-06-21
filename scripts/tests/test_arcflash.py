"""SUB-02 — arcflash.py IEEE 1584-2018 incident-energy engine + NFPA 70E PPE.

This durable contract test re-asserts, over the on-disk engine + the
fixtures/arcflash_cases.json golden data:

  (a) golden — each fixture worked example (AF-1/AF-2, VCB) lands within the
      published tolerances: incident energy ±0.05 cal/cm², boundary ±10 mm,
      PPE category exact;
  (b) range-invalid (D-03, AF-3) — Voc below the 208 V floor, above the 15 kV
      ceiling, a negative gap, and an unknown electrode all raise
      ArcFlashInputError (never a silent clamp);
  (c) the NFPA 70E PPE-band mapping (1.2/4/8/25/40) → {0,1,2,3,4} + >40 flag;
  (d) incident_energy is deterministic — identical input → byte-identical output;
  (e) to_report_blocks emits only the 12 schema block types.

Bare imports resolve via scripts/tests/conftest.py (puts hse_components on
sys.path). Stdlib + the engine only.

NOTE: the embedded IEEE 1584-2018 coefficient block is PROVISIONAL — VCB is
anchored to the AF-1/AF-2 published worked examples; the other electrode configs
are unverified pending owner confirmation against a licensed copy.
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
    """Each fixture case (AF-1/AF-2) lands within the published tolerances."""
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


def test_provisional_note_present():
    """incident_energy advertises the provisional-coefficient caveat in notes."""
    result = incident_energy(
        v_oc=400, i_bf_kA=7.56, gap_mm=32, electrode="VCB",
        working_distance_mm=304.8, arc_time_s=0.11, enclosure_mm=(508, 508, 508),
    )
    assert any("PROVISIONAL" in n for n in result["notes"]), result["notes"]


def test_non_vcb_flags_unverified():
    """A non-VCB config carries an extra UNVERIFIED-path note."""
    result = incident_energy(
        v_oc=400, i_bf_kA=7.56, gap_mm=32, electrode="HCB",
        working_distance_mm=304.8, arc_time_s=0.11, enclosure_mm=(508, 508, 508),
    )
    assert any("UNVERIFIED" in n for n in result["notes"]), result["notes"]


def test_range_invalid_raises():
    """AF-3 (D-03): out-of-range / invalid input raises ArcFlashInputError."""
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
        v_oc=400, i_bf_kA=7.56, gap_mm=32, electrode="VCB",
        working_distance_mm=304.8, arc_time_s=0.11, enclosure_mm=(508, 508, 508),
    )
    a = json.dumps(incident_energy(**kw), sort_keys=True)
    b = json.dumps(incident_energy(**kw), sort_keys=True)
    assert a == b


def test_arc_flash_boundary_standalone():
    """The boundary helper returns a positive distance for the AF-1 case."""
    db = arc_flash_boundary(0.85, 304.8, "VCB", enclosure_mm=(508, 508, 508))
    assert abs(db - 490) <= 10


def test_report_blocks_use_allowed_types_only():
    """Every block type from to_report_blocks is in the 12-type schema allowlist."""
    result = incident_energy(
        v_oc=400, i_bf_kA=7.56, gap_mm=32, electrode="VCB",
        working_distance_mm=304.8, arc_time_s=0.11, enclosure_mm=(508, 508, 508),
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
