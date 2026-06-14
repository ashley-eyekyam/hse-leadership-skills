"""
risk_matrix.py — deterministic (likelihood × severity) risk-scoring engine.

Turns a (likelihood, severity) pair into a numeric score + a named risk band
against a configurable matrix, so two assessors score the same input
identically (the masterplan's "consistent descriptors" bar). Pure-script — no
model judgement: the model only *chooses* likelihood/severity, this script does
the rest (A7 §3.1).

D-02 LOCKED DEFAULT CALIBRATION (cited verbatim by downstream B-skills — do NOT
parameterise the defaults away):

    scoring = "multiply"  (5×5 -> score 1..25, the most common HIRA convention)
    bands   = Low 1-4 / Medium 5-9 / High 10-15 / Critical 16-25

The four band-action strings are LOCKED constants. The A7 §3.1 spec spells the
High string verbatim ("Intolerable — stop / additional controls before
proceeding"); the Low/Medium/Critical strings use the standard HIRA / ALARP
band-action prose consistent with the spec example (recorded in the plan SUMMARY
for competent-person confirmation — see SUMMARY 03-02). `add` mode + custom band
cut-offs/labels remain available via a caller-supplied MatrixConfig.

A bad config raises MatrixConfigError (never silently falls back); a
likelihood/severity outside 1..len(axis) raises ValueError.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


class MatrixConfigError(Exception):
    """A MatrixConfig is malformed: band gap/overlap, out-of-range coverage,
    bad axis length, or unknown scoring mode. Raised instead of a silent
    fallback so an indefensible matrix never reaches a report."""


# --- D-02 LOCKED constants ---------------------------------------------------

# Band-action strings. ONLY "High" is spelled verbatim in the A7 §3.1 spec body;
# the others use standard HIRA/ALARP prose consistent with the spec example and
# are recorded in the plan SUMMARY for competent-person sign-off.
_LOW_ACTION = "Broadly acceptable — monitor / no further action required"
_MEDIUM_ACTION = "Tolerable — reduce risk so far as is reasonably practicable (ALARP)"
_HIGH_ACTION = "Intolerable — stop / additional controls before proceeding"
_CRITICAL_ACTION = "Intolerable — work must not start or continue until risk is reduced"

# Ordered list of {name, min, max, action}. Contiguous, covers the full 1..25
# multiply range of the default 5×5. These exact cut-offs are the locked
# out-of-box calibration.
DEFAULT_BANDS: List[Dict[str, Any]] = [
    {"name": "Low", "min": 1, "max": 4, "action": _LOW_ACTION},
    {"name": "Medium", "min": 5, "max": 9, "action": _MEDIUM_ACTION},
    {"name": "High", "min": 10, "max": 15, "action": _HIGH_ACTION},
    {"name": "Critical", "min": 16, "max": 25, "action": _CRITICAL_ACTION},
]

# Default 5×5 matrix: 5 severity rows + 5 likelihood cols, multiply scoring.
DEFAULT_5X5: Dict[str, Any] = {
    "rows": ["Negligible", "Minor", "Moderate", "Major", "Catastrophic"],   # severity low->high
    "cols": ["Rare", "Unlikely", "Possible", "Likely", "Almost Certain"],    # likelihood low->high
    "scoring": "multiply",
    "bands": [dict(b) for b in DEFAULT_BANDS],
}

# Type alias: a MatrixConfig is just a validated dict in this design.
MatrixConfig = Dict[str, Any]

_VALID_SCORING = ("multiply", "add")


# --- validation --------------------------------------------------------------

def _max_score(scoring: str, n_rows: int, n_cols: int) -> int:
    if scoring == "multiply":
        return n_rows * n_cols
    return n_rows + n_cols  # add


def _min_score(scoring: str) -> int:
    # 1×1 multiply = 1; 1+1 add = 2.
    return 1 if scoring == "multiply" else 2


def load_matrix(config: Optional[MatrixConfig] = None) -> MatrixConfig:
    """Validate (and return) a MatrixConfig. ``None`` -> a deep copy of
    DEFAULT_5X5. Raises MatrixConfigError on any structural fault: bad axis
    length (must be 3..5), unknown scoring mode, empty/malformed bands, a band
    gap or overlap, or bands that do not cover the full score range."""
    if config is None:
        return {
            "rows": list(DEFAULT_5X5["rows"]),
            "cols": list(DEFAULT_5X5["cols"]),
            "scoring": DEFAULT_5X5["scoring"],
            "bands": [dict(b) for b in DEFAULT_5X5["bands"]],
        }

    if not isinstance(config, dict):
        raise MatrixConfigError("MatrixConfig must be a dict")

    rows = config.get("rows")
    cols = config.get("cols")
    scoring = config.get("scoring", "multiply")
    bands = config.get("bands")

    if not isinstance(rows, list) or not isinstance(cols, list):
        raise MatrixConfigError("MatrixConfig requires 'rows' and 'cols' lists")
    if not (3 <= len(rows) <= 5) or not (3 <= len(cols) <= 5):
        raise MatrixConfigError(
            f"axis lengths must be 3..5 (got rows={len(rows)}, cols={len(cols)})"
        )
    if scoring not in _VALID_SCORING:
        raise MatrixConfigError(
            f"unknown scoring mode {scoring!r}; supported: {_VALID_SCORING}"
        )
    if not isinstance(bands, list) or not bands:
        raise MatrixConfigError("MatrixConfig requires a non-empty 'bands' list")

    _validate_bands(bands, scoring, len(rows), len(cols))
    return {
        "rows": list(rows),
        "cols": list(cols),
        "scoring": scoring,
        "bands": [dict(b) for b in bands],
    }


def _validate_bands(
    bands: List[Dict[str, Any]], scoring: str, n_rows: int, n_cols: int
) -> None:
    lo = _min_score(scoring)
    hi = _max_score(scoring, n_rows, n_cols)

    parsed: List[Dict[str, Any]] = []
    for band in bands:
        if not isinstance(band, dict):
            raise MatrixConfigError("each band must be a dict")
        for key in ("name", "min", "max", "action"):
            if key not in band:
                raise MatrixConfigError(f"band missing required key {key!r}: {band}")
        if not isinstance(band["min"], int) or not isinstance(band["max"], int):
            raise MatrixConfigError(f"band min/max must be ints: {band}")
        if band["min"] > band["max"]:
            raise MatrixConfigError(f"band min > max: {band}")
        parsed.append(band)

    parsed.sort(key=lambda b: b["min"])

    # Must start at the minimum score and end at the maximum score.
    if parsed[0]["min"] != lo:
        raise MatrixConfigError(
            f"bands must start at min score {lo} (got {parsed[0]['min']})"
        )
    if parsed[-1]["max"] != hi:
        raise MatrixConfigError(
            f"bands must cover up to max score {hi} (got {parsed[-1]['max']})"
        )

    # Contiguous, no gap, no overlap: each band starts exactly one above the
    # previous band's max.
    for prev, cur in zip(parsed, parsed[1:]):
        if cur["min"] != prev["max"] + 1:
            raise MatrixConfigError(
                f"bands must be contiguous (no gap/overlap): "
                f"{prev['name']}..{prev['max']} then {cur['name']} from {cur['min']}"
            )


# --- scoring -----------------------------------------------------------------

def _band_for(matrix: MatrixConfig, raw_score: int) -> Dict[str, Any]:
    for band in matrix["bands"]:
        if band["min"] <= raw_score <= band["max"]:
            return band
    # Unreachable for a validated matrix — coverage is checked at load time.
    raise MatrixConfigError(f"no band covers score {raw_score}")


def score(
    likelihood: int, severity: int, matrix: Optional[MatrixConfig] = None
) -> Dict[str, Any]:
    """Score a (likelihood, severity) pair against ``matrix`` (default
    DEFAULT_5X5). Returns a JSON-serialisable dict:

        {"likelihood", "severity", "score", "band", "band_action", "matrix_size"}

    Likelihood/severity outside 1..len(axis) raises ValueError. Pure — no
    file/network/env access."""
    cfg = load_matrix(matrix if matrix is not None else DEFAULT_5X5)
    n_cols = len(cfg["cols"])   # likelihood axis
    n_rows = len(cfg["rows"])   # severity axis

    if not isinstance(likelihood, int) or not isinstance(severity, int):
        raise ValueError("likelihood and severity must be integers")
    if not (1 <= likelihood <= n_cols):
        raise ValueError(
            f"likelihood {likelihood} out of range 1..{n_cols}"
        )
    if not (1 <= severity <= n_rows):
        raise ValueError(f"severity {severity} out of range 1..{n_rows}")

    if cfg["scoring"] == "multiply":
        raw = likelihood * severity
    else:  # add
        raw = likelihood + severity

    band = _band_for(cfg, raw)
    return {
        "likelihood": likelihood,
        "severity": severity,
        "score": raw,
        "band": band["name"],
        "band_action": band["action"],
        "matrix_size": f"{n_cols}x{n_rows}",
    }


def residual_delta(initial: Dict[str, Any], residual: Dict[str, Any]) -> Dict[str, Any]:
    """Describe the movement from an initial (pre-control) score to a residual
    (post-control) score. Both args are ``score()`` result dicts. Returns the
    score delta, the band movement, and whether the controls reduced risk."""
    for label, d in (("initial", initial), ("residual", residual)):
        if not isinstance(d, dict) or "score" not in d or "band" not in d:
            raise ValueError(f"{label} must be a score() result dict")

    delta = residual["score"] - initial["score"]
    return {
        "initial_score": initial["score"],
        "residual_score": residual["score"],
        "score_delta": delta,
        "initial_band": initial["band"],
        "residual_band": residual["band"],
        "reduced": delta < 0,
        "band_changed": initial["band"] != residual["band"],
    }


__all__ = [
    "MatrixConfig",
    "MatrixConfigError",
    "DEFAULT_BANDS",
    "DEFAULT_5X5",
    "load_matrix",
    "score",
    "residual_delta",
]
