<!-- KB-DATA-LEADING-INDICATORS -->
# Leading/lagging HSE indicator catalogue (single-source; each cited)

**Fragment ID:** `KB-DATA-LEADING-INDICATORS`
**What this is:** the curated **leading/lagging indicator catalogue** — the **single source** (D-03)
consumed by `leading-lagging-kpi-framework` (KPI design), `safety-walk-gemba` (commitment-closure as a
leading indicator), and `safety-culture-assessment` (maturity-linked indicator mix). Each entry is
tagged `leading|lagging` + formula + source. KPI design method lives in `KB-SNIP-KPI-DESIGN`.
**What this is NOT:** a per-skill private list — no skill duplicates this catalogue. Lagging rates are
**computed** by `incident_rates`, never invented here. Cited as **method, not law**.

> Source: HSE HSG65 active vs reactive monitoring · OECD / CCPS leading-indicator guidance (recognised method) · lagging-rate definitions per `incident_rates` (anchors TRIR 2.07 / LTIFR 6.00) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (sector benchmark targets revised; resolve current figure at use time).

---

## Leading indicators (active / predictive)

| Indicator | Tag | Formula | Source |
|---|---|---|---|
| % planned inspections completed | leading | (inspections completed ÷ inspections planned) × 100 | HSG65 active monitoring |
| Near-miss reporting rate | leading | near-misses reported ÷ exposure (e.g. per 100k hours) | HSG65 / OECD |
| Training completion | leading | (competencies achieved ÷ competencies required) × 100 | HSG65 active monitoring |
| Action close-out rate | leading | (actions closed on time ÷ actions due) × 100 | OECD/CCPS leading-indicator guidance |
| BBS percent-safe | leading | (safe ÷ total observed) × 100 (see `KB-DATA-BBS-METRICS`) | BBS method |
| Gemba-commitment closure | leading | (walk commitments closed ÷ walk commitments raised) × 100 | HSG65 felt leadership (`KB-SNIP-GEMBA-PROMPTS`) |
| PTW compliance | leading | (permits audited compliant ÷ permits audited) × 100 | HSG65 active monitoring |

## Lagging indicators (reactive / outcome) — computed by `incident_rates`

| Indicator | Tag | Definition source |
|---|---|---|
| TRIR | lagging | `incident_rates` standard definition (anchor 2.07) |
| LTIFR | lagging | `incident_rates` standard definition (anchor 6.00) |
| DART | lagging | `incident_rates` standard definition |

## Discipline

- Every indicator carries **formula · source · frequency · owner · target** when placed in a skill's
  framework (see `KB-SNIP-KPI-DESIGN`); a bare indicator with no definition fails specificity.
- A **lagging-only** set fails the balance gate — pair lagging outcomes with leading predictors.
- Lagging rates are **computed** by `incident_rates` to standard definitions, never invented.

## How the skills use this fragment

`leading-lagging-kpi-framework` builds its balanced set from this single catalogue; `safety-walk-gemba`
reports walk-commitment closure as the leading indicator named here; `safety-culture-assessment` shifts
the leading/lagging mix toward leading as maturity advances. No skill copies the catalogue.
