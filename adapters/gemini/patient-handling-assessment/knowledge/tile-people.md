<!-- KB-SNIP-TILE-PEOPLE -->
# TILE for people — move-toward-zero manual lifting of patients

**Fragment ID:** `KB-SNIP-TILE-PEOPLE`
**This is prompt text, applied by the model — not a generator.** It is the
patient-handling assessment + control gate for `hse-healthcare`: assess each
handling task by the **TILE** factors (Task, Individual, Load, Environment) and
apply the **avoid → assess → reduce** order, moving toward **zero / minimal manual
lifting of people** with mechanical aids as the default.

> Source: MHOR 1992 reg 4 + Schedule 1 (TILE) + ANA SPHM + the hierarchy of controls (`KB-SNIP-HOC`) — assessment + control prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — TILE assessment + move-toward-zero control order

1. **Avoid (first).** Can the manual handling of the person be avoided — can a
   mechanical aid, a reposition, or a different approach remove the manual lift?
   Record the avoid decision.
2. **Assess the unavoidable handling by TILE:**
   - **Task** — what is being done (lift, transfer, reposition, hold), distance,
     posture, repetition, twisting.
   - **Individual** — the handler's capability, training, and any limitation; the
     number of handlers.
   - **Load** — the patient: weight, dependency, cooperation, attachments (lines,
     drains), bariatric considerations, falling risk.
   - **Environment** — space, floor, bed/chair height, equipment availability,
     obstructions.
3. **Reduce.** Apply controls in order: mechanical lift/transfer equipment and
   slide aids first; then technique, handler numbers, and environment changes;
   manual lifting of the person only as the documented last resort.
4. **Score residual risk** on the shared `risk_matrix` 5×5; assign SMART actions.

## The gate (reject these)
- A control plan that defaults to "two staff lift" without first applying mechanical
  aids → **reject** (move-toward-zero not applied).
- A treatment that omits any of the four TILE factors → **reject** as not suitable
  and sufficient.
- Reporting a small handling-injury population in a way that allows
  re-identification → **reject** (apply small-cell suppression).

## How the skill uses this fragment
`patient-handling-assessment` (HC-03) assesses by TILE and applies the
move-toward-zero order here, grounded on MHOR (`KB-REG-UK-MHOR`) and SPHM
(`KB-STD-SPHM`); residual risk uses `risk_matrix`. No skill restates the logic in
its own body (anti-drift).
