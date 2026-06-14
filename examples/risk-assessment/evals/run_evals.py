#!/usr/bin/env python3
"""Phase-1 PLACEHOLDER eval runner for the risk-assessment contract-proof fixture.

The CANONICAL runner is authored by A8 in Phase 3 (shared at template/evals/ and
imported by CI eval.yml). This placeholder exists so the contract's evals/ folder
layout (A2 §3.4) is complete from Phase 1 and the linter's folder-layout rule
(rule 3) is satisfiable. It only validates that evals.json is well-formed and
carries >= 3 evals — it does NOT execute the skill.

Exit 0 = evals.json present, valid JSON, >= 3 evals; nonzero otherwise.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MIN_EVALS = 3


def main() -> int:
    evals_path = HERE / "evals.json"
    if not evals_path.is_file():
        print(f"FAIL: {evals_path} not found", file=sys.stderr)
        return 2
    try:
        data = json.loads(evals_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: evals.json is not valid JSON: {exc}", file=sys.stderr)
        return 1
    evals = data.get("evals", [])
    if len(evals) < MIN_EVALS:
        print(f"FAIL: need >= {MIN_EVALS} evals, found {len(evals)}", file=sys.stderr)
        return 1
    print(f"OK (placeholder): evals.json valid, {len(evals)} evals present.")
    print("NOTE: the real runner (A8, Phase 3) will execute the skill against the rubric.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
