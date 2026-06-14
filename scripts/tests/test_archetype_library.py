"""A6 ORCH-02/04 + SME-01/04 durable contract — KB-SNIP-ARCHETYPES library completeness.

The A8 quality harness (Phase 3 Plan 04) keys off this durable test. It re-asserts,
over the on-disk archetype library + the prompt-snippets registry:

  (a) knowledge-base/prompt-snippets/subagent-archetypes.md exists and is the
      KB-SNIP-ARCHETYPES fragment;
  (b) it enumerates the 7 core archetypes (Researcher, Regulatory-Checker,
      Risk-Scorer, Drafter, Critic/QA, De-identifier, Formatter) and the 3 optional;
  (c) it carries the HSE-SME reviewer persona hook with its FULL flag list
      (generic controls, PPE/admin-only, un-named owners, missing review triggers,
      un-evidenced claims, "survive a regulator") and frames it as decision-support
      that precedes — never replaces — a human competent-person review (SME-01/02);
  (d) it names the 5 sector-persona extension slots (Process-Safety,
      Chemical-Process-Safety, India-Regulatory, Aviation-SMS, Mine Manager) — SME-04;
  (e) it cross-references KB-SNIP-DEID-ARCHETYPE (the De-identifier canonical source);
  (f) KB-SNIP-ARCHETYPES resolves in prompt-snippets/_registry.yaml (rule-9 clean).

Plain pytest, sandbox-offline, stdlib (re + pathlib) + pyyaml. Paths resolve relative
to this test file — mirrors knowledge-base/tests/test_kb_resolution.py's registry idiom.
"""

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]

PROMPT_SNIPPETS = REPO / "knowledge-base" / "prompt-snippets"
LIBRARY = PROMPT_SNIPPETS / "subagent-archetypes.md"
REGISTRY = PROMPT_SNIPPETS / "_registry.yaml"

CORE_ARCHETYPES = [
    "Researcher",
    "Regulatory-Checker",
    "Risk-Scorer",
    "Drafter",
    "Critic/QA",
    "De-identifier",
    "Formatter",
]

OPTIONAL_ARCHETYPES = [
    "Stakeholder-Mapper",
    "Benchmarker",
    "Synthesizer",
]

SECTOR_SLOTS = [
    "Process-Safety",
    "Chemical-Process-Safety",
    "India-Regulatory",
    "Aviation-SMS",
    "Mine Manager",
]

SME_FLAG_TOKENS = [
    "generic controls",
    "PPE",
    "un-named owners",
    "review trigger",
    "un-evidenced",
    "survive a regulator",
]


def _read(p):
    return p.read_text(encoding="utf-8")


# (a) library exists ------------------------------------------------------------

def test_library_exists_and_is_the_archetypes_fragment():
    assert LIBRARY.exists(), "knowledge-base/prompt-snippets/subagent-archetypes.md missing"
    body = _read(LIBRARY)
    assert "KB-SNIP-ARCHETYPES" in body, "library must declare its KB-SNIP-ARCHETYPES fragment id"


# (b) 7 core + 3 optional archetypes -------------------------------------------

def test_library_has_all_seven_core_archetypes():
    body = _read(LIBRARY)
    for name in CORE_ARCHETYPES:
        assert name in body, f"archetype library missing core archetype: {name}"


def test_library_has_three_optional_archetypes():
    body = _read(LIBRARY)
    for name in OPTIONAL_ARCHETYPES:
        assert name in body, f"archetype library missing optional archetype: {name}"


# (c) HSE-SME reviewer persona hook + full flag list (SME-01/02) ----------------

def test_library_has_hse_sme_reviewer_hook():
    body = _read(LIBRARY)
    assert "HSE-SME" in body, "archetype library missing the HSE-SME reviewer persona hook"


def test_sme_reviewer_enumerates_full_flag_list():
    body = _read(LIBRARY).lower()
    for tok in SME_FLAG_TOKENS:
        assert tok.lower() in body, f"SME-reviewer persona missing flag: {tok!r}"


def test_sme_reviewer_is_decision_support_not_competent_person_signoff():
    body = _read(LIBRARY).lower()
    assert "competent person" in body or "competent-person" in body, (
        "SME-reviewer must reference the human competent-person review it precedes"
    )
    assert "decision-support" in body or "decision support" in body, (
        "SME-reviewer must be framed as decision-support (never AI-approving) — SME-02 boundary"
    )


# (d) 5 named sector-persona slots (SME-04) ------------------------------------

def test_library_names_all_five_sector_slots():
    body = _read(LIBRARY)
    for slot in SECTOR_SLOTS:
        assert slot in body, f"archetype library missing sector-persona slot: {slot}"


# (e) De-identifier reconciliation cross-reference ------------------------------

def test_library_cross_references_deid_archetype_canonical_source():
    body = _read(LIBRARY)
    assert "KB-SNIP-DEID-ARCHETYPE" in body, (
        "archetype library must cross-reference KB-SNIP-DEID-ARCHETYPE (De-identifier canonical source)"
    )


# (f) KB-SNIP-ARCHETYPES resolves in _registry.yaml (rule-9 clean) -------------

def test_archetypes_id_registered_in_registry():
    entries = yaml.safe_load(_read(REGISTRY))
    assert isinstance(entries, list), "_registry.yaml must be a list of fragment entries"
    ids = {e.get("id") for e in entries}
    assert "KB-SNIP-ARCHETYPES" in ids, "KB-SNIP-ARCHETYPES not registered in prompt-snippets/_registry.yaml"


def test_registered_file_matches_library():
    entries = yaml.safe_load(_read(REGISTRY))
    entry = next(e for e in entries if e.get("id") == "KB-SNIP-ARCHETYPES")
    assert entry.get("file") == "subagent-archetypes.md", (
        "KB-SNIP-ARCHETYPES registry entry must point at subagent-archetypes.md"
    )
