# Methodology — Lift planning (LOLER Reg 8 + BS 7121, SWL read-not-computed)

The lift-planning method this skill applies. The **risk half** reuses the standard HIRA loop
(ISO 45001 6.1.2 + the deterministic `risk_matrix` engine — **no second risk engine**); the
**lift half** categorises, transcribes the chart, sequences the method, and uses **no engine**.
The defining constraint: **SWL-at-radius and utilisation are READ from the manufacturer's
rated-capacity chart (transcribed and checked), never computed** (D-08a) — this skill carries
**no lifting calculator and no crane-capacity engine**.

## 0. De-identify the inputs (before any drafting)
Run the `deid` block + `references/deid-checklist.md`. Scrub any **incident-derived** name
(a named operator from a prior dropped-load near-miss) and **every medical-fitness / health
detail** to role labels. **Exception:** the **appointed person / operator / slinger the user
supplies at Q5 for the competence record stay named** — duty-holder assignments, not leaked
PII. A worker's medical-fitness note is **always** scrubbed and **never** circulated.

## 1. Lift categorisation (BS 7121)
Classify the lift **basic / standard / complex** against `KB-DATA-LIFT-CATEGORIES` — the
**highest** triggered criterion sets the category. The category sets the planning depth: a
**complex** lift (tandem / multi-crane, blind, over the public / occupied area, load near the
SWL, poor / unknown ground, overhead-line / structure proximity) mandates an **appointed-person
WRITTEN plan + contingency / abort criteria + supervision**. Cite the code + the triggering
criterion.

## 2. Confirm the load & rigging (the specificity anchor)
Record the **confirmed load weight INCLUDING rigging / lifting accessories**, the dimensions,
the centre of gravity, and the lifting points (Q2). **An unconfirmed weight is a `[GAP]` and a
stop — never assumed.**

## 3. Equipment SWL / utilisation — READ, not computed
**Transcribe** the **SWL at the working radius** and the **utilisation %** from the
**manufacturer's rated-capacity chart** (Q3). Present each value as
`<parameter> = <value> (<source: chart model, year>)` and **check** it against the
`KB-DATA-LIFT-CATEGORIES` utilisation test. If utilisation exceeds the planned safe-utilisation
margin → **flag re-selection of the equipment** (a larger crane / shorter radius); do **not**
proceed. **The skill computes no capacity** — a chart value the user has not supplied is a
`[GAP]`, never invented.

## 4. Ground & proximity hazards — the hierarchy-of-controls lever
For each Q4 hazard apply `KB-SNIP-HOC`: rank **Elimination → Substitution → Engineering →
Administrative → PPE**; call `controls.rank_controls` + `controls.validate_treatment`. The
lift-specific lever: an **overhead-line** hazard is treated by **eliminating the lift in that
zone / re-routing / an engineered exclusion (goal-posts, a banksman)** — a **PPE-only
"operatives to take care / wear PPE" overhead-line control is a defect** (`ppe_admin_only=True`
with no higher-order control and no justification) the Critic/QA pass must catch. Set the
**exclusion zone / segregation** from the proximity tests (GS6 overhead-line clearance, the
load-radius swing, the drop zone) and assess the **ground / outrigger bearing**.

## 5. Initial + residual risk scoring (the A7 `risk_matrix` engine)
For each residual hazard call `risk_matrix.load_matrix(config)` → `risk_matrix.score(likelihood,
severity, matrix)` (default 5×5); re-score **with the selected controls applied** and call
`risk_matrix.residual_delta(initial, residual)`. A residual **High / Critical** risk flags that
additional controls or a **hold-point (do-not-lift)** are required — not "accept and proceed".
**Residual scoring reuses `risk_matrix`; there is no lifting calculator.**

## 6. Sequenced lift method + roles + contingency / abort
Author the **ordered** safe lift method (**rig → trial-lift / weigh → travel → slew → place →
de-rig**), the **roles** (the named appointed person who plans / supervises, the operator, the
slinger / signaller — each with the competence basis from Q5), the **weather / wind limits**
(the chart's in-service wind speed), and the **contingency & abort criteria** (loss of
communication, wind exceedance, an unplanned obstruction — the named stop conditions). Narrative,
**no engine**.

## 7. SMART actions (named owners + dates)
For every control that is an action, produce a SMART action (specific, measurable, **assignable**,
relevant, **time-bound (ISO due date)**) and call `smart_actions.validate_register`. Any action
missing an owner, a date, a measure, or a hazard link is **invalid** and must be fixed.

## 8. Validate + assemble
Run `references/QUALITY_CHECKLIST.md`, then build `report.json`
(`assets/lift-plan.report.json`) and render via the `report-output` block.

## Regulatory grounding
- **UK** — LOLER 1998 **Reg 8** (plan / organise / supervise) + **Reg 9** (thorough examination)
  + **BS 7121** (`KB-REG-LOLER-BS7121`, read `../../knowledge-base/regulatory/loler-bs7121.md`); + **CDM 2015**
  (`KB-REG-CDM2015`) where the lift is part of construction works (the lifting operation sits
  under the Construction Phase Plan, per `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`).
- **US** — **29 CFR 1926 Subpart CC** (cranes & derricks) + Subpart H (rigging) via
  `KB-REG-OSHA1926`.
- **India** — defers to `hse-india`; **mandatory state detection** via `KB-REG-IN-STATEFORMS`;
  the state crane-rules form is a **literal `[GAP]`, never a minted national form number**.
- **Always** — ISO 45001 6.1.2 / 8.1.2 (`KB-STD-ISO45001`) + `KB-SNIP-HOC` on every control.
