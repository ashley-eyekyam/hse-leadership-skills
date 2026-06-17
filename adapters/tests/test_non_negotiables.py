"""test_non_negotiables.py — the four non-negotiables survive IN instructions (§3.8
check 3), with the A8 de-id fixture-PAIR philosophy: a bundle that SPILLED a
non-negotiable into knowledge/ instead of instructions FAILS.

The four: de-id block content · DISCLAIMER preamble (+ in knowledge/) · HoC
(KB-SNIP-HOC) · §2.7 intake heading + question set — all present IN the instruction
text specifically (not merely somewhere in knowledge/ — Pitfall 3, Copilot anti-XPIA).
"""

import build
import validate_adapters as va


def _emit(skill_dir, platform, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / platform / adapted.name
    build.emit(adapted, platform, out, platforms)
    return adapted, out


# --- POSITIVE: all four present in a clean bundle ⇒ no non-negotiable error -----


def test_all_four_present_chatgpt(risk_assessment_dir, tmp_path):
    adapted, out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, risk_assessment_dir, "chatgpt", platforms)
    nn = [e for e in rep.errors if "non-negotiable" in e or "hierarchy" in e or "intake" in e]
    assert not nn, nn
    instr = (out / "instructions.md").read_text(encoding="utf-8")
    assert "decision-support only" in instr.lower()
    assert "hierarchy-of-controls" in instr or "hierarchy of controls" in instr.lower()
    assert "intake" in instr.lower()


def test_all_four_present_copilot_anti_xpia(incident_investigation_dir, tmp_path):
    # Copilot keeps the four IN the 8000-char instruction field, never offloaded to
    # knowledge (Microsoft anti-XPIA guidance) — check 3 asserts presence-in-instructions.
    adapted, out = _emit(incident_investigation_dir, "copilot", tmp_path)
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, incident_investigation_dir, "copilot", platforms)
    nn = [e for e in rep.errors if "non-negotiable" in e or "hierarchy" in e or "intake" in e]
    assert not nn, nn


# --- NEGATIVE FIXTURE: a non-negotiable spilled to knowledge/ FAILS check 3 -----


def test_deid_spilled_to_knowledge_fails(risk_assessment_dir, tmp_path):
    """The de-id block is moved OUT of instructions (as if mis-spilled to knowledge/)
    — validate_bundle MUST error (mirrors A8's de-id fixture-pair hard-fail)."""
    adapted, out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    instr_path = out / "instructions.md"
    instr = instr_path.read_text(encoding="utf-8")
    # Strip the de-id block content out of the instruction surface entirely.
    deid_head = build.strip_markers(adapted.blocks["deid"]).strip().splitlines()[0]
    # Replace the whole de-id section heading + body with a knowledge pointer.
    leaned = instr.replace(
        "## Data Protection & De-identification (MANDATORY — apply before drafting)",
        "## Data Protection\n\n_Moved to knowledge/ (see deid-checklist.md)._",
    )
    # Also remove the distinctive de-id sentence so the content match fails.
    leaned = leaned.replace(deid_head, "")
    instr_path.write_text(leaned, encoding="utf-8")

    platforms = build.load_platforms()
    rep = va.validate_bundle(out, risk_assessment_dir, "chatgpt", platforms)
    assert not rep.ok
    assert any("de-id" in e.lower() and "non-negotiable" in e for e in rep.errors), rep.errors


def test_disclaimer_removed_from_instructions_fails(toolbox_talk_dir, tmp_path):
    adapted, out = _emit(toolbox_talk_dir, "chatgpt", tmp_path)
    instr_path = out / "instructions.md"
    instr = instr_path.read_text(encoding="utf-8")
    instr_path.write_text(instr.replace("decision-support only", "X"), encoding="utf-8")
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, toolbox_talk_dir, "chatgpt", platforms)
    assert any("DISCLAIMER" in e for e in rep.errors), rep.errors


def test_hoc_removed_from_instructions_fails(toolbox_talk_dir, tmp_path):
    adapted, out = _emit(toolbox_talk_dir, "gemini", tmp_path)
    instr_path = out / "instructions.md"
    instr = instr_path.read_text(encoding="utf-8")
    instr = instr.replace("hierarchy-of-controls", "X").replace("hierarchy of controls", "X")
    instr_path.write_text(instr, encoding="utf-8")
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, toolbox_talk_dir, "gemini", platforms)
    assert any("hierarchy" in e for e in rep.errors), rep.errors
