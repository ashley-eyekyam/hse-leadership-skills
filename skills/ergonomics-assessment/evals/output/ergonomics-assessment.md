# Ergonomics Assessment — Despatch-Bay Carton Lift (line-2 packer SEG, Plant 3)

*Decision-support only. A competent person (ergonomist / occupational-health professional) must
review and sign off this assessment. Special-category MSD/fitness data — reported by role/SEG
with `<5` small-cell suppression; the re-identification key is held separately.*

## 1. Task / workstation description

De-identification ran first: worker names and the individual reported back-injury / fitness note
were scrubbed to role/SEG labels; no named fitness note and no `<5` symptom cell appears below.

- **Task:** despatch-bay carton lift — cartons lifted from a floor-level pallet to the conveyor infeed.
- **Role / SEG:** line-2 packer SEG, Plant 3.
- **Method:** NIOSH revised lifting equation (1991) — selected at Q1 because the hazard is a manual lift.

## 2. Method & inputs (the scored parameters)

| Parameter | Captured value | Source |
|---|---|---|
| Load weight | 16 kg | measured |
| Horizontal location H | 30 cm | measured |
| Vertical origin V | 40 cm | measured |
| Vertical travel D | 110 cm (origin 40 → destination 150) | measured |
| Asymmetry angle A | 30° | measured |
| Frequency | 4 lifts/min | measured |
| Duration | 2 h | measured |
| Coupling | fair | observed |

Every score below traces to these captured parameters. No parameter was invented; a missing
required parameter would be recorded as a `[GAP]` and the measurement requested.

## 3. Computed score & action band (deterministic `ergonomics` engine)

Computed via `ergonomics.niosh_rwl(...)` then `ergonomics.to_report_blocks(result)` — the
`[metrics, table]` pair below is the engine's output:

| Metric | Value |
|---|---|
| Recommended Weight Limit (RWL) | **8.62 kg** |
| Lifting Index (LI = load ÷ RWL = 16 ÷ 8.62) | **1.86** |

| Multiplier | Value |
|---|---|
| HM (horizontal) | 0.83 |
| VM (vertical) | 0.90 |
| DM (distance) | 0.86 |
| AM (asymmetry) | 0.90 |
| FM (frequency) | 0.72 |
| CM (coupling) | 0.90 |

`RWL = LC(23) × HM × VM × DM × AM × FM × CM = 8.62 kg`.

## 4. Risk interpretation

The **Lifting Index is 1.86 (> 1.0)** — the lifting demand exceeds the NIOSH recommended weight
limit, indicating **elevated MSD (low-back) risk**. Interpretation cited to the NIOSH revised
(1991) lifting equation; the dominant penalties are the frequency multiplier (FM 0.72, 4
lifts/min over 2 h) and the horizontal reach (HM 0.83). This is not a borderline result —
control action is required.

## 5. Hierarchy-ranked controls

| Control | Tier | Owner |
|---|---|---|
| Raise the pallet on a spring positioner / scissor-lift so the lift origin is at knuckle height (raises V, removes the floor reach) | Engineering | Production Engineering Lead |
| Provide a vacuum lift-assist for the heavier cartons (mechanical aid) | Engineering | Production Engineering Lead |
| Rotate packers off the despatch lift on a defined cycle to cut cumulative exposure | Administrative | Despatch Supervisor |
| Manual-handling technique refresher — supports, does **not** replace, the redesign | Training | HSE Manufacturing |

> A Lifting Index of 1.86 whose only control were manual-handling training would be **training-led
> and inadequate** — training is not a control for a biomechanical overload. The task/workstation
> redesign (positioner / lift-assist) is the primary control; the LI must be re-scored to ≤ 1.0
> after the positioner is installed.

## 6. Surveillance / symptom linkage

- Re-score the lift with the engine after the pallet positioner / lift-assist is installed (target LI ≤ 1.0).
- Symptom-triggered review: any reported lower-back or shoulder symptom in the packer SEG triggers
  a re-assessment (reported by SEG, `<5` cells suppressed).
- Routine re-assessment on task change or annually, whichever is sooner.

## 7. Owned / dated actions

| Action | Priority | Owner | Due |
|---|---|---|---|
| Install the spring pallet positioner at the despatch lift origin | P1 | Production Engineering Lead | 2026-07-20 |
| Trial a vacuum lift-assist for cartons over 15 kg | P2 | Production Engineering Lead | 2026-08-15 |
| Re-score the lift with the engine after the positioner is installed | P2 | HSE Manufacturing | 2026-08-30 |

## 8. Assumptions / [GAP]

- No required NIOSH parameter was missing for this lift; any gap would be recorded here and the
  score withheld until measured — no parameter invented.
- India site (if applicable): the Factories Act health-provision return is resolved via
  `hse-india` with mandatory state detection; a state return owed is recorded as a `[GAP]`,
  never a national form number.

## 9. Review & sign-off

SME review (Chartered Ergonomist (CIEHF) / Occupational-Health Professional) ran and precedes —
and never replaces — the human competent-person sign-off. Regulatory basis: ISO 45001 §6.1.2 /
§8.1.2 (`KB-SNIP-MANUFACTURING-CLAUSE-MAP`); NIOSH revised lifting equation (1991); RULA / REBA;
ISO 11228-1/-2/-3.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
