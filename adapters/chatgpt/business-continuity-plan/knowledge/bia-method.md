<!-- KB-SNIP-BIA-METHOD -->
# BIA method — BIA → MTPD → RTO/RPO derivation

**Fragment ID:** `KB-SNIP-BIA-METHOD`
**This is prompt text, applied by the model — not a generator.** It is the method the
`business-continuity-plan` (#26) skill follows to run the Business Impact Analysis and derive
recovery objectives. The banding + the RTO<MTPD margin discipline are in
`KB-DATA-RTO-RPO-GUIDANCE`; the clause structure is `KB-STD-ISO22301`.

> Source: ISO 22301:2019 cl. 8.2.2 (BIA) / 8.2.3 (risk assessment) / 8.3 (BC strategies) / 8.4 (plans) / 8.5 (exercise) · ISO 22313:2020 (guidance) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

1. **Identify critical activities** (refuse a generic scope) and their **outputs** — what the
   organisation must keep doing.
2. **Map impact over time.** For each activity, how does the impact of its loss grow with
   time? This curve yields the **MTPD** (the point impact becomes unacceptable).
3. **Capture dependencies** — people, IT/systems, suppliers, premises, equipment. A strategy
   that ignores a stated dependency (e.g. a single supplier) is flagged (#26 eval case 2).
4. **Derive recovery objectives** (`KB-DATA-RTO-RPO-GUIDANCE`):
   - **RTO < MTPD**, with a stated margin — an RTO asserted with no MTPD basis, or RTO ≥
     MTPD, is invalid (#26 eval case 1 — `regulatory_citation_accuracy` hard-fail on 8.2.2).
   - **RPO** from the activity's data-loss tolerance.
5. **Select continuity strategies** covering every dependency, with preventive controls
   ranked via `KB-SNIP-HOC` where applicable.
6. **Document the plan** — recovery roles **each with a deputy**, an exercise/test schedule
   (`smart_actions`, owners/dates), and a one-line cross-reference to `emergency-response-plan`
   (#15) for the incident response (BCP complements, does not duplicate, the ERP).

## Output expectation

A BIA (activities / impact-over-time / dependencies), recovery objectives (MTPD/RTO/RPO per
activity), continuity strategies, recovery roles with deputies, and an exercise schedule.
Feeds `specificity`, `defensibility`, `regulatory_citation_accuracy`.
