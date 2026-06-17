"""test_emit_chatgpt.py — the ChatGPT Custom GPT emitter (Task 2, §3.3).

Real-engine report path; A7 asset reference iff has_a7; D-09 shared-asset INSTALL
naming (no committed heavy assets); byte-identical manifest across re-runs.
"""

import json

import build


def _emit(skill_dir, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / "chatgpt" / adapted.name
    build.emit_chatgpt(adapted, out, platforms)
    return adapted, out


def test_chatgpt_writes_required_files(risk_assessment_dir, tmp_path):
    _, out = _emit(risk_assessment_dir, tmp_path)
    assert (out / "instructions.md").is_file()
    assert (out / "manifest.json").is_file()
    assert (out / "INSTALL.md").is_file()
    assert (out / "knowledge").is_dir()


def test_chatgpt_instructions_marker_free_with_heading(risk_assessment_dir, tmp_path):
    _, out = _emit(risk_assessment_dir, tmp_path)
    text = (out / "instructions.md").read_text(encoding="utf-8")
    assert "<!-- hse:block" not in text
    assert "## Output format" in text
    # Code-Interpreter report path.
    assert "generate_report.py" in text
    assert "Code Interpreter" in text


def test_chatgpt_manifest_shape(risk_assessment_dir, tmp_path):
    adapted, out = _emit(risk_assessment_dir, tmp_path)
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["name"] == "risk-assessment"
    assert manifest["description"] == adapted.description
    assert manifest["instructions_file"] == "instructions.md"
    assert manifest["code_interpreter"] is True
    assert isinstance(manifest["knowledge_files"], list)
    assert manifest["knowledge_files"], "no knowledge files listed"
    assert isinstance(manifest["conversation_starters"], list)
    assert manifest["conversation_starters"], "no conversation starters lifted"


def test_chatgpt_a7_asset_reference_present_when_has_a7(risk_assessment_dir, tmp_path):
    _, out = _emit(risk_assessment_dir, tmp_path)
    install = (out / "INSTALL.md").read_text(encoding="utf-8")
    # D-09: INSTALL names the canonical shared assets to upload.
    assert "assets/report-engine/" in install
    assert "scripts/hse_components/" in install  # has_a7 True


def test_chatgpt_no_a7_reference_for_toolbox(toolbox_talk_dir, tmp_path):
    _, out = _emit(toolbox_talk_dir, tmp_path)
    install = (out / "INSTALL.md").read_text(encoding="utf-8")
    # toolbox-talk declared NO A7 — no hse_components reference.
    assert "scripts/hse_components/" not in install
    # Still references the report engine (every skill assembles a report.json).
    assert "assets/report-engine/" in install


def test_chatgpt_no_committed_heavy_assets(risk_assessment_dir, tmp_path):
    # D-09: the committed bundle carries instructions+knowledge+manifest only — the
    # heavy Code-Interpreter assets are NAMED in INSTALL, never physically duplicated.
    _, out = _emit(risk_assessment_dir, tmp_path)
    assert not (out / "assets").exists(), "heavy assets must not be duplicated into the bundle"


def test_chatgpt_knowledge_includes_disclaimer_and_skill_copy(risk_assessment_dir, tmp_path):
    _, out = _emit(risk_assessment_dir, tmp_path)
    names = {p.name for p in (out / "knowledge").iterdir()}
    assert "DISCLAIMER.md" in names
    assert "SKILL.md" in names
    # The knowledge SKILL.md copy PRESERVES the markers (re-ingestible, §3.2).
    skill_copy = (out / "knowledge" / "SKILL.md").read_text(encoding="utf-8")
    assert "<!-- hse:block" in skill_copy


def test_chatgpt_manifest_byte_identical_across_reruns(risk_assessment_dir, tmp_path):
    adapted = build.load_skill(risk_assessment_dir)
    platforms = build.load_platforms()
    out1 = tmp_path / "run1"
    out2 = tmp_path / "run2"
    build.emit_chatgpt(adapted, out1, platforms)
    build.emit_chatgpt(adapted, out2, platforms)
    m1 = (out1 / "manifest.json").read_bytes()
    m2 = (out2 / "manifest.json").read_bytes()
    assert m1 == m2, "manifest is not byte-identical across re-runs (Pitfall 5)"
    assert m1.endswith(b"\n")
