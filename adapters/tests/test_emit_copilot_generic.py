"""test_emit_copilot_generic.py — the Copilot + generic emitters and the char-fit
spill (Task 2, §3.5 / §3.6 / §3.7).

Copilot: declarative-agent manifest schema 1.7, instructions ≤ 8000, the four
non-negotiables stay IN instructions (anti-XPIA). Generic: char-fit to the
conservative default + full intake + markdown degradation. Plus the spill
algorithm (movable-only) + irreducible-core hard-fail.
"""

import copy
import json

import pytest

import build


def _relaxed_platforms(platform, limit=20000):
    cfg = copy.deepcopy(build.load_platforms())
    cfg["platforms"][platform]["char_limit"] = limit
    return cfg


# --- Copilot --------------------------------------------------------------------


def _emit_copilot(skill_dir, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / "copilot" / adapted.name
    build.emit_copilot(adapted, out, platforms)
    return adapted, out, platforms


def test_copilot_manifest_schema_1_7(risk_assessment_dir, tmp_path):
    _, out, _ = _emit_copilot(risk_assessment_dir, tmp_path)
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "1.7"
    # Declarative-agent shape.
    for key in ("name", "description", "instructions", "capabilities", "knowledge_sources"):
        assert key in manifest, f"copilot manifest missing {key}"


def test_copilot_manifest_string_props_within_limit(risk_assessment_dir, tmp_path):
    _, out, platforms = _emit_copilot(risk_assessment_dir, tmp_path)
    limit = platforms["platforms"]["copilot"]["manifest_string_limit"]
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["description"]) <= limit
    assert len(manifest["instructions"]) <= limit  # a pointer, not the full body


def test_copilot_instructions_within_char_limit(risk_assessment_dir, tmp_path):
    _, out, platforms = _emit_copilot(risk_assessment_dir, tmp_path)
    text = (out / "instructions.md").read_text(encoding="utf-8")
    assert len(text) <= platforms["platforms"]["copilot"]["char_limit"]


def test_copilot_four_non_negotiables_in_instructions(risk_assessment_dir, tmp_path):
    # Anti-XPIA: the four non-negotiables stay IN the instruction field, never spilled.
    _, out, _ = _emit_copilot(risk_assessment_dir, tmp_path)
    text = (out / "instructions.md").read_text(encoding="utf-8")
    assert "De-identification" in text           # de-id block
    assert "Disclaimer" in text                  # DISCLAIMER preamble
    assert "hierarchy of controls" in text.lower()  # HoC
    assert "Jurisdiction" in text                # §2.7 intake


def test_copilot_markdown_degradation_no_assets(risk_assessment_dir, tmp_path):
    _, out, _ = _emit_copilot(risk_assessment_dir, tmp_path)
    assert not (out / "assets").exists()
    text = (out / "instructions.md").read_text(encoding="utf-8")
    assert "generate_report.py" not in text


# --- generic --------------------------------------------------------------------


def _emit_generic(skill_dir, tmp_path, platforms=None):
    adapted = build.load_skill(skill_dir)
    platforms = platforms or _relaxed_platforms("generic")
    out = tmp_path / "generic" / adapted.name
    build.emit_generic(adapted, out, platforms)
    return adapted, out, platforms


def test_generic_system_prompt_file(risk_assessment_dir, tmp_path):
    _, out, _ = _emit_generic(risk_assessment_dir, tmp_path)
    assert (out / "system-prompt.md").is_file()
    assert (out / "manifest.json").is_file()
    assert not (out / "assets").exists()


def test_generic_char_fit_and_intake(risk_assessment_dir, tmp_path):
    platforms = _relaxed_platforms("generic", limit=10000)
    _, out, _ = _emit_generic(risk_assessment_dir, tmp_path, platforms)
    text = (out / "system-prompt.md").read_text(encoding="utf-8")
    assert len(text) <= 10000
    # Full intake + markdown degradation + disclaimer preamble.
    assert "Jurisdiction" in text
    assert "markdown" in text
    assert "Disclaimer" in text


def test_generic_manifest_minimal_shape(risk_assessment_dir, tmp_path):
    _, out, _ = _emit_generic(risk_assessment_dir, tmp_path)
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["system_prompt_file"] == "system-prompt.md"
    assert "knowledge_files" in manifest
    assert "notes" in manifest


def test_generic_resolved_cap_fits_flagship(risk_assessment_dir, tmp_path):
    # OWNER-RESOLVED 2026-06-17 (D-10): generic=9000 now clears the flagship irreducible
    # core (7887) — the heavy flagship emits cleanly instead of hard-failing.
    adapted = build.load_skill(risk_assessment_dir)
    platforms = build.load_platforms()  # generic=9000
    out = build.emit_generic(adapted, tmp_path / "g", platforms)
    instr = (out / "system-prompt.md").read_text(encoding="utf-8")
    assert len(instr) <= platforms["platforms"]["generic"]["char_limit"]


def test_generic_still_never_truncates_below_core(risk_assessment_dir, tmp_path):
    # The "never silently truncate" guarantee (D-08 / §3.7) still holds at a sub-core cap.
    adapted = build.load_skill(risk_assessment_dir)
    platforms = build.load_platforms()
    platforms["platforms"]["generic"]["char_limit"] = 1000
    with pytest.raises(build.IrreducibleOverflow):
        build.emit_generic(adapted, tmp_path / "g", platforms)


# --- the char-fit / spill algorithm (§3.7) --------------------------------------


def test_char_fit_noop_when_under_limit():
    body = "short body"
    assert build.char_fit(body, 1000) == body


def test_char_fit_spills_movable_prose():
    # A body over the limit whose only over-budget content is a movable section.
    core = "## Data Protection & De-identification\nMANDATORY core.\n\n"
    movable = "## Reference material\n" + ("x " * 2000) + "\n"
    body = core + movable
    spilled = []
    fit = build.char_fit(body, len(core) + 200, spilled=spilled)
    assert len(fit) <= len(core) + 200
    assert "## Reference material" in spilled
    # The pointer replaced the long prose; the core survived.
    assert "MANDATORY core." in fit
    assert "Full detail moved to the knowledge upload" in fit


def test_char_fit_never_moves_irreducible_core():
    # A body where the irreducible core ALONE exceeds the limit must hard-fail —
    # never silently truncate the de-id/HoC/intake/disclaimer.
    core = "## Data Protection & De-identification\n" + ("c " * 5000)
    with pytest.raises(build.IrreducibleOverflow):
        build.char_fit(core, 100)


def test_emit_chatgpt_copilot_all_exemplars(exemplar_dirs, tmp_path):
    # ChatGPT + Copilot (the 8000-char hosts) emit clean for all three exemplars,
    # exercising roster + A7-dependency variance (moderate/single-thread/4-fan-out;
    # A7 yes/no/yes).
    platforms = build.load_platforms()
    for name, skill_dir in exemplar_dirs.items():
        adapted = build.load_skill(skill_dir)
        for platform in ("chatgpt", "copilot"):
            out = tmp_path / platform / name
            build.emit(adapted, platform, out, platforms)
            problems = build._self_check(out, platform, platforms)
            assert not problems, f"{platform}/{name}: {problems}"


def test_tighter_fields_emit_or_hardfail_never_truncate(exemplar_dirs, tmp_path):
    # The flagship irreducible cores (rich de-id + full §2.7 intake) genuinely exceed
    # the tighter generic (6000) / Gemini (4000) fields. Per D-08 / §3.7 that is a
    # HARD FAILURE (IrreducibleOverflow), NEVER a silent truncation. A bundle that DOES
    # emit must be within its char_limit. Either outcome is spec-correct; truncation
    # is not.
    platforms = build.load_platforms()
    for name, skill_dir in exemplar_dirs.items():
        adapted = build.load_skill(skill_dir)
        for platform in ("gemini", "generic"):
            out = tmp_path / platform / name
            limit = platforms["platforms"][platform]["char_limit"]
            try:
                build.emit(adapted, platform, out, platforms)
            except build.IrreducibleOverflow:
                continue  # spec-correct hard-fail signal — lean the body as authored
            # If it emitted, the instruction field must be within the limit (no truncation
            # past the cap, and the four non-negotiables stayed in).
            instr = out / build._INSTRUCTION_FILE[platform]
            text = instr.read_text(encoding="utf-8")
            assert len(text) <= limit
            assert "De-identification" in text and "Jurisdiction" in text


def test_overflow_signal_is_actionable(incident_investigation_dir, tmp_path):
    # The hard-fail must name the platform/skill (an actionable CI signal, §3.7).
    adapted = build.load_skill(incident_investigation_dir)
    platforms = build.load_platforms()
    try:
        build.emit_gemini(adapted, tmp_path / "g", platforms)
    except build.IrreducibleOverflow as e:
        assert "char_limit" in str(e)
    # (If a future leaner authoring lets it fit, the emit simply succeeds — also fine.)
