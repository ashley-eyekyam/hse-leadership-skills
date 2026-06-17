#!/usr/bin/env python3
"""validate_adapters.py — the adapter-output validator (Unit C, §3.8).

Runs the SIX §3.8 checks against every emitted Tier-B bundle — PLUS the D-09
no-heavy-`assets/` "share don't duplicate" contract check — so the four
non-negotiables (de-id · DISCLAIMER · HoC · §2.7 intake) are CI-proven present IN
the instruction text (not merely somewhere in knowledge/), R2 is CI-verified
(no `<!-- hse:block` literal in any instruction field; markers preserved in the
knowledge SKILL.md copy; block CONTENTS survive marker-free), and a committed
bundle that drifts from a fresh build, or carries a stray heavy `assets/` payload,
hard-fails CI.

This carries A8's de-id-auto-fail philosophy into the adapter layer: a bundle that
spilled a non-negotiable into knowledge/ FAILS check 3 (the negative fixture). The
two enforcement classes stay distinct — ``errors`` HARD-block CI, ``warnings``
surface only (the ``Report`` shape copied from ``lint_skills``).

stdlib + pyyaml only — the same dependency floor as build.py / A7 / A8 / A10.

Public surface:
    Report                              — errors(block)/warnings(surface)/ok (lint_skills shape)
    validate_bundle(bundle_dir, skill_dir, platform, platforms_cfg) -> Report
    check_no_heavy_assets(bundle_dir, platform) -> list[str]
    bundle_diff(repo) -> Report
    main(argv) -> int
"""

from __future__ import annotations

import argparse
import difflib
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import build  # the build machinery this validator re-extracts canonical content from

ADAPTERS_DIR = Path(__file__).resolve().parent
REPO = ADAPTERS_DIR.parent
SKILLS_DIR = REPO / "skills"
PLATFORMS = build.PLATFORMS

# The instruction file each platform writes (mirrors build._INSTRUCTION_FILE).
_INSTRUCTION_FILE = build._INSTRUCTION_FILE
# The structural required files each bundle must carry (mirrors build._REQUIRED_FILES,
# plus the knowledge/ directory the validator additionally requires).
_REQUIRED_FILES = build._REQUIRED_FILES

# The ONLY top-level entries a committed bundle may carry (D-09 share-don't-duplicate).
# Anything else — especially a heavy `assets/` payload — is a hard error.
_ALLOWED_BUNDLE_ENTRIES = {
    "instructions.md",
    "system-prompt.md",
    "manifest.json",
    "INSTALL.md",
    "knowledge",
}

_RESIDUAL_MARKER_RE = re.compile(r"<!--\s*hse:block")


# --- the Report shape (copied byte-shape from lint_skills.Report, §3.8) ---------


@dataclass
class Report:
    """The structured validation result — the shared two-enforcement-classes shape:
    ``errors`` HARD-block CI; ``warnings`` surface only. Mirrors lint_skills.Report."""

    target: str
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def extend(self, other: "Report") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


# --- content-match helpers (§3.2 content-survives-even-if-marker-doesn't) -------


def _normalize(text: str) -> str:
    """Collapse all whitespace runs to single spaces for marker-independent content
    matching (markers already stripped from instructions; the source block carries
    them). Lets a block's CONTENTS be matched present regardless of re-wrapping."""
    return re.sub(r"\s+", " ", text).strip()


def _marker_free(text: str) -> str:
    """Strip every hse:block marker TOKEN (build.strip_markers) then normalize — so a
    source block's CONTENTS can be matched against the marker-free instruction text."""
    return _normalize(build.strip_markers(text))


def _contains(haystack_norm: str, needle: str, *, min_chars: int = 40) -> bool:
    """Is the (marker-free, normalized) ``needle`` substring present in the normalized
    haystack? For long block bodies we match a robust leading slice (the block's
    opening sentence survives the spill / re-wrap) rather than demanding a byte-for-byte
    whole-block match the renderer may have re-flowed."""
    n = _marker_free(needle)
    if not n:
        return False
    probe = n[:min_chars] if len(n) > min_chars else n
    return probe in haystack_norm


# --- the SIX §3.8 checks --------------------------------------------------------


def _check_well_formed(rep, bundle_dir, platform, has_a7) -> str:
    """Check 1 — required files present; manifest is valid JSON of the platform shape;
    knowledge/ present. Returns the instruction text (or "")."""
    for rel in _REQUIRED_FILES[platform]:
        if not (bundle_dir / rel).is_file():
            rep.error(f"{platform}/{bundle_dir.name}: missing required file {rel}")
    if not (bundle_dir / "knowledge").is_dir():
        rep.error(f"{platform}/{bundle_dir.name}: missing knowledge/ directory")
    manifest = bundle_dir / "manifest.json"
    if manifest.is_file():
        import json

        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            rep.error(f"{platform}/{bundle_dir.name}: manifest.json invalid JSON — {e}")
        else:
            if not isinstance(data, dict) or "name" not in data:
                rep.error(
                    f"{platform}/{bundle_dir.name}: manifest.json missing 'name' "
                    f"(not the platform shape)"
                )
    instr_path = bundle_dir / _INSTRUCTION_FILE[platform]
    instr = instr_path.read_text(encoding="utf-8") if instr_path.is_file() else ""
    if not instr:
        rep.error(f"{platform}/{bundle_dir.name}: empty/missing instruction surface")
    return instr


def _check_char_limit(rep, bundle_dir, platform, instr, platforms_cfg) -> None:
    """Check 2 — the instruction field char count ≤ the platform char_limit."""
    limit = platforms_cfg["platforms"][platform]["char_limit"]
    if len(instr) > limit:
        rep.error(
            f"{platform}/{bundle_dir.name}: instruction field {len(instr)} chars "
            f"exceeds char_limit {limit} (Decision 6)"
        )


def _check_non_negotiables(rep, bundle_dir, platform, instr, adapted) -> None:
    """Check 3 — the four non-negotiables present IN the instructions (NOT merely in
    knowledge/ — Pitfall 3 + the Copilot anti-XPIA note). The single biggest Phase-7
    safety gap; a bundle that spilled any one into knowledge/ FAILS here."""
    norm = _normalize(instr)
    tag = f"{platform}/{bundle_dir.name}"

    # De-id: the deid block CONTENTS present in the instruction text.
    if not _contains(norm, adapted.blocks["deid"]):
        rep.error(f"{tag}: de-id block content MISSING from instructions (non-negotiable)")

    # DISCLAIMER: the preamble line present in instructions AND DISCLAIMER.md in knowledge/.
    if "decision-support only" not in instr.lower():
        rep.error(f"{tag}: DISCLAIMER preamble MISSING from instructions (non-negotiable)")
    if not (bundle_dir / "knowledge" / "DISCLAIMER.md").is_file():
        rep.error(f"{tag}: DISCLAIMER.md MISSING from knowledge/ (non-negotiable)")

    # Hierarchy-of-controls (KB-SNIP-HOC): the HoC instruction content present.
    if "hierarchy-of-controls" not in norm and "hierarchy of controls" not in norm:
        rep.error(f"{tag}: hierarchy-of-controls (KB-SNIP-HOC) MISSING from instructions")

    # §2.7 intake: the intake heading + the skill's question set present.
    if not _contains(norm, adapted.intake_questions, min_chars=30):
        rep.error(f"{tag}: §2.7 intake question set MISSING from instructions (non-negotiable)")
    if "intake" not in norm:
        rep.error(f"{tag}: §2.7 intake heading MISSING from instructions")


def _check_r2_markers(rep, bundle_dir, platform, instr) -> None:
    """Check 4 — instructions carry NO `<!-- hse:block` literal; the knowledge SKILL.md
    copy DOES (preserved + re-ingestible). Block CONTENTS asserted by check 3."""
    tag = f"{platform}/{bundle_dir.name}"
    if _RESIDUAL_MARKER_RE.search(instr):
        rep.error(f"{tag}: residual `<!-- hse:block` marker leaked into instructions (R2)")
    skill_copy = bundle_dir / "knowledge" / "SKILL.md"
    if not skill_copy.is_file():
        rep.error(f"{tag}: knowledge/SKILL.md copy MISSING (R2 re-ingestible source)")
    elif not _RESIDUAL_MARKER_RE.search(skill_copy.read_text(encoding="utf-8")):
        rep.error(
            f"{tag}: knowledge/SKILL.md copy lost its hse:block markers "
            f"(must be preserved + re-ingestible — R2/§3.2)"
        )
    # The §3.3 report-output heading anchor must survive the strip (Pitfall 1).
    if "## Output format" not in instr:
        rep.error(f"{tag}: `## Output format` heading did not survive the marker strip (Pitfall 1)")


def _check_knowledge_resolvable(rep, bundle_dir, platform, skill_dir) -> None:
    """Check 5 — every KB fragment / reference the skill's _skill-kb.md names exists in
    the UPLOADED knowledge/ copy (adapter analogue of A8 rule 9 — the uploaded copy
    resolves, not the repo path)."""
    tag = f"{platform}/{bundle_dir.name}"
    manifest = skill_dir / "references" / "_skill-kb.md"
    if not manifest.is_file():
        return  # not every skill carries a _skill-kb manifest
    present = {p.name for p in (bundle_dir / "knowledge").iterdir() if p.is_file()}
    text = manifest.read_text(encoding="utf-8")
    for m in re.finditer(r"(?:\.\./)+knowledge-base/[A-Za-z0-9_./-]+\.md", text):
        basename = m.group(0).rsplit("/", 1)[-1]
        if basename not in present:
            rep.error(
                f"{tag}: KB fragment {basename!r} named in _skill-kb.md is NOT in the "
                f"uploaded knowledge/ (check 5 — unresolvable on the host)"
            )


def _check_orchestration_degraded(rep, bundle_dir, platform, instr) -> None:
    """Check 6 — the single-thread fallback + De-identifier-first sequencing + the
    mandatory Critic/QA instruction present; no dangling 'spawn parallel subagents'
    without a fallback."""
    tag = f"{platform}/{bundle_dir.name}"
    norm = _normalize(instr).lower()
    if "single-thread" not in norm and "single thread" not in norm:
        rep.error(f"{tag}: orchestration single-thread fallback MISSING (check 6)")
    if "de-identifier" not in norm and "de-identif" not in norm:
        rep.error(f"{tag}: De-identifier-first sequencing MISSING from orchestration (check 6)")
    if "critic" not in norm and "qa pass" not in norm and "critic/qa" not in norm:
        rep.error(f"{tag}: mandatory Critic/QA instruction MISSING (check 6)")


def check_no_heavy_assets(bundle_dir: Path, platform: str) -> List[str]:
    """D-09 no-heavy-`assets/` check — a committed bundle carries ONLY
    instructions/system-prompt + knowledge/ + manifest + INSTALL.md. A stray
    `assets/` payload (the heavy A4 engine / fonts / hse_components duplicated 49×)
    is a HARD error that would also slip the bundle-diff scope. For a ChatGPT bundle,
    the INSTALL.md must NAME the canonical shared assets (share, don't duplicate).
    Returns a list of problems ([] = clean)."""
    problems: List[str] = []
    tag = f"{platform}/{bundle_dir.name}"
    if (bundle_dir / "assets").exists():
        problems.append(
            f"{tag}: committed `assets/` payload present — heavy assets must be SHARED "
            f"from the single canonical copy (D-09), never duplicated into the bundle"
        )
    for entry in bundle_dir.iterdir():
        if entry.name not in _ALLOWED_BUNDLE_ENTRIES:
            problems.append(
                f"{tag}: unexpected bundle entry {entry.name!r} — only "
                f"instructions/system-prompt + knowledge/ + manifest.json + INSTALL.md "
                f"are permitted (D-09 share-don't-duplicate)"
            )
    if platform == "chatgpt":
        install = bundle_dir / "INSTALL.md"
        if install.is_file():
            text = install.read_text(encoding="utf-8")
            if "assets/report-engine/" not in text:
                problems.append(
                    f"{tag}: ChatGPT INSTALL.md does NOT name the canonical "
                    f"`assets/report-engine/` to upload (D-09 share-don't-duplicate)"
                )
    return problems


def validate_bundle(
    bundle_dir: Path, skill_dir: Path, platform: str, platforms_cfg: dict
) -> Report:
    """Run the SIX §3.8 checks + the D-09 no-heavy-`assets/` check on one bundle."""
    bundle_dir = Path(bundle_dir)
    rep = Report(target=f"{platform}/{bundle_dir.name}")
    if not bundle_dir.is_dir():
        rep.error(f"{platform}/{bundle_dir.name}: bundle directory does not exist")
        return rep

    # Re-extract the canonical block CONTENTS from the SOURCE SKILL.md (using the
    # markers, in the repo) — the §3.2 content-survives-even-if-marker-doesn't basis.
    try:
        adapted = build.load_skill(skill_dir)
    except (ValueError, build.IrreducibleOverflow) as e:
        rep.error(f"{platform}/{bundle_dir.name}: source skill failed to load — {e}")
        return rep

    has_a7 = adapted.has_a7
    instr = _check_well_formed(rep, bundle_dir, platform, has_a7)
    if instr:
        _check_char_limit(rep, bundle_dir, platform, instr, platforms_cfg)
        _check_non_negotiables(rep, bundle_dir, platform, instr, adapted)
        _check_r2_markers(rep, bundle_dir, platform, instr)
        _check_orchestration_degraded(rep, bundle_dir, platform, instr)
    _check_knowledge_resolvable(rep, bundle_dir, platform, skill_dir)
    for prob in check_no_heavy_assets(bundle_dir, platform):
        rep.error(prob)
    return rep


# --- bundle-diff drift detection (the gen_marketplace --check idiom) ------------


def bundle_diff(repo: Path, platforms_cfg: Optional[dict] = None) -> Report:
    """Rebuild every committed bundle in-memory (to a temp tree) and diff against the
    on-disk ``adapters/`` bytes — the gen_marketplace.py --check pattern. A hand-edited
    committed bundle fails this. Scoped to the committed files (instructions/knowledge/
    manifest/INSTALL.md) — consistent with the no-heavy-`assets/` contract."""
    repo = Path(repo).resolve()
    rep = Report(target="bundle-diff")
    adapters_root = repo / "adapters"
    tmp = Path(tempfile.mkdtemp(prefix="hse-bundle-diff-"))
    try:
        rc = build.main(["--all", "--out", str(tmp), "--repo", str(repo)])
        if rc != 0:
            rep.error("bundle-diff: a fresh build.py --all did not exit 0 (see build output)")
            return rep
        for platform in PLATFORMS:
            committed_p = adapters_root / platform
            fresh_p = tmp / platform
            if not committed_p.is_dir():
                rep.error(f"bundle-diff: committed adapters/{platform}/ is missing")
                continue
            for fresh_file in sorted(fresh_p.rglob("*")):
                if not fresh_file.is_file():
                    continue
                rel = fresh_file.relative_to(fresh_p)
                committed_file = committed_p / rel
                if not committed_file.is_file():
                    rep.error(f"bundle-diff: committed {platform}/{rel} is MISSING (drift)")
                    continue
                fresh_text = fresh_file.read_text(encoding="utf-8")
                committed_text = committed_file.read_text(encoding="utf-8")
                if fresh_text != committed_text:
                    diff = "".join(
                        difflib.unified_diff(
                            committed_text.splitlines(keepends=True),
                            fresh_text.splitlines(keepends=True),
                            fromfile=f"committed/{platform}/{rel}",
                            tofile=f"rebuilt/{platform}/{rel}",
                        )
                    )
                    rep.error(
                        f"bundle-diff: committed {platform}/{rel} DRIFTED from a fresh "
                        f"build (hand-edit?) — re-run build.py --all:\n{diff}"
                    )
            # Reverse scan: a committed file with no fresh counterpart (stale bundle).
            for committed_file in sorted(committed_p.rglob("*")):
                if not committed_file.is_file():
                    continue
                rel = committed_file.relative_to(committed_p)
                if not (fresh_p / rel).is_file():
                    rep.error(
                        f"bundle-diff: committed {platform}/{rel} has NO fresh "
                        f"counterpart (stale/orphan bundle file — drift)"
                    )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return rep


# --- CLI -----------------------------------------------------------------------


def _iter_skill_names(repo: Path) -> List[str]:
    return sorted(p.parent.name for p in (repo / "skills").rglob("SKILL.md"))


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Validate emitted Tier-B adapter bundles (C §3.8).")
    p.add_argument("--skill", action="append", help="skill name(s); omit with --all")
    p.add_argument("--all", action="store_true", help="validate every committed bundle")
    p.add_argument(
        "--platform", default="all",
        choices=["chatgpt", "gemini", "copilot", "generic", "all"],
    )
    p.add_argument(
        "--non-negotiables", action="store_true",
        help="run ONLY the four-non-negotiables check (its own named CI job)",
    )
    p.add_argument(
        "--no-diff", action="store_true",
        help="skip the rebuild-and-diff drift check (per-bundle checks only)",
    )
    p.add_argument("--repo", default=str(REPO), help="repo root (default: inferred)")
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()
    adapters_root = repo / "adapters"
    platforms_cfg = build.load_platforms()

    if args.all:
        skills = _iter_skill_names(repo)
    elif args.skill:
        skills = list(args.skill)
    else:
        p.error("no skills given (pass --skill NAME ... or --all)")
    targets = PLATFORMS if args.platform == "all" else [args.platform]

    reports: List[Report] = []
    for skill in skills:
        skill_dir = repo / "skills" / skill
        for platform in targets:
            bundle_dir = adapters_root / platform / skill
            rep = validate_bundle(bundle_dir, skill_dir, platform, platforms_cfg)
            if args.non_negotiables:
                # Keep only the non-negotiable / DISCLAIMER / HoC / intake errors.
                rep.errors = [
                    e for e in rep.errors
                    if "non-negotiable" in e or "hierarchy-of-controls" in e
                    or "intake" in e or "DISCLAIMER" in e
                ]
                rep.warnings = []
            reports.append(rep)

    # The rebuild-and-diff drift check (skipped for --non-negotiables / --no-diff).
    if args.all and not args.non_negotiables and not args.no_diff:
        reports.append(bundle_diff(repo, platforms_cfg))

    errors = [e for r in reports for e in r.errors]
    warnings = [w for r in reports for w in r.warnings]
    for w in warnings:
        print(f"WARN {w}", file=sys.stderr)
    for e in errors:
        print(f"FAIL {e}", file=sys.stderr)
    if errors:
        return 1
    label = "four-non-negotiables" if args.non_negotiables else "all §3.8 checks"
    print(f"OK: {len(reports)} bundle report(s) clean ({label})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
