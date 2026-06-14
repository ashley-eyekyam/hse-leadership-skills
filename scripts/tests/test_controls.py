"""COMP-02 — controls.py hierarchy-of-controls ranker/validator.

Durable contract test (A7 §3.2 / §3.8) over the on-disk engine:

  (a) an all-PPE/admin control list sets rank_controls ppe_admin_only=True with
      the verbatim §3.2 flag string;
  (b) adding an engineering control clears the flag (ppe_admin_only=False,
      flag=None);
  (c) the ranked output follows the fixed HIERARCHY (elimination first, ppe
      last), each with a rank int;
  (d) an empty list flags "no controls proposed";
  (e) rank_controls is deterministic — identical input yields identical output.

Bare imports resolve via scripts/tests/conftest.py (puts hse_components on
sys.path). The A8 quality harness (Plan 04) keys off this durable test.
"""

import copy

import pytest

from controls import (
    HIERARCHY,
    classify,
    rank_controls,
    validate_treatment,
)

PPE_ADMIN_FLAG = (
    "PPE/admin-only — justify why higher-order controls aren't reasonably practicable"
)
NO_CONTROLS_FLAG = "no controls proposed"


def test_all_ppe_admin_sets_flag():
    controls = [
        {"control": "Hi-vis vests and hard hats", "type": "ppe"},
        {"control": "Toolbox talk on traffic routes", "type": "administrative"},
    ]
    out = rank_controls(controls)
    assert out["ppe_admin_only"] is True
    assert out["flag"] == PPE_ADMIN_FLAG


def test_engineering_control_clears_flag():
    controls = [
        {"control": "Hi-vis vests", "type": "ppe"},
        {"control": "Physical barrier separating plant from pedestrians", "type": "engineering"},
    ]
    out = rank_controls(controls)
    assert out["ppe_admin_only"] is False
    assert out["flag"] is None
    assert out["highest_order"] == "engineering"


def test_ranked_order_follows_hierarchy():
    controls = [
        {"control": "Gloves", "type": "ppe"},
        {"control": "Remove the task entirely", "type": "elimination"},
        {"control": "Permit-to-work", "type": "administrative"},
        {"control": "Local exhaust ventilation", "type": "engineering"},
        {"control": "Use a non-hazardous solvent", "type": "substitution"},
    ]
    out = rank_controls(controls)
    ranked_types = [c["type"] for c in out["ranked"]]
    assert ranked_types == HIERARCHY  # elimination..ppe, in hierarchy order
    # each ranked entry carries an ascending rank int 1..5
    ranks = [c["rank"] for c in out["ranked"]]
    assert ranks == [1, 2, 3, 4, 5]
    assert out["highest_order"] == "elimination"


def test_empty_list_flags_no_controls():
    out = rank_controls([])
    assert out["flag"] == NO_CONTROLS_FLAG
    assert out["ranked"] == []


def test_classify_uses_declared_type_then_heuristic():
    # declared type wins
    assert classify("anything at all", declared_type="engineering") == "engineering"
    # unknown declared type falls back to text heuristic / conservative default
    assert classify("Provide respirators to all staff") == "ppe"
    assert classify("Eliminate the confined-space entry") == "elimination"
    # unrecognised text → conservative non-PPE default
    assert classify("misc note with no signal") == "administrative"


def test_validate_treatment_flags_ppe_only():
    out = validate_treatment([{"control": "earplugs", "type": "ppe"}])
    assert out["passed"] is False
    assert out["flag"] == PPE_ADMIN_FLAG

    out2 = validate_treatment(
        [{"control": "Enclose the noise source", "type": "engineering"}]
    )
    assert out2["passed"] is True
    assert out2["flag"] is None


def test_rank_controls_is_deterministic():
    controls = [
        {"control": "Gloves", "type": "ppe"},
        {"control": "Guard the pinch point", "type": "engineering"},
    ]
    a = rank_controls(copy.deepcopy(controls))
    b = rank_controls(copy.deepcopy(controls))
    assert a == b
