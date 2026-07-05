"""QA-02 — the canonical HSE rubric shape + the migrated proving fixture.

Wave-0 RED stub (Plan 03-04, Task 1). Pins A8 §4.2:

  * template/evals/rubric.yaml defines EXACTLY the 5 gating HSE dimensions
    (specificity, hierarchy_of_controls, defensibility, de_identification,
    regulatory_citation_accuracy), each at equal weight 0.20;
  * de_identification carries a LEAK hard-fail; regulatory_citation_accuracy
    carries a BELOW-4 hard-fail (the two distinct hard-fail dimensions);
  * the gate is weighted_mean_min == 4.0;
  * analyzer_model is the "most-capable-model" ALIAS (not a literal model id —
    run_evals.py resolves it in Plan 05, D-03);
  * examples/risk-assessment/evals/evals.json is MIGRATED to the canonical
    skill-creator schema (top-level evals[] each with query + files +
    expected_behavior + expectations[]); the bespoke {id,dimension,prompt,expect}
    format is gone.

Extended in v1.3 (Plan 18-03, FND-03 / D-18 / D-19):

  * a REPORTED-ONLY sixth dimension `completeness` (weight 0.0,
    reported_only: true, penalty anchors at 5/4/2/1 — no "3") that MUST stay
    outside the gating weighted mean;
  * every skills/*/evals/rubric.yaml is BYTE-IDENTICAL to the template
    (stamp_rubric.py enumeration: examples/ + skills/hse-skill-forge excluded,
    D-21) — re-stamp drift is a pytest failure;
  * the frozen examples/risk-assessment rubric is deliberately NOT re-stamped.
"""

import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent.parent
RUBRIC = REPO / "template" / "evals" / "rubric.yaml"
EVALS = REPO / "examples" / "risk-assessment" / "evals" / "evals.json"
FROZEN_EXAMPLE_RUBRIC = REPO / "examples" / "risk-assessment" / "evals" / "rubric.yaml"

# scripts/tests/test_rubric.py -> repo/scripts on sys.path for `stamp_rubric`.
SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import stamp_rubric  # noqa: E402

EXPECTED_DIMS = {
    "specificity",
    "hierarchy_of_controls",
    "defensibility",
    "de_identification",
    "regulatory_citation_accuracy",
    "completeness",
}

# The reported-only dims (D-18): present in the rubric, scored + displayed,
# NEVER counted in the gating weighted mean (run_evals.py REPORTED_ONLY_DIMS
# is the enforcing half, Plan 18-01).
REPORTED_ONLY_DIMS = {"completeness"}

# D-21: the frozen examples/risk-assessment rubric is the sole legitimate
# outlier — stamp_rubric.py must never touch it. md5 pinned from the v1.0
# frozen bytes (Phase-18 RESEARCH §3).
FROZEN_EXAMPLE_RUBRIC_MD5 = "9be5288af2262aafa135fdbffe78d9a8"


def _load_rubric():
    assert RUBRIC.is_file(), "template/evals/rubric.yaml not authored yet (Task 3)"
    return yaml.safe_load(RUBRIC.read_text(encoding="utf-8"))


def _dims(rubric):
    return {d["name"]: d for d in rubric["dimensions"]}


# --- rubric shape --------------------------------------------------------------

def test_rubric_has_exactly_the_six_hse_dimensions():
    dims = _dims(_load_rubric())
    assert set(dims) == EXPECTED_DIMS, f"dimension set mismatch: {set(dims)}"


def test_each_gating_dimension_is_equal_weight_0_20():
    dims = _dims(_load_rubric())
    for name, d in dims.items():
        if name in REPORTED_ONLY_DIMS:
            # Reported-only dims carry weight 0.0 — they must not dilute the
            # five gating dims' equal 0.20 shares (D-18).
            assert d["weight"] == pytest.approx(0.0), (
                f"{name} is reported-only and must be weight 0.0: {d['weight']}"
            )
            continue
        assert d["weight"] == pytest.approx(0.20), f"{name} weight != 0.20: {d['weight']}"


def test_de_identification_carries_a_leak_hard_fail():
    d = _dims(_load_rubric())["de_identification"]
    assert d.get("hard_fail"), "de_identification must carry a hard_fail"
    blob = json.dumps(d).lower()
    assert "leak" in blob, "de_identification hard_fail must be a LEAK auto-fail"


def test_citation_accuracy_carries_a_below_4_hard_fail():
    d = _dims(_load_rubric())["regulatory_citation_accuracy"]
    assert d.get("hard_fail"), "regulatory_citation_accuracy must carry a hard_fail"
    blob = json.dumps(d).lower()
    assert "4" in blob, "regulatory_citation_accuracy hard_fail must be a below-4 fail"


def test_two_distinct_hard_fail_dimensions():
    dims = _dims(_load_rubric())
    hard = {n for n, d in dims.items() if d.get("hard_fail")}
    assert hard == {"de_identification", "regulatory_citation_accuracy"}, hard


def test_gate_weighted_mean_min_is_4_0():
    rubric = _load_rubric()
    gate = rubric.get("gate", rubric)
    assert gate.get("weighted_mean_min") == pytest.approx(4.0), rubric


def test_analyzer_model_is_the_most_capable_model_alias():
    rubric = _load_rubric()
    assert rubric.get("analyzer_model") == "most-capable-model", (
        "analyzer_model must be the alias, not a literal model id (D-03)"
    )


# --- v1.3: the reported-only completeness dimension (FND-03, D-18/D-19) ---------

def test_completeness_is_reported_only():
    dims = _dims(_load_rubric())
    c = dims["completeness"]
    assert c.get("reported_only") is True, (
        "completeness must carry the machine-readable reported_only: true marker"
    )
    assert not c.get("hard_fail"), "completeness must NOT be a hard-fail dimension"
    assert c["weight"] == pytest.approx(0.0), (
        f"completeness must be weight 0.0 (outside the gate): {c['weight']}"
    )
    # The gating set is exactly the original five — completeness is NOT in it,
    # and the gating weights still sum to 1.0 (the >=4.0 gate is unmoved).
    gating = {n for n, d in dims.items() if not d.get("reported_only")}
    assert "completeness" not in gating
    assert gating == EXPECTED_DIMS - REPORTED_ONLY_DIMS, gating
    assert sum(dims[n]["weight"] for n in gating) == pytest.approx(1.0)


def test_completeness_penalty_anchors_are_5_4_2_1():
    c = _dims(_load_rubric())["completeness"]
    anchors = {str(k) for k in c["anchors"]}
    assert anchors == {"5", "4", "2", "1"}, (
        f"completeness anchors must be exactly 5/4/2/1 (no '3', D-19): {anchors}"
    )


# --- v1.3: byte-canonical re-stamp (stamp_rubric.py, RESEARCH §3) ----------------

def test_all_skill_rubrics_are_byte_identical_to_template():
    """Every stamp target equals the template byte-for-byte.

    Enumeration comes from stamp_rubric.iter_targets so the test and the
    re-stamp CLI can never diverge (examples/ + skills/hse-skill-forge
    excluded, D-21). Drift here means someone edited the template (or a copy)
    without running `scripts/stamp_rubric.py --write`.
    """
    targets = stamp_rubric.iter_targets(REPO)
    assert len(targets) >= 90, (
        f"suspiciously few stamp targets ({len(targets)}) — glob broken?"
    )
    assert all(
        "examples" not in t.parts and "hse-skill-forge" not in t.parts
        for t in targets
    ), "the stamp enumeration must exclude examples/ and hse-skill-forge (D-21)"
    canonical = RUBRIC.read_bytes()
    drifted = [
        str(t.relative_to(REPO)) for t in targets if t.read_bytes() != canonical
    ]
    assert drifted == [], (
        f"rubric drift — run `scripts/stamp_rubric.py --write`: {drifted}"
    )


def test_frozen_example_rubric_is_not_restamped():
    """D-21: the frozen examples/risk-assessment rubric stays byte-unchanged."""
    md5 = hashlib.md5(FROZEN_EXAMPLE_RUBRIC.read_bytes()).hexdigest()
    assert md5 == FROZEN_EXAMPLE_RUBRIC_MD5, (
        "the frozen examples/risk-assessment/evals/rubric.yaml was modified — "
        "it is the D-21 exempt outlier and must never be re-stamped"
    )


# --- the migrated proving fixture ----------------------------------------------

def test_evals_json_is_canonical_schema():
    data = json.loads(EVALS.read_text(encoding="utf-8"))
    evals = data["evals"]
    assert isinstance(evals, list) and evals, "evals[] must be a non-empty list"
    for e in evals:
        assert "query" in e, f"eval missing query: {e}"
        assert "files" in e and isinstance(e["files"], list), f"eval missing files[]: {e}"
        assert "expected_behavior" in e, f"eval missing expected_behavior: {e}"
        assert "expectations" in e and isinstance(e["expectations"], list) and e["expectations"], (
            f"eval missing expectations[]: {e}"
        )


def test_no_bespoke_eval_format_remains():
    data = json.loads(EVALS.read_text(encoding="utf-8"))
    for e in data["evals"]:
        assert "prompt" not in e, "bespoke 'prompt' key must be gone (use 'query')"
        assert "dimension" not in e, "bespoke 'dimension' key must be gone"
        assert "expect" not in e, "bespoke 'expect' key must be gone (use 'expected_behavior')"
