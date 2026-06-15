"""validate_repo_skill.py — the forge's validator is the SAME linter, never a fork.

A10 Decision 2 / FORGE-03: `hse-skill-forge` must validate scaffold output with the
EXACT module CI runs (`scripts/lint_skills.py`), so a skill can never pass the forge
yet fail CI (threat T-04-03). This module therefore re-EXPORTS the public lint API
rather than re-implementing any rule — the re-exported names are the SAME objects as
in `lint_skills` (the identity test in scripts/tests/test_validate_reexport.py asserts
`validate_repo_skill.validate_skill is lint_skills.validate_skill`).

The repo `scripts/` dir (which holds both `hse_components` and `lint_skills.py`) is put
on `sys.path` via the local verbatim `_shim.py` — the same portability mechanism A7
skills use (A10 D6). With the per-skill `scripts/` symlink stripped, `_shim` still walks
up to the repo's `scripts/` so `from lint_skills import ...` resolves (symlink-removed
trap; scripts/tests/test_shim_no_symlink.py proves it).

The `--sync` verb (the anti-drift healer, A10 D5/D-07) lives at the bottom of this file,
WRAPPING the re-export — never inside lint_skills.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path
from typing import List, Optional

# Put the repo scripts/ dir (hse_components + lint_skills.py) on sys.path via the
# verbatim portability shim, then re-export the linter's public API unchanged.
from _shim import ensure_hse_components

ensure_hse_components(__file__)

from lint_skills import (  # noqa: E402  (import after sys.path mutation, by design)
    Report,
    main as lint_main,
    registered_bundles,
    validate_skill,
)

# Re-export surface — the SAME objects as in lint_skills (identity, not a copy).
__all__ = [
    "validate_skill",
    "lint_main",
    "registered_bundles",
    "Report",
    "sync_skill",
    "main",
]

# The five inline blocks the --sync verb re-copies from template/blocks/* (rule-1
# anti-drift sources). Kept in step with lint_skills.INLINE_BLOCKS; imported so we
# never maintain a second list.
try:  # pragma: no cover - import is exercised at runtime
    from lint_skills import INLINE_BLOCKS  # noqa: E402
except ImportError:  # pragma: no cover
    INLINE_BLOCKS = ["deid", "kb-selection", "orchestration", "report-output", "attribution"]


def _repo_root() -> Path:
    """The repo root that owns template/blocks/* and scripts/lint_skills.py."""
    from lint_skills import REPO  # noqa: E402  - single source of truth

    return REPO


def _inner_marked(text: str, block: str):
    """The content STRICTLY BETWEEN the block's start/end markers, plus the marker
    spans so --sync can splice a canonical body back in place. Returns
    (inner, start_idx, end_idx) or None if the markers are absent."""
    m = re.search(
        rf"(<!-- hse:block:{re.escape(block)}:start -->)(.*?)(<!-- hse:block:{re.escape(block)}:end -->)",
        text,
        re.S,
    )
    if not m:
        return None
    # inner is group(2); the canonical splice replaces group(2) only, preserving the
    # exact marker comment lines and everything BELOW :end (roster/rows) untouched.
    return m.group(2), m.start(2), m.end(2)


def _canonical_inner(block: str, repo: Path) -> Optional[str]:
    """The canonical inner body of `block` from template/blocks/<block>.md.

    Block source files ship either marked or bare; mirror lint_skills._inner_region:
    if the file carries no markers, the whole file IS the bare body."""
    src = repo / "template" / "blocks" / f"{block}.md"
    if not src.is_file():
        return None
    raw = src.read_text(encoding="utf-8")
    m = re.search(
        rf"<!-- hse:block:{re.escape(block)}:start -->(.*?)<!-- hse:block:{re.escape(block)}:end -->",
        raw,
        re.S,
    )
    if m:
        return m.group(1)
    return raw if "hse:block:" not in raw else None


def sync_skill(skill_dir: Path, dry_run: bool = False, repo: Optional[Path] = None) -> int:
    """Heal block drift: re-copy each of the five canonical inline regions from
    template/blocks/* into the skill's in-marker regions, leaving everything BELOW
    each :end (roster, kb rows) untouched. Prints a unified diff of any change.

    `--dry-run` prints the diff and writes nothing. After a real write it re-lints
    and returns the lint exit code (0 only if the healed skill is clean). On a clean
    skill it is a no-op (no diff, write skipped) and returns the lint result. Touches
    ONLY in-marker invariant regions (T-04-04): author work below :end is never
    clobbered.
    """
    repo = repo or _repo_root()
    skill_dir = Path(skill_dir)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        print(f"ERROR  no SKILL.md in {skill_dir}", file=sys.stderr)
        return 2

    original = skill_md.read_text(encoding="utf-8")
    text = original
    changed = False

    # Splice from the LAST marker to the FIRST so earlier offsets stay valid as we
    # rewrite later regions in place.
    spans = []
    for block in INLINE_BLOCKS:
        found = _inner_marked(text, block)
        canonical = _canonical_inner(block, repo)
        if found is None or canonical is None:
            continue
        inner, start, end = found
        if inner != canonical:
            spans.append((start, end, canonical))
    for start, end, canonical in sorted(spans, key=lambda s: s[0], reverse=True):
        text = text[:start] + canonical + text[end:]
        changed = True

    if changed:
        diff = "".join(
            difflib.unified_diff(
                original.splitlines(keepends=True),
                text.splitlines(keepends=True),
                fromfile=f"{skill_dir.name}/SKILL.md (drifted)",
                tofile=f"{skill_dir.name}/SKILL.md (synced from template/blocks/*)",
            )
        )
        print(diff, end="")
        if dry_run:
            print(f"--sync --dry-run: {skill_dir.name} would be healed (nothing written).")
            return 0
        skill_md.write_text(text, encoding="utf-8")
        print(f"--sync: {skill_dir.name} block regions restored from template/blocks/*.")
    else:
        print(f"--sync: {skill_dir.name} already clean — no block drift (no-op).")

    # Re-lint after a real heal so a successful exit means the skill is genuinely clean.
    report = validate_skill(skill_dir, repo)
    for e in report.errors:
        print(f"ERROR  [{report.skill}] {e}", file=sys.stderr)
    return 1 if report.errors else 0


def main(argv: Optional[List[str]] = None) -> int:
    """CLI: pass-through to the linter, plus the `--sync` anti-drift verb.

        validate_repo_skill.py <skill>...            # lint (delegates to lint_skills.main)
        validate_repo_skill.py --sync <skill>        # heal block drift from template/blocks/*
        validate_repo_skill.py --sync --dry-run <s>  # preview the heal, write nothing
    """
    parser = argparse.ArgumentParser(
        description="Forge-side skill validator (re-export of lint_skills) + --sync drift healer."
    )
    parser.add_argument("skills", nargs="*", help="skill folder(s)")
    parser.add_argument("--sync", action="store_true", help="restore drifted inline blocks from template/blocks/*")
    parser.add_argument("--dry-run", action="store_true", help="with --sync: print the diff, write nothing")
    args, rest = parser.parse_known_args(argv)

    if args.sync:
        if not args.skills:
            parser.error("--sync requires at least one skill folder")
        rc = 0
        for s in args.skills:
            rc |= sync_skill(Path(s), dry_run=args.dry_run)
        return rc

    # Plain lint — delegate to the SAME linter CLI CI runs (no fork).
    return lint_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
