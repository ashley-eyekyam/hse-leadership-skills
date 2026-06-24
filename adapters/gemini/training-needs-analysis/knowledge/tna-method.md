<!-- KB-SNIP-TNA-METHOD -->
# Training Needs Analysis — gap-scoring + prioritisation method

**Fragment ID:** `KB-SNIP-TNA-METHOD`
**This is prompt text, applied by the model — not a generator.** It is the method the
`training-needs-analysis` (#13) skill follows to score competence gaps and prioritise the
training plan. The competence banding it scores against is `KB-DATA-COMPETENCE-LEVELS`.

> Source: ISO 45001:2018 cl. 7.2 (competence) · systematic TNA practice (role-profiling → gap-scoring → prioritisation) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

1. **Profile the named roles.** For each role in scope (refuse "everyone" — require named
   roles + headcounts), derive its **required competencies** from job profile, the task's
   real hazards, and any **legal-required competency** (cite the regulatory source).
2. **Establish current state from evidence.** Band each role×competence cell's current level
   on `KB-DATA-COMPETENCE-LEVELS` (aware/trained/competent/expert) from a named evidence
   source — never assert a level without evidence.
3. **Score the gap** = required level − current level. A statutory competence requirement
   that is unmet is a gap against its named legal source and is **never** downgraded to pass.
4. **Flag single-points-of-failure** — a competence held by only one named person (report
   by role, not identity; small-cell discipline).
5. **Prioritise** by `gap size × (risk of the task it gates) × legal-mandate`. Statutory and
   high-hazard competence gaps rank first.
6. **Plan as SMART actions** (`smart_actions`) with named owners + due dates. Training is an
   **administrative control** — never present "more training" as the sole treatment of a
   hazard that admits a higher-order control (`KB-SNIP-HOC`).

## Output expectation

A role×competence gap matrix (scored, evidence-traced), a single-point-of-failure register,
a certification/expiry tracker, and a prioritised costed training plan with owners/dates.
Feeds the eval `specificity`, `hierarchy_of_controls`, and `regulatory_citation_accuracy`
dimensions.
