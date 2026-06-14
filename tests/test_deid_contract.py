"""Persistent DEID-01/02/03 observable contract (A5 → A8).

This is the durable contract test the A8 quality harness keys off in Phase 3 —
NOT a one-shot inline check. It re-asserts, over the on-disk artifacts:

  (i)   the canonical deid block is finalized (five step tokens, no PLACEHOLDER);
  (ii)  the `hse:block:deid` marked region is byte-identical across
        template/blocks/deid.md, template/SKILL.md, and the fixture SKILL.md
        (the anti-drift contract — manual byte-sync until forge --sync, Phase 4);
  (iii) references/deid-checklist.md enumerates the 18 HIPAA Safe-Harbor
        identifiers + HSE addendum, has secondary suppression, the 3-jurisdiction
        mechanism tokens, and no fabricated statute body;
  (iv)  the re-identification-key separation rule appears in BOTH the deid block
        step 2 AND checklist §7;
  (v)   the fixture checklist is a real copy of the canonical (no placeholder).

Plain pytest, sandbox-offline, no framework config — mirrors the
assets/report-engine/tests style. Paths resolve relative to the repo root so the
suite runs from any working directory.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

BLOCK = REPO / "template" / "blocks" / "deid.md"
TEMPLATE_SKILL = REPO / "template" / "SKILL.md"
FIXTURE_SKILL = REPO / "examples" / "risk-assessment" / "SKILL.md"
CHECKLIST = REPO / "references" / "deid-checklist.md"
FIXTURE_CHECKLIST = REPO / "examples" / "risk-assessment" / "references" / "deid-checklist.md"
ARCHETYPE = REPO / "knowledge-base" / "prompt-snippets" / "deidentifier-archetype.md"

DEID_REGION_RE = re.compile(
    r"<!-- hse:block:deid:start -->.*?<!-- hse:block:deid:end -->", re.S
)

STEP_TOKENS = [
    "DETECT & FLAG",
    "PSEUDONYMIZE BY DEFAULT",
    "AGGREGATE SMALL NUMBERS",
    "WARN BEFORE WIDE DISTRIBUTION",
    "MINIMIZE & LIMIT PURPOSE",
]


def _read(p):
    return p.read_text(encoding="utf-8")


def _region(p):
    m = DEID_REGION_RE.search(_read(p))
    assert m, f"no hse:block:deid marked region in {p}"
    return m.group(0)


# (i) canonical block finalized -------------------------------------------------

def test_block_has_all_five_step_tokens():
    blk = _read(BLOCK)
    for tok in STEP_TOKENS:
        assert tok in blk, f"deid block missing step token: {tok}"


def test_block_has_no_placeholder():
    assert "PLACEHOLDER" not in _read(BLOCK), "deid block still has PLACEHOLDER"


def test_block_is_pseudonymize_by_default():
    # Active default (D-03), not the softened "offer".
    assert "PSEUDONYMIZE BY DEFAULT" in _read(BLOCK)


# (ii) anti-drift byte-sync -----------------------------------------------------

def test_deid_region_byte_identical_across_block_and_both_skills():
    rb = _region(BLOCK)
    rt = _region(TEMPLATE_SKILL)
    rf = _region(FIXTURE_SKILL)
    assert rb == rt, "template/SKILL.md deid region drifted from blocks/deid.md"
    assert rb == rf, "fixture SKILL.md deid region drifted from blocks/deid.md"


def test_skill_regions_have_no_placeholder():
    assert "PLACEHOLDER" not in _region(TEMPLATE_SKILL)
    assert "PLACEHOLDER" not in _region(FIXTURE_SKILL)


# (iii) checklist substance -----------------------------------------------------

def test_checklist_enumerates_18_hipaa_identifiers():
    c = _read(CHECKLIST)
    # 18 enumerated list items in the scrub-checklist section (1. .. 18.).
    numbered = re.findall(r"(?m)^\d+\.\s", c)
    assert len(numbered) >= 18, f"expected >=18 enumerated identifiers, found {len(numbered)}"


def test_checklist_has_hse_addendum():
    c = _read(CHECKLIST)
    assert "HSE addendum" in c
    assert "Aadhaar" in c, "HSE addendum must include Aadhaar / national-ID"


def test_checklist_has_small_cell_and_secondary_suppression():
    c = _read(CHECKLIST)
    assert "secondary suppression" in c
    # <5 small-cell rule present (either "5" threshold wording).
    assert "fewer than 5" in c or "< 5" in c or "<5" in c


def test_checklist_has_three_jurisdiction_mechanism_tokens():
    c = _read(CHECKLIST)
    for tok in ["29 CFR 1904.29", "Art. 9", "DPDP"]:
        assert tok in c, f"checklist missing jurisdiction mechanism token: {tok}"


def test_checklist_quickref_is_mechanism_only_no_fabricated_statute():
    # Guard against a reproduced statute body. The quick-ref must point at
    # mechanisms, not quote statutory text. Flag obvious statute-body markers.
    c = _read(CHECKLIST).lower()
    fabricated_markers = [
        "section 1 of the",
        "shall mean",
        "hereinafter referred to as",
        "provided that nothing in this",
    ]
    for m in fabricated_markers:
        assert m not in c, f"checklist appears to reproduce statute text: {m!r}"


# (iv) re-id key separation rule in BOTH block step 2 AND checklist §7 ----------

def test_reid_key_separation_rule_in_block_and_checklist():
    blk = _read(BLOCK)
    chk = _read(CHECKLIST)
    # Block step 2: separate key, never in the document.
    assert "SEPARATE re-identification key" in blk
    assert "Never put the key" in blk
    # Checklist §7: separate artifact, never embedded.
    assert "Re-identification key handling" in chk
    assert "never" in chk.lower() and "embedded" in chk.lower()


# (v) fixture checklist is a real copy of the canonical ------------------------

def test_fixture_checklist_is_real_copy_no_placeholder():
    assert FIXTURE_CHECKLIST.exists(), "fixture deid-checklist missing"
    assert not FIXTURE_CHECKLIST.is_symlink(), "fixture checklist must be a real copy, not a symlink"
    f = _read(FIXTURE_CHECKLIST)
    assert "placeholder" not in f.lower(), "fixture checklist still a placeholder"
    assert "secondary suppression" in f
    # Byte-identical real copy of the canonical.
    assert f == _read(CHECKLIST), "fixture checklist is not a verbatim copy of the canonical"


# archetype handed to A6 -------------------------------------------------------

def test_archetype_runs_first_and_returns_key_separately():
    a = _read(ARCHETYPE)
    assert "Runs FIRST" in a or "runs first" in a.lower()
    assert "SEPARATE" in a.upper() or "separate" in a
    assert "tools" in a.lower() and "none" in a.lower(), "archetype must declare no tools"
