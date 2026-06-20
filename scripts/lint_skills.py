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

# --- Rules 11/12 severity (FND-04 / D-02 staged rollout) -----------------------
# The elicitation-coverage (rule 11) + sme-review (rule 12) findings route through
# _emit() at this single level. As of the Phase-10 HARD cutover they land as
# ERROR (HARD) — the 48 in-scope skills were backfilled HARD-clean in Phase 9 and
# carry the promoted block, so `lint --all` stays GREEN. The flip was the single
# token below ("warn" -> "error"); the CLI/CI invocation is unchanged (no --strict,
# no env var) so D-11 holds and none of the 8 branch-protection CI contexts move.
RULE_11_12_LEVEL = "error"


def _emit(report: Report, msg: str) -> None:
    """Route a rule-11/12 finding to error or warn per RULE_11_12_LEVEL."""
    (report.error if RULE_11_12_LEVEL == "error" else report.warn)(msg)

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
    # WR-03: normalize CRLF before the LF-only frontmatter regex. _read() returns
    # raw UTF-8, so a CRLF-authored reference file (e.g. references/intake.md /
    # sme-review.md written on Windows) would otherwise fail the `^---\n...\n---\n`
    # match and yield fm={} — a false "manifest absent/unparseable". Both Rules 11
    # and 12 reach manifests through this function, so this single fix covers both.
    text = text.replace("\r\n", "\n")
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


# --- Rules 11/12 helpers (FND-04: elicitation-coverage + sme-review) -----------

# FROZEN normalized Q-type whitelist (rule 11 step 6, D-01). Built once from the
# six family-rollout specs by gathering every distinct `Type` cell of every
# branched Q-table and normalizing it (strip whitespace, lowercase):
#     grep '^|' docs/.../2026-06-20-elicitation-sme/0[1-6]-*.md | awk -F'|' '$4!="Type"{print $4}'
#     | <normalize: re.sub(r"\s+","",s.strip().lower())>
# 19 raw strings folded to the 17 normalized entries below; frozen 2026-06-20.
# D-01 accepted trade-off: a genuinely-new Phase-9 Type variant absent from all
# family specs will NOT auto-normalize through — it must be ADDED here by editing
# this set. Because rules 11/12 are WARN in Phase 9, such a stray variant surfaces
# as a WARN (not a hard block) before the Phase-10 HARD flip. The two arrow entries
# (free-text->role, mcq->confirm) carry a literal U+2192 that survives normalization.
_VALID_Q_TYPES = {
    "free-text",
    "free-text(date-time)",
    "free-text(ints)",
    "free-text(number)mandatory",
    "free-text(optional)",
    "free-text(structured)",
    "free-text+mcq",
    "free-text/mcq-if-enumerable",
    "free-text/mcqmulti",
    "free-text→role",
    "mcq",
    "mcq+free-text",
    "mcqmulti",
    "mcqmulti-select",
    "mcqmulti-select+free-text",
    "mcqperendpoint",
    "mcq→confirm",
}

# The persona never emits sign-off language — the optional rule-12 boundary WARN
# guards these phrases (kept in sync with scripts/sme_review.py:SIGN_OFF_FORBIDDEN,
# SME-02). Always WARN regardless of RULE_11_12_LEVEL.
SIGN_OFF_FORBIDDEN = (
    "approved by a competent person",
    "competent-person sign-off",
    "competent person sign-off",
    "signed off by a competent person",
    "reviewed and approved",
)


def _norm_qtype(s: str) -> str:
    """Normalize a Q-table Type cell for _VALID_Q_TYPES membership (D-01)."""
    return re.sub(r"\s+", "", str(s).strip().lower())


def _taxonomy_ids(repo: Path) -> set:
    """Every ELI-* id in knowledge-base/elicitation-taxonomy.yaml (its OWN
    namespace — not routed through PREFIX_FOLDER / resolve_kb_id / rule 9).
    Empty set if the file is absent."""
    f = repo / "knowledge-base" / "elicitation-taxonomy.yaml"
    if not f.is_file():
        return set()
    return {e["id"] for e in (yaml.safe_load(_read(f)) or []) if "id" in e}


def _taxonomy_universals(repo: Path) -> set:
    """The `universal: true` ELI-* ids (the floor for rule 11 step 3). Read from
    the SAME file so the floor stays single-sourced (never hard-coded)."""
    f = repo / "knowledge-base" / "elicitation-taxonomy.yaml"
    if not f.is_file():
        return set()
    return {e["id"] for e in (yaml.safe_load(_read(f)) or []) if e.get("universal")}


def _parse_q_table(text: str) -> List[dict]:
    """Parse the branched intake Q-table into a list of row dicts.

    Columns: | # | Question | Type | Options / prompt | Dim | Asked-when |.
    Skips the header row and the |---| separator row; trims cells; keys each data
    row by the header cells (tolerating the 4th-column label variance
    `Options` vs `Options / prompt`). Positional aliases are ALSO set
    (Type = 3rd data cell, Dim = 5th) so corpus variance can't break access.
    Never raises on a malformed row."""
    rows: List[dict] = []
    header: Optional[List[str]] = None
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        # separator row: all cells are dashes/colons.
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            continue
        if header is None:
            header = cells
            continue
        row: dict = {}
        for i, val in enumerate(cells):
            key = header[i] if i < len(header) else f"col{i}"
            row[key] = val
        # positional fallbacks (3rd data cell = Type, 5th = Dim) per Open Q2.
        if len(cells) > 2:
            row.setdefault("Type", cells[2])
        if len(cells) > 4:
            row.setdefault("Dim", cells[4])
        # tolerate the 4th-column label variance.
        if "Options / prompt" not in row and "Options" in row:
            row["Options / prompt"] = row["Options"]
        elif "Options" not in row and "Options / prompt" in row:
            row["Options"] = row["Options / prompt"]
        rows.append(row)
    return rows


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
    bundles = registered_bundles(vocab)
    if plugin and plugin not in bundles:
        report.error(f"rule 6: metadata.plugin '{plugin}' not a registered marketplace bundle")
    # D-06 cross-bundle membership: metadata.bundled_in is OPTIONAL; when present every
    # value must resolve to a registered bundle (same single source as plugin — WR-05).
    for extra in (meta.get("bundled_in") or []):
        if extra not in bundles:
            report.error(
                f"rule 6: metadata.bundled_in '{extra}' not a registered marketplace bundle"
            )


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
                # D-05c (CT-4): a registry entry may set a per-fragment staleness_days
                # override for a faster-decaying fragment (e.g. KB-REG-IN-OSH-CODE at 90d);
                # absent the key, the 180-day global STALENESS_DAYS default applies.
                window = entry.get("staleness_days", STALENESS_DAYS)
                if (today - lr).days > window:
                    report.warn(
                        f"rule 9: volatile KB fragment '{kb_id}' last_reviewed {lr} "
                        f"predates the {window}-day window"
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


def _rule11_intake_coverage(report: Report, body: str, skill_dir: Path, repo: Path) -> None:
    """FND-04 rule 11 — the elicitation-coverage contract on references/intake.md.

    Every finding routes through _emit() (WARN this phase). Steps per research §4.3.
    `body` is the SKILL.md body (for the lean-pointer step); the manifest + Q-table
    live in references/intake.md."""
    # 1. Presence.
    f = skill_dir / "references" / "intake.md"
    if not f.is_file():
        _emit(report, "rule 11: missing references/intake.md")
        return
    # 2. Parse manifest (YAML front-matter, §3.4 convention).
    fm, intake_body = _split_frontmatter(_read(f))
    mani = fm.get("intake-coverage")
    if not isinstance(mani, dict):
        _emit(report, "rule 11: intake-coverage manifest absent/unparseable")
        return
    covers = set(mani.get("covers") or [])
    omits = mani.get("omits") or {}
    if not isinstance(omits, dict):
        omits = {}
    branches = mani.get("branches") or []
    if not isinstance(branches, list):
        branches = []

    all_ids = _taxonomy_ids(repo)
    universals = _taxonomy_universals(repo)
    # WR-01: when the elicitation taxonomy could not load (file missing or empty),
    # _taxonomy_ids returns an empty set and EVERY downstream dimension check would
    # silently no-op: the universal floor (step 3) iterates an empty `universals`,
    # ID-resolution (step 4) is guarded by `if all_ids and ...`, and conditional
    # completeness (step 5) iterates `all_ids - universals` (empty). That silently
    # disables the specificity gate. Emit a finding and early-return BEFORE the
    # dependent steps no-op. The spec frames this HARD for HARD-flip safety; it
    # routes through _emit so it lands level-correct (WARN this phase) but MUST fire.
    if not all_ids:
        _emit(report, "rule 11: elicitation taxonomy missing or empty — cannot resolve dimensions")
        return
    conditionals = all_ids - universals

    # 3. Universal floor.
    for uid in sorted(universals):
        if uid not in covers:
            _emit(report, f"rule 11: covers must include the universal dimension {uid}")
    # 4. ID resolution.
    for cid in sorted(covers):
        if all_ids and cid not in all_ids:
            _emit(report, f"rule 11: unknown elicitation dimension '{cid}'")
    for oid in sorted(omits):
        if all_ids and oid not in all_ids:
            _emit(report, f"rule 11: unknown elicitation dimension '{oid}'")
    # 5. Conditional completeness.
    for cid in sorted(conditionals):
        if cid in covers:
            continue
        if cid in omits:
            reason = omits.get(cid)
            if not (isinstance(reason, str) and reason.strip()):
                _emit(report, f"rule 11: omits['{cid}'] needs a non-empty reason")
        else:
            _emit(
                report,
                f"rule 11: conditional dimension '{cid}' must be in covers or omits-with-reason",
            )

    # 6. Q-table typing + Dim binding (D-01). Q-table lives in the intake.md body.
    qrows = _parse_q_table(intake_body)
    for row in qrows:
        num = row.get("#", "?")
        qtype = row.get("Type", "")
        if _norm_qtype(qtype) not in _VALID_Q_TYPES:
            _emit(report, f"rule 11: Q-row '{num}' has untyped/invalid Type '{qtype}'")
        dim_cell = row.get("Dim", "") or ""
        for piece in re.split(r"[/,]", dim_cell):
            did = piece.strip()
            if not did:
                continue
            if did not in covers:
                _emit(report, f"rule 11: Q-row '{num}' Dim '{did}' not in covers")

    # Index the Q-rows by their declared id for branch integrity (step 7/8).
    q_by_id = {}
    for row in qrows:
        qid = (row.get("#", "") or "").strip()
        if qid:
            q_by_id[qid] = row

    def _options_of(row: dict) -> List[str]:
        cell = row.get("Options / prompt", row.get("Options", "")) or ""
        return [o.strip() for o in re.split(r"[/,;]", cell) if o.strip()]

    # 7. Branch integrity.
    for br in branches:
        if not isinstance(br, dict):
            _emit(report, "rule 11: branch entry is not a mapping")
            continue
        trig_q = str(br.get("when") or br.get("ask") or "").strip()
        trig_opt = str(br.get("option") or br.get("equals") or "").strip()
        # trigger references a real prior Q id; if an option is given it must be valid.
        if trig_q and trig_q not in q_by_id:
            _emit(report, f"rule 11: branch trigger references unknown question/option '{trig_q}'")
        elif trig_q and trig_opt:
            opts_norm = [o.lower() for o in _options_of(q_by_id[trig_q])]
            if trig_opt.lower() not in opts_norm:
                _emit(
                    report,
                    f"rule 11: branch trigger references unknown question/option '{trig_opt}'",
                )
        for tgt in (br.get("activates_questions") or []):
            if str(tgt).strip() not in q_by_id:
                _emit(
                    report,
                    f"rule 11: branch activates_questions target '{tgt}' has no matching Q-row",
                )

    # 8. Mandatory India->state branch.
    if "ELI-JURIS" in covers:
        juris_rows = [
            r for r in qrows
            if any(d.strip() == "ELI-JURIS" for d in re.split(r"[/,]", r.get("Dim", "") or ""))
        ]
        has_india = any("india" in (" ".join(_options_of(r))).lower() for r in juris_rows)
        if has_india:
            ok = False
            for br in branches:
                if not isinstance(br, dict):
                    continue
                trig = str(br.get("option") or br.get("equals") or br.get("when") or "").lower()
                if "india" not in trig:
                    continue
                for tgt in (br.get("activates_questions") or []):
                    row = q_by_id.get(str(tgt).strip())
                    if not row:
                        continue
                    blob = (row.get("Question", "") + " " + " ".join(_options_of(row))).lower()
                    if "state" in blob:
                        ok = True
            if not ok:
                _emit(report, "rule 11: ELI-JURIS covers India but no mandatory India->state branch")

    # 9. Echo-back + refuse-on-vague present.
    if not re.search(r"(?i)echo.{0,20}(back|the captured|confirm)", intake_body):
        _emit(report, "rule 11: intake.md missing echo-back cue")
    if not re.search(r"(?i)refuse|never proceed on (a )?vague|specificity anchor", intake_body):
        _emit(report, "rule 11: intake.md missing refuse-on-vague cue")

    # 10. SKILL.md lean pointer.
    if "references/intake.md" not in body:
        _emit(report, "rule 11: SKILL.md missing lean pointer to references/intake.md")


def _rule12_sme_review(report: Report, body: str, skill_dir: Path) -> None:
    """FND-04 rule 12 — the per-skill SME sign-off contract on
    references/sme-review.md. Every finding via _emit() (WARN this phase). Steps
    per research §4.4; the boundary phrase check is ALWAYS a WARN (SME-02)."""
    # 1. Presence.
    f = skill_dir / "references" / "sme-review.md"
    if not f.is_file():
        _emit(report, "rule 12: missing references/sme-review.md")
        return
    # 2. Parse manifest.
    fm, sme_body = _split_frontmatter(_read(f))
    mani = fm.get("sme-review")
    if not isinstance(mani, dict):
        _emit(report, "rule 12: sme-review manifest absent/unparseable")
        return
    # 3. Persona count + fields.
    personas = mani.get("personas")
    if not isinstance(personas, list) or not (1 <= len(personas) <= 2):
        n = len(personas) if isinstance(personas, list) else 0
        _emit(report, f"rule 12: sme-review needs 1-2 personas (got {n})")
    else:
        for i, persona in enumerate(personas):
            p = persona if isinstance(persona, dict) else {}
            if not all(
                isinstance(p.get(k), str) and p.get(k).strip()
                for k in ("role", "expertise", "lens")
            ):
                _emit(report, f"rule 12: persona {i} missing role/expertise/lens")
    # 4. Domain checklist >=3 items.
    checklist_items = 0
    in_section = False
    for line in sme_body.split("\n"):
        if re.match(r"^\s*#{1,6}\s", line):
            in_section = bool(re.search(r"(?i)checklist|domain checks", line))
            continue
        if in_section and re.match(r"^\s*[-*]\s", line):
            checklist_items += 1
    if checklist_items < 3:
        _emit(report, "rule 12: sme-review.md domain checklist missing or <3 items")
    # 5. Roster references the file.
    if "references/sme-review.md" not in _below_end(body, "orchestration"):
        _emit(report, "rule 12: orchestration roster does not reference references/sme-review.md")
    # Optional boundary WARN — ALWAYS report.warn (SME-02), regardless of level.
    # WR-02: negation-aware, per-line scan. The canonical boundary phrasing states
    # the prohibition AS A NEGATION (e.g. sme-signoff.md: 'never replaces … never
    # outputs "approved by a competent person"'), which a naive whole-body substring
    # scan false-WARNs on. Only WARN on an AFFIRMATIVE emission of a forbidden
    # phrase: skip any line that reads as a negation/quoted prohibition. A negator
    # token anywhere on the line, or the phrase occurring inside quotes, marks the
    # line as a documented boundary, not a claim.
    _NEGATORS = ("never", "not", "does not", "doesn't", "precedes", "replaces", "without")
    _found = None
    for raw_line in sme_body.split("\n"):
        line = raw_line.lower()
        for phrase in SIGN_OFF_FORBIDDEN:
            if phrase not in line:
                continue
            if any(neg in line for neg in _NEGATORS):
                continue  # negation phrasing — a documented boundary, not a claim
            # quoted occurrence (e.g. never outputs "approved by …") — a prohibition.
            quoted = any(f'{q}{phrase}{q}' in line for q in ('"', "'", "`"))
            if quoted:
                continue
            _found = phrase
            break
        if _found:
            break
    if _found:
        report.warn(
            f"rule 12: sme-review.md contains sign-off boundary phrase '{_found}'"
        )


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

    # Rules 11/12 (FND-04) — behind a TWO-PRONGED exemption gate: the forge
    # (plugin == hse-systems) OR the frozen examples/risk-assessment/ path. The
    # frozen example is plugin: hse-core (NOT hse-systems), so a plugin-only gate
    # would miss it — the path prong is mandatory. Gate lives INSIDE validate_skill
    # (not _iter_skill_dirs) so a direct lint of the exempt skill still runs the
    # other 10 rules. Findings route through _emit (WARN this phase, RULE_11_12_LEVEL).
    plugin = (fm.get("metadata") or {}).get("plugin")
    is_frozen_example = skill_dir.resolve() == (repo / "examples" / "risk-assessment").resolve()
    if plugin != "hse-systems" and not is_frozen_example:
        _rule11_intake_coverage(report, body, skill_dir, repo)
        _rule12_sme_review(report, body, skill_dir)
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
