#!/usr/bin/env python3
"""scaffold.py — the A10 forge's born-conformant skill scaffolder (FORGE-01/02).

Build-time CLI. Given a skill name + an answers.json (the author-interview facts,
A10 §3.4), it emits a complete `skills/<name>/` that `lint_skills.py` passes with
ZERO hand-edits, and it refuses to exit 0 unless its own output lints clean
(A10 AC#1 / D1). It reads the SAME authorities the linter reads —
`template/SKILL.md`, `template/blocks/*.md`, `template/metadata-vocab.yaml`,
`template/evals/rubric.yaml`, and `knowledge-base/**/_registry.yaml` — and copies
the five inline blocks BYTE-FOR-BYTE from `template/blocks/*` (it embeds no block
text of its own, so there is never a second source of truth; rule-1 anti-drift is
born-satisfied — A10 D1 / T-04-02).

Two intakes are NEVER conflated (A10 D4): the *runtime* §2.7 intake STEP this seeds
is a `<!-- TODO -->` scaffold from `templates/intake-todo.md` — the forge never
invents the skill's domain question VALUES; that is the author's job, categorically
distinct from the forge's own author-interview.

Roster pre-seed (A10 §7 RESOLVED, couples SC-1<->SC-5): when answers declare
`roster: flagship-b5` the FULL examined B5 four-agent roster is pre-seeded
verbatim; `roster: single-thread` seeds the one-liner; otherwise a moderate
Researcher+Drafter+Critic/QA starter.

Conditional A7 wiring (A10 D6): the `scripts/` symlink (-> repo
`scripts/hse_components/`) + a verbatim `_shim.py` are created ONLY when the answers
declare A7 components; a skill with none (e.g. B3 toolbox-talk) gets no `scripts/`.

CLI:
    scaffold.py --name <skill-name> --answers <answers.json>
                [--from-skill-creator <draft.md>] [--standalone]
                [--out-root <skills-dir>] [--force]

stdlib + pyyaml only (§2.5).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import List, Optional

import yaml

# --- repo + template authorities (the SAME files lint_skills reads) -------------
# scaffold.py lives at skills/hse-skill-forge/scripts/scaffold.py -> repo root is 3 up.
REPO = Path(__file__).resolve().parents[3]
TEMPLATE = REPO / "template"
BLOCKS_DIR = TEMPLATE / "blocks"
VOCAB_FILE = TEMPLATE / "metadata-vocab.yaml"
RUBRIC_FILE = TEMPLATE / "evals" / "rubric.yaml"
KB = REPO / "knowledge-base"
FORGE_DIR = Path(__file__).resolve().parent.parent          # skills/hse-skill-forge
FORGE_TEMPLATES = FORGE_DIR / "templates"

# The five inline blocks copied byte-for-byte from template/blocks/* (rule-1 sources).
INLINE_BLOCKS = ["deid", "kb-selection", "orchestration", "report-output", "attribution"]

NAME_RE = re.compile(r"^[a-z0-9-]+$")
MAX_NAME = 64

REQUIRED_META_KEYS = [
    "author", "version", "category", "tier", "audience",
    "industry", "jurisdiction", "status", "plugin",
]

# The §3.8 B5 flagship roster (examined + gate-approved; pre-seeded verbatim).
B5_ROSTER = """\
### Subagent roster for THIS skill
- **De-identifier** — runs FIRST (sequential dependency); scrub all PII/health detail —
  injured-party, witnesses, diagnoses, exact dates/locations, small injury cells — into role
  labels before any analysis. Returns the re-identification key SEPARATELY (to the orchestrator,
  not to any sibling). Everything below consumes only its scrubbed output.
- **A · Evidence & Timeline Reconstructor** — assemble the numbered, time-ordered event
  sequence and the numbered evidence log (E-1…) from the scrubbed inputs; flag [GAP].
  SCOPE-OUT: does not assign causes (B owns it) or decide reportability (C owns it).
- **B · Root-Cause Analyst** — apply the chosen method (5-Whys / ICAM / SCAT / Fishbone /
  Swiss-Cheese) via rca.py; every causal claim cites an evidence item (E-n); reach a
  systemic/organisational factor (rca.validate `reaches_systemic` true for whichever method).
  SCOPE-OUT: reportability (C owns it) and control selection (D owns it).
- **C · Regulatory Reportability Checker** — for the resolved jurisdiction (India → resolved
  STATE first), return verdict + clause/section + deadline + form (India state accident form
  via KB-REG-IN-STATEFORMS / UK RIDDOR / US OSHA 29 CFR 1904). Conservative — flag [GAP] and
  "ask a competent person" when unsure. SCOPE-OUT: does not draft the report or invent a form number.
- **D · Corrective-Action Drafter** — hierarchy-of-controls-tagged CAPAs, each tracing to a
  named cause (RC-n) with a named owner + ISO due date + measure; prefer higher-order controls,
  justify any PPE/admin-only. SCOPE-OUT: does not score causes (B) or check law (C).
- **Critic/QA** (MANDATORY) — adversarial read-only review: every cause evidence-backed, RCA
  reaches a systemic factor, reportability cited conservatively to the matched KB row, every
  CAPA traces to a cause with owner+date, no PPE/admin-only without justification, and ZERO
  PII/health leak (no residual identifier, no <5 cell, no re-id key in the output).
"""

SINGLE_THREAD_ROSTER = """\
### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

- Single-threaded by design — no subagents. (Replace with this skill's named
  fan-out jobs if the triage gate warrants them.)
"""

MODERATE_ROSTER = """\
### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

For a non-trivial task the triage gate may fan out to:

- **Researcher** — gathers the task/site facts, the resolved jurisdiction's
  requirements, and the relevant standards, from the scrubbed inputs only.
- **Drafter** — assembles the deliverable in this skill's output format, applying
  the hierarchy of controls and tracing every finding to evidence.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety
  output: specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.

Simple single-subject tasks run single-threaded — no subagents.
"""

# Default kb-selection jurisdiction rows (>=4 pipes so rule-2 passes). The author
# refines these for the jurisdictions the skill actually serves.
DEFAULT_KB_ROWS = """\

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
"""


# --- small helpers --------------------------------------------------------------

def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _inner_block(block: str) -> str:
    """The canonical inner body of `block` copied BYTE-FOR-BYTE from
    template/blocks/<block>.md (mirrors lint_skills._inner_region: a marker-less
    source file IS the bare body). scaffold.py embeds NO block text of its own."""
    raw = _read(BLOCKS_DIR / f"{block}.md")
    m = re.search(
        rf"<!-- hse:block:{re.escape(block)}:start -->(.*?)<!-- hse:block:{re.escape(block)}:end -->",
        raw,
        re.S,
    )
    return m.group(1) if m else raw


def _wrap_block(block: str) -> str:
    """A block's full marked region as it appears in a SKILL.md.

    report-output's canonical form (per template/SKILL.md + the frozen example) puts
    the start marker on the SAME line as `## Output format`; reproduce that exactly so
    the byte-match holds. The block source ships bare (no markers) for report-output, so
    `_inner_block` returns the whole body including the leading `## Output format`."""
    inner = _inner_block(block)
    start = f"<!-- hse:block:{block}:start -->"
    end = f"<!-- hse:block:{block}:end -->"
    if block == "report-output":
        # start marker glued to the first content line; the body already begins
        # "## Output…" and ends with its own trailing newline, so the end marker sits
        # on the next line with NO extra newline inserted (matches the frozen example).
        return f"{start}{inner}{end}"
    return f"{start}{inner}{end}"


def _validate_name(name: str) -> str:
    """MCP-safe, path-traversal-safe skill name (T-04-01)."""
    if not name or not NAME_RE.match(name) or len(name) > MAX_NAME:
        raise ValueError(
            f"invalid --name {name!r}: must be lowercase [a-z0-9-], <= {MAX_NAME} chars, "
            f"no path separators or '..'"
        )
    if ".." in name or "/" in name or "\\" in name or os.path.isabs(name):
        raise ValueError(f"invalid --name {name!r}: path escape rejected")
    return name


def _load_yaml(p: Path) -> dict:
    return yaml.safe_load(_read(p)) or {}


# --- the scaffolder -------------------------------------------------------------

def _frontmatter(name: str, answers: dict) -> str:
    """Build the YAML frontmatter from the author-interview answers, vocab-validating
    every controlled key BEFORE writing so rule 6 passes."""
    vocab = _load_yaml(VOCAB_FILE)
    meta = dict(answers.get("metadata", {}))
    meta.setdefault("author", answers.get("author", "eyekyam"))
    meta.setdefault("version", "1.0")
    meta.setdefault("hse_reviewed_by", "")
    meta.setdefault("hse_reviewed_date", "")

    for key in REQUIRED_META_KEYS:
        if key not in meta:
            raise ValueError(f"answers.metadata missing required key '{key}'")
    for key in ("category", "status", "tier"):
        if meta[key] not in vocab.get(key, []):
            raise ValueError(f"answers.metadata.{key} '{meta[key]}' not in controlled vocab")
    for key in ("audience", "industry", "jurisdiction"):
        vals = meta[key] if isinstance(meta[key], list) else [meta[key]]
        for v in vals:
            if v not in vocab.get(key, []):
                raise ValueError(f"answers.metadata.{key} value '{v}' not in controlled vocab")
    if meta["plugin"] not in vocab.get("plugin", []):
        raise ValueError(f"answers.metadata.plugin '{meta['plugin']}' not a registered bundle")

    description = answers.get("description", "").strip()
    if not description:
        description = (
            f"Produce a consultant-grade {name.replace('-', ' ')} artifact for a named "
            f"task, site, or asset, forcing task specificity and the hierarchy of controls."
        )

    fm = {
        "name": name,
        "description": description,
        "license": "Apache-2.0",
        "metadata": {k: meta[k] for k in (
            "author", "version", "category", "tier", "audience", "industry",
            "jurisdiction", "status", "plugin", "hse_reviewed_by", "hse_reviewed_date",
        ) if k in meta},
    }
    body = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
    return f"---\n{body}---\n"


def _roster_for(answers: dict) -> str:
    flag = str(answers.get("roster", "single-thread")).strip().lower()
    if flag in ("flagship-b5", "flagship", "b5"):
        return B5_ROSTER
    if flag in ("moderate", "fan-out"):
        return MODERATE_ROSTER
    return SINGLE_THREAD_ROSTER


def _skill_md(name: str, answers: dict, draft_overview: Optional[str] = None) -> str:
    """Assemble the SKILL.md: the 10-section frame with the five inline blocks copied
    byte-for-byte, the seeded runtime-intake STEP (TODO scaffold only), the roster, and
    the kb-selection rows."""
    title = name.replace("-", " ").title()
    overview = draft_overview or (
        f"A consultant-grade HSE skill that produces a specific, defensible "
        f"{name.replace('-', ' ')} for a named task, site, or asset. It forces the "
        f"single lever that separates a defensible artifact from copy-paste paperwork: "
        f"task/site specificity plus the full hierarchy of controls — never a vague, "
        f"PPE-only treatment."
    )
    intake_todo = _read(FORGE_TEMPLATES / "intake-todo.md")

    parts: List[str] = []
    parts.append(_frontmatter(name, answers))
    parts.append(f"\n# {title}\n\n{overview}\n")
    parts.append(
        "\n## When to use this skill\n\n"
        f"Use this skill when the user needs a {name.replace('-', ' ')} for a concrete "
        "task, site, or asset. List the trigger scenarios that reinforce the `description` "
        "so the host routes here rather than to a generic answer. If the request is vague, "
        "the Workflow intake below forces the specifics before any drafting.\n"
    )
    # deid block (byte-for-byte) ----------------------------------------------------
    parts.append("\n" + _wrap_block("deid") + "\n")
    # kb-selection block + per-skill rows below :end --------------------------------
    parts.append("\n" + _wrap_block("kb-selection") + "\n")
    parts.append(DEFAULT_KB_ROWS)
    # Workflow — seed the runtime intake STEP ONLY (TODO scaffold; never invent values)
    parts.append(
        "\n## Workflow\n\n"
        "Open with a **structured multi-step intake** — MCQ where the answer space is "
        "enumerable, free-text where it is open. Ask ONE question at a time, branch on the "
        "answers, and echo the captured facts back before any analysis. Never proceed on "
        "vague or missing inputs; this intake is the operational core of *forcing "
        "specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)\n\n"
        f"{intake_todo}\n"
        "Then: analyse / apply the domain method → validate the draft against "
        "`references/QUALITY_CHECKLIST.md` → produce the output via the Output format section "
        "below. This is the skill-authored section; author the domain method in "
        "`references/METHODOLOGY.md`.\n"
    )
    # orchestration block (byte-for-byte) + roster below :end -----------------------
    parts.append("\n" + _wrap_block("orchestration") + "\n")
    parts.append("\n" + _roster_for(answers).rstrip("\n") + "\n")
    # report-output block (byte-for-byte, one-line start marker) ---------------------
    parts.append("\n" + _wrap_block("report-output") + "\n")
    # attribution block (byte-for-byte) ---------------------------------------------
    parts.append("\n" + _wrap_block("attribution") + "\n")
    # reference pointers ------------------------------------------------------------
    parts.append(
        "\n## Reference material\n\n"
        "On-demand pointers (read only when needed):\n\n"
        "- `references/METHODOLOGY.md` — the domain method this skill applies.\n"
        "- `references/deid-checklist.md` — the full de-identification checklist (A5).\n"
        "- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.\n"
        "- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.\n"
    )
    return "".join(parts)


def _skill_kb_manifest(name: str, answers: dict) -> str:
    """The rule-9 reference manifest. Lists the answers' named KB ids so every id
    resolves against its folder's _registry.yaml. Defaults to the always-grounded
    ISO 45001 + HOC + INTAKE snippets when answers name none."""
    kb_ids = answers.get("kb_ids") or ["KB-STD-ISO45001", "KB-SNIP-HOC", "KB-SNIP-INTAKE"]
    id_path = {
        "KB-STD-ISO45001": "../../../knowledge-base/standards/iso-45001.md",
        "KB-STD-ISO14001": "../../../knowledge-base/standards/iso-14001.md",
        "KB-STD-ISO45003": "../../../knowledge-base/standards/iso-45003.md",
        "KB-SNIP-HOC": "../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md",
        "KB-SNIP-INTAKE": "../../../knowledge-base/prompt-snippets/intake-interview.md",
        "KB-SNIP-ARCHETYPES": "../../../knowledge-base/prompt-snippets/subagent-archetypes.md",
        "KB-REG-IN-FACTORIES": "../../../knowledge-base/regulatory/in-factories-act.md",
        "KB-REG-IN-STATEFORMS": "../../../knowledge-base/regulatory/in-state-forms.md",
    }
    rows = []
    for kb in kb_ids:
        path = id_path.get(kb, "")
        rows.append(f"| {kb} | (author the use) | {path} |")
    rows_md = "\n".join(rows)
    return (
        f"# Knowledge-base manifest for `{name}`\n\n"
        "The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). "
        "The A8 linter cross-checks every ID against the named folder's `_registry.yaml` "
        "and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list "
        "in step with the `kb-selection` rows.\n\n"
        "| ID | Use | Path |\n|---|---|---|\n"
        f"{rows_md}\n"
    )


def _evals_json(name: str) -> str:
    """A >=3-case evals.json in the canonical skill-creator schema (Plan 03-04). Case
    stubs the author fills; the third case is the de_identification hard-fail probe."""
    obj = {
        "_comment": f"Eval set for {name} (forge-seeded skeleton; author fills the domain expectations).",
        "skill": name,
        "rubric": "rubric.yaml",
        "evals": [
            {
                "query": "TODO — a vague request that should trigger the structured intake.",
                "files": [],
                "expected_behavior": "Runs the structured intake and refuses to draft until the specific task/site/asset and the domain specifics are captured.",
                "expectations": [
                    "Runs the structured intake (one question at a time) before any drafting.",
                    "Refuses to proceed on the vague request — elicits the specific task/site/asset.",
                    "Does not emit a generic or template-only artifact (specificity dimension).",
                ],
            },
            {
                "query": "TODO — a request whose only stated control is PPE.",
                "files": [],
                "expected_behavior": "Walks the full hierarchy of controls and flags any PPE-only treatment as inadequate, proposing higher-order controls first.",
                "expectations": [
                    "Walks the full hierarchy of controls: eliminate -> substitute -> engineer -> administrate -> PPE.",
                    "Flags the PPE-only treatment as inadequate; proposes higher-order controls first.",
                    "Assigns a named owner and a target/review date to each control action (defensibility).",
                ],
            },
            {
                "query": "TODO — a request carrying a real name, DOB, and a health condition.",
                "files": [],
                "expected_behavior": "The de-identification block runs first; the name, DOB, and health detail are pseudonymised/aggregated; any verbatim leak is a de_identification hard-fail.",
                "expectations": [
                    "The de-identification block runs FIRST — identifiers are detected and listed up front.",
                    "The real name is replaced with a stable role label; DOB and health detail are pseudonymised/aggregated, never verbatim.",
                    "No real name, DOB, or health detail in the circulated output, and no re-identification key embedded (de_identification hard-fail).",
                ],
            },
        ],
    }
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def _create_scripts_symlink(skill_dir: Path) -> None:
    """A7 wiring (A10 D6): a relative symlink scripts/ -> repo scripts/hse_components/
    + a verbatim _shim.py. Real-copy fallback on symlink-stripping hosts."""
    scripts_dir = skill_dir / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    # verbatim _shim.py (byte copy from the package, the SAME mechanism).
    shutil.copyfile(REPO / "scripts" / "hse_components" / "_shim.py", scripts_dir / "_shim.py")
    link = scripts_dir / "hse_components"
    target_rel = Path("..") / ".." / ".." / "scripts" / "hse_components"
    try:
        if link.exists() or link.is_symlink():
            return
        os.symlink(target_rel, link)
    except (OSError, NotImplementedError):
        # symlink-stripping host: real-copy fallback.
        shutil.copytree(REPO / "scripts" / "hse_components", link)


def scaffold_skill(
    name: str,
    answers: dict,
    out_root: Optional[Path] = None,
    from_skill_creator: Optional[Path] = None,
    standalone: bool = False,
    force: bool = False,
) -> Path:
    """Emit a born-conformant skills/<name>/ and return its path. Self-validates at the
    end and raises if its own output does not lint clean (A10 AC#1)."""
    name = _validate_name(name)
    out_root = Path(out_root) if out_root else (REPO / "skills")
    out_root = out_root.resolve()
    skill_dir = (out_root / name).resolve()
    # Path-traversal guard (T-04-01): the resolved dir must stay under out_root.
    if out_root not in skill_dir.parents and skill_dir != out_root / name:
        raise ValueError(f"refusing to write outside {out_root}: {skill_dir}")
    if skill_dir.exists():
        if not force:
            raise FileExistsError(f"{skill_dir} already exists (pass force=True to overwrite)")
        shutil.rmtree(skill_dir)

    draft_overview = None
    if from_skill_creator and Path(from_skill_creator).is_file():
        # skill-creator wrap: use its draft as the overview prose (domain body). The
        # contract scaffold (blocks/intake/roster/folders) is still forge-owned.
        draft_overview = _read(Path(from_skill_creator)).strip() or None

    skill_dir.mkdir(parents=True)

    # SKILL.md ----------------------------------------------------------------------
    (skill_dir / "SKILL.md").write_text(_skill_md(name, answers, draft_overview), encoding="utf-8")

    # references/ -------------------------------------------------------------------
    refs = skill_dir / "references"
    refs.mkdir()
    for fname in ("METHODOLOGY.md", "QUALITY_CHECKLIST.md", "deid-checklist.md"):
        shutil.copyfile(FORGE_TEMPLATES / "references" / fname, refs / fname)
    (refs / "_skill-kb.md").write_text(_skill_kb_manifest(name, answers), encoding="utf-8")

    # assets/ (+ a stub report.json) ------------------------------------------------
    assets = skill_dir / "assets"
    assets.mkdir()
    (assets / "report.json").write_text(
        json.dumps(
            {"_comment": f"Stub report.json for {name}; author the typed-block tree (A4).",
             "title": f"{name.replace('-', ' ').title()} Report", "sections": []},
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    # evals/ ------------------------------------------------------------------------
    evals = skill_dir / "evals"
    (evals / "files").mkdir(parents=True)
    (evals / "evals.json").write_text(_evals_json(name), encoding="utf-8")
    shutil.copyfile(RUBRIC_FILE, evals / "rubric.yaml")
    # run_evals.py — the thin per-skill shim (verbatim from the example). skills/<n>/
    # is two levels up; the example computes REPO as SKILL_DIR.parent.parent which for
    # skills/<n>/ resolves to the repo root (skills/<n>/ -> repo). Matches the example.
    shutil.copyfile(REPO / "examples" / "risk-assessment" / "evals" / "run_evals.py",
                    evals / "run_evals.py")
    # de-id fixture PAIR (clean + seeded-leak) modelled on examples/deid-canary -------
    shutil.copyfile(REPO / "examples" / "deid-canary" / "clean.md", evals / "files" / "deid-clean.md")
    shutil.copyfile(REPO / "examples" / "deid-canary" / "leak.md", evals / "files" / "deid-leak.md")

    # branding/ ---------------------------------------------------------------------
    branding = skill_dir / "branding"
    branding.mkdir()
    card_target_rel = Path("..") / ".." / ".." / "branding" / "company-card.yaml"
    card_link = branding / "company-card.yaml"
    try:
        os.symlink(card_target_rel, card_link)
    except (OSError, NotImplementedError):
        shutil.copyfile(REPO / "branding" / "company-card.yaml", card_link)

    # scripts/ — ONLY when A7 components declared (B1/B5 yes; B3 no) -----------------
    if answers.get("a7_components") or answers.get("components"):
        _create_scripts_symlink(skill_dir)

    # Self-validate: refuse to "succeed" unless the output lints clean (A10 AC#1) ----
    report = _self_lint(skill_dir)
    if report.errors:
        msg = "\n".join(f"  - {e}" for e in report.errors)
        raise RuntimeError(
            f"scaffold output for {name} does NOT lint clean (refusing exit 0):\n{msg}"
        )
    return skill_dir


def _self_lint(skill_dir: Path):
    """Run the SAME linter CI runs against the freshly scaffolded skill (A10 D1/AC#1)."""
    forge_scripts = str(Path(__file__).resolve().parent)
    if forge_scripts not in sys.path:
        sys.path.insert(0, forge_scripts)
    import validate_repo_skill  # re-export of lint_skills; never a fork
    return validate_repo_skill.validate_skill(skill_dir)


# --- CLI ------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Born-conformant HSE skill scaffolder (A10 forge).")
    parser.add_argument("--name", required=True, help="skill name (lowercase [a-z0-9-], <=64)")
    parser.add_argument("--answers", required=True, help="path to the author-interview answers.json")
    parser.add_argument("--from-skill-creator", default=None, help="optional skill-creator draft.md")
    parser.add_argument("--standalone", action="store_true", help="standalone fallback (no skill-creator)")
    parser.add_argument("--out-root", default=None, help="skills/ root to write under (default: repo skills/)")
    parser.add_argument("--force", action="store_true", help="overwrite an existing skill dir")
    args = parser.parse_args(argv)

    answers = json.loads(Path(args.answers).read_text(encoding="utf-8"))
    try:
        skill_dir = scaffold_skill(
            args.name, answers,
            out_root=args.out_root,
            from_skill_creator=args.from_skill_creator,
            standalone=args.standalone,
            force=args.force,
        )
    except (ValueError, FileExistsError, RuntimeError) as exc:
        print(f"ERROR  scaffold failed: {exc}", file=sys.stderr)
        return 1
    print(f"OK     scaffolded born-conformant skill at {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
