<!-- KB-DATA-PSYCHOSOCIAL-INDICATORS -->
# Psychosocial indicator-tool benchmark bands (each cited)

**Fragment ID:** `KB-DATA-PSYCHOSOCIAL-INDICATORS`
**What this is:** the **indicator-tool benchmark reference** the
`psychosocial-risk-assessment` (#18) skill uses to band validated survey results against
the six HSE Management Standards domains. Each band carries a named **authority + year** —
a benchmark is never a bare number.
**What this is NOT:** a clinical instrument, a diagnostic threshold, or a substitute for
the licensed tool. The HSE Indicator Tool and its interpretation tables are held by the
user; this fragment names **where to resolve** the benchmark band and the discipline for
quoting it. Survey/focus-group data is **special-category health data** — the de-id
discipline (`<5` small-cell suppression, no attribution to a nameable individual) governs
every use (see `references/deid-checklist.md`).

> Source: UK HSE Management Standards Indicator Tool + analysis benchmarks · ISO 45003:2021 (psychosocial risk) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (benchmark tables revised; resolve current band at use time).

---

## How to band a result (resolve the binding band from the named tool)

| Benchmark band | Interpretation (HSE Management Standards convention) | What to quote |
|---|---|---|
| **Top ~20% (urgent)** | Among the worst-scoring — "urgent action needed". | "HSE Management Standards Indicator Tool benchmark, [year], top-20% band" |
| **Below average — improve** | Worse than typical; clear improvement target. | "HSE MS Indicator Tool benchmark, [year]" |
| **Better than average — maintain** | Better than typical; sustain. | "HSE MS Indicator Tool benchmark, [year]" |
| **Top ~20% (good)** | Among the best-scoring — "doing very well, maintain". | "HSE MS Indicator Tool benchmark, [year], top-20% band" |

The six domains the score bands against: **demands · control · support · relationships ·
role · change** (see `KB-SNIP-HSE-MGMT-STANDARDS` for each domain's work-design controls).

**Quoting discipline:** present every band as `<domain> <band> — <tool>, <year>`, resolved
from the licensed tool's current interpretation table at use time, never a remembered cut-off.
A domain/team breakdown with **fewer than 5 respondents is suppressed** (special-category
data); never attribute a finding to a nameable individual.

## How the skill uses this fragment

- **#18 psychosocial-risk-assessment** bands each domain's multi-source result against the
  named benchmark (with source+year), triangulates across ≥2 data sources (never rates on a
  single anecdote — #18 eval case 3), suppresses any `<5`-respondent breakdown (#18 eval
  case 2, a `de_identification` hard-fail), and routes findings to **work-design controls**
  ranked above individual resilience training.
