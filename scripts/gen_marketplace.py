#!/usr/bin/env python3
"""gen_marketplace.py — generate Claude + Cursor marketplace manifests (A8 §4.7).

The marketplace manifests are GENERATED from each skill's `metadata.plugin`
frontmatter — never hand-maintained (no duplication; a skill's bundle membership
lives in exactly one place, its own SKILL.md). Each distinct `metadata.plugin`
value becomes one plugin entry whose `skills` list is the folders that name it.

Emits:
  * `.claude-plugin/marketplace.json` — Claude Code marketplace
  * `.cursor-plugin/marketplace.json` — Cursor Team Marketplace (same membership)
  * `skills/using-hse-skills/references/skill-index.yaml` — router index

  --check   regenerate Claude + Cursor manifests and the router skill-index in
            memory and DIFF each against its on-disk artifact; exit nonzero if
            ANY drifts (the CI gate — research §4.7; QUAL-04 index drift;
            Cursor parity drift).
  --write   rewrite the on-disk Claude + Cursor manifests AND the router
            skill-index from the skills.

Stdlib + pyyaml only. Reuses the S2 main(argv)->int contract.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
MANIFEST = REPO / ".claude-plugin" / "marketplace.json"
CURSOR_MANIFEST = REPO / ".cursor-plugin" / "marketplace.json"

# Cursor Team Marketplace constants (docs: https://cursor.com/docs/reference/plugins).
# Version is read from `.codex-plugin/plugin.json` so Claude / Codex / Cursor stay
# aligned on the same release semver without a third hard-coded constant.
_REPO_URL = "https://github.com/ashley-eyekyam/hse-leadership-skills"
_CURSOR_AUTHOR = {
    "name": "Eyekyam Risk Resolutions Pvt. Ltd.",
    "email": "ashley@eyekyam.com",
}
_CURSOR_SOURCE = "."
_CURSOR_LOGO = "docs/assets/logo.svg"
_CURSOR_CATEGORY = "Productivity"

# The committed routable-skill index the `using-hse-skills` router reads at
# runtime (ROUTE-02 / D-01). Emitted from the SAME _iter_skills/_frontmatter pass
# as the manifest (below) so the catalog roster and the router's index can never
# drift. Fixed path under REPO — NO user input flows into it (no traversal
# surface, threat T-16.1-01).
SKILL_INDEX = REPO / "skills" / "using-hse-skills" / "references" / "skill-index.yaml"

# Bundles excluded from the synthesized `hse-all` meta-plugin (D-13): the
# build-time forge (hse-systems) stays contributor-only and must NOT ship in the
# one-line "install everything" consumer pack.
EXCLUDE_FROM_META = {"hse-systems"}

# Skills excluded from the ROUTABLE index (D-01): you do not route TO the router
# itself, nor to the contributor build tool `hse-skill-forge`. Mirrors
# EXCLUDE_FROM_META and the extract_skill_cards.py forge exclusion.
EXCLUDE_FROM_INDEX = {"using-hse-skills", "hse-skill-forge"}

# Skills kept OUT of the synthesized `hse-all` meta-plugin (owner override
# 2026-06-24, supersedes T-17-17). DELIBERATELY NOT EXCLUDE_FROM_INDEX: the catalog
# router `using-hse-skills` is now INCLUDED in hse-all — a user new to the plugin
# who installs the one-line "install everything" pack needs the catalog navigator
# that routes them to the right skill (precisely the router's job). Only the
# contributor forge `hse-skill-forge` stays out of hse-all; it is ALSO already
# excluded via its EXCLUDE_FROM_META bundle (hse-systems), so this set is
# belt-and-suspenders for any future bundle the forge might land in. Keeping this
# separate from EXCLUDE_FROM_INDEX lets the router ship in hse-all while still
# being absent from the ROUTABLE index (you do not route TO the navigator).
EXCLUDE_FROM_META_SKILLS = {"hse-skill-forge"}

# Every plugin entry shares one marketplace-root source (the whole repo is git-cloned
# when a user runs `/plugin marketplace add owner/repo`). `source` is a REQUIRED field
# in the Claude Code marketplace schema — omitting it makes Claude Code fail to classify
# the plugin and emit the misleading "this plugin uses a source type your Claude Code
# version does not support" error. With a marketplace-root source, several plugin entries
# share the one top-level `skills/` folder; each entry's `skills` list (the curated
# `./skills/<name>` subdirectory paths emitted below) then becomes the COMPLETE set of
# skills for that bundle.
#   docs: https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources
_PLUGIN_SOURCE = "./"

# strict:false — these bundles have NO per-plugin plugin.json; the marketplace entry IS
# the entire component definition. This is also what makes the component summary
# resolvable from marketplace.json alone (no clone needed to count skills).
_PLUGIN_STRICT = False

# Human-facing bundle descriptions (shown in `/plugin` discovery and on install). Keyed
# by bundle name; a bundle missing here falls back to the generic line so the generator
# never crashes when a future bundle is registered in metadata-vocab.yaml.
_DESCRIPTIONS = {
    "hse-all": "Install everything — the full HSE Leadership Skills toolbox (all consultant skills across hse-core plus the five sector packs).",
    "hse-core": "Core HSE skills — risk assessments, JSAs, toolbox talks, incident investigations, safety audits, CAPAs, SOPs, RAMS, board reports, and incident-rate calculators.",
    "hse-process": "Process-safety pack — HAZOP, HAZID, What-If, LOPA, bow-tie, permit-to-work, management-of-change, mechanical integrity, PSM program, PESO licensing, and process-safety KPIs.",
    "hse-chemicals": "Chemicals & major-accident-hazard pack — GHS/SDS authoring, chemical exposure & transport, dust-explosion and toxic-release assessment, tank-farm bunding, India MSIHC/MAH, plus shared PHA tools.",
    "hse-india": "India compliance pack — state accident notices, Factories Act returns, BOCW, OSH Code, and the legacy-first state-form finder (mandatory state detection).",
    "hse-aviation": "Aviation SMS pack — SMS builder, hazard register, SPI/SPT framework, FDM/FOQA analysis, just-culture policy, confidential reporting, change safety assessment, and SRB minutes.",
    "hse-mining": "Mining pack — DGMS statutory pack, ICMM critical-control management, principal-hazard management plans, mine incident investigation, mine rescue ERP, and ventilation/strata/blasting plans.",
    "hse-systems": "Build-time tooling — hse-skill-forge, the scaffolder that authors born-conformant HSE skills (for contributors, not a consultant artifact bundle).",
}


def _describe(bundle: str) -> str:
    return _DESCRIPTIONS.get(
        bundle, f"HSE Leadership Skills bundle: {bundle}."
    )

# The stable manifest header (everything except the generated `plugins` array).
_HEADER = {
    "$schema": "https://json.schemastore.org/claude-code-marketplace.json",
    "_comment": "GENERATED by scripts/gen_marketplace.py — do not edit by hand",
    "name": "hse-leadership-skills",
    "description": "HSE Leadership Skills — consultant-grade health, safety & environment artifact tools",
    "owner": {"name": "Eyekyam", "email": "ashley@eyekyam.com"},
}

_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _frontmatter(skill_md: Path) -> Dict[str, Any]:
    m = _FM_RE.match(skill_md.read_text(encoding="utf-8"))
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _iter_skills(repo: Path) -> List[Path]:
    """Every shipped skill folder (skills/ — the examples/ proof stubs are NOT
    marketplace plugins).

    WR-06: single level only — skills/<name>/SKILL.md (glob, not rglob), so a nested
    SKILL.md (a vendored example or a bundled knowledge copy) can never be double-counted
    as a phantom skill named after the wrong parent directory."""
    root = repo / "skills"
    if not root.is_dir():
        return []
    return sorted(child.parent for child in root.glob("*/SKILL.md"))


def build_manifest(repo: Path = REPO) -> Dict[str, Any]:
    """Build the manifest dict from every skill's metadata.plugin."""
    bundles: Dict[str, List[str]] = {}
    for skill_dir in _iter_skills(repo):
        fm = _frontmatter(skill_dir / "SKILL.md")
        meta = fm.get("metadata") or {}
        plugin = meta.get("plugin")
        if not plugin:
            continue
        bundles.setdefault(plugin, []).append(skill_dir.name)
        # D-06 cross-bundle membership: a skill owned by one bundle (metadata.plugin)
        # may also appear in others via metadata.bundled_in. The manifest stays derived
        # from frontmatter alone (no second source of truth) — WR-05. rule-6 validates
        # each bundled_in value is a registered bundle at lint time.
        for extra in (meta.get("bundled_in") or []):
            bundles.setdefault(extra, []).append(skill_dir.name)

    # hse-all (D-13/D-14): the one-line "install everything" meta-plugin. Its
    # membership is SYNTHESIZED here as the sorted union of every skill in any
    # bundle except EXCLUDE_FROM_META (the forge bundle) — the ONLY source of truth
    # for hse-all (Pitfall 4 / WR-05). No skill declares `metadata.plugin: hse-all`;
    # adding a future consultant skill auto-folds it in with zero frontmatter
    # edits. The vocab registers the NAME only (so lint rule 6 accepts it).
    #
    # Owner override (2026-06-24, supersedes the P17/QUAL-04 T-17-17 exclusion): the
    # catalog router `using-hse-skills` is now INCLUDED in hse-all. A user new to the
    # plugin who installs the one-line "install everything" pack needs the catalog
    # navigator that routes them to the right skill — that is precisely the router's
    # job, so it belongs in the pack a newcomer reaches for first. The router carries
    # `metadata.plugin: hse-core`, so it is already in the hse-core bundle and folds
    # into the union below. ONLY the contributor forge is dropped at the skill level,
    # via EXCLUDE_FROM_META_SKILLS (it is also already out via its EXCLUDE_FROM_META
    # bundle hse-systems; the skill-level set is belt-and-suspenders for any future
    # bundle it might land in). EXCLUDE_FROM_INDEX stays unchanged and still governs
    # the ROUTABLE index (build_skill_index) — you do not route TO the navigator,
    # even though it now ships inside hse-all.
    meta_all = sorted({
        skill
        for plugin, skills in bundles.items()
        if plugin not in EXCLUDE_FROM_META
        for skill in skills
        if skill not in EXCLUDE_FROM_META_SKILLS
    })
    if meta_all:
        bundles["hse-all"] = meta_all

    plugins: List[Dict[str, Any]] = []
    for name in sorted(bundles):
        # WR-04: dedup the per-bundle skills list. A skill routed into the same bundle by
        # both `plugin: X` and `bundled_in: [X]` would otherwise be listed twice (the
        # hse-all synthesis already dedups via a set; the per-bundle path did not).
        skills = sorted(set(bundles[name]))
        plugins.append({
            "name": name,
            "source": _PLUGIN_SOURCE,
            "strict": _PLUGIN_STRICT,
            "description": _describe(name),
            # Schema requires component PATHS, not bare names: each entry points at the
            # skill's subdirectory under the shared marketplace-root `skills/` folder.
            "skills": [f"./skills/{s}" for s in skills],
        })

    manifest = dict(_HEADER)
    manifest["plugins"] = plugins
    return manifest


def _plugin_version(repo: Path) -> str:
    """Release semver from `.codex-plugin/plugin.json` (single ship version)."""
    path = repo / ".codex-plugin" / "plugin.json"
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = {}
        version = data.get("version") if isinstance(data, dict) else None
        if isinstance(version, str) and version.strip():
            return version.strip()
    return "0.0.0"


def _cursor_keywords(bundle: str) -> List[str]:
    """Stable discovery tags: shared base + the pack slug after the hse- prefix."""
    tag = bundle[4:] if bundle.startswith("hse-") else bundle
    return ["hse", "safety-leadership", "agent-skills", tag]


def build_cursor_manifest(repo: Path = REPO) -> Dict[str, Any]:
    """Cursor Team Marketplace derived from the SAME Claude bundle membership.

    Maps each Claude plugin to a Cursor entry: copies name/description/skills,
    adds version/author/license/homepage/repository/category/keywords/(logo),
    sets source to ".", and strips Claude-only fields ($schema, _comment, strict).
    Skill paths stay root-relative `./skills/<name>` (no `..`, no absolutes).
    """
    claude = build_manifest(repo)
    version = _plugin_version(repo)
    logo_path = repo / _CURSOR_LOGO
    include_logo = logo_path.is_file()

    plugins: List[Dict[str, Any]] = []
    for entry in claude["plugins"]:
        # Membership already deterministically sorted inside build_manifest.
        plugin: Dict[str, Any] = {
            "name": entry["name"],
            "source": _CURSOR_SOURCE,
            "description": entry["description"],
            "version": version,
            "author": dict(_CURSOR_AUTHOR),
            "license": "Apache-2.0",
            "homepage": _REPO_URL,
            "repository": _REPO_URL,
            "category": _CURSOR_CATEGORY,
            "keywords": _cursor_keywords(entry["name"]),
            "skills": list(entry["skills"]),
        }
        if include_logo:
            plugin["logo"] = _CURSOR_LOGO
        plugins.append(plugin)

    return {
        "name": "hse-leadership-skills",
        "owner": {"name": "Eyekyam", "email": "ashley@eyekyam.com"},
        "metadata": {
            "description": claude.get(
                "description",
                "HSE Leadership Skills — consultant-grade health, safety & environment artifact tools",
            ),
            "version": version,
        },
        "plugins": plugins,
    }



def _serialize(manifest: Dict[str, Any]) -> str:
    # IN-02: pass sort_keys=True explicitly (the manifest keys are already stable, so this
    # is a no-op on current output) — making determinism explicit instead of relying on
    # dict insertion order, and matching build._serialize's json.dumps options.
    return json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def _triggers(description: str, limit: int = 3) -> List[str]:
    """Lift representative trigger phrases from a skill description.

    Inline-copied verbatim from extract_skill_cards._triggers (stdlib-`re` only)
    so the index rows carry the same trigger signal the Wiki cards do, without a
    cross-script import. Skill descriptions follow a
    "<summary>. Use this skill whenever/when …" shape: pull the clauses after the
    trigger lead-in, split on the natural comma/`or` boundaries, return the first
    few as trigger phrases."""
    text = " ".join(description.split())
    lead = re.search(
        r"[Uu]se (?:this skill|it) (?:whenever|when)\b[: ]*(.*)", text
    )
    segment = lead.group(1) if lead else text
    # Stop at the first sentence boundary after the trigger lead-in.
    segment = re.split(r"(?<=[a-z0-9])\. [A-Z]", segment)[0]
    # Split into candidate phrases on commas and standalone "or".
    parts = re.split(r",| or ", segment)
    triggers: List[str] = []
    for raw in parts:
        phrase = raw.strip().strip(".").strip()
        # Drop tiny connective fragments.
        if len(phrase.split()) < 2:
            continue
        triggers.append(phrase)
        if len(triggers) >= limit:
            break
    return triggers


def build_skill_index(repo: Path = REPO) -> List[Dict[str, Any]]:
    """One routable-skill record per shipped skill (sorted by name), derived from
    the SAME _iter_skills/_frontmatter pass as build_manifest — so the index and
    the synthesized manifest can never drift (ROUTE-02 / D-01).

    Rows are derived from each skill's OWN frontmatter (metadata.plugin +
    metadata.bundled_in), NEVER from the on-disk synthesized manifest — that file
    is stale by design until P17 (it lists ~48 of the live folder count), so
    reading it would silently drop the Phase 11–16 skills the router must route to
    (Pitfall 1).

    Excludes the router itself and the contributor forge (EXCLUDE_FROM_INDEX), and
    skips any folder with no metadata.plugin (not a routable consultant skill)."""
    rows: List[Dict[str, Any]] = []
    for skill_dir in _iter_skills(repo):
        name = skill_dir.name
        if name in EXCLUDE_FROM_INDEX:
            continue
        fm = _frontmatter(skill_dir / "SKILL.md")
        meta = fm.get("metadata") or {}
        if not meta.get("plugin"):
            continue
        bundles = [meta["plugin"]] + list(meta.get("bundled_in") or [])
        description = (fm.get("description") or "").strip()
        rows.append({
            "name": fm.get("name") or name,
            "description": description,  # FULL frontmatter paragraph, verbatim
            "bundles": sorted(set(bundles)),
            "category": meta.get("category", ""),
            "triggers": _triggers(description),
        })
    rows.sort(key=lambda r: r["name"])
    return rows


def _serialize_skill_index(repo: Path = REPO) -> str:
    """Serialize the routable-skill index to YAML text WITHOUT writing it.
    Deterministic (sort_keys=True) so a re-run produces no diff — matching the
    _serialize convention used for marketplace.json. Shared by both the --write
    emit and the --check drift gate so the two paths produce byte-identical text."""
    data = {
        "_comment": "GENERATED by scripts/gen_marketplace.py — do not edit by hand",
        "skills": build_skill_index(repo),
    }
    return yaml.safe_dump(
        data, sort_keys=True, allow_unicode=True, default_flow_style=False
    )


def _write_skill_index(repo: Path = REPO) -> str:
    """Serialize the routable-skill index to the committed YAML artifact and
    return the text. Deterministic (sort_keys=True) so a re-run produces no diff —
    matching the _serialize convention used for marketplace.json."""
    text = _serialize_skill_index(repo)
    index_path = repo / "skills" / "using-hse-skills" / "references" / "skill-index.yaml"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(text, encoding="utf-8")
    return text


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Generate/check Claude + Cursor marketplace manifests (A8 §4.7)."
    )
    g = p.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true",
                   help="diff generated Claude+Cursor manifests and skill-index against disk; nonzero on drift")
    g.add_argument("--write", action="store_true",
                   help="rewrite Claude + Cursor marketplace.json and skill-index")
    p.add_argument("--repo", default=str(REPO), help="repo root (default: inferred)")
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()
    manifest_path = repo / ".claude-plugin" / "marketplace.json"
    cursor_path = repo / ".cursor-plugin" / "marketplace.json"

    generated = _serialize(build_manifest(repo))
    generated_cursor = _serialize(build_cursor_manifest(repo))

    if args.write:
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(generated, encoding="utf-8")
        print(f"WROTE {manifest_path}")
        cursor_path.parent.mkdir(parents=True, exist_ok=True)
        cursor_path.write_text(generated_cursor, encoding="utf-8")
        print(f"WROTE {cursor_path}")
        # ROUTE-02 / D-01: emit the routable-skill index in the SAME pass from the
        # same _iter_skills source, so index + manifests can never drift. The
        # `--check` drift-diff gate covers Claude, Cursor, and the index.
        index_path = repo / "skills" / "using-hse-skills" / "references" / "skill-index.yaml"
        _write_skill_index(repo)
        print(f"WROTE {index_path}")
        return 0

    # --check (default): compare Claude marketplace, Cursor marketplace, AND the
    # router skill-index against disk. QUAL-04 / D-08 W3 + Cursor parity: a stale
    # committed artifact would mis-route or break Team Marketplace import, so the
    # CI gate must catch any of the three. Diffs are in-memory (no write); exit 1
    # if ANY artifact is stale.
    import difflib

    drift = False

    on_disk = manifest_path.read_text(encoding="utf-8") if manifest_path.is_file() else ""
    if on_disk == generated:
        print("OK: .claude-plugin/marketplace.json in sync with skill metadata.plugin")
    else:
        drift = True
        print(
            "DRIFT: .claude-plugin/marketplace.json is stale; run `gen_marketplace.py --write`",
            file=sys.stderr,
        )
        for line in difflib.unified_diff(
            on_disk.splitlines(), generated.splitlines(),
            fromfile=".claude-plugin/marketplace.json (on disk)", tofile="generated",
            lineterm="",
        ):
            print(line, file=sys.stderr)

    on_disk_cursor = cursor_path.read_text(encoding="utf-8") if cursor_path.is_file() else ""
    if on_disk_cursor == generated_cursor:
        print("OK: .cursor-plugin/marketplace.json in sync with Claude bundle membership")
    else:
        drift = True
        print(
            "DRIFT: .cursor-plugin/marketplace.json is stale; run `gen_marketplace.py --write`",
            file=sys.stderr,
        )
        for line in difflib.unified_diff(
            on_disk_cursor.splitlines(), generated_cursor.splitlines(),
            fromfile=".cursor-plugin/marketplace.json (on disk)", tofile="generated",
            lineterm="",
        ):
            print(line, file=sys.stderr)

    index_path = SKILL_INDEX if repo == REPO else (
        repo / "skills" / "using-hse-skills" / "references" / "skill-index.yaml"
    )
    generated_index = _serialize_skill_index(repo)
    on_disk_index = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    if on_disk_index == generated_index:
        print("OK: skill-index.yaml in sync with skill metadata.plugin")
    else:
        drift = True
        print("DRIFT: skill-index.yaml is stale; run `gen_marketplace.py --write`", file=sys.stderr)
        for line in difflib.unified_diff(
            on_disk_index.splitlines(), generated_index.splitlines(),
            fromfile="skill-index.yaml (on disk)", tofile="generated", lineterm="",
        ):
            print(line, file=sys.stderr)

    return 1 if drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
