"""
rca.py — causal-analysis structural scaffold + completeness validator
*(prompt+script)*.

Provides the deterministic STRUCTURE and the systemic-reach RULE for the five
v1.0 RCA methods (A7 §3.3, masterplan §7.1 skill 5):

    5-Whys · ICAM · SCAT · Fishbone (Ishikawa) · Swiss-Cheese (Reason)

The model performs the causal REASONING (what the causes are); this script
guarantees the output has the right shape AND reaches a SYSTEMIC factor — the
§20 eval "RCA reaches a systemic factor, not only individual error".

SPEC-LOCKED CORRECTNESS TRAP (research Pitfall 3 / watchlist): every method
enforces ``reaches_systemic`` with a METHOD-SPECIFIC rule — NOT mere key
presence. A 5-Whys terminating in an individual act, an ICAM with no
Organisational Factor, a SCAT with no Basic Causes / Lack of Control, a Fishbone
with every cause under *Man*, and a Swiss-Cheese with active failures only MUST
all return ``reaches_systemic=False`` (and therefore ``valid=False``). ``valid``
is False whenever ``reaches_systemic`` is False.

Pure on inputs (no file/network/env access). Stdlib only.
"""

from __future__ import annotations

import re
from typing import Any, Callable, Dict, List, Set

METHODS: Set[str] = {"5-whys", "icam", "scat", "fishbone", "swiss-cheese"}

# Default minimum 5-Whys chain depth (§3.3 config surface: min_whys).
DEFAULT_MIN_WHYS = 5

# Fishbone Ishikawa branches (§3.3). reaches_systemic requires a NON-"Man" branch.
FISHBONE_BRANCHES = ["Man", "Machine", "Method", "Material", "Measurement", "Environment"]

# Swiss-Cheese (Reason) defence layers, sharp-end → latent. reaches_systemic
# requires the organisational-influence (latent) layer to be populated.
SWISS_LAYERS = [
    "active_failures",
    "preconditions",
    "supervisory_factors",
    "organisational_influences",
]

# Heuristic: a terminal 5-Whys "why" that still blames an individual act (no
# systemic reach). Matched case-insensitively against the last why.
_INDIVIDUAL_BLAME_RX = re.compile(
    r"\b(careless|negligent|did ?n'?t care|inattentive|lazy|forgot|"
    r"ignored the rules?|complacent|incompeten|reckless|"
    r"failed to (follow|comply)|did ?n'?t (follow|comply))\b",
    re.IGNORECASE,
)


# --- helpers -----------------------------------------------------------------

def _nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and v.strip() != ""


def _nonempty_list(v: Any) -> bool:
    return isinstance(v, list) and len(v) > 0


def _check_method(method: str) -> str:
    if method not in METHODS:
        raise ValueError(f"unknown method {method!r}; supported methods: {sorted(METHODS)}")
    return method


# --- scaffolds ---------------------------------------------------------------

_SCAFFOLDS: Dict[str, Callable[[str], Dict[str, Any]]] = {
    "5-whys": lambda problem: {"problem": problem, "whys": []},
    "icam": lambda problem: {
        "problem": problem,
        "absent_failed_defences": [],
        "individual_team_actions": [],
        "task_environmental_conditions": [],
        "organisational_factors": [],
    },
    "scat": lambda problem: {
        "problem": problem,
        "loss": "",
        "contact": "",
        "immediate_causes": [],
        "basic_causes": [],
        "lack_of_control": [],
    },
    "fishbone": lambda problem: {
        "problem": problem,
        "branches": {b: [] for b in FISHBONE_BRANCHES},
    },
    "swiss-cheese": lambda problem: {
        "problem": problem,
        "layers": {layer: [] for layer in SWISS_LAYERS},
    },
}


def scaffold(method: str, problem: str) -> Dict[str, Any]:
    """Return the empty template with ``method``'s required slots. Unknown method
    raises ValueError naming the supported set."""
    _check_method(method)
    return _SCAFFOLDS[method](problem)


# --- per-method validators ---------------------------------------------------
# Each returns (reaches_systemic: bool, issues: List[str], extra: dict). valid is
# derived centrally as (no issues) AND reaches_systemic.

def _validate_5_whys(analysis: Dict[str, Any], min_whys: int) -> tuple:
    issues: List[str] = []
    whys = analysis.get("whys")
    if not isinstance(whys, list):
        return False, ["'whys' must be a list"], {"depth": 0}
    depth = len(whys)
    if depth < min_whys:
        issues.append(f"chain has {depth} whys; needs >= {min_whys}")
    if any(not _nonempty_str(w) for w in whys):
        issues.append("every why must be a non-empty string")
    # reaches_systemic: terminal why must NOT still blame an individual act.
    terminal = whys[-1] if whys else ""
    terminal_is_individual = bool(_INDIVIDUAL_BLAME_RX.search(terminal or ""))
    reaches_systemic = (depth >= min_whys) and (not terminal_is_individual) and bool(whys) and all(
        _nonempty_str(w) for w in whys
    )
    if terminal_is_individual:
        issues.append("terminal 'why' still blames an individual act — no systemic reach")
    return reaches_systemic, issues, {"depth": depth}


def _validate_icam(analysis: Dict[str, Any]) -> tuple:
    issues: List[str] = []
    cats = (
        "absent_failed_defences",
        "individual_team_actions",
        "task_environmental_conditions",
        "organisational_factors",
    )
    for c in cats:
        if c not in analysis:
            issues.append(f"missing ICAM category '{c}'")
    # reaches_systemic: >= 1 Organisational Factor (the systems layer).
    org = analysis.get("organisational_factors")
    reaches_systemic = _nonempty_list(org) and all(_nonempty_str(x) for x in org)
    if not reaches_systemic:
        issues.append("no Organisational Factor — ICAM has not reached the systemic layer")
    return reaches_systemic, issues, {}


def _validate_scat(analysis: Dict[str, Any]) -> tuple:
    issues: List[str] = []
    for slot in ("loss", "contact"):
        if not _nonempty_str(analysis.get(slot)):
            issues.append(f"missing SCAT slot '{slot}'")
    if not _nonempty_list(analysis.get("immediate_causes")):
        issues.append("missing SCAT 'immediate_causes'")
    basic = analysis.get("basic_causes")
    loc = analysis.get("lack_of_control")
    # reaches_systemic: Basic Causes AND Lack of Control both present (links to
    # management-system failure).
    has_basic = _nonempty_list(basic)
    has_loc = _nonempty_list(loc)
    reaches_systemic = has_basic and has_loc
    if not has_basic:
        issues.append("no Basic Causes — SCAT stops at immediate causes")
    if not has_loc:
        issues.append("no Lack of Control — SCAT has not reached the management system")
    return reaches_systemic, issues, {}


def _validate_fishbone(analysis: Dict[str, Any]) -> tuple:
    issues: List[str] = []
    branches = analysis.get("branches")
    if not isinstance(branches, dict):
        return False, ["'branches' must be a dict of the six Ishikawa categories"], {}
    populated_non_man = []
    for name, causes in branches.items():
        if not _nonempty_list(causes):
            continue
        for c in causes:
            # each populated cause must be non-empty + evidence-referenced.
            if not isinstance(c, dict) or not _nonempty_str(c.get("cause")):
                issues.append(f"branch '{name}' has an empty cause")
            elif not _nonempty_str(c.get("evidence")):
                issues.append(f"cause under '{name}' is not evidence-referenced")
        if name != "Man":
            populated_non_man.append(name)
    # reaches_systemic: at least one non-"Man" branch populated (guards
    # individual-blame bias).
    reaches_systemic = len(populated_non_man) > 0
    if not reaches_systemic:
        issues.append("every cause sits under 'Man' — individual-blame bias, no systemic reach")
    return reaches_systemic, issues, {"populated_non_man_branches": populated_non_man}


def _validate_swiss_cheese(analysis: Dict[str, Any]) -> tuple:
    issues: List[str] = []
    layers = analysis.get("layers")
    if not isinstance(layers, dict):
        return False, ["'layers' must be a dict of the four defence layers"], {}
    for layer, entries in layers.items():
        if not _nonempty_list(entries):
            continue
        for e in entries:
            # each populated layer must name the failed/absent BARRIER.
            if not isinstance(e, dict) or not _nonempty_str(e.get("barrier")):
                issues.append(f"layer '{layer}' is populated but names no failed/absent barrier")
    # reaches_systemic: the organisational-influence (latent) layer populated.
    org_layer = layers.get("organisational_influences")
    reaches_systemic = _nonempty_list(org_layer) and all(
        isinstance(e, dict) and _nonempty_str(e.get("barrier")) for e in org_layer
    )
    if not reaches_systemic:
        issues.append(
            "no organisational-influence latent layer — only sharp-end failures, no systemic reach"
        )
    return reaches_systemic, issues, {}


def validate(method: str, analysis: Dict[str, Any], min_whys: int = DEFAULT_MIN_WHYS) -> Dict[str, Any]:
    """Validate an ``analysis`` against ``method``'s structural + systemic-reach
    rules.

    Returns ``{"method", "valid", "reaches_systemic", "issues", ...extra}``.
    ``valid`` is True iff there are no structural issues AND ``reaches_systemic``
    is True — so ``valid`` is ALWAYS False when ``reaches_systemic`` is False.
    Unknown method raises ValueError naming the supported set; a non-dict analysis
    raises ValueError.
    """
    _check_method(method)
    if not isinstance(analysis, dict):
        raise ValueError("analysis must be a dict")

    if method == "5-whys":
        reaches_systemic, issues, extra = _validate_5_whys(analysis, min_whys)
    elif method == "icam":
        reaches_systemic, issues, extra = _validate_icam(analysis)
    elif method == "scat":
        reaches_systemic, issues, extra = _validate_scat(analysis)
    elif method == "fishbone":
        reaches_systemic, issues, extra = _validate_fishbone(analysis)
    else:  # swiss-cheese
        reaches_systemic, issues, extra = _validate_swiss_cheese(analysis)

    valid = reaches_systemic and not issues
    result = {
        "method": method,
        "valid": valid,
        "reaches_systemic": reaches_systemic,
        "issues": issues,
    }
    result.update(extra)
    return result


__all__ = [
    "METHODS",
    "DEFAULT_MIN_WHYS",
    "FISHBONE_BRANCHES",
    "SWISS_LAYERS",
    "scaffold",
    "validate",
]
