# Pre-output Quality Checklist — job-safety-analysis (JSA / JHA)

The self-check loop the Workflow runs at step 8, before assembling the report. Every box
must pass; a failing box is a defect the Critic/QA pass must fix before delivery.

## Step decomposition (the spine)
- [ ] The job's **ordered step sequence** was elicited (Q4) and **confirmed** (Workflow
      step 2); the intake refused to proceed on a vague job or an empty/one-line step list.
- [ ] **No step invented or omitted** — any unconfirmed step is recorded `[GAP]`, never
      silently inserted.
- [ ] The output is a **JSA table with one row per step** (or a row-group where a step has
      multiple hazards at different risk levels).

## Specificity
- [ ] The JSA names the **actual job/task** (from Q3) and the named site/area/asset (Q8) —
      not "general maintenance".
- [ ] No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` / `[GAP]` only.

## Per-step scoring (deterministic)
- [ ] **Each step's hazard(s)** scored via the A7 `risk_matrix.score` engine (initial band)
      — not prose judgement.
- [ ] **Each step's** residual risk re-scored after controls; `risk_matrix.residual_delta`
      movement shown; a step left at residual High/Critical carries a "more controls /
      stop-hold before performing the step" flag.

## Hierarchy of controls per step (the core value)
- [ ] `KB-SNIP-HOC` applied to **every step's** controls; `controls.rank_controls` ranked
      them Elimination → Substitution → Engineering → Administrative → PPE.
- [ ] **No step** left with a lower-order-only (PPE/admin) treatment **without** a
      higher-order control or an explicit per-step "not reasonably practicable because…"
      justification (`ppe_admin_only` cleared or justified for that step).

## Actions
- [ ] Every consolidated action has a **named (role-label) owner**, an **ISO due date**, a
      measure, and a **step + hazard link**; `smart_actions.validate_register` reports zero
      invalid actions. No "ASAP", no anonymous actions.

## Citations
- [ ] ISO 45001 6.1.2 cited; for India the **resolved state form** is cited via
      `KB-REG-IN-STATEFORMS` (state confirmed at Q1a), **never a national form number**; for
      UK construction the CDM 2015 reg. 13/15 + Construction Phase Plan rows
      (`KB-REG-UK-HSWA`) where relevant.

## De-identification (non-waivable)
- [ ] The De-identifier ran FIRST; identifiers listed before drafting.
- [ ] Output uses role labels only — no residual name/ID/address, no re-identification key
      embedded, no injury/illness cell of fewer than 5 published.
- [ ] The **sign-off / acceptance block** ships with role-labelled rows and **EMPTY**
      signature + date columns — **no fabricated names** (completed at point of use).

## Report
- [ ] A valid `report.json` (`hse-report-model/v1`) assembled; the JSA `table` is the core
      with a `risk_column`; the band names match the `palette.risk` keys; the sign-off
      `table` block follows the consolidated register; the `report-output` call produces
      docx + pdf (or warns-and-degrades).
