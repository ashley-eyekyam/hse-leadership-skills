"""FND-04 — Rule 11 (`intake-coverage`) fixture suite.

These exercise `lint_skills._rule11_intake_coverage` (built in plan 08-05) in
isolation: a clean `references/intake.md` produces zero rule-11 findings, and
EVERY failure mode the elicitation-coverage contract enumerates fires its own
specific finding (research §4.3 / §6 fixture inventory).

Because the frozen `examples/risk-assessment/` is EXEMPT inside `validate_skill`
(the two-pronged gate), the rule-level fixtures call `_rule11_intake_coverage`
DIRECTLY on a mutated fixture skill_dir — bypassing the exemption gate so the
rule logic is tested on its own (research §6 "Fixture layout").

Rules 11/12 are HARD this phase; the helpers read `report.errors + report.warnings`
level-agnostically so the fixtures survive the WARN→HARD flip.

This test file asserts behavior; it NEVER edits `lint_skills.py`. The bad-Type
literal is constructed in test code and is written ONLY into a tmp_path fixture,
never into any committed SKILL.md / template.

`lint_skills.py` lives in `scripts/` (not `scripts/hse_components/`), so we
insert the scripts dir on sys.path here exactly as `test_lint_skills.py` does.
"""

import shutil
import sys
import textwrap
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

REPO = SCRIPTS_DIR.parent
FIXTURE = REPO / "examples" / "risk-assessment"

lint_skills = pytest.importorskip(
    "lint_skills", reason="scripts/lint_skills.py not implemented yet (plan 08-05)"
)


# --- the clean, born-conformant intake.md baseline -----------------------------
#
# covers = the 3 universal dims (born-passes step 3); every conditional sits in
# omits with a non-empty reason (born-passes step 5); a 3-row universal Q-table
# typed from _VALID_Q_TYPES with each Dim in covers (born-passes step 6); no
# branches (steps 7/8 vacuously pass — ELI-JURIS is omitted); echo-back +
# refuse-on-vague cues present (step 9). The SKILL.md lean pointer (step 10) is
# handled by make_skill writing "references/intake.md" into the body.

CLEAN_INTAKE = textwrap.dedent(
    """\
    ---
    intake-coverage:
      covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT]
      omits:
        ELI-JURIS: "single-jurisdiction skill — jurisdiction is fixed"
        ELI-INDUSTRY: "sector-agnostic method"
        ELI-LOCATION: "physical environment not material to this output"
        ELI-EXPOSURE: "exposed population fixed by the task"
        ELI-BASELINE: "no current-state baseline needed"
        ELI-EVIDENCE: "evidence captured inline by the method"
        ELI-OBLIGATIONS: "obligations resolved downstream"
        ELI-SCORING: "fixed scoring scheme"
        ELI-COMPETENCY: "competent persons captured at sign-off"
        ELI-TEMPORAL: "review cadence fixed by policy"
      branches: []
    ---

    # Structured intake — fixture skill

    Run one question at a time; **echo the captured facts back before any
    analysis**; **refuse on a vague subject** — never proceed on a vague input.

    | # | Question | Type | Options / prompt | Dim | Asked-when |
    |---|---|---|---|---|---|
    | Q0 | Scope of this assessment / output | MCQ | occupational / environmental | ELI-SCOPE | always |
    | Q1 | The named task / site / asset | free-text | the specific task broken into steps + the site | ELI-SUBJECT | always |
    | Q2 | Output artifact wanted + its reader | MCQ | leadership / consultant / frontline | ELI-OUTPUT | always |

    ## Echo-back
    Echo the captured facts back and ask the user to confirm before any analysis.

    ## Refuse-on-vague anchors
    - Q1 is the specificity anchor: refuse a vague subject; never proceed on a
      vague or missing input.
    """
)

# A clean intake that ALSO covers ELI-JURIS with a valid India->state branch
# (step 8 passes): the India option triggers a branch activating a state Q.
CLEAN_INTAKE_INDIA = textwrap.dedent(
    """\
    ---
    intake-coverage:
      covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS]
      omits:
        ELI-INDUSTRY: "sector-agnostic method"
        ELI-LOCATION: "physical environment not material to this output"
        ELI-EXPOSURE: "exposed population fixed by the task"
        ELI-BASELINE: "no current-state baseline needed"
        ELI-EVIDENCE: "evidence captured inline by the method"
        ELI-OBLIGATIONS: "obligations resolved downstream"
        ELI-SCORING: "fixed scoring scheme"
        ELI-COMPETENCY: "competent persons captured at sign-off"
        ELI-TEMPORAL: "review cadence fixed by policy"
      branches:
        - when: Q3
          option: India
          activates_questions: [Q4]
    ---

    # Structured intake — fixture skill (with jurisdiction)

    Run one question at a time; **echo the captured facts back before any
    analysis**; **refuse on a vague subject** — never proceed on a vague input.

    | # | Question | Type | Options / prompt | Dim | Asked-when |
    |---|---|---|---|---|---|
    | Q0 | Scope of this assessment / output | MCQ | occupational / environmental | ELI-SCOPE | always |
    | Q1 | The named task / site / asset | free-text | the specific task broken into steps + the site | ELI-SUBJECT | always |
    | Q2 | Output artifact wanted + its reader | MCQ | leadership / consultant / frontline | ELI-OUTPUT | always |
    | Q3 | Legal jurisdiction | MCQ | UK / India / Other | ELI-JURIS | always |
    | Q4 | Which Indian state | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi | ELI-JURIS | when India |

    ## Echo-back
    Echo the captured facts back and ask the user to confirm before any analysis.

    ## Refuse-on-vague anchors
    - Q1 is the specificity anchor: refuse a vague subject; never proceed on a
      vague or missing input.
    """
)


# --- fixture helpers -----------------------------------------------------------

def make_skill(tmp_path, intake_text=CLEAN_INTAKE, with_pointer=True):
    """Copy the frozen example into tmp, write a `references/intake.md`, and
    ensure the SKILL.md body carries the lean pointer (step 10) unless asked not
    to. Returns the fixture skill_dir (a Path under tmp_path)."""
    dst = tmp_path / "fixture-skill"
    shutil.copytree(FIXTURE, dst)
    (dst / "references" / "intake.md").write_text(intake_text, encoding="utf-8")

    skill_md = dst / "SKILL.md"
    body = skill_md.read_text(encoding="utf-8")
    if with_pointer and "references/intake.md" not in body:
        # Append a lean pointer to the Reference material list region.
        body = body + "\n- `references/intake.md` — the structured-intake coverage contract.\n"
    skill_md.write_text(body, encoding="utf-8")
    return dst


def rule11(skill_dir):
    """Run `_rule11_intake_coverage` DIRECTLY on the fixture skill_dir (bypassing
    the validate_skill exemption gate) and return the rule-11 findings.

    Level-agnostic: collects from `report.errors + report.warnings` so the suite
    survives the WARN→HARD flip (findings move from warnings to errors when
    RULE_11_12_LEVEL == "error"). The errors+warnings union is a superset, so
    warnings-only findings (pre-flip) still match."""
    report = lint_skills.Report(skill="fixture-skill")
    body = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    lint_skills._rule11_intake_coverage(report, body, skill_dir, REPO)
    return [m for m in (report.errors + report.warnings) if m.startswith("rule 11")]


# --- clean pass ----------------------------------------------------------------

def test_clean_intake_has_no_rule11_findings(tmp_path):
    skill = make_skill(tmp_path)
    assert rule11(skill) == [], "a clean intake.md must produce 0 rule-11 findings"


def test_clean_intake_with_india_state_branch_passes(tmp_path):
    skill = make_skill(tmp_path, intake_text=CLEAN_INTAKE_INDIA)
    assert rule11(skill) == [], (
        "a clean intake covering ELI-JURIS with a valid India->state branch must "
        "produce 0 rule-11 findings"
    )


# --- one test per failure mode -------------------------------------------------

def test_missing_universal_fires(tmp_path):
    # Drop ELI-SCOPE from covers (step 3).
    text = CLEAN_INTAKE.replace(
        "covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT]",
        "covers: [ELI-SUBJECT, ELI-OUTPUT]",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("universal dimension" in f and "ELI-SCOPE" in f for f in findings), findings


def test_unknown_id_in_covers_fires(tmp_path):
    # Add a bogus id to covers (step 4).
    text = CLEAN_INTAKE.replace(
        "covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT]",
        "covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-BOGUS]",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("unknown elicitation dimension" in f and "ELI-BOGUS" in f for f in findings), findings


def test_omit_without_reason_fires(tmp_path):
    # Blank the reason for an omitted conditional (step 5).
    text = CLEAN_INTAKE.replace(
        'ELI-INDUSTRY: "sector-agnostic method"',
        'ELI-INDUSTRY: "   "',
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("omits" in f and "ELI-INDUSTRY" in f for f in findings), findings


def test_conditional_in_neither_fires(tmp_path):
    # Remove ELI-EVIDENCE from omits entirely (and it is not in covers) — step 5.
    text = CLEAN_INTAKE.replace(
        '    ELI-EVIDENCE: "evidence captured inline by the method"\n',
        "",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any(
        "conditional dimension" in f and "ELI-EVIDENCE" in f and "covers or omits" in f
        for f in findings
    ), findings


def test_bad_type_fires(tmp_path):
    # Construct an invalid Type token IN TEST CODE (never written to a production
    # file): the word for ordinary written text is not in _VALID_Q_TYPES (step 6).
    bad_type = "prose"
    assert lint_skills._norm_qtype(bad_type) not in lint_skills._VALID_Q_TYPES
    text = CLEAN_INTAKE.replace(
        "| Q0 | Scope of this assessment / output | MCQ |",
        "| Q0 | Scope of this assessment / output | " + bad_type + " |",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("Type" in f and "Q0" in f for f in findings), findings


def test_compound_dim_not_in_covers_fires(tmp_path):
    # A compound Dim cell ELI-SCOPE/ELI-BOGUS where ELI-BOGUS is not in covers (step 6).
    text = CLEAN_INTAKE.replace(
        "| ELI-SCOPE | always |",
        "| ELI-SCOPE/ELI-BOGUS | always |",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("Dim" in f and "ELI-BOGUS" in f and "not in covers" in f for f in findings), findings


def test_india_no_state_branch_fires(tmp_path):
    # ELI-JURIS covers an India option but there is no India->state branch (step 8).
    text = CLEAN_INTAKE_INDIA.replace(
        "  branches:\n"
        "    - when: Q3\n"
        "      option: India\n"
        "      activates_questions: [Q4]\n",
        "  branches: []\n",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("India->state" in f for f in findings), findings


def test_dangling_branch_fires(tmp_path):
    # activates_questions references Q99 which has no Q-row (step 7).
    text = CLEAN_INTAKE_INDIA.replace(
        "      activates_questions: [Q4]",
        "      activates_questions: [Q99]",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("activates_questions" in f and "Q99" in f for f in findings), findings


def test_missing_echo_back_fires(tmp_path):
    # Strip the echo-back cue (step 9).
    text = CLEAN_INTAKE.replace(
        "**echo the captured facts back before any\nanalysis**; ",
        "",
    )
    text = text.replace(
        "## Echo-back\nEcho the captured facts back and ask the user to confirm before any analysis.\n",
        "",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("echo-back" in f for f in findings), findings


def test_missing_refuse_on_vague_fires(tmp_path):
    # Strip every refuse-on-vague cue (step 9).
    text = CLEAN_INTAKE.replace(
        "**refuse on a vague subject** — never proceed on a vague input.",
        "ask each question in turn.",
    )
    text = text.replace(
        "## Refuse-on-vague anchors\n"
        "- Q1 is the specificity anchor: refuse a vague subject; never proceed on a\n"
        "  vague or missing input.\n",
        "## Anchors\n- Q1 is the primary subject question.\n",
    )
    skill = make_skill(tmp_path, intake_text=text)
    findings = rule11(skill)
    assert any("refuse-on-vague" in f for f in findings), findings


def test_skill_md_missing_pointer_fires(tmp_path):
    # The SKILL.md body lacks the lean pointer to references/intake.md (step 10).
    skill = make_skill(tmp_path, with_pointer=False)
    # Be robust to any pre-existing pointer in the frozen body: ensure none.
    skill_md = skill / "SKILL.md"
    body = skill_md.read_text(encoding="utf-8")
    assert "references/intake.md" not in body, (
        "frozen example unexpectedly references references/intake.md"
    )
    findings = rule11(skill)
    assert any("lean pointer" in f and "references/intake.md" in f for f in findings), findings


def test_missing_intake_file_fires(tmp_path):
    # Presence (step 1): no references/intake.md at all.
    dst = tmp_path / "fixture-skill"
    shutil.copytree(FIXTURE, dst)
    (dst / "references" / "intake.md").unlink(missing_ok=True)
    findings = rule11(dst)
    assert any("missing references/intake.md" in f for f in findings), findings


# --- WR-01: missing/empty elicitation taxonomy must fire, not silently no-op ----
#
# When knowledge-base/elicitation-taxonomy.yaml is missing OR empty, _taxonomy_ids
# returns an empty set and every downstream dimension check (universal floor,
# ID-resolution, conditional completeness) would silently no-op — disabling the
# specificity gate. WR-01 emits a finding and early-returns BEFORE the dependent
# steps. We point the rule at a tmp `repo` whose taxonomy is missing/empty (rather
# than the real REPO, which ships a populated taxonomy).

def _rule11_against_repo(skill_dir, repo):
    """Run _rule11_intake_coverage directly with an explicit `repo` arg and return
    the rule-11 findings.

    Level-agnostic: collects from `report.errors + report.warnings` so the suite
    survives the WARN→HARD flip."""
    report = lint_skills.Report(skill="fixture-skill")
    body = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    lint_skills._rule11_intake_coverage(report, body, skill_dir, repo)
    return [m for m in (report.errors + report.warnings) if m.startswith("rule 11")]


def test_missing_taxonomy_fires(tmp_path):
    # A tmp repo with NO knowledge-base/elicitation-taxonomy.yaml at all.
    repo = tmp_path / "repo"
    (repo / "knowledge-base").mkdir(parents=True)
    assert not (repo / "knowledge-base" / "elicitation-taxonomy.yaml").exists()
    skill = make_skill(tmp_path)
    findings = _rule11_against_repo(skill, repo)
    assert any("elicitation taxonomy missing or empty" in f for f in findings), findings
    # And the dependent steps must NOT have produced their own findings (early-return):
    # with the taxonomy absent there is exactly one rule-11 finding, not the cascade.
    assert findings == [
        "rule 11: elicitation taxonomy missing or empty — cannot resolve dimensions"
    ], findings


def test_empty_taxonomy_fires(tmp_path):
    # A tmp repo whose elicitation-taxonomy.yaml is present but EMPTY (`[]`).
    repo = tmp_path / "repo"
    (repo / "knowledge-base").mkdir(parents=True)
    (repo / "knowledge-base" / "elicitation-taxonomy.yaml").write_text("[]\n", encoding="utf-8")
    assert lint_skills._taxonomy_ids(repo) == set()
    skill = make_skill(tmp_path)
    findings = _rule11_against_repo(skill, repo)
    assert any("elicitation taxonomy missing or empty" in f for f in findings), findings
    assert findings == [
        "rule 11: elicitation taxonomy missing or empty — cannot resolve dimensions"
    ], findings
