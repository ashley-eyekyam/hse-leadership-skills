<!-- KB-SNIP-PPE-MATRIX-LOGIC -->
# PPE-matrix logic — residual-hazard-only selection + controls-first gate

**Fragment ID:** `KB-SNIP-PPE-MATRIX-LOGIC`
**This is prompt text, applied by the model — not a generator.** It is the
residual-hazard-only PPE-selection logic and the **controls-first gate** for a
PPE-matrix skill: higher-order controls must be applied or justified **before** any PPE
is specified. It is the literal spine of #4's controls-first gate. Consumed by
`ppe-matrix` (MFG-04).

> Source: OSHA 29 CFR 1910 Subpart I (1910.132 hazard assessment + written certification) + the hierarchy of controls · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the controls-first gate, then PPE by residual hazard

1. **Controls-first gate** — for each body-region hazard, confirm the higher-order
   controls (eliminate / substitute / engineer / administrative) have been **applied or
   justified** (`KB-SNIP-HOC`). PPE is specified only for the **residual** hazard that
   survives those controls — never as the headline control.
2. **PPE hazard assessment** — assess by body region and task (1910.132(d)(1)).
3. **Select the PPE type** against the named residual hazard, and **cite the conformity
   standard** for the jurisdiction (`KB-DATA-PPE-STANDARDS`); do not assert protection
   without the standard.
4. **Written certification** — produce the 1910.132(d)(2) certification block (who
   assessed, what, date) — it is mandatory.

## Discipline
- A PPE matrix that lists PPE for a hazard with no higher-order control applied or
  justified fails the controls-first gate.
- Never assert a protection level without the cited conformity standard + year.
- A missing input (no task, no hazard) is a `[GAP]`; the written certification is never
  omitted.

## How the skill uses this fragment
`ppe-matrix` runs the controls-first gate per body-region hazard, selects residual-only
PPE against the cited standard (`KB-DATA-PPE-STANDARDS`), grounds the duty on
`KB-REG-OSHA1910-I`, and emits the PPE-matrix grid + certification block.
