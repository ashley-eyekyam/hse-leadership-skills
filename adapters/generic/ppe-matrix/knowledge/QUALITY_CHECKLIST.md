# Pre-output Quality Checklist — ppe-matrix

The self-check loop the Workflow runs before assembling the report. Every box must pass; a
failing box is a defect the Critic/QA + SME passes must fix before delivery. Nothing here is
ever signed off as **approved by a competent person** — this gate precedes the human review.

## Specificity (named scope)
- [ ] The matrix names the **actual area / line / role set and the tasks** (from Q1) — not a
      site-wide PPE sheet; the intake refused to proceed on a generic or whole-plant scope.
- [ ] The named site/area and the affected role(s) appear in the output.
- [ ] No conclusion rests on an unstated assumption — explicit `[GAP]` only.

## The controls-first gate (the core value, the spine)
- [ ] `KB-SNIP-PPE-MATRIX-LOGIC` + `KB-SNIP-HOC` applied to **every** body-region hazard via
      `controls.rank_controls` / `controls.validate_treatment` **before** any PPE row.
- [ ] **PPE appears only for the residual hazard surviving the higher-order controls** —
      eliminate / substitute / engineer / administrative were applied or justified first.
- [ ] **A hazard with no higher-order control recorded shows a "controls-first" FLAG, NOT a PPE
      row** — no PPE row was invented to fill the gate (`ppe_admin_only=True` / no higher-order
      control = flag, withhold the PPE cell). This is the headline failure mode; it must not occur.

## PPE selection + citation (the citation core)
- [ ] Every PPE row names the **residual hazard** it protects against and **cites its EN/ANSI
      conformity standard + year** (`KB-DATA-PPE-STANDARDS`) — a protection level asserted
      without the cited standard is a `regulatory_citation_accuracy` hard-fail.
- [ ] Respiratory PPE carries a fit-test / medical-clearance action at **role level** (no named
      clearance note).

## Written certification (mandatory — 1910.132(d)(2))
- [ ] The **written hazard-assessment certification** block is present: the workplace assessed,
      the certifier (named role), and the date. **Omitting it is a `regulatory_citation_accuracy`
      hard-fail.** No certifier or date is fabricated — a missing input is a `[GAP]`.

## Citations
- [ ] ISO 45001 6.1.2 cited (and `KB-SNIP-MANUFACTURING-CLAUSE-MAP`); the PPE duty cited to
      `KB-REG-OSHA1910-I` (1910.132). For India the **resolved state** is handled via
      `hse-india` — a state return owed is a `[GAP]`, **never a national form number**.

## De-identification (non-waivable — special-category respiratory-clearance / fitness data)
- [ ] The De-identifier ran FIRST; identifiers listed before drafting.
- [ ] Output uses **role labels only** — no residual name, no named respiratory medical-clearance
      / fitness note, **no `<5` health-outcome cell published**, no re-identification key embedded.

## Actions + report
- [ ] Every PPE-gap, fit-test, and controls-first action has a named role owner + an ISO date.
- [ ] A valid `report.json` (`hse-report-model/v1`) assembled from the cloned template; the
      `report-output` call produces docx + pdf (or warns-and-degrades).
