"""test_codex_marketplace_catalog.py — repo-root Codex marketplace invariants.

Locks `.agents/plugins/marketplace.json`, the catalog Codex reads when this
repository (or a checkout) is added with `codex plugin marketplace add`.
Verified on codex-cli 0.142.5: when this native file exists it completely
shadows `.claude-plugin/marketplace.json`, and a self-referential
`source.path: "./"` resolves to the marketplace root.

Encodes the diagnosed install failure (docs/
CODEX_MARKETPLACE_NAME_MISMATCH_DIAGNOSIS.md in the private build repo):
Codex requires each `plugins[].name` to EQUAL the `.codex-plugin/plugin.json`
`name` at that entry's source. One directory carries one manifest, so this
catalog must expose exactly ONE entry, named after the manifest — never the
Claude bundle names (`hse-all`, `hse-core`, ...), which all point at the same
root and can never match.

Pure deterministic Python against the committed repo tree: no network, no
model, no key.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
CATALOG = REPO / ".agents" / "plugins" / "marketplace.json"
MANIFEST = REPO / ".codex-plugin" / "plugin.json"


@pytest.fixture(scope="module")
def catalog() -> dict:
    assert CATALOG.is_file(), "missing .agents/plugins/marketplace.json"
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


@pytest.fixture(scope="module")
def manifest_name() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["name"]


def test_marketplace_name(catalog):
    assert catalog["name"] == "hse-leadership-skills"
    assert catalog["interface"]["displayName"].strip()


def test_exactly_one_plugin_entry(catalog):
    """One root, one manifest, one entry. Bundle names cannot be listed here:
    each would need its own .codex-plugin/plugin.json with a matching name."""
    assert len(catalog["plugins"]) == 1


def test_entry_name_matches_codex_manifest(catalog, manifest_name):
    """THE diagnosed failure: `plugin.json name X does not match marketplace
    plugin name Y`. codex plugin add refuses any entry whose name differs from
    the manifest at its source path."""
    (entry,) = catalog["plugins"]
    assert entry["name"] == manifest_name


def test_entry_source_resolves_to_plugin_root(catalog):
    (entry,) = catalog["plugins"]
    source = entry["source"]
    assert source["source"] == "local"
    path = source["path"]
    assert path.startswith("./"), "source.path must be relative (absolute paths are ignored)"
    root = (CATALOG.parent.parent.parent / path).resolve()
    assert (root / ".codex-plugin" / "plugin.json").is_file()
    assert (root / "skills").is_dir()


def test_entry_policy_and_category(catalog):
    (entry,) = catalog["plugins"]
    assert entry["policy"] == {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }
    assert entry["category"] == "Productivity"


def test_no_claude_bundle_names_leak_in(catalog):
    """The Claude bundles stay in .claude-plugin/marketplace.json only."""
    claude = json.loads(
        (REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    bundle_names = {p["name"] for p in claude["plugins"]}
    codex_names = {p["name"] for p in catalog["plugins"]}
    assert not (codex_names & bundle_names), (
        "Claude bundle entries can never install via Codex from this root: "
        "their names cannot match the single .codex-plugin manifest name"
    )
