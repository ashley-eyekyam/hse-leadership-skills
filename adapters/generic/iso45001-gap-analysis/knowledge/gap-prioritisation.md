<!-- KB-SNIP-GAP-PRIORITISATION -->
# Gap prioritisation — severity × certification-blocking

**Fragment ID:** `KB-SNIP-GAP-PRIORITISATION`
**This is prompt text, applied by the model — not a generator.** It is the method the
`iso45001-gap-analysis` (#19) skill uses to order its costed remediation roadmap. Clause
conformance is scored on `KB-DATA-ISO45001-MATURITY`.

> Source: ISO 45001:2018 (clause set 4-10) · ISO/IEC 17021-1 (certification readiness) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

1. **Score every clause** on `KB-DATA-ISO45001-MATURITY` (0–4) from the supplied evidence;
   a clause with no evidence is a scored gap, not silently omitted. Mark any clause **N/A
   only with a stated reason**. Omitting a clause (e.g. 6.1.2 hazard-id) fails the analysis
   (#19 eval case 1).
2. **Classify each gap** on two axes:
   - **Severity** = (required − current maturity) × the risk the clause governs.
   - **Certification-blocking** = is this a mandatory clause sitting at level ≤ 2? A missing
     documented OH&S policy (5.2), hazard-id (6.1.2), internal audit (9.2) or
     incident/nonconformity (10.2) is a **blocker**, not a minor gap (#19 eval case 2 —
     `regulatory_citation_accuracy` hard-fail).
3. **Prioritise** = certification-blockers first (ordered by severity), then high-severity
   non-blockers, then the remainder. Every gap traces to its **clause + a named owner**.
4. **Cost & date** the roadmap as SMART actions (`smart_actions`) — owners + due dates;
   controls in the planning clauses ranked via `KB-SNIP-HOC`.

## Output expectation

A clause-by-clause conformance score, a gap register, explicit certification-blocker flags,
and a prioritised costed remediation roadmap. Feeds `specificity`, `defensibility`,
`regulatory_citation_accuracy`.
