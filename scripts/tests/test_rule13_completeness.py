"""FND-05 — Rule 13 (completeness / mode-manifest presence floor) fixture suite.

Exercises `lint_skills._rule13_completeness` in isolation against the static
fixtures under `scripts/tests/fixtures/rule13/` (NOT under `skills/`, so they
are invisible to the catalog and the rubric re-stamp). Pins the four contract
points of the staged-switch discipline (18-02 / D-20):

  (a) a deliberately-broken `modes:` map produces rule-13 findings routed to
      `report.warnings` (NOT `report.errors`) while the module-level severity
      token is "warn" — WARN-not-HARD this phase;
  (b) with the severity token monkeypatched to "error" the SAME broken fixture
      routes to `report.errors` — the single-token level flip is the ONLY
      Phase-20 change, and it flips independently of the rules-11/12 token;
  (c) a well-formed `modes:` map + omission-lens section yields ZERO rule-13
      findings (the presence floor accepts a structurally valid manifest);
  (d) an un-compilable author anchor is reported as a finding and does NOT
      raise (lint-time re.error safety, T-18-02-01).

This test file asserts behavior; it NEVER edits `lint_skills.py`.
`lint_skills.py` lives in `scripts/`, so the scripts dir goes on sys.path here
exactly as `test_rule12_sme.py` does.
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import lint_skills  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "rule13"
WELL_FORMED = FIXTURES / "well-formed"
BROKEN = FIXTURES / "broken-modes"
BAD_ANCHOR = FIXTURES / "bad-anchor"
UNCOVERABLE = FIXTURES / "uncoverable-min-matches"


def run_rule13(skill_dir):
    """Run `_rule13_completeness` DIRECTLY on the fixture skill_dir (bypassing
    the validate_skill exemption gate) and return the Report. `body` is empty —
    rule 13 reads only references/sme-review.md."""
    report = lint_skills.Report(skill=skill_dir.name)
    lint_skills._rule13_completeness(report, "", skill_dir)
    return report


def _r13(msgs):
    return [m for m in msgs if m.startswith("rule 13")]


# --- the staged-switch tokens are DISTINCT (Phase-20 flip independence) ---------

def test_rule13_level_is_a_distinct_warn_token():
    # RULE_13_LEVEL must exist as its own module constant, currently "warn",
    # SEPARATE from the already-HARD rules-11/12 token — so the Phase-20 flip
    # of rule 13 cannot entangle rules 11/12.
    assert lint_skills.RULE_13_LEVEL == "warn"
    assert lint_skills.RULE_11_12_LEVEL == "error"


# --- (a) broken fixture: WARN, not HARD, while RULE_13_LEVEL == "warn" ----------

def test_broken_fixture_routes_to_warnings_not_errors():
    assert lint_skills.RULE_13_LEVEL == "warn"
    report = run_rule13(BROKEN)
    assert _r13(report.warnings), "broken modes: fixture must produce rule-13 findings"
    assert _r13(report.errors) == [], (
        "rule-13 findings must be WARN (not HARD) while the level token is 'warn': "
        f"{report.errors}"
    )


def test_broken_fixture_fires_each_specific_structural_break():
    findings = _r13(run_rule13(BROKEN).warnings)
    joined = "\n".join(findings)
    assert "detected_by" in joined, findings          # missing detected_by
    assert "need >=3" in joined, findings             # floor <3 items
    assert "missing id" in joined, findings           # item without id
    assert "non-empty list" in joined, findings       # empty anchors list
    assert "min_matches" in joined, findings          # min_matches: 0
    assert "Omission lens" in joined, findings        # section absent


# --- (b) the level flip routes the SAME fixture to errors -----------------------

def test_level_flip_to_error_routes_same_fixture_to_errors(monkeypatch):
    monkeypatch.setattr(lint_skills, "RULE_13_LEVEL", "error")
    report = run_rule13(BROKEN)
    assert _r13(report.errors), (
        "under RULE_13_LEVEL='error' the broken fixture must route to report.errors"
    )
    assert _r13(report.warnings) == [], report.warnings


def test_level_flip_does_not_touch_rules_11_12_token(monkeypatch):
    # Flipping rule 13 must leave the rules-11/12 severity token untouched —
    # the two staged switches are independent by construction.
    monkeypatch.setattr(lint_skills, "RULE_13_LEVEL", "error")
    assert lint_skills.RULE_11_12_LEVEL == "error"
    monkeypatch.setattr(lint_skills, "RULE_13_LEVEL", "warn")
    assert lint_skills.RULE_11_12_LEVEL == "error"


# --- (c) well-formed fixture: zero rule-13 findings ------------------------------

def test_well_formed_fixture_yields_zero_rule13_findings():
    report = run_rule13(WELL_FORMED)
    assert _r13(report.errors + report.warnings) == [], (
        "a structurally valid modes: map + omission-lens section must yield "
        f"ZERO rule-13 findings: {report.errors + report.warnings}"
    )


# --- (d) un-compilable anchor: a finding, never a crash --------------------------

def test_bad_anchor_is_a_finding_not_a_crash():
    # Must not raise (the try/except re.error inside the rule).
    report = run_rule13(BAD_ANCHOR)
    findings = _r13(report.warnings)
    assert any("does not compile" in f for f in findings), findings
    # The bad-anchor fixture is otherwise well-formed: the compile failure is
    # the ONLY finding (presence floor — no collateral findings).
    assert len(findings) == 1, findings
    assert _r13(report.errors) == []


# --- (18-REVIEW W3) min_matches must not exceed the anchor count -----------------

def test_min_matches_exceeding_anchor_count_is_a_warn_finding():
    # A floor item with min_matches: 3 but only 2 anchors can NEVER be
    # covered_by_content (content_hits counts DISTINCT matching anchors) —
    # uncoverable by construction. Rule 13 must flag it, WARN-routed while
    # RULE_13_LEVEL == "warn" (the staged discipline is untouched).
    assert lint_skills.RULE_13_LEVEL == "warn"
    report = run_rule13(UNCOVERABLE)
    findings = _r13(report.warnings)
    assert len(findings) == 1, findings  # the ONLY finding on this fixture
    assert "min_matches (3)" in findings[0], findings
    assert "anchor count (2)" in findings[0], findings
    assert "item-2" in findings[0], findings
    assert _r13(report.errors) == []


def test_min_matches_equal_to_anchor_count_is_not_flagged():
    # Boundary: the well-formed fixture's item-3 declares min_matches: 2 with
    # exactly 2 anchors — satisfiable, must stay finding-free (already pinned
    # by the zero-findings test; re-asserted here as the explicit boundary).
    report = run_rule13(WELL_FORMED)
    assert _r13(report.errors + report.warnings) == []


def test_uncoverable_min_matches_does_not_double_fire_on_invalid_shapes():
    # The broken-modes fixture's shapeless item (anchors: [] + min_matches: 0)
    # must keep firing exactly its OWN findings — the new satisfiability check
    # is an `elif` and must not stack a second min_matches finding on top.
    findings = _r13(run_rule13(BROKEN).warnings)
    mm_findings = [f for f in findings if "min_matches" in f]
    assert len(mm_findings) == 1, mm_findings
    assert "int >=1" in mm_findings[0]


# --- presence-floor boundary: missing file is rule 12's finding, not rule 13's ---

def test_missing_sme_review_file_is_silent_for_rule13(tmp_path):
    # Rule 12 already reports a missing references/sme-review.md; rule 13 must
    # not double-fire on the same absence.
    empty_skill = tmp_path / "no-sme-review"
    (empty_skill / "references").mkdir(parents=True)
    report = run_rule13(empty_skill)
    assert _r13(report.errors + report.warnings) == []
