"""Regression pins for the TRUE weighted gate mean (18-REVIEW W2).

`grade_case`'s gate mean previously computed an UNWEIGHTED mean over
MODEL_GRADED_DIMS while the field, the log line, and the rubric all said
"weighted" — correct only because the canonical rubric weights every gating
dim equally (0.20). The mean now honours the rubric's declared `weight:` per
dimension via `dim_weights`, so a future rubric retune of any gating weight is
honoured by the gate instead of silently ignored.

Pins, all keyless and hazard-content-free (driven through the ACTUAL
grade_case mean path with a monkeypatched model grader):

  (a) UNEQUAL declared weights move the mean exactly as arithmetic says —
      distinguishable from the old unweighted mean;
  (b) with the canonical template rubric's EQUAL weights the weighted mean
      equals the plain mean (the shipped pilots' gate value is unchanged);
  (c) a rubric with NO weight fields (the synthetic-test shape) defaults every
      dim to an equal share — plain-mean behaviour preserved;
  (d) the reported-only `completeness` dim still CANNOT move the mean, weights
      or not (D-18 structural exclusion is iteration-based, not weight-based);
  (e) `dim_weights` is defensive on junk shapes (non-dict dims, boolean /
      negative / non-numeric weights) — never raises, defaults to 1.0.
"""

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_evals  # noqa: E402

# A benign OUTPUT artifact: role labels only, no identifier/date/KB-id —
# passes the deterministic de-id + citation gates (same shape as the
# reported-only regression fixture).
_BENIGN_OUTPUT = """\
# Benign weighted-mean regression fixture

Hierarchy of controls (ranked):
1. Elimination: remove the task step entirely.
2. Engineering: guard the point of operation.
3. Administrative: permit-to-work with a trained standby.
4. PPE: last layer only, justified.

Residual risk re-scored after controls. Actions assigned to the Supervisor.
"""


def _make_skill_dir(tmp_path, name):
    skill_dir = tmp_path / name
    (skill_dir / "evals" / "output").mkdir(parents=True)
    (skill_dir / "evals" / "output" / "case.md").write_text(
        _BENIGN_OUTPUT, encoding="utf-8")
    case = {"query": "q", "output_files": ["evals/output/case.md"]}
    return skill_dir, case


def _graded_record(monkeypatch, tmp_path, name, rubric, scores):
    skill_dir, case = _make_skill_dir(tmp_path, name)
    monkeypatch.setattr(
        run_evals, "run_model_grader",
        lambda *a, **k: {"scored": True, "model": "m", "scores": dict(scores)})
    return run_evals.grade_case(skill_dir, case, rubric, "m", None)


def _rubric(dims, gate=4.0):
    return {"dimensions": dims, "gate": {"weighted_mean_min": gate}}


# --- (a) unequal declared weights are honoured -----------------------------------

def test_unequal_weights_move_the_gate_mean(monkeypatch, tmp_path):
    rubric = _rubric([
        {"name": "specificity", "weight": 0.5},
        {"name": "hierarchy_of_controls", "weight": 0.3},
        {"name": "defensibility", "weight": 0.2},
    ])
    scores = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 3}
    record = _graded_record(monkeypatch, tmp_path, "skill-unequal", rubric, scores)
    # (5*0.5 + 4*0.3 + 3*0.2) / 1.0 = 4.3 — the OLD unweighted mean was 4.0.
    assert record["weighted_mean"] == pytest.approx(4.3)
    assert record["pass"] is True


def test_unequal_weights_can_flip_the_gate_verdict(monkeypatch, tmp_path):
    # Weight mass on the LOW dim drags the mean below the 4.0 gate even though
    # the unweighted mean (4.0) would have squeaked past it.
    rubric = _rubric([
        {"name": "specificity", "weight": 0.2},
        {"name": "hierarchy_of_controls", "weight": 0.2},
        {"name": "defensibility", "weight": 0.6},
    ])
    scores = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 3}
    record = _graded_record(monkeypatch, tmp_path, "skill-flip", rubric, scores)
    assert record["weighted_mean"] == pytest.approx(3.6)
    assert record["pass"] is False


# --- (b) the canonical template rubric: weighted == plain mean --------------------

def test_canonical_rubric_equal_weights_match_plain_mean(monkeypatch, tmp_path):
    repo = Path(run_evals.__file__).resolve().parent.parent
    import yaml
    rubric = yaml.safe_load(
        (repo / "template" / "evals" / "rubric.yaml").read_text(encoding="utf-8"))
    scores = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 5}
    record = _graded_record(monkeypatch, tmp_path, "skill-canonical", rubric, scores)
    expected = round(sum(scores.values()) / len(scores), 3)
    assert record["weighted_mean"] == expected  # equal 0.20 weights: unchanged
    assert record["pass"] is True


# --- (c) no weight fields at all: equal-share default ------------------------------

def test_rubric_without_weight_fields_defaults_to_plain_mean(monkeypatch, tmp_path):
    rubric = _rubric([
        {"name": "specificity"},
        {"name": "hierarchy_of_controls"},
        {"name": "defensibility"},
    ])
    scores = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 5}
    record = _graded_record(monkeypatch, tmp_path, "skill-weightless", rubric, scores)
    assert record["weighted_mean"] == round(sum(scores.values()) / 3, 3)


# --- (d) reported-only completeness still cannot move the weighted mean -----------

def test_completeness_weight_never_enters_the_gate_mean(monkeypatch, tmp_path):
    # Even a rubric that (wrongly) gave completeness a HUGE weight cannot move
    # the gate mean: the exclusion is structural (MODEL_GRADED_DIMS iteration),
    # not weight-based (D-18).
    rubric = _rubric([
        {"name": "specificity", "weight": 0.2},
        {"name": "hierarchy_of_controls", "weight": 0.2},
        {"name": "defensibility", "weight": 0.2},
        {"name": "completeness", "weight": 10.0},
    ])
    gating = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 5}
    record = _graded_record(monkeypatch, tmp_path, "skill-comp-weight", rubric,
                            {**gating, "completeness": 1})
    assert record["weighted_mean"] == round(sum(gating.values()) / 3, 3)
    assert record["pass"] is True


# --- (e) dim_weights is defensive ---------------------------------------------------

def test_dim_weights_defensive_on_junk_shapes():
    weights = run_evals.dim_weights({"dimensions": [
        {"name": "ok", "weight": 0.4},
        {"name": "bool-weight", "weight": True},      # bool is NOT a weight
        {"name": "negative", "weight": -3},           # negative -> default
        {"name": "stringy", "weight": "heavy"},       # non-numeric -> default
        {"name": "absent"},                            # missing -> default
        "not-a-dict",                                  # skipped
        {"weight": 0.9},                               # nameless -> skipped
    ]})
    assert weights == {
        "ok": 0.4, "bool-weight": 1.0, "negative": 1.0,
        "stringy": 1.0, "absent": 1.0,
    }
    assert run_evals.dim_weights({}) == {}


def test_all_zero_gating_weights_fall_back_to_plain_mean(monkeypatch, tmp_path):
    rubric = _rubric([
        {"name": "specificity", "weight": 0.0},
        {"name": "hierarchy_of_controls", "weight": 0.0},
        {"name": "defensibility", "weight": 0.0},
    ])
    scores = {"specificity": 5, "hierarchy_of_controls": 4, "defensibility": 5}
    record = _graded_record(monkeypatch, tmp_path, "skill-zero-w", rubric, scores)
    # No division-by-zero; degenerate rubric falls back to the plain mean.
    assert record["weighted_mean"] == round(sum(scores.values()) / 3, 3)
