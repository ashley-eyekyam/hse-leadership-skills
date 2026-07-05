"""Regression pins for the D-18 reported-only completeness wiring (FND-03).

Three invariants, all keyless and hazard-content-free:

  (a) the weighted >=4.0 gate mean is INVARIANT to `completeness` — driven
      through the ACTUAL run_evals mean path (grade_case with a monkeypatched
      model grader), not a re-implementation. If anyone re-adds completeness to
      the gating mean (e.g. reverts to a mean over all of `scores`), the
      with-completeness record's mean shifts and this test goes RED;
  (b) the dim-tuple structure: REPORTED_ONLY_DIMS == ("completeness",) and
      `completeness` is absent from MODEL_GRADED_DIMS (which stays the
      unchanged three-dim gate);
  (c) the D-11 structural path: a skill whose NAME is in
      POLICY_SENSITIVE_GRADER_EXEMPT still yields a POPULATED deterministic
      completeness record while its model_grade.scored is False. Proven via a
      SYNTHETIC benign fixture dir + the exempt-set membership branch ONLY —
      no hazard golden is read (D-11 guardrail).

Also pins the prohibitions: a missing-everything completeness record leaves
`hard_fail` False (completeness never enters the hard-fail expression).
"""

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_evals  # noqa: E402

_RUBRIC = {
    "dimensions": [
        {"name": "specificity"},
        {"name": "hierarchy_of_controls"},
        {"name": "defensibility"},
        {"name": "completeness"},
    ],
    "gate": {"weighted_mean_min": 4.0},
}

# A clean, benign OUTPUT artifact: role labels only, ranked HoC, no identifier,
# no date, no KB-id — passes the deterministic de-id + citation gates.
_BENIGN_OUTPUT = """\
# Risk Assessment — benign regression fixture

Hierarchy of controls (ranked):
1. Elimination: remove the task step entirely.
2. Engineering: guard the point of operation.
3. Administrative: permit-to-work with a trained standby.
4. PPE: last layer only, justified.

Residual risk re-scored after controls. Actions assigned to the Supervisor.
Training records are maintained per role. The next review is scheduled
quarterly. Each action owner is a named role.
"""

# Synthetic mode-keyed sme-review frontmatter (benign structural fixture — the
# floor anchors match _BENIGN_OUTPUT phrases).
_SME_FM = """---
sme-review:
  personas:
    - Reviewer
modes:
  default:
    detected_by: always
    floor:
      - id: training-records
        description: "training records section"
        anchors: ["training records"]
        min_matches: 1
      - id: review-date
        description: "next review stated"
        anchors: ["next review"]
        min_matches: 1
      - id: owner-assignment
        description: "named role owner for each action"
        anchors: ["action owner"]
        min_matches: 1
---
body
"""


def _make_skill_dir(tmp_path, name, *, sme_fm=None, output=_BENIGN_OUTPUT):
    skill_dir = tmp_path / name
    (skill_dir / "evals" / "output").mkdir(parents=True)
    (skill_dir / "evals" / "output" / "case.md").write_text(output, encoding="utf-8")
    if sme_fm is not None:
        (skill_dir / "references").mkdir(parents=True)
        (skill_dir / "references" / "sme-review.md").write_text(
            sme_fm, encoding="utf-8")
    case = {"query": "q", "output_files": ["evals/output/case.md"]}
    return skill_dir, case


def _graded_record(monkeypatch, tmp_path, name, scores):
    """Drive grade_case through the ACTUAL mean path with stubbed model scores."""
    skill_dir, case = _make_skill_dir(tmp_path, name)
    monkeypatch.setattr(
        run_evals, "run_model_grader",
        lambda *a, **k: {"scored": True, "model": "m", "scores": dict(scores)})
    return run_evals.grade_case(skill_dir, case, _RUBRIC, "m", None)


# --- (a) the gate mean is invariant to completeness -----------------------------

def test_low_completeness_score_leaves_weighted_mean_unchanged(monkeypatch, tmp_path):
    gating = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 5}
    with_comp = _graded_record(monkeypatch, tmp_path, "skill-with-comp",
                               {**gating, "completeness": 1})
    without_comp = _graded_record(monkeypatch, tmp_path, "skill-without-comp",
                                  gating)
    # The deliberately LOW completeness score must not move the mean AT ALL.
    assert with_comp["weighted_mean"] == without_comp["weighted_mean"]
    expected = round(sum(gating.values()) / len(gating), 3)
    assert with_comp["weighted_mean"] == expected  # mean of the 3 gating dims
    # Regression tripwire: a mean over ALL of `scores` would be (5+4+5+1)/4 =
    # 3.75 -> below the 4.0 gate; the structural exclusion keeps this passing.
    assert with_comp["pass"] is True
    assert without_comp["pass"] is True


def test_reported_completeness_is_stashed_under_a_distinct_key(monkeypatch, tmp_path):
    gating = {"specificity": 5, "hierarchy_of_controls": 5, "defensibility": 5}
    record = _graded_record(monkeypatch, tmp_path, "skill-reported",
                            {**gating, "completeness": 2})
    assert record["model_grade"]["reported"] == {"completeness": 2}


def test_only_completeness_scored_never_divides_by_zero(monkeypatch, tmp_path):
    # Pathological: the model returns ONLY the reported-only dim. The gating
    # mean has nothing to iterate -> no crash, mean None, deterministic verdict
    # stands.
    record = _graded_record(monkeypatch, tmp_path, "skill-only-comp",
                            {"completeness": 1})
    assert record["weighted_mean"] is None
    assert record["pass"] is True


# --- (b) the dim tuples ----------------------------------------------------------

def test_reported_only_dims_tuple():
    assert run_evals.REPORTED_ONLY_DIMS == ("completeness",)


def test_completeness_absent_from_model_graded_dims():
    assert "completeness" not in run_evals.MODEL_GRADED_DIMS
    assert run_evals.MODEL_GRADED_DIMS == (
        "specificity", "hierarchy_of_controls", "defensibility")


# --- (c) D-11: deterministic completeness present / model grade skipped ----------

def test_d11_exempt_skill_gets_deterministic_completeness_not_model_grade(
        monkeypatch, tmp_path):
    name = "lab-biosafety-assessment"
    assert name in run_evals.POLICY_SENSITIVE_GRADER_EXEMPT  # membership branch
    skill_dir, case = _make_skill_dir(tmp_path, name, sme_fm=_SME_FM)
    case["mode"] = "default"

    def boom(*a, **k):
        raise AssertionError(
            "model grader must NOT run for a D-11 grader-exempt skill")

    monkeypatch.setattr(run_evals, "run_model_grader", boom)
    record = run_evals.grade_case(skill_dir, case, _RUBRIC, "m", None)

    # Model grade skipped (D-11 a-priori exemption)...
    assert record["model_grade"]["scored"] is False
    assert "model-grader-exempt" in record["model_grade"]["reason"]
    # ...but the DETERMINISTIC completeness record is POPULATED — the six get
    # their completeness signal from this record only.
    comp = record["deterministic"]["completeness"]
    assert comp["scored"] is True
    assert comp["mode"] == "default"
    assert comp["floor_total"] == 3
    assert comp["coverage_pct"] == 1.0
    assert record["pass"] is True


# --- prohibition pin: completeness never influences hard_fail --------------------

def test_missing_everything_completeness_leaves_hard_fail_false(monkeypatch, tmp_path):
    # An output covering NONE of the floor: completeness reports 0% coverage,
    # yet hard_fail stays False (the expression is deid/citation ONLY).
    skill_dir, case = _make_skill_dir(
        tmp_path, "skill-zero-coverage", sme_fm=_SME_FM,
        output="A short benign note that matches no floor anchor at all.\n")
    case["mode"] = "default"
    monkeypatch.setattr(run_evals, "_model_available", lambda: False)  # CI path
    record = run_evals.grade_case(skill_dir, case, _RUBRIC, "m", None)

    comp = record["deterministic"]["completeness"]
    assert comp["scored"] is True
    assert comp["coverage_pct"] == 0.0
    assert len(comp["missing"]) == 3
    assert record["deterministic"]["hard_fail"] is False  # never gated (D-18)
    assert record["pass"] is True


def test_modeless_case_completeness_noop_in_grade_case(monkeypatch, tmp_path):
    # A case WITHOUT a mode: key (all 94 shipped skills today) -> the record is
    # the back-compat no-op, nothing else changes.
    skill_dir, case = _make_skill_dir(tmp_path, "skill-modeless")
    monkeypatch.setattr(run_evals, "_model_available", lambda: False)
    record = run_evals.grade_case(skill_dir, case, _RUBRIC, "m", None)
    comp = record["deterministic"]["completeness"]
    assert comp["scored"] is False
    assert comp["reason"] == "no modes declared"
    assert record["deterministic"]["hard_fail"] is False
    assert record["pass"] is True
