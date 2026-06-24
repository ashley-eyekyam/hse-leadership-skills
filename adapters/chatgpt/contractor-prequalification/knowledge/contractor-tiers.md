<!-- KB-DATA-CONTRACTOR-TIERS -->
# Contractor risk tiers — tier → PQQ-depth → pass-threshold map

**Fragment ID:** `KB-DATA-CONTRACTOR-TIERS`
**What this is:** the **risk-tier map** the `contractor-prequalification` (#16) skill uses
to set PQQ depth and the evidence/pass thresholds proportionate to the work's risk. It
bands a scope of work into a risk tier and states what evidence each tier demands and what
clears it.
**What this is NOT:** a scoring engine or a guarantee of competence. The tiers are a
**proportionality convention** (more risk → deeper questioning → higher evidence bar), not
a deterministic calculation; scoring stays evidence-anchored structured prose. Statutory
duties (UK CDM 2015 reg. 8, US OSHA multi-employer/controlling-employer policy) are read
from the regulatory fragments at use time, not encoded here.

> Source: ISO 45001:2018 cl. 8.1.4 (procurement/contractors/outsourcing) · UK CDM 2015 reg. 8 · UK SSIP (Safety Schemes in Procurement) baseline · US OSHA multi-employer policy CPL 02-00-124 · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## The tier map

| Tier | Work risk (examples) | PQQ depth | Evidence demanded (minimum) | Pass threshold |
|---|---|---|---|---|
| **T1 — Low / admin** | Office, cleaning, light maintenance — no high-hazard activity. | Core PQQ only. | Insurance; basic H&S policy; relevant references. | All core evidence present + no unresolved enforcement flag. |
| **T2 — Medium** | General trades, mechanical/electrical, plant on a managed site. | Core + task-specific section. | T1 + method statements/RAMS; accident/enforcement history; competence records for the trade; recognised accreditation (e.g. SSIP / ISO 45001) where applicable. | T1 + verified competence for the trade + no high-order control gap. |
| **T3 — High-hazard** | Hot work, confined space, work at height, lifting, energised electrical, demolition. | Full PQQ + activity-specific high-hazard module. | T2 + specific competence/certification for the high-hazard activity; safe-system-of-work / permit awareness; sub-contractor management; verified accident-rate data. | **Cannot pass on PPE/competence claims alone**; high-order controls evidenced; every score tied to a verified evidence item; unverifiable claim → conditional/reject. |

**Tiering rule:** tier is set by the **highest-risk activity** in the scope, not the
average. A single high-hazard task lifts the whole package to T3. Missing evidence becomes
a `[GAP]` and blocks an unconditional pass; a self-asserted claim with no certificate is
**never** scored as met (#16 eval case 1).

## How the skill uses this fragment

- **#16 contractor-prequalification** reads the scope/risk answer → assigns the tier →
  selects PQQ depth and the question bank (`KB-SNIP-PQQ-BANK`) for that tier → applies the
  pass threshold over the **verified** evidence register. High-hazard (T3) work demands the
  deeper PQQ and higher bar (#16 eval case 2 — risk-tier sensitivity), and any unverified
  claim or missing evidence yields a conditional/reject with named conditions and a review
  date, never an unconditional pass.
