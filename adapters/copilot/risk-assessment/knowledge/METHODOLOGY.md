# Methodology — HIRA (ISO 45001 6.1.2) + the optional ISO 14001 6.1.2 environmental-aspects branch

This is the domain method `risk-assessment` applies. The SKILL.md Workflow is the
operational summary; this file is the full reference. Everything here is traced to
evidence with a named owner and a date, and every control is ranked through the
hierarchy of controls — never a vague or PPE-only treatment without justification.

## 1. The safety HIRA loop (ISO 45001 clause 6.1.2)

The loop is jurisdiction-independent (Chennai / Houston / Aberdeen alike); the
resolved jurisdiction only changes the *regulatory-basis* citations, not the method.

1. **Identify hazards per task step.** Use the Q3 step breakdown. For each step name
   the specific, observable hazard (energy source, substance, environment, human
   factor) and **who/what is exposed** (Q5). Grounded in `KB-STD-ISO45001` 6.1.2.
   Where a step's hazards are uncertain, record `[GAP]` — never invent.
2. **Score initial risk deterministically.** Call `risk_matrix.load_matrix(config)`
   (config from Q9; default `DEFAULT_5X5`) then `risk_matrix.score(likelihood,
   severity, matrix)` per hazard. The returned `{score, band, band_action,
   matrix_size}` is authoritative — the band is the engine's, not prose judgement.
   The calibrated 5×5 bands are **Low 1–4 · Medium 5–9 · High 10–15 · Critical
   16–25** (A7 D-02, `multiply` scoring). These band names key the report's
   `palette.risk` colour scale — keep them aligned (A4↔A7 seam).
3. **Select controls — the hierarchy of controls.** Apply `KB-SNIP-HOC`: rank
   **Elimination → Substitution → Engineering → Administrative → PPE**, then call
   `controls.rank_controls` + `controls.validate_treatment`. If the returned
   `ppe_admin_only` is `True`, you **must** add a higher-order control **or** record
   an explicit justification that higher-order controls are not reasonably
   practicable. A lower-order-only treatment with no justification is a defect — the
   Critic/QA pass catches it.
4. **Re-score residual risk.** Re-score each hazard with the selected controls
   applied via `risk_matrix.score`, then `risk_matrix.residual_delta(initial,
   residual)` for the movement. A residual High/Critical band triggers a "more
   controls or stop-work" flag, never "accept and proceed".
5. **SMART actions.** Each control that is an action becomes a SMART action (named
   owner + ISO due date + measure + hazard link), validated by
   `smart_actions.validate_register`. No anonymous or undated actions.

## 2. The environmental-aspects branch (ISO 14001 clause 6.1.2) — Decision 8

Activated only when Q0 = *Environmental* or *Both*. It runs the **same loop shape**
on environmental aspects, reusing the **same `risk_matrix` engine** and the **same
hierarchy of controls** — there is **no new scoring engine**.

1. **Identify aspect → impact pairs** for each activity/product/service (Q-E1/Q-E2/
   Q-E3): emissions to air, releases to water, waste, land contamination,
   resource/energy use. Tag each with its Q-E4 operating condition (normal /
   abnormal / emergency) — emergency conditions often dominate significance.
   Grounded in `KB-STD-ISO14001` 6.1.2.
2. **Score significance with the SAME `risk_matrix.score`** — read the likelihood/
   consequence axes against **environmental consequence descriptors** (scale/extent
   of release, reversibility, duration) rather than injury descriptors. Same
   `MatrixConfig`, same `{score, band, …}` return — only the descriptor semantics
   differ.
3. **Apply the hierarchy of controls to the aspect** — **eliminate or substitute the
   aspect first** (switch to an aqueous degreaser; enclose + carbon-capture the VOC;
   close-loop the solvent) before mitigating. The same `ppe_admin_only` rule applies.
4. **Re-score residual significance** and show the movement.
5. **SMART actions** for each environmental control, same validation.

The environmental basis (ISO 14001 6.1.2 + any Q-E5 compliance obligations —
discharge consents, emission limits, waste licences) is added to the report's
regulatory-basis section.

## 3. Output / report assembly

Assemble one `report.json` (`hse-report-model/v1`) from `assets/hira-report.template.json`
and run the canonical `report-output` call. House section order (A4): executive
summary → scope & method → key findings (risk register) → [environmental
aspects/impacts register, branch only] → hierarchy of controls → residual risk →
recommendations → regulatory basis. The engine auto-stamps the cover,
classification, TOC, and the limitations/de-id notice.

**Risk-register block form (D-04):** render the safety risk register and the
environmental aspects/impacts register as A4 **`findings` risk-rated cards by
default** (richer, evidence-per-hazard). For a **long register (> ~10 hazards)** fall
back to a **`table` with `risk_column`** for density — both are A4-native, so this is
a presentation knob, not a contract change. The `risk_level` value uses the band
names from step 2 so the `palette.risk` colour scale resolves.

## 4. Evidence & defensibility

Every hazard names what is hazardous and who is exposed; every score is the engine's;
every control is HoC-ranked; every action has a named owner and an ISO date; every
citation traces to the KB (ISO 45001 6.1.2 always; ISO 14001 6.1.2 when the branch
ran; India → the resolved state form via `KB-REG-IN-STATEFORMS`, never a national
number). No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` /
`[GAP]` only. De-identification runs first; the output is decision-support and must
be reviewed by a competent person.
