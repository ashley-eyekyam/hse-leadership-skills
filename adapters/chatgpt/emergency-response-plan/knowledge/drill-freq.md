<!-- KB-DATA-DRILL-FREQ -->
# Emergency-drill frequencies by scenario / site-class (each cited)

**Fragment ID:** `KB-DATA-DRILL-FREQ`
**What this is:** the **drill-frequency reference** the `emergency-response-plan` (#15)
skill uses to schedule exercises by scenario and site-class. Each frequency carries a
named **authority + year** — a drill cadence is never a bare number.
**What this is NOT:** a definitive or current statutory schedule. Drill obligations are
jurisdiction- and sector-specific and revised periodically; the **binding** frequency is
resolved from the cited authority for the user's jurisdiction/site-class at use time. The
rows below are **reference cadences with their source+year**, never a substitute for the
authority. Where a jurisdiction has no explicit drill mandate, `[GAP]`-flag it and
recommend the most-protective referenced cadence — never invent a legal frequency.

> Source: UK Regulatory Reform (Fire Safety) Order 2005 art. 15 / US OSHA 29 CFR 1910.38 / ISO 45001:2018 cl. 8.2 / sector good-practice (per-row authority+year) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (drill mandates revised; resolve current obligation at use time).

---

## Reference cadences (each carries authority + year — resolve the binding value at use time)

| Scenario / site-class | Reference cadence | Authority + year (the source line) |
|---|---|---|
| General workplace evacuation (fire) | At least annually; new starters within induction | "UK RRFSO 2005 art.15 — periodic; HSE good practice ≥ annual, 2006" |
| US workplace — Emergency Action Plan review/drill | On plan adoption, when duties/plan change, and periodically (commonly annual) | "US OSHA 29 CFR 1910.38(e)/(f), 2002" |
| Higher-occupancy / multi-storey / public premises | More frequent than annual (e.g. 6-monthly) per fire risk assessment | "UK RRFSO 2005 fire-risk-assessment-driven, 2006" |
| Major-accident-hazard (MAH) on-site emergency plan | Periodic test of the on-site emergency plan (sector-defined; commonly annual full + interval partial) | "ISO 45001 8.2 + jurisdiction MAH regime — resolve sector frequency, [GAP] if unstated" |
| Scenario-specific (gas release / spill / confined-space rescue) | Per the credible-scenario register; rescue capability proven before reliance | "ISO 45001 8.2 — scenario-keyed; sector rescue standard, [GAP] if unstated" |
| India factory on-site emergency plan | Defers to `hse-india` (Factories Act 1948 s.41B mock-drill provisions resolved by state rule) | "→ hse-india / KB-REG-IN-FACTORIES; state rule resolves cadence; [GAP] until detected" |

*The cadences above are reference points for scheduling; the binding obligation for a named
site + jurisdiction + scenario is resolved from the cited authority at use time, with its
source+year carried into the artifact. India drill obligations route to `hse-india`.*

## How the skill uses this fragment

- **#15 emergency-response-plan** schedules each credible scenario's drill from this
  reference (with its source+year), proves rescue/response capability before the plan
  relies on it, and `[GAP]`-flags any scenario whose jurisdiction sets no explicit cadence
  — recommending the most-protective referenced value, never a fabricated legal frequency.
