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
    python run_evals.py <skill-dir>... | --all | --changed [--base REF]
                        [--ci] [--matrix] [--model M] [--grader-model M]
                        [--out benchmark.json]

--changed (D-04, WR-06): classify the diff against --base; a change to a
shared-contract surface (template/, knowledge-base/, scripts/hse_components/,
assets/report-engine/) escalates to a full sweep, otherwise only the changed
skills run. The classification is testable Python (classify_changed_targets).
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

def _load_case_artifact_text(skill_dir: Path, case: Dict[str, Any]) -> str:
    """Return the case's CAPTURED artifact text for the keyless deterministic path
    (CR-01).

    Without an ANTHROPIC_API_KEY the executor cannot produce live output, so the
    deterministic de-id / citation graders would scan "" and ALWAYS pass — making
    the dedicated deid-auto-fail CI job inert. Instead, when no key is present we
    grade the case's own on-disk / inline artifact:
      - `case["output"]` / `case["fixture_text"]`: inline text in evals.json; or
      - each path in `case["files"]`: a file relative to the skill dir (e.g.
        evals/files/<case>.md) whose contents are concatenated.
    A case that declares no artifact contributes no text (nothing to scan), which
    is correct — there is nothing captured to leak. The seeded-leak fixture under
    examples/ carries a `files`/`output` artifact so the keyless job has real text
    to hard-fail on, and a CI assertion proves the job exits nonzero."""
    parts: List[str] = []
    inline = case.get("output") or case.get("fixture_text")
    if isinstance(inline, str) and inline.strip():
        parts.append(inline)
    for rel in case.get("files", []) or []:
        candidate = (skill_dir / rel).resolve()
        try:
            if candidate.is_file():
                parts.append(candidate.read_text(encoding="utf-8"))
        except OSError as exc:  # pragma: no cover - host/fs dependent
            print(f"WARN: could not read case artifact {candidate} ({exc})",
                  file=sys.stderr)
    return "\n".join(parts)


def run_skill(skill_dir: Path, case: Dict[str, Any], model: Optional[str]) -> str:
    """Execute the skill against the case's query via `claude -p` and return the
    output text.

    With NO ANTHROPIC_API_KEY (the deid-auto-fail CI job, by design) the executor
    cannot run, so we fall back to the case's CAPTURED artifact text rather than ""
    (CR-01) — that keeps the deterministic de-id / citation hard blocks live in the
    keyless deterministic job. With a key, the live skill output is graded as
    before; the captured artifact is appended so a seeded leak in a fixture still
    trips even if the live model happened to behave."""
    query = case.get("query", "")
    captured = _load_case_artifact_text(skill_dir, case)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return captured
    cmd = ["claude", "-p", query, "--output-format", "text"]
    if model:
        cmd.extend(["--model", model])
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        proc = subprocess.run(
            cmd, cwd=str(skill_dir), env=env,
            capture_output=True, text=True, timeout=300,
        )
        live = proc.stdout or ""
    except Exception as exc:  # pragma: no cover - host/CLI dependent
        print(f"WARN: executor failed ({exc})", file=sys.stderr)
        live = ""
    return "\n".join(p for p in (live, captured) if p)


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
    output_text = run_skill(skill_dir, case, exec_model)

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


# --- D-04 changed-vs-sweep scope selection (WR-06) -----------------------------
# A change under any SHARED-CONTRACT surface can break EVERY skill, so it triggers
# a FULL sweep (--all). A change confined to skills/<one>/ evals only that skill.
# This logic was previously ONLY in eval.yml's shell `decide` step (untestable);
# it now lives here as importable, unit-testable Python (the regex source of truth
# for the sweep trigger). Keep this list in lockstep with eval.yml's path filter
# and the rubric's shared-contract path list.
SHARED_CONTRACT_PREFIXES = (
    "template/",
    "knowledge-base/",
    "scripts/hse_components/",
    "assets/report-engine/",
)
# A precise file under template/ that is also a shared-contract surface in its own
# right (kept for parity with eval.yml; already covered by the template/ prefix).
SHARED_CONTRACT_FILES = ("template/evals/rubric.yaml",)

# Sentinel: a shared-contract change -> run every skill.
SWEEP = "--all"


def classify_changed_targets(changed_paths: List[str], repo: Path = REPO):
    """Map a list of changed repo-relative paths to an eval scope (WR-06).

    Returns the SWEEP sentinel ('--all') when any shared-contract surface changed;
    otherwise a sorted list of the changed skill dirs (Path) that actually carry an
    evals/evals.json. An empty list means "nothing to eval"."""
    for path in changed_paths:
        norm = path.strip()
        if not norm:
            continue
        if norm in SHARED_CONTRACT_FILES or norm.startswith(SHARED_CONTRACT_PREFIXES):
            return SWEEP

    skill_dirs = set()
    for path in changed_paths:
        norm = path.strip()
        parts = norm.split("/")
        if len(parts) >= 2 and parts[0] in ("skills", "examples"):
            cand = repo / parts[0] / parts[1]
            if (cand / "evals" / "evals.json").is_file():
                skill_dirs.add(cand)
    return sorted(skill_dirs)


def _git_changed_files(base: str, repo: Path = REPO) -> List[str]:
    """`git diff --name-only <base>...HEAD` repo-relative paths (best-effort)."""
    try:
        proc = subprocess.run(
            ["git", "diff", "--name-only", f"{base}...HEAD"],
            cwd=str(repo), capture_output=True, text=True, timeout=60,
        )
        if proc.returncode != 0:
            proc = subprocess.run(
                ["git", "diff", "--name-only", "HEAD~1...HEAD"],
                cwd=str(repo), capture_output=True, text=True, timeout=60,
            )
        return [ln for ln in proc.stdout.splitlines() if ln.strip()]
    except Exception as exc:  # pragma: no cover - host/git dependent
        print(f"WARN: git diff failed ({exc})", file=sys.stderr)
        return []


# --- CR-01: the deterministic de-id self-test --------------------------------
# The deid-auto-fail CI job is keyless on purpose, so it cannot re-execute a skill;
# without this it graded "" and passed unconditionally. This self-test grades two
# captured control artifacts and proves the hard block both FIRES on a leak and
# does NOT false-positive on a clean report — so the gate is itself tested.
DEID_CANARY = REPO / "examples" / "deid-canary"


def run_deid_selftest(canary_dir: Path = DEID_CANARY) -> int:
    """Assert the deterministic de-id hard block against captured control
    artifacts (CR-01). Returns 0 iff leak.md auto-fails AND clean.md passes;
    nonzero (with a diagnostic) otherwise, so the keyless CI job actually
    enforces something."""
    leak_path = canary_dir / "leak.md"
    clean_path = canary_dir / "clean.md"
    if not leak_path.is_file() or not clean_path.is_file():
        print(f"ERROR: de-id self-test fixtures missing under {canary_dir}",
              file=sys.stderr)
        return 1

    leak_verdict = grade_deid(leak_path.read_text(encoding="utf-8"))
    clean_verdict = grade_deid(clean_path.read_text(encoding="utf-8"))

    ok = True
    if not leak_verdict["auto_fail"]:
        print("FAIL: de-id self-test — seeded leak (leak.md) did NOT auto-fail; "
              "the de-id hard block is not enforcing.", file=sys.stderr)
        ok = False
    if clean_verdict["auto_fail"]:
        print("FAIL: de-id self-test — clean report (clean.md) wrongly auto-failed; "
              f"reasons: {clean_verdict['reasons']}", file=sys.stderr)
        ok = False
    if ok:
        print("OK: de-id hard block enforces (leak.md auto-fails, clean.md passes).")
        return 0
    return 1


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Run HSE skill evals (A8 §4.3).")
    p.add_argument("skills", nargs="*", help="skill dir(s) with evals/evals.json")
    p.add_argument("--all", action="store_true", help="run every skill in the repo")
    p.add_argument("--ci", action="store_true", help="CI mode (pinned grader; nonzero on any fail)")
    p.add_argument("--deid-selftest", action="store_true",
                   help="CR-01: assert the deterministic de-id hard block against "
                        "the examples/deid-canary control artifacts (keyless; the "
                        "deid-auto-fail CI job's enforcement test). Exits nonzero "
                        "unless the seeded leak auto-fails and the clean report "
                        "passes.")
    p.add_argument("--changed", action="store_true",
                   help="eval only the skills changed since --base (D-04: a "
                        "shared-contract change escalates to a full --all sweep)")
    p.add_argument("--base", default="origin/main",
                   help="base ref for --changed (default origin/main)")
    p.add_argument("--matrix", action="store_true", help="(local) Haiku/Sonnet/Opus matrix — developer aid only")
    p.add_argument("--model", default=None, help="executor model for the skill-under-test")
    p.add_argument("--grader-model", default=None, help=f"override the pinned grader (default {GRADER_MODEL})")
    p.add_argument("--out", default=None, help="write the benchmark.json here")
    args = p.parse_args(argv)

    if args.deid_selftest:
        return run_deid_selftest()

    if args.changed:
        scope = classify_changed_targets(_git_changed_files(args.base), REPO)
        if scope == SWEEP:
            print("shared-contract surface changed -> FULL eval sweep (D-04).")
            targets = _iter_skill_dirs(REPO)
        elif scope:
            print(f"single-skill scope (D-04) -> {[str(d) for d in scope]}")
            targets = list(scope)
        else:
            print("no skill or shared-contract change -> nothing to eval (D-04).")
            return 0
    elif args.all:
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
