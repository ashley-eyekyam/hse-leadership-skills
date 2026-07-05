"""D-02 per-case ``deterministic_only`` flag — unit tests (v1.3 Phase 19, 19-01).

Contract under test (settles the 18-10 finding-2 deferral):

- A case carrying ``"deterministic_only": true`` SKIPS the local model-grader
  leg in ``grade_case`` while the deterministic gate (de-id / citation) and the
  reported-only completeness split still run — the deterministic verdict stays
  binding. ``record["model_grade"]["scored"] is False`` with the literal D-02
  reason, ``record["pass"] is True``, ``record["weighted_mean"] is None``.
- The SAME case WITHOUT the flag is unchanged: it still reaches
  ``run_model_grader`` (proven via a monkeypatched sentinel), so the flag —
  and only the flag — causes the skip.

Per-CASE only: this is distinct from the whole-run ``--deterministic-only``
argparse flag, which skips the model leg for the ENTIRE run (rejected by D-02
because a per-family sweep would lose model grading on the real PAIR cases).
"""

import sys as _sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

_SCRIPTS = REPO / "scripts"
if str(_SCRIPTS) not in _sys.path:
    _sys.path.insert(0, str(_SCRIPTS))

import run_evals  # noqa: E402

D02_REASON = "deterministic_only case (D-02; deterministic verdict binding)"

# A minimal clean graded-output artifact: no identifier, no citation, no
# phone-like digit run, date written as prose (never ISO — the de-id _PHONE_RE
# false-positives on ISO dates, todo 260623-p15).
CLEAN_OUTPUT = (
    "Prequalification questionnaire coverage summary.\n"
    "Prepared by the Procurement HSE Lead on 5 July 2026.\n"
    "All evidence items are demanded as verifiable records, never claims.\n"
)


def _case(flagged: bool) -> dict:
    """A minimal eval case with an inline graded OUTPUT artifact (non-empty, so
    grade_case gets PAST the empty-output short-circuit and the flag branch is
    the deciding path)."""
    case = {
        "query": "D-02 flag unit-test case",
        "output": CLEAN_OUTPUT,
    }
    if flagged:
        case["deterministic_only"] = True
    return case


def _sentinel_grader(calls):
    def _stub(skill_dir, case, output_text, rubric, grader_model):
        calls.append((skill_dir, grader_model))
        return {"scored": False, "model": "sentinel", "scores": {}}
    return _stub


def test_deterministic_only_skips_model_leg(tmp_path, monkeypatch):
    """A flagged case never invokes the model grader; the deterministic verdict
    (including the reported-only completeness record) still runs and binds."""
    calls = []
    monkeypatch.setattr(run_evals, "run_model_grader", _sentinel_grader(calls))

    record = run_evals.grade_case(
        tmp_path, _case(flagged=True), rubric={}, grader_model="stub", exec_model=None,
    )

    # The model leg was skipped with the literal D-02 reason.
    assert record["model_grade"]["scored"] is False
    assert record["model_grade"]["reason"] == D02_REASON
    assert record["pass"] is True
    assert record["weighted_mean"] is None
    # The sentinel proves run_model_grader was NEVER invoked.
    assert calls == []
    # The deterministic gate + the reported-only completeness split still ran.
    assert record["deterministic"]["hard_fail"] is False
    assert "completeness" in record["deterministic"]


def test_unflagged_case_still_reaches_model_grader(tmp_path, monkeypatch):
    """The SAME case without the flag reaches run_model_grader — the flag is
    the cause of the skip, not any other property of the case."""
    calls = []
    monkeypatch.setattr(run_evals, "run_model_grader", _sentinel_grader(calls))

    record = run_evals.grade_case(
        tmp_path, _case(flagged=False), rubric={}, grader_model="stub", exec_model=None,
    )

    # The sentinel was invoked exactly once — the model leg is intact.
    assert len(calls) == 1
    # With the stub unscored, pass defers to the deterministic verdict.
    assert record["model_grade"]["scored"] is False
    assert record["model_grade"].get("reason") != D02_REASON
    assert record["pass"] is True


def test_flag_must_be_boolean_true(tmp_path, monkeypatch):
    """Only the literal JSON true triggers the skip — truthy strings do not
    (the branch tests `is True`, mirroring a strict schema read)."""
    calls = []
    monkeypatch.setattr(run_evals, "run_model_grader", _sentinel_grader(calls))

    case = _case(flagged=False)
    case["deterministic_only"] = "true"  # WRONG type — must not skip
    run_evals.grade_case(
        tmp_path, case, rubric={}, grader_model="stub", exec_model=None,
    )

    assert len(calls) == 1
