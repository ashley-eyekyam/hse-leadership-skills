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

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
FORGE_SCRIPTS = REPO / "skills" / "hse-skill-forge" / "scripts"
LINT_SCRIPTS = REPO / "scripts"

for p in (str(FORGE_SCRIPTS), str(LINT_SCRIPTS)):
    if p not in sys.path:
        sys.path.insert(0, p)

import validate_repo_skill  # noqa: E402
import lint_skills  # noqa: E402


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
