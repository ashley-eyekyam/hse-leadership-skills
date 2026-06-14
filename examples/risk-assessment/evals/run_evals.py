#!/usr/bin/env python3
"""Thin per-skill shim — runs THIS skill's evals via the shared A8 runner.

The Phase-1 placeholder (which only counted >=3 evals) is gone; the canonical
runner is scripts/run_evals.py (A8, Plan 03-05). Every skill's evals/run_evals.py
is this same thin shim: it imports the shared module and runs its own folder, so
the executor -> deterministic graders -> model grader pipeline + the pinned
GRADER_MODEL live in ONE place.
"""

import sys
from pathlib import Path

# This skill dir is two levels up from evals/run_evals.py; the repo root is found
# by walking up to the scripts/ package.
SKILL_DIR = Path(__file__).resolve().parent.parent
REPO = SKILL_DIR.parent.parent  # examples/<skill>/ -> repo root
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_evals  # the shared A8 runner


def main() -> int:
    # Delegate to the shared runner, scoped to this skill folder.
    return run_evals.main([str(SKILL_DIR)])


if __name__ == "__main__":
    sys.exit(main())
