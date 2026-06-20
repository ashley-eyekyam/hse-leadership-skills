"""test_extract_strip.py — the parse layer (Task 1): extract_blocks, strip_markers,
has_a7, AdaptedSkill capture, platforms.yaml constants.

Runs against the real committed skills (read-only) — the three spec exemplars.
"""

import build


# --- extract_blocks: all five blocks, fail loud on a missing one ----------------


def test_extract_blocks_returns_all_five_nonempty(risk_assessment_dir):
    text = (risk_assessment_dir / "SKILL.md").read_text(encoding="utf-8")
    blocks = build.extract_blocks(text)
    assert set(blocks) == set(build.INLINE_BLOCKS)
    for name in build.INLINE_BLOCKS:
        assert blocks[name].strip(), f"block {name!r} extracted empty"


def test_extract_blocks_fails_loud_on_missing_block():
    # A body with only four of the five blocks must raise (A2 mitigation).
    partial = (
        "<!-- hse:block:deid:start -->X<!-- hse:block:deid:end -->\n"
        "<!-- hse:block:kb-selection:start -->Y<!-- hse:block:kb-selection:end -->\n"
        "<!-- hse:block:orchestration:start -->Z<!-- hse:block:orchestration:end -->\n"
        "<!-- hse:block:report-output:start -->W<!-- hse:block:report-output:end -->\n"
        # attribution block deliberately absent
    )
    try:
        build.extract_blocks(partial)
    except ValueError as e:
        assert "attribution" in str(e)
    else:
        raise AssertionError("extract_blocks did not fail loud on a missing block")


def test_extract_blocks_content_marker_free(risk_assessment_dir):
    text = (risk_assessment_dir / "SKILL.md").read_text(encoding="utf-8")
    blocks = build.extract_blocks(text)
    for name, content in blocks.items():
        assert "<!-- hse:block" not in content, f"{name} content still carries a marker"


# --- strip_markers: the Pitfall-1 shared-line trap ------------------------------


def test_strip_markers_keeps_heading_on_shared_line():
    line = "<!-- hse:block:report-output:start -->## Output format"
    stripped = build.strip_markers(line)
    assert "## Output format" in stripped, "the heading was dropped by the strip"
    assert "<!-- hse:block" not in stripped, "the marker token survived"


def test_strip_markers_removes_every_marker_in_body(risk_assessment_dir):
    text = (risk_assessment_dir / "SKILL.md").read_text(encoding="utf-8")
    _, body = build._split_frontmatter(text)
    stripped = build.strip_markers(body)
    assert "<!-- hse:block" not in stripped


def test_strip_markers_real_skill_preserves_output_format(risk_assessment_dir):
    # The risk-assessment line-297 trap, end-to-end on the real file.
    text = (risk_assessment_dir / "SKILL.md").read_text(encoding="utf-8")
    _, body = build._split_frontmatter(text)
    stripped = build.strip_markers(body)
    assert "## Output format" in stripped


# --- has_a7: detect, never assume -----------------------------------------------


def test_has_a7_true_for_risk_assessment(risk_assessment_dir):
    assert build.has_a7(risk_assessment_dir) is True


def test_has_a7_false_for_toolbox_talk(toolbox_talk_dir):
    assert build.has_a7(toolbox_talk_dir) is False


def test_has_a7_true_for_incident_investigation(incident_investigation_dir):
    assert build.has_a7(incident_investigation_dir) is True


# --- AdaptedSkill capture (roster / rows / intake verbatim) ----------------------


def test_adapted_skill_captures_core(risk_assessment_dir):
    adapted = build.load_skill(risk_assessment_dir)
    assert adapted.name == "risk-assessment"
    assert adapted.description, "description not captured from frontmatter"
    assert "<!-- hse:block" not in adapted.instructions_core
    assert "## Output format" in adapted.instructions_core
    assert set(adapted.blocks) == set(build.INLINE_BLOCKS)
    assert adapted.has_a7 is True


def test_adapted_skill_roster_and_rows_verbatim(risk_assessment_dir):
    adapted = build.load_skill(risk_assessment_dir)
    # Roster prose lives below orchestration:end — presence-only, unedited.
    assert "roster" in adapted.roster_prose.lower()
    assert "De-identifier" in adapted.roster_prose
    # Jurisdiction rows live below kb-selection:end — the markdown table.
    assert "|" in adapted.jurisdiction_rows
    assert "India" in adapted.jurisdiction_rows


def test_adapted_skill_intake_questions_captured(risk_assessment_dir):
    adapted = build.load_skill(risk_assessment_dir)
    assert adapted.intake_questions, "intake question set not captured"
    # Sourced from references/intake.md (Phase-9 INTK-01 home), Q-table region only.
    assert "Structured intake" in adapted.intake_questions
    # The §2.7 intake table carries the typed Q-rows (Q1 Jurisdiction MCQ).
    assert "Jurisdiction" in adapted.intake_questions
    # Q-table region ONLY — the prose echo-back / evidence sections are NOT embedded
    # (they push past the ChatGPT/Copilot char cap; they ship as knowledge/intake.md).
    assert "Echo-back" not in adapted.intake_questions


def test_adapted_skill_intake_for_all_exemplars(exemplar_dirs):
    for name, skill_dir in exemplar_dirs.items():
        adapted = build.load_skill(skill_dir)
        assert adapted.intake_questions.strip(), f"{name}: no intake captured"


def test_adapted_skill_toolbox_no_a7(toolbox_talk_dir):
    adapted = build.load_skill(toolbox_talk_dir)
    assert adapted.has_a7 is False


def test_knowledge_files_include_disclaimer_and_skill_copy(risk_assessment_dir):
    adapted = build.load_skill(risk_assessment_dir)
    names = [p.name for p in adapted.knowledge_files]
    assert "DISCLAIMER.md" in names
    assert "SKILL.md" in names
    # references/ pulled in.
    assert "METHODOLOGY.md" in names
    # A resolved KB fragment (named in _skill-kb.md) pulled in.
    assert any("iso-45001" in p.as_posix() for p in adapted.knowledge_files)


def test_knowledge_files_resolve_under_repo(risk_assessment_dir, repo):
    adapted = build.load_skill(risk_assessment_dir)
    for p in adapted.knowledge_files:
        assert p.is_file(), f"{p} does not resolve on disk"
        assert repo in p.parents or p == repo, f"{p} escapes the repo root"


# --- platforms.yaml constants ---------------------------------------------------


def test_platforms_yaml_loads_and_carries_constants():
    cfg = build.load_platforms()
    assert cfg["keep_markers"] is False
    platforms = cfg["platforms"]
    # REAL vendor-enforced hard limits stay 8000 (chatgpt/copilot).
    assert platforms["chatgpt"]["char_limit"] == 8000
    assert platforms["copilot"]["char_limit"] == 8000
    # OWNER-RESOLVED 2026-06-17 (D-10): no published vendor cap → raised to fit the
    # outputs fully (heaviest irreducible core 8516; 9000 gives headroom).
    assert platforms["generic"]["char_limit"] == 9000
    assert platforms["gemini"]["char_limit"] == 9000
    # ChatGPT is the only Code-Interpreter host.
    assert platforms["chatgpt"]["code_interpreter"] is True
    assert platforms["gemini"]["code_interpreter"] is False
    assert platforms["copilot"]["code_interpreter"] is False
    assert platforms["generic"]["code_interpreter"] is False


def test_platforms_yaml_gemini_owner_resolved_flagged():
    # D-10: the unpublished Gemini cap was OWNER-RESOLVED 2026-06-17 — the inline
    # comment records the resolution + date (replacing the prior OWNER-VERIFY flag).
    raw = build.PLATFORMS_FILE.read_text(encoding="utf-8")
    assert "OWNER-RESOLVED 2026-06-17" in raw
    assert "Gem instruction cap" in raw


def test_platforms_yaml_copilot_schema_and_string_limit():
    cfg = build.load_platforms()
    copilot = cfg["platforms"]["copilot"]
    assert copilot["manifest_schema"] == "1.7"
    assert copilot["manifest_string_limit"] == 4000
