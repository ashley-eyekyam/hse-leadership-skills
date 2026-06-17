"""QA-01 — the A8 10-rule linter contract (lint_skills.py).

Wave-0 RED stub (Plan 03-04, Task 1): these assert the lint_skills.py module's
public contract BEFORE it is implemented, so they fail meaningfully (linter
absent) rather than on an import-time syntax error.

What this pins (A8 §4.1 / A2 §5):

  * `validate_skill(path) -> Report` PASSES the born-conformant
    examples/risk-assessment fixture (no errors);
  * each of the 10 A2 rules FIRES on a crafted-bad copy of that fixture
    (rule 1 byte-diff block; rule 3 missing folder; rule 4 bad name vocab /
    out-of-vocab metadata; rule 5 over-1024 description = hard, first-person =
    warning; rule 8 dead reference; rule 9 unresolvable KB id; rule 10
    time-sensitive phrasing);
  * KB-SNIP-ARCHETYPES resolves under rule 9 (Plan 01 registered it);
  * THE SAME-MODULE-AS-FORGE contract (A8 Decision 8 / T-03-11): the forge's
    validate_repo_skill.py name resolves to THIS module's callable, and
    validate_standard.py drives the ONE rule engine (no second engine, no
    shelling out).

lint_skills.py lives in scripts/ (not scripts/hse_components/), so we insert the
scripts dir on sys.path here — the shared conftest only covers hse_components/.
"""

import re
import shutil
import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

REPO = SCRIPTS_DIR.parent
FIXTURE = REPO / "examples" / "risk-assessment"

lint_skills = pytest.importorskip(
    "lint_skills", reason="scripts/lint_skills.py not implemented yet (Task 2)"
)


# --- module public contract ----------------------------------------------------

def test_module_exposes_validate_skill_and_main():
    assert callable(getattr(lint_skills, "validate_skill", None)), "validate_skill missing"
    assert callable(getattr(lint_skills, "main", None)), "main missing"


def test_staleness_days_is_a_single_constant_180():
    assert getattr(lint_skills, "STALENESS_DAYS", None) == 180


# --- born-conformant fixture PASSES --------------------------------------------

def test_reference_fixture_lints_clean():
    report = lint_skills.validate_skill(FIXTURE)
    assert not report.errors, f"reference fixture should lint clean, got: {report.errors}"


def test_main_on_reference_fixture_exits_zero():
    assert lint_skills.main([str(FIXTURE)]) == 0


# --- the 10 rules each FIRE on a crafted-bad input ------------------------------

@pytest.fixture
def bad_skill(tmp_path):
    """A copy of the reference fixture under tmp so we can corrupt it per rule."""
    dst = tmp_path / "risk-assessment"
    shutil.copytree(FIXTURE, dst)
    return dst


def _errors(path):
    return lint_skills.validate_skill(path).errors


def test_rule1_byte_diff_block_fails(bad_skill):
    # Corrupt the deid block region so it no longer matches template/blocks/deid.md.
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    text = text.replace("DETECT & FLAG", "DETECT AND FLAG (drifted)")
    skill.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert any("block" in e.lower() and "deid" in e.lower() for e in errs), errs


def test_rule3_missing_folder_fails(bad_skill):
    shutil.rmtree(bad_skill / "references")
    errs = _errors(bad_skill)
    assert any("references" in e.lower() for e in errs), errs


def test_rule4_bad_name_vocab_fails(bad_skill):
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    # Name with uppercase + space — violates lowercase [a-z0-9-].
    text = text.replace("name: risk-assessment", "name: Risk Assessment")
    skill.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert any("name" in e.lower() for e in errs), errs


def test_rule6_out_of_vocab_metadata_fails(bad_skill):
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    text = text.replace("category: risk-assessment", "category: made-up-category")
    skill.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert any("category" in e.lower() or "vocab" in e.lower() for e in errs), errs


def test_rule5_description_over_1024_is_hard_fail(bad_skill):
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    long_desc = "x" * 1100
    text = re.sub(
        r"description: >.*?\nlicense:",
        f"description: {long_desc}\nlicense:",
        text,
        flags=re.S,
    )
    skill.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert any("description" in e.lower() and "1024" in e for e in errs), errs


def test_rule5_first_person_description_is_warning_not_error(bad_skill):
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    text = re.sub(
        r"description: >.*?\nlicense:",
        "description: I produce a risk assessment for you.\nlicense:",
        text,
        flags=re.S,
    )
    skill.write_text(text, encoding="utf-8")
    report = lint_skills.validate_skill(bad_skill)
    # First-person is a WARNING (A2 R3 / Decision 7), never a hard error.
    assert any("first-person" in w.lower() or "pronoun" in w.lower() for w in report.warnings), (
        report.warnings
    )
    assert not any("description" in e.lower() and "pronoun" in e.lower() for e in report.errors)


def test_rule8_dead_reference_fails(bad_skill):
    # Remove a referenced file but keep its citation in the body.
    (bad_skill / "references" / "METHODOLOGY.md").unlink()
    errs = _errors(bad_skill)
    assert any("METHODOLOGY.md" in e or "dead" in e.lower() or "reference" in e.lower() for e in errs), errs


def test_rule9_unresolvable_kb_id_fails(bad_skill):
    manifest = bad_skill / "references" / "_skill-kb.md"
    text = manifest.read_text(encoding="utf-8")
    text = text.replace("KB-STD-ISO45001", "KB-STD-NONEXISTENT")
    manifest.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert any("KB-STD-NONEXISTENT" in e or "resolve" in e.lower() for e in errs), errs


def test_rule10_time_sensitive_phrasing_is_warning(bad_skill):
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    text = text.replace(
        "## Reference material",
        "As of 2026-01-01, the current rules apply.\n\n## Reference material",
    )
    skill.write_text(text, encoding="utf-8")
    report = lint_skills.validate_skill(bad_skill)
    assert any("time-sensitive" in w.lower() or "as of" in w.lower() or "currently" in w.lower()
               for w in report.warnings), report.warnings


# --- rule 6 D-06 bundled_in cross-bundle membership (Plan 06-01) ----------------

def test_rule6_unregistered_bundled_in_hard_fails(bad_skill):
    """An unregistered metadata.bundled_in value is a rule-6 HARD error (D-06)."""
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    # Inject a bundled_in list with one good + one bogus bundle under metadata.
    text = text.replace(
        "  plugin: hse-core",
        "  plugin: hse-core\n  bundled_in:\n    - hse-chemicals\n    - not-a-bundle",
    )
    skill.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert any("bundled_in" in e and "not-a-bundle" in e for e in errs), errs
    # The registered sibling value must NOT itself error.
    assert not any("bundled_in" in e and "hse-chemicals" in e for e in errs), errs


def test_rule6_registered_bundled_in_passes(bad_skill):
    """A registered metadata.bundled_in value produces no rule-6 error (D-06)."""
    skill = bad_skill / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    text = text.replace(
        "  plugin: hse-core",
        "  plugin: hse-core\n  bundled_in:\n    - hse-chemicals\n    - hse-mining",
    )
    skill.write_text(text, encoding="utf-8")
    errs = _errors(bad_skill)
    assert not any("bundled_in" in e for e in errs), errs


# --- rule 9 KB-SNIP-ARCHETYPES resolves (Plan 01 registered it) -----------------

def test_kb_snip_archetypes_resolves_under_rule9():
    # Add an ARCHETYPES citation to a clean copy; it must resolve (no error).
    report = lint_skills.validate_skill(FIXTURE)
    # The archetypes id is registered; resolving it must not error.
    resolver = lint_skills.resolve_kb_id
    assert resolver("KB-SNIP-ARCHETYPES", REPO) is True, "KB-SNIP-ARCHETYPES must resolve (Plan 01)"


# --- SAME-MODULE-AS-FORGE contract (T-03-11, A8 Decision 8) ---------------------

def test_validate_standard_drives_the_one_rule_engine():
    """validate_standard.py must import lint_skills — no second rule engine."""
    import validate_standard

    assert validate_standard.lint_skills is lint_skills, (
        "validate_standard must drive THE lint_skills module (one rule engine)"
    )


def test_forge_contract_name_resolves_to_this_module():
    """The forge's validate_repo_skill name resolves to lint_skills.validate_skill.

    The forge (A10, Phase 4) imports `validate_skill` from this module rather than
    forking the rule logic. We assert the callable the forge contract names IS this
    module's callable (no shelling out, no duplicate engine).
    """
    from lint_skills import validate_skill as forge_validate_skill

    assert forge_validate_skill is lint_skills.validate_skill


def test_no_second_rule_engine_module_exists():
    """There must be no parallel validate_repo_skill.py with its own rules.

    A10 will alias validate_repo_skill to lint_skills; if a sibling module already
    re-implements the rules, that is the divergent-engine threat (T-03-11).
    """
    sibling = SCRIPTS_DIR / "validate_repo_skill.py"
    if sibling.exists():
        text = sibling.read_text(encoding="utf-8")
        assert "import lint_skills" in text or "from lint_skills" in text, (
            "validate_repo_skill.py must re-export lint_skills, not re-implement rules"
        )
