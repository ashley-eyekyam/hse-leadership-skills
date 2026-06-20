"""test_review_v101.py — regression locks for the Phase-7 v1.0.1 code-review fixes.

Each test pins the FIXED behavior from 07-REVIEW.md so a future regression hard-fails:

  CR-01 — emitted instruction surfaces ship NO repo-relative file pointer
          (`../../knowledge-base/…`, `references/<file>`, `branding/<file>`); every
          pointer is rehomed to the flat on-host `knowledge/<basename>` layout, and
          `branding/company-card.yaml` is actually bundled so the attribution resolves.
  WR-01 — the orchestration single-thread fallback prose survives intact (no dangling
          `Single-threaded fallback:` header).
  WR-02 — the HoC discipline is inline on the ChatGPT engine path, and the validator's
          HoC check requires the discipline phrase, not a path pointer.
  WR-03 — a knowledge-file basename collision fails loud instead of silently
          overwriting.
"""

import re

import pytest

import build
import validate_adapters as va

# Every shipped skill × every platform — the regression must hold across the full tree.
_REPO_RELATIVE_RE = re.compile(
    r"(?:\.\./)+knowledge-base/"
    r"|\breferences/[A-Za-z0-9_.-]+\.\w+"
    r"|\bbranding/[A-Za-z0-9_.-]+\.\w+"
)
_KNOWLEDGE_POINTER_RE = re.compile(r"\bknowledge/([A-Za-z0-9_.-]+\.\w+)")
_INSTRUCTION_FILE = build._INSTRUCTION_FILE


def _emit(skill_dir, platform, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / platform / adapted.name
    build.emit(adapted, platform, out, platforms)
    return adapted, out


# --- CR-01 -----------------------------------------------------------------------


@pytest.mark.parametrize("platform", build.PLATFORMS)
def test_cr01_no_repo_relative_pointer_in_instructions(risk_assessment_dir, platform, tmp_path):
    """No `../../`, `references/<file>`, or `branding/<file>` pointer survives — they are
    DEAD on a host that flattens uploads to knowledge/<basename>."""
    _adapted, out = _emit(risk_assessment_dir, platform, tmp_path)
    instr = (out / _INSTRUCTION_FILE[platform]).read_text(encoding="utf-8")
    leaked = _REPO_RELATIVE_RE.findall(instr)
    assert not leaked, f"repo-relative pointer(s) leaked into {platform} instructions: {leaked}"


@pytest.mark.parametrize("platform", build.PLATFORMS)
def test_cr01_every_knowledge_pointer_resolves(risk_assessment_dir, platform, tmp_path):
    """Every rehomed `knowledge/<file>` pointer in the instructions resolves to an
    actually-uploaded file in the bundle's knowledge/ directory."""
    _adapted, out = _emit(risk_assessment_dir, platform, tmp_path)
    instr = (out / _INSTRUCTION_FILE[platform]).read_text(encoding="utf-8")
    present = {p.name for p in (out / "knowledge").iterdir() if p.is_file()}
    for base in _KNOWLEDGE_POINTER_RE.findall(instr):
        assert base in present, f"{platform}: knowledge/{base} pointed at but not uploaded"


@pytest.mark.parametrize("platform", build.PLATFORMS)
def test_cr01_company_card_bundled_and_attribution_resolves(risk_assessment_dir, platform, tmp_path):
    """`branding/company-card.yaml` is bundled into knowledge/, and the attribution
    pointer (when it survives char-fit — the Attribution section is spillable) is the
    rehomed `knowledge/company-card.yaml`, never the dead `branding/` form."""
    _adapted, out = _emit(risk_assessment_dir, platform, tmp_path)
    # The card is always bundled, even if the attribution prose is spilled to knowledge.
    assert (out / "knowledge" / "company-card.yaml").is_file()
    instr = (out / _INSTRUCTION_FILE[platform]).read_text(encoding="utf-8")
    # The dead `branding/` pointer must never appear; if the rehomed pointer survives the
    # spill, it points into knowledge/ (and resolves — asserted by the resolver test).
    assert "branding/company-card.yaml" not in instr
    if "company-card.yaml" in instr:
        assert "knowledge/company-card.yaml" in instr


# --- WR-01 -----------------------------------------------------------------------


@pytest.mark.parametrize("platform", build.PLATFORMS)
def test_wr01_single_thread_fallback_prose_survives(risk_assessment_dir, platform, tmp_path):
    """The fallback is no longer truncated to a dangling header — the skill's own
    fallback words (de-id scrub first · scope discipline · the promoted SME Review &
    Sign-off pass) survive."""
    _adapted, out = _emit(risk_assessment_dir, platform, tmp_path)
    instr = (out / _INSTRUCTION_FILE[platform]).read_text(encoding="utf-8")
    assert "Single-threaded fallback:" in instr
    # The continuation prose (not just the header) must be present — the FND-07/08
    # promoted "SME Review & Sign-off" wording (was "Critic/QA pass").
    assert "perform the SME Review & Sign-off pass yourself in THIS context" in instr
    assert "pass the review before presenting any output" in instr


def test_wr01_fallback_regex_captures_full_blockquote():
    """Unit-level: the fixed _FALLBACK_RE captures every `> ` continuation line."""
    block = (
        "> Single-threaded fallback: if your host has no subagent capability, perform\n"
        "> the SME Review & Sign-off pass yourself in THIS context — run the\n"
        "> de-identification scrub first, keep the scope discipline, and pass the review.\n"
        "Some later non-blockquote line that must NOT be captured."
    )
    m = build._FALLBACK_RE.search(block)
    assert m is not None
    captured = m.group(0)
    assert "SME Review & Sign-off pass" in captured
    assert "Some later non-blockquote line" not in captured


# --- WR-02 -----------------------------------------------------------------------


def test_wr02_hoc_discipline_inline_on_chatgpt_engine_path(board_safety_report_dir, tmp_path):
    """The ChatGPT engine path (_ENGINE_REPORT) now carries the HoC discipline INLINE,
    not only as a knowledge/ pointer."""
    _adapted, out = _emit(board_safety_report_dir, "chatgpt", tmp_path)
    instr = (out / "instructions.md").read_text(encoding="utf-8")
    assert "hierarchy of controls" in instr.lower()
    assert "no PPE-only" in instr


def test_wr02_validator_rejects_hoc_pointer_without_discipline(board_safety_report_dir, tmp_path):
    """The validator HoC check requires the discipline phrase — a bundle whose only HoC
    trace is a topic word / pointer (no discipline) FAILS check 3."""
    _adapted, out = _emit(board_safety_report_dir, "gemini", tmp_path)
    instr_path = out / "instructions.md"
    instr = instr_path.read_text(encoding="utf-8")
    instr = instr.replace("hierarchy of controls", "X").replace("no PPE-only", "no X-only")
    instr_path.write_text(instr, encoding="utf-8")
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, board_safety_report_dir, "gemini", platforms)
    assert any("hierarchy-of-controls DISCIPLINE" in e for e in rep.errors), rep.errors


# --- WR-03 -----------------------------------------------------------------------


def test_wr03_knowledge_basename_collision_fails_loud(risk_assessment_dir, tmp_path):
    """Two distinct sources with the same basename must raise, not silently overwrite."""
    adapted = build.load_skill(risk_assessment_dir)
    # Forge a collision: two different real files that share a basename.
    a = tmp_path / "dir_a" / "iso-45001.md"
    b = tmp_path / "dir_b" / "iso-45001.md"
    a.parent.mkdir(parents=True)
    b.parent.mkdir(parents=True)
    a.write_text("A", encoding="utf-8")
    b.write_text("B", encoding="utf-8")
    adapted.knowledge_files = [a, b]
    with pytest.raises(ValueError, match="basename collision"):
        build._write_knowledge(adapted, tmp_path / "out")
