"""
fatigue.py — SUB-03 driver-fatigue engine: FMCSA HOS + EU 561/2006 window math
+ a deterministic ADVISORY fatigue index.

Two classes of output, kept strictly distinct (Assumption A4 / threat T-11-04):

  1. COMPLIANCE FLAGS — authoritative, primary output, derived directly from the
     regulations. ``fmcsa_compliance`` implements the US FMCSA Hours-of-Service
     rules for property-carrying CMVs (49 CFR 395.3); ``eu561_compliance``
     implements EU Regulation (EC) 561/2006 drivers' hours. Each returns per-rule
     booleans where True == compliant with that rule and False == a breach, plus
     the binding limit and the working figures used.

  2. FATIGUE INDEX — a clearly-labelled ADVISORY / derived metric. The
     regulations give *compliance*, not a numeric fatigue score; the index is a
     transparent, golden-testable weighted-stressor heuristic, NOT a validated
     biomathematical model and NOT a regulatory threshold. ``fatigue_index``'s
     result dict carries ``advisory: True`` and a note saying exactly that.

Fatigue-index formula (owner-confirmed weighted-stressor approach, weights
LOCKED below):

    fatigue_index = 0.4·(cumulative_driving_h / daily_limit)
                  + 0.3·(hours_since_last_qualifying_rest / window)
                  + 0.3·time_of_day_factor

where ``time_of_day_factor`` peaks (→1.0) inside the Window of Circadian Low
(WOCL, ~02:00–06:00) and tapers toward 0.0 across the waking day. The score is
clamped to [0,1] and banded Low/Moderate/High/Severe at 0.25/0.50/0.75.

Fail-loud (D-03): negative durations, a single-day duty total > 24 h, or a
malformed segment raise ``FatigueInputError`` — never a silent clamp. The unit
contract: all durations are hours as floats; ``status`` is one of the documented
enum ``driving | on_duty | off_duty | sleeper``; ``time_of_day`` is a 0–24 clock
hour (float). Pure stdlib — no numpy/scipy.

Golden anchors (fixtures/fatigue_cases.json): FAT-1 (12 h driving → FMCSA
driving_11h FAIL); FAT-2 (5 h continuous → EU break_45min FAIL); FAT-3 /
FAT-3b (9.5 h driving, extension-aware daily_driving); FAT-4 (clean shift →
all flags PASS + index ∈ [0,1]).
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

# --- LOCKED constants: FMCSA HOS, 49 CFR 395.3 (property-carrying CMV) --------
# Source: fmcsa.dot.gov Summary of HOS Regulations.
DRIVE_LIMIT_H = 11.0          # max 11 h driving after 10 consecutive h off duty
WINDOW_H = 14.0              # may not drive beyond the 14th consecutive on-duty h
BREAK_AFTER_DRIVING_H = 8.0  # 30-min break required after 8 cumulative driving h
BREAK_MIN = 30              # …the break must be >= 30 minutes
CYCLE_60_7 = 60.0            # 60 h on duty in 7 consecutive days (non-daily carrier)
CYCLE_70_8 = 70.0            # 70 h on duty in 8 consecutive days (daily carrier)
RESTART_H = 34.0            # >=34 consecutive h off duty resets the 60/70 clock

# --- LOCKED constants: EU Regulation (EC) 561/2006 ---------------------------
# Source: transport.ec.europa.eu, eur-lex.europa.eu.
EU_DAILY_DRIVE_H = 9.0          # daily driving <= 9 h…
EU_DAILY_DRIVE_EXT_H = 10.0     # …extendable to 10 h twice per week
EU_EXT_PER_WEEK = 2            # number of 10 h extensions permitted per week
EU_BREAK_AFTER_H = 4.5          # break required after 4.5 h continuous driving
EU_BREAK_MIN = 45              # …the break must total >= 45 minutes
EU_DAILY_REST_H = 11.0          # daily rest >= 11 h…
EU_DAILY_REST_REDUCED_H = 9.0   # …reducible to 9 h up to 3x between weekly rests
EU_WEEKLY_DRIVE_H = 56.0        # weekly driving <= 56 h
EU_FORTNIGHT_DRIVE_H = 90.0     # fortnightly driving <= 90 h

# --- LOCKED constants: advisory fatigue index (owner-confirmed weights) -------
# Weighted-stressor heuristic — ADVISORY, not a regulatory threshold (A4).
W_DRIVING = 0.4              # cumulative driving load
W_TIME_AWAKE = 0.3          # hours since the last qualifying rest, vs the window
W_TIME_OF_DAY = 0.3         # circadian timing (WOCL)
WOCL_START_H = 2.0          # Window of Circadian Low start (~02:00)
WOCL_END_H = 6.0            # Window of Circadian Low end   (~06:00)
_INDEX_BANDS = (            # (upper_exclusive_bound, band) — last is the catch-all
    (0.25, "Low"),
    (0.50, "Moderate"),
    (0.75, "High"),
    (1.01, "Severe"),
)

# qualifying-rest minimum (a non-driving interruption that "resets" continuous
# driving for the index's time-awake term): the EU 45-min break in hours.
_QUALIFYING_REST_H = EU_BREAK_MIN / 60.0

# The 12 report.json block types (the only ones to_report_blocks may emit).
_REPORT_BLOCK_TYPES = frozenset({
    "heading", "paragraph", "bullets", "table", "metrics", "callout",
    "findings", "hoc_table", "recommendations", "divider", "page_break", "spacer",
})

_STATUSES = frozenset({"driving", "on_duty", "off_duty", "sleeper"})
_NON_DRIVING = frozenset({"on_duty", "off_duty", "sleeper"})
_REST = frozenset({"off_duty", "sleeper"})


class FatigueInputError(ValueError):
    """Raised on an invalid duty log (negative hours, >24 h day, malformed)."""


# --- input validation (D-03 fail-loud) ---------------------------------------

def _validate_log(duty_log: Any) -> List[Dict[str, Any]]:
    """Validate a duty log and return a normalized list of segments.

    Fail-loud: a non-list, a malformed segment, an unknown status, a negative
    duration, or a single-day total > 24 h each raise FatigueInputError. There
    is NEVER a silent clamp (D-03)."""
    if not isinstance(duty_log, list) or not duty_log:
        raise FatigueInputError("duty_log must be a non-empty list of segments")

    segments: List[Dict[str, Any]] = []
    total = 0.0
    for i, seg in enumerate(duty_log):
        if not isinstance(seg, dict):
            raise FatigueInputError(f"segment {i} must be a dict (got {type(seg).__name__})")
        status = seg.get("status")
        hours = seg.get("hours")
        if status not in _STATUSES:
            raise FatigueInputError(
                f"segment {i} status must be one of {sorted(_STATUSES)} (got {status!r})"
            )
        if isinstance(hours, bool) or not isinstance(hours, (int, float)):
            raise FatigueInputError(f"segment {i} hours must be a number (got {hours!r})")
        hours = float(hours)
        if hours < 0:
            raise FatigueInputError(f"segment {i} hours must be >= 0 (got {hours})")
        total += hours
        segments.append({"status": status, "hours": hours})

    if total > 24.0:
        raise FatigueInputError(
            f"duty-log day total {total} h exceeds 24 h — invalid single-day log"
        )
    return segments


def _validate_time_of_day(time_of_day: Any) -> Optional[float]:
    """Validate an optional 0–24 clock hour, or raise FatigueInputError."""
    if time_of_day is None:
        return None
    if isinstance(time_of_day, bool) or not isinstance(time_of_day, (int, float)):
        raise FatigueInputError(f"time_of_day must be a number (got {time_of_day!r})")
    tod = float(time_of_day)
    if not (0.0 <= tod <= 24.0):
        raise FatigueInputError(f"time_of_day must be in 0..24 (got {tod})")
    return tod


# --- FMCSA Hours-of-Service compliance (49 CFR 395.3) ------------------------

def fmcsa_compliance(duty_log: Any) -> Dict[str, Any]:
    """FMCSA HOS per-rule compliance flags (property-carrying CMV, 49 CFR 395.3).

    Returns booleans where True == compliant with the rule. ``duty_log`` is a
    list of ``{status, hours}`` segments for one shift; multi-day cycle rules
    (60/70 h, 34 h restart) default to compliant for a single-shift log unless a
    breach is detectable.
    """
    segments = _validate_log(duty_log)

    total_driving = sum(s["hours"] for s in segments if s["status"] == "driving")
    # On-duty window = elapsed time from the first work segment to the last work
    # segment (off-duty inside the span counts toward the 14 h but never extends
    # it). With no timestamps, that is the sum of segments between the first and
    # last non-off-duty segment.
    work_idx = [i for i, s in enumerate(segments) if s["status"] in ("driving", "on_duty")]
    if work_idx:
        window_used = sum(s["hours"] for s in segments[work_idx[0]: work_idx[-1] + 1])
    else:
        window_used = 0.0

    # 30-min break after 8 cumulative driving hours: walk the log; the rule is
    # breached only if continuous driving EXCEEDS 8 h without an intervening
    # >= 30-min non-driving interruption. Driving exactly to the limit and then
    # taking a qualifying break is compliant, so a strict > comparison is used
    # and a qualifying interruption resets the counter before the next segment.
    cumulative_drive = 0.0
    break_ok = True
    for s in segments:
        if s["status"] == "driving":
            cumulative_drive += s["hours"]
            if cumulative_drive > BREAK_AFTER_DRIVING_H + 1e-9:
                break_ok = False
                break
        elif s["hours"] * 60.0 >= BREAK_MIN:
            cumulative_drive = 0.0  # a qualifying interruption resets the counter

    driving_11h = total_driving <= DRIVE_LIMIT_H + 1e-9
    within_14h_window = window_used <= WINDOW_H + 1e-9

    if not driving_11h:
        binding = "11 h driving limit (49 CFR 395.3(a)(3))"
    elif not within_14h_window:
        binding = "14 h on-duty window (49 CFR 395.3(a)(2))"
    elif not break_ok:
        binding = "30-min break after 8 h driving (49 CFR 395.3(a)(3)(ii))"
    else:
        binding = "within all FMCSA HOS limits"

    return {
        "driving_11h": driving_11h,
        "within_14h_window": within_14h_window,
        "break_30min_after_8h": break_ok,
        "cycle_60_70h": True,   # single-shift log: no multi-day breach detectable
        "restart_34h": True,    # single-shift log: restart not applicable
        "binding_limit": binding,
        "working": {
            "total_driving_h": round(total_driving, 3),
            "window_used_h": round(window_used, 3),
            "drive_limit_h": DRIVE_LIMIT_H,
            "window_h": WINDOW_H,
        },
    }


# --- EU 561/2006 compliance --------------------------------------------------

def eu561_compliance(duty_log: Any, extensions_used: int = 0) -> Dict[str, Any]:
    """EU Regulation (EC) 561/2006 per-rule compliance flags.

    ``extensions_used`` is the number of 10 h daily-driving extensions already
    used this week (0, 1 or 2): the daily-driving limit is 9 h, or 10 h while a
    twice-weekly extension is still available. Returns booleans where True ==
    compliant. Weekly/fortnight/daily-rest rules default to compliant for a
    single-shift log unless a breach is detectable from the segments.
    """
    segments = _validate_log(duty_log)

    if isinstance(extensions_used, bool) or not isinstance(extensions_used, int):
        raise FatigueInputError(f"extensions_used must be an int (got {extensions_used!r})")
    if not (0 <= extensions_used <= EU_EXT_PER_WEEK):
        raise FatigueInputError(
            f"extensions_used must be in 0..{EU_EXT_PER_WEEK} (got {extensions_used})"
        )

    total_driving = sum(s["hours"] for s in segments if s["status"] == "driving")

    # Daily driving: the 10 h extension applies only if one is still available.
    extension_available = extensions_used < EU_EXT_PER_WEEK
    daily_limit = EU_DAILY_DRIVE_EXT_H if extension_available else EU_DAILY_DRIVE_H
    daily_driving = total_driving <= daily_limit + 1e-9

    # 45-min break after 4.5 h continuous driving (Art. 7): walk the log; the
    # rule is breached only if continuous driving EXCEEDS 4.5 h without an
    # intervening >= 45-min break. Driving exactly to 4.5 h and then taking a
    # qualifying break is compliant (FAT-3), so a strict > comparison is used
    # and a qualifying interruption resets the counter before the next segment.
    cumulative_drive = 0.0
    break_ok = True
    for s in segments:
        if s["status"] == "driving":
            cumulative_drive += s["hours"]
            if cumulative_drive > EU_BREAK_AFTER_H + 1e-9:
                break_ok = False
                break
        elif s["hours"] * 60.0 >= EU_BREAK_MIN:
            cumulative_drive = 0.0

    # Daily rest is a SINGLE consolidated rest period (>= 11 h, or >= 9 h
    # reduced) — NOT the sum of short continuous-driving breaks. Assess the
    # LONGEST rest segment: if it reaches the reduced floor it is the daily rest
    # and must be >= 11 h (else a reduced-rest breach); if no segment is long
    # enough to be a daily rest, this single-shift log does not represent the
    # daily rest period -> not assessable here -> default True. This prevents a
    # cluster of short 45-min breaks from reading as an under-length daily rest.
    rest_segments = [s["hours"] for s in segments if s["status"] in _REST]
    longest_rest = max(rest_segments) if rest_segments else 0.0
    is_daily_rest = longest_rest >= EU_DAILY_REST_REDUCED_H - 1e-9
    daily_rest_11h = (not is_daily_rest) or longest_rest >= EU_DAILY_REST_H - 1e-9

    weekly_driving_56h = total_driving <= EU_WEEKLY_DRIVE_H + 1e-9
    fortnight_driving_90h = total_driving <= EU_FORTNIGHT_DRIVE_H + 1e-9

    if not daily_driving:
        binding = f"{daily_limit:g} h daily driving (Art. 6(1))"
    elif not break_ok:
        binding = "45-min break after 4.5 h driving (Art. 7)"
    elif not daily_rest_11h:
        binding = "11 h daily rest (Art. 8)"
    else:
        binding = "within all EU 561/2006 limits"

    return {
        "daily_driving": daily_driving,
        "break_45min_after_4.5h": break_ok,
        "daily_rest_11h": daily_rest_11h,
        "weekly_driving_56h": weekly_driving_56h,
        "fortnight_driving_90h": fortnight_driving_90h,
        "binding_limit": binding,
        "working": {
            "total_driving_h": round(total_driving, 3),
            "daily_limit_h": daily_limit,
            "extensions_used": extensions_used,
            "extension_available": extension_available,
            "longest_rest_h": round(longest_rest, 3),
        },
    }


# --- advisory fatigue index (ADVISORY / derived — not a regulatory threshold) -

def _time_of_day_factor(time_of_day: Optional[float]) -> float:
    """Circadian-timing stressor in [0,1], peaking in the WOCL (~02:00–06:00).

    Deterministic piecewise curve: 1.0 across the WOCL, tapering linearly to 0.0
    over the ~8 h on either side of the WOCL midpoint. When ``time_of_day`` is
    unknown, return a neutral 0.0 (no circadian penalty asserted)."""
    if time_of_day is None:
        return 0.0
    midpoint = (WOCL_START_H + WOCL_END_H) / 2.0  # ~04:00
    # circular distance (hours) from the WOCL midpoint on a 24 h clock
    raw = abs(time_of_day - midpoint)
    dist = min(raw, 24.0 - raw)
    half_wocl = (WOCL_END_H - WOCL_START_H) / 2.0  # 2 h
    if dist <= half_wocl:
        return 1.0
    taper = 8.0  # hours over which the factor decays to 0 outside the WOCL
    factor = 1.0 - (dist - half_wocl) / taper
    return max(0.0, min(1.0, factor))


def _band(score: float) -> str:
    for upper, name in _INDEX_BANDS:
        if score < upper:
            return name
    return _INDEX_BANDS[-1][1]


def fatigue_index(
    duty_log: Any,
    time_of_day: Optional[float] = None,
    daily_limit: float = DRIVE_LIMIT_H,
    window: float = WINDOW_H,
) -> Dict[str, Any]:
    """Deterministic ADVISORY weighted-stressor fatigue index.

    NOT a regulatory threshold and NOT a validated biomathematical model — a
    transparent heuristic for triage only. The result dict carries
    ``advisory: True`` and a note saying so (A4 / T-11-04).

    score = 0.4·(cumulative_driving_h / daily_limit)
          + 0.3·(hours_since_last_qualifying_rest / window)
          + 0.3·time_of_day_factor          # peaks in the WOCL

    clamped to [0,1] and banded Low/Moderate/High/Severe at 0.25/0.50/0.75.
    Same input -> byte-identical output (rounded to 3 dp).
    """
    segments = _validate_log(duty_log)
    tod = _validate_time_of_day(time_of_day)
    if not isinstance(daily_limit, (int, float)) or isinstance(daily_limit, bool) or daily_limit <= 0:
        raise FatigueInputError("daily_limit must be a positive number")
    if not isinstance(window, (int, float)) or isinstance(window, bool) or window <= 0:
        raise FatigueInputError("window must be a positive number")

    cumulative_driving = sum(s["hours"] for s in segments if s["status"] == "driving")

    # hours since the last qualifying rest = hours elapsed (any status) after the
    # last >= 45-min rest segment; if none, the whole shift's elapsed time.
    last_rest_end = 0.0
    elapsed = 0.0
    for s in segments:
        elapsed += s["hours"]
        if s["status"] in _REST and s["hours"] >= _QUALIFYING_REST_H - 1e-9:
            last_rest_end = elapsed
    hours_since_rest = elapsed - last_rest_end

    driving_term = W_DRIVING * (cumulative_driving / daily_limit)
    awake_term = W_TIME_AWAKE * (hours_since_rest / window)
    tod_term = W_TIME_OF_DAY * _time_of_day_factor(tod)

    score = round(max(0.0, min(1.0, driving_term + awake_term + tod_term)), 3)
    band = _band(score)

    return {
        "score": score,
        "band": band,
        "advisory": True,
        "note": (
            "ADVISORY / derived metric — a transparent weighted-stressor "
            "heuristic, NOT a regulatory threshold and NOT a validated "
            "biomathematical model. Use the FMCSA / EU 561 compliance flags as "
            "the authoritative output."
        ),
        "weights": {
            "driving": W_DRIVING,
            "time_awake": W_TIME_AWAKE,
            "time_of_day": W_TIME_OF_DAY,
        },
        "working": {
            "cumulative_driving_h": round(cumulative_driving, 3),
            "hours_since_last_rest_h": round(hours_since_rest, 3),
            "time_of_day": tod,
            "wocl_window": [WOCL_START_H, WOCL_END_H],
            "daily_limit_h": daily_limit,
            "window_h": window,
        },
    }


# --- report blocks (12-block schema types only) ------------------------------

def to_report_blocks(result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Emit report.json block dicts (existing 12-block types only).

    ``result`` is a dict that may carry any of: ``fmcsa`` (an fmcsa_compliance
    result), ``eu561`` (an eu561_compliance result), and ``fatigue_index`` (a
    fatigue_index result). Produces a ``metrics`` headline (index + flag
    summary), a ``table`` of per-rule compliance, and a ``warning`` callout when
    any compliance flag is False.
    """
    if not isinstance(result, dict):
        raise FatigueInputError("to_report_blocks expects a result dict")

    fmcsa = result.get("fmcsa") or {}
    eu = result.get("eu561") or {}
    idx = result.get("fatigue_index") or {}

    _FLAG_KEYS = (
        "driving_11h", "within_14h_window", "break_30min_after_8h",
        "cycle_60_70h", "restart_34h",
        "daily_driving", "break_45min_after_4.5h", "daily_rest_11h",
        "weekly_driving_56h", "fortnight_driving_90h",
    )

    rows: List[List[Any]] = []
    any_breach = False
    for src_name, src in (("FMCSA", fmcsa), ("EU 561", eu)):
        for k in _FLAG_KEYS:
            if k in src:
                ok = bool(src[k])
                any_breach = any_breach or not ok
                rows.append([src_name, k, "PASS" if ok else "FAIL"])

    metrics: List[Dict[str, Any]] = []
    if idx:
        metrics.append({"label": "Fatigue index (advisory)", "value": idx.get("score")})
        metrics.append({"label": "Band (advisory)", "value": idx.get("band")})
    metrics.append({"label": "Compliance", "value": "BREACH" if any_breach else "OK"})

    blocks: List[Dict[str, Any]] = [
        {"type": "metrics", "metrics": metrics},
    ]
    if rows:
        blocks.append({
            "type": "table",
            "headers": ["Standard", "Rule", "Result"],
            "rows": rows,
            "caption": "FMCSA 49 CFR 395.3 / EU 561/2006 per-rule compliance",
        })
    if any_breach:
        blocks.append({
            "type": "callout",
            "box_type": "warning",
            "text": (
                "One or more hours-of-service compliance rules are breached — "
                "review the failing rule(s) above. The fatigue index is advisory "
                "only; the compliance flags are the authoritative finding."
            ),
        })
    return blocks


__all__ = [
    "fmcsa_compliance",
    "eu561_compliance",
    "fatigue_index",
    "to_report_blocks",
    "FatigueInputError",
]
