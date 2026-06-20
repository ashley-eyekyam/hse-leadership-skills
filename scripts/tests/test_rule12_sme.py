"""FND-04 — Rule 12 (`sme-review`) fixture suite.

These exercise `lint_skills._rule12_sme_review` (built in plan 08-05) in
isolation: a clean `references/sme-review.md` + a roster that references it
produces zero rule-12 findings, and EVERY failure mode the per-skill SME
sign-off contract enumerates fires its own specific finding (research §4.4 / §6
fixture inventory). The optional boundary phrase always fires a WARN.

The frozen `examples/risk-assessment/` is EXEMPT inside `validate_skill`, so the
rule-level fixtures call `_rule12_sme_review` DIRECTLY on the mutated fixture
skill_dir — bypassing the exemption gate (research §6 "Fixture layout").

Rules 11/12 are HARD this phase; the `rule12()` helper reads
`report.errors + report.warnings` level-agnostically so the fixtures survive the
WARN→HARD flip. The optional SME-02 boundary-phrase check stays a WARN and asserts
on `report.warnings` directly.

This test file asserts behavior; it NEVER edits `lint_skills.py`.

`lint_skills.py` lives in `scripts/`, so we insert the scripts dir on sys.path
here exactly as `test_lint_skills.py` does.
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
ORCH_END = "<!-- hse:block:orchestration:end -->"

lint_skills = pytest.importorskip(
    "lint_skills", reason="scripts/lint_skills.py not implemented yet (plan 08-05)"
)


# --- the clean, born-conformant sme-review.md baseline -------------------------
#
# 1 persona with non-empty role/expertise/lens (born-passes step 3); a ≥3-item
# domain checklist under a "Domain checklist" heading (born-passes step 4); a
# sign-off note that does NOT use a forbidden boundary phrase (boundary WARN does
# not fire). Step 5 (roster references the file) is satisfied by make_skill
# injecting "references/sme-review.md" into the roster below orchestration:end.

CLEAN_SME = textwrap.dedent(
    """\
    ---
    sme-review:
      personas:
        - role: "Competent HSE practitioner (generic SME reviewer)"
          expertise: "General HSE law and standards, the hierarchy of controls, defensibility, and de-identification."
          lens: "would a regulator accept this — every control specific to the named task, higher-order controls before PPE, every claim cited, zero de-id leak"
    ---

    # SME Review & Sign-off — fixture skill

    ## Domain checklist (the nuanced things only this expert catches)
    - [ ] every control is specific to the named task / site / asset
    - [ ] hierarchy of controls applied — no PPE/admin-only treatment unjustified
    - [ ] every conclusion traced to evidence; actions have named owners and dates

    ## Sign-off note
    SME review ran (persona: Competent HSE practitioner); this is decision-support;
    a FLAG it raises is recorded, never merge-blocking — it precedes and never
    replaces the human competent-person review.
    """
)


def _two_personas_block():
    return textwrap.dedent(
        """\
        sme-review:
          personas:
            - role: "Competent HSE practitioner (generic SME reviewer)"
              expertise: "General HSE law and standards, the hierarchy of controls, defensibility, and de-identification."
              lens: "would a regulator accept this"
            - role: "Process safety engineer"
              expertise: "Process hazards, LOPA, safe operating limits."
              lens: "are the process-safety hazards and safeguards specific and defensible"
        """
    )


def _n_personas_block(n):
    """A `sme-review:` manifest with exactly n personas (each fully populated)."""
    head = "sme-review:\n"
    if n == 0:
        return head + "  personas: []\n"
    body = "  personas:\n"
    for i in range(n):
        body += (
            f'    - role: "Reviewer {i}"\n'
            f'      expertise: "Expertise {i}"\n'
            f'      lens: "Lens {i}"\n'
        )
    return head + body


# --- fixture helpers -----------------------------------------------------------

def make_skill(tmp_path, sme_text=CLEAN_SME, roster_references=True):
    """Copy the frozen example into tmp, write a `references/sme-review.md`, and
    (by default) inject a roster line referencing references/sme-review.md below
    the orchestration :end marker so step 5 passes. Returns the fixture
    skill_dir."""
    dst = tmp_path / "fixture-skill"
    shutil.copytree(FIXTURE, dst)
    (dst / "references" / "sme-review.md").write_text(sme_text, encoding="utf-8")

    skill_md = dst / "SKILL.md"
    body = skill_md.read_text(encoding="utf-8")
    if roster_references:
        roster_line = (
            ORCH_END
            + "\n\n- **SME Reviewer** — applies the personas in "
            + "`references/sme-review.md` as a recorded (non-blocking) review.\n"
        )
        body = body.replace(ORCH_END, roster_line, 1)
    skill_md.write_text(body, encoding="utf-8")
    return dst


def rule12(skill_dir):
    """Run `_rule12_sme_review` DIRECTLY on the fixture skill_dir (bypassing the
    validate_skill exemption gate) and return the rule-12 findings.

    Level-agnostic: collects from `report.errors + report.warnings` so the suite
    survives the WARN→HARD flip. NOTE: the OPTIONAL SME-02 boundary-phrase check
    (further down this file) stays a WARN regardless of the flip and asserts on
    `report.warnings` directly — do not route it through this helper."""
    report = lint_skills.Report(skill="fixture-skill")
    body = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    lint_skills._rule12_sme_review(report, body, skill_dir)
    return [m for m in (report.errors + report.warnings) if m.startswith("rule 12")]


# --- clean pass ----------------------------------------------------------------

def test_clean_sme_review_has_no_rule12_findings(tmp_path):
    skill = make_skill(tmp_path)
    assert rule12(skill) == [], "a clean sme-review.md + roster reference must yield 0 rule-12 findings"


# --- one test per failure mode -------------------------------------------------

def test_zero_personas_fires(tmp_path):
    text = CLEAN_SME.replace(_clean_personas_block(), _n_personas_block(0))
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert any("1-2 personas" in f for f in findings), findings


def test_three_personas_fires(tmp_path):
    text = CLEAN_SME.replace(_clean_personas_block(), _n_personas_block(3))
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert any("1-2 personas" in f for f in findings), findings


def test_two_personas_passes(tmp_path):
    # 2 personas is the upper bound of the allowed 1-2 range — must NOT fire.
    text = CLEAN_SME.replace(_clean_personas_block(), _two_personas_block())
    skill = make_skill(tmp_path, sme_text=text)
    assert rule12(skill) == [], "2 personas is within the allowed 1-2 range"


def test_empty_lens_fires(tmp_path):
    # Blank the single persona's lens (step 3 fields check).
    text = CLEAN_SME.replace(
        '      lens: "would a regulator accept this — every control specific to the named task, higher-order controls before PPE, every claim cited, zero de-id leak"',
        '      lens: "   "',
    )
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert any("role/expertise/lens" in f for f in findings), findings


def test_under_three_checklist_fires(tmp_path):
    # Drop one checklist item so only 2 remain (step 4).
    text = CLEAN_SME.replace(
        "- [ ] every conclusion traced to evidence; actions have named owners and dates\n",
        "",
    )
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert any("checklist" in f for f in findings), findings


def test_no_roster_reference_fires(tmp_path):
    # The roster below orchestration:end does not reference references/sme-review.md (step 5).
    skill = make_skill(tmp_path, roster_references=False)
    body = (skill / "SKILL.md").read_text(encoding="utf-8")
    after_end = body.split(ORCH_END, 1)[1]
    assert "references/sme-review.md" not in after_end, (
        "frozen roster unexpectedly references references/sme-review.md"
    )
    findings = rule12(skill)
    assert any("roster does not reference" in f for f in findings), findings


def test_missing_sme_file_fires(tmp_path):
    # Presence (step 1): no references/sme-review.md at all.
    dst = tmp_path / "fixture-skill"
    shutil.copytree(FIXTURE, dst)
    (dst / "references" / "sme-review.md").unlink(missing_ok=True)
    findings = rule12(dst)
    assert any("missing references/sme-review.md" in f for f in findings), findings


# --- optional boundary WARN (always WARN regardless of RULE_11_12_LEVEL) -------

def test_boundary_phrase_triggers_warn(tmp_path):
    # Inject a forbidden sign-off boundary phrase into the sme-review body.
    boundary = "approved by a competent person"
    assert boundary in lint_skills.SIGN_OFF_FORBIDDEN
    text = CLEAN_SME.replace(
        "SME review ran (persona: Competent HSE practitioner);",
        "This artifact has been " + boundary + ";",
    )
    skill = make_skill(tmp_path, sme_text=text)
    report = lint_skills.Report(skill="fixture-skill")
    body = (skill / "SKILL.md").read_text(encoding="utf-8")
    lint_skills._rule12_sme_review(report, body, skill)
    assert any(
        boundary in w for w in report.warnings
    ), report.warnings


# --- WR-02: negation-aware boundary scan ---------------------------------------
#
# The canonical boundary phrasing (knowledge-base/prompt-snippets/sme-signoff.md +
# skills/hse-skill-forge/templates/sme-review.md) states the prohibition AS A
# NEGATION. A naive whole-body substring scan false-WARNs on it. WR-02 makes the
# scan negation-aware: a line containing a negator token (never/not/precedes/
# replaces/without) OR a quoted occurrence of the phrase is a documented boundary,
# not an affirmative claim, and must NOT WARN. Only an affirmative emission WARNs.

# The exact canonical negation phrasing every authored sme-review.md mirrors
# (sme-signoff.md lines 31-32): both a "never replaces" negation AND a quoted,
# never-outputs occurrence of the forbidden phrase. Neither may WARN.
CANONICAL_NEGATION_SIGNOFF = (
    "## Sign-off note\n"
    "Decision-support only. This review PRECEDES — and never replaces, never emits — the\n"
    "human competent-person sign-off. It never outputs \"approved by a competent person\".\n"
)


def test_canonical_negation_phrasing_does_not_warn(tmp_path):
    # Replace the clean sign-off note with the canonical negation phrasing — which
    # CONTAINS the forbidden substrings 'approved by a competent person' and
    # 'competent person sign-off' but only as negations/quotes. NO boundary WARN.
    text = CLEAN_SME.replace(
        "## Sign-off note\n"
        "SME review ran (persona: Competent HSE practitioner); this is decision-support;\n"
        "a FLAG it raises is recorded, never merge-blocking — it precedes and never\n"
        "replaces the human competent-person review.\n",
        CANONICAL_NEGATION_SIGNOFF,
    )
    # Guard: the replace actually landed and the forbidden phrase IS present in body.
    assert CANONICAL_NEGATION_SIGNOFF in text
    assert "approved by a competent person" in text
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert not any("sign-off boundary phrase" in f for f in findings), (
        "canonical negation/quoted boundary phrasing must NOT trip the boundary WARN: "
        f"{findings}"
    )
    # No OTHER rule-12 finding either (the rest of CLEAN_SME is born-conformant).
    assert findings == [], findings


def test_affirmative_signoff_claim_warns(tmp_path):
    # An affirmative emission of the forbidden phrase WITH NO negator on the line
    # MUST still WARN (the boundary guard must not over-suppress).
    boundary = "approved by a competent person"
    text = CLEAN_SME.replace(
        "## Sign-off note\n"
        "SME review ran (persona: Competent HSE practitioner); this is decision-support;\n"
        "a FLAG it raises is recorded, never merge-blocking — it precedes and never\n"
        "replaces the human competent-person review.\n",
        "## Sign-off note\nThis artifact is " + boundary + " and ready to issue.\n",
    )
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert any(
        "sign-off boundary phrase" in f and boundary in f for f in findings
    ), findings


def test_forge_template_signoff_does_not_warn(tmp_path):
    # The born-conformant forge sme-review.md template states the boundary as a
    # negation ("it precedes and never replaces the human competent-person review").
    # Running the rule against that exact sign-off note must produce NO boundary WARN.
    template = (
        REPO / "skills" / "hse-skill-forge" / "templates" / "sme-review.md"
    ).read_text(encoding="utf-8")
    # Lift the template's sign-off note (negation phrasing) into the clean baseline.
    note = template.split("## Sign-off note", 1)[1]
    text = CLEAN_SME.replace(
        "## Sign-off note\n"
        "SME review ran (persona: Competent HSE practitioner); this is decision-support;\n"
        "a FLAG it raises is recorded, never merge-blocking — it precedes and never\n"
        "replaces the human competent-person review.\n",
        "## Sign-off note" + note,
    )
    skill = make_skill(tmp_path, sme_text=text)
    findings = rule12(skill)
    assert not any("sign-off boundary phrase" in f for f in findings), findings


# --- the clean-persona block (single source for the replace-based mutations) ---

def _clean_personas_block():
    """The exact `sme-review:` personas block in CLEAN_SME — replace target for
    the persona-count mutations."""
    start = CLEAN_SME.index("sme-review:")
    end = CLEAN_SME.index("---\n", start)
    return CLEAN_SME[start:end]
