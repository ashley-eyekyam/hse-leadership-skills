"""COMP-04 — smart_actions.py SMART-action validator/tracker.

Durable contract test (A7 §3.4 / §3.8) over the on-disk engine:

  (a) an action missing a named owner is invalid;
  (b) an action with an "ASAP"/malformed due date is invalid (due_iso_ok False);
  (c) an action with no links_to_cause is invalid (untraced);
  (d) a complete action (action, owner, ISO due, measure, links_to_cause) is
      valid;
  (e) validate_register reports total/valid/invalid + all_traced_to_cause;
  (f) days_until_due computes from two ISO dates;
  (g) the validators are deterministic.

ISO-date parsing is stdlib datetime.date.fromisoformat — "ASAP"/"TBD" reject for
free. Bare imports resolve via scripts/tests/conftest.py.
"""

import copy

import pytest

from smart_actions import days_until_due, validate_action, validate_register


def _complete():
    return {
        "action": "Install a fixed guard over the rotating shaft.",
        "owner": "J. Doe",
        "due": "2026-07-31",
        "measure": "Guard fitted and verified by maintenance sign-off.",
        "links_to_cause": "RC-2",
    }


def test_complete_action_valid():
    out = validate_action(_complete())
    assert out["valid"] is True
    assert out["missing"] == []
    assert out["due_iso_ok"] is True


def test_missing_owner_invalid():
    a = _complete()
    del a["owner"]
    out = validate_action(a)
    assert out["valid"] is False
    assert "owner" in out["missing"]


def test_placeholder_owner_invalid():
    a = _complete()
    a["owner"] = "TBD"
    out = validate_action(a)
    assert out["valid"] is False
    assert "owner" in out["missing"]


def test_asap_due_invalid():
    a = _complete()
    a["due"] = "ASAP"
    out = validate_action(a)
    assert out["valid"] is False
    assert out["due_iso_ok"] is False
    assert "due" in out["missing"]


def test_malformed_due_invalid():
    a = _complete()
    a["due"] = "31/07/2026"
    out = validate_action(a)
    assert out["valid"] is False
    assert out["due_iso_ok"] is False


def test_untraced_action_invalid():
    a = _complete()
    del a["links_to_cause"]
    out = validate_action(a)
    assert out["valid"] is False
    assert "links_to_cause" in out["missing"]


def test_validate_register_reports_traceability():
    good = _complete()
    bad = _complete()
    del bad["links_to_cause"]
    out = validate_register([good, bad])
    assert out["total"] == 2
    assert out["valid"] == 1
    assert len(out["invalid"]) == 1
    assert out["all_traced_to_cause"] is False

    out2 = validate_register([_complete(), _complete()])
    assert out2["all_traced_to_cause"] is True
    assert out2["valid"] == 2


def test_days_until_due():
    assert days_until_due("2026-07-31", "2026-07-01") == 30
    assert days_until_due("2026-07-01", "2026-07-31") == -30  # overdue
    assert days_until_due("2026-07-01", "2026-07-01") == 0


def test_validate_action_is_deterministic():
    a = _complete()
    x = validate_action(copy.deepcopy(a))
    y = validate_action(copy.deepcopy(a))
    assert x == y
