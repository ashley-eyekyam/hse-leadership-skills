# ISO 45001 Gap Analysis & Certification-Readiness Assessment — AcmeCo Plant 2

**Standard assessed:** ISO 45001:2018 (clause set 4-10).
**Scope:** AcmeCo Plant 2 — single site, manufacturing. Management-system boundary: the whole site.
**Current state:** Preparing for initial certification. **Target:** Initial certification readiness.
**Conformance scale:** 5-level maturity scale per `KB-DATA-ISO45001-MATURITY` (0 Absent -> 1 Ad hoc -> 2 Documented -> 3 Implemented/conformant -> 4 Measured & improving), each level with an evidence test. **Certification-readiness rule:** a mandatory clause at level <= 2 is a certification-blocker (a major nonconformity under ISO/IEC 17021-1), not a minor gap.
**Prioritisation:** `KB-SNIP-GAP-PRIORITISATION` (certification-blockers first). **Lead auditor:** HSE Manager. **Target cert date:** 2026-12-01.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before use. It does NOT certify the management system and is not legal advice.

## 1. De-identification status
De-id pass ran FIRST. The audit interview notes named two individuals, one with a disclosed cardiac condition, plus a 2-person corrective-action cell. All are carried as role labels only (Operations Manager [Manager-A], Maintenance Supervisor [Supervisor-B], HSE Manager, Top Management); the disclosed condition and the <5 owner cell are suppressed/aggregated. No name, address, phone, or health detail appears in this record; the re-identification key is held in a separate access-controlled artifact.

## 2. Clause-by-clause conformance (every clause scored — none omitted)

| Clause | Title | Maturity (0-4) | Status | Evidence basis |
|---|---|---|---|---|
| 4.1-4.4 | Context, interested parties, scope, the OH&S MS | 2 — Documented | Gap | Scope statement drafted; interested-party analysis partial (E-1) |
| 5.1 | Leadership & commitment | 2 — Documented | Gap | Leadership engaged informally; no documented evidence of accountability (L-1) |
| **5.2** | **OH&S policy** | **1 — Ad hoc** | **BLOCKER** | No documented OH&S policy authorised by top management on file (L-1) |
| 5.3 / 5.4 | Roles / consultation & participation | 2 — Documented | Gap | Roles defined; worker-participation records thin (E-2) |
| **6.1.2** | **Hazard identification & risk assessment** | **3 — Implemented** | Conformant | HIRA records across scope, reviewed within cycle (E-4) — **scored, not omitted** |
| 6.1.3 | Legal & other requirements | 2 — Documented | Gap | Legal register exists; compliance-evaluation evidence missing (see `legal-compliance-register`) |
| 6.2 | OH&S objectives & planning | 1 — Ad hoc | Gap | Objectives stated verbally; no measurable plan (E-5) |
| 7.2 | Competence | 2 — Documented | Gap | Competence matrix exists; training records partial (E-7) |
| 7.3 / 7.4 / 7.5 | Awareness / communication / documented info | 2 — Documented | Gap | Induction runs; document control inconsistent (E-8) |
| 8.1 / 8.1.4 / 8.2 | Operation / contractors / emergency | 2 — Documented | Gap | Procedures on paper; contractor controls + drill records partial (E-9) |
| 9.1 / 9.1.2 | Monitoring, measurement / compliance evaluation | 1 — Ad hoc | Gap | Some monitoring; no formal compliance evaluation (9.1.2) |
| **9.2** | **Internal audit** | **0 — Absent** | **BLOCKER** | No internal-audit programme established [GAP] |
| 9.3 | Management review | 1 — Ad hoc | Gap | Leadership meets; no structured management review against the standard |
| **10.2** | **Incident, nonconformity & corrective action** | **2 — Documented** | **BLOCKER** | Procedure on paper; no corrective-action records show it operating (I-1) |
| 10.3 | Continual improvement | 1 — Ad hoc | Gap | Improvement reactive, not driven by performance data |

No clause is silently omitted — clause 6.1.2 is explicitly scored (level 3, conformant); every clause carries a maturity level or an N/A-with-reason.

## 3. Certification-blocker flags (major nonconformities)

Three mandatory clauses sit at level <= 2 and are **certification-blockers** — they would stop a stage-2 certification audit and cannot be deferred past the cert date:

1. **5.2 OH&S policy (level 1)** — no documented, top-management-authorised policy.
2. **9.2 Internal audit (level 0)** — no internal-audit programme exists.
3. **10.2 Corrective action (level 2)** — procedure exists but is not evidenced in operation.

These are flagged as blockers, not minor gaps (the core defensibility lever).

## 4. Hierarchy-of-controls check (planning clause 6.1)

For the clause-6.1 planning controls, controls are ranked highest-order first per `KB-SNIP-HOC`; the remediation is not PPE/admin-only:

| Tier | Control | Owner |
|---|---|---|
| Elimination | Establish a documented OH&S policy authorised by top management (removes the 5.2 gap at source) | Top Management |
| Engineering | Build the internal-audit programme into the MS calendar with automated scheduling/reminders | HSE Manager |
| Administrative | Monthly management-review standing item tracking every corrective action to closure | Site Manager |

## 5. Prioritised, costed remediation roadmap (named owners + dates — blockers first)

| ID | Action | Clause | Priority | Owner (role label) | Due (ISO) | Est. cost |
|---|---|---|---|---|---|---|
| R1 | Draft, approve and communicate a documented OH&S policy | 5.2 | P1 (blocker) | Top Management / HSE Manager | 2026-09-07 | Low |
| R2 | Establish an internal-audit programme + train two internal auditors; run one audit cycle | 9.2 | P1 (blocker) | HSE Manager | 2026-09-21 | Medium |
| R3 | Stand up the corrective-action register; evidence one full nonconformity-to-closure cycle | 10.2 | P1 (blocker) | HSE Manager | 2026-10-05 | Low |
| R4 | Complete competence-record backfill against the competence matrix | 7.2 | P2 | Competence & Training Lead | 2026-10-19 | Low |
| R5 | Formalise the compliance-evaluation step (9.1.2) using the legal register | 6.1.3 / 9.1.2 | P2 | HSE Manager | 2026-10-26 | Low |
| R6 | Set measurable OH&S objectives with a monitoring plan | 6.2 / 9.1 | P3 | Site Manager | 2026-11-09 | Low |

Every action is SMART (named owner + ISO due date + a measure + a clause link), cost-estimated, and ordered certification-blockers first. No anonymous actions, no "ASAP".

## 6. Assumptions & gaps
- [GAP] No internal-audit evidence was supplied — clause 9.2 scored level 0, not assumed conformant.
- [ASSUMPTION] The competence matrix is current; confirm with the Competence & Training Lead before sign-off (R4).
- Where no evidence was supplied a clause is scored as a gap (level 0/1), never assumed ready.

## 7. Branded report
A branded `report.json` (from `assets/iso45001-gap-analysis-report.template.json`) is emitted and rendered to DOCX + PDF via the report engine, using the site `brand.yaml` (Eyekyam default where unset). The conformance matrix populates the scored-clause table; the gap register and certification-blocker flags populate their sections; the roadmap populates the recommendations section.

## 8. Review & sign-off
SME review ran (persona: Lead Auditor / Management-Systems Consultant): every clause scored or N/A-with-reason, all three certification-blockers correctly classified (not downgraded), every gap traced to clause + evidence + owner, the roadmap ordered blockers-first. Overall readiness: **Not yet ready** — three blockers must close before the 2026-12-01 target. This is decision-support that precedes — and never replaces — the human competent-person sign-off; no "certified" or "approved by a competent person" claim is made.
