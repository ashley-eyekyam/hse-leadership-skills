<!-- KB-SNIP-ESG-ASSURANCE -->
# ESG assurance method — boundary · data-quality · materiality · strictest de-id

**Fragment ID:** `KB-SNIP-ESG-ASSURANCE`
**This is prompt text, applied by the model — not a generator.** It is the **assurance method** the
`hse-annual-esg-report` skill applies to make its OH&S disclosures assurable. The disclosure→artifact
crosswalk (GRI 403-1…403-10 ↔ SASB ↔ ESRS S1) is **NOT authored here** — it **reuses the shipped
`KB-STD-ESG-GRI403`** (D-02). `KB-DP-ESG-DISCLOSURES` is **deliberately not minted** (it would
duplicate that index). This fragment carries only the assurance discipline below. Injury-rate figures
come from `incident_rates` (anchors TRIR 2.07 / LTIFR 6.00), never invented. Cited as **concept
anchor, not law**.

> Source: ISAE 3000 (Revised) — assurance engagements other than audits · AA1000 Assurance Standard v3 · ESRS double materiality (impact + financial) · GRI / GHG-Protocol reporting-boundary concepts · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (ESRS/CSRD assurance phase-in settling — resolve current expectation at use time).

---

## Instruction — make every figure assurable

### 1. Assurance level

| Level | Conclusion | Drives |
|---|---|---|
| **Limited** | negative — "nothing came to our attention" | lighter evidence; ESRS/CSRD currently phases in here. |
| **Reasonable** | positive — explicit conclusion | higher evidence rigour. |

State the engagement's intended level so the evidence rigour matches it.

### 2. Reporting boundary (every figure carries its boundary)

- **Consolidation:** operational control vs financial control vs equity-share — define explicitly.
- **Workforce split:** **own-workforce vs non-employee/contractors** — ESRS S1 mandates the
  employee/non-employee split. A figure with no stated boundary is not assurable.

### 3. Data-quality criteria (per metric)

Each published metric needs **definition + denominator + source + period + completeness/accuracy
note**. No figure is published without its denominator and basis — this is the refuse-on-vague gate
for ESG.

### 4. Materiality

Apply **double materiality** (impact + financial): own-workforce H&S is reported when material; state
the materiality basis. A disclosure with no materiality rationale is incomplete.

### 5. De-id at the strictest tier (external publication)

This is the strictest de-id tier in the bundle — the report is publicly published.

- **Aggregate all**; **mandatory `<5` suppression** on any injury/illness category (especially
  fatalities/illness by site or demographic — a small cell could identify the deceased).
- **Secondary suppression** — a suppressed cell must not be back-calculable from a published total or
  the other cells; suppress a second cell where arithmetic would otherwise recover the first.
- Define **denominators and boundaries** so totals cannot be reverse-engineered to a small cell.

## Framework alignment (via the existing crosswalk, not re-authored)

Reference `KB-STD-ESG-GRI403` for the disclosure codes: GRI 403:2018 (403-8…403-10 = the assurable
injury/ill-health figures), SASB industry workforce-H&S metrics, ESRS S1-14 (own-workforce H&S) —
each cross-checked to `incident-rate-calculator` denominators.

## How the skill uses this fragment

`hse-annual-esg-report` selects disclosures via `KB-STD-ESG-GRI403`, then applies THIS assurance
method (level · boundary · data-quality · materiality · strictest-tier de-id with secondary
suppression) so every figure is denominator-defined, boundary-stated, and non-back-calculable.
