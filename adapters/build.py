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

import argparse
import json
import re
import shutil
import sys
import tempfile
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


def _rows_below_end(body: str, block: str) -> str:
    """The per-skill ROWS subsection below a block's :end marker — bounded to the next
    top-level ``## `` heading so it captures only the presence-only rows (the
    jurisdiction table), NOT the Workflow/method prose that may sit in the gap before
    the next block marker. ``_below_end`` is unbounded (used for the roster, whose
    block is immediately followed by the orchestration roster then a marker)."""
    raw = _below_end(body, block)
    nxt = re.search(r"(?m)^##[ \t]+(?!#)", raw)
    return raw[: nxt.start()] if nxt else raw


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
    """The §2.7 structured-intake question set — the ``## Workflow`` preamble through
    the end of the ``### Step 0 — … intake`` subsection (bounded before the
    ``### … method`` subsection so it carries the intake question set, NOT the full
    domain method prose, which is movable and lives in references/METHODOLOGY.md).

    Presence-driven: every skill's Workflow opens with a one-at-a-time intake table
    (verified across risk-assessment, toolbox-talk, incident-investigation). Captured
    verbatim; the build never edits a question (C §3.0)."""
    m = re.search(r"(?m)^##[ \t]+Workflow\b", body)
    if not m:
        return ""
    start = m.start()
    rest = body[m.end():]
    # The next "### " subsection that is NOT a "Step 0 … intake" subsection bounds the
    # intake (i.e. the "### … method" subsection or the orchestration block).
    end = len(body)
    for sm in re.finditer(r"(?m)^###[ \t]+(?P<title>.+)$", rest):
        if "intake" in sm.group("title").lower():
            continue
        end = m.end() + sm.start()
        break
    # Never cross into the next top-level ## block (orchestration) either.
    top = re.search(r"(?m)^##[ \t]+(?!#)", rest)
    if top:
        end = min(end, m.end() + top.start())
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
        # Roster / rows / intake all flow into the emitted INSTRUCTION surface, so they
        # carry the R2 strip too (a Workflow that ends right before the orchestration
        # block can otherwise drag in that block's :start marker line — §3.2).
        roster_prose=strip_markers(_below_end(body, "orchestration")).strip(),
        jurisdiction_rows=strip_markers(_rows_below_end(body, "kb-selection")).strip(),
        intake_questions=strip_markers(_extract_intake(body)).strip(),
        knowledge_files=_resolve_knowledge_files(skill_dir),
        has_a7=has_a7(skill_dir),
    )


def load_platforms(path: Path = PLATFORMS_FILE) -> dict:
    """Read platforms.yaml once (analog: template/metadata-vocab.yaml)."""
    return yaml.safe_load(_read(Path(path)))


# === Task 2: the four emitters + char-fit + CLI ================================

PLATFORMS = ["chatgpt", "gemini", "copilot", "generic"]

# The A4 house-standard section order (C §3.4) the markdown-report degradation
# follows on every non-Code-Interpreter host (Gemini/Copilot/generic).
HOUSE_SECTION_ORDER = [
    "Cover",
    "Classification",
    "Executive summary",
    "Scope & method",
    "Key findings (risk-rated)",
    "Hierarchy-of-controls table",
    "Recommendations (owner/due)",
    "Regulatory basis",
    "Limitations & de-id notice",
]

# The report-output instruction per report path (§3.3 vs §3.4 degradation).
_ENGINE_REPORT = (
    "## Output format\n\n"
    "Assemble a `report.json` conforming to the shared report-model schema, then "
    "run `generate_report.py` in Code Interpreter on the assembled `report.json` to "
    "render the branded DOCX + PDF (the A4 engine + bundled fonts are uploaded as "
    "Code-Interpreter assets). Resolve branding from the user's `brand.yaml` (Eyekyam "
    "default); surface the output paths and a one-line provenance note."
)


def _markdown_report_instruction() -> str:
    order = " → ".join(HOUSE_SECTION_ORDER)
    return (
        "## Output format\n\n"
        "This host has no Code Interpreter, so emit the deliverable as a **structured "
        "markdown report** following the house section order (" + order + "). Apply the "
        "A7 logic as prompt-side discipline: rank every control by the hierarchy of "
        "controls (no PPE-only treatment without justification) and give every SMART "
        "action a named owner and a due date — by instruction, not a script call. The "
        "report stays specific, HoC-ranked, de-identified, and owner/date-bearing."
    )


# The canonical DISCLAIMER preamble line (a one-line pointer survives into every
# instruction surface; the full DISCLAIMER.md is a knowledge file — §3.8 check 3).
DISCLAIMER_PREAMBLE = (
    "> **Disclaimer — decision-support only.** Outputs are drafts to assist a "
    "competent person — not finished, approved, or legal deliverables; every output "
    "must be reviewed and signed off by a competent person. (Full text: "
    "`knowledge/DISCLAIMER.md`.)"
)


# --- the char-fit / spill algorithm (§3.7, Decision 6) -------------------------

# Headings whose section body is MOVABLE prose (longest-movable-first spill). The
# IRREDUCIBLE CORE (de-id block, HoC instruction, §2.7 intake, orchestration single-
# thread, report-call/degradation, attribution, DISCLAIMER preamble) is NEVER listed
# here, so it can never be spilled (Pitfall 3 / T-07-01-NN).
_MOVABLE_HEADINGS = [
    "## Subagent roster (preserved as a sequential checklist)",
    "## Jurisdiction routing",
    "## Attribution (non-intrusive)",
    "## Reference material",
    "## When to use this skill",
]

# The compact single-thread fallback line every degraded host keeps inline (the
# orchestration "instruction", not the full block — §3.7). Extracted from the block's
# own fallback line so it is the skill's own words, never invented.
_FALLBACK_RE = re.compile(r"(?m)^>\s*Single-threaded fallback:.*?(?:\n(?!>).*)*")


def _orchestration_instruction(block: str) -> str:
    """The irreducible orchestration instruction: the De-identifier-first sequencing
    + the single-thread fallback line + the mandatory Critic/QA pass — a compact
    directive, not the full multi-step block (which spills to the roster checklist /
    knowledge)."""
    fallback = ""
    m = _FALLBACK_RE.search(block)
    if m:
        fallback = m.group(0).strip()
    return (
        "## Agentic Execution (single-thread on this host)\n\n"
        "Run the De-identifier FIRST (sequential gate — its scrubbed output feeds every "
        "later step), then work through the roster checklist sequentially in this one "
        "context, keeping the same decomposition discipline, and finish with the "
        "MANDATORY Critic/QA pass before delivery.\n\n" + fallback
    ).strip()


def _section_span(text: str, heading: str):
    """Return (start, end) char offsets of a top-level ``## heading`` section body
    (heading line through the next ``## `` heading), or None if absent."""
    m = re.search(r"(?m)^" + re.escape(heading) + r"[ \t]*$", text)
    if not m:
        return None
    start = m.start()
    nxt = re.search(r"(?m)^##[ \t]+(?!#)", text[m.end():])
    end = m.end() + nxt.start() if nxt else len(text)
    return start, end


class IrreducibleOverflow(Exception):
    """Raised when the irreducible core alone exceeds a platform char_limit — a hard
    bundle failure (§3.7 step 4); never a silent truncation."""


def char_fit(body: str, char_limit: int, spilled: Optional[List[str]] = None) -> str:
    """Fit ``body`` to ``char_limit`` by spilling MOVABLE prose to a knowledge
    pointer, longest-movable-first; the irreducible core is never moved.

    Records each moved heading in ``spilled`` (if given). Raises
    ``IrreducibleOverflow`` if the body still overflows once only the irreducible
    core remains — CI then reports which platform/skill overflowed (§3.7)."""
    if len(body) <= char_limit:
        return body

    work = body
    # Spill candidates present in this body, longest section first.
    candidates = []
    for heading in _MOVABLE_HEADINGS:
        span = _section_span(work, heading)
        if span:
            candidates.append((span[1] - span[0], heading))
    candidates.sort(reverse=True)

    for _size, heading in candidates:
        if len(work) <= char_limit:
            break
        span = _section_span(work, heading)
        if not span:
            continue
        start, end = span
        pointer = (
            f"{heading}\n\n_Full detail moved to the knowledge upload "
            f"(see `knowledge/`)._\n\n"
        )
        work = work[:start] + pointer + work[end:]
        if spilled is not None:
            spilled.append(heading)

    if len(work) > char_limit:
        raise IrreducibleOverflow(
            f"irreducible core ({len(work)} chars) exceeds char_limit {char_limit} "
            f"after spilling movable prose — the body is too heavy for this host; "
            f"lean it as authored (A2 §2.5), never truncate"
        )
    return work


# --- shared render: the lean body in the canonical order -----------------------


def _render_body(adapted: AdaptedSkill, report_instruction: str) -> str:
    """Render the AdaptedSkill into the platform-neutral instruction body in the
    §3.3 canonical order, markers already stripped. ``report_instruction`` is the
    Code-Interpreter call (ChatGPT) or the markdown-degradation block (others).

    Ordering separates the IRREDUCIBLE CORE (de-id block · HoC/kb-selection rubric ·
    §2.7 intake · compact orchestration single-thread instruction · report · attribution ·
    disclaimer preamble) from MOVABLE sections (the roster checklist + the jurisdiction
    rows) that the char-fit spill (§3.7) may move to knowledge under their `## ` headings.
    The irreducible core is never under a `_MOVABLE_HEADINGS` heading, so it can never
    be spilled (Pitfall 3 / T-07-01-NN)."""
    parts = [
        f"# {adapted.name}",
        DISCLAIMER_PREAMBLE,
        adapted.blocks["deid"],
        adapted.blocks["kb-selection"],
        adapted.intake_questions,
        _orchestration_instruction(adapted.blocks["orchestration"]),
        report_instruction,
        # --- movable sections below (spillable under their own ## headings) ---
        "## Subagent roster (preserved as a sequential checklist)\n\n"
        + (adapted.roster_prose or "Single-threaded by design — no subagents."),
        "## Jurisdiction routing\n\n" + (adapted.jurisdiction_rows or ""),
        adapted.blocks["attribution"],
    ]
    return "\n\n".join(p.strip() for p in parts if p and p.strip()) + "\n"


def _serialize(obj: dict) -> str:
    """Byte-identical JSON — the same contract as gen_marketplace._serialize
    (sorted keys, indent 2, ensure_ascii False, trailing newline) so re-runs are
    idempotent (Pitfall 5)."""
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def _conversation_starters(intake: str, limit: int = 4) -> List[str]:
    """Lift conversation starters from the intake's first MCQ options (§3.3)."""
    starters: List[str] = []
    for line in intake.splitlines():
        cells = [c.strip() for c in line.split("|") if c.strip()]
        # A table row whose Type cell is MCQ and whose options cell has choices.
        if len(cells) >= 4 and "MCQ" in cells[2]:
            for opt in re.split(r"[·|]| · ", cells[3]):
                opt = re.sub(r"\(.*?\)|\*+|_+", "", opt).strip(" -—")
                if opt and len(opt) < 60:
                    starters.append(opt)
            if starters:
                break
    return starters[:limit]


def _write_knowledge(adapted: AdaptedSkill, out: Path) -> List[str]:
    """Copy the knowledge files into ``out/knowledge/`` and return their sorted
    POSIX-relative names."""
    kdir = out / "knowledge"
    kdir.mkdir(parents=True, exist_ok=True)
    names = []
    for src in adapted.knowledge_files:
        # The marker-preserved SKILL.md copy keeps the skill's own name distinct.
        dest_name = src.name
        if src.name == "SKILL.md":
            dest_name = "SKILL.md"
        shutil.copyfile(src, kdir / dest_name)
        names.append(f"knowledge/{dest_name}")
    return sorted(set(names))


def _emit_common(adapted, out, report_instruction, char_limit):
    """Render + char-fit the body, write knowledge/, return (instructions, knowledge)."""
    out.mkdir(parents=True, exist_ok=True)
    body = _render_body(adapted, report_instruction)
    instructions = char_fit(body, char_limit)
    knowledge = _write_knowledge(adapted, out)
    return instructions, knowledge


def emit_chatgpt(adapted: AdaptedSkill, out: Path, platforms: dict) -> Path:
    """ChatGPT Custom GPT bundle (§3.3) — real A4 engine via Code Interpreter."""
    cfg = platforms["platforms"]["chatgpt"]
    out = Path(out)
    instructions, knowledge = _emit_common(adapted, out, _ENGINE_REPORT, cfg["char_limit"])
    (out / "instructions.md").write_text(instructions, encoding="utf-8")

    manifest = {
        "name": adapted.name,
        "description": adapted.description,
        "instructions_file": "instructions.md",
        "knowledge_files": knowledge,
        "code_interpreter": True,
        "conversation_starters": _conversation_starters(adapted.intake_questions),
    }
    (out / "manifest.json").write_text(_serialize(manifest), encoding="utf-8")

    # INSTALL.md — per D-09, NAME the canonical shared assets to upload; never
    # physically duplicate the heavy A4 engine / A7 package into the committed bundle.
    a7_line = (
        "5. Upload the A7 deterministic engines from `scripts/hse_components/` "
        "(`risk_matrix.py`, `controls.py`, `rca.py`, `smart_actions.py`, "
        "`incident_rates.py`, `__init__.py`, `_shim.py`).\n"
        if adapted.has_a7
        else ""
    )
    install = (
        f"# Install `{adapted.name}` as a ChatGPT Custom GPT\n\n"
        "1. Create a new Custom GPT (Configure tab).\n"
        "2. Paste `instructions.md` into the **Instructions** field.\n"
        "3. Upload every file under `knowledge/` as **Knowledge**.\n"
        "4. Enable **Code Interpreter & Data Analysis**, then upload the canonical "
        "report engine from `assets/report-engine/` (`generate_report.py`, "
        "`render_docx.py`, `render_pdf.py`, `theme.py`, the schemas, `brand.yaml`, "
        "`house-standard.yaml`, and the `fonts/` directory).\n"
        f"{a7_line}"
        "6. The GPT runs `generate_report.py` in Code Interpreter to produce the "
        "branded DOCX + PDF.\n\n"
        "_Heavy Code-Interpreter assets are shared from the repo's single canonical "
        "copy (D-09) — they are named here, not duplicated into this bundle._\n"
    )
    (out / "INSTALL.md").write_text(install, encoding="utf-8")
    return out


def emit_gemini(adapted: AdaptedSkill, out: Path, platforms: dict) -> Path:
    """Gemini Gem bundle (§3.4) — char-fit, markdown-report degradation, NO assets/."""
    cfg = platforms["platforms"]["gemini"]
    out = Path(out)
    instructions, knowledge = _emit_common(
        adapted, out, _markdown_report_instruction(), cfg["char_limit"]
    )
    (out / "instructions.md").write_text(instructions, encoding="utf-8")
    manifest = {
        "name": adapted.name,
        "description": adapted.description,
        "instructions_file": "instructions.md",
        "knowledge_files": knowledge,
        "code_interpreter": False,
    }
    (out / "manifest.json").write_text(_serialize(manifest), encoding="utf-8")
    install = (
        f"# Install `{adapted.name}` as a Gemini Gem\n\n"
        "1. Create a new Gem.\n"
        "2. Paste `instructions.md` into the Gem's instructions.\n"
        "3. Attach every file under `knowledge/` as knowledge.\n"
        "4. The Gem emits a structured markdown report (no Code Interpreter on this host).\n"
    )
    (out / "INSTALL.md").write_text(install, encoding="utf-8")
    return out


def emit_copilot_manifest(adapted: AdaptedSkill, instructions: str,
                          knowledge: List[str], cfg: dict) -> dict:
    """The declarative-agent manifest (§3.5, schema 1.7) — isolated so a vendor
    schema change touches ONE function. String props are capped at
    manifest_string_limit (instructions stay in the instruction field; the manifest
    carries a pointer, never the full body)."""
    limit = cfg.get("manifest_string_limit", 4000)
    return {
        "schema": cfg.get("manifest_schema", "1.7"),
        "name": adapted.name,
        "description": adapted.description[:limit],
        "instructions": "See instructions.md (the full instruction field).",
        "capabilities": [],
        "knowledge_sources": knowledge,
    }


def emit_copilot(adapted: AdaptedSkill, out: Path, platforms: dict) -> Path:
    """Microsoft Copilot declarative-agent bundle (§3.5) — same markdown degradation
    as Gemini; the four non-negotiables stay IN instructions (anti-XPIA), NO assets/."""
    cfg = platforms["platforms"]["copilot"]
    out = Path(out)
    instructions, knowledge = _emit_common(
        adapted, out, _markdown_report_instruction(), cfg["char_limit"]
    )
    (out / "instructions.md").write_text(instructions, encoding="utf-8")
    manifest = emit_copilot_manifest(adapted, instructions, knowledge, cfg)
    (out / "manifest.json").write_text(_serialize(manifest), encoding="utf-8")
    install = (
        f"# Install `{adapted.name}` as a Microsoft Copilot declarative agent\n\n"
        "1. Register a new declarative agent (Copilot Studio / agent manifest).\n"
        "2. Use `manifest.json` (declarative-agent schema 1.7) as the agent manifest.\n"
        "3. Paste `instructions.md` into the agent's instruction field.\n"
        "4. Attach every file under `knowledge/` as a knowledge source.\n"
        "5. The agent emits a structured markdown report (no Python execution on this host).\n"
    )
    (out / "INSTALL.md").write_text(install, encoding="utf-8")
    return out


def emit_generic(adapted: AdaptedSkill, out: Path, platforms: dict) -> Path:
    """Generic system-prompt bundle (§3.6) — the portability backstop; char-fit to
    the conservative default, markdown degradation, NO assets/."""
    cfg = platforms["platforms"]["generic"]
    out = Path(out)
    instructions, knowledge = _emit_common(
        adapted, out, _markdown_report_instruction(), cfg["char_limit"]
    )
    (out / "system-prompt.md").write_text(instructions, encoding="utf-8")
    manifest = {
        "name": adapted.name,
        "description": adapted.description,
        "system_prompt_file": "system-prompt.md",
        "knowledge_files": knowledge,
        "notes": "Markdown-report degradation; run the intake conversationally.",
    }
    (out / "manifest.json").write_text(_serialize(manifest), encoding="utf-8")
    install = (
        f"# Install `{adapted.name}` on any system-prompt host\n\n"
        "1. Paste `system-prompt.md` as the system prompt.\n"
        "2. Attach the files under `knowledge/` if the host supports file uploads; "
        "otherwise the system prompt's pointers explain that the detail lives there.\n"
        "3. Run the structured intake conversationally; the host emits a markdown report.\n"
    )
    (out / "INSTALL.md").write_text(install, encoding="utf-8")
    return out


_EMITTERS = {
    "chatgpt": emit_chatgpt,
    "gemini": emit_gemini,
    "copilot": emit_copilot,
    "generic": emit_generic,
}

# The required files each platform bundle must carry (the structural self-check).
_REQUIRED_FILES = {
    "chatgpt": ["instructions.md", "manifest.json", "INSTALL.md"],
    "gemini": ["instructions.md", "manifest.json", "INSTALL.md"],
    "copilot": ["instructions.md", "manifest.json", "INSTALL.md"],
    "generic": ["system-prompt.md", "manifest.json", "INSTALL.md"],
}
_INSTRUCTION_FILE = {
    "chatgpt": "instructions.md",
    "gemini": "instructions.md",
    "copilot": "instructions.md",
    "generic": "system-prompt.md",
}


def emit(adapted: AdaptedSkill, platform: str, out: Path, platforms: dict) -> Path:
    """Emit one (skill × platform) bundle."""
    return _EMITTERS[platform](adapted, out, platforms)


def _self_check(bundle_dir: Path, platform: str, platforms: dict) -> List[str]:
    """A structural self-check: required files written + char limit respected + no
    residual marker in the instruction surface (the full validator lands in 07-02).
    Returns a list of problems ([] = clean)."""
    problems: List[str] = []
    for rel in _REQUIRED_FILES[platform]:
        if not (bundle_dir / rel).is_file():
            problems.append(f"{platform}/{bundle_dir.name}: missing {rel}")
    instr_path = bundle_dir / _INSTRUCTION_FILE[platform]
    if instr_path.is_file():
        text = instr_path.read_text(encoding="utf-8")
        limit = platforms["platforms"][platform]["char_limit"]
        if len(text) > limit:
            problems.append(
                f"{platform}/{bundle_dir.name}: instruction field {len(text)} chars "
                f"exceeds char_limit {limit}"
            )
        if _RESIDUAL_MARKER_RE.search(text):
            problems.append(
                f"{platform}/{bundle_dir.name}: residual hse:block marker in instructions"
            )
    return problems


def _iter_skill_names(repo: Path) -> List[str]:
    root = repo / "skills"
    return sorted(p.parent.name for p in root.rglob("SKILL.md"))


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Render skills into Tier-B bundles (C §3.1).")
    p.add_argument("--skill", action="append", help="skill name(s); omit with --all")
    p.add_argument("--all", action="store_true", help="render every skill in skills/")
    p.add_argument(
        "--platform", default="all",
        choices=["chatgpt", "gemini", "copilot", "generic", "all"],
    )
    p.add_argument("--out", default=str(ADAPTERS_DIR), help="output root (default: adapters/)")
    p.add_argument(
        "--check", action="store_true",
        help="emit to a temp dir + self-validate WITHOUT writing the committed tree (CI mode)",
    )
    p.add_argument("--repo", default=str(REPO), help="repo root (default: inferred)")
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()

    if args.all:
        skills = _iter_skill_names(repo)
    elif args.skill:
        skills = list(args.skill)
    else:
        p.error("no skills given (pass --skill NAME ... or --all)")

    platforms_cfg = load_platforms()
    targets = PLATFORMS if args.platform == "all" else [args.platform]

    # --check emits to a throwaway temp dir; the real run writes the committed tree.
    if args.check:
        out_root = Path(tempfile.mkdtemp(prefix="hse-adapters-check-"))
    else:
        out_root = Path(args.out).resolve()

    problems: List[str] = []
    try:
        for skill in skills:
            skill_dir = repo / "skills" / skill
            if not (skill_dir / "SKILL.md").is_file():
                problems.append(f"{skill}: no skills/{skill}/SKILL.md")
                continue
            try:
                adapted = load_skill(skill_dir)
            except (ValueError, IrreducibleOverflow) as e:
                problems.append(f"{skill}: load failed — {e}")
                continue
            for platform in targets:
                bundle_dir = out_root / platform / skill
                try:
                    emit(adapted, platform, bundle_dir, platforms_cfg)
                except IrreducibleOverflow as e:
                    problems.append(f"{platform}/{skill}: {e}")
                    continue
                problems.extend(_self_check(bundle_dir, platform, platforms_cfg))
    finally:
        if args.check:
            shutil.rmtree(out_root, ignore_errors=True)

    if problems:
        for prob in problems:
            print(f"FAIL {prob}", file=sys.stderr)
        # build.py REFUSES to exit 0 unless every emitted bundle passes (§3.1 step 4).
        return 1
    print(f"OK: {len(skills)} skill(s) × {len(targets)} platform(s) emitted clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
