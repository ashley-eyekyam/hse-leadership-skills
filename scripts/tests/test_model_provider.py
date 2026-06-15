"""Model-grader provider: the local Claude CLI on the subscription (D-03,
2026-06-15 owner decision — the model-graded path runs via `claude -p`, NOT an API
key, and self-skips in headless CI).

These pin: the Sonnet-class grader id; that the model path only runs when the Claude
CLI is available; the exact `claude -p` invocation (model flag, text output, cwd,
CLAUDECODE dropped so a nested call works); fail-soft on a CLI error; and the
tolerant JSON parse. subprocess.run is monkeypatched, so NO real `claude` call is
made. The deterministic de-id / citation gate stays model-independent and is covered
in test_run_evals_scope.py.

sys.path is wired to scripts/ so imports resolve the way run_evals does at runtime.
"""

import sys
import types
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_evals  # noqa: E402


def _fake_proc(stdout):
    return types.SimpleNamespace(stdout=stdout, stderr="", returncode=0)


# --- the pinned grader id (D-03) -----------------------------------------------

def test_grader_model_default_is_sonnet_class():
    assert run_evals.GRADER_MODEL == "claude-sonnet-4-6"


# --- _model_available gates the whole model path -------------------------------

def test_model_available_true_when_cli_on_path(monkeypatch):
    monkeypatch.setattr(run_evals.shutil, "which", lambda name: "/usr/bin/claude")
    assert run_evals._model_available() is True


def test_model_available_false_when_no_cli(monkeypatch):
    monkeypatch.setattr(run_evals.shutil, "which", lambda name: None)
    assert run_evals._model_available() is False


def test_call_model_returns_empty_without_cli(monkeypatch):
    monkeypatch.setattr(run_evals, "_model_available", lambda: False)
    assert run_evals.call_model("hi", "claude-sonnet-4-6") == ""


# --- the exact `claude -p` invocation ------------------------------------------

def test_call_model_shells_claude_p_with_model_and_drops_claudecode(monkeypatch):
    monkeypatch.setattr(run_evals, "_model_available", lambda: True)
    monkeypatch.setenv("CLAUDECODE", "1")
    captured = {}

    def fake_run(cmd, cwd=None, env=None, capture_output=None, text=None, timeout=None):
        captured["cmd"] = cmd
        captured["cwd"] = cwd
        captured["env"] = env
        return _fake_proc("graded text")

    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)

    out = run_evals.call_model("score this", "claude-sonnet-4-6", cwd=Path("/tmp/skill"))
    assert out == "graded text"
    assert captured["cmd"] == [
        "claude", "-p", "score this", "--output-format", "text",
        "--model", "claude-sonnet-4-6",
    ]
    assert captured["cwd"] == "/tmp/skill"
    # CLAUDECODE must be stripped from the child env so a nested call runs.
    assert "CLAUDECODE" not in captured["env"]


def test_call_model_omits_model_flag_when_none(monkeypatch):
    monkeypatch.setattr(run_evals, "_model_available", lambda: True)

    def fake_run(cmd, **kw):
        return _fake_proc("ok")

    holder = {}
    monkeypatch.setattr(run_evals.subprocess, "run",
                        lambda cmd, **kw: holder.setdefault("cmd", cmd) or _fake_proc("ok"))
    run_evals.call_model("q", None)
    assert "--model" not in holder["cmd"]


def test_call_model_failsoft_on_cli_error(monkeypatch):
    monkeypatch.setattr(run_evals, "_model_available", lambda: True)

    def boom(cmd, **kw):
        raise OSError("claude crashed")

    monkeypatch.setattr(run_evals.subprocess, "run", boom)
    assert run_evals.call_model("x", "claude-sonnet-4-6") == ""


# --- _extract_json_obj: tolerate fenced / wrapped JSON -------------------------

def test_extract_json_obj_plain():
    assert run_evals._extract_json_obj('{"specificity": 5}') == {"specificity": 5}


def test_extract_json_obj_fenced():
    raw = "```json\n{\"specificity\": 4, \"defensibility\": 5}\n```"
    assert run_evals._extract_json_obj(raw) == {"specificity": 4, "defensibility": 5}


def test_extract_json_obj_with_prose():
    raw = "Here are the scores: {\"specificity\": 3} — done."
    assert run_evals._extract_json_obj(raw) == {"specificity": 3}


# --- run_model_grader over `claude -p` -----------------------------------------

_RUBRIC = {"dimensions": [
    {"name": "specificity"},
    {"name": "hierarchy_of_controls"},
    {"name": "defensibility"},
]}


def test_model_grader_noop_without_cli(monkeypatch, tmp_path):
    monkeypatch.setattr(run_evals, "_model_available", lambda: False)
    verdict = run_evals.run_model_grader(
        tmp_path, {"query": "q"}, "out", _RUBRIC, "claude-sonnet-4-6")
    assert verdict == {"scored": False, "model": "claude-sonnet-4-6", "scores": {}}


def test_model_grader_parses_fenced_scores(monkeypatch, tmp_path):
    monkeypatch.setattr(run_evals, "_model_available", lambda: True)

    def fake_run(cmd, **kw):
        return _fake_proc(
            "```json\n{\"specificity\": 5, \"hierarchy_of_controls\": 4, "
            "\"defensibility\": 4}\n```")

    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    verdict = run_evals.run_model_grader(
        tmp_path, {"query": "q"}, "out", _RUBRIC, "claude-sonnet-4-6")
    assert verdict["scored"] is True
    assert verdict["model"] == "claude-sonnet-4-6"
    assert verdict["scores"] == {
        "specificity": 5, "hierarchy_of_controls": 4, "defensibility": 4}


def test_model_grader_failsoft_on_unparseable_output(monkeypatch, tmp_path):
    monkeypatch.setattr(run_evals, "_model_available", lambda: True)
    monkeypatch.setattr(run_evals.subprocess, "run",
                        lambda cmd, **kw: _fake_proc("I cannot score this."))
    verdict = run_evals.run_model_grader(
        tmp_path, {"query": "q"}, "out", _RUBRIC, "claude-sonnet-4-6")
    assert verdict["scored"] is False
