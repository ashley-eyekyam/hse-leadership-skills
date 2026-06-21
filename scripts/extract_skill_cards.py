#!/usr/bin/env python3
"""extract_skill_cards.py — seed the FACTUAL fields of every skill's Wiki card.

The Wiki user manual (`docs/wiki/<Pack>.md`) carries one medium-depth "skill
card" per consultant skill. The factual half of each card — name, audience,
Packs (bundle membership), version, jurisdiction, trigger phrases — must be
transcribed from each skill's own `SKILL.md` frontmatter + the generated
`.claude-plugin/marketplace.json`, NEVER invented (spec §6/§10.2; threat
T-jld-01/T-jld-03). This script is that authoring aid: per-pack authors run it
to seed the factual fields, then fill the prose fields (currently the literal
token `TODO`) from each skill's `SKILL.md`.

It is ALSO the verifier's drift hook (spec §13): re-running it and diffing the
factual fields against the committed Wiki pages surfaces any factual drift.

Skill iteration mirrors `gen_marketplace.py::_iter_skills` exactly (single-level
`skills/*/SKILL.md` glob — the stray `skills/README.md` has no SKILL.md so the
glob excludes it). `hse-skill-forge` is EXCLUDED: it is the contributor build
tool, documented only as a Home "Extending the pack" note (spec §3/§5.2). The
result is therefore exactly 48 consultant skills.

The `Packs` field is read from `marketplace.json` (NOT the single
`metadata.plugin`): every bundle whose `skills` list contains `./skills/<name>`,
EXCLUDING the synthesized `hse-all` meta-plugin and the forge bundle
`hse-systems`. A shared PHA tool therefore shows its true multi-pack membership
(e.g. bowtie-builder → hse-chemicals, hse-mining, hse-process).

CLI:
  (default)            print every skill's full seed card (markdown draft stub)
                       to stdout — `### <name>` per skill, factual fields filled,
                       prose fields = TODO. (`grep -c '^### '` == 48.)
  --facts              emit ONLY the factual fields in a stable, diffable form
                       keyed by skill name (sorted) — the verifier re-runs this
                       and diffs against the committed pages (spec §13).
  --json               same factual data as machine-readable JSON.
  --repo PATH          point at the repo root (default: inferred from this file).

Output is idempotent (skills emitted in sorted order). Stdlib + pyyaml only
(mirrors gen_marketplace.py — no new dependencies; threat T-jld-SC).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
MANIFEST = REPO / ".claude-plugin" / "marketplace.json"

# Default wiki clone URL (documented; the live value is derived from the origin
# remote at runtime so the owner is never hard-coded — shared with
# publish_wiki.py).
DEFAULT_WIKI_URL = "https://github.com/ashley-eyekyam/hse-leadership-skills.wiki.git"

# Excluded from the per-skill consultant manual entirely: the build-time forge is
# documented only as a Home note (spec §3/§5.2).
EXCLUDE_SKILLS = {"hse-skill-forge"}

# Bundles that are NOT real packs for the Packs field: the synthesized
# "install everything" meta-plugin and the contributor forge bundle.
EXCLUDE_BUNDLES = {"hse-all", "hse-systems"}

# The prose card fields the author fills from SKILL.md (spec §6) — emitted as the
# literal token TODO in the seed so an unfilled card is grep-detectable.
PROSE_FIELDS = [
    "Produces",
    "Use when",
    "Don't use for",
    "Have ready",
    "You get",
    "Pairs well with",
]

_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _frontmatter(skill_md: Path) -> Dict[str, Any]:
    """Parse a SKILL.md YAML frontmatter block (mirrors gen_marketplace)."""
    m = _FM_RE.match(skill_md.read_text(encoding="utf-8"))
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _iter_skills(repo: Path) -> List[Path]:
    """Every shipped skill folder — `skills/<name>/SKILL.md`, single level only
    (glob, not rglob), exactly mirroring gen_marketplace._iter_skills so the two
    scripts can never diverge on which folders count as skills (WR-06)."""
    root = repo / "skills"
    if not root.is_dir():
        return []
    return sorted(child.parent for child in root.glob("*/SKILL.md"))


def wiki_url_from_origin(repo: Path = REPO) -> str:
    """Derive the `.wiki.git` clone URL from the `origin` remote — swap a trailing
    `.git` for `.wiki.git`. Never hard-codes the owner; falls back to the
    documented default if the remote cannot be read (e.g. no git, no origin)."""
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "remote", "get-url", "origin"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return DEFAULT_WIKI_URL
    if not out:
        return DEFAULT_WIKI_URL
    if out.endswith(".git"):
        return out[: -len(".git")] + ".wiki.git"
    return out + ".wiki.git"


def _packs_index(manifest_path: Path = MANIFEST) -> Dict[str, List[str]]:
    """Map each skill name → sorted list of real pack bundles it belongs to,
    read from marketplace.json (the single source of bundle membership — NOT
    metadata.plugin, so shared skills show true multi-pack membership)."""
    index: Dict[str, List[str]] = {}
    if not manifest_path.is_file():
        return index
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    for bundle in data.get("plugins", []):
        name = bundle.get("name")
        if name in EXCLUDE_BUNDLES:
            continue
        for skill_path in bundle.get("skills", []):
            skill = skill_path.rsplit("/", 1)[-1]
            index.setdefault(skill, [])
            if name not in index[skill]:
                index[skill].append(name)
    for skill in index:
        index[skill].sort()
    return index


def _triggers(description: str, limit: int = 3) -> List[str]:
    """Lift representative trigger phrases from the skill description.

    Skill descriptions follow a "<summary>. Use this skill whenever/when …"
    shape. Pull the clauses after the trigger lead-in, split on the natural
    comma/`or` boundaries, and return the first few as trigger phrases."""
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


def collect(repo: Path = REPO) -> List[Dict[str, Any]]:
    """Collect the factual seed record for every consultant skill (sorted)."""
    packs = _packs_index(repo / ".claude-plugin" / "marketplace.json")
    records: List[Dict[str, Any]] = []
    for skill_dir in _iter_skills(repo):
        name = skill_dir.name
        if name in EXCLUDE_SKILLS:
            continue
        fm = _frontmatter(skill_dir / "SKILL.md")
        meta = fm.get("metadata") or {}
        description = (fm.get("description") or "").strip()
        records.append({
            "name": fm.get("name") or name,
            "folder": name,
            "description": description,
            "audience": list(meta.get("audience") or []),
            "version": str(meta.get("version") or ""),
            "jurisdiction": list(meta.get("jurisdiction") or [])
            if isinstance(meta.get("jurisdiction"), list)
            else ([meta["jurisdiction"]] if meta.get("jurisdiction") else []),
            "plugin": meta.get("plugin") or "",
            "packs": packs.get(name, []),
            "triggers": _triggers(description),
        })
    records.sort(key=lambda r: r["folder"])
    return records


def _fmt_list(values: List[str]) -> str:
    return ", ".join(values) if values else "—"


def render_seed_card(rec: Dict[str, Any]) -> str:
    """A markdown draft card stub: factual fields filled, prose fields = TODO.

    Anchored with `### <folder>` so `grep -c '^### '` over the full output is the
    48-skill count check, and each card deep-links via its lower-cased hyphenated
    folder name."""
    lines: List[str] = []
    lines.append(f"### {rec['folder']}")
    lines.append("")
    # Each labelled field is its own markdown list item so it renders on its own
    # line — a bare `**Label:**` line per field collapses into one run-on
    # paragraph on GitHub (soft line breaks become spaces). Bullets match the
    # published pack-page cards and Home's "how to read a card" legend.
    lines.append(f"- **For:** {_fmt_list(rec['audience'])}")
    lines.append(f"- **Packs:** {_fmt_list(rec['packs'])}")
    lines.append(f"- **Version:** {rec['version'] or '—'}")
    lines.append(f"- **Jurisdiction:** {_fmt_list(rec['jurisdiction'])}")
    triggers = rec["triggers"]
    lines.append(
        "- **Trigger:** "
        + ("; ".join(triggers) if triggers else "TODO")
    )
    lines.append("")
    for field in PROSE_FIELDS:
        lines.append(f"- **{field}:** TODO")
    lines.append("")
    return "\n".join(lines)


def render_facts(rec: Dict[str, Any]) -> str:
    """The stable, diffable factual-field block keyed by skill name — the
    verifier re-runs `--facts` and diffs this against the committed pages."""
    return (
        f"{rec['folder']}\n"
        f"  name: {rec['name']}\n"
        f"  audience: {_fmt_list(rec['audience'])}\n"
        f"  packs: {_fmt_list(rec['packs'])}\n"
        f"  version: {rec['version']}\n"
        f"  jurisdiction: {_fmt_list(rec['jurisdiction'])}\n"
        f"  triggers: {' | '.join(rec['triggers']) if rec['triggers'] else '—'}\n"
    )


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Seed the factual fields of every skill's Wiki card "
                    "(authoring aid + verifier drift hook, spec §6/§13)."
    )
    g = p.add_mutually_exclusive_group()
    g.add_argument(
        "--facts", action="store_true",
        help="emit only the stable, diffable factual fields (the verifier hook)",
    )
    g.add_argument(
        "--json", action="store_true",
        help="emit the factual seed records as JSON",
    )
    p.add_argument(
        "--repo", default=str(REPO),
        help="repo root (default: inferred from this script's location)",
    )
    p.add_argument(
        "--wiki-url", action="store_true",
        help="print the derived .wiki.git clone URL (from origin) and exit",
    )
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()

    if args.wiki_url:
        print(wiki_url_from_origin(repo))
        return 0

    records = collect(repo)

    if args.json:
        payload = {
            "wiki_url": wiki_url_from_origin(repo),
            "count": len(records),
            "skills": records,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
        return 0

    if args.facts:
        for rec in records:
            sys.stdout.write(render_facts(rec))
        return 0

    # Default: full seed cards to stdout (one `### <folder>` per skill).
    for rec in records:
        print(render_seed_card(rec))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
