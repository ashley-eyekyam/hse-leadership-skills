"""QA-02 — the deterministic citation grader (A8 §4.4.2).

A model may invent a regulatory citation; the grader proves every cited KB id
resolves to a knowledge-base _registry.yaml fragment. An unresolvable cite forces
regulatory_citation_accuracy below 4 = FAIL (the second hard-fail enforcement
class, distinct from the de-id leak).

The grader REUSES the lint_skills rule-9 resolver (resolve_kb_id) — it must not
re-derive a second resolver (correctness trap: same module, no fork).
"""

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

REPO = SCRIPTS.parent


def _grade(text):
    from graders.citation import grade_citation
    return grade_citation(text, REPO)


def test_unresolvable_citation_forces_score_below_4():
    # KB-REG-XX-NOPE does not resolve in any _registry.yaml.
    verdict = _grade("Per KB-REG-XX-NOPE the operator must file form 99-Z.")
    assert verdict["fail"] is True
    assert verdict["regulatory_citation_accuracy"] < 4
    assert any("KB-REG-XX-NOPE" in r for r in verdict["reasons"])


def test_resolvable_citation_passes():
    # KB-STD-ISO45001 resolves via standards/_registry.yaml (proven by
    # knowledge-base/tests/test_kb_resolution.py).
    verdict = _grade("This assessment maps to KB-STD-ISO45001 clause 6.1.2.")
    assert verdict["fail"] is False
    assert verdict["regulatory_citation_accuracy"] >= 4


def test_no_citations_does_not_fail():
    verdict = _grade("A risk assessment with no regulatory citation ids at all.")
    assert verdict["fail"] is False


def test_india_stateform_citation_resolves():
    # India citations must resolve to the KB-REG-IN-STATEFORMS row (no hard-coded
    # national form number) — the fixture references it (AC8/AC10).
    verdict = _grade("File the state form per KB-REG-IN-STATEFORMS.")
    assert verdict["fail"] is False


def test_grader_uses_shared_lint_resolver():
    # The grader must import the rule-9 resolver from lint_skills, not fork it.
    import graders.citation as cit
    src = Path(cit.__file__).read_text(encoding="utf-8")
    assert "lint_skills" in src, "citation grader must import the shared lint_skills resolver"
