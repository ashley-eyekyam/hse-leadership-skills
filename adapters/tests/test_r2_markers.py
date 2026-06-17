"""test_r2_markers.py — R2 closed + CI-verified (§3.2 / §3.8 check 4).

The instructions carry NO `<!-- hse:block` literal; the knowledge SKILL.md copy
DOES (preserved + re-ingestible); the block CONTENTS survive marker-free; AND the
`## Output format` heading survives the strip (the line-297 Pitfall-1 trap).
"""

import build
import validate_adapters as va


def _emit_validate(skill_dir, platform, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / platform / adapted.name
    build.emit(adapted, platform, out, platforms)
    rep = va.validate_bundle(out, skill_dir, platform, platforms)
    return out, rep


def test_no_marker_literal_in_chatgpt_instructions(risk_assessment_dir, tmp_path):
    out, rep = _emit_validate(risk_assessment_dir, "chatgpt", tmp_path)
    instr = (out / "instructions.md").read_text(encoding="utf-8")
    assert "<!-- hse:block" not in instr
    # The validator agrees: no R2 error for a clean bundle.
    assert not any("R2" in e or "hse:block" in e for e in rep.errors), rep.errors


def test_knowledge_skill_copy_preserves_markers(risk_assessment_dir, tmp_path):
    out, rep = _emit_validate(risk_assessment_dir, "chatgpt", tmp_path)
    skill_copy = (out / "knowledge" / "SKILL.md").read_text(encoding="utf-8")
    assert "<!-- hse:block" in skill_copy, "knowledge SKILL.md must keep its markers"


def test_output_format_heading_survives_strip(risk_assessment_dir, tmp_path):
    # Pitfall 1: the report-output marker shares its line with `## Output format`.
    out, rep = _emit_validate(risk_assessment_dir, "chatgpt", tmp_path)
    instr = (out / "instructions.md").read_text(encoding="utf-8")
    assert "## Output format" in instr
    assert not any("Output format" in e for e in rep.errors), rep.errors


def test_validator_catches_marker_leak_in_instructions(risk_assessment_dir, tmp_path):
    # NEGATIVE: a hand-tampered instructions field with a leaked marker FAILS check 4.
    out, _ = _emit_validate(risk_assessment_dir, "chatgpt", tmp_path)
    instr_path = out / "instructions.md"
    instr_path.write_text(
        instr_path.read_text(encoding="utf-8") + "\n<!-- hse:block:deid:start -->\n",
        encoding="utf-8",
    )
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, risk_assessment_dir, "chatgpt", platforms)
    assert not rep.ok
    assert any("hse:block" in e or "R2" in e for e in rep.errors), rep.errors


def test_validator_catches_missing_output_format(toolbox_talk_dir, tmp_path):
    out, _ = _emit_validate(toolbox_talk_dir, "chatgpt", tmp_path)
    instr_path = out / "instructions.md"
    text = instr_path.read_text(encoding="utf-8").replace("## Output format", "## Report")
    instr_path.write_text(text, encoding="utf-8")
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, toolbox_talk_dir, "chatgpt", platforms)
    assert any("Output format" in e for e in rep.errors), rep.errors
