<!-- KB-SNIP-HOC -->
# Hierarchy of Controls — canonical control-ranking instruction

**Fragment ID:** `KB-SNIP-HOC`
**This is prompt text, applied by the model — not a generator.** The deterministic
risk-matrix / HOC scoring engine is A7 (Phase 3); this snippet is the instruction the
model *and* that script both honour. Referenced by every skill via the kb-selection
rubric's "always apply" line, never inlined, so the wording lives in one place.

> Source: hierarchy of controls (ISO 45001 8.1.2 / NIOSH / EU general principles of prevention) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false.

---

## Instruction (apply to EVERY control recommendation)

Rank every control you propose through the hierarchy of controls, **most effective
first**:

1. **Elimination** — remove the hazard entirely (design it out, stop the task).
2. **Substitution** — replace the hazard with a less hazardous alternative.
3. **Engineering controls** — isolate people from the hazard (guarding, ventilation,
   interlocks, barriers).
4. **Administrative controls** — change how people work (procedures, training,
   permits, signage, rotation).
5. **PPE** — protect the individual as the last line of defence.

For each control you MUST:

- **Name the specific hazard it addresses** — never a generic "wear PPE" or "be
  careful". State *which hazard*, *which control*, *which level*.
- **State its level** (Elimination / Substitution / Engineering / Administrative / PPE).

## Mandatory flag — lower-order-only recommendations

If a recommendation is **PPE-only** or **Administrative-only** (no higher-order
control proposed for that hazard), flag it explicitly:

> **Lower-order control — justify why higher-order controls (elimination /
> substitution / engineering) are not reasonably practicable, or escalate.**

Do not present PPE or administrative measures as a complete treatment of a hazard
that admits an engineering or substitution control. This operationalises the project's
core value: **no PPE-only treatments**.

## Output expectation

Controls are presented ranked, each tied to its named hazard and level, with any
lower-order-only control carrying the justification-or-escalate flag. This feeds the
eval `specificity` and `hierarchy_of_controls` dimensions (A8).
