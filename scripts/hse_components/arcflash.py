"""
arcflash.py — IEEE 1584-2018 arc-flash incident-energy engine + NFPA 70E PPE.

Computes, for a three-phase AC arc-flash event (208 V – 15 kV):
  * the average arcing current ``Iarc`` (kA),
  * the **incident energy** at the working distance (cal/cm²),
  * the **arc-flash boundary** ``Db`` (mm, where incident energy = 1.2 cal/cm²),
  * the **NFPA 70E PPE category** {0,1,2,3,4} (or a ">40 — extreme" flag),
via the genuine IEEE 1584-2018 model: arcing current at the three reference
voltages (600 / 2700 / 14300 V) from the ``IE_coeffs`` polynomial → arcing-current
variation factor ``VarCf`` → ``Iarc_min`` → reference-voltage interpolation by Voc
(eq 16–18) → equivalent-enclosure-size box-size correction factor ``CF`` (eq 11/12/14)
→ incident energy ``E`` at each reference voltage from the ``incident_energy_*_coeffs``
model → interpolation by Voc → ``E`` in J/cm², converted to cal/cm² (÷4.184) at the
public boundary. The arc-flash boundary is solved from the same model where
``E = 1.2 cal/cm² = 5 J/cm²`` (eq 22/23).

This is the SUB-02 engine that UTIL-01 (arc-flash-assessment, Ph15) consumes.
The incident-energy number must be computed deterministically, never narrated —
a wrong arc-flash figure is indefensible before a regulator (D-01).

The embedded coefficient set is the genuine IEEE 1584-2018 standard, transcribed
from the owner-supplied licensed copy (Maple Flow worked implementation,
`hse-skills-screenshot/acrflashcalculation_iee1584-2018_final.pdf`). The engine
reproduces the standard's fully-worked HCB switchgear example
(13.8 kV, 18.241 kA, 152 mm gap, 914 mm working distance, 191 ms, 1244.6/1244.6/1143 mm
enclosure → E ≈ 8.89 cal/cm² [37.217 J/cm²], AFB ≈ 3037 mm, PPE category 3) and the
intermediate values it publishes (Iarc, VarCf, Iarc_min, CF, per-reference E and AFB).
The owner-confirmed coefficient gap (todo 260621-p11-arcflash-coefficients-licensed-verify)
is closed by this re-implementation.

Fail-loud edges (D-03): voltage outside 208 V – 15 kV, a non-positive gap /
current / arc time, or an unknown electrode configuration raises
``ArcFlashInputError`` — never a silent clamp that would yield a quietly-wrong
(and indefensible) number.

Units trap: the model computes internally in J/cm² and converts to cal/cm² only
at the public boundary (÷4.184). The HCB worked example is ≈37.217 J/cm² internal
= 8.89 cal/cm² output.
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
# arcing current + incident energy at each and interpolates between them by Voc).
REF_VOLTAGES_V = (600, 2700, 14300)

# Enclosure depth threshold separating "typical" (> 203.2 mm) from "shallow".
_SHALLOW_DEPTH_MM = 203.2
# Width/Height clamp used in the equivalent-enclosure-size derivation (eq 11/12).
_EES_DIM_CLAMP_MM = 1244.6

# ==============================================================================
# IEEE 1584-2018 coefficient block — verbatim from the licensed standard copy.
# (See module docstring for provenance.) The structure is the genuine
# 3-reference-voltage model, not a fitted surrogate.
# ==============================================================================

# --- Intermediate average arcing current: log10(Iarc) polynomial -------------
# Model (per electrode config × reference voltage):
#   Iarc = 10^(k1 + k2·log10(Ibf/kA) + k3·log10(G/mm))
#          · (k4·(Ibf)^6 + k5·(Ibf)^5 + … + k9·(Ibf) + k10)   [kA]
# The polynomial tail aligns its LAST coefficient to Ibf^0 (the constant); rows
# carry 7 coefficients (k4..k10, powers 6..0) except the HCB/HOA 2700/14300 V
# rows which carry 6 (powers 5..0) — handled generically by ``_poly_desc``.
IE_COEFFS: Dict[str, Dict[int, List[float]]] = {
    "VCB": {
        600:   [-0.04287, 1.035, -0.083, 0.0, 0.0, -4.783e-9, 1.962e-6, -0.000229, 0.003141, 1.092],
        2700:  [0.0065, 1.001, -0.024, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.9729],
        14300: [0.005795, 1.015, -0.011, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.9729],
    },
    "VCBB": {
        600:   [-0.017432, 0.98, -0.05, 0.0, 0.0, -5.767e-9, 2.524e-6, -0.00034, 0.01187, 1.013],
        2700:  [0.002823, 0.995, -0.0125, 0.0, -9.204e-11, 2.901e-9, -3.262e-6, 0.0001569, -0.004003, 0.9825],
        14300: [0.014827, 1.01, -0.01, 0.0, -9.204e-11, 2.901e-9, -3.262e-6, 0.0001569, -0.004003, 0.9825],
    },
    "HCB": {
        600:   [0.054922, 0.988, -0.11, 0.0, 0.0, -5.382e-9, 2.316e-6, -0.000302, 0.0091, 0.9725],
        # HCB 2700 V: 6-term polynomial tail (powers 5..0) — re-read from the PDF
        # page-3 image cell-by-cell (OQ4); the text layer renders one fewer term.
        2700:  [0.001011, 1.003, -0.0249, 0.0, 4.859e-10, -1.814e-7, -9.128e-6, -0.0007, 0.9881],
        14300: [0.008693, 0.999, -0.02, 0.0, -5.043e-11, 2.233e-8, -3.046e-6, 0.000116, -0.001145, 0.9839],
    },
    "VOA": {
        600:   [0.043785, 1.04, -0.18, 0.0, 0.0, -4.783e-9, 1.962e-6, -0.000229, 0.003141, 1.092],
        2700:  [-0.02395, 1.006, -0.0188, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.972],
        14300: [0.005371, 1.0102, -0.029, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.97],
    },
    "HOA": {
        600:   [0.111147, 1.008, -0.24, 0.0, 0.0, -3.895e-9, 1.641e-6, -0.000197, 0.002615, 1.1],
        # HOA 2700 V / 14300 V: 6-term polynomial tails (powers 5..0) — OQ4.
        2700:  [0.000435, 1.006, -0.038, 0.0, 7.859e-10, -1.914e-7, -9.128e-6, -0.0007, 0.9981],
        14300: [0.000904, 0.999, -0.02, 0.0, 7.859e-10, -1.914e-7, -9.128e-6, -0.0007, 0.9981],
    },
}

# --- Arcing-current variation factor VarCf (k1..k7), per config --------------
#   VarCf = k1·(Voc/kV)^6 + k2·(Voc/kV)^5 + … + k6·(Voc/kV) + k7
#   Iarc_min_<ref> = Iarc_<ref> · (1 − 0.5·VarCf)
VARC_COEFFS: Dict[str, List[float]] = {
    "VCB":  [0.0, -0.0000014269, 0.000083137, -0.0019382, 0.022366, -0.12645, 0.30226],
    "VCBB": [1.138e-6, -6.0287e-5, 0.0012758, -0.013778, 0.080217, -0.24066, 0.33524],
    "HCB":  [0.0, -3.097e-6, 0.00016405, -0.0033609, 0.033308, -0.16182, 0.34627],
    "VOA":  [9.5606e-7, -5.1543e-5, 0.0011161, -0.01242, 0.075125, -0.23584, 0.33696],
    "HOA":  [0.0, -3.1555e-6, 0.0001682, -0.0034607, 0.034124, -0.1599, 0.34629],
}

# --- Box-size correction factor (Table 7, b1/b2/b3), per config --------------
# CF = b1·(EES/mm)^2 + b2·(EES/mm) + b3   (typical, depth > 203.2 mm)
TYPICAL_ENCLOSURE_COEFFS: Dict[str, List[float]] = {
    "VCB":  [-0.000302, 0.03441, 0.4325],
    "VCBB": [-0.0002976, 0.032, 0.479],
    "HCB":  [-0.0001923, 0.01935, 0.6899],
}
SHALLOW_ENCLOSURE_COEFFS: Dict[str, List[float]] = {
    "VCB":  [0.002222, -0.02556, 0.6222],
    "VCBB": [-0.002778, 0.1194, -0.2778],
    "HCB":  [-0.0005556, 0.03722, 0.4778],
}
# Equivalent-enclosure-size derivation constants (eq 11/12), per config.
_EES_A: Dict[str, float] = {"VCB": 4.0, "VCBB": 10.0, "HCB": 10.0, "VOA": 1.0, "HOA": 1.0}
_EES_B: Dict[str, float] = {"VCB": 20.0, "VCBB": 24.0, "HCB": 22.0, "VOA": 1.0, "HOA": 1.0}

# --- Incident-energy coefficients (k1..k13), per config × reference voltage ---
# Model (J/cm²):
#   E = (12.552/50)·(T/ms) · 10^( k1 + k2·log10(G/mm)
#       + (k3·Iarc/kA) / (k4·Ibf^7 + k5·Ibf^6 + … + k9·Ibf^2 + k10·Ibf)
#       + k11·log10(Ibf/kA) + k12·log10(Dis/mm) + k13·log10(Iarc/kA) + log10(1/CF) )
# The denominator polynomial runs powers 7..1 (k4..k10, NO constant term) except
# the HCB/HOA 2700/14300 V rows which carry 6 coefficients (powers 6..1) — handled
# generically by ``_ie_denominator``.
INCIDENT_ENERGY_600_COEFFS: Dict[str, List[float]] = {
    "VCB":  [0.753364, 0.566, 1.752636, 0.0, 0.0, -4.783e-9, 1.962e-6, -0.000229, 0.003141, 1.092, 0.0, -1.598, 0.957],
    "VCBB": [3.068459, 0.26, -0.098107, 0.0, 0.0, -5.767e-9, 2.524e-6, -0.00034, 0.01187, 1.013, -0.06, -1.809, 1.19],
    "HCB":  [4.073745, 0.344, -0.370259, 0.0, 0.0, -5.382e-9, 2.316e-6, -0.000302, 0.0091, 0.9725, 0.0, -2.03, 1.036],
    "VOA":  [0.679294, 0.746, 1.222636, 0.0, 0.0, -4.783e-9, 1.962e-6, -0.000229, 0.003141, 1.092, 0.0, -1.598, 0.997],
    "HOA":  [3.470417, 0.465, -0.261863, 0.0, 0.0, -3.895e-9, 1.641e-6, -0.000197, 0.002615, 1.1, 0.0, -1.99, 1.04],
}
INCIDENT_ENERGY_2700_COEFFS: Dict[str, List[float]] = {
    "VCB":  [2.40021, 0.165, 0.354202, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.9729, 0.0, -1.569, 0.9778],
    "VCBB": [3.870592, 0.185, -0.736618, 0.0, -9.204e-11, 2.901e-9, -3.262e-6, 0.0001569, -0.004003, 0.9825, 0.0, -1.742, 1.09],
    # HCB 2700 V incident: 6-coefficient denominator tail (powers 6..1) — OQ4.
    "HCB":  [3.486391, 0.177, -0.193101, 0.0, 4.859e-10, -1.814e-7, -9.128e-6, 0.0007, 0.9881, 0.027, -1.723, 1.055],
    "VOA":  [3.880724, 0.105, -1.906033, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.9729, 0.0, -1.515, 1.115],
    "HOA":  [3.616266, 0.149, -0.761561, 0.0, 7.859e-10, -1.914e-7, -9.128e-6, -0.0007, 0.9981, 0.0, -1.639, 1.078],
}
INCIDENT_ENERGY_14300_COEFFS: Dict[str, List[float]] = {
    "VCB":  [3.825917, 0.11, -0.999749, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.9729, 0.0, -1.568, 0.99],
    "VCBB": [3.644309, 0.215, -0.585522, 0.0, -9.204e-11, 2.901e-9, -3.262e-6, 0.0001569, -0.004003, 0.9825, 0.0, -1.677, 1.06],
    "HCB":  [3.044516, 0.125, 0.245106, 0.0, -5.043e-11, 2.233e-8, -3.046e-6, 0.000116, -0.001145, 0.9839, 0.0, -1.655, 1.084],
    "VOA":  [3.405454, 0.12, -0.93245, -1.557e-12, 4.556e-10, -4.186e-8, 8.346e-7, 0.00005482, -0.003191, 0.9729, 0.0, -1.534, 0.979],
    "HOA":  [2.04049, 0.177, 1.005092, 0.0, 7.859e-10, -1.914e-7, -9.128e-6, -0.0007, 0.9981, -0.05, -1.633, 1.151],
}
_INCIDENT_ENERGY_COEFFS: Dict[int, Dict[str, List[float]]] = {
    600: INCIDENT_ENERGY_600_COEFFS,
    2700: INCIDENT_ENERGY_2700_COEFFS,
    14300: INCIDENT_ENERGY_14300_COEFFS,
}

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
    if not isinstance(electrode, str) or electrode not in IE_COEFFS:
        raise ArcFlashInputError(
            f"electrode {electrode!r} must be one of {ELECTRODE_CONFIGS}"
        )


# --- IEEE 1584-2018 model internals (all in J/cm² until the public boundary) -
def _arc_poly(coeffs: List[float], i_bf_kA: float) -> float:
    """Arcing-current polynomial tail: last coefficient is the Ibf^0 constant.

    Handles the variable-length rows (7-term powers 6..0, or 6-term powers 5..0).
    """
    n = len(coeffs)
    return sum(coeffs[i] * (i_bf_kA ** (n - 1 - i)) for i in range(n))


def _arcing_current_kA(i_bf_kA: float, gap_mm: float, coeffs: List[float]) -> float:
    """Average arcing current at one reference voltage (IEEE 1584-2018)."""
    k1, k2, k3 = coeffs[0], coeffs[1], coeffs[2]
    base = 10 ** (k1 + k2 * math.log10(i_bf_kA) + k3 * math.log10(gap_mm))
    return base * _arc_poly(coeffs[3:], i_bf_kA)


def _varcf(v_oc_kV: float, coeffs: List[float]) -> float:
    """Arcing-current variation factor VarCf (degree-6 polynomial in Voc/kV)."""
    return sum(coeffs[i] * (v_oc_kV ** (6 - i)) for i in range(7))


def _correction_factor(
    v_oc: float,
    electrode: str,
    enclosure_mm: Optional[Sequence[float]],
) -> float:
    """Box-size correction factor CF (eq 11/12/14). Open-air → 1.0."""
    if electrode in ("VOA", "HOA") or enclosure_mm is None:
        return 1.0
    if len(enclosure_mm) != 3:
        raise ArcFlashInputError(
            "enclosure_mm must be a (height, width, depth) triple in mm"
        )
    height, width, depth = (float(x) for x in enclosure_mm)
    if height <= 0 or width <= 0 or depth <= 0:
        raise ArcFlashInputError("enclosure_mm dimensions must be > 0")

    a = _EES_A[electrode]
    b = _EES_B[electrode]
    v_oc_kV = v_oc / 1000.0

    def _equiv_dim(dim_mm: float) -> float:
        clamped = min(dim_mm, _EES_DIM_CLAMP_MM)
        return (660.4 + (clamped - 660.4) * ((v_oc_kV + a) / b)) * (1.0 / 25.4)

    ees = (_equiv_dim(height) + _equiv_dim(width)) / 2.0
    # Depth only switches the typical/shallow coefficient set below 600 V.
    shallow = depth <= _SHALLOW_DEPTH_MM and v_oc < 600
    coeffs = (SHALLOW_ENCLOSURE_COEFFS if shallow else TYPICAL_ENCLOSURE_COEFFS)[electrode]
    return coeffs[0] * ees ** 2 + coeffs[1] * ees + coeffs[2]


def _ie_denominator(coeffs: List[float], i_bf_kA: float) -> float:
    """Incident-energy denominator polynomial (k4..k10), powers run …→1 (no constant).

    7 coefficients → powers 7..1; 6 coefficients → powers 6..1 (HCB/HOA high-V rows).
    """
    tail = coeffs[3:-3]
    n = len(tail)
    return sum(tail[i] * (i_bf_kA ** (n - i)) for i in range(n))


def _incident_energy_jcm2(
    coeffs: List[float],
    gap_mm: float,
    i_bf_kA: float,
    i_arc_kA: float,
    working_distance_mm: float,
    arc_time_ms: float,
    cf: float,
) -> float:
    """Incident energy at one reference voltage (J/cm²)."""
    k1, k2, k3 = coeffs[0], coeffs[1], coeffs[2]
    k11, k12, k13 = coeffs[-3], coeffs[-2], coeffs[-1]
    exponent = (
        k1
        + k2 * math.log10(gap_mm)
        + (k3 * i_arc_kA) / _ie_denominator(coeffs, i_bf_kA)
        + k11 * math.log10(i_bf_kA)
        + k12 * math.log10(working_distance_mm)
        + k13 * math.log10(i_arc_kA)
        + math.log10(1.0 / cf)
    )
    return (12.552 / 50.0) * arc_time_ms * (10 ** exponent)


def _afb_mm(
    coeffs: List[float],
    gap_mm: float,
    i_bf_kA: float,
    i_arc_kA: float,
    i_arc_min_kA: float,
    arc_time_ms: float,
    cf: float,
) -> float:
    """Arc-flash boundary at one reference voltage (mm), solved where E = 1.2 cal/cm²."""
    k1, k2, k3 = coeffs[0], coeffs[1], coeffs[2]
    k11, k12, k13 = coeffs[-3], coeffs[-2], coeffs[-1]
    inner = (
        k1
        + k2 * math.log10(gap_mm)
        + (k3 * i_arc_kA) / _ie_denominator(coeffs, i_bf_kA)
        + k11 * math.log10(i_bf_kA)
        + k13 * math.log10(i_arc_min_kA)
        + math.log10(1.0 / cf)
        - math.log10(20.0 / arc_time_ms)
    )
    return 10 ** ((1.0 / (-k12)) * inner)


def _interpolate_by_voc(values: Dict[int, float], v_oc_kV: float) -> float:
    """IEEE 1584-2018 reference-voltage interpolation (eq 16–18)."""
    x600, x2700, x14300 = values[600], values[2700], values[14300]
    term1 = (x2700 - x600) / (2.7 - 0.6) * (v_oc_kV - 2.7) + x2700
    term2 = (x14300 - x2700) / (14.3 - 2.7) * (v_oc_kV - 14.3) + x14300
    if v_oc_kV > 2.7:
        return term2
    term3 = (
        term1 * (2.7 - v_oc_kV) / (2.7 - 0.6)
        + term2 * (v_oc_kV - 0.6) / (2.7 - 0.6)
    )
    return term3


def _solve(
    v_oc: float,
    i_bf_kA: float,
    gap_mm: float,
    electrode: str,
    working_distance_mm: float,
    arc_time_s: float,
    enclosure_mm: Optional[Sequence[float]],
) -> Dict[str, Any]:
    """Run the full IEEE 1584-2018 model; return intermediate + final values (J/cm²)."""
    v_oc_kV = v_oc / 1000.0
    arc_time_ms = arc_time_s * 1000.0

    # Arcing current + variation factor at each reference voltage.
    var_coeffs = VARC_COEFFS[electrode]
    var_cf = _varcf(v_oc_kV, var_coeffs)
    i_arc: Dict[int, float] = {}
    i_arc_min: Dict[int, float] = {}
    for ref in REF_VOLTAGES_V:
        ia = _arcing_current_kA(i_bf_kA, gap_mm, IE_COEFFS[electrode][ref])
        i_arc[ref] = ia
        i_arc_min[ref] = ia * (1.0 - 0.5 * var_cf)

    cf = _correction_factor(v_oc, electrode, enclosure_mm)

    # Incident energy + boundary at each reference voltage, then interpolate.
    e_ref: Dict[int, float] = {}
    afb_ref: Dict[int, float] = {}
    for ref in REF_VOLTAGES_V:
        ie_coeffs = _INCIDENT_ENERGY_COEFFS[ref][electrode]
        e_ref[ref] = _incident_energy_jcm2(
            ie_coeffs, gap_mm, i_bf_kA, i_arc[ref],
            working_distance_mm, arc_time_ms, cf,
        )
        afb_ref[ref] = _afb_mm(
            ie_coeffs, gap_mm, i_bf_kA, i_arc[ref], i_arc_min[ref],
            arc_time_ms, cf,
        )

    e_j_cm2 = _interpolate_by_voc(e_ref, v_oc_kV)
    boundary_mm = _interpolate_by_voc(afb_ref, v_oc_kV)
    i_arc_final = _interpolate_by_voc(i_arc, v_oc_kV)

    return {
        "incident_energy_j_cm2": e_j_cm2,
        "boundary_mm": boundary_mm,
        "arcing_current_kA": i_arc_final,
        "correction_factor": cf,
        "var_cf": var_cf,
    }


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
    """Arc-flash boundary Db (mm) — back-compatible helper.

    Retained for API compatibility (the engine computes the boundary directly from
    the IEEE 1584-2018 model in ``incident_energy``; this helper approximates Db
    from a known incident energy at a working distance via the inverse-square-of-
    distance relationship the standard's model exhibits, using the bare-skin
    boundary energy Eb = 1.2 cal/cm²). Prefer ``incident_energy(...)['arc_flash_boundary_mm']``.
    """
    if electrode not in IE_COEFFS:
        raise ArcFlashInputError(
            f"electrode {electrode!r} must be one of {ELECTRODE_CONFIGS}"
        )
    e = _as_number(incident_energy_cal_cm2, "incident_energy_cal_cm2")
    d = _as_number(working_distance_mm, "working_distance_mm")
    if e <= 0 or d <= 0:
        raise ArcFlashInputError("incident energy and working distance must be > 0")
    # IEEE 1584-2018 incident energy scales with distance^k12 (k12 ≈ -1.6 to -2.0);
    # using the dominant near-quadratic falloff to project the boundary distance.
    return round(d * math.sqrt(e / EB_CAL_CM2), 1)


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
    incident energy in cal/cm² and the boundary in mm (the genuine IEEE 1584-2018
    model computes internally in J/cm² and converts to cal/cm² at this boundary).

    Raises ``ArcFlashInputError`` on any out-of-range / invalid input (D-03).
    """
    _check_inputs(v_oc, i_bf_kA, gap_mm, electrode,
                  working_distance_mm, arc_time_s)
    v_oc = float(v_oc)
    i_bf_kA = float(i_bf_kA)
    gap_mm = float(gap_mm)
    working_distance_mm = float(working_distance_mm)
    arc_time_s = float(arc_time_s)

    solved = _solve(
        v_oc, i_bf_kA, gap_mm, electrode,
        working_distance_mm, arc_time_s, enclosure_mm,
    )

    # Convert J/cm² → cal/cm² AT THE PUBLIC BOUNDARY (÷4.184).
    e_cal = round(solved["incident_energy_j_cm2"] / J_PER_CAL, _ROUND_DP)
    boundary = round(solved["boundary_mm"], 1)
    iarc = round(solved["arcing_current_kA"], _ROUND_DP)
    cat = ppe_category(e_cal)

    notes: List[str] = []
    if cat == ">40 — extreme":
        notes.append(
            "Incident energy exceeds 40 cal/cm² — no table PPE; eliminate the "
            "hazard via engineering controls (de-energize / remote operation)."
        )

    return {
        "arcing_current_kA": iarc,
        "incident_energy_cal_cm2": e_cal,
        "incident_energy_j_cm2": round(solved["incident_energy_j_cm2"], 3),
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
            "arcing_current_kA": iarc,
            "reference_time_s": T_REF_S,
            "eb_cal_cm2": EB_CAL_CM2,
            "correction_factor": round(solved["correction_factor"], 4),
            "var_cf": round(solved["var_cf"], 4),
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
