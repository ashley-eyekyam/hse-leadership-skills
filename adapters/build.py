#!/usr/bin/env python3
"""build.py — the Cross-platform Adapter build (Unit C, §3.1).

Reads one read-only ``skills/<name>/SKILL.md``, parses it ONCE into a host-neutral
``AdaptedSkill`` intermediate (parse once → emit four times), and renders it
through four platform emitters: ChatGPT Custom GPT · Gemini Gem · MS Copilot ·
generic system-prompt (Task 2). C REUSES skill content; it never re-authors it.

stdlib + pyyaml only — the same dependency floor as A7/A8/A10 (C Decision 3 / §2.5).

R2 (Decision 1, the headline): the build PARSES the ``<!-- hse:block:* -->``
markers to extract each block (the anchors do their one job), then emits
platform-native instruction text with the markers STRIPPED on every Tier-B host
(a stray HTML comment can render as literal text in a chat field). The markers are
preserved verbatim only inside the uploaded knowledge SKILL.md copy. CI proves the
block CONTENTS survived marker-free (§3.2).

This module reuses — rather than re-invents — the ``lint_skills`` regex family
(``INLINE_BLOCKS``, ``_inner_region``, ``_below_end``, ``_split_frontmatter``) and
the ``gen_marketplace`` ``_serialize`` byte-identical JSON contract, so a re-run is
deterministic and idempotent (Pitfall 5).

Public surface (this plan, Task 1):
    AdaptedSkill            — the host-neutral intermediate (Pattern 1)
    extract_blocks(text)    — the five-block CONTENTS dict (fail loud — A2 mitigation)
    strip_markers(text)     — remove only the comment token, keep surrounding text
    has_a7(skill_dir)       — scripts/hse_components present (DETECT, never assume)
    load_skill(skill_dir)   — parse one SKILL.md into an AdaptedSkill
    load_platforms()        — read platforms.yaml once
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

# adapters/ -> repo root
ADAPTERS_DIR = Path(__file__).resolve().parent
REPO = ADAPTERS_DIR.parent
SKILLS_DIR = REPO / "skills"
PLATFORMS_FILE = ADAPTERS_DIR / "platforms.yaml"
DISCLAIMER_FILE = REPO / "DISCLAIMER.md"

# The five inline blocks — the SAME list the linter anti-drifts (lint_skills.INLINE_BLOCKS).
# Kept as a local constant so build.py has no import-time dependency on the linter's
# REPO-rooted module state, but it is byte-identical to that single source.
INLINE_BLOCKS = ["deid", "kb-selection", "orchestration", "report-output", "attribution"]

# --- the marker regex family (reused shape from lint_skills / Pattern 2) -------

# Captures each block's CONTENTS strictly between its :start/:end markers.
_BLOCK_RE = re.compile(
    r"<!--\s*hse:block:(?P<name>[a-z-]+):start\s*-->(?P<body>.*?)"
    r"<!--\s*hse:block:(?P=name):end\s*-->",
    re.S,
)

# Removes ONLY the marker comment TOKEN (not the whole line) so a marker that shares
# its line with prose — e.g. `<!-- hse:block:report-output:start -->## Output format`
# at risk-assessment line 297 — keeps the trailing `## Output format` heading anchor
# R2 depends on (Pitfall 1). Never anchor-and-consume the rest of the line.
MARKER_LINE_RE = re.compile(
    r"[ \t]*<!--\s*hse:block:[a-z-]+:(?:start|end)\s*-->[ \t]*"
)

# Any residual hse:block literal — the post-strip assertion the validator depends on.
_RESIDUAL_MARKER_RE = re.compile(r"<!--\s*hse:block")

_FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


# --- frontmatter / region helpers (reused shape from lint_skills) --------------


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _split_frontmatter(text: str) -> tuple:
    """Return (frontmatter_dict, body_text) — mirrors lint_skills._split_frontmatter."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, m.group(2)


def _below_end(body: str, block: str) -> str:
    """The per-skill prose AUTHORED below a block's :end marker, up to the next
    block start (roster / jurisdiction rows — presence-only, verbatim). Mirrors
    lint_skills._below_end."""
    marker = f"<!-- hse:block:{block}:end -->"
    if marker not in body:
        return ""
    after = body.split(marker, 1)[1]
    nxt = re.search(r"<!-- hse:block:", after)
    return after[: nxt.start()] if nxt else after


# --- the parse layer (Pattern 1 / Pattern 2 / §3.0–§3.2) -----------------------


def extract_blocks(text: str) -> Dict[str, str]:
    """Return the five-block CONTENTS dict keyed by INLINE_BLOCKS name.

    FAIL LOUD (A2 mitigation, RESEARCH A2 risk): if any of the five expected blocks
    is missing/malformed in ``text``, raise ValueError — a mis-extracted skill must
    never ship a bundle silently missing a non-negotiable.
    """
    found = {m["name"]: m["body"].strip() for m in _BLOCK_RE.finditer(text)}
    missing = [b for b in INLINE_BLOCKS if b not in found or not found[b]]
    if missing:
        raise ValueError(
            f"extract_blocks: missing/empty hse:block(s) {missing} — "
            f"the skill is malformed; refusing to adapt it (A2 mitigation)"
        )
    # Return only the canonical five, in canonical order.
    return {b: found[b] for b in INLINE_BLOCKS}


def strip_markers(text: str) -> str:
    """Remove every ``<!-- hse:block:*:start|end -->`` comment TOKEN, keeping any
    surrounding text on the same line (Pitfall 1 — the report-output marker shares
    its line with ``## Output format``)."""
    return MARKER_LINE_RE.sub("", text)


def has_a7(skill_dir: Path) -> bool:
    """True iff the skill declares an A7 dependency — DETECT, never assume (C §3.0).

    A skill carries ``scripts/hse_components`` as a symlink (B1/B5) or not at all
    (B3). ``.exists()`` resolves the symlink, so this is symlink-or-real."""
    return (Path(skill_dir) / "scripts" / "hse_components").exists()


def _extract_intake(body: str) -> str:
    """The §2.7 structured-intake question set — the ``## Workflow`` section through
    to the next top-level ``##`` heading (the method subsection or a block).

    Presence-driven: the intake table + its preamble open every skill's Workflow
    (verified across risk-assessment, toolbox-talk, incident-investigation). Captured
    verbatim; the build never edits a question (C §3.0)."""
    m = re.search(r"\n##[ \t]+Workflow\b", body)
    if not m:
        return ""
    start = m.start()
    # Next top-level "## " heading after Workflow (not "### ", not a marker line).
    nxt = re.search(r"\n##[ \t]+(?!#)", body[m.end():])
    end = m.end() + nxt.start() if nxt else len(body)
    return body[start:end].strip()


def _resolve_knowledge_files(skill_dir: Path) -> List[Path]:
    """Enumerate the knowledge files a bundle uploads: references/* + the resolved
    KB fragments named in references/_skill-kb.md + the DISCLAIMER + a SKILL.md copy.

    Every ``../../knowledge-base/…`` reference is resolved with ``Path.resolve()`` and
    asserted to stay UNDER the repo root before it is recorded (T-07-01-PT mitigation:
    no path-escape when composing knowledge copies). Returns sorted, de-duplicated,
    POSIX-comparable absolute paths (Pitfall 5 determinism)."""
    skill_dir = Path(skill_dir).resolve()
    files: List[Path] = []

    # references/* (the on-demand pointers + the de-id checklist where present).
    refs = skill_dir / "references"
    if refs.is_dir():
        files.extend(sorted(p for p in refs.iterdir() if p.is_file()))

    # Resolved KB fragments named in references/_skill-kb.md (the rule-9 manifest).
    manifest = refs / "_skill-kb.md"
    if manifest.is_file():
        for m in re.finditer(r"(\.\./)+knowledge-base/[A-Za-z0-9_./-]+\.md", _read(manifest)):
            target = (manifest.parent / m.group(0)).resolve()
            # V5 input validation — the resolved path must stay under the repo root.
            if REPO not in target.parents and target != REPO:
                raise ValueError(
                    f"_resolve_knowledge_files: KB reference {m.group(0)!r} escapes "
                    f"the repo root ({target}) — refusing (T-07-01-PT)"
                )
            if target.is_file():
                files.append(target)

    # The canonical DISCLAIMER (a non-negotiable knowledge file on every host).
    if DISCLAIMER_FILE.is_file():
        files.append(DISCLAIMER_FILE.resolve())

    # The marker-PRESERVED SKILL.md copy (re-ingestible by the repo linter, §3.2).
    skill_md = skill_dir / "SKILL.md"
    if skill_md.is_file():
        files.append(skill_md.resolve())

    # De-duplicate (a checklist may be both a reference and KB-named) + sort by POSIX path.
    seen = {}
    for p in files:
        seen[p.as_posix()] = p
    return [seen[k] for k in sorted(seen)]


@dataclass
class AdaptedSkill:
    """The host-neutral intermediate (Pattern 1). Parsed ONCE from one SKILL.md;
    the four emitters (Task 2) render it. All host-specific surface lives in the
    emitter + its platforms.yaml block, never here (drift containment, §7)."""

    name: str
    description: str                       # frontmatter, third-person
    instructions_core: str                # lean body, markers STRIPPED, headings kept
    blocks: Dict[str, str]                # the five INLINE_BLOCKS CONTENTS only
    roster_prose: str                     # below orchestration:end, verbatim
    jurisdiction_rows: str                # below kb-selection:end, verbatim
    intake_questions: str                 # the §2.7 Workflow intake set, verbatim
    knowledge_files: List[Path] = field(default_factory=list)
    has_a7: bool = False


def load_skill(skill_dir: Path) -> AdaptedSkill:
    """Parse one ``skills/<name>/SKILL.md`` into an ``AdaptedSkill`` (C §3.1 step 1-2).

    Read SKILL.md → split frontmatter+body → extract the five block CONTENTS
    (fail loud) → strip markers from the body for instructions_core → capture the
    below-:end roster + jurisdiction rows + the §2.7 intake set verbatim →
    enumerate knowledge files → detect has_a7."""
    skill_dir = Path(skill_dir)
    text = _read(skill_dir / "SKILL.md")
    fm, body = _split_frontmatter(text)

    blocks = extract_blocks(body)
    return AdaptedSkill(
        name=fm.get("name", skill_dir.name),
        description=str(fm.get("description", "") or ""),
        instructions_core=strip_markers(body),
        blocks=blocks,
        roster_prose=_below_end(body, "orchestration").strip(),
        jurisdiction_rows=_below_end(body, "kb-selection").strip(),
        intake_questions=_extract_intake(body),
        knowledge_files=_resolve_knowledge_files(skill_dir),
        has_a7=has_a7(skill_dir),
    )


def load_platforms(path: Path = PLATFORMS_FILE) -> dict:
    """Read platforms.yaml once (analog: template/metadata-vocab.yaml)."""
    return yaml.safe_load(_read(Path(path)))
