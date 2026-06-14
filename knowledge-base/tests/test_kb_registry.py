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

from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
KB = REPO / "knowledge-base"

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
