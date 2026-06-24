# Pre-output Quality Checklist — Safety Walk / Gemba

Before producing any walk plan or walk record, validate the draft against this gate. Any
unchecked item is fixed (or escalated) before output.

## Engagement, not inspection
- [ ] The walk is built from **OPEN, area-specific, non-interrogative prompts** (from
  `KB-SNIP-GEMBA-PROMPTS`) — **not a closed yes/no tick-box checklist**. A closed checklist
  is flagged (specificity · defensibility) and the user is steered to the open prompt bank
  (or to `safety-audit` if they want an inspection).
- [ ] The prompts are anchored to the **named area / task / shift** in scope (Q2), not
  generic.

## Psychological safety (de-identification)
- [ ] The De-identification pass ran **FIRST**, before any drafting; identifiers listed up
  front.
- [ ] Every worker concern is captured **role-labelled** — **no concern is attributed to a
  nameable individual** (a named-worker→concern attribution is a `de_identification`
  hard-fail).
- [ ] No residual direct identifier (name, phone, email, address, payroll ID) and no
  re-identification key embedded in the output.

## Commitments owned, dated, tracked
- [ ] **Every commitment** made on the walk is converted to a **SMART action** with a named
  **role-label owner** + an **ISO due date** + a measure (`smart_actions.validate_register`).
  **No anonymous commitments, no "ASAP".**
- [ ] Any control a commitment implies is ranked via the **hierarchy of controls**
  (`KB-SNIP-HOC` + `controls`), higher-order first — no PPE-only / "retrain the worker"
  default.
- [ ] A walk with **no tracked commitment** is recorded as `[GAP]`, **not** signed off as
  complete (defensibility).

## Leading indicator + citations
- [ ] The **count and closure-rate of walk commitments** is reported as a **leading
  indicator** (`KB-DATA-LEADING-INDICATORS`, `source`+`year` quoted).
- [ ] ISO 45001:2018 **5.1 / 5.4** cited accurately (`KB-SNIP-LEADERSHIP-CLAUSE-MAP`); no
  fabricated clause or figure.

## Boundary
- [ ] The output is decision-support only; it does not assert it has already been signed off
  — a competent person must review it. The SME persona (HSE Leadership / Engagement Coach)
  pass ran before output.
