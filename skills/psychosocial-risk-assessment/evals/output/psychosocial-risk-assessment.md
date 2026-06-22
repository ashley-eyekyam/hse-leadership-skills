# Psychosocial Risk Assessment — Night-Shift Contact-Centre Advisers (Site B)

**Assessment type:** Issue-based (post-restructure review of work-related psychosocial risk).
**Unit in scope:** Night-shift contact-centre advisers, Site B — a named work-design population (≈22 advisers across the overnight roster). Assessed as a group; no individual named.
**Framework:** ISO 45003:2021 + UK HSE Management Standards (demands · control · support · relationships · role · change). Domains in scope this cycle: **demands, control, support**.
**Jurisdiction:** UK — general risk-assessment duty under the Management of Health and Safety at Work Regulations 1999 reg. 3 (psychosocial risk is in scope); HSWA 1974.
**Scoring engine:** org 5×5 matrix (score 1–25; bands Low 1–4 / Medium 5–9 / High 10–15 / Critical 16–25), per `risk_matrix.score`.
**Standard basis:** ISO 45003:2021; hazard identification per ISO 45001 clause 6.1.2; benchmark bands from the HSE Management Standards Indicator Tool (source + year quoted per domain).

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person (occupational-health / psychosocial specialist) before use. This is not a clinical or individual mental-health assessment, and not legal advice.

## 1. De-identification status (special-category data)

De-id pass ran **FIRST**. Survey, focus-group and sickness-absence inputs were treated as **special-category health data**. Identifiers detected in the raw pack (two respondent names, one home address, one phone number, one disclosed health detail) were pseudonymised to **role/group labels**; the re-identification key is held in a SEPARATE access-controlled artifact and is NOT reproduced here. **No individual is named as the risk.** Any sub-team breakdown of fewer than 5 respondents was **suppressed** with **secondary suppression** so a suppressed value cannot be back-calculated from totals. All findings are reported at the role-group level only.

## 2. Method & data sources (triangulated — ≥2)

The rating draws on **three** data sources for the named group (the ≥2 triangulation gate is met):
- **Validated HSE Indicator Tool survey** — banded against the HSE Management Standards Indicator Tool benchmark, 2026.
- **Focus-group themes** — aggregated and anonymised (no verbatim that could identify a small-group speaker).
- **Stress-related sickness-absence trend** — aggregated to the role-group (sub-5 cells suppressed).

No domain is rated on a single source or a single anecdote.

## 3. Psychosocial hazards by domain (assessed at source — work design, not the individual)

| Domain | Work-design hazard | Exposed group | Benchmark band (tool, year) |
|---|---|---|---|
| Demands | Night-shift call volumes + after-call work exceed an achievable workload for the role; sustained overload since the restructure. | Night-shift advisers | Top-20% urgent — HSE MS Indicator Tool, 2026 |
| Control | Low decision latitude over pacing, breaks and adherence targets. | Night-shift advisers | Below average — HSE MS Indicator Tool, 2026 |
| Support | Overnight supervisory cover and manager-support routes weakened by the restructure. | Night-shift advisers | Below average — HSE MS Indicator Tool, 2026 |

[GAP] "Relationships", "role" and "change" domains were out of scope this cycle (Q2) — scheduled for the next review. No finding is attributed to a nameable individual.

## 4. Risk rating (deterministic 5×5; triangulated)

| Domain | Likelihood | Severity | Initial score (L×S) | Band |
|---|---|---|---|---|
| Demands | 4 (Likely) | 4 (Major) | 16 | Critical |
| Control | 3 (Possible) | 3 (Moderate) | 9 | Medium |
| Support | 3 (Possible) | 3 (Moderate) | 9 | Medium |

The band is the `risk_matrix.score` engine's, not prose. Each rating is corroborated across the three sources above.

## 5. Work-design controls — full hierarchy of controls

Controls ranked highest-order first (Elimination → Substitution → Engineering → Administrative → PPE/individual) per `KB-SNIP-HOC`, then verified by `controls.rank_controls` / `controls.validate_treatment`. **Organisational work-design controls rank ABOVE individual resilience training**; individual resilience / EAP referral is the last-resort support measure, never the primary control.

### Demands
| Tier | Control |
|------|---------|
| Elimination | Re-balance night-shift call volumes and after-call work to an achievable workload — staffing + queue routing fixes that remove the chronic overload. |
| Substitution | Replace fixed back-to-back call handling with a blended workload (calls + lower-intensity tasks) overnight. |
| Engineering | Workforce-management tooling that caps concurrent queue load per adviser to the achievable level. |
| Administrative | Workload monitoring + a documented escalation route when volumes exceed the agreed cap. |
| Individual (last resort) | Optional resilience / stress-management support OFFERED — never the primary control, never a substitute for the workload fix. |

### Control
| Tier | Control |
|------|---------|
| Substitution | Give advisers decision latitude over break timing and pacing within service levels. |
| Administrative | Involve the role-group in designing the overnight schedule (consultation, ISO 45003 participation). |

### Support
| Tier | Control |
|------|---------|
| Engineering | Restore overnight supervisory cover so a manager-support route exists on every night shift. |
| Administrative | Manager training on supportive overnight supervision (an organisational support system, not individual resilience). |

`controls.ppe_admin_only` does **not** clear on an individual-resilience-only treatment — the demands hazard carries Elimination/Engineering work-design controls, so the treatment is defensible.

## 6. Residual risk (post-control re-score) — initial → residual movement

| Domain | Initial score / band | Residual score / band | Movement |
|---|---|---|---|
| Demands | 16 Critical | L2 × S4 = 8 Medium | Critical → Medium (after workload re-balance + cap) |
| Control | 9 Medium | L1 × S3 = 4 Low | Medium → Low (after decision-latitude controls) |
| Support | 9 Medium | L2 × S3 = 6 Medium | Medium → Medium-low (after supervisory cover restored) |

Residual scoring uses the same `risk_matrix.score` engine. The demands residual remains tracked until the P1 workload action is verified complete.

## 7. SMART action plan (named role-label owner + ISO due date + domain link)

| ID | Action | Domain | Owner (role label) | Due | Review trigger |
|----|--------|--------|--------------------|-----------|----------------|
| A1 | Re-balance night-shift workload; confirm achievable staffing + queue routing | Demands | Operations Manager | 20 Jul 2026 | Before next roster; on volume change |
| A2 | Implement concurrent-queue load cap per adviser in WFM tooling | Demands | Resource Planning Lead | 10 Aug 2026 | Post-implementation review |
| A3 | Pilot adviser-controlled break/pacing within service levels | Control | Resource Planning Lead | 10 Aug 2026 | Pilot review |
| A4 | Reinstate overnight supervisory cover + manager-support route | Support | Site Manager | 31 Jul 2026 | Each shift; on rota change |
| A5 | Manager training on supportive overnight supervision | Support | OH / HR Lead | 15 Sep 2026 | On completion; annual refresh |

Every action carries a named role owner, an ISO date, a domain link, and a review trigger — no anonymous actions, no "ASAP".

## 8. Confidentiality statement

This assessment relies on special-category psychosocial data. All respondents are reported as role/group labels; no breakdown of fewer than 5 respondents is published; secondary suppression is applied; the re-identification key is held separately. No individual is named as the risk. Do not widen distribution beyond the named recipients without a further de-identification review.

## 9. Branded report

A branded `report.json` (see `assets/psychosocial-risk-assessment-report.template.json`) is emitted and rendered to DOCX + PDF via the report engine, using the site `brand.yaml` (Eyekyam default where unset). The domain findings populate the hazards-by-domain section; the SMART-action table populates the action-plan section; the confidentiality statement is a first-class section.

## 10. Review & sign-off

Whole-assessment review trigger: on change (a further restructure or a material volume change) or at 12 months — whichever is first; the remaining HSE Management Standards domains (relationships, role, change) are scheduled for the next cycle. **Competent-person sign-off (occupational-health / psychosocial specialist) is required prior to circulation.** This decision-support output precedes — and never replaces — that human sign-off.
