# Methodology — ISO 22301 business continuity plan (BIA → MTPD → RTO/RPO → strategy → plan)

The domain method this skill applies. It is **prompt method, not a generator**: the BIA and
the RTO/RPO derivation are a structured method over the duty-holder's own inputs, and the
**RTO < MTPD rule is a checklist constraint** (`references/QUALITY_CHECKLIST.md`), not a
deterministic engine. The canonical method fragment is **`KB-SNIP-BIA-METHOD`**; the banding
+ margin discipline is **`KB-DATA-RTO-RPO-GUIDANCE`**; the clause structure is
**`KB-STD-ISO22301`** (clauses 8.2.2 / 8.2.3 / 8.3 / 8.4 / 8.5). Recovery actions and the
exercise schedule are **`smart_actions`** (named owners + ISO dates).

## The method

0. **De-identify the inputs first** (the `deid` block + the De-identifier-runs-first
   orchestration rule). Recovery roles legitimately name individuals, but a recovery-role
   holder's **home address or medical note** is scrubbed/role-labelled before anything
   downstream consumes the text.

1. **Identify critical activities + their outputs (ISO 22301 8.2.2).** From intake Q2, list
   the **time-critical activities** and what each must keep producing. **Refuse a generic
   scope** — "the whole company" with no named function is rejected (the specificity anchor).

2. **Map impact over time → derive the MTPD.** For each critical activity, describe how the
   impact of its loss **grows with time** (financial, regulatory, reputational, safety). The
   point at which impact becomes **unacceptable** is the **MTPD (Maximum Tolerable Period of
   Disruption)** — derived from the curve, never asserted.

3. **Capture dependencies.** For each activity, name every dependency — **people · IT/systems
   · suppliers · premises · equipment**. A single-point dependency (e.g. one supplier, one
   key person) is flagged here so the strategy step must cover it. Flag `[GAP]` where a
   dependency is unknown — never invent one.

4. **Derive recovery objectives (8.2.2, `KB-DATA-RTO-RPO-GUIDANCE`).** Per critical activity:
   - State the **MTPD first** (from step 2).
   - Set the **RTO strictly inside the MTPD, with a stated margin** — *RTO < MTPD*. An RTO
     asserted with **no MTPD basis**, or an **RTO ≥ MTPD**, is **invalid** (a
     `regulatory_citation_accuracy` hard-fail on ISO 22301 8.2.2).
   - Set the **RPO** from the activity's data/transaction-loss tolerance and backup cadence.

5. **Risk assessment of the prioritised activities (8.2.3).** Identify the threats to the
   time-critical activities (the disruption scenarios from intake Q3); rank them so the
   highest-impact / least-tolerable disruptions drive the strategy.

6. **Select continuity strategies (8.3) — covering every dependency.** For each activity,
   choose a strategy that **meets its RTO/RPO and covers every stated dependency** (e.g. a
   second qualified supplier for a single-supplier dependency, cross-training for a key-person
   dependency, warm/hot standby for an IT dependency). A strategy that **ignores a stated
   dependency is a defect** the Critic/QA pass must catch. Rank any **preventive** control via
   `KB-SNIP-HOC` (eliminate the single point of failure before merely mitigating it).

7. **Document the plan & recovery roles (8.4).** Assemble the plan: **recovery roles each
   with a named deputy** (no single point of failure in the response itself), the activation/
   stand-down triggers, and the review cycle. Carry a **one-line cross-reference to
   `emergency-response-plan`** for the immediate incident-response leg (muster, evacuation,
   scenario procedures) — BCP complements, never duplicates, the ERP (D-07).

8. **Exercise / test programme (8.5).** Produce an **exercise/test schedule** as
   `smart_actions` (specific, measurable, **assignable (named owner/role)**, relevant,
   **time-bound (ISO due date)**); an untested plan is recorded as `[GAP]`, never assumed
   adequate.

9. **Validate against `references/QUALITY_CHECKLIST.md`** — every critical activity has an
   RTO under a stated MTPD + an RPO; strategies cover the dependencies; recovery roles have
   deputies; an exercise schedule exists; every citation traces to `KB-STD-ISO22301`; de-id
   applied. Then assemble the branded report (`assets/business-continuity-plan-report.template.json`)
   and run the canonical `report-output` call.

## Evidence discipline

Every MTPD, RTO, RPO and strategy traces to the BIA input it came from (the activity, its
impact-over-time, its dependency). The duty-holder's BIA supplies the values — this skill
supplies the **method, the RTO < MTPD discipline, and the dependency-coverage check**, never
invented recovery times.
