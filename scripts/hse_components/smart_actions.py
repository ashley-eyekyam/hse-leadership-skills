"""
smart_actions.py — SMART corrective/preventive-action validator/tracker
*(prompt+script)*.

Validates that every action is **S**pecific, **M**easurable, **A**ssignable
(named owner), **R**elevant (traced to a cause), **T**ime-bound (a real ISO due
date) — the masterplan's "SMART corrective actions (owners/dates)" bar and the
§20 eval "every CAPA has owner + due date" (A7 §3.4). Consumed by B5
incident-investigation and B7 capa-manager.

The model authors the action TEXT; this script enforces the RULES: a named
non-placeholder owner, a valid ISO-8601 due date (no vague "ASAP"), a measurable
element, and cause-traceability. All-stdlib date parsing via
``datetime.date.fromisoformat`` — which rejects "ASAP"/"TBD"/"31/07/2026" for
free.

Pure on inputs (no file/network/env access).
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List

# Required fields (§3.4 config surface). ``links_to_cause`` ties each action to
# an rca.py cause id — enforcing "every CAPA traces to a cause".
REQUIRED_FIELDS = ["action", "owner", "due", "measure", "links_to_cause"]

# Owner values that are present-but-meaningless → treated as missing (no
# anonymous actions; defensibility).
_PLACEHOLDER_OWNERS = {"", "tbd", "tba", "n/a", "na", "none", "?", "-", "unassigned"}


def _is_present(value: Any) -> bool:
    """A field counts as present iff it is a non-empty, non-whitespace string."""
    return isinstance(value, str) and value.strip() != ""


def _owner_ok(value: Any) -> bool:
    if not _is_present(value):
        return False
    return value.strip().lower() not in _PLACEHOLDER_OWNERS


def _due_iso_ok(value: Any) -> bool:
    """True iff ``value`` is a valid ISO-8601 calendar date. ``date.fromisoformat``
    rejects "ASAP", "TBD", and locale formats like "31/07/2026" — exactly the
    vague/ malformed dates we must refuse."""
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value.strip())
    except ValueError:
        return False
    return True


def validate_action(action: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single action dict.

    Returns ``{"valid": bool, "missing": [field, ...], "due_iso_ok": bool}``.
    A field is "missing" when absent, empty, a placeholder owner, or — for
    ``due`` — not a valid ISO date.
    """
    if not isinstance(action, dict):
        raise ValueError("action must be a dict")

    missing: List[str] = []

    if not _is_present(action.get("action")):
        missing.append("action")
    if not _owner_ok(action.get("owner")):
        missing.append("owner")

    due_iso_ok = _due_iso_ok(action.get("due"))
    if not due_iso_ok:
        missing.append("due")

    if not _is_present(action.get("measure")):
        missing.append("measure")
    if not _is_present(action.get("links_to_cause")):
        missing.append("links_to_cause")

    return {
        "valid": not missing,
        "missing": missing,
        "due_iso_ok": due_iso_ok,
    }


def validate_register(actions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Validate a whole action register.

    Returns ``{"total", "valid", "invalid": [{"index", "missing"} ...],
    "all_traced_to_cause": bool}``. ``all_traced_to_cause`` is True iff every
    action has a non-empty ``links_to_cause`` (the register-level CAPA-traceability
    gate).
    """
    if not isinstance(actions, list):
        raise ValueError("actions must be a list of action dicts")

    valid_count = 0
    invalid: List[Dict[str, Any]] = []
    all_traced = True

    for idx, action in enumerate(actions):
        result = validate_action(action)
        if result["valid"]:
            valid_count += 1
        else:
            invalid.append({"index": idx, "missing": result["missing"]})
        if "links_to_cause" in result["missing"]:
            all_traced = False

    return {
        "total": len(actions),
        "valid": valid_count,
        "invalid": invalid,
        "all_traced_to_cause": all_traced if actions else False,
    }


def days_until_due(due_iso: str, today_iso: str) -> int:
    """Whole days from ``today_iso`` to ``due_iso`` (both ISO-8601 dates).

    Positive = due in the future; zero = due today; negative = overdue. Raises
    ValueError on a malformed date (no silent zero that would hide an overdue
    action).
    """
    try:
        due = date.fromisoformat(str(due_iso).strip())
        today = date.fromisoformat(str(today_iso).strip())
    except ValueError as exc:
        raise ValueError(f"dates must be ISO-8601 (YYYY-MM-DD): {exc}") from exc
    return (due - today).days


__all__ = [
    "REQUIRED_FIELDS",
    "validate_action",
    "validate_register",
    "days_until_due",
]
