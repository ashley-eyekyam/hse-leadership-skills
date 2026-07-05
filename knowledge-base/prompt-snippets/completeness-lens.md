<!-- KB-SNIP-COMPLETENESS -->
# Omission lens — the shared completeness protocol

**Fragment ID:** `KB-SNIP-COMPLETENESS`
**This is the single-source omission-lens PROTOCOL.** Every skill's
`references/sme-review.md` carries an `## Omission lens` section that references THIS
fragment and adds ONLY skill-specific blind-spot hints + the mode floor — it never
restates the protocol (CONV-10 single source). The orchestration block's Step-4
MANDATE names this protocol; the `HSE-SME-Reviewer` archetype
(`KB-SNIP-ARCHETYPES`) runs it as its second pass.

> Source: v1.3 completeness contract (Phase 18, D-06/D-07) · Year: 2026 · Reviewed: 2026-07-05 · Volatile: false.

---

## When it runs

After the persona's conformance checklist (the first pass), the SAME Step-4 reviewer
runs ONE further, unconstrained pass — generative absence-listing FIRST, floor
reconciliation SECOND. The declared mode floor is a tripwire, not the search space:
the pass is free-form ("what would a competent [persona] have included for THIS
artifact mode that is ABSENT?"), then reconciled against the floor. On a
single-threaded host, the orchestration block's fallback runs this same pass inline.

## The protocol (must-list-then-refute)

1. **Detect the emitted mode.** Identify which mode (from the skill's
   `references/sme-review.md` `modes:` map) the artifact was actually produced in.
   If no declared mode matches what was emitted, flag the mismatch itself as a finding.
2. **List, unconstrained.** As the competent persona, enumerate everything a competent
   consultant would have included in THIS artifact mode for THIS task/site/asset —
   internally, BEFORE looking at the floor. Derive candidates from the skill's KB rows,
   jurisdiction triggers, and intake facets — never free-hand padding.
3. **Refute or confirm each candidate.** For every enumerated candidate: locate it in
   the artifact (confirmed present) or mark it a genuine omission. A candidate may be
   dropped ONLY by refuting it (present, or genuinely not applicable to this
   mode/task) — never by fatigue or brevity.
4. **Reconcile against the mode floor.** Classify every floor item three ways:
   covered by substantive content, covered by an honest `[GAP]` entry, or SILENTLY
   missing. Silent absence is the failure signature; an explicit `[GAP]` naming the
   item is the rewarded behaviour.
5. **Surface — never fabricate.** Every real miss becomes a `[GAP]` / deficiency-list
   entry naming the item. NEVER fabricate content (form-ids, figures, citations,
   clauses, thresholds) to fill a gap; route unresolved facts to a competent person.

## Bounded single-pass exit

Run the lens ONCE per review cycle. Do not loop it until it finds nothing — one
disciplined pass, findings handed to the orchestrator, done. (Re-running the whole SME
review after fixes is the Step-4 review loop's job, not the lens's.)

## Verbosity guard

Enumerate internally; surface only a SHORT deficiency note — the `[GAP]` /
deficiency list with item names and one-line reasons. Never pad the artifact or the
review with the full internal enumeration; verbosity cannot substitute for coverage
and cannot raise a score.
