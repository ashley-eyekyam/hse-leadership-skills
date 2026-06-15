"""CR-01 + WR-06 — run_evals scope selection and the de-id self-test.

Two enforcement-surface behaviours the code review flagged as untested:

  CR-01: the keyless `deid-auto-fail` job must actually enforce the de-id hard
         block. It now grades captured control artifacts (examples/deid-canary/)
         via `run_deid_selftest` / a keyless `run_skill` fallback, instead of
         re-executing the skill (which returns "" with no API key and made the
         gate inert). These tests prove the self-test fires on a leak, passes a
         clean report, and that the keyless executor falls back to captured text.

  WR-06: the D-04 changed-vs-sweep classification used to live only in eval.yml's
         shell `decide` step. It now lives in `classify_changed_targets` — these
         tests pin the shared-contract-sweep vs single-skill behaviour.

sys.path is wired to scripts/ so the imports resolve the way run_evals does at
runtime, regardless of invoking cwd.
"""

import os
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

REPO = SCRIPTS.parent

import run_evals  # noqa: E402


# --- CR-01: the de-id self-test enforces ---------------------------------------

def test_deid_selftest_passes_on_shipped_canary():
    # The shipped examples/deid-canary/ fixtures: leak.md auto-fails, clean.md
    # passes -> the self-test (and thus the keyless deid-auto-fail CI job) exits 0.
    assert run_evals.run_deid_selftest() == 0


def test_deid_selftest_fails_when_leak_does_not_leak(tmp_path):
    # If the seeded leak fixture stops leaking, the self-test MUST go nonzero —
    # proving the gate is not vacuous (the CR-01 bug was a gate that always passed).
    (tmp_path / "leak.md").write_text("Total recordable injuries = 18, aggregated.")
    (tmp_path / "clean.md").write_text("A clean report with no identifiers.")
    assert run_evals.run_deid_selftest(tmp_path) == 1


def test_deid_selftest_fails_on_false_positive_clean(tmp_path):
    # If the clean control wrongly auto-fails, the self-test also goes nonzero —
    # it guards BOTH directions of the hard block.
    (tmp_path / "leak.md").write_text("Worker John Smith, DOB 1985-04-12.")
    (tmp_path / "clean.md").write_text("Worker John Smith, DOB 1985-04-12.")
    assert run_evals.run_deid_selftest(tmp_path) == 1


def test_deid_selftest_missing_fixtures_is_nonzero(tmp_path):
    assert run_evals.run_deid_selftest(tmp_path) == 1


# --- CR-01: keyless run_skill grades captured artifact text, not "" ------------

def test_run_skill_keyless_returns_captured_inline_output(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    case = {"query": "q", "output": "Worker John Smith leaked here."}
    text = run_evals.run_skill(REPO / "examples" / "risk-assessment", case, None)
    assert "John Smith" in text  # NOT "" — the deterministic graders get real text


def test_run_skill_keyless_reads_case_files(monkeypatch, tmp_path):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    artifact = tmp_path / "evals" / "files"
    artifact.mkdir(parents=True)
    (artifact / "case1.md").write_text("Phone 555-867-5309 leaked.")
    case = {"query": "q", "files": ["evals/files/case1.md"]}
    text = run_evals.run_skill(tmp_path, case, None)
    assert "555-867-5309" in text


def test_run_skill_keyless_no_artifact_is_empty(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    case = {"query": "q", "files": []}
    text = run_evals.run_skill(REPO / "examples" / "risk-assessment", case, None)
    assert text == ""  # nothing captured -> nothing to scan (correct)


# --- WR-06: changed-vs-sweep classification ------------------------------------

@pytest.mark.parametrize("path", [
    "template/blocks/deid.md",
    "knowledge-base/_registry.yaml",
    "scripts/hse_components/rca.py",
    "assets/report-engine/generate_report.py",
    "template/evals/rubric.yaml",
])
def test_shared_contract_change_triggers_full_sweep(path):
    assert run_evals.classify_changed_targets([path]) == run_evals.SWEEP


def test_single_skill_change_scopes_to_that_skill():
    scope = run_evals.classify_changed_targets(["examples/risk-assessment/SKILL.md"])
    assert scope != run_evals.SWEEP
    assert [p.name for p in scope] == ["risk-assessment"]


def test_unrelated_change_evals_nothing():
    assert run_evals.classify_changed_targets(["README.md", "docs/x.md"]) == []


def test_skill_without_evals_json_is_skipped():
    # A path under skills/ for a dir with no evals/evals.json is not a target.
    assert run_evals.classify_changed_targets(["skills/ghost/SKILL.md"]) == []
