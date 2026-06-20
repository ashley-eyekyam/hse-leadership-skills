"""Anti-drift contract for the marketing README (Plan 07-03, Unit E).

E authors zero new domain facts: the README's load-bearing claims are LIFTED or
REFERENCED from the artifact that owns them. These deterministic, stdlib-only checks
lock the contract so the public README cannot silently drift away from:

  * the verbatim DISCLAIMER.md trust line (Decision 3 — never paraphrased);
  * dynamic CI status badges (Decision 6 / §3.2 — never a hard-coded "passing");
  * the E §3.1 section spine (hero → catalog → install → 60-sec → trust → brand → roadmap);
  * the hse-all hero one-liner (D-15 — the prominent whole-pack install);
  * the absence of the D-03 Avoid-list hype phrases.

Run: python -m pytest tests/test_readme_contract.py -x
"""

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
DISCLAIMER = REPO / "DISCLAIMER.md"


@pytest.fixture(scope="module")
def readme_text() -> str:
    assert README.exists(), "README.md must exist"
    return README.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def disclaimer_text() -> str:
    assert DISCLAIMER.exists(), "DISCLAIMER.md must exist"
    return DISCLAIMER.read_text(encoding="utf-8")


def test_readme_quotes_disclaimer_trust_line_verbatim(readme_text, disclaimer_text):
    """The trust band must quote the canonical disclaimer VERBATIM, not paraphrase it."""
    # The first sentence of the canonical disclaimer body (DISCLAIMER.md line 5),
    # whitespace-normalised so a re-wrap doesn't break the byte check on intent.
    canonical = (
        "The HSE Leadership Skills pack is a **decision-support tool**. "
        "Its outputs are drafts to assist a qualified professional — **not** finished, "
        "authoritative, or approved deliverables. **Every output must be reviewed, "
        "validated, and signed off by a competent person**"
    )
    norm_readme = " ".join(readme_text.split())
    norm_canonical = " ".join(canonical.split())
    assert norm_canonical in norm_readme, (
        "README must quote the DISCLAIMER.md decision-support line verbatim "
        "(Decision 3 — link + quote, never reword)."
    )
    # And the canonical fragment must actually be present in DISCLAIMER.md (catches
    # a future disclaimer edit that would silently diverge from this expectation).
    assert norm_canonical in " ".join(disclaimer_text.split()), (
        "The expected verbatim line is no longer present in DISCLAIMER.md — "
        "update both surfaces together (A1 owns the wording)."
    )


def test_no_hardcoded_passing_badge(readme_text):
    """CI badges must be DYNAMIC GitHub-Actions status badges — never a literal 'passing'."""
    lowered = readme_text.lower()
    assert "passing" not in lowered, (
        "Found a hard-coded 'passing' claim — CI badges must be dynamic "
        "actions/workflows/*.yml/badge.svg status badges (§3.2)."
    )
    # The two CI workflow status badges must be present as dynamic-status URLs.
    for wf in ("validate-skills.yml", "eval.yml"):
        assert f"actions/workflows/{wf}/badge.svg" in readme_text, (
            f"Missing the dynamic CI status badge for {wf}."
        )


def test_all_e_section_headers_present(readme_text):
    """Every E §3.1 section must appear, in the README's canonical order:
    hero → install (30s) → catalog → 60-sec example → trust band →
    customize/brand → roadmap/community. The README is the source of truth;
    these anchors track its actual headers (install precedes catalog, and the
    catalog header carries its full "(the catalog)" parenthetical)."""
    ordered_anchors = [
        "# HSE Leadership Skills",              # 1 · hero
        "## Install in 30 seconds",             # 2 · install (30s quick start)
        "## What's in the box (the catalog)",   # 3 · catalog
        '## A 60-second "try it"',              # 4 · worked example
        "## Trust & safety",                    # 5 · trust band
        "## Customize & brand",                 # 6 · brand
        "## Roadmap & community",               # 7 · roadmap/community
    ]
    last = -1
    for anchor in ordered_anchors:
        idx = readme_text.find(anchor)
        assert idx != -1, f"Missing README section: {anchor!r}"
        assert idx > last, f"Section out of E §3.1 order: {anchor!r}"
        last = idx


def test_hse_all_hero_one_liner(readme_text):
    """The hse-all whole-pack install (D-15) must appear as the prominent hero install."""
    assert "/plugin marketplace add ashley-eyekyam/hse-leadership-skills" in readme_text, (
        "Missing the G13 marketplace-add line."
    )
    assert "hse-all@hse-leadership-skills" in readme_text, (
        "Missing the hse-all hero one-liner (D-15 — installs all 48 skills in one line)."
    )


def test_no_avoid_list_hype_phrases(readme_text):
    """None of the D-03 Avoid-list phrases may appear in the public README."""
    lowered = readme_text.lower()
    avoid = [
        "guarantees compliance",
        "ai-powered safety compliance",
        "automate safety management",
        "approved safety documents",
        "no hse expertise required",
        "revolutionary ai",
    ]
    hits = [p for p in avoid if p in lowered]
    assert not hits, f"D-03 Avoid-list phrase(s) present in README: {hits}"


def test_positioning_india_is_one_of_five(readme_text):
    """Decision 6 guardrail: the five sector packs are equal peers; India is one of five."""
    for pack in (
        "hse-process",
        "hse-chemicals",
        "hse-india",
        "hse-aviation",
        "hse-mining",
    ):
        assert pack in readme_text, f"Sector pack {pack} missing from catalog (must be equal-peer)."
