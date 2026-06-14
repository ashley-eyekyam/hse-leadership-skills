"""scripts/sme_review.py — the automated HSE-SME-persona pre-human review (A8 §4.5).

A read-only adversarial pass that runs the **HSE-SME-Reviewer** persona
(`knowledge-base/prompt-snippets/subagent-archetypes.md` — the cross-cutting
KB-SNIP-ARCHETYPES hook authored in Plan 01) over a finished skill artifact and
attaches a findings list. Each finding is a **FLAG, never a block**.

Two enforcement classes — KEPT DISTINCT (the core governance invariant, T-03-19):

  1. THIS module (the FLAG class):    decision-support; recorded-as-ran; a FLAG
     surfaces to the human reviewer but NEVER self-blocks. main() ALWAYS exits 0.
  2. run_evals.py (the HARD-BLOCK class): the deterministic de-id leak / invented
     citation / weighted-<4.0 hard blocks that DO fail the gate. Those live in
     run_evals.py + scripts/graders/, NOT here.

The mechanical realisation of "decision-support that PRECEDES — never replaces,
never emits — the competent-person sign-off" (SME-02 / SME-03 / QA-05). This
module MUST NOT emit "approved by a competent person" or any human sign-off; it
only reads, flags, and records that the review ran.

Stdlib only. Runnable under `python3` with no model call (the regulator-survival
heuristics are deterministic text checks; the runtime persona pass is the LLM
sibling described in the archetype, invoked inside a running skill — this CI
module is its recorded-as-ran shadow).

CLI:
    python sme_review.py <artifact-path> [--json] [--out findings.json]
    python sme_review.py --text "<artifact text>" [--json]

Exit code is ALWAYS 0 — even when the findings include a FLAG (QA-05).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# The persona never emits any of these — asserting their ABSENCE is the SME-02
# boundary (this module is decision-support, it never signs off).
SIGN_OFF_FORBIDDEN = (
    "approved by a competent person",
    "competent-person sign-off",
    "competent person sign-off",
    "signed off by a competent person",
    "reviewed and approved",
)

# Marker strings a downstream consumer / CI log can grep for to confirm the
# review actually RAN (SME-03: no skill merges without a recorded SME pass).
REVIEW_RAN_MARKER = "hse-sme-review: ran"
VERDICT_PASS = "PASS"
VERDICT_FLAG = "FLAG"


# --- the HSE-SME-Reviewer defensibility checklist (archetype "Returns" list) ---
# Each check returns zero or more FLAG findings. None of these blocks; they are
# the "would this survive a regulator's challenge?" surfacing.

def _check_generic_controls(text: str) -> List[str]:
    """Generic, non-task/site/asset-specific controls (the core anti-pattern)."""
    findings: List[str] = []
    generic = re.findall(
        r"(?im)^\s*[-*\d.]*\s*(?:ensure|implement|use|maintain|provide|follow)\s+"
        r"(?:appropriate|adequate|suitable|proper|good|safe)\s+"
        r"(?:controls?|measures?|procedures?|practices?|precautions?)\b.*$",
        text,
    )
    for line in generic:
        findings.append(
            "generic control (not specific to the named task/site/asset): "
            + line.strip()[:120]
        )
    return findings


def _check_ppe_admin_only(text: str) -> List[str]:
    """PPE/admin-only treatment with no higher-order control justified/escalated."""
    findings: List[str] = []
    # Lines that treat a hazard with PPE or administration alone.
    for m in re.finditer(
        r"(?im)^.*\b(?:controlled|mitigated|managed|addressed)\b.*\b"
        r"(?:ppe|personal protective equipment|training|signage|toolbox talk|"
        r"administrative control)s?\b.*$",
        text,
    ):
        line = m.group(0).strip()
        # Only flag when NO higher-order control word co-occurs on the line.
        if not re.search(
            r"(?i)\b(elimination|eliminate|substitut|engineer|isolat|guard|"
            r"ventilat|interlock)\w*\b",
            line,
        ):
            findings.append("PPE/admin-only treatment (no higher-order control "
                            "justified or escalated): " + line[:120])
    return findings


def _check_unnamed_owners(text: str) -> List[str]:
    """Actions/controls with no named accountable owner.

    Operates per blank-line-delimited BLOCK (not per physical line) so an
    "Owner:" cue on the line following the "Action:"/"Control:" header still
    satisfies the check — real artifacts wrap the owner onto its own line.
    """
    findings: List[str] = []
    owner_cue = re.compile(
        r"(?i)\b(owner|responsible|assigned to|accountable)\b\s*[:\-]")
    block_header = re.compile(
        r"(?im)^\s*[-*\d.]*\s*(action|control|corrective action|capa)\b[:\-]?\s*(.+)$")
    for block in re.split(r"\n\s*\n", text):
        m = block_header.search(block)
        if not m:
            continue
        if not owner_cue.search(block):
            header_line = m.group(0).strip()
            findings.append("un-named owner (no named accountable owner): "
                            + header_line[:120])
    return findings


def _check_missing_review_triggers(text: str) -> List[str]:
    """Controls with no review date / no re-assessment trigger."""
    findings: List[str] = []
    has_control = re.search(r"(?im)^\s*[-*\d.]*\s*control\b", text)
    has_review = re.search(
        r"(?i)\b(review date|re-?assess(?:ment)?|review trigger|next review|"
        r"review by|valid until)\b",
        text,
    )
    if has_control and not has_review:
        findings.append("missing review trigger (a control with no review date / "
                        "re-assessment trigger)")
    return findings


def _check_unevidenced_claims(text: str) -> List[str]:
    """Conclusions not traced to a cited source (source + year)."""
    findings: List[str] = []
    for m in re.finditer(
        r"(?im)^\s*[-*\d.]*\s*(?:conclusion|finding|root cause|determination)\b[:\-]?\s*(.+)$",
        text,
    ):
        line = m.group(0).strip()
        # An evidence cue: a 4-digit year, "per", "see", "(...)" citation form.
        if not re.search(r"(?:\b(?:19|20)\d{2}\b|\bper\b|\bsee\b|\bsource\b)", line, re.I):
            findings.append("un-evidenced claim (conclusion not traced to a cited "
                            "source + year): " + line[:120])
    return findings


_CHECKS = (
    _check_generic_controls,
    _check_ppe_admin_only,
    _check_unnamed_owners,
    _check_missing_review_triggers,
    _check_unevidenced_claims,
)


def review(text: str) -> Dict[str, Any]:
    """Run the HSE-SME-Reviewer defensibility checklist over `text`.

    Returns a record with:
      - review_ran: True (always — the review RAN; SME-03)
      - verdict: "PASS" | "FLAG" (a FLAG is decision-support, never a block)
      - findings: list[str]
      - sign_off: None (this module NEVER signs off — SME-02 boundary)

    NOTE: a FLAG verdict does NOT change the exit code. main() always returns 0.
    """
    findings: List[str] = []
    for check in _CHECKS:
        findings.extend(check(text))

    return {
        "review_ran": True,
        "marker": REVIEW_RAN_MARKER,
        "verdict": VERDICT_FLAG if findings else VERDICT_PASS,
        "findings": findings,
        # Explicitly None: the SME-persona review is decision-support and PRECEDES
        # — never replaces, never emits — the human competent-person sign-off.
        "sign_off": None,
    }


def _render_human(record: Dict[str, Any]) -> str:
    lines = [REVIEW_RAN_MARKER,
             f"verdict: {record['verdict']} "
             f"({'decision-support FLAG — NOT a merge block' if record['verdict'] == VERDICT_FLAG else 'no findings'})"]
    if record["findings"]:
        lines.append(f"findings ({len(record['findings'])}):")
        lines.extend(f"  - [FLAG] {f}" for f in record["findings"])
    lines.append("(decision-support only — precedes, never replaces, the human "
                 "competent-person review)")
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Automated HSE-SME-persona pre-human review (A8 §4.5). "
                    "Records the review ran + attaches FLAG findings; ALWAYS "
                    "exits 0 — a FLAG NEVER self-blocks (QA-05).")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("artifact", nargs="?", help="path to the artifact to review")
    src.add_argument("--text", help="artifact text passed inline (testing/CI)")
    p.add_argument("--json", action="store_true", help="emit the record as JSON")
    p.add_argument("--out", default=None, help="write the findings record here")
    args = p.parse_args(argv)

    if args.text is not None:
        text = args.text
    else:
        text = Path(args.artifact).read_text(encoding="utf-8")

    record = review(text)

    if args.out:
        Path(args.out).write_text(json.dumps(record, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(record, indent=2))
    else:
        print(_render_human(record))

    # ALWAYS 0 — a FLAG is recorded-as-ran decision-support, never a merge block
    # (SME-03 / QA-05). The deterministic hard blocks live in run_evals.py.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
