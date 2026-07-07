"""graders/completeness.py — the deterministic completeness-coverage grader (FND-04).

The FIRST reported-only grader in the deterministic class (D-18): it measures
mode-keyed floor coverage of a produced output against the skill's
`references/sme-review.md` `modes:` map and NEVER contributes to `hard_fail`
(unlike grade_deid / grade_citation). Its record is the ONLY completeness
enforcement for the six D-11 POLICY_SENSITIVE_GRADER_EXEMPT skills, whose model
grade is skipped — so it must run for EVERY skill and must be crash-proof.

Three-way split per floor item (D-10 anchor matching / D-11 honest-gap credit):

    covered_by_content — any anchor matches the output OUTSIDE a gap segment;
    covered_by_gap     — a literal ``[GAP`` marker line NAMES the item (its id,
                         or one of the item's OWN anchors) — honest surfacing
                         is COVERED, never pressured toward a FILL;
    missing            — silently absent.

    coverage_pct = (covered_by_content + covered_by_gap) / floor_total

Safety (T-18-01-01 / T-18-01-02): author-supplied anchors are UNTRUSTED regex —
each is compiled ONCE per invocation inside try/except re.error with a defensive
length cap; a bad anchor degrades its item toward `missing` with a logged reason
and NEVER raises. Malformed `modes:` YAML / a modeless skill / a case with no
`mode:` key is the back-compat no-op ``{"scored": False, "reason": "no modes
declared"}`` so the 94 shipped skills stay green under WARN.

Stdlib + pyyaml only — keyless, no model subprocess, no API key (D-03/D-12).
The `modes:` frontmatter is parsed via the linter's shared `_split_frontmatter`
(one parser, no second YAML reader). The CLI is reported-only by default; under
`--gate` (the Phase-20 HARD cutover, D-01) it exits 1 on any missing floor item.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Pattern, Tuple

# scripts/ on sys.path so `import lint_skills` resolves the shared module
# whatever the invoking cwd (run_evals.py imports the same way).
_SCRIPTS = Path(__file__).resolve().parent.parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from lint_skills import _read, _split_frontmatter  # the SHARED frontmatter parser

REPO = _SCRIPTS.parent

# The pack's established honest-gap convention: a literal "[GAP" marker.
_GAP_MARK = "[GAP"

# Defensive cap on author-anchor length before compiling (ReDoS hygiene —
# T-18-01-01). Anchors are short content phrases; anything longer is rejected
# as non-matching with a logged reason, never compiled.
_MAX_ANCHOR_LEN = 512

def _compile_anchor(anchor: Any) -> Optional[Pattern[str]]:
    """Compile ONE untrusted author anchor case-insensitively (D-10).

    Returns None (a non-matching sentinel) on any non-string / over-long /
    un-compilable anchor — the caller logs a reason; the grader NEVER raises
    re.error into the WARN sweep (T-18-01-01)."""
    if not isinstance(anchor, str) or not anchor:
        return None
    if len(anchor) > _MAX_ANCHOR_LEN:
        return None
    try:
        return re.compile(anchor, re.IGNORECASE)
    except re.error:
        return None


def _split_gap_segments(text: str) -> Tuple[List[str], str]:
    """Split output text into (gap_segment_lines, non_gap_text).

    A gap segment is any line carrying the literal gap marker. Anchor matches
    inside gap segments do NOT count as content coverage; a gap segment that
    names an item yields covered_by_gap."""
    gap_lines: List[str] = []
    non_gap_lines: List[str] = []
    for line in text.splitlines():
        (gap_lines if _GAP_MARK in line else non_gap_lines).append(line)
    return gap_lines, "\n".join(non_gap_lines)


def _gap_names_item(
    gap_lines: List[str], item_id: str, anchors_compiled: List[Pattern[str]],
) -> bool:
    """True when a literal gap-marker line NAMES this specific item — its id
    (case-insensitive substring) or one of the item's OWN compiled anchors
    (D-11: honest surfacing counts as covered_by_gap).

    Gap-credit is bound to the item's OWN identity, NEVER generic word overlap
    with the item description: a ``[GAP]`` line honestly naming item A must not
    credit a silently-absent item B that merely shares a common English word
    (18-REVIEW CR-01 — silent absence masked as honest surfacing would invert
    the contract's core signal)."""
    id_low = (item_id or "").lower()
    for line in gap_lines:
        if id_low and id_low in line.lower():
            return True
        if any(rx.search(line) for rx in anchors_compiled):
            return True
    return False


def grade_completeness(output_text: str, sme_review_path: Path, mode: str) -> Dict:
    """Deterministic reported-only completeness grader (FND-04). Returns::

        {"scored": bool, "mode": str, "floor_total": int,
         "covered_by_content": [ids], "covered_by_gap": [ids], "missing": [ids],
         "coverage_pct": float, "reasons": [str, ...], "error": str|None}

    Back-compat no-op (Pitfall 4): a skill with no ``modes:`` map (or an
    absent/unreadable ``sme-review.md``) OR a case with no ``mode:`` key returns
    ``{"scored": False, "reason": "no modes declared", ...}``. A mode absent
    from the skill's ``modes:`` map records ``error`` with ``scored: False``.
    NEVER raises on untrusted author input; NEVER contributes to hard_fail."""
    text = output_text or ""
    result: Dict[str, Any] = {
        "scored": False,
        "mode": mode or "",
        "floor_total": 0,
        "covered_by_content": [],
        "covered_by_gap": [],
        "missing": [],
        "coverage_pct": 0.0,
        "reasons": [],
        "error": None,
    }

    # --- load the modes: map (defensive at every step — T-18-01-02) ------------
    try:
        path = Path(sme_review_path) if sme_review_path else None
        if path is None or not path.is_file():
            result["reason"] = "no modes declared"
            return result
        fm, _body = _split_frontmatter(_read(path))
    except Exception as exc:  # unreadable file — never crash the sweep
        result["reason"] = "no modes declared"
        result["error"] = f"unreadable sme-review.md ({exc})"
        return result

    modes = fm.get("modes") if isinstance(fm, dict) else None
    if not isinstance(modes, dict) or not modes:
        result["reason"] = "no modes declared"
        return result
    if not mode:
        # The eval case declares no mode: back-compat no-op (Pitfall 4).
        result["reason"] = "no modes declared"
        return result

    entry = modes.get(mode)
    if not isinstance(entry, dict):
        result["error"] = (
            f"mode {mode!r} is absent from the skill's modes: map "
            f"(declared: {sorted(str(k) for k in modes)})"
        )
        return result

    floor = entry.get("floor")
    if not isinstance(floor, list) or not floor:
        result["error"] = f"mode {mode!r} declares no floor items"
        return result

    # --- three-way split over the floor (D-10 / D-11) --------------------------
    result["scored"] = True
    result["floor_total"] = len(floor)
    gap_lines, non_gap_text = _split_gap_segments(text)

    for idx, item in enumerate(floor):
        if not isinstance(item, dict):
            item_id = f"item-{idx + 1}"
            result["missing"].append(item_id)
            result["reasons"].append(
                f"{item_id}: floor item is not a mapping — treated as missing")
            continue
        item_id = str(item.get("id") or f"item-{idx + 1}")
        raw_anchors = item.get("anchors")
        raw_anchors = raw_anchors if isinstance(raw_anchors, list) else []
        raw_min = item.get("min_matches", 1)
        min_matches = raw_min if isinstance(raw_min, int) and raw_min >= 1 else 1

        compiled: List[Pattern[str]] = []
        for anchor in raw_anchors:
            rx = _compile_anchor(anchor)
            if rx is None:
                result["reasons"].append(
                    f"{item_id}: anchor {str(anchor)[:80]!r} did not compile as a "
                    f"case-insensitive regex (or exceeded the {_MAX_ANCHOR_LEN}-char "
                    f"cap) — treated as non-matching")
            else:
                compiled.append(rx)
        if not raw_anchors:
            result["reasons"].append(f"{item_id}: no anchors declared")

        # Anchor hits OUTSIDE gap segments = content coverage (D-10 any-match;
        # min_matches counts DISTINCT matching anchors, default 1).
        content_hits = sum(1 for rx in compiled if rx.search(non_gap_text))
        if compiled and content_hits >= min_matches:
            result["covered_by_content"].append(item_id)
        elif _gap_names_item(gap_lines, item_id, compiled):
            result["covered_by_gap"].append(item_id)
        else:
            result["missing"].append(item_id)

    covered = len(result["covered_by_content"]) + len(result["covered_by_gap"])
    result["coverage_pct"] = covered / result["floor_total"]
    return result


# --- thin keyless CLI (CI gating step — D-01; --gate exits 1 on any miss) -------

def _iter_skill_dirs(repo: Path) -> List[Path]:
    """Every skill dir under skills/ carrying an evals/evals.json (nested-safe)."""
    found: List[Path] = []
    root = repo / "skills"
    if root.is_dir():
        for child in sorted(root.rglob("evals/evals.json")):
            found.append(child.parent.parent)
    return found


def _golden_mode_and_output(skill_dir: Path) -> Tuple[Optional[str], str]:
    """Resolve the skill's golden mode from evals.json: the FIRST case bearing a
    ``mode:`` key wins; its pre-captured output artifact text is returned for
    grading. (None, "") when no case declares a mode — the grader then no-ops."""
    evals_path = skill_dir / "evals" / "evals.json"
    try:
        data = json.loads(evals_path.read_text(encoding="utf-8"))
    except Exception:
        return None, ""
    for case in data.get("evals", []) or []:
        if not isinstance(case, dict):
            continue
        mode = case.get("mode")
        if not mode:
            continue
        parts: List[str] = []
        inline = case.get("output")
        if isinstance(inline, str) and inline.strip():
            parts.append(inline)
        for rel in case.get("output_files", []) or []:
            candidate = skill_dir / rel
            try:
                if candidate.is_file():
                    parts.append(candidate.read_text(encoding="utf-8"))
            except OSError:
                pass
        return str(mode), "\n".join(parts)
    return None, ""


def _fmt_row(cols: List[str], widths: List[int]) -> str:
    return "  ".join(c.ljust(w) for c, w in zip(cols, widths)).rstrip()


def main(argv: Optional[List[str]] = None) -> int:
    """Keyless coverage-table CLI. Prints the coverage table always; under
    ``--gate`` (the Phase-20 HARD cutover, D-01) exits 1 if ANY scored skill has
    missing floor items, else 0. Without ``--gate`` it stays reported-only and
    exits 0 (back-compat)."""
    p = argparse.ArgumentParser(
        description="Deterministic completeness coverage (keyless, no model call). "
                    "Reported-only by default; with --gate, exits 1 on any missing "
                    "floor item (Phase-20 HARD cutover, D-01).")
    p.add_argument("--all", action="store_true",
                   help="grade every skill under skills/ (golden mode from evals.json)")
    p.add_argument("--skill", default=None,
                   help="grade one skill by directory name")
    p.add_argument("--gate", action="store_true",
                   help="HARD gate: exit 1 if any scored skill has missing floor "
                        "items (D-01); the coverage table still prints (GATE-05)")
    args = p.parse_args(argv)

    targets: List[Path]
    if args.skill:
        targets = [d for d in _iter_skill_dirs(REPO) if d.name == args.skill]
        if not targets:
            print(f"WARN: no skill dir named {args.skill!r} under skills/")
            return 0
    elif args.all:
        targets = _iter_skill_dirs(REPO)
    else:
        p.print_help()
        return 0

    widths = [42, 16, 6, 8, 4, 8, 9]
    print(_fmt_row(["skill", "mode", "floor", "content", "gap", "missing",
                    "coverage"], widths))
    print(_fmt_row(["-" * w for w in widths], widths))
    scored_count = 0
    missing_total = 0
    skills_with_missing: List[str] = []
    for skill_dir in targets:
        sme = skill_dir / "references" / "sme-review.md"
        try:
            mode, out_text = _golden_mode_and_output(skill_dir)
            verdict = grade_completeness(out_text, sme, mode or "")
        except Exception as exc:  # belt-and-braces: the sweep never crashes
            print(_fmt_row([skill_dir.name, "-", "-", "-", "-", "-",
                            f"error: {exc}"], widths))
            continue
        if verdict["scored"]:
            scored_count += 1
            n_missing = len(verdict["missing"])
            if n_missing:
                missing_total += n_missing
                skills_with_missing.append(skill_dir.name)
            print(_fmt_row([
                skill_dir.name, verdict["mode"], str(verdict["floor_total"]),
                str(len(verdict["covered_by_content"])),
                str(len(verdict["covered_by_gap"])),
                str(n_missing),
                f"{verdict['coverage_pct']:.0%}",
            ], widths))
            for reason in verdict["reasons"]:
                print(f"    note: {reason}")
        else:
            note = verdict.get("error") or verdict.get("reason", "not scored")
            print(_fmt_row([skill_dir.name, "-", "-", "-", "-", "-", note], widths))

    gated = " (HARD gate — D-01)" if args.gate else " (reported-only)"
    print(f"\ncompleteness coverage: {scored_count}/{len(targets)} skill(s) scored"
          f"{gated}; {missing_total} missing floor item(s) across "
          f"{len(skills_with_missing)} skill(s).")

    if args.gate and missing_total > 0:
        print("FAIL: completeness floor coverage incomplete — missing items in: "
              + ", ".join(skills_with_missing))
        return 1  # HARD gate (D-01): any missing floor item fails the CI lint step
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
