# Pre-output Quality Checklist — risk-assessment (HIRA)

The self-check loop the Workflow runs at step 7, before assembling the report. Every
box must pass; a failing box is a defect the Critic/QA pass must fix before delivery.

## Specificity
- [ ] The assessment names the **actual task/activity** (from Q3), not "general site
      safety"; the intake refused to proceed on a vague task.
- [ ] The named site/area/asset (Q4) and exposed population (Q5) appear in the output.
- [ ] No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` / `[GAP]`
      only.

## Scoring (deterministic)
- [ ] Every hazard is scored via the A7 `risk_matrix.score` engine (initial band) —
      not prose judgement.
- [ ] Residual risk re-scored after controls; `risk_matrix.residual_delta` movement
      shown; a residual High/Critical band carries a "more controls / stop-work" flag.

## Hierarchy of controls (the core value)
- [ ] `KB-SNIP-HOC` applied to **every** control; `controls.rank_controls` ranked them
      Elimination → Substitution → Engineering → Administrative → PPE.
- [ ] No lower-order-only (PPE/admin) treatment **without** a higher-order control or
      an explicit "not reasonably practicable because…" justification
      (`ppe_admin_only` cleared or justified).

## Actions
- [ ] Every action has a **named owner**, an **ISO due date**, a measure, and a
      hazard link; `smart_actions.validate_register` reports zero invalid actions. No
      "ASAP", no anonymous actions.

## Citations
- [ ] ISO 45001 6.1.2 cited; for India the **resolved state form** is cited via
      `KB-REG-IN-STATEFORMS` (state confirmed at Q1a), **never a national form number**.
- [ ] When the environmental branch ran: ISO 14001 6.1.2 cited and any Q-E5
      compliance obligations recorded.

## Environmental branch (only when Q0 = Environmental/Both)
- [ ] Each aspect → impact pair identified and tagged with its operating condition.
- [ ] Significance scored via the **same** `risk_matrix.score` engine.
- [ ] Hierarchy of controls applied to the aspect (eliminate/substitute first); the
      report carries the environmental aspects/impacts register section.

## De-identification (non-waivable)
- [ ] The De-identifier ran FIRST; identifiers listed before drafting.
- [ ] Output uses role labels only — no residual name/ID/address, no re-identification
      key embedded, no injury/illness cell of fewer than 5 published.

## Report
- [ ] A valid `report.json` (`hse-report-model/v1`) assembled; the `risk_level` band
      names match the `palette.risk` keys; the `report-output` call produces docx + pdf
      (or warns-and-degrades).
