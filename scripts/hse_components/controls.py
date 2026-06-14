"""
controls.py — hierarchy-of-controls generator/validator *(prompt+script)*.

Given the controls the model proposed, deterministically RANK them by the
hierarchy of controls and FLAG any treatment that is PPE/admin-only without a
higher-order justification — the pack's core defensibility lever (A7 §3.2,
masterplan §16/§20 ``hierarchy_of_controls`` rubric dimension).

A7↔A3 boundary (§1, §6 AC9): this module contains NO canonical prompt prose —
the *instruction* that tells the model to rank Elimination→…→PPE lives in
``KB-SNIP-HOC`` (A3). Here is ONLY the deterministic ranking/flagging logic: the
model owns *what* the controls are; the script owns the tier maths + the flag
that feeds the eval rubric and a skill's self-check loop.

Pure on inputs (no file/network/env access). Stdlib only.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

# --- Fixed hierarchy (a standard, NOT org-configurable — §3.2 config surface) -
# Highest-order (most effective) first → lowest-order (least effective) last.
HIERARCHY: List[str] = [
    "elimination",
    "substitution",
    "engineering",
    "administrative",
    "ppe",
]

# rank int 1..5 for each tier (elimination = 1, ppe = 5).
_RANK = {name: i + 1 for i, name in enumerate(HIERARCHY)}

# A treatment made up only of these tiers is "PPE/admin-only" and must be flagged
# unless higher-order controls are justified as not reasonably practicable.
_ADMIN_PPE = {"administrative", "ppe"}

# LOCKED verbatim flag strings (§3.2). Downstream skills + the eval rubric match
# these byte-for-byte — do NOT reword.
PPE_ADMIN_ONLY_FLAG = (
    "PPE/admin-only — justify why higher-order controls aren't reasonably practicable"
)
NO_CONTROLS_FLAG = "no controls proposed"

# Keyword heuristic used ONLY as a safety net when the model's declared_type is
# absent or unrecognised (§3.2: "falls back to a keyword heuristic only as a
# safety net"). Checked highest-order first so the strongest matching tier wins.
_KEYWORDS = {
    "elimination": ("eliminat", "remove the", "avoid the", "do not "),
    "substitution": ("substitut", "replace", "non-hazardous", "less hazardous", "lower-hazard"),
    "engineering": (
        "guard", "barrier", "ventilation", "interlock", "enclos", "isolat",
        "extraction", "lev", "fume", "engineer", "fixed ",
    ),
    "administrative": (
        "procedure", "training", "permit", "toolbox", "signage", "sign ",
        "rotation", "supervis", "policy", "instruction", "warning", "induction",
    ),
    "ppe": (
        "ppe", "respirator", "glove", "goggle", "hard hat", "helmet", "hi-vis",
        "harness", "ear plug", "earplug", "ear defender", "mask", "boots",
        "face shield", "protective",
    ),
}


def classify(control_text: str, declared_type: Optional[str] = None) -> str:
    """Return the hierarchy tier (one of ``HIERARCHY``) for a control.

    Resolution order (§3.2):
      1. the model-``declared_type`` when it is a recognised tier;
      2. otherwise a keyword heuristic over ``control_text``;
      3. otherwise ``administrative`` — the most conservative *non-PPE* fallback
         (an unknown control is never silently treated as adequate PPE).
    """
    if declared_type is not None:
        dt = str(declared_type).strip().lower()
        if dt in _RANK:
            return dt

    text = (control_text or "").lower()
    for tier in HIERARCHY:  # highest-order first → strongest match wins
        for kw in _KEYWORDS[tier]:
            if kw in text:
                return tier

    # Conservative default: never PPE (which would understate the treatment).
    return "administrative"


def rank_controls(controls: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Rank a list of ``{"control": str, "type"?: str}`` items by the hierarchy.

    Returns a JSON-serialisable dict:

        {"ranked": [{"control", "type", "rank"} ...],   # highest-order first
         "highest_order": str | None,
         "ppe_admin_only": bool,    # True iff every control is admin/ppe
         "flag": None | NO_CONTROLS_FLAG | PPE_ADMIN_ONLY_FLAG}

    Deterministic: a stable sort by (rank, original index) keeps equal-tier
    controls in input order, so identical input yields identical output.
    """
    if not isinstance(controls, list):
        raise ValueError("controls must be a list of {control, type} dicts")

    if not controls:
        return {
            "ranked": [],
            "highest_order": None,
            "ppe_admin_only": False,
            "flag": NO_CONTROLS_FLAG,
        }

    enriched: List[Dict[str, Any]] = []
    for idx, item in enumerate(controls):
        if not isinstance(item, dict):
            raise ValueError(f"each control must be a dict (got {type(item).__name__})")
        tier = classify(item.get("control", ""), item.get("type"))
        enriched.append(
            {
                "control": item.get("control", ""),
                "type": tier,
                "rank": _RANK[tier],
                "_idx": idx,
            }
        )

    enriched.sort(key=lambda c: (c["rank"], c["_idx"]))
    ranked = [{"control": c["control"], "type": c["type"], "rank": c["rank"]} for c in enriched]

    highest_order = ranked[0]["type"]
    ppe_admin_only = all(c["type"] in _ADMIN_PPE for c in ranked)
    flag = PPE_ADMIN_ONLY_FLAG if ppe_admin_only else None

    return {
        "ranked": ranked,
        "highest_order": highest_order,
        "ppe_admin_only": ppe_admin_only,
        "flag": flag,
    }


def validate_treatment(controls: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Rubric-aligned pass/flag over a proposed treatment.

    A treatment PASSES when at least one higher-order (non admin/PPE) control is
    present; it is FLAGGED when the treatment is empty or PPE/admin-only. Returns
    ``{"passed", "ppe_admin_only", "highest_order", "flag", "ranked"}`` — the
    ``flag`` is the verbatim §3.2 string so the eval rubric can match it.
    """
    ranked = rank_controls(controls)
    passed = ranked["flag"] is None
    return {
        "passed": passed,
        "ppe_admin_only": ranked["ppe_admin_only"],
        "highest_order": ranked["highest_order"],
        "flag": ranked["flag"],
        "ranked": ranked["ranked"],
    }


__all__ = [
    "HIERARCHY",
    "PPE_ADMIN_ONLY_FLAG",
    "NO_CONTROLS_FLAG",
    "classify",
    "rank_controls",
    "validate_treatment",
]
