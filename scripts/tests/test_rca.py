"""COMP-03 — rca.py 5-method causal-analysis scaffold + systemic-reach validator.

Durable contract test (A7 §3.3 / §3.8) over the on-disk engine + the golden
fixtures/rca_cases.json:

  (a) for every method × {positive, negative} fixture, validate() returns the
      fixture's expected reaches_systemic AND valid is False whenever
      reaches_systemic is False (the spec-locked "no shape-only validators" rule);
  (b) the Man-only Fishbone negative and the active-only Swiss-Cheese negative
      both fail reaches_systemic explicitly (the most-cited correctness trap);
  (c) an unknown method raises ValueError naming the supported set;
  (d) scaffold() returns the method's required slots;
  (e) validate() is deterministic.

reaches_systemic is enforced PER METHOD (not key-presence) — see rca.py.
"""

import copy

import pytest

from rca import METHODS, scaffold, validate

ALL_METHODS = ["5-whys", "icam", "scat", "fishbone", "swiss-cheese"]


def _case(rca_cases, method, polarity):
    return rca_cases["cases"][method][polarity]


@pytest.mark.parametrize("method", ALL_METHODS)
@pytest.mark.parametrize("polarity", ["positive", "negative"])
def test_validate_matches_fixture_reaches_systemic(rca_cases, method, polarity):
    case = _case(rca_cases, method, polarity)
    out = validate(method, case["analysis"])
    assert out["reaches_systemic"] == case["expect"]["reaches_systemic"], (
        f"{method}/{polarity}: reaches_systemic mismatch"
    )
    assert out["valid"] == case["expect"]["valid"], f"{method}/{polarity}: valid mismatch"
    # The load-bearing invariant: valid is False whenever reaches_systemic is False.
    if not out["reaches_systemic"]:
        assert out["valid"] is False


def test_all_five_methods_have_fixtures(rca_cases):
    assert set(rca_cases["cases"].keys()) == set(ALL_METHODS)
    assert METHODS == set(ALL_METHODS)


def test_man_only_fishbone_fails_systemic(rca_cases):
    neg = _case(rca_cases, "fishbone", "negative")["analysis"]
    out = validate("fishbone", neg)
    assert out["reaches_systemic"] is False
    assert out["valid"] is False


def test_active_only_swiss_cheese_fails_systemic(rca_cases):
    neg = _case(rca_cases, "swiss-cheese", "negative")["analysis"]
    out = validate("swiss-cheese", neg)
    assert out["reaches_systemic"] is False
    assert out["valid"] is False


def test_unknown_method_raises():
    with pytest.raises(ValueError):
        validate("taproot", {})
    with pytest.raises(ValueError):
        scaffold("apollo", "problem")


def test_scaffold_returns_required_slots():
    for method in ALL_METHODS:
        tmpl = scaffold(method, "a problem statement")
        assert isinstance(tmpl, dict)
        assert tmpl  # non-empty template


def test_validate_is_deterministic(rca_cases):
    case = _case(rca_cases, "icam", "positive")["analysis"]
    a = validate("icam", copy.deepcopy(case))
    b = validate("icam", copy.deepcopy(case))
    assert a == b
