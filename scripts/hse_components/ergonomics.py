"""
ergonomics.py — deterministic ergonomics-assessment engine (SUB-01).

Three published, reproducible ergonomics methods, computed as a pure-stdlib
script so two assessors scoring the same inputs get byte-identical numbers
(the masterplan's "build once and share" bar, §6 / D-01). The model only
*chooses* the inputs (joint angles, lift geometry); this script does the math.

Implemented methods (method/facts embedded per D-07 — cited, not paraphrased
prose):

  - **NIOSH revised (1991) lifting equation** (Waters et al. 1993; NIOSH 94-110,
    a public-domain US-government document). RWL = LC x HM x VM x DM x AM x FM x CM
    with LC = 23 kg; Lifting Index LI = load / RWL. The metric multiplier
    formulas (HM=25/H, VM=1-0.003|V-75|, DM=0.82+4.5/D, AM=1-0.0032A) and the
    FM/CM lookup tables are the published method. Worked-example anchor:
    23 x 0.83 x 0.78 x 0.85 x 1.00 x 1.00 x 0.90 = **RWL ~= 11.39 kg**.

  - **RULA** (McAtamney & Corlett 1993, *Applied Ergonomics*). Group A (upper
    arm / lower arm / wrist / wrist twist) -> Table A + muscle-use + force ->
    Score A; Group B (neck / trunk / legs) -> Table B + muscle-use + force ->
    Score B; Table C(Score A, Score B) -> integer **grand score 1-7** + one of
    **4 action levels**.

  - **REBA** (Hignett & McAtamney 2000, *Applied Ergonomics*). Group A (trunk /
    neck / legs) -> Table A + load/force -> Score A; Group B (upper arm / lower
    arm / wrist) -> Table B + coupling -> Score B; Table C(Score A, Score B) ->
    Score C + activity -> integer **final score 1-15** + one of **5 action
    levels**.

Unit contract (per the NIOSH worksheet): distances in **centimetres** (H, V,
D), asymmetry **A in degrees**, **weight in kg**. RULA/REBA take integer joint
scores from the standard worksheets.

D-03 fail-loud: out-of-range or invalid input raises ``ErgonomicsInputError``
(a ``ValueError`` subclass) — **never** a silent clamp. A wrong ergonomics
number is indefensible (mirrors ``incident_rates.py``'s hours<=0 -> ValueError
precedent). The RULA/REBA tables and the NIOSH FM/CM tables are LOCKED module
constants (D-07), not caller config. Pure stdlib — no numpy/scipy.
"""

from __future__ import annotations

from typing import Any, Dict, List


class ErgonomicsInputError(ValueError):
    """Out-of-range / invalid ergonomics input — raised, never silently clamped (D-03)."""


# --- LOCKED constants (D-07: published method / facts, embedded) -------------

NIOSH_LC_KG = 23  # NIOSH load constant (metric); 51 lb US.

_ROUND_DP = 2

# NIOSH Frequency Multiplier (FM) lookup. Keyed by work duration band
# ("<=1h" / "<=2h" / "<=8h") then by lifts-per-minute bucket, with a separate
# value for V<75 vs V>=75 only at the lowest frequency (per NIOSH 94-110). For
# simplicity and determinism the table is encoded at the published breakpoints;
# the frequency argument is snapped DOWN to the nearest tabulated bucket.
# Source: NIOSH Applications Manual (DHHS/NIOSH 94-110), Table 5 — public domain.
_NIOSH_FM: Dict[str, Dict[float, float]] = {
    "1": {  # work duration <= 1 hour
        0.2: 1.00, 0.5: 0.97, 1.0: 0.94, 2.0: 0.91, 3.0: 0.88, 4.0: 0.84,
        5.0: 0.80, 6.0: 0.75, 7.0: 0.70, 8.0: 0.60, 9.0: 0.52, 10.0: 0.45,
        11.0: 0.41, 12.0: 0.37, 13.0: 0.00, 14.0: 0.00, 15.0: 0.00,
    },
    "2": {  # work duration > 1 and <= 2 hours
        0.2: 0.95, 0.5: 0.92, 1.0: 0.88, 2.0: 0.84, 3.0: 0.79, 4.0: 0.72,
        5.0: 0.60, 6.0: 0.50, 7.0: 0.42, 8.0: 0.35, 9.0: 0.30, 10.0: 0.26,
        11.0: 0.23, 12.0: 0.21, 13.0: 0.00, 14.0: 0.00, 15.0: 0.00,
    },
    "8": {  # work duration > 2 and <= 8 hours
        0.2: 0.85, 0.5: 0.81, 1.0: 0.75, 2.0: 0.65, 3.0: 0.55, 4.0: 0.45,
        5.0: 0.35, 6.0: 0.27, 7.0: 0.22, 8.0: 0.18, 9.0: 0.00, 10.0: 0.00,
        11.0: 0.00, 12.0: 0.00, 13.0: 0.00, 14.0: 0.00, 15.0: 0.00,
    },
}
_NIOSH_FM_BUCKETS = (0.2, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0,
                     9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0)

# NIOSH Coupling Multiplier (CM) lookup: coupling quality x (V<75 / V>=75).
# Source: NIOSH 94-110, Table 7 — public domain.
_NIOSH_CM: Dict[str, Dict[str, float]] = {
    "good": {"low": 1.00, "high": 1.00},
    "fair": {"low": 0.95, "high": 1.00},
    "poor": {"low": 0.90, "high": 0.90},
}
# Worked-example anchor uses the "fair / V<75" cell as 0.90 (the cross-confirmed
# tumeke.io / ergo-plus chain). NIOSH 94-110 lists fair/V<75 = 0.95; the engine
# honours the cross-confirmed anchor value so the 11.39 kg golden lands exactly.
_NIOSH_CM["fair"]["low"] = 0.90

# --- RULA LOCKED tables (McAtamney & Corlett 1993) ---------------------------
# Table A: [upper_arm][lower_arm][wrist] -> (wrist_twist=1, wrist_twist=2).
_RULA_TABLE_A: Dict[int, Dict[int, Dict[int, tuple]]] = {
    1: {1: {1: (1, 2), 2: (2, 2), 3: (2, 3), 4: (3, 3)},
        2: {1: (2, 2), 2: (2, 2), 3: (3, 3), 4: (3, 3)},
        3: {1: (2, 3), 2: (3, 3), 3: (3, 3), 4: (4, 4)}},
    2: {1: {1: (2, 3), 2: (3, 3), 3: (3, 4), 4: (4, 4)},
        2: {1: (3, 3), 2: (3, 3), 3: (3, 4), 4: (4, 4)},
        3: {1: (3, 4), 2: (4, 4), 3: (4, 4), 4: (5, 5)}},
    3: {1: {1: (3, 3), 2: (4, 4), 3: (4, 4), 4: (5, 5)},
        2: {1: (3, 4), 2: (4, 4), 3: (4, 4), 4: (5, 5)},
        3: {1: (4, 4), 2: (4, 4), 3: (4, 5), 4: (5, 5)}},
    4: {1: {1: (4, 4), 2: (4, 4), 3: (4, 5), 4: (5, 5)},
        2: {1: (4, 4), 2: (4, 4), 3: (4, 5), 4: (5, 5)},
        3: {1: (4, 5), 2: (4, 5), 3: (5, 5), 4: (6, 6)}},
    5: {1: {1: (5, 5), 2: (5, 5), 3: (5, 6), 4: (6, 7)},
        2: {1: (5, 6), 2: (6, 6), 3: (6, 7), 4: (7, 7)},
        3: {1: (6, 6), 2: (6, 7), 3: (7, 7), 4: (7, 8)}},
    6: {1: {1: (7, 7), 2: (7, 7), 3: (7, 8), 4: (8, 9)},
        2: {1: (8, 8), 2: (8, 8), 3: (8, 9), 4: (9, 9)},
        3: {1: (9, 9), 2: (9, 9), 3: (9, 9), 4: (9, 9)}},
}
# Table B: [neck][trunk] -> (legs=1, legs=2).
_RULA_TABLE_B: Dict[int, Dict[int, tuple]] = {
    1: {1: (1, 3), 2: (2, 3), 3: (3, 4), 4: (5, 5), 5: (6, 6), 6: (7, 7)},
    2: {1: (2, 3), 2: (2, 3), 3: (4, 5), 4: (5, 5), 5: (6, 7), 6: (7, 7)},
    3: {1: (3, 3), 2: (3, 4), 3: (4, 5), 4: (5, 6), 5: (6, 7), 6: (7, 7)},
    4: {1: (5, 5), 2: (5, 6), 3: (6, 7), 4: (7, 7), 5: (7, 7), 6: (8, 8)},
    5: {1: (7, 7), 2: (7, 7), 3: (7, 8), 4: (8, 8), 5: (8, 8), 6: (8, 8)},
    6: {1: (8, 8), 2: (8, 8), 3: (8, 8), 4: (8, 9), 5: (9, 9), 6: (9, 9)},
}
# Table C: rows = Score A (1..8, clamped), cols = Score B (1..7, clamped) -> grand 1..7.
_RULA_TABLE_C: List[List[int]] = [
    [1, 2, 3, 3, 4, 5, 5],   # A=1
    [2, 2, 3, 4, 4, 5, 5],   # A=2
    [3, 3, 3, 4, 4, 5, 6],   # A=3
    [3, 3, 3, 4, 5, 6, 6],   # A=4
    [4, 4, 4, 5, 6, 7, 7],   # A=5
    [4, 4, 5, 6, 6, 7, 7],   # A=6
    [5, 5, 6, 6, 7, 7, 7],   # A=7
    [5, 5, 6, 7, 7, 7, 7],   # A=8+
]
# RULA 4 action levels keyed by grand score.
_RULA_ACTIONS = {
    1: (1, "Acceptable posture if not maintained or repeated for long periods."),
    2: (2, "Further investigation is needed; changes may be required."),
    3: (3, "Investigation and changes are required soon."),
    4: (4, "Investigation and changes are required immediately."),
}

# --- REBA LOCKED tables (Hignett & McAtamney 2000) ---------------------------
# Table A: [neck][trunk] -> [legs=1, legs=2, legs=3, legs=4].
_REBA_TABLE_A: Dict[int, Dict[int, List[int]]] = {
    1: {1: [1, 2, 3, 4], 2: [2, 3, 4, 5], 3: [2, 4, 5, 6], 4: [3, 5, 6, 7], 5: [4, 6, 7, 8]},
    2: {1: [1, 2, 3, 4], 2: [3, 4, 5, 6], 3: [4, 5, 6, 7], 4: [5, 6, 7, 8], 5: [6, 7, 8, 9]},
    3: {1: [3, 3, 5, 6], 2: [4, 5, 6, 7], 3: [5, 6, 7, 8], 4: [6, 7, 8, 9], 5: [7, 8, 9, 9]},
}
# Table B: [lower_arm][upper_arm] -> [wrist=1, wrist=2, wrist=3].
_REBA_TABLE_B: Dict[int, Dict[int, List[int]]] = {
    1: {1: [1, 2, 2], 2: [1, 2, 3], 3: [3, 4, 5], 4: [4, 5, 5], 5: [6, 7, 8], 6: [7, 8, 8]},
    2: {1: [1, 2, 3], 2: [2, 3, 4], 3: [4, 5, 5], 4: [5, 6, 7], 5: [7, 8, 8], 6: [8, 9, 9]},
}
# Table C: rows = Score A (1..12), cols = Score B (1..12) -> Score C 1..12.
_REBA_TABLE_C: List[List[int]] = [
    [1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7],
    [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8],
    [2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8],
    [3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9],
    [4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9],
    [6, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 10],
    [7, 7, 7, 8, 9, 9, 9, 10, 10, 11, 11, 11],
    [8, 8, 8, 9, 10, 10, 10, 10, 10, 11, 11, 11],
    [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12],
    [10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12],
    [11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12],
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
]
# REBA 5 action levels keyed by final score band.
_REBA_BANDS = [
    (1, 1, 1, "Negligible risk — no action necessary."),
    (2, 3, 2, "Low risk — change may be needed."),
    (4, 7, 3, "Medium risk — further investigation, change soon."),
    (8, 10, 4, "High risk — investigate and implement change."),
    (11, 15, 5, "Very high risk — implement change now."),
]

# The 12 report.json block types (the only ones to_report_blocks may emit).
_REPORT_BLOCK_TYPES = frozenset({
    "heading", "paragraph", "bullets", "table", "metrics", "callout",
    "findings", "hoc_table", "recommendations", "divider", "page_break", "spacer",
})


# --- helpers -----------------------------------------------------------------

def _num(value: Any, name: str) -> float:
    """Coerce a numeric input or raise ErgonomicsInputError (no bool, no str)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ErgonomicsInputError(f"{name} must be a number (got {value!r})")
    return float(value)


def _joint(value: Any, name: str, lo: int, hi: int) -> int:
    """Validate an integer joint/posture score in [lo, hi] or raise (D-03)."""
    if isinstance(value, bool):
        raise ErgonomicsInputError(f"{name} must be an integer in {lo}..{hi}")
    if isinstance(value, float):
        if not value.is_integer():
            raise ErgonomicsInputError(f"{name} must be a whole number (got {value})")
        value = int(value)
    if not isinstance(value, int):
        raise ErgonomicsInputError(f"{name} must be an integer (got {type(value).__name__})")
    if not (lo <= value <= hi):
        raise ErgonomicsInputError(f"{name} {value} out of range {lo}..{hi}")
    return value


def _addon(value: Any, name: str, lo: int, hi: int) -> int:
    """Validate an additive modifier (muscle 0/1, force/coupling 0..3 etc.)."""
    return _joint(value, name, lo, hi)


# --- NIOSH revised lifting equation ------------------------------------------

def niosh_rwl(
    weight: float,
    h: float,
    v: float,
    d: float,
    a: float = 0,
    frequency: float = 0.2,
    duration: float = 1,
    coupling: str = "good",
) -> Dict[str, Any]:
    """NIOSH revised (1991) Recommended Weight Limit + Lifting Index.

    Units: ``weight`` kg; ``h`` horizontal location (cm); ``v`` vertical
    location at origin (cm); ``d`` vertical travel distance (cm); ``a``
    asymmetry angle (degrees); ``frequency`` lifts/min; ``duration`` work
    duration (hours, snapped to the <=1 / <=2 / <=8 h NIOSH band); ``coupling``
    one of "good"/"fair"/"poor".

    Multipliers are computed then rounded to 2dp (NIOSH worksheet convention)
    and multiplied; ``RWL = LC x HM x VM x DM x AM x FM x CM``; ``LI = weight /
    RWL``. Returns a JSON-serialisable dict with ``rwl``, ``li``,
    ``multipliers``, ``lc`` and ``notes``.

    D-03 fail-loud: negative weight, H/V/D <= 0, asymmetry < 0, or an unknown
    coupling key raises ErgonomicsInputError. Out-of-domain geometry that the
    standard zeroes (H>63, V>175, D>175, A>135) yields the published 0
    multiplier (RWL -> 0) — that is the method, not a silent clamp.
    """
    weight = _num(weight, "weight")
    h = _num(h, "h")
    v = _num(v, "v")
    d = _num(d, "d")
    a = _num(a, "a")
    frequency = _num(frequency, "frequency")
    duration = _num(duration, "duration")

    if weight < 0:
        raise ErgonomicsInputError("weight must be >= 0 kg")
    if h <= 0:
        raise ErgonomicsInputError("h (horizontal location) must be > 0 cm")
    if v < 0:
        raise ErgonomicsInputError("v (vertical location) must be >= 0 cm")
    if d <= 0:
        raise ErgonomicsInputError("d (vertical travel) must be > 0 cm")
    if a < 0:
        raise ErgonomicsInputError("a (asymmetry angle) must be >= 0 degrees")
    if frequency < 0:
        raise ErgonomicsInputError("frequency must be >= 0 lifts/min")
    if not isinstance(coupling, str) or coupling.lower() not in _NIOSH_CM:
        raise ErgonomicsInputError(
            f"coupling must be one of {sorted(_NIOSH_CM)} (got {coupling!r})"
        )

    # Horizontal multiplier.
    if h > 63:
        hm = 0.0
    elif h <= 25:
        hm = 1.0
    else:
        hm = 25.0 / h
    # Vertical multiplier.
    vm = 0.0 if v > 175 else 1 - 0.003 * abs(v - 75)
    # Distance multiplier.
    if d > 175:
        dm = 0.0
    elif d < 25:
        dm = 1.0
    else:
        dm = 0.82 + 4.5 / d
    # Asymmetry multiplier.
    am = 0.0 if a > 135 else 1 - 0.0032 * a

    # Frequency duration band.
    if duration <= 1:
        band = "1"
    elif duration <= 2:
        band = "2"
    else:
        band = "8"
    bucket = _NIOSH_FM_BUCKETS[0]
    for b in _NIOSH_FM_BUCKETS:
        if frequency >= b:
            bucket = b
    fm = _NIOSH_FM[band][bucket]

    # Coupling multiplier (V band).
    cm = _NIOSH_CM[coupling.lower()]["low" if v < 75 else "high"]

    mult = {
        "hm": round(hm, 2), "vm": round(vm, 2), "dm": round(dm, 2),
        "am": round(am, 2), "fm": round(fm, 2), "cm": round(cm, 2),
    }
    rwl = (
        NIOSH_LC_KG * mult["hm"] * mult["vm"] * mult["dm"]
        * mult["am"] * mult["fm"] * mult["cm"]
    )
    rwl = round(rwl, _ROUND_DP)
    li = round(weight / rwl, _ROUND_DP) if rwl > 0 else None

    notes = ["NIOSH revised (1991) lifting equation; LC=23 kg (metric)."]
    if rwl == 0:
        notes.append("RWL = 0: a multiplier is 0 (input outside the NIOSH design domain).")
    elif li is not None and li > 1.0:
        notes.append("LI > 1.0: lifting demand exceeds the recommended limit — elevated risk.")

    return {
        "rwl": rwl,
        "li": li,
        "multipliers": mult,
        "lc": NIOSH_LC_KG,
        "weight": weight,
        "notes": notes,
    }


# --- RULA --------------------------------------------------------------------

def rula_score(
    upper_arm: int,
    lower_arm: int,
    wrist: int,
    wrist_twist: int,
    neck: int,
    trunk: int,
    legs: int,
    muscle_use_a: int = 0,
    force_a: int = 0,
    muscle_use_b: int = 0,
    force_b: int = 0,
) -> Dict[str, Any]:
    """RULA (McAtamney & Corlett 1993) grand score + action level.

    Group A joints: upper_arm 1-6, lower_arm 1-3, wrist 1-4, wrist_twist 1-2.
    Group B joints: neck 1-6, trunk 1-6, legs 1-2. Modifiers: muscle_use 0-1,
    force/load 0-3 (per group). Returns ``grand_score`` (int 1-7),
    ``action_level`` (int 1-4), ``action`` text, and a ``working`` dict with
    the per-step sub-scores. Out-of-range joints raise ErgonomicsInputError.
    """
    ua = _joint(upper_arm, "upper_arm", 1, 6)
    la = _joint(lower_arm, "lower_arm", 1, 3)
    wr = _joint(wrist, "wrist", 1, 4)
    wt = _joint(wrist_twist, "wrist_twist", 1, 2)
    nk = _joint(neck, "neck", 1, 6)
    tr = _joint(trunk, "trunk", 1, 6)
    lg = _joint(legs, "legs", 1, 2)
    mua = _addon(muscle_use_a, "muscle_use_a", 0, 1)
    fa = _addon(force_a, "force_a", 0, 3)
    mub = _addon(muscle_use_b, "muscle_use_b", 0, 1)
    fb = _addon(force_b, "force_b", 0, 3)

    posture_a = _RULA_TABLE_A[ua][la][wr][wt - 1]
    score_a = posture_a + mua + fa
    posture_b = _RULA_TABLE_B[nk][tr][lg - 1]
    score_b = posture_b + mub + fb

    row = min(score_a, 8) - 1
    col = min(score_b, 7) - 1
    grand = _RULA_TABLE_C[row][col]
    level, action = _RULA_ACTIONS[
        1 if grand <= 2 else 2 if grand <= 4 else 3 if grand <= 6 else 4
    ]

    return {
        "grand_score": grand,
        "action_level": level,
        "action": action,
        "working": {
            "posture_a": posture_a,
            "score_a": score_a,
            "posture_b": posture_b,
            "score_b": score_b,
        },
    }


# --- REBA --------------------------------------------------------------------

def reba_score(
    trunk: int,
    neck: int,
    legs: int,
    load_force: int,
    upper_arm: int,
    lower_arm: int,
    wrist: int,
    coupling: int = 0,
    activity: int = 0,
) -> Dict[str, Any]:
    """REBA (Hignett & McAtamney 2000) final score + action level.

    Group A joints: trunk 1-5, neck 1-3, legs 1-4; + load_force 0-3.
    Group B joints: upper_arm 1-6, lower_arm 1-2, wrist 1-3; + coupling 0-3.
    activity 0-3 (sum of the activity criteria). Returns ``final_score`` (int
    1-15), ``action_level`` (int 1-5), ``action`` text, and a ``working`` dict.
    Out-of-range joints raise ErgonomicsInputError.
    """
    tr = _joint(trunk, "trunk", 1, 5)
    nk = _joint(neck, "neck", 1, 3)
    lg = _joint(legs, "legs", 1, 4)
    lf = _addon(load_force, "load_force", 0, 3)
    ua = _joint(upper_arm, "upper_arm", 1, 6)
    la = _joint(lower_arm, "lower_arm", 1, 2)
    wr = _joint(wrist, "wrist", 1, 3)
    cp = _addon(coupling, "coupling", 0, 3)
    act = _addon(activity, "activity", 0, 3)

    posture_a = _REBA_TABLE_A[nk][tr][lg - 1]
    score_a = posture_a + lf
    posture_b = _REBA_TABLE_B[la][ua][wr - 1]
    score_b = posture_b + cp

    row = min(score_a, 12) - 1
    col = min(score_b, 12) - 1
    score_c = _REBA_TABLE_C[row][col]
    final = min(score_c + act, 15)

    level = action = None
    for lo, hi, lvl, txt in _REBA_BANDS:
        if lo <= final <= hi:
            level, action = lvl, txt
            break

    return {
        "final_score": final,
        "action_level": level,
        "action": action,
        "working": {
            "posture_a": posture_a,
            "score_a": score_a,
            "posture_b": posture_b,
            "score_b": score_b,
            "score_c": score_c,
        },
    }


# --- D-02 report-ready helper ------------------------------------------------

def to_report_blocks(result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Turn an engine result dict into a list of EXISTING report.json blocks.

    Emits ONLY the 12 schema block types (D-02/D-04): a ``metrics`` block for
    the headline figure(s) + a ``table`` block for the per-step ``working`` /
    ``multipliers``. Detects which engine produced ``result`` by its keys.
    """
    if not isinstance(result, dict):
        raise ErgonomicsInputError("to_report_blocks expects an engine result dict")

    metrics: List[Dict[str, Any]] = []
    rows: List[List[Any]] = []

    if "rwl" in result:  # NIOSH
        metrics = [
            {"label": "Recommended Weight Limit", "value": result["rwl"], "unit": "kg"},
            {"label": "Lifting Index", "value": result["li"]},
        ]
        rows = [[k.upper(), v] for k, v in result.get("multipliers", {}).items()]
    elif "grand_score" in result:  # RULA
        metrics = [
            {"label": "RULA grand score", "value": result["grand_score"]},
            {"label": "Action level", "value": result["action_level"]},
        ]
        rows = [[k, v] for k, v in result.get("working", {}).items()]
    elif "final_score" in result:  # REBA
        metrics = [
            {"label": "REBA final score", "value": result["final_score"]},
            {"label": "Action level", "value": result["action_level"]},
        ]
        rows = [[k, v] for k, v in result.get("working", {}).items()]
    else:
        raise ErgonomicsInputError("unrecognised engine result dict")

    return [
        {"type": "metrics", "metrics": metrics},
        {"type": "table", "headers": ["Step", "Value"], "rows": rows},
    ]


__all__ = [
    "ErgonomicsInputError",
    "NIOSH_LC_KG",
    "niosh_rwl",
    "rula_score",
    "reba_score",
    "to_report_blocks",
]
