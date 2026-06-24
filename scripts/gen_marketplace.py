#!/usr/bin/env python3
"""gen_marketplace.py — generate .claude-plugin/marketplace.json (A8 §4.7, QA-04).

The marketplace manifest is GENERATED from each skill's `metadata.plugin`
frontmatter — never hand-maintained (no duplication; a skill's bundle membership
lives in exactly one place, its own SKILL.md). Each distinct `metadata.plugin`
value becomes one plugin entry whose `skills` list is the folders that name it.

  --check   regenerate BOTH the manifest and the router skill-index in memory and
            DIFF each against its on-disk artifact; exit nonzero if EITHER drifts
            (the CI gate — research §4.7; QUAL-04 index drift gate added Phase 17).
  --write   rewrite the on-disk manifest AND the router skill-index from the skills.

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
    # P17 (QUAL-04): also drop the non-consumer skills named in EXCLUDE_FROM_INDEX
    # — the router (`using-hse-skills`) and the contributor forge (`hse-skill-forge`).
    # The router carries `metadata.plugin: hse-core` so it ships INSIDE the hse-core
    # bundle, but it is a meta/routing skill, not a consultant artifact, so it must
    # NOT appear in the "install everything" consumer pack (T-17-17). EXCLUDE_FROM_INDEX
    # is exactly that {router, forge} set; reusing it keeps BOTH named exclusion
    # constants byte-unchanged while excluding the router from hse-all symmetrically
    # with the index. (The forge is already out via its EXCLUDE_FROM_META bundle; this
    # also covers any future bundle the forge might land in.)
    meta_all = sorted({
        skill
        for plugin, skills in bundles.items()
        if plugin not in EXCLUDE_FROM_META
        for skill in skills
        if skill not in EXCLUDE_FROM_INDEX
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
    p = argparse.ArgumentParser(description="Generate/check marketplace.json (A8 §4.7).")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true",
                   help="diff the generated manifest against disk; nonzero on drift")
    g.add_argument("--write", action="store_true", help="rewrite marketplace.json")
    p.add_argument("--repo", default=str(REPO), help="repo root (default: inferred)")
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()
    manifest_path = repo / ".claude-plugin" / "marketplace.json"

    generated = _serialize(build_manifest(repo))

    if args.write:
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(generated, encoding="utf-8")
        print(f"WROTE {manifest_path}")
        # ROUTE-02 / D-01: emit the routable-skill index in the SAME pass from the
        # same _iter_skills source, so index + manifest can never drift. The
        # `--check` index drift-diff gate is now wired in below (Phase 17, QUAL-04),
        # so a fresh `--write` then `--check` is clean for BOTH artifacts.
        index_path = repo / "skills" / "using-hse-skills" / "references" / "skill-index.yaml"
        _write_skill_index(repo)
        print(f"WROTE {index_path}")
        return 0

    # --check (default): compare BOTH the manifest AND the router skill-index against
    # disk. QUAL-04 / D-08 W3: a stale committed skill-index would mis-route the
    # catalog at runtime (T-17-15), so the CI gate must catch index drift the same
    # way it catches manifest drift. Both diffs are computed in-memory (no write);
    # the gate fails (exit 1) if EITHER artifact is stale. EXCLUDE_FROM_INDEX /
    # EXCLUDE_FROM_META are honored by build_skill_index/build_manifest, so the
    # router and the forge stay out of the index and out of hse-all respectively.
    import difflib

    drift = False

    on_disk = manifest_path.read_text(encoding="utf-8") if manifest_path.is_file() else ""
    if on_disk == generated:
        print("OK: marketplace.json in sync with skill metadata.plugin")
    else:
        drift = True
        print("DRIFT: marketplace.json is stale; run `gen_marketplace.py --write`", file=sys.stderr)
        for line in difflib.unified_diff(
            on_disk.splitlines(), generated.splitlines(),
            fromfile="marketplace.json (on disk)", tofile="generated", lineterm="",
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
