# Pre-output Quality Checklist — BBS Program Designer

The self-check loop run **before any output** (Workflow step 8). A BBS program design
that fails any item below is **not** ready — fix it and re-validate.

## Specificity & scope
- [ ] The program is anchored to a **named site / crew / operation** — not "improve our
  safety culture" in the abstract (Q1 refuse anchor held).
- [ ] The request is genuinely a **BBS program design** — not a culture-maturity
  assessment, a leadership gemba walk, or a KPI framework (routed to the sibling if so).

## Observable behaviours (the specificity lever)
- [ ] **Every card item is observable and site-specific**, tied to a named task/area —
  **no non-observable slogan** ("work safely", "be careful") published (Q3 gate held).
- [ ] Each behaviour has its **ABC** mapped (antecedent · observable behaviour ·
  consequence), with the system designed so the safe behaviour carries the
  soon/certain/positive consequence.

## Non-punitive design (HARD)
- [ ] Observation cards are **role-labelled or anonymous**, **voluntary**, and used for
  **trending and learning, never individual sanction**.
- [ ] **No card records a nameable individual for discipline** (any such card is a
  `de_identification` **hard-fail**, non-waivable).

## Metrics & confidentiality (special-care — HARD)
- [ ] Metrics are **defined** per `KB-DATA-BBS-METRICS` (percent-safe / participation /
  trend-by-category), trended **by behaviour category, never by person**.
- [ ] **No team breakdown of fewer than 5 is published**; **secondary suppression**
  applied so a suppressed cell cannot be back-calculated. (A percent-safe for a 4-person
  crew is suppressed.)
- [ ] No real name, contact detail, or individual identifier carried verbatim into the
  output; no re-identification key / name↔label mapping embedded.

## Hierarchy of controls (the core value)
- [ ] **At-risk behaviours route to hierarchy-ranked SYSTEM fixes** (eliminate /
  substitute / engineer / administrate before PPE) via the `controls` engine — **never
  "retrain the worker", "be more careful", or discipline** as the response to a trended
  at-risk category (`controls.validate_treatment` cleared or escalated).

## Actions & traceability
- [ ] Every system-fix action carries a **named role-label owner + an ISO due date + a
  measure** (`smart_actions.validate_register` passes) — no anonymous actions, no "ASAP".
- [ ] ISO 45001 clause 5.4 (worker participation) and the jurisdiction's
  worker-consultation duty are cited accurately; no invented standard reference.

## Output
- [ ] The observer-feedback loop is closed to **systemic** learning (not just a tally).
- [ ] De-identification pass was completed **BEFORE** drafting (the De-identifier ran
  first).
