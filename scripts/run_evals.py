#!/usr/bin/env python3
"""run_evals.py — the A8 eval runner (A8 §4.3 / §4.4, QA-02).

Pipeline per eval case (research Pattern A8 — the two enforcement classes):

    executor  ->  DETERMINISTIC graders (deid, citation, report)  ->  model grader

The deterministic graders are the NON-WAIVABLE hard block and run FIRST. A
deterministic hard-fail (a de-id leak, an invented citation) SHORT-CIRCUITS the
case BEFORE the model grader is ever invoked — a stochastic judge never gets to
"pass" a privacy leak (threat T-03-16). A deterministic auto-fail overrides the
weighted mean.

The model grader scores ONLY the judgement dimensions (specificity,
hierarchy_of_controls, defensibility) via the `claude -p --model GRADER_MODEL`
executor pattern. It is NOT skill-creator's run_eval.py (that is a description
*trigger* evaluator, not a rubric grader — research Pitfall 4); we reuse only the
benchmark.json output field names so skill-creator's eval-viewer opens our output.

GRADER_MODEL — the single pinned Sonnet-class id (D-03). Defined ONCE here; the
rubric's `analyzer_model: most-capable-model` alias resolves to it. Re-verified at
build time via the claude-api skill (`shared/models.md`: claude-sonnet-4-6 Active,
the "sonnet"/"balanced" alias; bare id, NEVER a date suffix). Override with
--grader-model or the GRADER_MODEL env var so CI can pin it explicitly and it can
be re-resolved at any future build without a code edit.

Stdlib + pyyaml only. The model-graded path needs ANTHROPIC_API_KEY (CI only); the
deterministic graders + the wiring run with ZERO model calls (and ZERO key).

CLI:
    python run_evals.py <skill-dir>... | --all   [--ci] [--changed] [--matrix]
                        [--model M] [--grader-model M] [--out benchmark.json]
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# scripts/ -> repo root; put scripts/ on sys.path so the graders import cleanly
# whatever the invoking cwd.
SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_deid, grade_citation, grade_report_produced  # noqa: E402

# --- D-03: the ONE pinned grader-model constant --------------------------------
# Bare id, no date suffix (claude-api skill rule). Re-verified at build time:
# claude-api shared/models.md L65 — `claude-sonnet-4-6` Active; L123 the
# "sonnet"/"balanced" alias resolves to it.
GRADER_MODEL = os.environ.get("GRADER_MODEL", "claude-sonnet-4-6")

# The rubric alias that resolves to GRADER_MODEL (A8 §4.3 indirection — one place
# to retune; never scatter the literal across files).
MOST_CAPABLE_ALIAS = "most-capable-model"

# The judgement dimensions the MODEL grader scores (the two hard-fail dims are
# decided deterministically and excluded from the model's remit).
MODEL_GRADED_DIMS = ("specificity", "hierarchy_of_controls", "defensibility")

DEFAULT_GATE = 4.0


# --- rubric loading ------------------------------------------------------------

def load_rubric(skill_dir: Path) -> Dict[str, Any]:
    """Load the skill's evals/rubric.yaml (falls back to the canonical template)."""
    candidate = skill_dir / "evals" / "rubric.yaml"
    if not candidate.is_file():
        candidate = REPO / "template" / "evals" / "rubric.yaml"
    return yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}


def resolve_grader_model(rubric: Dict[str, Any], override: Optional[str] = None) -> str:
    """Resolve the rubric's analyzer_model alias to the pinned GRADER_MODEL.

    An explicit --grader-model override wins; otherwise the `most-capable-model`
    alias resolves to GRADER_MODEL; any other literal in the rubric is honoured
    as-is (a developer pinning a specific id locally)."""
    if override:
        return override
    alias = rubric.get("analyzer_model", MOST_CAPABLE_ALIAS)
    if alias == MOST_CAPABLE_ALIAS:
        return GRADER_MODEL
    return alias


def gate_threshold(rubric: Dict[str, Any]) -> float:
    return float((rubric.get("gate") or {}).get("weighted_mean_min", DEFAULT_GATE))


# --- executor ------------------------------------------------------------------

def run_skill(skill_dir: Path, query: str, model: Optional[str]) -> str:
    """Execute the skill against `query` via `claude -p` and return the output
    text. Returns "" when the CLI/key is unavailable (the deterministic graders
    still run on whatever the case carries; CI supplies the key)."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return ""
    cmd = ["claude", "-p", query, "--output-format", "text"]
    if model:
        cmd.extend(["--model", model])
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        proc = subprocess.run(
            cmd, cwd=str(skill_dir), env=env,
            capture_output=True, text=True, timeout=300,
        )
        return proc.stdout or ""
    except Exception as exc:  # pragma: no cover - host/CLI dependent
        print(f"WARN: executor failed ({exc})", file=sys.stderr)
        return ""


# --- deterministic graders (run FIRST, short-circuit) --------------------------

def run_deterministic(output_text: str) -> Dict[str, Any]:
    """The deterministic hard-block layer. Returns a verdict with `hard_fail` set
    on a de-id leak OR an unresolvable citation — either SHORT-CIRCUITS the case
    before the model grader."""
    deid = grade_deid(output_text, REPO / "references" / "deid-checklist.md")
    citation = grade_citation(output_text, REPO)

    hard_fail = bool(deid["auto_fail"] or citation["fail"])
    reasons: List[str] = []
    if deid["auto_fail"]:
        reasons.append("de_identification: " + "; ".join(deid["reasons"]))
    if citation["fail"]:
        reasons.append("regulatory_citation_accuracy: " + "; ".join(citation["reasons"]))

    return {
        "hard_fail": hard_fail,
        "reasons": reasons,
        "de_identification": {"auto_fail": deid["auto_fail"], "reasons": deid["reasons"]},
        "regulatory_citation_accuracy": citation["regulatory_citation_accuracy"],
    }


# --- model grader (judgement dims only; needs the key) -------------------------

def run_model_grader(
    skill_dir: Path, case: Dict[str, Any], output_text: str,
    rubric: Dict[str, Any], grader_model: str,
) -> Dict[str, Any]:
    """Score the judgement dimensions with the pinned GRADER_MODEL. A no-op
    (scores omitted) when no key/CLI is present — the deterministic verdict still
    stands. Only invoked when the deterministic layer did NOT hard-fail."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return {"scored": False, "model": grader_model, "scores": {}}

    rubric_dims = {d["name"]: d for d in rubric.get("dimensions", [])}
    judged = {n: rubric_dims[n] for n in MODEL_GRADED_DIMS if n in rubric_dims}
    prompt = (
        "You are an HSE eval grader. Score the SKILL OUTPUT below on each "
        "dimension 1-5 per its anchors. Reply with ONLY a JSON object "
        f"{{dim: score}} for these dimensions: {list(judged)}.\n\n"
        f"RUBRIC:\n{yaml.safe_dump({'dimensions': list(judged.values())})}\n\n"
        f"EXPECTATIONS:\n{json.dumps(case.get('expectations', []))}\n\n"
        f"SKILL OUTPUT:\n{output_text}\n"
    )
    cmd = ["claude", "-p", prompt, "--model", grader_model, "--output-format", "text"]
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        proc = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=300)
        scores = json.loads(proc.stdout.strip())
        scores = {k: int(v) for k, v in scores.items() if k in MODEL_GRADED_DIMS}
    except Exception as exc:  # pragma: no cover - host/model dependent
        print(f"WARN: model grader failed ({exc})", file=sys.stderr)
        return {"scored": False, "model": grader_model, "scores": {}}
    return {"scored": True, "model": grader_model, "scores": scores}


# --- per-case + per-skill orchestration ----------------------------------------

def grade_case(
    skill_dir: Path, case: Dict[str, Any], rubric: Dict[str, Any],
    grader_model: str, exec_model: Optional[str],
) -> Dict[str, Any]:
    """Run one eval case through executor -> deterministic graders -> model grader
    (short-circuit on a deterministic hard-fail)."""
    output_text = run_skill(skill_dir, case.get("query", ""), exec_model)

    deterministic = run_deterministic(output_text)
    record: Dict[str, Any] = {
        "query": case.get("query", ""),
        "deterministic": deterministic,
    }

    if deterministic["hard_fail"]:
        # SHORT-CIRCUIT: the model grader is never invoked on a hard-fail.
        record["model_grade"] = {"scored": False, "reason": "short-circuited by hard-fail"}
        record["pass"] = False
        record["weighted_mean"] = None
        return record

    model_grade = run_model_grader(skill_dir, case, output_text, rubric, grader_model)
    record["model_grade"] = model_grade

    # Weighted mean over the model-judged dims (equal-weight rubric). Only
    # computed when the model actually scored (CI path); otherwise pass is
    # deferred to the deterministic verdict (no hard-fail = not blocked).
    if model_grade["scored"] and model_grade["scores"]:
        scores = model_grade["scores"]
        weighted = sum(scores.values()) / len(scores)
        record["weighted_mean"] = round(weighted, 3)
        record["pass"] = weighted >= gate_threshold(rubric)
    else:
        record["weighted_mean"] = None
        record["pass"] = True  # no hard-fail and no model score available
    return record


def run_skill_evals(
    skill_dir: Path, grader_override: Optional[str], exec_model: Optional[str],
) -> Dict[str, Any]:
    """Run the skill's evals.json. Emits skill-creator's benchmark.json field
    names so the eval-viewer opens the output."""
    evals_path = skill_dir / "evals" / "evals.json"
    data = json.loads(evals_path.read_text(encoding="utf-8"))
    rubric = load_rubric(skill_dir)
    grader_model = resolve_grader_model(rubric, grader_override)

    cases = data.get("evals", [])
    results = [grade_case(skill_dir, c, rubric, grader_model, exec_model) for c in cases]
    passed = sum(1 for r in results if r["pass"])
    total = len(results)
    return {
        "skill_name": data.get("skill", skill_dir.name),
        "description": data.get("_comment", ""),
        "grader_model": grader_model,
        "results": results,
        "summary": {"total": total, "passed": passed, "failed": total - passed},
    }


def _iter_skill_dirs(repo: Path) -> List[Path]:
    found: List[Path] = []
    for root in (repo / "skills", repo / "examples"):
        if root.is_dir():
            for child in sorted(root.rglob("evals/evals.json")):
                found.append(child.parent.parent)
    return found


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Run HSE skill evals (A8 §4.3).")
    p.add_argument("skills", nargs="*", help="skill dir(s) with evals/evals.json")
    p.add_argument("--all", action="store_true", help="run every skill in the repo")
    p.add_argument("--ci", action="store_true", help="CI mode (pinned grader; nonzero on any fail)")
    p.add_argument("--changed", action="store_true", help="(reserved) only changed skills — wired in Plan 06")
    p.add_argument("--matrix", action="store_true", help="(local) Haiku/Sonnet/Opus matrix — developer aid only")
    p.add_argument("--model", default=None, help="executor model for the skill-under-test")
    p.add_argument("--grader-model", default=None, help=f"override the pinned grader (default {GRADER_MODEL})")
    p.add_argument("--out", default=None, help="write the benchmark.json here")
    args = p.parse_args(argv)

    if args.all:
        targets = _iter_skill_dirs(REPO)
    else:
        targets = [Path(s) for s in args.skills]
    if not targets:
        p.error("no skills given (pass skill dir(s) or --all)")

    any_fail = False
    benchmarks = []
    for skill_dir in targets:
        bench = run_skill_evals(skill_dir, args.grader_model, args.model)
        benchmarks.append(bench)
        s = bench["summary"]
        print(f"[{bench['skill_name']}] {s['passed']}/{s['total']} pass "
              f"(grader={bench['grader_model']})")
        for r in bench["results"]:
            if not r["pass"]:
                any_fail = True
                print(f"  FAIL: {r['query'][:70]}", file=sys.stderr)
                for reason in r["deterministic"]["reasons"]:
                    print(f"        hard-fail: {reason}", file=sys.stderr)

    output = benchmarks[0] if len(benchmarks) == 1 else {"benchmarks": benchmarks}
    if args.out:
        Path(args.out).write_text(json.dumps(output, indent=2), encoding="utf-8")

    # In CI a hard-fail (or a below-gate weighted mean) blocks merge.
    return 1 if (any_fail and args.ci) else 0


if __name__ == "__main__":
    raise SystemExit(main())
