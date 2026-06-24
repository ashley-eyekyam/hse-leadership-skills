# Pre-output Quality Checklist — Pre-Construction Information (PCI)

Before producing any output, validate the draft against this gate. The **gap-discipline**
and **Reg 4 citation** items are load-bearing — a PCI that fails either is not defensible.

## Gap discipline (the core-value lever)
- [ ] **Every missing information source is recorded as a `[GAP]`, never silently omitted** — a dropped missing asbestos survey / ground investigation / as-builts is a defensibility failure.
- [ ] **Every `[GAP]` carries a named owner + an ISO due date** (via `smart_actions`) — no anonymous gaps, no "ASAP".
- [ ] Any gap that blocks construction (e.g. an outstanding asbestos survey before strip-out) is flagged as a **hold-point**.

## Existing-structure hazard information
- [ ] **Asbestos status is explicit** — present-and-surveyed, presumed-pending-survey, or `[GAP]` — never silently absent on a refurbishment/demolition.
- [ ] **Buried & overhead services are addressed** — presence/location or a `[GAP]`.
- [ ] Ground conditions, structural form, and the existing H&S file content are each stated or `[GAP]`.
- [ ] Every existing-structure hazard is **traced to its source** (survey / drawing / file); no invented result; `[ASSUMPTION]` / `[GAP]` flagged where uncertain.

## Regulatory citation (hard-fail dimension)
- [ ] **The client's Reg 4 duty AND timing are stated** — provided as soon as practicable to everyone appointed/considered (Reg 4(4)); **omitting the Reg 4 duty/timing is a `regulatory_citation_accuracy` hard-fail.**
- [ ] The one-line **PCI → CPP → H&S File** (Reg 4 → 12 → 12(5)) cross-reference is present, sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **without assuming a sibling skill ran**.
- [ ] India: the state is resolved before any form; defers to `hse-india`; an un-seeded state → `[GAP]`, **never a minted national form number**.

## De-identification & defensibility
- [ ] De-identification pass complete **BEFORE** drafting; **no survey-occupier name or health detail** leaked; `<5` cells suppressed; no embedded re-id key.
- [ ] Restricted-distribution flag set where the pack carries sensitive site / occupier detail.
- [ ] The user-supplied gap-action owners + client/principal-designer duty-holders stay named (legitimate record); survey-occupier names scrub to role labels.
- [ ] No conclusion rests on an unstated assumption.
- [ ] SME review (CDM Principal Designer + CDM Client Adviser personas) ran; it never emits "approved by a competent person".
