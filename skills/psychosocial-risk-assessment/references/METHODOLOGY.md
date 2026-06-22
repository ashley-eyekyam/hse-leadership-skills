# Methodology — Psychosocial Risk Assessment (ISO 45003 + HSE Management Standards)

The domain method the `psychosocial-risk-assessment` skill applies. It assesses
work-related psychosocial risk **at source — the work design, not the individual** —
grounded in **ISO 45003:2021** (`KB-STD-ISO45003`) and the **UK HSE Management
Standards** (`KB-SNIP-HSE-MGMT-STANDARDS`), on the same ISO 45001 clause 6.1.2
hazard-identification discipline as the physical RA. Scoring is deterministic (the A7
`risk_matrix`/`controls` engines), never prose judgement.

## Principle 1 — Assess the hazard at source (work design, not the worker)

A psychosocial hazard is a **feature of how work is organised**, not a deficiency of
the person doing it. Each finding names **what in the work design** is hazardous
(workload pattern, low decision latitude, weak manager support, unresolved conflict,
role ambiguity, poorly managed change) and **which role/group** is exposed. The skill
never produces a clinical or individual-diagnosis output, and **never names an
individual as "the risk"**. Where an individual is in distress, route to a competent
occupational-health professional — that is out of this skill's scope.

## Principle 2 — Multi-source triangulation (never a single anecdote)

Every rated domain draws on **at least two data sources** from: a validated survey
(e.g. the HSE Indicator Tool), focus groups, sickness-absence & turnover data, and
grievance/incident data. A single anecdote or a single survey item is **not** a basis
for a rating — if only one source is available, **refuse to rate** and record `[GAP]`
with a request for corroborating data. Triangulation is what makes the conclusion
defensible.

## Principle 3 — Confidentiality thresholds (special-category data)

Survey/focus-group responses and sickness-absence are **special-category health data**
(GDPR Art. 9). Apply `references/deid-checklist.md` in full **before any analysis**:
- Suppress any domain/team breakdown with **fewer than 5 respondents**.
- Apply **secondary suppression** so a suppressed cell cannot be back-calculated from
  row/column totals.
- Attribute findings to **roles/groups**, never to a nameable individual.
- Hold any re-identification key separately; never embed it in the output.

## Principle 4 — Organisational controls before individual resilience

Apply `KB-SNIP-HOC` to every control: **work-design (organisational) controls rank
ABOVE individual resilience training**. For each domain the indicative work-design
controls are in `KB-SNIP-HSE-MGMT-STANDARDS`:

| Domain | Work-design control (organisational — first) | Individual measure (last resort only) |
|---|---|---|
| Demands | Achievable workloads, job/role redesign, staffing, environment fixes | (time-management coaching) |
| Control | Decision latitude, flexibility, involve in how work is done | — |
| Support | Manager-support systems, resources, supportive policies | EAP / counselling referral |
| Relationships | Anti-bullying policy + enforcement, conflict resolution, reporting routes | (individual mediation) |
| Role | Clear role definitions, resolve conflicting demands | — |
| Change | Early consultation, clear communication, transition support | (change-resilience support) |

An assessment whose **only** control is "resilience training" or "offer counselling" is
a defect — the Critic/QA and SME passes must flag it and push the treatment up to
work-design controls.

## The method loop

1. **De-identify first** — scrub to role/group labels, suppress <5 cells, apply
   secondary suppression (Principle 3). Everything downstream consumes scrubbed text.
2. **Confirm ≥2 data sources** for the named unit (Principle 2) — else refuse to rate.
3. **Identify the hazard by domain** — for each Q2 domain, the work-design hazard +
   exposed role/group, grounded in `KB-SNIP-HSE-MGMT-STANDARDS` (Principle 1).
4. **Rate** — band each domain against `KB-DATA-PSYCHOSOCIAL-INDICATORS` (quote
   source+year), triangulate, then score on the org 5×5 via
   `risk_matrix.load_matrix` + `risk_matrix.score`.
5. **Select work-design controls** — `KB-SNIP-HOC` + `controls.rank_controls` +
   `controls.validate_treatment`; organisational controls above individual resilience
   (Principle 4).
6. **Re-score residual** — `risk_matrix.score` with controls applied +
   `risk_matrix.residual_delta`; a High/Critical residual needs further work-design
   controls or escalation.
7. **SMART action plan** — `smart_actions.validate_register`; every action a named
   role-label owner + ISO due date + measure + domain link.
8. **Validate** against `QUALITY_CHECKLIST.md`.
9. **Assemble** the branded report (`assets/psychosocial-risk-assessment-report.template.json`),
   including the explicit **confidentiality statement** section.

## Citations

ISO 45003:2021 (psychosocial risk management) · UK HSE Management Standards (six
domains) · ISO 45001:2018 clause 6.1.2 (hazard identification) · the jurisdiction's
legal duty (UK MHSWR 1999 reg. 3; US NIOSH Total Worker Health framing; EU OSH
Framework Directive 89/391/EEC; India OSH Code 2020 welfare provisions via `hse-india`).
Quote each benchmark band's `source`+`year`; never invent a standard reference.
