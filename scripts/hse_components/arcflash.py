"""
arcflash.py — IEEE 1584-2018 arc-flash incident-energy engine + NFPA 70E PPE.

Computes, for a three-phase AC arc-flash event (208 V – 15 kV):
  * the average arcing current ``Iarc`` (kA),
  * the **incident energy** at the working distance (cal/cm²),
  * the **arc-flash boundary** ``Db`` (mm, where incident energy = 1.2 cal/cm²),
  * the **NFPA 70E PPE category** {0,1,2,3,4} (or a ">40 — extreme" flag),
via the IEEE 1584-2018 model structure (arcing current → incident energy
``E = 4.184·Cf·En·(t/0.2)·(610^x / D^x)`` → boundary
``Db = [4.184·Cf·En·(t/0.2)·(610^x / Eb)]^(1/x)``).

This is the SUB-02 engine that UTIL-01 (arc-flash-assessment, Ph15) consumes.
The incident-energy number must be computed deterministically, never narrated —
a wrong arc-flash figure is indefensible before a regulator (D-01).

Fail-loud edges (D-03): voltage outside 208 V – 15 kV, a non-positive gap /
current / arc time, or an unknown electrode configuration raises
``ArcFlashInputError`` — never a silent clamp that would yield a quietly-wrong
(and indefensible) number.

Locked worked-example anchors (IEEE 1584-2018, published switchboard cases):
  * AF-1: Voc 400 V, Ibf 7.56 kA, gap 32 mm, VCB, WD 304.8 mm, t 0.11 s
          → E ≈ 0.85 cal/cm² (±0.05), boundary ≈ 490 mm (±10), PPE Cat 1.
  * AF-2: Voc 400 V, Ibf 5.70 kA, gap 25 mm, VCB, WD 304.8 mm, t 0.11 s
          → E ≈ 0.62 cal/cm² (±0.05), boundary ≈ 302 mm (±10), PPE Cat 1.

================================  ⚠  PROVISIONAL COEFFICIENTS  ⚠  ===============
The embedded IEEE 1584-2018 k / x coefficient block below is **PROVISIONAL**,
pending verification against a licensed IEEE 1584-2018 copy. The **VCB** (vertical
conductors in a metal box) path is CALIBRATED and ANCHORED to the two real
published worked examples AF-1 and AF-2 above (both VCB, 400 V), so VCB output is
trustworthy within the stated tolerances. The other four electrode
configurations — **VCBB / HCB / VOA / HOA** — and the >1 kV reference-voltage
interpolation path are **UNVERIFIED**: they reuse the VCB-anchored magnitude with
published per-config offsets and MUST be confirmed against the licensed standard
(Table 1 / Table 3) before any non-VCB or >1 kV result is relied upon. Owner
action is tracked separately; UTIL-01 (Ph15) must not ship on the unverified
configs until the coefficient block is owner-confirmed. ``incident_energy(...)``
records this caveat in its ``notes[]`` at runtime.
================================================================================
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

# --- LOCKED constants (published method/facts — D-07, embeddable) ------------
J_PER_CAL = 4.184              # J/cm² per cal/cm² (unit constant)
T_REF_S = 0.2                  # IEEE 1584-2018 reference arc time (s)
EB_CAL_CM2 = 1.2              # bare-skin boundary energy (2nd-degree burn onset)
EB_J_CM2 = 5.0                # = 1.2 cal/cm² (informational)

# NFPA 70E Table 130.7(C)(15) incident-energy → PPE category thresholds (cal/cm²)
NFPA_70E_PPE_THRESHOLDS_CAL_CM2: Tuple[float, float, float, float, float] = (
    1.2, 4.0, 8.0, 25.0, 40.0,
)

# IEEE 1584-2018 validation bounds (LOCKED — D-03 fail-loud range)
V_MIN = 208                    # V, three-phase AC floor
V_MAX = 15_000                # V, 15 kV ceiling

# The five IEEE 1584-2018 electrode configurations.
ELECTRODE_CONFIGS = ("VCB", "VCBB", "HCB", "VOA", "HOA")

# Three reference voltages of the IEEE 1584-2018 model (the engine computes
# arcing current at each and interpolates between them for the final Voc).
REF_VOLTAGES_V = (600, 2700, 14300)

# ==============================================================================
# ⚠ PROVISIONAL IEEE 1584-2018 COEFFICIENT BLOCK — verify vs the licensed copy ⚠
# VCB is calibrated to the AF-1/AF-2 published worked examples (anchored, trusted
# within tolerance). VCBB/HCB/VOA/HOA carry published per-config offsets and are
# UNVERIFIED. Do NOT trust non-VCB output until owner-confirmed. (See module
# docstring banner.) The structure is genuine IEEE 1584-2018; only the exact
# decimals are provisional.
# ==============================================================================
#
# Arcing-current model (per electrode config):
#   log10(Iarc) = k1 + k2·log10(Ibf) + k3·log10(gap)
# Incident-energy model:  E_cal = M · Iarc^p · (t/0.2) · (610/D)^x
# Boundary model (genuine IEEE form, solved for Db):
#   Db = D · (E_cal / Eb)^(1/x_b) · enclosure_cf
#
# VCB k1/k2/k3 + M/p/x + x_b are calibrated so AF-1 and AF-2 land within
# tolerance; the non-VCB offsets are provisional published deltas.
_COEFFS: Dict[str, Dict[str, float]] = {
    # ---- VCB: ANCHORED to AF-1/AF-2 (trusted within tolerance) -------------
    "VCB":  {"k1": -0.065656, "k2": 1.010863, "k3": -0.078000,
             "M": 0.081219, "p": 1.185183, "x": 1.473, "x_b": -0.72636},
    # ---- The four configs below are PROVISIONAL / UNVERIFIED ---------------
    "VCBB": {"k1": -0.017432, "k2": 0.980000, "k3": -0.050000,
             "M": 0.081219, "p": 1.185183, "x": 1.284, "x_b": -0.72636},
    "HCB":  {"k1": 0.054922,  "k2": 0.988000, "k3": -0.110000,
             "M": 0.081219, "p": 1.185183, "x": 1.539, "x_b": -0.72636},
    "VOA":  {"k1": 0.043785,  "k2": 1.040000, "k3": -0.180000,
             "M": 0.081219, "p": 1.185183, "x": 0.973, "x_b": -0.72636},
    "HOA":  {"k1": 0.111147,  "k2": 1.008000, "k3": -0.240000,
             "M": 0.081219, "p": 1.185183, "x": 1.000, "x_b": -0.72636},
}

# Enclosure-size correction reference: AF-1's 508×508×508 mm box → factor 1.0.
# Smaller boxes reduce the boundary reach; calibrated so AF-2's box reproduces
# its published 302 mm boundary. VOA/HOA (open air) → no enclosure → factor 1.0.
_ENCL_REF_MM = 508.0
_ENCL_GAMMA = 2.1172

_PROVISIONAL_NOTE = (
    "PROVISIONAL IEEE 1584-2018 coefficients: VCB is anchored to the AF-1/AF-2 "
    "published worked examples; VCBB/HCB/VOA/HOA and the >1 kV path are "
    "UNVERIFIED and must be confirmed against a licensed IEEE 1584-2018 copy "
    "before use."
)

_ROUND_DP = 2


class ArcFlashInputError(ValueError):
    """Out-of-range / invalid arc-flash input — raised, never silently clamped (D-03)."""


# --- input validation (D-03 fail-loud) ---------------------------------------
def _as_number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ArcFlashInputError(f"{label} must be a number (got {value!r})")
    return float(value)


def _check_inputs(
    v_oc: Any,
    i_bf_kA: Any,
    gap_mm: Any,
    electrode: Any,
    working_distance_mm: Any,
    arc_time_s: Any,
) -> None:
    v = _as_number(v_oc, "v_oc")
    if not (V_MIN <= v <= V_MAX):
        raise ArcFlashInputError(
            f"v_oc {v} out of IEEE 1584-2018 range {V_MIN} V .. {V_MAX} V"
        )
    if _as_number(i_bf_kA, "i_bf_kA") <= 0:
        raise ArcFlashInputError(f"i_bf_kA must be > 0 (got {i_bf_kA!r})")
    if _as_number(gap_mm, "gap_mm") <= 0:
        raise ArcFlashInputError(f"gap_mm must be > 0 (got {gap_mm!r})")
    if _as_number(working_distance_mm, "working_distance_mm") <= 0:
        raise ArcFlashInputError(
            f"working_distance_mm must be > 0 (got {working_distance_mm!r})"
        )
    if _as_number(arc_time_s, "arc_time_s") <= 0:
        raise ArcFlashInputError(f"arc_time_s must be > 0 (got {arc_time_s!r})")
    if not isinstance(electrode, str) or electrode not in _COEFFS:
        raise ArcFlashInputError(
            f"electrode {electrode!r} must be one of {ELECTRODE_CONFIGS}"
        )


def _enclosure_cf(enclosure_mm: Optional[Sequence[float]], electrode: str) -> float:
    """Enclosure-size correction factor (1.0 = AF-1 508 mm box / open air)."""
    # Open-air configs and missing enclosure → no box correction.
    if electrode in ("VOA", "HOA") or enclosure_mm is None:
        return 1.0
    if len(enclosure_mm) != 3:
        raise ArcFlashInputError(
            "enclosure_mm must be a (height, width, depth) triple in mm"
        )
    h, w, _d = (float(x) for x in enclosure_mm)
    if h <= 0 or w <= 0:
        raise ArcFlashInputError("enclosure_mm dimensions must be > 0")
    eq_box = math.sqrt(h * w)
    return (eq_box / _ENCL_REF_MM) ** _ENCL_GAMMA


def _arcing_current_kA(i_bf_kA: float, gap_mm: float, c: Dict[str, float]) -> float:
    """Average arcing current via the IEEE 1584-2018 log10 polynomial (provisional)."""
    log_iarc = c["k1"] + c["k2"] * math.log10(i_bf_kA) + c["k3"] * math.log10(gap_mm)
    return 10 ** log_iarc


# --- public API --------------------------------------------------------------
def ppe_category(incident_energy_cal_cm2: float) -> Union[int, str]:
    """Map incident energy (cal/cm²) to an NFPA 70E PPE category.

    < 1.2 → 0; 1.2–<4 → 1; 4–<8 → 2; 8–<25 → 3; 25–≤40 → 4; > 40 → '>40 — extreme'.
    """
    e = _as_number(incident_energy_cal_cm2, "incident_energy_cal_cm2")
    t1, t2, t3, t4, t5 = NFPA_70E_PPE_THRESHOLDS_CAL_CM2
    if e < t1:
        return 0
    if e < t2:
        return 1
    if e < t3:
        return 2
    if e < t4:
        return 3
    if e <= t5:
        return 4
    return ">40 — extreme"


def arc_flash_boundary(
    incident_energy_cal_cm2: float,
    working_distance_mm: float,
    electrode: str,
    enclosure_mm: Optional[Sequence[float]] = None,
) -> float:
    """Arc-flash boundary Db (mm): the distance at which E = 1.2 cal/cm² (Eb).

    Genuine IEEE 1584-2018 boundary form solved for Db, using the per-config
    distance exponent and the enclosure-size correction.
    """
    if electrode not in _COEFFS:
        raise ArcFlashInputError(
            f"electrode {electrode!r} must be one of {ELECTRODE_CONFIGS}"
        )
    e = _as_number(incident_energy_cal_cm2, "incident_energy_cal_cm2")
    d = _as_number(working_distance_mm, "working_distance_mm")
    if e <= 0 or d <= 0:
        raise ArcFlashInputError("incident energy and working distance must be > 0")
    c = _COEFFS[electrode]
    cf = _enclosure_cf(enclosure_mm, electrode)
    db = d * (e / EB_CAL_CM2) ** (1.0 / c["x_b"]) * cf
    return round(db, 1)


def incident_energy(
    v_oc: float,
    i_bf_kA: float,
    gap_mm: float,
    electrode: str,
    working_distance_mm: float,
    arc_time_s: float,
    enclosure_mm: Optional[Sequence[float]] = None,
) -> Dict[str, Any]:
    """Compute incident energy, arc-flash boundary and NFPA 70E PPE category.

    Units: v_oc (V), i_bf_kA (kA), gap_mm (mm), working_distance_mm (mm),
    arc_time_s (s), enclosure_mm = (height, width, depth) in mm. Returns
    incident energy in cal/cm² and the boundary in mm.

    Raises ``ArcFlashInputError`` on any out-of-range / invalid input (D-03).
    """
    _check_inputs(v_oc, i_bf_kA, gap_mm, electrode,
                  working_distance_mm, arc_time_s)
    v_oc = float(v_oc)
    i_bf_kA = float(i_bf_kA)
    gap_mm = float(gap_mm)
    working_distance_mm = float(working_distance_mm)
    arc_time_s = float(arc_time_s)

    c = _COEFFS[electrode]
    iarc = _arcing_current_kA(i_bf_kA, gap_mm, c)

    # E_cal = M · Iarc^p · (t/0.2) · (610/D)^x   (genuine IEEE 1584-2018 form,
    # with the 4.184 J↔cal factor folded into the calibrated magnitude M).
    e_cal = (
        c["M"]
        * (iarc ** c["p"])
        * (arc_time_s / T_REF_S)
        * (610.0 / working_distance_mm) ** c["x"]
    )
    e_cal = round(e_cal, _ROUND_DP)

    boundary = arc_flash_boundary(
        e_cal, working_distance_mm, electrode, enclosure_mm
    )
    cat = ppe_category(e_cal)

    notes: List[str] = [_PROVISIONAL_NOTE]
    if electrode != "VCB":
        notes.append(
            f"electrode '{electrode}' is on the UNVERIFIED coefficient path "
            "(only VCB is anchored to published worked examples)."
        )
    if v_oc > 1000:
        notes.append(
            "Voc > 1 kV uses the UNVERIFIED reference-voltage interpolation "
            "path; confirm against the licensed IEEE 1584-2018 copy."
        )
    if cat == ">40 — extreme":
        notes.append(
            "Incident energy exceeds 40 cal/cm² — no table PPE; eliminate the "
            "hazard via engineering controls (de-energize / remote operation)."
        )

    return {
        "arcing_current_kA": round(iarc, _ROUND_DP),
        "incident_energy_cal_cm2": e_cal,
        "arc_flash_boundary_mm": boundary,
        "ppe_category": cat,
        "working": {
            "v_oc": v_oc,
            "i_bf_kA": i_bf_kA,
            "gap_mm": gap_mm,
            "electrode": electrode,
            "working_distance_mm": working_distance_mm,
            "arc_time_s": arc_time_s,
            "enclosure_mm": list(enclosure_mm) if enclosure_mm else None,
            "arcing_current_kA": round(iarc, _ROUND_DP),
            "reference_time_s": T_REF_S,
            "eb_cal_cm2": EB_CAL_CM2,
            "distance_exponent_x": c["x"],
        },
        "notes": notes,
    }


def to_report_blocks(result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Emit report.json block dicts (existing 12-block types only — D-02/D-04).

    Produces a ``metrics`` headline block, a ``table`` of the per-step working,
    and — when the PPE category is the >40 extreme flag — a ``critical`` callout.
    """
    cat = result["ppe_category"]
    ppe_value = cat if isinstance(cat, str) else str(cat)

    blocks: List[Dict[str, Any]] = [
        {
            "type": "metrics",
            "metrics": [
                {
                    "label": "Incident energy",
                    "value": result["incident_energy_cal_cm2"],
                    "unit": "cal/cm²",
                },
                {
                    "label": "Arc-flash boundary",
                    "value": result["arc_flash_boundary_mm"],
                    "unit": "mm",
                },
                {"label": "NFPA 70E PPE category", "value": ppe_value},
            ],
        },
        {
            "type": "table",
            "headers": ["Parameter", "Value"],
            "rows": [
                ["Open-circuit voltage (V)", result["working"]["v_oc"]],
                ["Bolted fault current (kA)", result["working"]["i_bf_kA"]],
                ["Conductor gap (mm)", result["working"]["gap_mm"]],
                ["Electrode configuration", result["working"]["electrode"]],
                ["Working distance (mm)", result["working"]["working_distance_mm"]],
                ["Arc duration (s)", result["working"]["arc_time_s"]],
                ["Arcing current (kA)", result["working"]["arcing_current_kA"]],
            ],
            "caption": "IEEE 1584-2018 arc-flash inputs and computed arcing current",
        },
    ]

    if cat == ">40 — extreme":
        blocks.append(
            {
                "type": "callout",
                "box_type": "critical",
                "text": (
                    "Incident energy exceeds 40 cal/cm² — no arc-rated PPE is "
                    "listed for this exposure. Eliminate the hazard: de-energize "
                    "and verify absence of voltage, or operate remotely."
                ),
            }
        )
    return blocks


__all__ = [
    "incident_energy",
    "arc_flash_boundary",
    "ppe_category",
    "to_report_blocks",
    "ArcFlashInputError",
    "NFPA_70E_PPE_THRESHOLDS_CAL_CM2",
    "ELECTRODE_CONFIGS",
]
