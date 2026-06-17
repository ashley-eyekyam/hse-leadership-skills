"""test_no_heavy_assets.py — the D-09 "share don't duplicate" contract (§3.8 + Open
Question 1 RESOLVED, option b).

A committed bundle carries ONLY instructions/system-prompt + knowledge/ + manifest +
INSTALL.md — NO heavy `assets/` payload. The ChatGPT INSTALL.md NAMES the canonical
shared assets (`assets/report-engine/` + iff has_a7 `scripts/hse_components/`). A
planted `assets/` dir FAILS (the de-id fixture-PAIR philosophy: positive + negative).
"""

import build
import validate_adapters as va


def _emit(skill_dir, platform, tmp_path):
    adapted = build.load_skill(skill_dir)
    platforms = build.load_platforms()
    out = tmp_path / platform / adapted.name
    build.emit(adapted, platform, out, platforms)
    return adapted, out


# --- POSITIVE: a clean ChatGPT bundle has no heavy assets/, names the shared ones --


def test_chatgpt_bundle_has_no_committed_assets(risk_assessment_dir, tmp_path):
    adapted, out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    assert not (out / "assets").exists(), "heavy assets/ must never be committed (D-09)"
    problems = va.check_no_heavy_assets(out, "chatgpt")
    assert problems == [], problems


def test_chatgpt_install_names_shared_assets(risk_assessment_dir, tmp_path):
    # has_a7 exemplar: INSTALL names both report-engine AND hse_components.
    adapted, out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    install = (out / "INSTALL.md").read_text(encoding="utf-8")
    assert "assets/report-engine/" in install
    assert "scripts/hse_components/" in install  # has_a7 True
    assert va.check_no_heavy_assets(out, "chatgpt") == []


def test_chatgpt_install_no_a7_for_toolbox(toolbox_talk_dir, tmp_path):
    adapted, out = _emit(toolbox_talk_dir, "chatgpt", tmp_path)
    install = (out / "INSTALL.md").read_text(encoding="utf-8")
    assert "assets/report-engine/" in install
    assert "scripts/hse_components/" not in install  # no A7
    assert va.check_no_heavy_assets(out, "chatgpt") == []


def test_all_platforms_no_heavy_assets(incident_investigation_dir, tmp_path):
    platforms = build.load_platforms()
    for platform in build.PLATFORMS:
        adapted, out = _emit(incident_investigation_dir, platform, tmp_path)
        rep = va.validate_bundle(out, incident_investigation_dir, platform, platforms)
        assert not any("assets" in e for e in rep.errors), (platform, rep.errors)


# --- NEGATIVE FIXTURE: a planted assets/ payload FAILS -------------------------


def test_planted_assets_dir_fails(risk_assessment_dir, tmp_path):
    adapted, out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    planted = out / "assets" / "report-engine"
    planted.mkdir(parents=True)
    (planted / "generate_report.py").write_text("# heavy duplicate\n", encoding="utf-8")
    problems = va.check_no_heavy_assets(out, "chatgpt")
    assert problems, "a planted assets/ payload must hard-fail (D-09)"
    platforms = build.load_platforms()
    rep = va.validate_bundle(out, risk_assessment_dir, "chatgpt", platforms)
    assert not rep.ok
    assert any("assets" in e for e in rep.errors), rep.errors


def test_chatgpt_install_missing_asset_name_fails(risk_assessment_dir, tmp_path):
    adapted, out = _emit(risk_assessment_dir, "chatgpt", tmp_path)
    install_path = out / "INSTALL.md"
    text = install_path.read_text(encoding="utf-8").replace("assets/report-engine/", "X")
    install_path.write_text(text, encoding="utf-8")
    problems = va.check_no_heavy_assets(out, "chatgpt")
    assert any("report-engine" in p for p in problems), problems
