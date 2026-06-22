# Training Needs Analysis — Scaffolding Crew, North-tower Project (UK)

**Scope:** Specific project — the scaffolding crew on the north-tower project.
**Roles in scope:** Scaffolding Supervisor ×1, Advanced Scaffolder ×2, Labourer ×2 (5 people).
**Jurisdiction:** UK. **Industry:** Construction. **Driver:** Audit finding (competence-record gap).
**Competence sources used:** job descriptions · legal-required-competency map · dated training records · appraisal data · incident-driven gaps.
**Competence scale:** the 4-level scale (1 aware → 2 trained → 3 competent → 4 expert), `KB-DATA-COMPETENCE-LEVELS`.
**Standard basis:** ISO 45001:2018 clause 7.2 (competence) + 7.3 (awareness). Legal-required-competency: UK Management of Health and Safety at Work Regulations 1999 reg. 13 (capabilities & training); the Work at Height Regulations 2005 competence duty for scaffold inspection.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before use. Not legal advice.

## 1. De-identification status
De-id pass ran FIRST. Competence and appraisal data is personal data. All workers are carried as **role labels** ("Scaffolding Supervisor", "Advanced Scaffolder", "Labourer") — no names, employee IDs, addresses, appraisal scores, or health detail appear in this matrix. Where a competence is held by a single named person, the gap is reported **by role**, not identity (small-cell suppression). The re-identification key is held separately and is not part of this document.

## 2. Required competencies per role (with legal-required rows)

| Role | Required competence | Required level | Legal-required? |
|---|---|---|---|
| Scaffolding Supervisor | Scaffold inspection (competent person) | 3 (competent) + valid ticket | **Yes** — WAHR 2005 + MHSWR 1999 reg. 13 |
| Scaffolding Supervisor | Work-at-height rescue | 3 (competent) | No (best practice) |
| Advanced Scaffolder | Scaffold erection & inspection | 3 (competent) | **Yes** — WAHR 2005 |
| Advanced Scaffolder | Work-at-height rescue assist | 2 (trained) | No |
| Labourer | Manual handling | 2 (trained) | Partial — MHSWR reg. 13 |
| Labourer | Work-at-height awareness | 1–2 | No |

The **statutory scaffold-inspection competence** is a mandatory row — it is never omitted and never downgraded to "pass" to green the matrix.

## 3. Role × competence gap matrix (current vs required)

| Role (headcount) | Scaffold inspection (L3*) | Work-at-height rescue (L3) | Manual handling (L2) |
|---|---|---|---|
| Scaffolding Supervisor (×1) | **L2 — GAP 1 [LEGAL]** | L3 ✓ | L3 ✓ |
| Advanced Scaffolder (×2) | L3 ✓ (sole night-shift holder — **SPOF**) | L2 — GAP 1 | L2 ✓ |
| Labourer (×2) | L1 — supervised only | L1 — GAP 2 | L1 — GAP 1 |

\* Required level set by **task risk**, not the person; high-hazard scaffold inspection requires L3 (competent) + a current valid ticket where the law mandates one. Each current level is banded from a named evidence source (training record / appraisal); cells with no evidence would be flagged `[GAP]` and treated as unmet — none here.

## 4. Single-point-of-failure register

| Critical competence | Sole-holder role | Task it gates | Resilience action |
|---|---|---|---|
| Scaffold inspection (L3) | Advanced Scaffolder (night shift) | Pre-use scaffold inspection sign-off | Cross-train a second night-shift scaffolder to L3 |

Reported by role, not identity. If the sole holder is absent, no compliant night-shift inspection can occur — a resilience and compliance risk, not just a training gap.

## 5. Certification / expiry tracker

| Competence / certificate | Holder role | Expiry | Refresher due |
|---|---|---|---|
| Scaffold inspection (CISRS-equiv.) | Advanced Scaffolder ×2 | 2027-03-15 | 2027-01-15 |
| IPAF / work-at-height | Advanced Scaffolder ×2 | 2026-07-31 | **2026-06-30 — OVERDUE (P1)** |
| First aid at work | Scaffolding Supervisor | 2026-09-30 | 2026-08-01 |

## 6. Prioritised, costed training plan (SMART — owner, date, cost)

Prioritised by **gap size × task risk × legal mandate**. Statutory + high-hazard gaps and the SPOF rank first.

| # | Priority | Action | Gap addressed | Owner (role) | Due | Indicative cost |
|---|---|---|---|---|---|---|
| A1 | **P1** | Enrol Scaffolding Supervisor on an accredited scaffold-inspection competent-person course and assess to L3 | Supervisor L2→L3 [LEGAL] | Site HSE Lead | 2026-07-31 | ~£650 + 2 days `[ASSUMPTION]` |
| A2 | **P1** | Renew the two overdue IPAF/work-at-height certificates before next access work | Expired statutory cert | Training Coordinator | 2026-07-05 | ~£300 ×2 `[ASSUMPTION]` |
| A3 | **P2** | Cross-train a second night-shift scaffolder to L3 inspection (resolve the SPOF) | Single-point-of-failure | Scaffolding Supervisor | 2026-09-30 | internal time `[ASSUMPTION]` |
| A4 | **P3** | Deliver work-at-height rescue-assist training to the two labourers (L1→L2) | Rescue gap | Training Coordinator | 2026-10-31 | ~£200 ×2 `[ASSUMPTION]` |

Every action is specific, measurable (competence outcome), assignable (named owner role), relevant, and time-bound (ISO date) — validated via `smart_actions`. No "TBD", no "ASAP".

## 7. Training in the hierarchy of controls
Training is an **administrative** control (`KB-SNIP-HOC`). For the fall-from-height hazard it gates, training is paired with the higher-order site controls (edge protection, exclusion zones, a managed inspection regime) — it is **never** offered as the sole control. The competent-person inspection regime (A1) is the route by which the higher-order controls stay effective.

## 8. Assumptions & gaps
- Indicative course costs are `[ASSUMPTION]` pending supplier quotes.
- No current competence level was asserted without an evidence source; any unevidenced cell would be flagged `[GAP]` and treated as unmet — none in this run.

## 9. Review & sign-off
SME review ran (persona: **Competence & Training Manager**) — named-roles confirmed, the statutory scaffold-inspection competence present and cited, the SPOF flagged by role, training framed as an administrative control. This is decision-support; it **precedes and does not replace** the human competent-person sign-off. Next review: on workforce change or annually.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
