"""FND-01 completeness-contract grep tests (D-05, the D-10 contract-test pattern).

Pins the Phase-18 staged-carrier invariant over the on-disk artifacts:

  (i)   every lens token is PRESENT in the staged next-version block
        (template/blocks/staged/orchestration.md — the exact future bytes for
        the Phase-20 atomic cutover), inside its marked region;
  (ii)  every lens token is PRESENT in the live block
        (template/blocks/orchestration.md — promoted at the Phase-20 atomic
        cutover). This is the "cutover applied" invariant: the suite FAILS if
        any lens string is missing from the live block after cutover;
  (iii) the staged block retains the orchestration start/end markers
        byte-identical to the live block (the cutover is a byte-exact copy);
  (iv)  the completeness KB snippet resolves — the snippet file exists in
        prompt-snippets/ AND its registry row resolves via the linter's own
        Rule-9 resolver.

The gated literals live ONLY in the module constants below (KB_ID,
LENS_TOKENS, SNIPPET_TOKENS — no duplicates in comments or docstrings) so any
future owner LOCK can re-pin them to newly approved bytes with a one-place
edit. These are the OWNER-LOCKED bytes: approved at the consolidated 18-10
review (CONV-5 / D-09, 2026-07-05). Full approved carrier lines are pinned
verbatim; any drift in the staged block or the snippet BREAKS this suite
until a new owner LOCK re-pins the constants.

Plain pytest, sandbox-offline, no framework config — mirrors
tests/test_deid_contract.py. Paths resolve relative to the repo root so the
suite runs from any working directory.
"""

import re
import sys as _sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]

STAGED = REPO / "template" / "blocks" / "staged" / "orchestration.md"
LIVE = REPO / "template" / "blocks" / "orchestration.md"
SNIPPET = REPO / "knowledge-base" / "prompt-snippets" / "completeness-lens.md"
REGISTRY = REPO / "knowledge-base" / "prompt-snippets" / "_registry.yaml"

_SCRIPTS = REPO / "scripts"
if str(_SCRIPTS) not in _sys.path:
    _sys.path.insert(0, str(_SCRIPTS))

from lint_skills import resolve_kb_id  # noqa: E402

ORCH_REGION_RE = re.compile(
    r"<!-- hse:block:orchestration:start -->.*?<!-- hse:block:orchestration:end -->",
    re.S,
)

START_MARKER = "<!-- hse:block:orchestration:start -->"
END_MARKER = "<!-- hse:block:orchestration:end -->"

# ---------------------------------------------------------------------------
# The re-pinnable constants (OWNER-LOCKED — pinned to the bytes approved at the
# consolidated 18-10 owner review, CONV-5 / D-09, 2026-07-05). Each token sits
# on ONE line in its carrier file, so plain substring matching is exact.
# ---------------------------------------------------------------------------

KB_ID = "KB-SNIP-COMPLETENESS"
KB_FILE = "completeness-lens.md"

LENS_TOKENS = [
    # The Step-4 MANDATE strings (short leak-sentinels — these must also stay
    # ABSENT from the live block until the Phase-20 cutover).
    "Omission lens",
    "detect the emitted mode",
    "never fabricate",
    KB_ID,
    # The named single-thread omission-pass clause — the load-bearing line for
    # hosts with no subagent capability.
    "run the Omission lens absence-listing pass yourself",
    # The owner-LOCKED exact carrier lines, pinned verbatim (one line each in
    # the staged block's marked region).
    "Omission lens (the SECOND, unconstrained omission pass): detect the emitted mode,",
    "list what a competent consultant would have included for THIS mode BEFORE checking",
    "the mode's floor, surface every miss as a `[GAP]` / deficiency-list entry, and",
    "never fabricate content to fill a gap (protocol: `KB-SNIP-COMPLETENESS`).",
    "run the Omission lens absence-listing pass yourself (unconstrained, BEFORE the floor",
    "check — surface misses as `[GAP]`, never fabricate), and pass the review before",
]

# The D-07 PROTOCOL carriers the snippet must hold (single source) — the short
# section anchors plus the owner-LOCKED exact protocol lines, pinned verbatim.
SNIPPET_TOKENS = [
    "must-list-then-refute",
    "Bounded single-pass exit",
    "[GAP]",
    "never fabricate",
    "Verbosity guard",
    # The owner-LOCKED exact carrier lines (one line each in the snippet).
    "**Fragment ID:** `KB-SNIP-COMPLETENESS`",
    "1. **Detect the emitted mode.** Identify which mode (from the skill's",
    "5. **Surface — never fabricate.** Every real miss becomes a `[GAP]` / deficiency-list",
    "Run the lens ONCE per review cycle. Do not loop it until it finds nothing — one",
    "deficiency list with item names and one-line reasons. Never pad the artifact or the",
]


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _region(p: Path) -> str:
    m = ORCH_REGION_RE.search(_read(p))
    assert m, f"no hse:block:orchestration marked region in {p}"
    return m.group(0)


# (i) lens tokens PRESENT in the staged block -----------------------------------

def test_staged_block_exists():
    assert STAGED.is_file(), "staged next-version block is missing"


def test_lens_tokens_present_in_staged():
    staged = _read(STAGED)
    for tok in LENS_TOKENS:
        assert tok in staged, f"staged block missing lens token: {tok!r}"


def test_lens_tokens_sit_inside_the_staged_marked_region():
    region = _region(STAGED)
    for tok in LENS_TOKENS:
        assert tok in region, (
            f"lens token {tok!r} sits outside the staged marked region — it "
            "would not survive the Phase-20 copy + forge --sync"
        )


# (ii) lens tokens PRESENT in the live block — post-cutover invariant -----------
# Phase-20 GATE-01 atomic cutover: the staged bytes are now promoted live, so the
# D-10 pre-flight invariant is INVERTED — every lens token that had to stay ABSENT
# until the cutover must now be PRESENT in the live block (and, since live == staged,
# test_staged_markers_byte_identical_to_live still holds).

def test_lens_tokens_present_in_live_block():
    live = _read(LIVE)
    for tok in LENS_TOKENS:
        assert tok in live, (
            f"lens token {tok!r} is missing from the LIVE block after the "
            "Phase-20 atomic cutover — template/blocks/orchestration.md must "
            "carry the promoted omission-lens bytes (GATE-01)"
        )


# (iii) marker byte-identity staged <-> live ------------------------------------

def test_staged_markers_byte_identical_to_live():
    staged = _read(STAGED)
    live = _read(LIVE)
    for marker in (START_MARKER, END_MARKER):
        assert marker in staged, f"staged block missing marker {marker!r}"
        assert marker in live, f"live block missing marker {marker!r}"


def test_staged_block_is_exactly_one_marked_region():
    matches = ORCH_REGION_RE.findall(_read(STAGED))
    assert len(matches) == 1, (
        f"staged block must carry exactly ONE marked region, found {len(matches)}"
    )


# (iv) the completeness KB snippet resolves -------------------------------------

def test_completeness_snippet_file_exists():
    assert SNIPPET.is_file(), (
        "completeness snippet file missing from knowledge-base/prompt-snippets/"
    )


def test_completeness_registry_row_points_at_snippet_file():
    rows = yaml.safe_load(_read(REGISTRY)) or []
    matches = [e for e in rows if e.get("id") == KB_ID]
    assert len(matches) == 1, f"expected exactly one {KB_ID} registry row"
    row = matches[0]
    assert row.get("file") == KB_FILE, (
        f"registry row 'file' is {row.get('file')!r}, expected {KB_FILE!r}"
    )
    assert row.get("facets", {}).get("jurisdiction") == ["All"], (
        "registry row must carry jurisdiction: [All]"
    )


def test_completeness_kb_id_resolves_via_rule9():
    assert resolve_kb_id(KB_ID, REPO), (
        f"{KB_ID} does not resolve through the linter's Rule-9 resolver"
    )


def test_snippet_carries_the_protocol_tokens():
    body = _read(SNIPPET)
    for tok in SNIPPET_TOKENS:
        assert tok in body, f"completeness snippet missing protocol token: {tok!r}"
