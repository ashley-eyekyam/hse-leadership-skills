# Methodology — Contractor Prequalification (ISO 45001 cl. 8.1.4)

The method this skill applies: **tier the rigour to the work's risk → ask for verifiable
evidence not claims → verify each claim → score only on verified evidence → recommend
approve/conditional/reject with named conditions, owners, and a review date.** Grounded in
**ISO 45001:2018 clause 8.1.4** (procurement / contractors / outsourcing), with **UK CDM 2015
reg. 8** where the work is construction and the **US OSHA multi-employer worksite policy
(CPL 02-00-124)** for controlling-employer duties. The scoring is a **cited weighted rubric
applied as structured prose** (`KB-DATA-CONTRACTOR-TIERS` + `KB-SNIP-PQQ-BANK`) — **there is
no `contractor_score` engine** (§8 anti-sprawl).

## 0. De-identify FIRST (before any scoring)

A contractor's **accident / enforcement history can name injured persons** (prosecutions,
RIDDOR / OSHA records). Run the de-identification scrub **before** the evidence reaches the
scorer: replace names, exact dates, and locations with role labels; **suppress any injury
cell < 5** on a small contractor; keep the re-identification key separate. Supplier-confidential
pricing/commercial data is minimised. See `references/deid-checklist.md`.

## 1. Risk-tiering — set the depth and the bar

Band the scope of work into a tier per `KB-DATA-CONTRACTOR-TIERS`:

| Tier | Work risk | PQQ depth | Pass threshold (summary) |
|---|---|---|---|
| **T1 — Low / admin** | office, cleaning, light maintenance | Core PQQ only | All core evidence present + no unresolved enforcement flag |
| **T2 — Medium** | general trades, M&E, plant on a managed site | Core + task-specific | T1 + verified trade competence + no high-order control gap |
| **T3 — High-hazard** | hot work · confined space · work at height · lifting · energised electrical · demolition | Full PQQ + high-hazard module | **Cannot pass on PPE/competence claims alone**; high-order controls evidenced; every score tied to a verified evidence item |

**Tiering rule:** the tier is set by the **highest-risk activity** in the scope, not the
average. A single high-hazard task lifts the whole package to **T3**.

## 2. Build the tiered PQQ (evidence-anchored)

Select the question set for the tier from `KB-SNIP-PQQ-BANK`: **Core** (HSE policy, insurance,
accident/enforcement history, workforce competence) for T1+; **Task-specific** (RAMS,
recognised accreditation, sub-contractor management) for T2+; the **high-hazard module**
(activity-specific competence/certification, safe-system-of-work/permit integration, verified
accident-rate data) for T3. **Each question names the verifiable evidence that answers it** —
the signed policy, the current certificate, the in-date competence record.

## 3. Build the evidence register & verify each claim

For every PQQ item record: the claim · the evidence supplied · a **verification status**
(verified / unverified / not-supplied). **A self-asserted claim with no supporting evidence is
`[GAP]` — never scored as met.** This is the integrity gate the core value enforces: a "pass"
on a self-asserted accreditation with no certificate is a defect, not an approval. Evaluate the
contractor's proposed controls / safe system of work up the hierarchy via
`controls.rank_controls` + `controls.validate_treatment` and `KB-SNIP-HOC` — **T3 work cannot
pass on PPE/competence claims alone**; higher-order controls must be evidenced.

## 4. Score against the threshold (cited rubric, structured prose)

Score each criterion **only on its verified evidence**, then apply the tier's pass threshold
from `KB-DATA-CONTRACTOR-TIERS`. The scoring is a proportionality convention applied as prose,
**not a deterministic calculation** — but the discipline is hard: every score traces to a named
evidence item; an unverified or `[GAP]` criterion cannot clear the threshold.

## 5. Recommend — approve / conditional / reject

- **Approve** — only when **every** threshold criterion is met on **verified** evidence, with
  no open `[GAP]`.
- **Conditional** — when gaps are closeable. Each condition is a **SMART action**
  (`smart_actions.validate_register`: named owner + ISO due date + measure, tied to the gap it
  closes), **plus a review date**. Never "approve and proceed" over an open `[GAP]`.
- **Reject** — when a threshold criterion fails irrecoverably (e.g. unresolved serious
  enforcement, no high-hazard competence for T3 work, no insurance).

## 6. Re-approval cadence

Set a review date from the evidence's expiry (insurance, accreditation, competence
certificates) or the client's cadence (annual / per-project). Re-approval re-runs the verify →
score → recommend loop against current evidence; expired evidence reverts to `[GAP]`.

## 7. Validate, then assemble the report

Run `references/QUALITY_CHECKLIST.md`, then build `report.json` from
`assets/contractor-prequalification-report.template.json` and render via the shared engine.
