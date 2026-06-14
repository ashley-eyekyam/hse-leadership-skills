"""COMP-05 — incident_rates.py TRIR/DART/LTIFR calculator + locked OSHA bases.

This durable contract test re-asserts, over the on-disk engine:

  (a) the locked worked-example anchors hold exactly:
      trir(3, 290_000) == 2.07 and ltifr(6, 1_000_000) == 6.00;
  (b) the OSHA bases are module CONSTANTS (OSHA_BASE 200_000, MILLION_BASE
      1_000_000) — not config;
  (c) fail-loud edges: hours_worked <= 0 raises ValueError for trir/dart/ltifr
      (never a silent 0.0, which would read as "perfect safety"); negative
      counts raise ValueError;
  (d) NO implicit annualization — compute_all does not scale by period;
  (e) compute_all returns all three rates;
  (f) each function is deterministic.

Bare imports resolve via scripts/tests/conftest.py. Stdlib + the engine only.
"""

import json

import pytest

from incident_rates import (
    MILLION_BASE,
    OSHA_BASE,
    compute_all,
    dart,
    ltifr,
    trir,
)


def test_locked_bases_are_constants():
    """OSHA bases are the spec-locked constants (D5 — not configurable)."""
    assert OSHA_BASE == 200_000
    assert MILLION_BASE == 1_000_000


def test_trir_anchor():
    """3 recordables / 290,000 h -> TRIR 2.07 (hand-verified worked example)."""
    assert trir(3, 290_000) == 2.07


def test_ltifr_anchor():
    """6 lost-time injuries / 1,000,000 h -> LTIFR 6.00."""
    assert ltifr(6, 1_000_000) == 6.00


def test_dart_uses_osha_base():
    """DART uses the 200,000-hour OSHA base, same denominator as TRIR."""
    assert dart(3, 290_000) == 2.07


def test_zero_or_negative_hours_raises():
    """hours_worked <= 0 raises ValueError for every rate — never silent 0.0."""
    for fn in (trir, dart, ltifr):
        with pytest.raises(ValueError):
            fn(3, 0)
        with pytest.raises(ValueError):
            fn(3, -290_000)


def test_negative_counts_raise():
    """Negative event counts raise ValueError (defensibility: no impossible rates)."""
    for fn in (trir, dart, ltifr):
        with pytest.raises(ValueError):
            fn(-1, 290_000)


def test_compute_all_returns_three_rates():
    """compute_all returns trir, dart and ltifr for one (counts, hours) input."""
    out = compute_all(
        {"recordables": 3, "dart_cases": 3, "lost_time_injuries": 6},
        290_000,
    )
    assert out["trir"] == 2.07
    assert out["dart"] == 2.07
    assert "ltifr" in out


def test_no_implicit_annualization():
    """A partial-period actual-hours figure is NOT scaled up to a full year.

    With period given but the same hours-to-date, the rate is identical to the
    period-actual computation — compute_all records the figure, it does not
    annualize it.
    """
    base = compute_all({"recordables": 3}, 290_000)
    with_period = compute_all({"recordables": 3}, 290_000, period="H1-2026")
    assert base["trir"] == with_period["trir"] == 2.07


def test_compute_all_is_deterministic():
    """compute_all called twice on the same input yields byte-identical output."""
    counts = {"recordables": 3, "dart_cases": 3, "lost_time_injuries": 6}
    a = json.dumps(compute_all(counts, 290_000), sort_keys=True)
    b = json.dumps(compute_all(counts, 290_000), sort_keys=True)
    assert a == b
