# RAMS methodology — Risk Assessment + Method Statement (construction)

This is the full domain method for `rams-builder`. A RAMS is **two coupled halves in
one document**: the **Risk Assessment (RA)** — the task/site-specific HIRA for the
activity — and the **Method Statement (MS)** — the sequenced safe system of work — tied
together by a **bidirectional RA↔MS cross-reference**. The RA half is the standard HIRA
loop (reused verbatim from the `risk-assessment` flagship; the same A7
`risk_matrix`/`controls` engine calls — **no second risk engine**). The MS half is
structured narrative and uses **no engine**.

## 1. Inputs (from the structured intake, SKILL.md Step 0)

The two load-bearing inputs are **Q2 (the construction activity)** and **Q-S (the
sequence of works)** — refuse to proceed on a vague activity or an unsequenced method.
Also captured: the site & environment (Q3), plant/equipment (Q-P), personnel &
competencies / the named competent persons (Q-C), permits (Q-W), existing controls /
the Construction Phase Plan (Q4), the org matrix size (Q5), the jurisdiction (Q1 →
CDM/BOCW; Q1a state for India), and the CDM/contractor role (Q6).

## 2. The RA half (the HIRA loop — ISO 45001 6.1.2, reused verbatim)

For each step in the sequence of works (Q-S):

1. **Hazard identification** — name the specific, observable hazards (working at height,
   excavation collapse, lifting, hot work, plant/pedestrian interface, electrical,
   manual handling, COSHH/dust); each names **what** is hazardous and **who/what is
   exposed** (own operatives, other trades, the public adjacent to the site). Assign an
   **RA-id** (RA-01…) to each hazard for the cross-reference. Flag `[GAP]` where a step's
   hazards are uncertain — never invent.
2. **Initial scoring** — `risk_matrix.load_matrix(config)` then
   `risk_matrix.score(likelihood, severity, matrix)` per hazard (Q5 config; default 5×5).
   Deterministic; the band is the engine's, not prose.
3. **Control selection (hierarchy of controls)** — apply `KB-SNIP-HOC` (Elimination →
   Substitution → Engineering → Administrative → PPE), then
   `controls.rank_controls` + `controls.validate_treatment`. If `ppe_admin_only` is
   `True`, **add a higher-order control or record an explicit justification** — a
   lower-order-only treatment with no justification is a defect the Critic/QA pass must
   catch. In construction, "PPE + a safe-working briefing" is the classic under-control:
   prefer edge protection / a MEWP over "wear a harness", an exclusion zone over "be
   careful".
4. **Residual re-scoring** — `risk_matrix.score(...)` with controls applied, then
   `risk_matrix.residual_delta(initial, residual)` for the movement. Residual
   High/Critical → additional controls or a hold-point (do-not-start).

## 3. The MS half (the sequenced safe system of work — no engine)

For the sequence in Q-S, produce **in order**, for each step:

- **Work-step description** — what is done at this step.
- **Plant/equipment** (Q-P) — the access/lifting/excavation/tooling used at this step.
- **Competencies / cards required** (Q-C) — CSCS/CPCS/IPAF/PASMA/appointed-person where
  the user names them; **never invent a certification the user did not supply** (record
  `[GAP]`).
- **Permits-to-work** (Q-W) — the hot-work / excavation / confined-space / lifting /
  working-at-height permit that gates this step.
- **Step-specific controls** — drawn from the RA half's control selection.

The MS is a **safe-system-of-work narrative**, not a hazard table — it tells the crew
*how* to do the job safely, in sequence.

## 4. The bidirectional RA↔MS cross-reference (the load-bearing coupling)

Tie each method step's residual hazards to the RA rows that treat them (an **RA-refs**
column: "Step 3 (excavate) → RA-04 collapse, RA-07 buried services"). The check is
**bidirectional**:

- **Forward:** refuse to ship a method step whose hazards are **not** in the RA.
- **Backward:** flag any RA hazard that **no** method step addresses.

This bidirectional check is the difference between a real RAMS and stapled-together
paperwork. The Critic/QA pass verifies both directions.

## 5. Emergency & rescue arrangements

Author the **activity-specific** provisions: a rescue plan for at-height / excavation /
confined-space / suspended-access work (a generic "call 999" is insufficient where a
rescue plan is required), first-aid provision, emergency contacts / RV point, and the
spill / fire / services-strike response relevant to the sequence.

## 6. SMART actions

Every control that is an action → a SMART action (specific, measurable, **assignable
(named owner / role)**, relevant, **time-bound (ISO due date)**), validated by
`smart_actions.validate_register`. No anonymous actions, no "ASAP".

## 7. Jurisdiction branches (both grounded — never fabricate a citation)

### UK — CDM 2015 (via `KB-REG-UK-HSWA`)

- **Reg 13** — principal-contractor duties (plan, manage & monitor the construction
  phase); the masterplan-named RAMS frame.
- **Reg 15** — contractor duties (a contractor plans, manages & monitors its own work);
  the method-statement / safe-system-of-work framing.
- **Construction Phase Plan (CPP)** — Reg 12(1)–(2) & Reg 15(4): the CPP is the
  construction-phase H&S management document the RAMS feeds into. Cite the regulation
  for the role captured at Q6.

### India — BOCW (via `KB-REG-IN-STATEFORMS`)

- **Mandatory state detection first** (Q1a) — confirm the state before citing any form.
- The **BOCW** Form XXV annual return (BOCW Rules, due ~15 Feb, state welfare board) is
  the **legacy-first** answer; append the **OSH-Code transition** note (the OSH Code
  subsumes BOCW; rules pending in most states).
- **Never** cite a national form number. An **unseeded state → `[GAP]`** + "verify with
  a competent person" — never fabricate.

## 8. De-id ↔ named-competent-persons exception

The de-id block scrubs personal data that arrives **as input evidence** (e.g. an
operative named in a prior near-miss) to role labels — a leak there is an **auto-fail**.
The **sign-off / briefing record** carries the names the user **deliberately supplies as
duty-holders / competent persons** at Q-C — these stay **named** (contractually required,
not leaked PII). The briefing-acknowledgement table ships with **empty signature rows**
for the crew to complete on site (it never pre-populates operative names). The
distinction: "names the user assigned as duty-holders for this document" (legitimate
output) vs "names that leaked from the evidence" (scrub to roles). This **layers on top
of** the standard de-id gate; it does not weaken it.

## 9. Output

Assemble `assets/rams-report.template.json` into a `report.json`
(`hse-report-model/v1`): the RA register (each row carrying its RA-id) → the
hierarchy-of-controls plan → residual risk → the **sequenced method statement with the
RA-refs cross-reference column** → emergency & rescue → recommendations (SMART actions)
→ regulatory basis (CDM 2015 Reg 13/15 or BOCW + the resolved state form) → the
**sign-off & briefing record (empty signature rows)**. Render the branded DOCX + PDF via
the shared engine.
