<!-- KB-DATA-RTO-RPO-GUIDANCE -->
# Recovery-objective banding — RTO / RPO under MTPD

**Fragment ID:** `KB-DATA-RTO-RPO-GUIDANCE`
**What this is:** the **recovery-objective banding reference** the
`business-continuity-plan` (#26) skill uses to derive and sanity-check RTO and RPO from the
Business Impact Analysis, under the binding **RTO < MTPD** constraint.
**What this is NOT:** a prescriptive set of recovery times for any organisation. Every RTO,
RPO and MTPD is derived from the organisation's own BIA — this fragment supplies the
**method bands and the margin discipline**, not values to assert. The binding clause
requirements are read from `KB-STD-ISO22301` (the user holds the licensed standard).

> Source: ISO 22301:2019 cl. 8.2.2 (BIA) / 8.2.3 (risk assessment) / 8.3 (BC strategies) · ISO 22313:2020 (guidance) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## The terms (derived per critical activity from the BIA)

| Term | Definition | Constraint |
|---|---|---|
| **MTPD** (Maximum Tolerable Period of Disruption) | The longest an activity can be unavailable before the impact becomes unacceptable. | Derived from the BIA's impact-over-time curve. |
| **RTO** (Recovery Time Objective) | The target time to resume the activity after disruption. | **RTO must be < MTPD** — with a margin; an RTO equal to or above MTPD is invalid. |
| **RPO** (Recovery Point Objective) | The maximum tolerable data/transaction loss, expressed as a time window. | Set by data-change rate and backup cadence. |

## Banding the recovery urgency (an indicative convention, not a mandate)

| Band | Indicative RTO window | Typical strategy implication |
|---|---|---|
| **Critical** | Hours | Hot standby / immediate failover; RPO near-zero. |
| **Essential** | Within ~1 day | Warm standby; short-interval backups. |
| **Important** | A few days | Cold recovery / manual workaround documented. |
| **Deferrable** | A week+ | Reconstitute later; accept the gap. |

**Margin discipline:** state the MTPD first (from the BIA), then set RTO strictly inside it
with a stated margin; set RPO from the activity's data-loss tolerance. An RTO asserted with
no MTPD basis, or RTO ≥ MTPD, is invalid (#26 eval case 1 — a `regulatory_citation_accuracy`
hard-fail on ISO 22301 8.2.2). Every recovery objective must cover the activity's stated
**dependencies** (people, IT, suppliers, premises) — a strategy ignoring a stated dependency
is flagged (#26 eval case 2).

## How the skill uses this fragment

- **#26 business-continuity-plan** runs the BIA → reads the impact-over-time per critical
  activity → derives MTPD → sets RTO < MTPD (with margin) + RPO using these bands
  (`KB-SNIP-BIA-METHOD` drives the method) → selects continuity strategies covering the
  dependencies → documents recovery roles with deputies and an exercise schedule.
