"""Assistive-boundary contract for offshore-safety-case (MAR-01) — the ONLY assistive
skill of Phase 16, built as a deliberate mirror of comah-safety-report-assistant.

MAR-01 ASSEMBLES / STRUCTURES the SI 2015/398 (SCR 2015) Schedule 6/7 safety-case
argument (claim -> argument -> evidence); it does NOT author the underlying engineering.
This test pins the four assistive-boundary invariants over the skill's golden CANDIDATE
output and its SKILL.md body, mirroring comah's assistive discipline retargeted to
Schedule 6/7:

  (a) it RECORDS [GAP] for any unsupplied element / figure / barrier-effectiveness claim;
  (b) it NEVER emits an invented QRA / consequence figure or a fabricated ALARP demonstration
      (no computed major-accident frequency / consequence distance presented as the skill's own);
  (c) it NEVER asserts a barrier / SCE effective without a cited performance-standard /
      verifier-finding evidence reference;
  (d) it NEVER emits "accepted / approved / authorised" acceptance language — acceptance is
      the competent authority's (HSE + OPRED) act, which this output PRECEDES.

Pure deterministic Python over the on-disk artifacts: no network, no model, no key. Paths
resolve relative to the repo root so the suite runs from any working directory.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills" / "offshore-safety-case"
GOLDEN = SKILL / "evals" / "output" / "offshore-safety-case.md"
SKILL_MD = SKILL / "SKILL.md"
REPORT_CANONICAL = SKILL / "assets" / "offshore-safety-case.report.json"


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


# --- skill IS the only assistive one ------------------------------------------

def test_skill_is_assistive_status():
    """MAR-01 is the assistive skill: status: assistive in the frontmatter."""
    body = _read(SKILL_MD)
    assert re.search(r"(?m)^\s*status:\s*assistive\b", body), (
        "offshore-safety-case must carry metadata.status: assistive (the only assistive skill)"
    )


def test_skill_declares_records_not_produces():
    """The body must declare the assistive 'assembles/structures, never produces autonomously'
    posture (mirrors comah)."""
    body = _read(SKILL_MD).lower()
    assert "assistive" in body
    assert "never produces the safety case autonomously" in body, (
        "the assistive posture (never produces autonomously) is not stated in the body"
    )


# --- (a) records [GAP] for unsupplied elements --------------------------------

def test_golden_records_gap_for_unsupplied_element():
    """The golden CANDIDATE must RECORD [GAP] for at least one unsupplied Schedule 6/7
    element/figure (the external QRA / a missing SCE performance standard)."""
    g = _read(GOLDEN)
    assert "[GAP]" in g, "golden output records no [GAP] — the assistive gap discipline is absent"
    # The defining gap: the external QRA / ALARP demonstration is recorded [GAP], not invented.
    assert re.search(r"ALARP[^\n]*\[GAP\]|\[GAP\][^\n]*(QRA|external)", g, re.IGNORECASE), (
        "the external QRA / ALARP demonstration must be recorded [GAP] when unsupplied"
    )


# --- (b) no invented QRA / consequence figure / fabricated ALARP --------------

# A computed-and-presented-as-own QRA result: a scientific-notation frequency or a
# consequence distance asserted as the skill's own finding. The golden records external
# figures with provenance and records the ALARP demonstration as [GAP] when unsupplied;
# it must contain NO fabricated quantitative MAH frequency / consequence number.
_FREQ_RE = re.compile(r"\b\d(?:\.\d+)?\s*[eE]-?\d+\s*(?:per\s*year|/\s*year|/yr)\b")
_CONSEQUENCE_RE = re.compile(r"consequence distance[^.\n]*\b\d{2,4}\s*m\b", re.IGNORECASE)


def test_golden_has_no_invented_qra_or_consequence_number():
    """The golden CANDIDATE must contain NO computed major-accident frequency or consequence
    distance presented as the skill's own analysis (no-fabrication boundary)."""
    g = _read(GOLDEN)
    assert not _FREQ_RE.search(g), (
        "golden output presents a computed major-accident frequency — the skill must never "
        "compute/invent QRA numbers"
    )
    assert not _CONSEQUENCE_RE.search(g), (
        "golden output presents a computed consequence distance — the skill must never "
        "compute/invent consequence numbers"
    )


def test_golden_frames_external_figures_with_provenance():
    """The golden must state that QRA/consequence figures are EXTERNAL and recorded with
    provenance, never computed by the skill."""
    g = _read(GOLDEN).lower()
    assert "external" in g and ("provenance" in g)
    assert "never computed" in g or "not computed" in g or "does not compute" in g, (
        "golden must state external figures are recorded, never computed by the skill"
    )


# --- (c) no barrier / SCE asserted effective without evidence -----------------

# A leak: "<SCE> is effective" / "barrier is effective" with no nearby performance-standard
# or verifier evidence cue. In the golden, every "effective" appears as "Effective — evidenced"
# in the SCE table where a PS-/verifier reference is present, OR as the boundary statement
# ("asserts no barrier effective without a cited performance standard"). We assert there is NO
# bare un-evidenced effectiveness assertion.
_UNEVIDENCED_EFFECTIVE_RE = re.compile(
    r"(?:barrier|SCE|safety-critical element|detection)\b[^.\n]{0,40}\bis effective\b"
    r"(?![^.\n]{0,80}(?:performance standard|PS-|verifier|verification|evidenced))",
    re.IGNORECASE,
)


def test_golden_asserts_no_unevidenced_barrier_effective():
    """No barrier / SCE is asserted effective without a cited performance-standard / verifier
    evidence reference."""
    g = _read(GOLDEN)
    m = _UNEVIDENCED_EFFECTIVE_RE.search(g)
    assert not m, (
        f"golden asserts a barrier/SCE effective without performance-standard evidence: {m.group(0)!r}"
    )


def test_golden_records_gap_for_unevidenced_sce():
    """An SCE without a supplied performance standard must be recorded [GAP] / not asserted
    effective (the golden carries at least one such SCE)."""
    g = _read(GOLDEN)
    assert re.search(r"\[GAP\][^\n]*not asserted effective|not asserted effective", g, re.IGNORECASE), (
        "an unsupplied SCE performance standard must be recorded [GAP] and not asserted effective"
    )


# --- (d) no acceptance language ----------------------------------------------

# Acceptance is the competent authority's act. A LEAK is an ASSERTION that the safety case is
# accepted/approved/authorised. The golden legitimately DISCUSSES acceptance ("PRECEDES
# competent-authority acceptance", "does not assert 'accepted'") — so we forbid the positive
# assertion form, not the bare word.
_ACCEPTANCE_ASSERTION_RE = re.compile(
    r"\b(?:safety case|it|this)\b[^.\n]{0,40}\bis\b[^.\n]{0,20}\b(?:accepted|approved|authorised|authorized)\b",
    re.IGNORECASE,
)


def test_golden_emits_no_acceptance_assertion():
    """The golden CANDIDATE must NOT assert the safety case is accepted/approved/authorised."""
    g = _read(GOLDEN)
    m = _ACCEPTANCE_ASSERTION_RE.search(g)
    assert not m, (
        f"golden emits acceptance language (the assistive boundary forbids it): {m.group(0)!r}"
    )


def test_golden_states_acceptance_is_the_authoritys_act():
    """The golden must state acceptance is the competent authority's act and that the output
    PRECEDES it (the assistive disclaimer)."""
    g = _read(GOLDEN).lower()
    assert "precedes" in g and "acceptance" in g, (
        "golden must state the output precedes competent-authority acceptance"
    )
    assert "does not assert" in g and (
        "accepted" in g or "approved" in g or "authorised" in g
    ), "golden must explicitly disclaim accepted/approved/authorised status"


# --- regime currency (SI 2015/398 current, SCR 2005 legacy) -------------------

def test_golden_cites_current_regime_not_legacy_as_live():
    """SI 2015/398 is cited as current; SCR 2005 appears only as the named legacy reference."""
    g = _read(GOLDEN)
    assert "SI 2015/398" in g, "golden must cite SI 2015/398 (the current regime)"
    if "SCR 2005" in g:
        assert re.search(r"SCR 2005[^.\n]*(?:superseded|legacy)", g, re.IGNORECASE), (
            "SCR 2005 must appear only as the superseded/legacy reference, never as the live duty"
        )


# --- canonical report template carries the assistive boundary ----------------

def test_canonical_report_template_carries_assistive_boundary():
    """The canonical report.json template must carry the assistive disclaimer (precedes
    acceptance) and a [GAP]-bearing argument map — proof the rendered deliverable holds the
    boundary."""
    r = _read(REPORT_CANONICAL)
    assert "[GAP]" in r, "canonical report template records no [GAP]"
    assert "precedes" in r.lower() and "acceptance" in r.lower(), (
        "canonical report template must carry the precedes-acceptance assistive disclaimer"
    )
    assert not _ACCEPTANCE_ASSERTION_RE.search(r), (
        "canonical report template asserts accepted/approved/authorised status"
    )
