#!/usr/bin/env python3
"""stamp_rubric.py — byte-canonical rubric re-stamp + drift-check (v1.3 FND-03).

template/evals/rubric.yaml is the ONE canonical HSE eval rubric; every
skills/*/evals/rubric.yaml is meant to be a byte-identical copy. Before this
tool existed there was NO re-stamp mechanism (Phase-18 RESEARCH §3): the forge
copies the rubric only at scaffold time (scaffold.py shutil.copyfile) and
sync_skill() heals the five inline blocks only — so a template edit silently
left every existing skill copy stale. This CLI closes that gap, cloning the
proven gen_marketplace.py --check/--write drift-gate shape.

Usage:
  python3 scripts/stamp_rubric.py --write   # copy template bytes over every target
  python3 scripts/stamp_rubric.py --check   # unified diff + exit 1 on any drift
  python3 scripts/stamp_rubric.py           # same as --check (safe default)

EXCLUSIONS (D-21 — the only legitimate outliers):
  * any path under examples/            (the frozen examples/risk-assessment
                                         rubric is deliberately NOT re-stamped)
  * any path under skills/hse-skill-forge/  (forge-owned; never re-stamped here)

Stdlib only — the stamp is a byte copy; no YAML parsing needed.
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path
from typing import List, Optional

REPO = Path(__file__).resolve().parent.parent
TEMPLATE_REL = Path("template") / "evals" / "rubric.yaml"

# Skill directories under skills/ that are NEVER re-stamped (D-21).
EXCLUDED_SKILL_DIRS = frozenset({"hse-skill-forge"})


def iter_targets(repo: Path) -> List[Path]:
    """Every skills/*/evals/rubric.yaml that must equal the template, sorted.

    Excludes skills/hse-skill-forge/** and (belt-and-braces — examples/ lives
    at the repo top level, outside skills/) any path containing an examples/
    segment.
    """
    targets: List[Path] = []
    for path in sorted((repo / "skills").glob("*/evals/rubric.yaml")):
        if "examples" in path.parts:
            continue
        skill_dir = path.parent.parent.name
        if skill_dir in EXCLUDED_SKILL_DIRS:
            continue
        targets.append(path)
    return targets


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Re-stamp / drift-check the byte-canonical HSE rubric "
                    "(template/evals/rubric.yaml -> skills/*/evals/rubric.yaml)."
    )
    g = p.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true",
                   help="diff every skill copy against the template; nonzero on drift")
    g.add_argument("--write", action="store_true",
                   help="overwrite every skill copy with the template bytes")
    p.add_argument("--repo", default=str(REPO), help="repo root (default: inferred)")
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()

    template = repo / TEMPLATE_REL
    if not template.is_file():
        print(f"ERROR: canonical template not found: {template}", file=sys.stderr)
        return 2
    canonical = template.read_bytes()

    targets = iter_targets(repo)
    if not targets:
        print("ERROR: no skills/*/evals/rubric.yaml targets found "
              "(wrong --repo root?)", file=sys.stderr)
        return 2

    if args.write:
        wrote = 0
        for t in targets:
            if t.read_bytes() != canonical:
                t.write_bytes(canonical)
                wrote += 1
        print(f"WROTE {wrote}/{len(targets)} skill rubric copies "
              f"(the rest were already byte-identical)")
        return 0

    # --check (default): per-file unified diff on drift, exit 1 if any.
    drift = False
    for t in targets:
        on_disk = t.read_bytes()
        if on_disk == canonical:
            continue
        drift = True
        rel = t.relative_to(repo)
        print(f"DRIFT: {rel} differs from the template; "
              f"run `scripts/stamp_rubric.py --write`", file=sys.stderr)
        for line in difflib.unified_diff(
            on_disk.decode("utf-8", errors="replace").splitlines(),
            canonical.decode("utf-8", errors="replace").splitlines(),
            fromfile=f"{rel} (on disk)",
            tofile=f"{TEMPLATE_REL} (canonical)",
            lineterm="",
        ):
            print(line, file=sys.stderr)
    if not drift:
        print(f"OK: {len(targets)} skill rubric copies byte-identical to "
              f"{TEMPLATE_REL}")
    return 1 if drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
