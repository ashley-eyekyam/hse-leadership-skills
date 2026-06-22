# Business Continuity Plan — Claims Processing, Northgate Operations Centre

**Standard basis:** ISO 22301:2019 — cl. 8.2.2 (Business Impact Analysis), 8.2.3 (risk
assessment), 8.3 (continuity strategies), 8.4 (plans & procedures), 8.5 (exercise
programme). Recovery objectives are derived from this organisation's own BIA, not asserted.
**Scope:** continuity of the time-critical activities of the claims-processing function at
the Northgate Operations Centre. **Audience:** exec / management / consultant.
**Boundary:** this BCP covers *continuity of critical activities* after a disruption; the
immediate incident response (muster, evacuation, scenario procedures, call-out tree, drills)
is owned by the **emergency-response-plan** and cross-referenced, not duplicated, here.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent
> person before use. Not legal advice. SME review (Business Continuity Manager, ISO 22301)
> ran and precedes — never replaces — the human competent-person sign-off.

## 1. De-identification status
De-id pass ran FIRST. Recovery roles are carried by **role label only** (Operations Director,
Continuity Lead, IT Recovery Owner, Finance Approver, Claims Manager, Comms Lead, and their
deputies). No real names, home addresses, personal mobiles, or medical detail of any
role-holder appear in this circulated plan; the role-label-to-post-holder **contact key is
held separately**, access-controlled, and is not part of this document.

## 2. Business Impact Analysis (BIA) — ISO 22301 8.2.2

For each critical activity: its output, how the impact of its loss grows over time, the MTPD
that impact-over-time curve yields, and its dependencies. Single-points-of-failure are
flagged so the strategy step must cover them.

| # | Critical activity | Output | Impact over time (loss) | **MTPD** | Dependencies |
|---|---|---|---|---|---|
| A1 | Claims intake & validation | Validated claims in queue | Regulatory SLA pressure by ~24h; customer detriment escalates after 48h | **48h** | Claims IT platform · **1 case-management supplier (SINGLE — flagged)** · claims team |
| A2 | Claims payment run | Settled payments to claimants | Hardship + reputational impact within 24h; FCA-reportable after 72h | **72h** | Payments gateway · Finance approver (**key person — flagged**) · banking partner |
| A3 | Customer contact centre | Answered claimant queries | Complaint spike within 8h; trust erosion after 24h | **24h** | Telephony/IT · contact-centre staff · premises (Northgate) |

[GAP] Backup cadence for the payments ledger not stated in intake — RPO for A2 set
conservatively at 1 business day pending confirmation (action E2).

## 3. Recovery objectives (MTPD / RTO / RPO) — ISO 22301 8.2.2

**Every RTO is derived under a stated MTPD (RTO < MTPD) with a stated margin; every activity
has an RPO.** An RTO with no MTPD basis, or an RTO ≥ MTPD, is invalid and is not set.

| Activity | **MTPD** | **RTO** (must be < MTPD) | Margin inside MTPD | **RPO** |
|---|---|---|---|---|
| A1 Claims intake & validation | 48h | **24h** | 24h | 4h (last validated batch) |
| A2 Claims payment run | 72h | **48h** | 24h | 1 business day (reconcilable) [GAP→E2] |
| A3 Customer contact centre | 24h | **8h** | 16h | Not data-bound (call routing) |

*Worked check (the core constraint):* a proposed "RTO = 48h" for A1 would be **invalid** —
A1's MTPD is 48h, and RTO must be strictly *inside* the MTPD, not equal to it. A "RTO" stated
with no MTPD behind it is likewise invalid (ISO 22301 8.2.2). Both are rejected here.

## 4. Continuity strategies — ISO 22301 8.3 (every dependency covered)

Each strategy meets its activity's RTO/RPO and **covers every stated dependency**; the
single-supplier and key-person single-points-of-failure are eliminated, not merely mitigated
(hierarchy of controls — eliminate the SPOF first).

| Activity / dependency | Strategy | Covers the dependency? |
|---|---|---|
| A1 — single case-management supplier | Onboard a **second qualified supplier** + a documented manual-validation workaround that meets the 24h RTO | Yes — SPOF eliminated |
| A1/A2 — claims IT platform / payments gateway | **Warm standby** failover for platform + gateway, tested to the 24h/48h RTOs | Yes |
| A2 — key-person Finance approver | **Cross-train a deputy approver**; dual-control payment authority | Yes — key-person SPOF removed |
| A3 — premises (Northgate) | Pre-arranged **alternate work-area / remote** contact-centre recovery for the 8h RTO | Yes |

## 5. Plan & recovery roles (with deputies) — ISO 22301 8.4

**Every recovery role has a named deputy** — no single point of failure in the response itself.

| Recovery role | Owner (role label) | **Deputy** (role label) | Responsibility |
|---|---|---|---|
| BCP activation authority | Operations Director | Continuity Lead | Declare invocation / stand-down |
| IT recovery | IT Recovery Owner | Infrastructure Lead | Restore platform + gateway to RTO |
| Claims continuity | Claims Manager | Senior Claims Officer | Run claims via the recovery strategy |
| Payments continuity | Finance Approver | Deputy Finance Approver | Execute payment run within RTO/RPO |
| Stakeholder comms | Comms Lead | Customer Experience Lead | Claimant + regulator communications |

## 6. Exercise / test schedule — ISO 22301 8.5 (smart_actions: owners + ISO dates)

| ID | Exercise | Type | Owner (role) | Cadence / due |
|---|---|---|---|---|
| E1 | Supplier-failover walkthrough | Tabletop | Continuity Lead | 2026-09-15 |
| E2 | Confirm payments backup cadence + set firm RPO for A2 | Action [GAP] | IT Recovery Owner | 2026-07-15 |
| E3 | IT warm-standby failover | Technical test | IT Recovery Owner | 2026-10-01 |
| E4 | Full BCP invocation drill | Live exercise | Operations Director | Annual — 2027-03-01 |

An untested plan is recorded as a `[GAP]`, never assumed adequate.

## 7. Review & sign-off
**Next review:** annual (2027-06-22) or on material change (new critical activity, supplier
change, or a failed exercise).

> **Cross-reference (BCP ↔ ERP boundary, D-07):** for the immediate incident / emergency
> response — muster, evacuation, scenario response procedures, the call-out tree, and
> emergency drills — see the **emergency-response-plan**. This BCP complements it and covers
> continuity of critical activities after the incident is controlled; the two are never
> merged.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
