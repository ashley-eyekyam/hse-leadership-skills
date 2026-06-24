# Methodology — Annual ESG OH&S disclosure (assurance-ready, strictest de-id tier)

The domain method `hse-annual-esg-report` applies. It produces an **externally-publishable**
GRI 403 / SASB / ESRS S1 occupational-health-&-safety disclosure in which **every figure is
boundary-stated and denominator-defined** and **no small cell is back-calculable**. It mints
no new disclosure index — it **reuses `KB-STD-ESG-GRI403`** (D-02) — and grounds its
assurance discipline in `KB-SNIP-ESG-ASSURANCE`.

## 0. De-identify FIRST (strictest tier — `references/deid-checklist.md`)

The output is published externally and permanently. Before any analysis: aggregate all
injury/illness figures to the reporting boundary; **suppress any category with `<5`
individuals**; apply **secondary suppression** so a suppressed cell cannot be back-calculated
from a published total or the remaining cells; define denominators/boundaries so totals can't
be reverse-engineered. No individual incident is narrated. Everything downstream consumes only
the scrubbed, aggregated, suppression-safe figures.

## 1. Select disclosures from the reused crosswalk (`KB-STD-ESG-GRI403`)

Resolve each required OH&S disclosure in the shipped crosswalk:

- **GRI 403 (OH&S 2018):** 403-1 (management system) … 403-7 (process disclosures);
  **403-8** (workforce coverage), **403-9** (work-related injuries), **403-10** (work-related
  ill health) are the **assurable figure disclosures**.
- **SASB:** the industry workforce-health-&-safety metrics.
- **ESRS S1 (own workforce, CSRD):** S1-14 own-workforce H&S.

A "GRI 403" claim must carry every required 403 disclosure or record the absent one as
`[GAP]` — a **claimed-but-absent required disclosure is a `regulatory_citation_accuracy`
hard-fail**. Cite disclosure codes only; never reproduce framework text.

## 2. Define the reporting boundary for every figure (`KB-SNIP-ESG-ASSURANCE` §2)

Each figure states its **consolidation boundary** — operational control vs financial control
vs equity-share — and its **workforce split**: own-workforce vs non-employee/contractors
(**ESRS S1 mandates the split**). A figure with no stated boundary is **not assurable** and is
not published.

## 3. Validate every lagging rate deterministically (`incident_rates` + `KB-DATA-TRIR-BENCHMARKS`)

Compute TRIR / DART / LTIFR / fatality rate via the **`incident_rates`** engine from the
period's recordable counts and hours worked, to the standard definitions in
`KB-DATA-TRIR-BENCHMARKS` (anchors **TRIR 2.07 / LTIFR 6.00**). The rate and its denominator
are the engine's, never prose. **A rate with no denominator/definition is refused**, not
estimated. Quote each benchmark comparator's `source`+`year`; an unsourced comparator is
`[GAP]`, never invented.

## 4. Apply per-metric data quality (`KB-SNIP-ESG-ASSURANCE` §3)

Every published metric carries **definition + denominator + source + period +
completeness/accuracy note**. No figure is published without its basis — this is the
refuse-on-vague gate for ESG.

## 5. State assurance level + materiality (`KB-SNIP-ESG-ASSURANCE` §1, §4)

Record the intended **assurance level** — *limited* (negative conclusion) vs *reasonable*
(positive conclusion) — so the evidence rigour matches it. State the **double-materiality**
basis (impact + financial) for reporting own-workforce H&S.

## 6. Narrate improvement commitments via the hierarchy of controls (`KB-SNIP-HOC` + `smart_actions`)

Where the disclosure describes the OH&S programme or its response to the period's
performance, apply the **hierarchy of controls** (higher-order controls above PPE/admin) and
record any forward commitment as an **owned + dated** action via `smart_actions` — never a
published "we will try harder".

## 7. Locate the disclosure in the leadership clause-map (`KB-SNIP-LEADERSHIP-CLAUSE-MAP`)

This skill is **ISO 45001 clause 9.1** (monitoring, measurement, analysis and performance
evaluation) — the disclosed figures ARE the 9.1 performance evaluation made external.

## 8. Validate + assemble

Run `references/QUALITY_CHECKLIST.md` (the pre-output gate), then assemble `report.json`
(period-figures shape) and render the branded DOCX + PDF via the shared engine. The report
carries a **de-id/aggregation notice** and a **decision-support / pre-assurance** disclaimer,
and **never reads as a final assured, audited, or legal document** — it precedes, never
replaces, the assurance engagement and the competent-person review.
