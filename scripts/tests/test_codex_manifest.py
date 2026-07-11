"""test_codex_manifest.py — native Codex plugin manifest invariants.

Locks `.codex-plugin/plugin.json` to the rules enforced by the official Codex
plugin validator (plugin-creator's validate_plugin.py, read against
codex-cli 0.142.5) plus this repo's own release policy:

  * only validator-accepted top-level / interface keys (`hooks` etc. rejected);
  * strict semver with NO local cachebuster suffix (a committed
    `1.3.0+codex.local-...` dev version must fail CI);
  * `skills` stays `./skills/` — the canonical catalog, never a copy;
  * the exposed skill set matches gen_marketplace's canonical iteration
    (single source of truth, no hard-coded skill count);
  * the decision-support / competent-person review boundary stays in the
    long description;
  * no `[TODO: ...]` placeholders, HTTPS-only URLs, <=3 default prompts each
    under 128 chars;
  * `mcpServers` / `apps` stay absent unless their manifest files ship too.

Pure deterministic Python against the committed repo tree: no network, no
model, no key.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

# scripts/tests/<this> -> repo/scripts on sys.path for `gen_marketplace`.
SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import gen_marketplace  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
MANIFEST = REPO / ".codex-plugin" / "plugin.json"

# Mirrors validate_manifest_shape() in the official plugin-creator validator.
ALLOWED_TOP_LEVEL = {
    "id",
    "name",
    "version",
    "description",
    "skills",
    "apps",
    "mcpServers",
    "interface",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
}
ALLOWED_INTERFACE = {
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
    "capabilities",
    "websiteURL",
    "privacyPolicyURL",
    "termsOfServiceURL",
    "brandColor",
    "composerIcon",
    "logo",
    "logoDark",
    "screenshots",
    "defaultPrompt",
    "default_prompt",
}
REQUIRED_INTERFACE_STRINGS = (
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
)

# Strict release semver: MAJOR.MINOR.PATCH only — pre-release/build suffixes
# (incl. the dev cachebuster `+codex.local-...`) must never be committed.
RELEASE_SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


@pytest.fixture(scope="module")
def manifest() -> dict:
    assert MANIFEST.is_file(), "missing .codex-plugin/plugin.json"
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def test_only_validator_accepted_top_level_keys(manifest):
    unknown = set(manifest) - ALLOWED_TOP_LEVEL
    assert not unknown, f"keys rejected by the Codex validator: {sorted(unknown)}"


def test_name_is_kebab_and_stable(manifest):
    assert manifest["name"] == "hse-leadership-skills"
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", manifest["name"])


def test_version_is_clean_release_semver(manifest):
    assert RELEASE_SEMVER_RE.fullmatch(manifest["version"]), (
        f"version {manifest['version']!r} must be plain MAJOR.MINOR.PATCH — a"
        " committed dev cachebuster suffix (+codex.local-...) is a release defect"
    )


def test_skills_points_at_canonical_catalog(manifest):
    assert manifest["skills"] == "./skills/"


def test_every_skill_dir_has_skill_md():
    skills_root = REPO / "skills"
    missing = [
        d.name
        for d in sorted(skills_root.iterdir())
        if d.is_dir() and not d.name.startswith(".") and not (d / "SKILL.md").is_file()
    ]
    assert not missing, f"skill dirs without SKILL.md: {missing}"


def test_exposed_skills_match_canonical_catalog():
    """The dirs Codex will load == gen_marketplace's canonical skill iteration.

    Uses the same single source of truth that generates the Claude marketplace
    and the router index — deliberately no hard-coded count.
    """
    exposed = {
        d.name
        for d in (REPO / "skills").iterdir()
        if d.is_dir() and not d.name.startswith(".") and (d / "SKILL.md").is_file()
    }
    canonical = {p.name for p in gen_marketplace._iter_skills(REPO)}
    assert exposed == canonical


def test_author_and_urls(manifest):
    author = manifest["author"]
    assert set(author) <= {"name", "email", "url"}
    assert author["name"].strip()
    for url in (
        author.get("url"),
        manifest.get("homepage"),
        manifest.get("repository"),
        manifest["interface"].get("websiteURL"),
    ):
        if url is not None:
            assert url.startswith("https://"), f"non-HTTPS URL: {url}"


def test_interface_shape(manifest):
    interface = manifest["interface"]
    unknown = set(interface) - ALLOWED_INTERFACE
    assert not unknown, f"interface keys rejected by the Codex validator: {sorted(unknown)}"
    for field in REQUIRED_INTERFACE_STRINGS:
        assert isinstance(interface.get(field), str) and interface[field].strip()
    capabilities = interface["capabilities"]
    assert isinstance(capabilities, list) and capabilities
    assert all(isinstance(c, str) and c.strip() for c in capabilities)
    assert re.fullmatch(r"#[0-9A-Fa-f]{6}", interface["brandColor"])


def test_default_prompts_within_limits(manifest):
    prompts = manifest["interface"]["defaultPrompt"]
    assert isinstance(prompts, list) and 1 <= len(prompts) <= 3
    for prompt in prompts:
        assert isinstance(prompt, str) and prompt.strip()
        assert len(prompt) < 128, f"default prompt too long: {prompt!r}"


def test_competent_person_boundary_preserved(manifest):
    text = manifest["interface"]["longDescription"].lower()
    assert "competent-person review" in text or "competent person" in text, (
        "the decision-support / competent-person review boundary must stay in"
        " the long description"
    )


def test_no_todo_placeholders():
    assert "[TODO:" not in MANIFEST.read_text(encoding="utf-8")


def test_optional_subsystems_absent_without_their_manifests(manifest):
    if "mcpServers" in manifest:
        assert (REPO / ".mcp.json").is_file(), "mcpServers set but .mcp.json missing"
    if "apps" in manifest:
        assert (REPO / ".app.json").is_file(), "apps set but .app.json missing"
    # First release ships neither (brief non-goals).
    assert "mcpServers" not in manifest
    assert "apps" not in manifest


def test_no_visual_asset_fields_without_files(manifest):
    interface = manifest["interface"]
    for field in ("composerIcon", "logo", "logoDark"):
        if field in interface:
            rel = interface[field]
            assert (REPO / rel).is_file(), f"{field} points at missing {rel}"
    for rel in interface.get("screenshots", []):
        assert (REPO / rel).is_file(), f"screenshot missing: {rel}"
