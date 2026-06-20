"""test_validate_reexport.py — the forge validator IS the linter, never a fork.

A10 Decision 2 / FORGE-03 + threat T-04-03: `hse-skill-forge`'s
`validate_repo_skill.py` must re-EXPORT the public lint API from
`scripts/lint_skills.py` so a skill can never pass the forge yet fail CI. These are
IDENTITY assertions (same object, not an equal copy) — the strongest proof that
there is one module and no second rule engine.

Also a regression guard for the Wave-0 blocker: `hse-systems` must resolve as a
registered marketplace bundle (else the forge's own metadata.plugin fails rule 6).

Plain pytest; both the forge scripts/ dir and the repo scripts/ dir are put on
sys.path the same way the portability shim resolves them at runtime.
"""

import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
FORGE_SCRIPTS = REPO / "skills" / "hse-skill-forge" / "scripts"
LINT_SCRIPTS = REPO / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

for p in (str(FORGE_SCRIPTS), str(LINT_SCRIPTS)):
    if p not in sys.path:
        sys.path.insert(0, p)

import validate_repo_skill  # noqa: E402
import lint_skills  # noqa: E402
import scaffold  # noqa: E402


def test_validate_skill_is_lint_skills_object():
    """The re-exported validate_skill is the SAME object as lint_skills.validate_skill."""
    assert validate_repo_skill.validate_skill is lint_skills.validate_skill


def test_registered_bundles_is_lint_skills_object():
    """registered_bundles is re-exported by identity, not re-implemented."""
    assert validate_repo_skill.registered_bundles is lint_skills.registered_bundles


def test_report_is_lint_skills_object():
    """The Report return shape is the SAME class — the forge and CI agree on it."""
    assert validate_repo_skill.Report is lint_skills.Report


def test_no_rule_reimplemented_in_forge_validator():
    """validate_repo_skill.py defines no rule function (no fork of the engine)."""
    src = (FORGE_SCRIPTS / "validate_repo_skill.py").read_text(encoding="utf-8")
    assert "from lint_skills import" in src
    assert "def _rule" not in src, "the forge validator must not re-implement a rule"


def test_hse_systems_registered_bundle():
    """Wave-0 blocker regression guard: hse-systems resolves as a registered bundle."""
    assert "hse-systems" in validate_repo_skill.registered_bundles()
    assert "hse-systems" in lint_skills.registered_bundles()


def test_rules_11_12_inherited_by_reexport():
    """FND-05 — Rules 11/12 (added to lint_skills.py only) are inherited by the forge
    re-export FOR FREE: validating a skill missing references/intake.md through the
    forge `validate_repo_skill.validate_skill` produces the EXACT SAME findings as
    `lint_skills.validate_skill` (same object => same rule-11/12 findings). Proves no
    fork; the forge sees what CI sees. As of the Phase-10 HARD cutover the missing-
    intake finding is a HARD ERROR (RULE_11_12_LEVEL == 'error')."""
    answers = json.loads((FIXTURES / "probe_answers.json").read_text(encoding="utf-8"))
    name = "ztest-reexport-r1112"
    skill_dir = None
    try:
        skill_dir = scaffold.scaffold_skill(name, answers, force=True)
        # Break born-conformance: remove the intake reference so Rule 11 fires (HARD).
        (skill_dir / "references" / "intake.md").unlink()

        via_forge = validate_repo_skill.validate_skill(skill_dir)
        via_lint = lint_skills.validate_skill(skill_dir)

        # The forge re-export and CI agree on every finding (identity => same engine).
        assert via_forge.errors == via_lint.errors
        assert via_forge.warnings == via_lint.warnings
        # And the rule-11 missing-intake finding is among the HARD errors (Rule 11 reached the forge).
        assert any(e.startswith("rule 11") for e in via_forge.errors), via_forge.errors
    finally:
        if skill_dir is not None:
            shutil.rmtree(skill_dir, ignore_errors=True)
