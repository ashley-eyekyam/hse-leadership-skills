"""test_build_all.py — the §5 acceptance #8 integration test (Task 2).

`build.py --all --check` emits + self-validates the full v1.2 catalog (94 skills ×
4 platforms, minus the documented per-(skill, platform) known-overflow exclusions)
and exits 0; the three exemplars (roster + A7-dependency variance) each produce a
passing bundle on all four platforms; and NO committed bundle directory carries a
heavy `assets/` payload (the D-09 share-don't-duplicate contract, tree-wide).
Deterministic — no network, no model.

P17 (17-07): the catalog expanded from 49 → 94 skills. Three skills carry an
irreducible four-non-negotiables core that genuinely exceeds the REAL 8,000-char
ChatGPT/Copilot vendor cap even after char_fit() spills every movable section;
D-07 forbids leaning the source body or truncating the core, so those specific
(skill, platform) bundles are emitted on gemini/generic (9,000) only and skipped
on the overflowing 8,000-cap host (build.KNOWN_OVERFLOW_SKIP — owner decision
2026-06-24). The expected per-platform bundle count is therefore 94 minus the
skips for that platform; the settled tree carries 92 chatgpt + 94 gemini + 91
copilot + 94 generic = 371 bundles.
"""

from pathlib import Path

import build
import validate_adapters as va

REPO = Path(__file__).resolve().parent.parent.parent
ADAPTERS = REPO / "adapters"


def test_build_all_check_exits_zero():
    # The G3 everything-at-once gate: the full 94-skill catalog (minus the documented
    # known-overflow skips) emits + self-validates clean and exits 0.
    assert build.main(["--all", "--check"]) == 0


def test_validate_all_committed_tree_green():
    # The committed tree passes every §3.8 check + bundle-diff + no-heavy-assets.
    assert va.main(["--all"]) == 0


def test_four_non_negotiables_job_green():
    # The dedicated four-non-negotiables CI job is green on the committed tree.
    assert va.main(["--all", "--non-negotiables"]) == 0


def test_committed_tree_has_full_catalog_on_4_platforms():
    # P17: the v1.2 catalog is 94 skills. Every skill ships an adapter on every
    # platform EXCEPT the documented per-(skill, platform) known-overflow skips
    # (build.KNOWN_OVERFLOW_SKIP — owner decision 2026-06-24, real 8000 vendor cap,
    # D-07 no-truncation): those bundles ship on gemini/generic only.
    skill_names = sorted(p.parent.name for p in (REPO / "skills").glob("*/SKILL.md"))
    assert len(skill_names) == 94, f"expected 94 skills, found {len(skill_names)}"
    for platform in build.PLATFORMS:
        for skill in skill_names:
            bundle = ADAPTERS / platform / skill
            if platform in build.KNOWN_OVERFLOW_SKIP.get(skill, ()):
                # Intentionally skipped on the overflowing 8000-cap host; assert it is
                # ABSENT (so a future accidental rebuild here is caught) but present on
                # the non-overflowing hosts.
                assert not bundle.exists(), (
                    f"{platform}/{skill}: bundle present but is in KNOWN_OVERFLOW_SKIP "
                    f"(should be emitted on gemini/generic only)"
                )
                continue
            assert bundle.is_dir(), f"missing committed bundle {platform}/{skill}"
            instr = bundle / build._INSTRUCTION_FILE[platform]
            assert instr.is_file(), f"{platform}/{skill}: missing {instr.name}"
            assert (bundle / "manifest.json").is_file()
            assert (bundle / "INSTALL.md").is_file()
            assert (bundle / "knowledge").is_dir()


def test_known_overflow_skips_present_iff_not_skipped():
    # Each known-overflow skill ships a complete adapter on EXACTLY the platforms NOT in
    # its skip list, and is ABSENT on the platforms IN its skip list. The exclusion drops
    # only the host(s) whose REAL vendor cap the irreducible core exceeds — never the
    # skill itself where it fits (D-07: source intact, core never truncated).
    #
    # Post-Phase-20 v1.3 HARD cutover the promoted single-thread fallback added a uniform
    # +138 chars (the omission re-bind), so the skip map grew from 3 to 9 pairs (D-06):
    #   - risk-assessment / lift-plan / lone-working-assessment spill on the 8000 hosts
    #     (chatgpt/copilot) but STILL ship on the 9000 hosts (gemini/generic);
    #   - wind-turbine-work-at-height-rescue now exceeds even the 9000 hosts and ships on
    #     NO adapter platform — still a native skill, just no Tier-B adapter.
    # This test therefore asserts the general present-iff-not-skipped invariant rather
    # than a blanket "ships on gemini/generic" (which wind-turbine no longer satisfies).
    for skill, skip_platforms in build.KNOWN_OVERFLOW_SKIP.items():
        for platform in build.PLATFORMS:
            bundle = ADAPTERS / platform / skill
            if platform in skip_platforms:
                assert not bundle.exists(), (
                    f"{platform}/{skill}: in KNOWN_OVERFLOW_SKIP but a bundle is present"
                )
            else:
                assert bundle.is_dir(), (
                    f"{platform}/{skill}: not skipped but its adapter bundle is missing"
                )
                assert (bundle / build._INSTRUCTION_FILE[platform]).is_file()


def test_known_overflow_set_is_genuinely_irreducible():
    # Guard against a stale skip map: each documented (skill, platform) skip must
    # STILL genuinely raise IrreducibleOverflow at its real cap (so the map is never
    # masking a skill that has since been leaned under the cap). Re-derive deterministically.
    platforms_cfg = build.load_platforms()
    for skill, skip_platforms in build.KNOWN_OVERFLOW_SKIP.items():
        skill_dir = REPO / "skills" / skill
        adapted = build.load_skill(skill_dir, REPO)
        for platform in skip_platforms:
            limit = platforms_cfg["platforms"][platform]["char_limit"]
            try:
                build.emit(adapted, platform, ADAPTERS / "_overflow_probe" / platform / skill, platforms_cfg)
            except build.IrreducibleOverflow:
                continue  # expected — genuinely over the cap
            else:
                raise AssertionError(
                    f"{platform}/{skill}: in KNOWN_OVERFLOW_SKIP but no longer overflows "
                    f"char_limit {limit} — remove it from the skip map (it now fits)"
                )
    # cleanup the throwaway probe tree
    import shutil
    shutil.rmtree(ADAPTERS / "_overflow_probe", ignore_errors=True)


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
            if platform in build.KNOWN_OVERFLOW_SKIP.get(name, ()):
                # D-06: this exemplar's irreducible core exceeds the platform's REAL cap
                # post-cutover; it ships only where it fits. Assert ABSENT here (never a
                # silently-truncated bundle) — the exemplar still validates on the hosts
                # where it does ship (e.g. risk-assessment on gemini/generic).
                assert not bundle.exists(), (
                    f"{platform}/{name}: in KNOWN_OVERFLOW_SKIP but a bundle is present"
                )
                continue
            rep = va.validate_bundle(bundle, skill_dir, platform, platforms)
            assert rep.ok, f"{platform}/{name}: {rep.errors}"


def test_a7_variance_in_committed_install():
    # job-safety-analysis + incident-investigation declare A7 → ChatGPT INSTALL names
    # hse_components; toolbox-talk does NOT. (risk-assessment also declares A7, but per
    # D-06 it overflows the 8000-char ChatGPT cap post-cutover and ships gemini/generic
    # only — and the A7 shared-asset naming lives specifically in the ChatGPT
    # Code-Interpreter INSTALL — so a chatgpt-shipping A7 flagship stands in for it here.)
    def install(name):
        return (ADAPTERS / "chatgpt" / name / "INSTALL.md").read_text(encoding="utf-8")

    assert "scripts/hse_components/" in install("job-safety-analysis")
    assert "scripts/hse_components/" in install("incident-investigation")
    assert "scripts/hse_components/" not in install("toolbox-talk")


def test_bundle_diff_clean_on_committed_tree():
    # A fresh rebuild byte-matches the committed tree (no drift / hand-edit).
    rep = va.bundle_diff(REPO)
    assert rep.ok, rep.errors
