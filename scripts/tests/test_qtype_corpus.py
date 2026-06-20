"""FND-04 — frozen Q-type corpus + the WARN-not-HARD severity guard.

This file asserts the rule-11 Q-type whitelist contract built in plan 08-05:

  * every one of the 17 FROZEN normalized `_VALID_Q_TYPES` strings passes the
    membership predicate (`_norm_qtype(s) in _VALID_Q_TYPES`);
  * an unknown ordinary-prose token + the literal "essay" are NOT members
    (the bad token is constructed in test code and never echoed into a
    committed SKILL.md / template — D-01);
  * raw spacing variants fold identically (`MCQ + free-text` == `MCQ+free-text`);
  * the WARN-not-HARD staging guard: `RULE_11_12_LEVEL == "warn"`, and a skill
    missing `references/intake.md` run through `_rule11_intake_coverage` yields a
    WARNING (not an error) — proving the repo stays GREEN this phase while the
    48 skills are backfilled (Phase 9). The Phase-10 HARD flip is the one-line
    change of that constant to "error".

This test file asserts behavior; it NEVER edits `lint_skills.py`. `lint_skills.py`
lives in `scripts/` (not `scripts/hse_components/`), so we insert the scripts dir
on sys.path here exactly as `test_lint_skills.py` does.
"""

import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

REPO = SCRIPTS_DIR.parent

lint_skills = pytest.importorskip(
    "lint_skills", reason="scripts/lint_skills.py not implemented yet (plan 08-05)"
)


# --- the FROZEN corpus -------------------------------------------------------------
#
# The 17 normalized Q-type strings, frozen 2026-06-20. Built once from the six
# family-rollout specs by gathering every distinct `Type` cell of every branched
# Q-table and normalizing it (strip whitespace, lowercase):
#
#     grep '^|' docs/.../2026-06-20-elicitation-sme/0[1-6]-*.md \
#       | awk -F'|' '$4!="Type"{print $4}' \
#       | <normalize: re.sub(r"\s+","",s.strip().lower())>
#
# 19 raw strings folded to the 17 normalized entries below. The two arrow entries
# (free-text->role, mcq->confirm) carry a literal U+2192 that survives normalize.
#
# D-01 accepted trade-off: the public test tree cannot reach the private specs,
# so this literal list is frozen here as the single in-test source. A genuinely-new
# Phase-9 Type variant absent from all family specs will NOT auto-normalize
# through — it must be ADDED by editing `_VALID_Q_TYPES` in lint_skills.py (and
# this fixture). Because rules 11/12 are WARN in Phase 9, a stray variant surfaces
# as a WARN (not a hard block) before the Phase-10 HARD flip.
CORPUS_NORMALIZED = [
    "free-text",
    "free-text(date-time)",
    "free-text(ints)",
    "free-text(number)mandatory",
    "free-text(optional)",
    "free-text(structured)",
    "free-text+mcq",
    "free-text/mcq-if-enumerable",
    "free-text/mcqmulti",
    "free-text→role",
    "mcq",
    "mcq+free-text",
    "mcqmulti",
    "mcqmulti-select",
    "mcqmulti-select+free-text",
    "mcqperendpoint",
    "mcq→confirm",
]


# --- corpus passes / unknowns fail -------------------------------------------------

def test_corpus_is_seventeen_entries():
    """The frozen corpus is exactly the 17 normalized strings (D-01)."""
    assert len(CORPUS_NORMALIZED) == 17
    assert len(set(CORPUS_NORMALIZED)) == 17, "no duplicate normalized entries"


def test_corpus_matches_valid_set():
    """The fixture corpus and lint_skills._VALID_Q_TYPES are the SAME 17-set
    (the in-test freeze tracks the production whitelist; drift is caught here)."""
    assert set(CORPUS_NORMALIZED) == set(lint_skills._VALID_Q_TYPES)


def test_every_corpus_qtype_passes():
    """Each of the 17 frozen normalized strings passes the membership predicate."""
    for s in CORPUS_NORMALIZED:
        assert lint_skills._norm_qtype(s) in lint_skills._VALID_Q_TYPES, (
            f"frozen corpus Type {s!r} must be in _VALID_Q_TYPES"
        )


def test_unknown_qtype_fails():
    """An unknown ordinary-prose token + the literal 'essay' are NOT members.

    The bad token is constructed here from a normalized-prose word so the
    rejected literal lives ONLY in this test file (never echoed into a linted
    production file). 'prose' is the ordinary word for ordinary written text."""
    bad_token = "pr" + "ose"  # the ordinary-prose word, assembled in test code only
    assert lint_skills._norm_qtype(bad_token) not in lint_skills._VALID_Q_TYPES
    assert lint_skills._norm_qtype("essay") not in lint_skills._VALID_Q_TYPES


def test_spacing_folds():
    """Raw spacing variants normalize identically and both land in the set."""
    a = lint_skills._norm_qtype("MCQ + free-text")
    b = lint_skills._norm_qtype("MCQ+free-text")
    assert a == b == "mcq+free-text"
    assert a in lint_skills._VALID_Q_TYPES
    assert b in lint_skills._VALID_Q_TYPES


# --- the WARN-not-HARD staging guard -----------------------------------------------

def test_rule_level_is_warn():
    """Rules 11/12 land as WARN this phase so the repo stays GREEN (D-02 staged
    rollout). Phase 10 flips this single token to 'error' — do NOT change it here."""
    assert lint_skills.RULE_11_12_LEVEL == "warn"


def test_missing_intake_is_warning_not_error(tmp_path):
    """A skill with a `references/` dir but no `intake.md`, run through
    `_rule11_intake_coverage`, yields a WARNING (not an error) — proving the
    severity constant routes rule-11 findings to warnings this phase."""
    skill_dir = tmp_path / "fixture-skill"
    (skill_dir / "references").mkdir(parents=True)
    # No intake.md written — the rule-11 presence step (1) must fire.
    report = lint_skills.Report(skill="fixture-skill")
    lint_skills._rule11_intake_coverage(report, "", skill_dir, REPO)
    assert report.errors == [], "missing intake.md must NOT be a hard error this phase"
    assert report.warnings, "missing intake.md must produce a WARNING this phase"
    assert any(w.startswith("rule 11") for w in report.warnings)
