"""lint_skills.py — the A8 quality-harness linter (A2 §5 / A8 §4.1, QA-01).

ONE importable module, stdlib + pyyaml only (§2.5). It is the deterministic
merge-gate floor: no model calls. Critically it is the SAME module the forge's
`validate_repo_skill.py` imports in Phase 4 (A8 Decision 8 / A2 §2.2) — A10 must
import `validate_skill` from here rather than fork the rule logic, so a skill can
never pass the forge but fail CI (threat T-03-11).

Public API
----------
    validate_skill(path: Path) -> Report
        Run the 10 A2 rules against one skill folder; returns a Report with
        `errors` (hard, block merge) and `warnings` (surfaced, non-blocking).
    main(argv=None) -> int
        CLI: `python lint_skills.py <skill>... | --all` ; flags `--all`,
        `--standard-only`. Returns 0 on a clean lint, 1 on any hard error.
    resolve_kb_id(kb_id, repo) -> bool
        Rule-9 helper: True iff the KB id exists in its folder's _registry.yaml.

The 10 A2 §5 rules (hard/warn split per A8 §4.1):
    1. Block markers — the 5 inline hse:block:* regions byte-identical to
       template/blocks/<block>.md (canonical core above :end). HARD.
    2. Orchestration roster + kb-selection rows — present + non-empty below the
       respective :end markers (presence-only, never diffed). HARD.
    3. Folder layout — references/, assets/, evals/{evals.json,rubric.yaml,
       run_evals.py,files/}, branding/company-card.yaml present. HARD.
    4. name — equals folder name, lowercase [a-z0-9-], <=64 chars. HARD.
    5. description — <=1024 chars (HARD); third-person pronoun heuristic (WARN).
    6. metadata — required keys present; values in the A2 §4.1 controlled vocab;
       plugin resolves to a registered marketplace bundle. HARD.
    7. body length — warn approaching ~400 lines; HARD-fail >500. (license also
       checked HARD == Apache-2.0.)
    8. Dead reference links — every references/... path cited in the body
       resolves on disk. HARD.
    9. KB resolution — every ../../knowledge-base/... path resolves on disk;
       every KB-... id resolves in its folder's _registry.yaml; staleness WARN
       when a referenced volatile:true fragment's last_reviewed predates
       STALENESS_DAYS; source/year WARN for an empty-source data-point. HARD on
       an unresolvable path/id; WARN on staleness/source.
   10. No time-sensitive phrasing — absolute dates / "as of" / "currently" in the
       body -> WARN (push the volatile fact into the KB).
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import List, Optional

import yaml

# --- single config constant (A3 §3.10 / Phase-2 D-05) --------------------------
STALENESS_DAYS = 180

# scripts/ -> repo root
REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "template"
BLOCKS_DIR = TEMPLATE / "blocks"
VOCAB_FILE = TEMPLATE / "metadata-vocab.yaml"
KB = REPO / "knowledge-base"

# The five inline blocks (rule 1 anti-drift sources).
INLINE_BLOCKS = ["deid", "kb-selection", "orchestration", "report-output", "attribution"]

# Blocks whose per-skill rows live BELOW :end and so are diffed only up to :end
# (kb-selection rows + orchestration roster are rule-2's concern, A8 §4.1 rule 1).
CANONICAL_CORE_ONLY = {"kb-selection", "orchestration"}

# Folder + ID-prefix maps (rule 9; promoted from knowledge-base/tests/test_kb_resolution.py).
PREFIX_FOLDER = {
    "REG": "regulatory",
    "STD": "standards",
    "SNIP": "prompt-snippets",
    "DATA": "data-points",
    "RES": "research",
}

# Required metadata keys (A2 §4 schema).
REQUIRED_META_KEYS = [
    "author", "version", "category", "tier", "audience",
    "industry", "jurisdiction", "status", "plugin",
]
# Single-valued vs list-valued facets validated against the controlled vocab.
SCALAR_VOCAB_KEYS = ["category", "status", "tier"]
LIST_VOCAB_KEYS = ["audience", "industry", "jurisdiction"]

# Marketplace bundles a `plugin` may name (A2 §4.2). SINGLE SOURCE OF TRUTH:
# template/metadata-vocab.yaml's `plugin:` list, the same file every other
# controlled vocab is read from. The old hand-maintained literal here included
# hse-operations / hse-systems, which are NOT in the architecture's bundle set
# (hse-core + 5 sector packs) and are never produced by
# gen_marketplace.build_manifest — a second source of truth that could let a skill
# name a phantom bundle, pass the linter, yet never appear as a plugin (WR-05).
# Derived lazily via registered_bundles() so it always tracks the vocab file.

# Regexes.
# KB id: KB-<PREFIX>-<suffix...>. The PREFIX (folder selector) stays upper/digit;
# suffix tokens may carry mixed case (e.g. KB-STD-ISO45001-AnnexA) and there may be
# several hyphen-joined tokens. The old `KB-[A-Z0-9]+-[A-Z0-9-]+` excluded
# lowercase, so it truncated `KB-STD-ISO45001-AnnexA` to `KB-STD-ISO45001-A` and
# the citation grader then resolved the WRONG id (WR-02). We anchor on a word
# boundary at both ends and allow alnum suffix tokens of either case so the WHOLE
# id is captured; resolve_kb_id treats any non-registry id as unresolved so a
# malformed id cannot silently alias onto a shorter registered one.
ID_RE = re.compile(r"\bKB-[A-Z0-9]+(?:-[A-Za-z0-9]+)+\b")
REF_PATH_RE = re.compile(r"references/[A-Za-z0-9_./-]+\.md")
KB_PATH_RE = re.compile(r"(\.\./)+knowledge-base/[A-Za-z0-9_./-]+\.md")
FIRST_PERSON_RE = re.compile(r"\b(I|we|my|our|us|me)\b", re.IGNORECASE)
TIME_SENSITIVE_RE = re.compile(
    r"\bas of\b|\bcurrently\b|\bat present\b|\b20\d{2}-\d{2}-\d{2}\b", re.IGNORECASE
)

MAX_BODY_LINES_WARN = 400
MAX_BODY_LINES_HARD = 500
MAX_DESCRIPTION = 1024
MAX_NAME = 64
NAME_RE = re.compile(r"^[a-z0-9-]+$")


@dataclass
class Report:
    """The structured lint result — the shared-with-forge return shape."""

    skill: str
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


# --- helpers -------------------------------------------------------------------

def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _normalize(text: str) -> str:
    """Anti-drift normalisation: trailing whitespace + line-endings only (A8 §4.1)."""
    return "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n"))


def _region(text: str, block: str) -> Optional[str]:
    """The full hse:block:<block> marked region (start..end inclusive), or None."""
    m = re.search(
        rf"<!-- hse:block:{re.escape(block)}:start -->.*?<!-- hse:block:{re.escape(block)}:end -->",
        text,
        re.S,
    )
    return m.group(0) if m else None


def _inner_region(text: str, block: str) -> Optional[str]:
    """The block content STRICTLY BETWEEN the markers (marker-agnostic).

    Anti-drift compares the block body, not the marker comment lines, so a block
    source file that ships bare (no markers) and one that ships marked compare
    equal as long as the prose is byte-identical (after trailing-ws normalisation).
    If `text` carries no markers it is treated as the bare body itself.
    """
    m = re.search(
        rf"<!-- hse:block:{re.escape(block)}:start -->(.*?)<!-- hse:block:{re.escape(block)}:end -->",
        text,
        re.S,
    )
    return m.group(1) if m else (text if "hse:block:" not in text else None)


def _split_frontmatter(text: str) -> tuple:
    """Return (frontmatter_dict, body_text). Empty dict if no/invalid frontmatter."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, m.group(2)


def _load_vocab() -> dict:
    return yaml.safe_load(_read(VOCAB_FILE))


def registered_bundles(vocab: Optional[dict] = None) -> set:
    """The registered marketplace bundle set (rule-6 `metadata.plugin` check),
    derived from template/metadata-vocab.yaml's `plugin:` list — the SINGLE source
    of truth, so the linter never drifts from gen_marketplace / the architecture
    (WR-05)."""
    if vocab is None:
        vocab = _load_vocab()
    return set(vocab.get("plugin", []))


def _registry_ids(folder: str, repo: Path) -> set:
    reg = repo / "knowledge-base" / folder / "_registry.yaml"
    if not reg.is_file():
        return set()
    return {e["id"] for e in (yaml.safe_load(_read(reg)) or [])}


def _registry_entry(folder: str, kb_id: str, repo: Path) -> Optional[dict]:
    reg = repo / "knowledge-base" / folder / "_registry.yaml"
    if not reg.is_file():
        return None
    for e in (yaml.safe_load(_read(reg)) or []):
        if e.get("id") == kb_id:
            return e
    return None


def resolve_kb_id(kb_id: str, repo: Path = REPO) -> bool:
    """Rule-9 ID resolver: True iff `kb_id` exists in its folder's _registry.yaml."""
    parts = kb_id.split("-")
    if len(parts) < 3:
        return False
    folder = PREFIX_FOLDER.get(parts[1])
    if not folder:
        return False
    return kb_id in _registry_ids(folder, repo)


# --- the rules -----------------------------------------------------------------

def _rule1_blocks(report: Report, body: str, repo: Path) -> None:
    """Each inline block's content (between markers) is byte-identical to its
    canonical template/blocks/<block>.md source (after trailing-ws normalisation).

    For kb-selection + orchestration the diffed region is the canonical CORE
    (start..end); the per-skill rows/roster below :end are rule 2's concern and
    are never captured here (they sit outside the marked region)."""
    blocks_dir = repo / "template" / "blocks"
    for block in INLINE_BLOCKS:
        inner = _inner_region(body, block)
        if inner is None:
            report.error(f"rule 1: missing hse:block:{block} marked region")
            continue
        canonical_path = blocks_dir / f"{block}.md"
        if not canonical_path.is_file():
            report.error(f"rule 1: canonical template/blocks/{block}.md not found")
            continue
        canonical_inner = _inner_region(_read(canonical_path), block)
        if canonical_inner is None:
            report.error(f"rule 1: canonical template/blocks/{block}.md has no usable region")
            continue
        if _normalize(inner) != _normalize(canonical_inner):
            report.error(
                f"rule 1: hse:block:{block} region drifted from "
                f"template/blocks/{block}.md (run hse-skill-forge --sync)"
            )


def _below_end(body: str, block: str) -> str:
    marker = f"<!-- hse:block:{block}:end -->"
    if marker not in body:
        return ""
    after = body.split(marker, 1)[1]
    nxt = re.search(r"<!-- hse:block:", after)
    return after[: nxt.start()] if nxt else after


def _rule2_rosters(report: Report, body: str) -> None:
    # Orchestration roster (below orchestration:end).
    roster = _below_end(body, "orchestration")
    if "roster" not in roster.lower() or len(roster.strip()) < 20:
        report.error("rule 2: orchestration roster subsection missing/empty below :end")
    # kb-selection jurisdiction rows (below kb-selection:end).
    rows = _below_end(body, "kb-selection")
    if rows.count("|") < 4:
        report.error("rule 2: kb-selection rows subsection missing/empty below :end")


def _rule3_layout(report: Report, skill_dir: Path) -> None:
    required = [
        "references", "assets",
        "evals/evals.json", "evals/rubric.yaml", "evals/run_evals.py", "evals/files",
        "branding/company-card.yaml",
    ]
    for rel in required:
        if not (skill_dir / rel).exists():
            report.error(f"rule 3: missing required path {rel}/")


def _rule4_name(report: Report, fm: dict, skill_dir: Path) -> None:
    name = fm.get("name", "")
    if name != skill_dir.name:
        report.error(f"rule 4: name '{name}' must equal folder name '{skill_dir.name}'")
    if not name or not NAME_RE.match(str(name)):
        report.error(f"rule 4: name '{name}' must be lowercase [a-z0-9-]")
    if len(str(name)) > MAX_NAME:
        report.error(f"rule 4: name exceeds {MAX_NAME} chars")


def _rule5_description(report: Report, fm: dict) -> None:
    desc = str(fm.get("description", "") or "")
    if len(desc) > MAX_DESCRIPTION:
        report.error(f"rule 5: description exceeds {MAX_DESCRIPTION} chars ({len(desc)})")
    # third-person heuristic = WARNING only (A2 R3 / Decision 7).
    m = FIRST_PERSON_RE.search(desc)
    if m:
        report.warn(
            f"rule 5: description uses first-person pronoun '{m.group(0)}' "
            f"(prefer third-person): {desc.strip()[:80]}"
        )


def _rule6_metadata(report: Report, fm: dict) -> None:
    meta = fm.get("metadata", {}) or {}
    vocab = _load_vocab()
    for key in REQUIRED_META_KEYS:
        if key not in meta:
            report.error(f"rule 6: metadata missing required key '{key}'")
    for key in SCALAR_VOCAB_KEYS:
        if key in meta and meta[key] not in vocab.get(key, []):
            report.error(f"rule 6: metadata.{key} '{meta[key]}' not in controlled vocab")
    for key in LIST_VOCAB_KEYS:
        if key in meta:
            for val in meta[key] if isinstance(meta[key], list) else [meta[key]]:
                if val not in vocab.get(key, []):
                    report.error(f"rule 6: metadata.{key} value '{val}' not in controlled vocab")
    plugin = meta.get("plugin")
    if plugin and plugin not in registered_bundles(vocab):
        report.error(f"rule 6: metadata.plugin '{plugin}' not a registered marketplace bundle")


def _rule7_length_and_license(report: Report, fm: dict, body: str) -> None:
    if fm.get("license") != "Apache-2.0":
        report.error(f"rule 7: license must be Apache-2.0 (got {fm.get('license')!r})")
    n = len(body.split("\n"))
    if n > MAX_BODY_LINES_HARD:
        report.error(f"rule 7: body length {n} lines exceeds hard cap {MAX_BODY_LINES_HARD}")
    elif n >= MAX_BODY_LINES_WARN:
        report.warn(f"rule 7: body length {n} lines approaching cap {MAX_BODY_LINES_HARD}")


def _rule8_dead_refs(report: Report, body: str, skill_dir: Path) -> None:
    for m in REF_PATH_RE.finditer(body):
        ref = m.group(0)
        if not (skill_dir / ref).exists():
            report.error(f"rule 8: dead reference link '{ref}' does not resolve on disk")


def _rule9_kb_resolution(report: Report, body: str, skill_dir: Path, repo: Path) -> None:
    # Gather text from the SKILL body + the references/_skill-kb.md manifest.
    sources = [(body, skill_dir / "SKILL.md")]
    manifest = skill_dir / "references" / "_skill-kb.md"
    if manifest.is_file():
        sources.append((_read(manifest), manifest))

    today = date.today()
    for text, base in sources:
        # Path form — every ../../knowledge-base/... path resolves on disk.
        for m in KB_PATH_RE.finditer(text):
            target = (base.parent / m.group(0)).resolve()
            if not target.is_file():
                report.error(f"rule 9: dead KB path '{m.group(0)}' (from {base.name})")
        # ID form — every KB-... id resolves in its folder registry + staleness/source warns.
        for kb_id in set(ID_RE.findall(text)):
            parts = kb_id.split("-")
            folder = PREFIX_FOLDER.get(parts[1]) if len(parts) >= 3 else None
            if not folder:
                report.error(f"rule 9: KB id '{kb_id}' has unknown folder prefix")
                continue
            entry = _registry_entry(folder, kb_id, repo)
            if entry is None:
                report.error(f"rule 9: KB id '{kb_id}' does not resolve in {folder}/_registry.yaml")
                continue
            # Staleness WARN (A3 §3.10) — volatile fragment past the window.
            if entry.get("volatile") and entry.get("last_reviewed"):
                lr = entry["last_reviewed"]
                if isinstance(lr, str):
                    lr = datetime.strptime(lr, "%Y-%m-%d").date()
                if (today - lr).days > STALENESS_DAYS:
                    report.warn(
                        f"rule 9: volatile KB fragment '{kb_id}' last_reviewed {lr} "
                        f"predates the {STALENESS_DAYS}-day window"
                    )
            # Source/year WARN (A3 §3.9) — a data-point with an empty source/year.
            if folder == "data-points":
                if not entry.get("source"):
                    report.warn(f"rule 9: data-point '{kb_id}' has an empty source")
                if not entry.get("year"):
                    report.warn(f"rule 9: data-point '{kb_id}' has an empty year")


def _rule10_time_sensitive(report: Report, body: str) -> None:
    for i, line in enumerate(body.split("\n"), 1):
        m = TIME_SENSITIVE_RE.search(line)
        if m:
            report.warn(
                f"rule 10: time-sensitive phrasing '{m.group(0)}' at line {i} "
                f"(push the volatile fact into the KB)"
            )
            break  # one warning is enough to surface the issue


# --- public API ----------------------------------------------------------------

def validate_skill(path: Path, repo: Path = REPO) -> Report:
    """Run all 10 A2 rules against the skill folder at `path`."""
    skill_dir = Path(path)
    report = Report(skill=skill_dir.name)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        report.error(f"rule 0: no SKILL.md in {skill_dir}")
        return report

    text = _read(skill_md)
    fm, body = _split_frontmatter(text)

    _rule1_blocks(report, body, repo)
    _rule2_rosters(report, body)
    _rule3_layout(report, skill_dir)
    _rule4_name(report, fm, skill_dir)
    _rule5_description(report, fm)
    _rule6_metadata(report, fm)
    _rule7_length_and_license(report, fm, body)
    _rule8_dead_refs(report, body, skill_dir)
    _rule9_kb_resolution(report, body, skill_dir, repo)
    _rule10_time_sensitive(report, body)
    return report


def _validate_standard_only(path: Path, repo: Path = REPO) -> Report:
    """The open-standard frontmatter subset: name + description + license + metadata
    vocab (rules 4, 5, 6, 7-license). Drives the SAME rule functions — no second
    engine (research Open Q2 / A3)."""
    skill_dir = Path(path)
    report = Report(skill=skill_dir.name)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        report.error(f"rule 0: no SKILL.md in {skill_dir}")
        return report
    fm, body = _split_frontmatter(_read(skill_md))
    _rule4_name(report, fm, skill_dir)
    _rule5_description(report, fm)
    _rule6_metadata(report, fm)
    if fm.get("license") != "Apache-2.0":
        report.error(f"rule 7: license must be Apache-2.0 (got {fm.get('license')!r})")
    return report


def _iter_skill_dirs(repo: Path) -> List[Path]:
    """Every skill folder under skills/ + the examples/ reference stubs."""
    found: List[Path] = []
    for root in (repo / "skills", repo / "examples"):
        if root.is_dir():
            for child in sorted(root.rglob("SKILL.md")):
                found.append(child.parent)
    return found


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Lint HSE skills against the A2 10-rule contract (A8 §4.1)."
    )
    parser.add_argument("skills", nargs="*", help="skill folder(s) to lint")
    parser.add_argument("--all", action="store_true", help="lint every skill in the repo")
    parser.add_argument(
        "--standard-only", action="store_true",
        help="run only the open-standard frontmatter rules (name/description/license/metadata)",
    )
    parser.add_argument("--repo", default=str(REPO), help="repo root (default: inferred)")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()

    if args.all:
        targets = _iter_skill_dirs(repo)
    else:
        targets = [Path(s) for s in args.skills]
    if not targets:
        parser.error("no skills given (pass folders or --all)")

    runner = _validate_standard_only if args.standard_only else validate_skill
    any_error = False
    for target in targets:
        report = runner(target, repo)
        for e in report.errors:
            print(f"ERROR  [{report.skill}] {e}", file=sys.stderr)
        for w in report.warnings:
            print(f"WARN   [{report.skill}] {w}")
        if report.errors:
            any_error = True
        else:
            print(f"OK     [{report.skill}] lint clean ({len(report.warnings)} warnings)")
    return 1 if any_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
