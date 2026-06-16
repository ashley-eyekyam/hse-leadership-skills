"""Measurement-validity fix (2026-06-16): the QUALITY grade reads a pre-captured
OUTPUT artifact, the DETERMINISTIC gate scans intake + output, and there is NO
live skill executor / 300s intake-timeout fallback.

These tests pin the four properties the fix guarantees:

  (a) the model grader grades the OUTPUT artifact text (`output_files`/`output`),
      NOT the intake fixtures (`files`);
  (b) a clean OUTPUT artifact with ranked hierarchy-of-controls is NOT hard-failed
      by the deterministic layer;
  (c) a seeded-leak `files` (intake) fixture is STILL caught (deterministic
      hard-fail) even when a clean OUTPUT artifact is present;
  (d) no live skill-executor `claude -p` is invoked for the quality grade — the
      ONLY model user is the grader path (run_model_grader); grade_case never
      calls call_model itself, and the removed `run_skill` executor is gone.

subprocess / call_model are monkeypatched so NO real `claude` call is made.
sys.path is wired to scripts/ so imports resolve the way run_evals does at runtime.
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
    ],
    "gate": {"weighted_mean_min": 4.0},
}

# A clean, consultant-grade OUTPUT artifact: role labels only, ranked HoC, an ISO
# clause cited as PROSE (no machine KB-id), no residual identifier, no <5 cell.
_CLEAN_OUTPUT = """\
# Risk Assessment — Tank T-402 Confined-Space Entry, Plant 3

Hazards scored on the org 5x5 matrix (risk_matrix engine).

Hierarchy of controls (ranked):
1. Elimination: remove the need to enter — clean in place via lance.
2. Engineering: forced-air ventilation + continuous gas monitoring.
3. Administrative: permit-to-work, trained entrant + standby.
4. PPE: SCBA as a last layer.

Residual risk re-scored after controls. ISO 45001 clause 6.1.2 applied.
Actions assigned to the Supervisor with ISO due dates.
"""

# A seeded-leak INTAKE fixture — a real name + DOB-with-date the de-id gate catches.
_LEAK_INTAKE = "Raw record: Worker John Smith, DOB 1985-04-12, manual-handling injury.\n"


def _write_case_dir(tmp_path, *, intake=None, output=None):
    """Create a skill dir with evals/files + evals/output and return (dir, case)."""
    (tmp_path / "evals" / "files").mkdir(parents=True)
    (tmp_path / "evals" / "output").mkdir(parents=True)
    case = {"query": "q"}
    if intake is not None:
        (tmp_path / "evals" / "files" / "intake.md").write_text(intake)
        case["files"] = ["evals/files/intake.md"]
    if output is not None:
        (tmp_path / "evals" / "output" / "case.md").write_text(output)
        case["output_files"] = ["evals/output/case.md"]
    return tmp_path, case


# --- (a) the model grader grades the OUTPUT artifact, NOT the intake ------------

def test_model_grader_receives_output_not_intake(monkeypatch, tmp_path):
    # Clean intake (so nothing short-circuits) — assert solely on WHICH text
    # reaches the model grader: the OUTPUT artifact, never the intake.
    skill_dir, case = _write_case_dir(tmp_path, intake="clean intake scope only",
                                      output=_CLEAN_OUTPUT)

    seen = {}

    def fake_grader(skill_dir, case, output_text, rubric, grader_model):
        seen["text"] = output_text
        return {"scored": True, "model": grader_model,
                "scores": {"specificity": 5, "hierarchy_of_controls": 5,
                           "defensibility": 5}}

    monkeypatch.setattr(run_evals, "run_model_grader", fake_grader)
    run_evals.grade_case(skill_dir, case, _RUBRIC, "claude-sonnet-4-6", None)

    assert "Hierarchy of controls" in seen["text"]      # the OUTPUT artifact
    assert "intake scope only" not in seen["text"]       # NOT the intake


# --- (b) a clean OUTPUT with ranked HoC is NOT hard-failed ----------------------

def test_clean_output_is_not_hard_failed(monkeypatch, tmp_path):
    skill_dir, case = _write_case_dir(tmp_path, intake="clean intake scope only",
                                      output=_CLEAN_OUTPUT)
    monkeypatch.setattr(run_evals, "_model_available", lambda: False)  # CI path
    record = run_evals.grade_case(skill_dir, case, _RUBRIC, "claude-sonnet-4-6", None)
    assert record["deterministic"]["hard_fail"] is False
    assert record["pass"] is True


# --- (c) seeded-leak intake is STILL caught with a clean OUTPUT present ---------

def test_seeded_leak_intake_caught_even_with_clean_output(monkeypatch, tmp_path):
    skill_dir, case = _write_case_dir(tmp_path, intake=_LEAK_INTAKE,
                                      output=_CLEAN_OUTPUT)
    monkeypatch.setattr(run_evals, "_model_available", lambda: False)

    # If the model grader were (wrongly) reached, fail loudly.
    def boom(*a, **k):
        raise AssertionError("model grader must NOT run on a deterministic hard-fail")

    monkeypatch.setattr(run_evals, "run_model_grader", boom)
    record = run_evals.grade_case(skill_dir, case, _RUBRIC, "claude-sonnet-4-6", None)
    assert record["deterministic"]["hard_fail"] is True  # the intake leak is caught
    assert record["pass"] is False
    reasons = " ".join(record["deterministic"]["reasons"])
    assert "de_identification" in reasons


# --- (d) no live skill-executor claude -p for the quality grade -----------------

def test_no_skill_executor_call_model_invocation(monkeypatch, tmp_path):
    # call_model is the ONLY `claude -p` shim. After the fix the ONLY caller is the
    # grader path (run_model_grader). grade_case must NEVER call call_model itself.
    skill_dir, case = _write_case_dir(tmp_path, intake="clean intake scope only",
                                      output=_CLEAN_OUTPUT)

    calls = []
    monkeypatch.setattr(run_evals, "call_model",
                        lambda *a, **k: calls.append(a) or "")

    # Stub the grader so the model path is exercised WITHOUT call_model — proving
    # grade_case has no executor call of its own.
    monkeypatch.setattr(run_evals, "run_model_grader",
                        lambda *a, **k: {"scored": False, "model": "m", "scores": {}})
    run_evals.grade_case(skill_dir, case, _RUBRIC, "claude-sonnet-4-6", None)
    assert calls == []  # grade_case made zero `claude -p` calls (no skill executor)


def test_run_skill_executor_is_removed():
    # The live skill executor (and its 300s intake-timeout fallback) is gone.
    assert not hasattr(run_evals, "run_skill")


def test_load_case_output_text_reads_output_files(tmp_path):
    skill_dir, case = _write_case_dir(tmp_path, output=_CLEAN_OUTPUT)
    text = run_evals._load_case_output_text(skill_dir, case)
    assert "Hierarchy of controls" in text


def test_load_case_output_text_empty_when_no_output():
    case = {"query": "q", "files": ["evals/files/x.md"]}
    assert run_evals._load_case_output_text(Path("/nonexistent"), case) == ""


# --- (e) a de-id PAIR case (no graded output) is NOT model-graded ---------------
# The de-id pair cases wire the CLEAN positive into `files` and carry no
# `output_files`. With no graded OUTPUT artifact there is nothing to quality-grade,
# so the model grader must NOT run (an empty-text grade would score 1/1/1 and
# pollute the quality pass-rate); the case passes on the deterministic verdict.

def test_no_output_artifact_case_is_not_model_graded(monkeypatch, tmp_path):
    # Clean intake (no leak -> no short-circuit), NO output_files.
    skill_dir, case = _write_case_dir(tmp_path, intake="clean intake scope only")
    assert "output_files" not in case  # de-id-pair shape

    def boom(*a, **k):
        raise AssertionError("model grader must NOT run when there is no graded "
                             "OUTPUT artifact")

    monkeypatch.setattr(run_evals, "run_model_grader", boom)
    record = run_evals.grade_case(skill_dir, case, _RUBRIC, "claude-sonnet-4-6", None)

    assert record["model_grade"]["scored"] is False
    assert "no graded output artifact" in record["model_grade"]["reason"]
    assert record["weighted_mean"] is None
    assert record["pass"] is True            # passes on the deterministic verdict
