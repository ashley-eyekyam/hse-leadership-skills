"""A6 ORCH-01..03 durable contract — orchestration block byte-identity + §3.1 structure.

The A8 quality harness (Phase 3 Plan 04) keys off this durable test, not a one-shot
check. It re-asserts, over the on-disk artifacts:

  (a) the `hse:block:orchestration` marked region is BYTE-IDENTICAL across
      template/blocks/orchestration.md and template/SKILL.md (the anti-drift
      contract — manual byte-sync until forge --sync lands in Phase 4);
  (b) the region carries the full A6 §3.1 structure (Step 0 triage, Step 4
      mandatory Critic/QA, literal MAX=6, single-thread fallback, De-identifier
      sequencing, the KB-SNIP-ARCHETYPES pointer);
  (c) the region contains NO PLACEHOLDER / TODO / {{ substitution token;
  (d) the single-threaded roster one-liner is present BELOW :end in
      template/SKILL.md (ORCH-03, presence-only subsection).

Plain pytest, sandbox-offline, stdlib only (re + pathlib). Paths resolve relative
to this test file so the suite runs from any working directory — mirrors
tests/test_deid_contract.py's region-extraction idiom.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

BLOCK = REPO / "template" / "blocks" / "orchestration.md"
TEMPLATE_SKILL = REPO / "template" / "SKILL.md"

ORCH_REGION_RE = re.compile(
    r"<!-- hse:block:orchestration:start -->.*?<!-- hse:block:orchestration:end -->",
    re.S,
)

REQUIRED_SUBSTRINGS = [
    "### Step 0",
    "### Step 4 — Critic",
    "MAX=6",
    "Single-threaded fallback",
    "De-identif",
    "KB-SNIP-ARCHETYPES",
]

FORBIDDEN_TOKENS = ["PLACEHOLDER", "TODO", "{{"]


def _read(p):
    return p.read_text(encoding="utf-8")


def _region(p):
    m = ORCH_REGION_RE.search(_read(p))
    assert m, f"no hse:block:orchestration marked region in {p}"
    return m.group(0)


# (a) anti-drift byte-sync ------------------------------------------------------

def test_orchestration_region_byte_identical_across_block_and_template_skill():
    rb = _region(BLOCK)
    rt = _region(TEMPLATE_SKILL)
    assert rb == rt, "template/SKILL.md orchestration region drifted from blocks/orchestration.md"


# (b) full §3.1 structure -------------------------------------------------------

def test_block_region_carries_full_a6_structure():
    region = _region(BLOCK)
    for tok in REQUIRED_SUBSTRINGS:
        assert tok in region, f"orchestration block missing required §3.1 substring: {tok!r}"


def test_block_max6_is_literal_not_substitution():
    region = _region(BLOCK)
    assert "MAX=6" in region, "MAX=6 must be a literal"
    assert "{{" not in region, "MAX must be hard-coded — no {{…}} substitution token"


# (c) no placeholder / todo / substitution -------------------------------------

def test_block_region_has_no_forbidden_tokens():
    region = _region(BLOCK)
    for tok in FORBIDDEN_TOKENS:
        assert tok not in region, f"orchestration block still contains forbidden token: {tok!r}"


def test_template_skill_region_has_no_forbidden_tokens():
    region = _region(TEMPLATE_SKILL)
    for tok in FORBIDDEN_TOKENS:
        assert tok not in region, f"template SKILL.md orchestration region has forbidden token: {tok!r}"


# (d) single-threaded roster one-liner below :end (ORCH-03) --------------------

def test_single_threaded_roster_one_liner_below_end():
    text = _read(TEMPLATE_SKILL)
    end_marker = "<!-- hse:block:orchestration:end -->"
    idx = text.index(end_marker)
    after = text[idx + len(end_marker):]
    # stop at the next top-level block marker so we only inspect the roster subsection
    nxt = re.search(r"<!-- hse:block:", after)
    roster = after[: nxt.start()] if nxt else after
    assert "Single-threaded by design — no subagents." in roster, (
        "ORCH-03 single-threaded roster one-liner missing below :end in template/SKILL.md"
    )
