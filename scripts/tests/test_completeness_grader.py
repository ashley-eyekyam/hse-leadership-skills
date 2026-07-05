"""Unit tests for the keyless deterministic completeness grader (FND-04, D-10/D-11).

Pins the three-way split contract of `graders.completeness.grade_completeness`:

  * covered_by_content — an anchor matches the output OUTSIDE a gap segment;
  * covered_by_gap     — the output honestly NAMES the item as a gap (D-11:
                         honest surfacing is COVERED, never pressures a FILL);
  * missing            — silently absent.

Plus the two crash-proofing invariants:
  * an un-compilable author anchor degrades that item toward `missing` with a
    logged reason — the grader NEVER raises (T-18-01-01 ReDoS/re.error);
  * a skill with no modes map / a case with no mode key is a back-compat no-op
    (`scored: False`) so the 94 shipped modeless skills stay green under WARN.

Test-data hygiene: the gap-marker literal and anchor regex strings live ONLY
inside test data (built by concatenation), never as bare tokens in this file.
"""

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from graders import grade_completeness  # noqa: E402

# The pack's gap-marker literal, built by concatenation (kept out of bare text
# so a later negative grep over test sources never gates on this file).
_GAP = "[" + "GAP]"


def _write_sme_review(tmp_path: Path, frontmatter: str) -> Path:
    """Write a synthetic references/sme-review.md with the given frontmatter."""
    ref_dir = tmp_path / "references"
    ref_dir.mkdir(parents=True, exist_ok=True)
    p = ref_dir / "sme-review.md"
    p.write_text(frontmatter, encoding="utf-8")
    return p


_MODES_FM = """---
sme-review:
  personas:
    - Reviewer
modes:
  default:
    detected_by: always
    floor:
      - id: training-records
        description: "training records section"
        anchors: ["training records"]
        min_matches: 1
      - id: review-date
        description: "next review date stated"
        anchors: ["next review"]
        min_matches: 1
      - id: owner-assignment
        description: "named role owner for each action"
        anchors: ["action owner"]
        min_matches: 1
---
body
"""


def test_fully_covered_output_scores_full_coverage(tmp_path):
    sme = _write_sme_review(tmp_path, _MODES_FM)
    text = (
        "Training records are maintained per role.\n"
        "The next review is scheduled quarterly.\n"
        "Each action owner is a named role.\n"
    )
    v = grade_completeness(text, sme, "default")
    assert v["scored"] is True
    assert v["mode"] == "default"
    assert v["floor_total"] == 3
    assert sorted(v["covered_by_content"]) == [
        "owner-assignment", "review-date", "training-records"]
    assert v["covered_by_gap"] == []
    assert v["missing"] == []
    assert v["coverage_pct"] == 1.0
    assert v["error"] is None


def test_gap_naming_counts_as_covered_by_gap(tmp_path):
    sme = _write_sme_review(tmp_path, _MODES_FM)
    # review-date is not present as content, but the output HONESTLY names it
    # as a gap on a marker line -> covered_by_gap (D-11).
    text = (
        "Training records are maintained per role.\n"
        + _GAP + " review-date — the next review cadence was not provided.\n"
        + "Each action owner is a named role.\n"
    )
    v = grade_completeness(text, sme, "default")
    assert v["scored"] is True
    assert "review-date" in v["covered_by_gap"]
    assert "review-date" not in v["covered_by_content"]
    assert "review-date" not in v["missing"]
    assert v["coverage_pct"] == 1.0  # gap-surfacing is COVERED, never penalised


def test_gap_line_for_item_a_never_credits_silent_item_b(tmp_path):
    # 18-REVIEW CR-01 regression: gap-credit is bound to the item's OWN
    # identity (id / its own anchors), NEVER shared description words. item-B
    # is NEVER surfaced; item-A's honest gap line shares ordinary >=4-char
    # description words with item-B ("decision", "owner") — item-B must land
    # in `missing`, not `covered_by_gap`.
    fm = (
        "---\n"
        "modes:\n"
        "  default:\n"
        "    detected_by: always\n"
        "    floor:\n"
        "      - id: item-a\n"
        '        description: "approval decision owner sign-off"\n'
        '        anchors: ["approval authority"]\n'
        "        min_matches: 1\n"
        "      - id: item-b\n"
        '        description: "review date recorded for the decision"\n'
        '        anchors: ["review date"]\n'
        "        min_matches: 1\n"
        "---\n"
        "body\n"
    )
    sme = _write_sme_review(tmp_path, fm)
    text = (
        _GAP
        + " item-a — no approval authority or decision owner named for sign-off.\n"
    )
    v = grade_completeness(text, sme, "default")
    assert v["scored"] is True
    assert v["covered_by_gap"] == ["item-a"]
    assert v["missing"] == ["item-b"]  # silent absence stays MISSING
    assert v["coverage_pct"] == 0.5


def test_gap_line_matching_items_own_anchor_credits_that_item(tmp_path):
    # The item-identity binding admits the item's OWN anchors: a gap line that
    # does not carry the literal id but does match one of the item's anchors
    # still earns covered_by_gap (honest surfacing by the item's own signal).
    sme = _write_sme_review(tmp_path, _MODES_FM)
    text = (
        "Training records are maintained per role.\n"
        "Each action owner is a named role.\n"
        + _GAP + " the next review cadence was never confirmed with the site.\n"
    )
    v = grade_completeness(text, sme, "default")
    assert "review-date" in v["covered_by_gap"]  # via its own "next review" anchor
    assert v["missing"] == []


def test_silently_missing_item_lands_in_missing(tmp_path):
    sme = _write_sme_review(tmp_path, _MODES_FM)
    text = (
        "Training records are maintained per role.\n"
        "Each action owner is a named role.\n"
    )
    v = grade_completeness(text, sme, "default")
    assert v["scored"] is True
    assert v["missing"] == ["review-date"]
    assert v["coverage_pct"] == 2 / 3


def test_anchor_match_only_inside_gap_segment_is_not_content(tmp_path):
    sme = _write_sme_review(tmp_path, _MODES_FM)
    # The anchor phrase appears ONLY on the gap-marker line -> not content
    # coverage; the line also names the item id -> covered_by_gap.
    text = (
        "Training records are maintained per role.\n"
        "Each action owner is a named role.\n"
        + _GAP + " review-date — next review not confirmed with the site.\n"
    )
    v = grade_completeness(text, sme, "default")
    assert "review-date" in v["covered_by_gap"]
    assert "review-date" not in v["covered_by_content"]


def test_bad_regex_anchor_degrades_to_missing_without_raising(tmp_path):
    bad_anchor = "(" + "unclosed"  # un-compilable pattern, built in data
    fm = (
        "---\n"
        "modes:\n"
        "  default:\n"
        "    detected_by: always\n"
        "    floor:\n"
        "      - id: broken-item\n"
        '        description: "item with an un-compilable author anchor"\n'
        '        anchors: ["' + bad_anchor + '"]\n'
        "        min_matches: 1\n"
        "      - id: good-item\n"
        '        description: "item with a valid anchor"\n'
        '        anchors: ["escape routes"]\n'
        "        min_matches: 1\n"
        "---\n"
        "body\n"
    )
    sme = _write_sme_review(tmp_path, fm)
    v = grade_completeness("Escape routes are kept clear at all times.", sme, "default")
    assert v["scored"] is True  # the sweep never crashes on a bad anchor
    assert "broken-item" in v["missing"]
    assert "good-item" in v["covered_by_content"]
    assert any("broken-item" in r for r in v["reasons"])  # reason logged


def test_overlong_anchor_is_rejected_defensively(tmp_path):
    long_anchor = "a" * 2048  # over the defensive length cap
    fm = (
        "---\n"
        "modes:\n"
        "  default:\n"
        "    detected_by: always\n"
        "    floor:\n"
        "      - id: capped-item\n"
        '        description: "item with an over-long anchor"\n'
        '        anchors: ["' + long_anchor + '"]\n'
        "        min_matches: 1\n"
        "---\n"
        "body\n"
    )
    sme = _write_sme_review(tmp_path, fm)
    v = grade_completeness("a" * 4096, sme, "default")
    assert v["scored"] is True
    assert "capped-item" in v["missing"]
    assert any("capped-item" in r for r in v["reasons"])


def test_no_modes_map_is_a_backcompat_noop(tmp_path):
    fm = "---\nsme-review:\n  personas:\n    - Reviewer\n---\nbody\n"
    sme = _write_sme_review(tmp_path, fm)
    v = grade_completeness("any output text", sme, "default")
    assert v["scored"] is False
    assert v["reason"] == "no modes declared"


def test_no_mode_key_is_a_backcompat_noop(tmp_path):
    sme = _write_sme_review(tmp_path, _MODES_FM)
    v = grade_completeness("any output text", sme, "")
    assert v["scored"] is False
    assert v["reason"] == "no modes declared"


def test_missing_sme_review_file_is_a_backcompat_noop(tmp_path):
    v = grade_completeness("any output text", tmp_path / "references" / "sme-review.md",
                           "default")
    assert v["scored"] is False
    assert v["reason"] == "no modes declared"


def test_unknown_mode_records_error_and_is_not_scored(tmp_path):
    sme = _write_sme_review(tmp_path, _MODES_FM)
    v = grade_completeness("any output text", sme, "no-such-mode")
    assert v["scored"] is False
    assert v["error"]  # error recorded (stated default per CONTEXT discretion)
    assert "no-such-mode" in v["error"]


def test_malformed_modes_yaml_never_raises(tmp_path):
    # modes present but not a mapping -> back-compat no-op, never an exception
    # (T-18-01-02 tampering: malformed modes must not crash the WARN sweep).
    fm = "---\nmodes: just-a-string\n---\nbody\n"
    sme = _write_sme_review(tmp_path, fm)
    v = grade_completeness("any output text", sme, "default")
    assert v["scored"] is False
    assert v["reason"] == "no modes declared"
