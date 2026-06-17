"""test_build_all.py — the §5 acceptance #8 integration test (Task 2).

`build.py --all --check` emits + self-validates all 49 skills × 4 platforms and
exits 0; the three exemplars (roster + A7-dependency variance) each produce a
passing bundle on all four platforms; and NO committed bundle directory carries a
heavy `assets/` payload (the D-09 share-don't-duplicate contract, tree-wide).
Deterministic — no network, no model.
"""

from pathlib import Path

import build
import validate_adapters as va

REPO = Path(__file__).resolve().parent.parent.parent
ADAPTERS = REPO / "adapters"


def test_build_all_check_exits_zero():
    # The G3 everything-at-once gate: all 49 × 4 emit + self-validate clean.
    assert build.main(["--all", "--check"]) == 0


def test_validate_all_committed_tree_green():
    # The committed tree passes every §3.8 check + bundle-diff + no-heavy-assets.
    assert va.main(["--all"]) == 0


def test_four_non_negotiables_job_green():
    # The dedicated four-non-negotiables CI job is green on the committed tree.
    assert va.main(["--all", "--non-negotiables"]) == 0


def test_committed_tree_has_all_49_on_4_platforms():
    skill_names = sorted(p.parent.name for p in (REPO / "skills").rglob("SKILL.md"))
    assert len(skill_names) == 49, f"expected 49 skills, found {len(skill_names)}"
    for platform in build.PLATFORMS:
        for skill in skill_names:
            bundle = ADAPTERS / platform / skill
            assert bundle.is_dir(), f"missing committed bundle {platform}/{skill}"
            instr = bundle / build._INSTRUCTION_FILE[platform]
            assert instr.is_file(), f"{platform}/{skill}: missing {instr.name}"
            assert (bundle / "manifest.json").is_file()
            assert (bundle / "INSTALL.md").is_file()
            assert (bundle / "knowledge").is_dir()


def test_no_committed_heavy_assets_tree_wide():
    # D-09: not a single committed bundle may carry a heavy assets/ payload.
    for platform in build.PLATFORMS:
        for bundle in (ADAPTERS / platform).iterdir():
            if not bundle.is_dir():
                continue
            assert not (bundle / "assets").exists(), (
                f"{platform}/{bundle.name}: committed assets/ payload — heavy assets "
                f"must be SHARED from the canonical copy, never duplicated (D-09)"
            )
            assert va.check_no_heavy_assets(bundle, platform) == []


def test_chatgpt_bundles_name_shared_assets():
    # Every ChatGPT INSTALL.md NAMES the canonical assets/report-engine/ to upload.
    for bundle in (ADAPTERS / "chatgpt").iterdir():
        if not bundle.is_dir():
            continue
        install = (bundle / "INSTALL.md").read_text(encoding="utf-8")
        assert "assets/report-engine/" in install, f"{bundle.name}: INSTALL omits shared assets"


def test_three_exemplars_validate_all_platforms(exemplar_dirs):
    platforms = build.load_platforms()
    for name, skill_dir in exemplar_dirs.items():
        for platform in build.PLATFORMS:
            bundle = ADAPTERS / platform / name
            rep = va.validate_bundle(bundle, skill_dir, platform, platforms)
            assert rep.ok, f"{platform}/{name}: {rep.errors}"


def test_a7_variance_in_committed_install():
    # risk-assessment + incident-investigation declare A7 → ChatGPT INSTALL names
    # hse_components; toolbox-talk does NOT.
    def install(name):
        return (ADAPTERS / "chatgpt" / name / "INSTALL.md").read_text(encoding="utf-8")

    assert "scripts/hse_components/" in install("risk-assessment")
    assert "scripts/hse_components/" in install("incident-investigation")
    assert "scripts/hse_components/" not in install("toolbox-talk")


def test_bundle_diff_clean_on_committed_tree():
    # A fresh rebuild byte-matches the committed tree (no drift / hand-edit).
    rep = va.bundle_diff(REPO)
    assert rep.ok, rep.errors
