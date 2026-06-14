"""QA-02 — the canonical HSE rubric shape + the migrated proving fixture.

Wave-0 RED stub (Plan 03-04, Task 1). Pins A8 §4.2:

  * template/evals/rubric.yaml defines EXACTLY the 5 HSE dimensions
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

Fails now: rubric.yaml is a .gitkeep and evals.json is still bespoke.
"""

import json
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent.parent
RUBRIC = REPO / "template" / "evals" / "rubric.yaml"
EVALS = REPO / "examples" / "risk-assessment" / "evals" / "evals.json"

EXPECTED_DIMS = {
    "specificity",
    "hierarchy_of_controls",
    "defensibility",
    "de_identification",
    "regulatory_citation_accuracy",
}


def _load_rubric():
    assert RUBRIC.is_file(), "template/evals/rubric.yaml not authored yet (Task 3)"
    return yaml.safe_load(RUBRIC.read_text(encoding="utf-8"))


def _dims(rubric):
    return {d["name"]: d for d in rubric["dimensions"]}


# --- rubric shape --------------------------------------------------------------

def test_rubric_has_exactly_the_five_hse_dimensions():
    dims = _dims(_load_rubric())
    assert set(dims) == EXPECTED_DIMS, f"dimension set mismatch: {set(dims)}"


def test_each_dimension_is_equal_weight_0_20():
    dims = _dims(_load_rubric())
    for name, d in dims.items():
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
