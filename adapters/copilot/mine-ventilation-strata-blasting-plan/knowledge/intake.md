---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-LOCATION, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-OBLIGATIONS: "narrows to the Mines Act/DGMS plan-duty citation — plans are site documents, not numbered forms."
    ELI-EXPOSURE: "the exposed population is folded into the plan-type parameter set — districts (ventilation) and the blast-exclusion zone (blasting) define who is exposed."
    ELI-TEMPORAL: "plan review cycle only — a light review-on-change/annual default, not a statutory deadline."
  branches:
    - ask: ELI-SCOPE
      when: Q1
      option: "ventilation"
      activates_questions: [Q4V]   # ventilation parameter set
    - ask: ELI-SCOPE
      when: Q1
      option: "strata-ground-control"
      activates_questions: [Q4S]   # strata parameter set
    - ask: ELI-SCOPE
      when: Q1
      option: "blasting-shotfiring"
      activates_questions: [Q4B]   # blasting parameter set
    - ask: ELI-SCOPE
      when: Q1
      option: "review-existing"
      activates_output_section: gap-check
    - ask: ELI-JURIS
      when: Q3
      equals: "infer-then-confirm the DGMS region and the **state** if the jurisdiction is India"
      activates_questions: [Q3]   # India -> DGMS region/state infer-then-confirm (mandatory)
    - ask: ELI-INDUSTRY
      when: Q2
      option: "a) Coal — UG"
      # coal-UG surfaces methane/firedamp + gas-category emphasis; opencast -> highwall/blast-vibration
---

# Structured intake — mine-ventilation-strata-blasting-plan

Run **one question at a time** (`KB-SNIP-INTAKE`). MCQ where the answer space is
enumerable, free-text where it is open; **branch on the answers**; **echo the captured
facts back before any drafting**; **refuse on a vague subject** — a generic-template request
is rejected ("the parameters are the plan"), a PPE/admin-only control of a principal hazard
is flagged/escalated, and a missing engineering value is `[GAP]`, **never fabricated**.

**The plan type (Q1) activates exactly one parameter set** (Q4V / Q4S / Q4B). For India the
**DGMS region/state (Q3) is resolved infer-then-confirm**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Which plan + new or review? | MCQ | ventilation / strata-ground-control / blasting-shotfiring / draft-new / review-existing | ELI-SCOPE | always |
| Q2 | Commodity + mine type? | MCQ | a) Coal — UG / b) Coal — opencast / c) Metalliferous — UG / d) Metalliferous — opencast / e) Other | ELI-INDUSTRY | always (branch driver) |
| Q3 | DGMS region / state (India)? | MCQ→confirm | infer-then-confirm the DGMS region and the **state** if the jurisdiction is India | ELI-JURIS/ELI-LOCATION | India |
| Q4V | Ventilation parameters | free-text | "Gas regime / seam gassiness category, required air quantity & quality, method (forcing/exhausting/booster), districts, gas-monitoring setup" | ELI-SUBJECT/ELI-EVIDENCE | Q1=ventilation |
| Q4S | Strata parameters | free-text | "Seam/orebody geology + depth, roof/highwall conditions, support regime (bolt/prop/standing), geotech/convergence data" | ELI-SUBJECT/ELI-EVIDENCE | Q1=strata |
| Q4B | Blasting parameters | free-text | "Explosive type, blast design (burden/spacing/charge/delay), exclusion zone, misfire procedure, vibration/flyrock limits" | ELI-SUBJECT/ELI-EVIDENCE | Q1=blasting |
| Q5 | Principal hazards to address? | mcqmulti-select | confirm from `KB-DATA-MINING-HAZARDS` for the selected plan type | ELI-SUBJECT | always |
| Q6 | Sign-off competent person (role)? | free-text | "Ventilation officer / shotfirer / geotech engineer / mine manager — as a role label" | ELI-COMPETENCY | always |
| Q7 | Risk-rating scheme? | MCQ | a) Org's existing matrix / b) Default 5×5 (D-02 bands) — confirm | ELI-SCORING | always |
| Q8 | Output + distribution? | MCQ | a) Plan document / b) Plan + gap-check / c) Review notes | ELI-OUTPUT | always |

## Branch map
- **Q1 plan type** → activates exactly one of **Q4V / Q4S / Q4B** (the parameter set) and the
  matching hazard subset of Q5.
- **Q1 review-existing** → a **gap-check output section** against the existing plan.
- **Q2 coal-UG** → the ventilation branch surfaces methane / firedamp + gas-category
  questions; **opencast** → highwall / blast-vibration emphasis.
- **Q3** (India) resolves the DGMS region / state, infer-then-confirm.
- Hazard ranking via `risk_matrix` (5×5, D-02 bands, Q7); a PPE/admin-only treatment of a
  principal hazard → escalated / justified, never accepted.
- Any unsupplied engineering value → `[GAP]`, never fabricated.

## Echo-back
"**{plan type}** plan (**{new / review}**) for **{mine, commodity / type}** (DGMS
**{zone}**); key parameters **{summary}**; hazards **{list}**; sign-off **{role}**. Confirm
before I draft." — echo the captured facts back and **confirm** before any drafting.

## Refuse-on-vague anchors
- **"Write a ventilation plan"** with no air quantity / gas regime → ask (the parameters are
  the plan).
- A **generic-template request** → reject ("the parameters are the plan").
- A **PPE/admin-only control of a principal hazard** → flag / escalate.
- **Missing engineering value** → `[GAP]`, never fabricate.

## Domain evidence types (ELI-EVIDENCE)
Gas-monitoring / firedamp survey data; ventilation survey (air quantity / quality); geotech
borehole & convergence-monitoring logs; seam / orebody geology; blast vibration & flyrock
records; explosive magazine / inventory.
