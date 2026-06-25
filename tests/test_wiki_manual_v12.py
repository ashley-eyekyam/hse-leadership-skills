"""v1.2 GitHub Wiki manual contract.

These tests lock the public repo's docs/wiki mirror to the v1.2 manual shape:
the 19-page wiki source set, router-first navigation, full card fields for
owning pages, shared-skill stubs for secondary pages, current catalog counts,
and publish dry-run coverage.

Run:
    python -m pytest tests/test_wiki_manual_v12.py -q
"""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WIKI = REPO / "docs" / "wiki"

EXPECTED_WIKI_PAGES = {
    "Home.md",
    "_Sidebar.md",
    "Start-Here-Guided-Mode.md",
    "Core.md",
    "Operations.md",
    "Leadership.md",
    "Process-Safety.md",
    "Chemicals.md",
    "India-Compliance.md",
    "Aviation.md",
    "Mining.md",
    "Construction.md",
    "Manufacturing.md",
    "Utilities-Power.md",
    "Healthcare.md",
    "Logistics-Transport.md",
    "Marine-Offshore.md",
    "Rail.md",
    "Renewables.md",
}

REQUIRED_FULL_CARD_FIELDS = (
    "- **Produces:**",
    "- **For:**",
    "**Grounded in:**",
    "**Packs:**",
    "- **Use when:**",
    "- **Don't use for:**",
    "- **Have ready:**",
    "- **Trigger:**",
    "- **You get:**",
    "- **Pairs well with:**",
)

FULL_CARD_PAGE = {
    "arc-flash-assessment": "Utilities-Power.md",
    "bocw-compliance": "India-Compliance.md",
    "bowtie-builder": "Process-Safety.md",
    "chemical-exposure-register": "Chemicals.md",
    "chemical-transport-safety": "Chemicals.md",
    "construction-phase-plan": "Construction.md",
    "emergency-response-plan": "Operations.md",
    "hazid-facilitator": "Process-Safety.md",
    "hazop-facilitator": "Process-Safety.md",
    "health-risk-assessment": "Operations.md",
    "live-working-risk-assessment": "Utilities-Power.md",
    "lopa-worksheet": "Process-Safety.md",
    "management-of-change": "Process-Safety.md",
    "permit-to-work": "Process-Safety.md",
    "psychosocial-risk-assessment": "Operations.md",
    "risk-assessment": "Core.md",
    "toolbox-talk": "Core.md",
    "whatif-facilitator": "Process-Safety.md",
}

PRIMARY_PLUGIN_PAGE = {
    "hse-core": "Core.md",
    "hse-operations": "Operations.md",
    "hse-leadership": "Leadership.md",
    "hse-process": "Process-Safety.md",
    "hse-chemicals": "Chemicals.md",
    "hse-india": "India-Compliance.md",
    "hse-aviation": "Aviation.md",
    "hse-mining": "Mining.md",
    "hse-construction": "Construction.md",
    "hse-manufacturing": "Manufacturing.md",
    "hse-utilities-power": "Utilities-Power.md",
    "hse-healthcare": "Healthcare.md",
    "hse-logistics-transport": "Logistics-Transport.md",
    "hse-marine-offshore": "Marine-Offshore.md",
    "hse-rail": "Rail.md",
    "hse-renewables": "Renewables.md",
}

PACK_PAGE_BY_PLUGIN = PRIMARY_PLUGIN_PAGE


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path.relative_to(REPO)}"
    return path.read_text(encoding="utf-8")


def _load_extractor():
    script = REPO / "scripts" / "extract_skill_cards.py"
    spec = importlib.util.spec_from_file_location("extract_skill_cards", script)
    assert spec and spec.loader, "cannot load extract_skill_cards.py"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _records():
    return _load_extractor().collect(REPO)


def _card_block(page_text: str, skill: str) -> str:
    marker = f"### {skill}"
    start = page_text.find(marker)
    assert start != -1, f"missing card heading {marker!r}"
    next_start = page_text.find("\n### ", start + len(marker))
    return page_text[start:] if next_start == -1 else page_text[start:next_start]


def test_wiki_source_page_set_is_v12_complete():
    pages = {p.name for p in WIKI.glob("*.md")}
    assert pages == EXPECTED_WIKI_PAGES


def test_publish_wiki_dry_run_lists_every_v12_page():
    result = subprocess.run(
        ["python3", "scripts/publish_wiki.py", "--dry-run"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    output = result.stdout
    assert "[dry-run] pages (19):" in output
    for page in EXPECTED_WIKI_PAGES:
        assert f"- {page}" in output


def test_extractor_count_policy_is_current():
    records = _records()
    folders = {r["folder"] for r in records}
    assert len(records) == 93
    assert "using-hse-skills" in folders
    assert "hse-skill-forge" not in folders


def test_no_stale_count_language_in_wiki_or_tool_docs():
    forbidden = (
        "48 consultant skills",
        "grep -c '^### ' == 48",
        "8 source-of-truth pages",
        "6 pack pages",
        "old 48-skill",
    )
    checked = [
        REPO / "scripts" / "publish_wiki.py",
        REPO / "scripts" / "extract_skill_cards.py",
        *WIKI.glob("*.md"),
    ]
    for path in checked:
        text = _read(path)
        hits = [phrase for phrase in forbidden if phrase in text]
        assert not hits, f"{path.relative_to(REPO)} contains stale language: {hits}"


def test_router_is_visible_from_all_required_surfaces():
    home = _read(WIKI / "Home.md")
    sidebar = _read(WIKI / "_Sidebar.md")
    core = _read(WIKI / "Core.md")
    router = _read(WIKI / "Start-Here-Guided-Mode.md")

    assert "/using-hse-skills" in home
    assert "[Start Here" in home and "(Start-Here-Guided-Mode)" in home
    assert "| I am not sure which skill I need | [`using-hse-skills`](Start-Here-Guided-Mode) |" in home
    assert "hands over" in home or "hand over" in home

    assert "[Start Here" in sidebar and "(Start-Here-Guided-Mode)" in sidebar

    first_core_heading = next(line for line in core.splitlines() if line.startswith("### "))
    assert first_core_heading == "### using-hse-skills"
    assert "[Start Here" in _card_block(core, "using-hse-skills")

    required_router_sections = (
        "## What to run first",
        "## What it is",
        "## What it is not",
        "## Typical use patterns",
        "## When to skip it",
        "## How routing works",
        "## Examples",
        "## Links",
    )
    for section in required_router_sections:
        assert section in router
    assert "/using-hse-skills" in router
    assert "`hse-core`" in router and "`hse-all`" in router


def test_home_links_every_pack_page_and_readme_targets():
    home = _read(WIKI / "Home.md")
    for page in sorted(EXPECTED_WIKI_PAGES - {"Home.md", "_Sidebar.md", "Start-Here-Guided-Mode.md"}):
        target = page.removesuffix(".md")
        assert f"({target})" in home, f"Home.md must link {target}"
    assert "../README.md#install-in-30-seconds" in home
    assert "../docs/USER_MANUAL.md" in home
    assert "../docs/USER_JOURNEYS.md" in home
    assert "../CONTRIBUTING.md" in home


def test_no_compact_summary_cards_remain():
    for page in WIKI.glob("*.md"):
        text = _read(page)
        assert "- **Summary:**" not in text, f"{page.name} still has compact Summary cards"


def test_full_cards_have_all_required_fields_or_are_declared_stubs():
    for page in WIKI.glob("*.md"):
        text = _read(page)
        for line in text.splitlines():
            if not line.startswith("### "):
                continue
            skill = line.removeprefix("### ").split(" -> ", 1)[0].strip()
            if page.name in {"_Sidebar.md"}:
                continue
            block = _card_block(text, skill)
            if " -> see [" in line:
                assert "Full card on the" in block
                continue
            missing = [field for field in REQUIRED_FULL_CARD_FIELDS if field not in block]
            assert not missing, f"{page.name} {skill} missing fields: {missing}"


def test_every_non_forge_record_has_primary_full_card():
    by_folder = {r["folder"]: r for r in _records()}
    for folder, rec in sorted(by_folder.items()):
        primary_page = FULL_CARD_PAGE.get(folder) or PRIMARY_PLUGIN_PAGE[rec["plugin"]]
        block = _card_block(_read(WIKI / primary_page), folder)
        missing = [field for field in REQUIRED_FULL_CARD_FIELDS if field not in block]
        assert not missing, f"{primary_page} {folder} missing fields: {missing}"


def test_shared_skills_use_full_primary_and_stubs_elsewhere():
    records = {r["folder"]: r for r in _records()}
    for folder, primary_page in FULL_CARD_PAGE.items():
        rec = records[folder]
        primary_text = _read(WIKI / primary_page)
        primary_block = _card_block(primary_text, folder)
        assert " -> see [" not in primary_block.splitlines()[0]
        for pack in rec["packs"]:
            page = PACK_PAGE_BY_PLUGIN[pack]
            if page == primary_page:
                continue
            text = _read(WIKI / page)
            block = _card_block(text, folder)
            first_line = block.splitlines()[0]
            assert " -> see [" in first_line, f"{page} {folder} should be a cross-reference stub"
            assert "Full card on the" in block


def test_readme_reaches_wiki_and_guided_router():
    readme = _read(REPO / "README.md")
    assert "../../wiki" in readme
    assert "/using-hse-skills" in readme
    assert "skills/using-hse-skills/" in readme
