<!-- KB-SNIP-OPS-CLAUSE-MAP -->
# hse-operations clause cross-walk — ISO 45001 operations clause → owning skill

**Fragment ID:** `KB-SNIP-OPS-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the **bundle-shared**
ISO 45001:2018 operations clause cross-walk (D-10): which `hse-operations` skill / artifact
owns each operations-related clause. Every OPS skill's `kb-selection` references it so a user
asking "which skill covers clause X?" is routed consistently, and each skill knows which
sibling owns an adjacent clause. Single source — never duplicated into a skill body.

> Source: ISO 45001:2018 (clauses 6.1.3 / 7.2 / 7.3 / 8.1.4 / 8.2 / 9.1 / 9.1.2) · adjacent: ISO 22301:2019 (BCP) · ISO 45003:2021 (psychosocial) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the operations clause cross-walk

| ISO 45001:2018 clause | Operations area | Owning hse-operations skill / artifact |
|---|---|---|
| **6.1.3** Determination of legal & other requirements | Compliance obligations | `legal-compliance-register` (#20) — register rows |
| **7.2** Competence | Competence | `training-needs-analysis` (#13) — role×competence matrix |
| **7.3** Awareness | Awareness | `induction-pack` (#14) — induction content + verification |
| **8.1.4** Procurement / contractors / outsourcing | Contractor control | `contractor-prequalification` (#16) — PQQ + scorecard |
| **8.2** Emergency preparedness & response | Emergency | `emergency-response-plan` (#15) — scenario procedures + drill schedule |
| **9.1** Monitoring, measurement, analysis & evaluation | Performance evaluation | `iso45001-gap-analysis` (#19) — clause-9.1 conformance (leadership KPI skill cross-refs) |
| **9.1.2** Evaluation of compliance | Compliance evaluation | `legal-compliance-register` (#20) — compliance-evaluation summary |
| *(6.1.2 hazard-id, cross-cut)* | Health/psychosocial hazard-id | `health-risk-assessment` (#25) + `psychosocial-risk-assessment` (#18) |

## Adjacent management-system standards (pointers, not ISO 45001 clause rows)

- **ISO 22301:2019** — business continuity (`business-continuity-plan` #26): BIA → MTPD →
  RTO/RPO; complements the 8.2 emergency response, does not duplicate it.
- **ISO 45003:2021** — psychosocial risk (`psychosocial-risk-assessment` #18): extends ISO
  45001 6.1.2 hazard-id to work-related psychosocial hazards.
- **Statutory returns** — `regulatory-returns` (#27) sits beside 9.1.2 (evidence of
  compliance) but is driven by the jurisdiction's recordkeeping rule, not an ISO clause.

## How every OPS skill uses this fragment

Each skill references `KB-SNIP-OPS-CLAUSE-MAP` in its `kb-selection` so the bundle presents a
single, consistent clause→skill map. A user who asks for the wrong artifact for a clause is
routed to the owning sibling; no skill restates the cross-walk in its own body (anti-drift).
