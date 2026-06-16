# Methodology — Job Safety Analysis (JSA / JHA): the step-decomposition method

This is the domain method `job-safety-analysis` applies. The SKILL.md Workflow is the
operational summary; this file is the full reference. The JSA *is* the ISO 45001 6.1.2
HIRA loop **anchored to a task's ordered step sequence** — the step is the unit of
analysis. Everything here is traced to evidence with a named owner and a date, and every
per-step control is ranked through the hierarchy of controls — never a vague or PPE-only
treatment of a step without justification.

## 1. Decompose the job into its ordered steps (the spine)

A JSA starts from the job's **ordered sequence of steps**, not from a list of hazards. The
intake (Q3/Q4) elicits the exact job and its steps; Workflow step 2 confirms and normalises
them as `Step 1, Step 2, …`. **Never invent or omit a step** — if the user's sequence has an
obvious gap (e.g. no isolation before a maintenance step), *ask*; an unconfirmed step is
recorded `[GAP]`. The confirmed ordered list is the skeleton every later step iterates over.
A job with no real step sequence is not a JSA — refuse to proceed and elicit the steps.

## 2. The per-step ISO 45001 6.1.2 loop

For **each step** in the confirmed sequence, run the loop. The loop is
jurisdiction-independent (Chennai / Houston / Aberdeen alike); the resolved jurisdiction
only changes the *regulatory-basis* citations, not the method.

1. **Identify the step's hazards (energy-source paired).** For the step, name the specific,
   observable hazards introduced *by performing that step*, paired with their **energy
   source** — gravity (falls, dropped objects), electrical, mechanical/kinetic (moving
   parts, stored energy), pressure, chemical (substances, gases), thermal (hot/cold),
   biological, noise/vibration, ergonomic. Name **who/what is exposed**. Grounded in
   `KB-STD-ISO45001` 6.1.2. Where a step's hazards are uncertain, record `[GAP]` — never
   invent.
2. **Score the step's initial risk deterministically.** Call `risk_matrix.load_matrix(config)`
   once (config from Q11; default `DEFAULT_5X5`), then `risk_matrix.score(likelihood,
   severity, matrix)` for the step's hazard(s). The returned `{score, band, band_action,
   matrix_size}` is authoritative — the band is the engine's, not prose. The calibrated 5×5
   bands are **Low 1–4 · Medium 5–9 · High 10–15 · Critical 16–25** (A7 D-02, `multiply`
   scoring). These band names key the report's `palette.risk` colour scale — keep them
   aligned (A4↔A7 seam).
3. **Select the step's controls — the hierarchy of controls.** Apply `KB-SNIP-HOC`: rank
   **Elimination → Substitution → Engineering → Administrative → PPE**, then call
   `controls.rank_controls` + `controls.validate_treatment`. If the returned
   `ppe_admin_only` is `True` for the step, you **must** add a higher-order control for that
   step **or** record an explicit per-step justification that higher-order controls are not
   reasonably practicable. A step left lower-order-only with no justification is a defect —
   the Critic/QA pass catches it. This is the core value enforced *per step*.
4. **Re-score the step's residual risk.** Re-score the step with its selected controls
   applied via `risk_matrix.score`, then `risk_matrix.residual_delta(initial, residual)` for
   the movement. A step whose residual stays High/Critical triggers a "more controls or
   stop/hold before performing the step" flag, never "accept and proceed".

## 3. Consolidate the per-step controls into SMART actions

Gather the controls that are *actions* (not already in place) across all steps into one
register. Each becomes a SMART action — specific, measurable, **assignable (named
role-label owner)**, relevant, **time-bound (ISO due date)**, and **linked to the step (and
hazard) it addresses** — validated by `smart_actions.validate_register`. Any action missing
an owner, a valid date, a measure, or a step/hazard link is **invalid** and must be fixed.
No anonymous or undated actions, no "ASAP".

## 4. Output / report assembly

Assemble one `report.json` (`hse-report-model/v1`) from `assets/jsa-report.template.json`
and run the canonical `report-output` call. House section order (A4): executive summary →
scope & method (incl. the confirmed ordered step list) → **key findings = the JSA table**
(step → hazards → initial risk → controls[HoC tier] → residual risk → owner) → hierarchy of
controls (consolidated control plan) → residual risk (per-step deltas) → recommendations
(consolidated SMART actions) → regulatory basis → **sign-off / acceptance block**. The
engine auto-stamps the cover, classification, TOC, and the limitations/de-id notice.

**The JSA table is the core.** It is step-keyed and dense (often >10 step-rows), so it
renders as an A4 **`table` with a `risk_column`** rather than `findings` cards (the
step-sequence density a JSA reviewer expects). The risk-rated cells use the band names from
§2 step 2 (Low/Medium/High/Critical) so the `palette.risk` colour scale resolves.

**The sign-off / acceptance block** (CORE-02 / ROADMAP SC-1) is the named "sign-off"
deliverable: render it as an A4 `table` block (the existing report-engine block type — no
new renderer behaviour) placed AFTER the JSA table / consolidated register, with
**role-labelled rows** (Worker(s), Supervisor, Reviewed-by) and **EMPTY signature + date
columns** completed at point of use. Honour the de-id convention exactly: input names scrub
to roles and the signature rows ship **EMPTY** (no fabricated names) — this is what a worker
and supervisor physically sign to accept the safe system of work before the job starts,
mirroring the named-competent-persons / empty-signature-rows pattern.

## 5. Evidence & defensibility

Every step is confirmed (none invented); every step's hazard names what is hazardous, its
energy source, and who is exposed; every score is the engine's; every per-step control is
HoC-ranked; every action has a named owner and an ISO date; every citation traces to the KB
(ISO 45001 6.1.2 always; the jurisdiction fragment + India → the resolved state form via
`KB-REG-IN-STATEFORMS`, never a national number; UK construction → CDM 2015 reg. 13/15 +
Construction Phase Plan via `KB-REG-UK-HSWA`). No conclusion rests on an unstated assumption
— explicit `[ASSUMPTION]` / `[GAP]` only. De-identification runs first; the output is
decision-support and must be reviewed by a competent person.
