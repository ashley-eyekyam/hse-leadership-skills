"""
incident_rates.py — OSHA-standard lagging incident-rate calculator.

Computes TRIR / DART / LTIFR with the **correct, non-overridable denominators**.
This is the most safety-critical engine to get exactly right — a wrong base
produces a non-comparable, indefensible figure (A7 §3.5).

The OSHA bases are module CONSTANTS by design (D5 — NOT config). The industry
benchmark figure is data the caller supplies (carrying its own source + year per
A3's KB discipline); this engine only computes the delta.

Fail-loud edges (D6): hours_worked <= 0 raises ValueError (never a divide-by-
zero, never a silent 0.0 that would read as "perfect safety"); negative counts
raise ValueError; non-integer counts are coerced via int() only if exact, else
ValueError. **No implicit annualization** for partial periods — the caller
passes the actual hours-to-date and the period label; ``notes`` records that the
figure is period-actual.

Locked worked-example anchors (A7 §3.8): trir(3, 290_000) == 2.07 and
ltifr(6, 1_000_000) == 6.00. Rates round to 2 dp at the boundary.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

# --- LOCKED constants (D5 — bases are constants by design, never config) -----
OSHA_BASE = 200_000        # 100 full-time workers × 40 h × 50 wk (TRIR / DART)
MILLION_BASE = 1_000_000   # LTIFR convention

_ROUND_DP = 2


def _check_inputs(count: Any, hours_worked: Any, count_label: str) -> int:
    """Validate a (count, hours_worked) pair, returning the count as an int.

    Fail-loud: hours_worked <= 0 -> ValueError; negative count -> ValueError;
    non-integer count -> ValueError unless it is an exact integer value."""
    if not isinstance(hours_worked, (int, float)) or isinstance(hours_worked, bool):
        raise ValueError("hours_worked must be a number")
    if hours_worked <= 0:
        raise ValueError("hours_worked must be > 0")

    if isinstance(count, bool):
        raise ValueError(f"{count_label} must be a non-negative integer")
    if isinstance(count, float):
        if not count.is_integer():
            raise ValueError(f"{count_label} must be an exact integer (got {count})")
        count = int(count)
    if not isinstance(count, int):
        raise ValueError(f"{count_label} must be an integer (got {type(count).__name__})")
    if count < 0:
        raise ValueError(f"{count_label} must be >= 0 (got {count})")
    return count


def trir(recordables: int, hours_worked: float) -> float:
    """Total Recordable Incident Rate = recordables × 200,000 / hours_worked."""
    n = _check_inputs(recordables, hours_worked, "recordables")
    return round(n * OSHA_BASE / hours_worked, _ROUND_DP)


def dart(dart_cases: int, hours_worked: float) -> float:
    """Days-Away/Restricted/Transfer rate = dart_cases × 200,000 / hours_worked."""
    n = _check_inputs(dart_cases, hours_worked, "dart_cases")
    return round(n * OSHA_BASE / hours_worked, _ROUND_DP)


def ltifr(lost_time_injuries: int, hours_worked: float) -> float:
    """Lost-Time Injury Frequency Rate = LTIs × 1,000,000 / hours_worked."""
    n = _check_inputs(lost_time_injuries, hours_worked, "lost_time_injuries")
    return round(n * MILLION_BASE / hours_worked, _ROUND_DP)


def compute_all(
    counts: Dict[str, Any], hours_worked: float, period: Optional[str] = None
) -> Dict[str, Any]:
    """Compute all three rates for one (counts, hours_worked) input.

    ``counts`` keys (each optional, default 0): ``recordables``, ``dart_cases``,
    ``lost_time_injuries``. ``hours_worked`` is the ACTUAL hours-to-date — it is
    NOT annualized, even when ``period`` is given; ``period`` is a label
    recorded in the output, never a scaling factor.

    Returns a JSON-serialisable dict with the three rates, the bases used, the
    period label, and a note that the figures are period-actual (not
    annualized)."""
    if not isinstance(counts, dict):
        raise ValueError("counts must be a dict")

    recordables = counts.get("recordables", 0)
    dart_cases = counts.get("dart_cases", 0)
    lost_time = counts.get("lost_time_injuries", 0)

    return {
        "trir": trir(recordables, hours_worked),
        "dart": dart(dart_cases, hours_worked),
        "ltifr": ltifr(lost_time, hours_worked),
        "hours_worked": hours_worked,
        "base_trir_dart": OSHA_BASE,
        "base_ltifr": MILLION_BASE,
        "period": period,
        "notes": ["rates use OSHA-standard bases; period-actual, not annualized"],
    }


def benchmark_delta(rate: float, industry_rate: float) -> Dict[str, Any]:
    """Compare a computed rate against a caller-supplied industry benchmark.

    The industry figure is the caller's data (it carries its own source + year
    per A3 §17); this only computes the signed delta and direction. A lower rate
    is better, so ``better_than_industry`` is True when rate < industry_rate."""
    if not isinstance(rate, (int, float)) or isinstance(rate, bool):
        raise ValueError("rate must be a number")
    if not isinstance(industry_rate, (int, float)) or isinstance(industry_rate, bool):
        raise ValueError("industry_rate must be a number")
    if industry_rate < 0:
        raise ValueError("industry_rate must be >= 0")

    delta = round(rate - industry_rate, _ROUND_DP)
    return {
        "rate": rate,
        "industry_rate": industry_rate,
        "delta": delta,
        "better_than_industry": rate < industry_rate,
    }


__all__ = [
    "OSHA_BASE",
    "MILLION_BASE",
    "trir",
    "dart",
    "ltifr",
    "compute_all",
    "benchmark_delta",
]
