"""test_emit_gemini.py — the Gemini Gem emitter (Task 2, §3.4).

Char-fit to the Gem limit; markdown-report degradation in house-section order;
code_interpreter false; NO committed assets/.

The flagship irreducible cores genuinely exceed the conservative 4000 Gemini default
(de-id block + full §2.7 intake ≈ 5600+ chars — an OWNER-VERIFY item, D-10). So the
emitter MECHANICS (degradation, manifest shape, no-assets) are exercised against a
relaxed-limit config; the real-cap overflow is asserted separately as the spec-correct
hard-fail (never a silent truncation).
"""

import copy
import json

import pytest

import build


def _relaxed_platforms(limit=20000):
    cfg = copy.deepcopy(build.load_platforms())
    cfg["platforms"]["gemini"]["char_limit"] = limit
    return cfg


def _emit(skill_dir, tmp_path, platforms=None):
    adapted = build.load_skill(skill_dir)
    platforms = platforms or _relaxed_platforms()
    out = tmp_path / "gemini" / adapted.name
    build.emit_gemini(adapted, out, platforms)
    return adapted, out, platforms


def test_gemini_writes_required_files(risk_assessment_dir, tmp_path):
    _, out, _ = _emit(risk_assessment_dir, tmp_path)
    assert (out / "instructions.md").is_file()
    assert (out / "manifest.json").is_file()
    assert (out / "INSTALL.md").is_file()
    assert (out / "knowledge").is_dir()


def test_gemini_no_assets(risk_assessment_dir, tmp_path):
    _, out, _ = _emit(risk_assessment_dir, tmp_path)
    assert not (out / "assets").exists(), "Gemini bundle must carry NO assets/"


def test_gemini_char_fit_within_limit(risk_assessment_dir, tmp_path):
    platforms = _relaxed_platforms(limit=10000)
    _, out, _ = _emit(risk_assessment_dir, tmp_path, platforms)
    text = (out / "instructions.md").read_text(encoding="utf-8")
    assert len(text) <= 10000


def test_gemini_markdown_degradation(risk_assessment_dir, tmp_path):
    _, out, _ = _emit(risk_assessment_dir, tmp_path)
    text = (out / "instructions.md").read_text(encoding="utf-8")
    # Degrades to a markdown report; no Code-Interpreter call.
    assert "structured" in text and "markdown" in text
    assert "generate_report.py" not in text
    # House section order present.
    assert "Hierarchy-of-controls table" in text
    assert "Executive summary" in text


def test_gemini_manifest_code_interpreter_false(risk_assessment_dir, tmp_path):
    _, out, _ = _emit(risk_assessment_dir, tmp_path)
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["code_interpreter"] is False
    assert manifest["name"] == "risk-assessment"


def test_gemini_non_negotiables_in_instructions(risk_assessment_dir, tmp_path):
    _, out, _ = _emit(risk_assessment_dir, tmp_path)
    text = (out / "instructions.md").read_text(encoding="utf-8")
    # de-id block content, HoC instruction, intake, disclaimer preamble — all present.
    assert "De-identification" in text
    assert "hierarchy of controls" in text.lower()
    assert "Disclaimer" in text
    assert "Jurisdiction" in text  # intake table


def test_gemini_manifest_byte_identical(risk_assessment_dir, tmp_path):
    adapted = build.load_skill(risk_assessment_dir)
    platforms = _relaxed_platforms()
    build.emit_gemini(adapted, tmp_path / "a", platforms)
    build.emit_gemini(adapted, tmp_path / "b", platforms)
    assert (tmp_path / "a" / "manifest.json").read_bytes() == (
        tmp_path / "b" / "manifest.json"
    ).read_bytes()


def test_gemini_real_cap_hardfails_heavy_flagship(risk_assessment_dir, tmp_path):
    # At the conservative 4000 default the flagship overflows → IrreducibleOverflow
    # (the spec-correct CI signal: lean the body as authored, D-08 / §3.7). NEVER a
    # silent truncation.
    adapted = build.load_skill(risk_assessment_dir)
    platforms = build.load_platforms()  # gemini=4000
    with pytest.raises(build.IrreducibleOverflow):
        build.emit_gemini(adapted, tmp_path / "g", platforms)
