# Methodology — Ergonomics assessment (method → parameters → engine score → action band → controls → surveillance)

This is the domain method `ergonomics-assessment` applies. The SKILL.md Workflow is the
operational summary; this file is the full reference. Every score is the deterministic
`ergonomics` engine's output (RULA / REBA / NIOSH — grounded in `KB-STD-ISO11228`), every
control is ranked through the hierarchy of controls (task/workstation redesign before
PPE/training), and every action carries a named owner and a date — never a narrated score,
never a guessed parameter, never a training-led treatment of a biomechanical overload.

## 0. De-identify first — special-category MSD/fitness data

Reported MSD symptoms and medical-fitness notes are **GDPR Art. 9 / India DPDP special-category
health data**. Before any drafting (the `deid` block + `references/deid-checklist.md`): scrub
names to stable role/SEG labels, **report reported symptoms by role/SEG not by individual**,
apply `<5` small-cell suppression to any symptom/outcome breakdown, and **never circulate a
named back-injury or fitness note**. The re-identification key is held separately, never embedded.

## 1. Select the method (Q1) and capture its required parameters (Q3)

From Q1, select the scoring method and branch to its required parameters. Refuse a generic task
("general handling"); each scored item names the task/role and the workstation. **Refuse to
score on a missing required parameter** — record `[GAP]` and request the measurement; never
invent a posture angle or a load weight.

- **NIOSH lifting equation** (manual lifting/lowering): load weight (kg); horizontal location H
  (cm); vertical location at origin V (cm); vertical travel distance D (cm); asymmetry angle A
  (degrees); frequency (lifts/min); duration (h); coupling (good/fair/poor).
- **RULA** (upper-limb/posture): upper arm, lower arm, wrist, wrist-twist, neck, trunk, legs
  joint scores; muscle-use and force/load add-ons per group.
- **REBA** (whole-body posture): trunk, neck, legs, load/force; upper arm, lower arm, wrist,
  coupling; activity score.
- **ISO 11228-2 push/pull · 11228-3 repetitive · DSE/workstation**: assessed against the ISO
  11228 method scope (`KB-STD-ISO11228`), with the relevant captured parameters.

## 2. Score deterministically with the engine

Call the `ergonomics` engine via the `scripts/hse_components` symlink for the Q1 method —
**the score is the engine's, never narrated free-text** (grounded in `KB-STD-ISO11228`):

```python
from hse_components import ergonomics

# NIOSH lift
r = ergonomics.niosh_rwl(weight=16, h=30, v=40, d=110, a=30,
                         frequency=4, duration=2, coupling="fair")
# or RULA upper-limb
r = ergonomics.rula_score(upper_arm=3, lower_arm=2, wrist=2, wrist_twist=1,
                          neck=2, trunk=2, legs=1, muscle_use_a=1, force_a=0)
# or REBA whole-body
r = ergonomics.reba_score(trunk=2, neck=1, legs=1, load_force=1,
                          upper_arm=3, lower_arm=2, wrist=2, coupling=1, activity=1)

blocks = ergonomics.to_report_blocks(r)   # -> exactly a [metrics, table] pair
```

`to_report_blocks(result)` returns the tool-named **`[metrics, table]`** pair (NIOSH RWL +
Lifting Index / RULA grand score + action level / REBA final score + action level) that drops
straight into `report.json`'s "Computed score & action band" section. Out-of-range inputs raise
`ErgonomicsInputError` — fix the input, never a silent clamp; the NIOSH equation's published
out-of-domain zeroes (H>63, V>175, D>175, A>135 → multiplier 0) are the method, not an error.

## 3. Interpret against the method's action band

Interpret the engine result against the published action band: NIOSH **Lifting Index > 1.0**
exceeds the recommended limit (elevated risk); RULA **action level** (1 acceptable → 4
investigate & change now); REBA **action level** (negligible → very high). The interpretation is
cited to the method, never asserted.

## 4. Rate residual MSD risk & rank controls up the hierarchy

Rate residual MSD risk on `risk_matrix.score`. Apply `KB-SNIP-HOC` + `KB-SNIP-ERGO-CONTROLS`
and call `controls.rank_controls` + `controls.validate_treatment`: **eliminate the handling →
engineer the workstation / mechanise / add an aid → administrative rotation/limits → training
LAST**. A high RULA/REBA/LI whose only control is manual-handling training is **training-led
and inadequate** — training is **not** a control for a biomechanical overload; push it up the
hierarchy (task/workstation redesign first) **or** record an explicit "higher-order controls
not reasonably practicable because…" justification. If `ppe_admin_only` is `True`, add a
higher-order control or the justification.

## 5. Link symptoms to a surveillance / re-assessment cadence

Reported MSD symptoms (Q5) and the exposure pattern (Q4) drive a symptom-surveillance /
re-assessment cadence (e.g. re-score on task change, symptom-triggered review). Surveillance
outcomes are reported by role/SEG with `<5` suppression.

## 6. SMART actions (named owners + dates)

Every redesign / aid / surveillance action becomes a SMART action (named role owner + ISO due
date + measure), validated by `smart_actions.validate_register`. No anonymous or undated
actions, no "ASAP".

## 7. Output / report assembly

Assemble one `report.json` (`hse-report-model/v1`) from
`assets/ergonomics-assessment.report.json` and run the canonical `report-output` call. Section
order: Task/workstation description → Method & inputs → **Computed score & action band (the
engine `[metrics, table]` pair)** → Risk interpretation → Hierarchy-ranked controls →
Surveillance/symptom linkage → Owned/dated actions → Assumptions/`[GAP]` → Review & sign-off.

## 8. Evidence & defensibility

Every task named; every score the engine's with its inputs shown; every missing parameter a
`[GAP]`, never a guess; every control HoC-ranked above PPE and above training; every action
owned + dated; every citation traced to the KB. The output is **decision-support**; a competent
person (ergonomist / occupational-health professional) must review it. India defers to
`hse-india` with mandatory state detection; a state return owed is a `[GAP]`, never a minted
national form number.
