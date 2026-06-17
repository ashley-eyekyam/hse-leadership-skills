"""test_char_limit.py — §3.8 check 2 + §3.7 spill discipline.

An over-limit instruction field is an error; the spill moves only MOVABLE prose;
an irreducible-core overflow hard-fails at build time (IrreducibleOverflow), never
a silent truncation.
"""

import pytest

import build
import validate_adapters as va


def _emit(skill_dir, platform, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / platform / adapted.name
    build.emit(adapted, platform, out, platforms)
    return out


def test_emitted_instruction_within_limit(risk_assessment_dir, tmp_path):
    out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    platforms = build.load_platforms()
    limit = platforms["platforms"]["chatgpt"]["char_limit"]
    instr = (out / "instructions.md").read_text(encoding="utf-8")
    assert len(instr) <= limit
    rep = va.validate_bundle(out, risk_assessment_dir, "chatgpt", platforms)
    assert not any("char_limit" in e for e in rep.errors), rep.errors


def test_validator_flags_over_limit_instruction(toolbox_talk_dir, tmp_path):
    out = _emit(toolbox_talk_dir, "chatgpt", tmp_path)
    instr_path = out / "instructions.md"
    # Pad the instruction field beyond the 8000 cap.
    instr_path.write_text(
        instr_path.read_text(encoding="utf-8") + "X" * 9000, encoding="utf-8"
    )
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, toolbox_talk_dir, "chatgpt", platforms)
    assert not rep.ok
    assert any("char_limit" in e for e in rep.errors), rep.errors


def test_irreducible_overflow_hard_fails_not_truncate():
    # A char_fit that cannot reach the cap by spilling movable prose raises
    # IrreducibleOverflow — never silently truncates (§3.7 step 4 / D-08).
    body = "## Core\n\n" + ("irreducible " * 2000)  # ~24k of non-movable core
    with pytest.raises(build.IrreducibleOverflow):
        build.char_fit(body, char_limit=1000)


def test_movable_prose_spills_before_core(risk_assessment_dir, tmp_path):
    # A tight (but core-clearing) cap spills movable headings to a knowledge pointer.
    adapted = build.load_skill(risk_assessment_dir)
    body = build._render_body(adapted, build._ENGINE_REPORT)
    spilled = []
    fitted = build.char_fit(body, char_limit=len(body) - 50, spilled=spilled)
    # The irreducible core sentence (de-id MANDATORY) is never spilled.
    assert "apply before drafting" in fitted.lower() or "MANDATORY" in fitted
