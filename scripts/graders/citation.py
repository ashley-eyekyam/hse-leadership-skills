"""graders/citation.py — the deterministic regulatory-citation grader (A8 §4.4.2).

A model may invent a regulatory citation; this grader proves every cited KB id in
the output resolves to a knowledge-base _registry.yaml fragment. An unresolvable
cite forces regulatory_citation_accuracy below 4 = FAIL (threat T-03-15) — the
second hard-fail enforcement class, distinct from the de-id leak.

It REUSES the lint_skills rule-9 resolver (`resolve_kb_id`) — the SAME importable
module the forge validator uses (correctness trap: no second resolver). India
citations resolve to the KB-REG-IN-STATEFORMS row (no hard-coded national form
number).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List

# scripts/ on sys.path so `import lint_skills` resolves the shared module whatever
# the invoking cwd (run_evals.py imports the same way).
_SCRIPTS = Path(__file__).resolve().parent.parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from lint_skills import resolve_kb_id, ID_RE  # the SHARED rule-9 resolver

# Pass / fail scores for the regulatory_citation_accuracy dimension. An
# unresolvable citation forces the dimension below the rubric's fail_below=4.
_SCORE_PASS = 5
_SCORE_FAIL = 1


def grade_citation(output_text: str, repo: Path) -> Dict:
    """Deterministic citation grader. Returns::

        {"fail": bool,
         "regulatory_citation_accuracy": int,   # <4 on any unresolvable cite
         "reasons": [str, ...],
         "unresolved": [kb_id, ...],
         "resolved": [kb_id, ...]}

    `repo` is the public-repo root (the resolver looks under
    repo/knowledge-base/<folder>/_registry.yaml). An output with no KB-id
    citations passes (nothing to fabricate).
    """
    text = output_text or ""
    repo = Path(repo)

    cited = sorted(set(ID_RE.findall(text)))
    resolved: List[str] = []
    unresolved: List[str] = []
    for kb_id in cited:
        if resolve_kb_id(kb_id, repo):
            resolved.append(kb_id)
        else:
            unresolved.append(kb_id)

    reasons: List[str] = []
    for kb_id in unresolved:
        reasons.append(
            f"cited id {kb_id} does not resolve to any knowledge-base _registry.yaml "
            f"fragment (invented or wrong-jurisdiction citation)"
        )

    fail = bool(unresolved)
    score = _SCORE_FAIL if fail else _SCORE_PASS
    return {
        "fail": fail,
        "regulatory_citation_accuracy": score,
        "reasons": reasons,
        "unresolved": unresolved,
        "resolved": resolved,
    }
