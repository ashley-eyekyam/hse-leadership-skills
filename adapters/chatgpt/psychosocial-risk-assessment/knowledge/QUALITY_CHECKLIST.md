# Pre-output Quality Checklist — Psychosocial Risk Assessment

The self-check loop run **before any output** (Workflow step 8). A psychosocial RA that
fails any item below is **not** ready — fix it and re-validate.

## Specificity & scope
- [ ] The assessment is anchored to a **named team / role / function** — not "the whole
  company" without a sampling plan (Q1 refuse anchor held).
- [ ] Every selected HSE Management Standards domain (demands · control · support ·
  relationships · role · change) is addressed or explicitly marked out-of-scope — no
  domain silently dropped.

## Hazard at source (work design, not the individual)
- [ ] Each finding names **what in the work design** is hazardous and the exposed
  **role/group** — never an individual.
- [ ] No individual is named as "the risk"; no finding frames the worker (rather than
  the work) as the problem.

## Evidence & triangulation
- [ ] Every rated domain draws on **≥2 data sources** — no rating built on a single
  survey item or a single anecdote (Q3 triangulation gate held).
- [ ] Each banded result quotes its indicator-tool **`source`+`year`**
  (`KB-DATA-PSYCHOSOCIAL-INDICATORS`) — no bare benchmark numbers.

## Confidentiality (special-category data — HARD)
- [ ] **No domain/team breakdown with fewer than 5 respondents is published.**
- [ ] **Secondary suppression** applied — a suppressed cell cannot be back-calculated
  from totals.
- [ ] No real name, contact detail, sickness-absence record, or health detail carried
  verbatim into the circulated output; no re-identification key / name↔label mapping
  embedded. (Any such leak is a `de_identification` **hard-fail**, non-waivable.)

## Hierarchy of controls
- [ ] **Work-design (organisational) controls rank above individual resilience
  training** for every domain; "resilience training" / EAP referral is never the sole
  or primary control (`controls.ppe_admin_only` cleared or escalated).
- [ ] Residual risk re-scored **with controls applied**; a High/Critical residual
  triggers further work-design controls or escalation — not "offer counselling and
  proceed".

## Actions & traceability
- [ ] Every action carries a **named role-label owner + an ISO due date + a measure + a
  domain link** (`smart_actions.validate_register` passes) — no anonymous actions, no
  "ASAP".
- [ ] ISO 45003 / HSE Management Standards (and the jurisdiction's legal duty) cited
  accurately; no invented standard reference.

## Output
- [ ] The report carries an explicit **confidentiality statement** section.
- [ ] De-identification pass was completed **BEFORE** drafting (the De-identifier ran
  first).
