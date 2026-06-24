# Pre-output Quality Checklist — Annual ESG OH&S disclosure

Before producing any output, validate the draft against this gate. Any unchecked item is a
defect to fix before output; the de-id and citation items are non-waivable hard-fails.

## De-identification (strictest tier — non-waivable)
- [ ] De-identification pass ran **BEFORE** drafting; identifiers and small cells listed up front.
- [ ] All injury/illness figures aggregated to the reporting boundary; no individual incident narrated.
- [ ] **No injury/illness cell of fewer than 5 published** (the `<5` small-cell rule).
- [ ] **Secondary suppression applied** — no suppressed cell is back-calculable from a published total or the remaining cells.
- [ ] No residual direct identifier and no re-identification key / name↔label mapping in the output.

## Boundary + denominator (assurability)
- [ ] **Every figure states its reporting boundary** (operational / financial / equity-share).
- [ ] **Every figure states its workforce split** (own-workforce vs non-employee/contractors — ESRS S1).
- [ ] **Every rate carries its denominator + definition** (hours worked, recordable basis), source, period, and completeness note — no figure published without its basis.
- [ ] Lagging rates (TRIR / DART / LTIFR / fatality rate) computed by `incident_rates` to the `KB-DATA-TRIR-BENCHMARKS` standard definitions; comparators carry `source`+`year` or `[GAP]`.

## Framework fidelity (citation accuracy — non-waivable)
- [ ] Disclosures selected from the **reused `KB-STD-ESG-GRI403`** crosswalk; **no duplicate index minted**.
- [ ] **Every claimed GRI 403 / SASB / ESRS S1 disclosure is actually present**; a claimed-but-absent required disclosure is recorded `[GAP]` (citation hard-fail) — never papered over.

## Assurance + materiality
- [ ] Intended **assurance level** (limited / reasonable) stated so the evidence rigour matches it.
- [ ] **Double-materiality** basis stated for reporting own-workforce H&S.

## Boundary held (decision-support framing)
- [ ] Improvement commitments narrated via the hierarchy of controls; each forward action owned + dated (`smart_actions`).
- [ ] The disclosure carries a de-id/aggregation notice + a decision-support / pre-assurance disclaimer.
- [ ] The document **never reads as a final assured, audited, or legal disclosure**, and never asserts it has been approved — it precedes, never replaces, the assurance engagement and the competent-person review.
