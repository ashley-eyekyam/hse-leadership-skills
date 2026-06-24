<!-- KB-SNIP-LEADERSHIP-CLAUSE-MAP -->
# hse-leadership clause cross-walk — ISO 45001 leadership clause → owning skill

**Fragment ID:** `KB-SNIP-LEADERSHIP-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the **bundle-shared**
ISO 45001:2018 leadership-cluster clause cross-walk (CONV-10): which `hse-leadership` skill /
artifact owns each leadership-related clause. Every leadership skill's `kb-selection` references
it so a user asking "which skill covers clause X?" is routed consistently, and each skill knows
which sibling owns an adjacent clause. Single source — never duplicated into a skill body.

> Source: ISO 45001:2018 (clauses 5.1 / 5.2 / 5.4 / 9.1) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the leadership clause cross-walk

| ISO 45001:2018 clause | Leadership area | Owning hse-leadership skill / artifact |
|---|---|---|
| **5.1** Leadership and commitment | Felt leadership / visible commitment | `safety-walk-gemba` (felt-leadership walk) + `safety-culture-assessment` (leadership dimension) |
| **5.2** OH&S policy | Documented, top-management-signed policy | `hse-policy-generator` (primary) — the clause-5.2 mandatory commitment set |
| **5.4** Consultation and participation of workers | Worker participation | `bbs-program-designer` (non-punitive observation) + `safety-walk-gemba` (two-way conversation) + `safety-culture-assessment` (worker-voice survey) |
| **9.1** Monitoring, measurement, analysis & performance evaluation | Performance evaluation | `leading-lagging-kpi-framework` (primary — the balanced indicator set) + `hse-annual-esg-report` (the assurable performance figures) |

## Adjacent leadership-cluster pointers (not clause rows)

- **5.3** Organizational roles, responsibilities & authorities — surfaced through every skill's
  named-owner discipline (`smart_actions`), not a dedicated skill.
- **ISO 14001:2015 5.1/5.2** and **ISO 45003:2021** policy/leadership variants — `hse-policy-generator`
  selects the environmental / psychosocial commitment variant via its intake.

## How every leadership skill uses this fragment

Each skill references `KB-SNIP-LEADERSHIP-CLAUSE-MAP` in its `kb-selection` so the bundle presents a
single, consistent clause→skill map. A user who asks for the wrong artifact for a clause is
routed to the owning sibling; no skill restates the cross-walk in its own body (anti-drift).
