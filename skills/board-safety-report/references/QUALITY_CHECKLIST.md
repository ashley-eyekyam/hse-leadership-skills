# Pre-output Quality Checklist — board safety report

Validate the draft against this gate before producing any output. This is the
self-check the Workflow's step 7 runs and the Critic/QA pass enforces.

## De-identification & aggregation (hard — a leak is an auto-fail)

- [ ] The de-identifier ran FIRST, before any analysis.
- [ ] No individual incident, injured party, or person is identifiable — key events and
      HiPo/SIF are **aggregated** (counts and categories, not anecdotes with date +
      location + injury detail).
- [ ] No injury/illness category with **fewer than 5** individuals is published;
      secondary suppression applied so a <5 cell can't be back-calculated.
- [ ] No re-identification key (and no name↔label mapping) anywhere in the report.

## Exec narrative, not data dump (the core lever)

- [ ] The report **leads with an executive narrative** — what changed / why it matters
      / what leadership must decide — not an indicator table.
- [ ] **Every figure surfaced carries a narrative reading** (a trend or benchmark
      interpretation); no naked table stands as the deliverable.
- [ ] The strategic-actions section frames **board-level decisions** (resource / policy
      / accountability), not operational CAPA tasks.

## HiPo / SIF lens (D-01)

- [ ] The HiPo/SIF lens is **present AND interpreted** — what the pattern reveals about
      exposure and where the next serious event is most likely — not merely a list.

## Benchmarks & figures (defensibility)

- [ ] Every benchmark carries its **source + year** (from `KB-DATA-TRIR-BENCHMARKS` or
      a user-stated source); no unsourced "industry average"; an absent benchmark is
      `[GAP]`, never invented.
- [ ] Rates come from `incident_rates` (computed only when hours + counts present, or a
      pre-computed input / `[GAP]`); the Narrative-Drafter changed no figure.
- [ ] Trends are computed against the **stated prior period**; absent → `[GAP]`.

## Grounding & traceability

- [ ] Grounded in ISO 45001 **9.1** (indicators) and **9.3** (management review).
- [ ] The optional ISO 14001 9.1.2 environmental line appears **only** when env metrics
      were supplied (D-02) — a single line, not a full ESG branch.
- [ ] Every claim traces to an input or is flagged `[ASSUMPTION]` / `[GAP]`.
- [ ] The deliverable is decision-support only; a competent person must review it.
