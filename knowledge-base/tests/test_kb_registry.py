"""A3 KB registry-schema contract (KB-01/04/05 — §3.2 / §3.3 / §3.9).

Durable on-disk contract handed to A8 (the Phase-3 linter implements the enforcing
version). Over every `knowledge-base/*/_registry.yaml` it asserts:

  - each entry validates the §3.2 field schema (required keys present, correct types);
  - every `file` referenced by an entry exists on disk in that folder;
  - every `id` is unique repo-wide and scheme-conformant (`KB-<FOLDER>-…`, §3.3);
  - every facets block carries jurisdiction / industry / topics / audience;
  - every figure-bearing fragment (the `data-points/` folder, §3.9) has a
    non-empty `source` + `year`.

Plain pytest, sandbox-offline, no framework config. Paths resolve from the repo
root so the suite runs from any working directory.
"""

import sys
from datetime import date, timedelta
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
KB = REPO / "knowledge-base"

# lint_skills lives in scripts/ — wire it onto sys.path for the rule-9 staleness test.
_SCRIPTS = REPO / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

# §3.2 required fields on every registry entry.
REQUIRED_FIELDS = [
    "id",
    "file",
    "title",
    "facets",
    "summary",
    "source",
    "year",
    "last_reviewed",
    "volatile",
    "supersedes",
]
REQUIRED_FACETS = ["jurisdiction", "industry", "topics", "audience"]

# §3.3 fragment-ID scheme: KB-<FOLDER-TOKEN>-... . The folder token is derived from
# the facet folder name; map the on-disk folder to its id prefix segment.
FOLDER_ID_PREFIX = {
    "regulatory": "REG",
    "standards": "STD",
    "prompt-snippets": "SNIP",
    "data-points": "DATA",
    "research": "RES",
    "hazard-library": "HAZ",
}


def _registries():
    return sorted(KB.glob("*/_registry.yaml"))


def _load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or []


def test_registries_exist():
    found = {p.parent.name for p in _registries()}
    # The facet folders that must carry a registry (assets/ is excluded — no entries).
    assert FOLDER_ID_PREFIX.keys() <= found, f"missing registries: {set(FOLDER_ID_PREFIX) - found}"


@pytest.mark.parametrize("reg", _registries(), ids=lambda p: p.parent.name)
def test_entry_schema_and_files_exist(reg: Path):
    folder = reg.parent
    entries = _load(reg)
    assert isinstance(entries, list) and entries, f"{reg} is empty or not a list"
    for e in entries:
        for field in REQUIRED_FIELDS:
            assert field in e, f"{reg}:{e.get('id','?')} missing field '{field}'"
        # facets sub-schema
        facets = e["facets"]
        assert isinstance(facets, dict), f"{e['id']} facets not a mapping"
        for f in REQUIRED_FACETS:
            assert f in facets and facets[f], f"{e['id']} facets missing/empty '{f}'"
        # types
        assert isinstance(e["year"], int), f"{e['id']} year must be int"
        assert isinstance(e["volatile"], bool), f"{e['id']} volatile must be bool"
        assert str(e["title"]).strip(), f"{e['id']} title empty"
        assert str(e["summary"]).strip(), f"{e['id']} summary empty"
        # the referenced file exists in this folder
        target = folder / e["file"]
        assert target.is_file(), f"{e['id']} file '{e['file']}' not found in {folder.name}/"


def test_ids_unique_and_scheme_conformant():
    seen = {}
    for reg in _registries():
        folder = reg.parent.name
        prefix = FOLDER_ID_PREFIX.get(folder)
        if prefix is None:
            continue
        for e in _load(reg):
            kid = e["id"]
            assert kid not in seen, f"duplicate id {kid} in {folder} and {seen.get(kid)}"
            seen[kid] = folder
            assert kid.startswith(f"KB-{prefix}-"), (
                f"{kid} in {folder}/ does not match scheme KB-{prefix}-…"
            )


def test_data_points_have_source_and_year():
    """§3.9 — figures are never bare: every data-points entry carries source+year."""
    reg = KB / "data-points" / "_registry.yaml"
    entries = _load(reg)
    assert entries, "data-points registry empty"
    for e in entries:
        assert str(e.get("source", "")).strip(), f"{e['id']} has empty source"
        assert e.get("year"), f"{e['id']} has empty year"


# --- Phase 13-01: the 11 NEW hse-leadership KB registry entries -------------------
#
# Named (not just folder-scanned) assertions so a future drop of any of the 11
# leadership fragment registry entries fails loudly. Each is registered in its folder,
# scheme-conformant (KB-<PREFIX>-…), and carries a NON-EMPTY source + year (the
# refuse-on-vague gate depends on real citations).
LEADERSHIP_REGISTRY = {
    "prompt-snippets": [
        "KB-SNIP-LEADERSHIP-CLAUSE-MAP",
        "KB-SNIP-CULTURE-MODELS",
        "KB-SNIP-BBS-METHOD",
        "KB-SNIP-ESG-ASSURANCE",
        "KB-SNIP-POLICY-COMMITMENTS",
        "KB-SNIP-GEMBA-PROMPTS",
        "KB-SNIP-KPI-DESIGN",
    ],
    "data-points": [
        "KB-DATA-CULTURE-MATURITY",
        "KB-DATA-BBS-METRICS",
        "KB-DATA-LEADING-INDICATORS",
        "KB-DATA-ROAD-SAFETY-INDICATORS",
    ],
}


@pytest.mark.parametrize(
    "folder,kid",
    [(folder, kid) for folder, ids in LEADERSHIP_REGISTRY.items() for kid in ids],
)
def test_leadership_entry_registered_with_source_and_year(folder, kid):
    """Each of the 11 NEW leadership ids is registered, scheme-conformant, file-on-disk,
    and carries a non-empty source + year."""
    entries = _load(KB / folder / "_registry.yaml")
    entry = next((e for e in entries if e["id"] == kid), None)
    assert entry is not None, f"{kid} not registered in {folder}/_registry.yaml"
    prefix = FOLDER_ID_PREFIX[folder]
    assert kid.startswith(f"KB-{prefix}-"), f"{kid} not scheme-conformant for {folder}/"
    assert (KB / folder / entry["file"]).is_file(), f"{kid} file missing in {folder}/"
    assert str(entry.get("source", "")).strip(), f"{kid} has empty source"
    assert entry.get("year"), f"{kid} has empty year"


def test_leadership_esg_disclosures_not_minted():
    """D-02: KB-DP-ESG-DISCLOSURES is never minted; the GRI403 crosswalk is reused."""
    for reg in _registries():
        for e in _load(reg):
            assert e["id"] != "KB-DP-ESG-DISCLOSURES", (
                f"KB-DP-ESG-DISCLOSURES must NOT be minted (found in {reg.parent.name}/)"
            )


# --- D-05c per-fragment staleness_days override (Plan 06-01, Task 2) -------------

def _build_kb_with_entry(tmp_path: Path, entry: dict) -> tuple:
    """A minimal tmp repo: one regulatory registry entry + the file it points at, plus
    a skill body citing the entry's id. Returns (body, skill_dir, repo)."""
    repo = tmp_path
    reg_dir = repo / "knowledge-base" / "regulatory"
    reg_dir.mkdir(parents=True)
    (reg_dir / entry["file"]).write_text("# fragment\n", encoding="utf-8")
    (reg_dir / "_registry.yaml").write_text(yaml.safe_dump([entry]), encoding="utf-8")
    skill_dir = repo / "skills" / "demo"
    skill_dir.mkdir(parents=True)
    body = f"This skill cites {entry['id']} for the rule.\n"
    return body, skill_dir, repo


def _entry(days_old: int, staleness_days=None) -> dict:
    lr = date.today() - timedelta(days=days_old)
    e = {
        "id": "KB-REG-IN-OSH-CODE",
        "file": "in-osh-code.md",
        "title": "India OSH Code (volatile)",
        "summary": "test",
        "source": "test",
        "year": 2026,
        "last_reviewed": lr.strftime("%Y-%m-%d"),
        "volatile": True,
        "supersedes": None,
    }
    if staleness_days is not None:
        e["staleness_days"] = staleness_days
    return e


def _staleness_warns(tmp_path, days_old, staleness_days=None) -> bool:
    import lint_skills

    body, skill_dir, repo = _build_kb_with_entry(
        tmp_path, _entry(days_old, staleness_days)
    )
    report = lint_skills.Report(skill="demo")
    lint_skills._rule9_kb_resolution(report, body, skill_dir, repo)
    return any("predates" in w and "window" in w for w in report.warnings)


def test_staleness_override_90d_warns_a_100day_old_fragment(tmp_path):
    """A 100-day-old volatile fragment with staleness_days: 90 WARNs (it would NOT at
    the 180d global default) — D-05c per-fragment override is honoured."""
    # With the 90d override → 100d old > 90d window → WARN.
    assert _staleness_warns(tmp_path / "a", 100, staleness_days=90) is True
    # Same age, NO override → 100d < 180d default → no staleness WARN.
    assert _staleness_warns(tmp_path / "b", 100) is False


def test_global_180d_default_unchanged(tmp_path):
    """Without an override the 180d global default still governs: 200d old WARNs,
    100d old does not."""
    assert _staleness_warns(tmp_path / "c", 200) is True
    assert _staleness_warns(tmp_path / "d", 100) is False
