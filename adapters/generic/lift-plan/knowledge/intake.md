---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-SCORING: "The lift's residual risk is scored on the org's risk matrix at the residual-scoring step via the A7 risk_matrix engine (default 5×5), not asked up front — and the SWL-at-radius / utilisation are READ from the manufacturer's rated-capacity chart (Q3), never scored by a calculator. So a dedicated matrix-size question is not asked at intake; the skill defaults the matrix and re-confirms on the residual rows."
  branches:
    - {when: Q1, option: Complex, activates_output_section: appointed-person-written-plan-contingency, mandatory: true}
    - {when: Q4, option: Overhead power lines, activates_output_section: exclusion-zones-segregation, mandatory: true}
    - {when: Q6, option: UK, activates_kb_row: KB-REG-CDM2015, activates_output_section: loler-bs7121-basis, mandatory: false}
    - {when: Q6, option: USA, activates_kb_row: KB-REG-OSHA1926, activates_output_section: osha-1926-basis, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: india-state-gap, mandatory: true}
---

# Structured intake — lift-plan

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**.

**The GATE (refuse-on-vague):** **no lift plan is produced** until all three of **a confirmed
load weight including rigging (Q2)**, **the equipment SWL at the working radius (Q3)**, and —
for a standard / complex lift — **a named appointed person (Q5)** are captured. The skill
**refuses to plan on an unconfirmed weight, an unknown SWL-at-radius, or a "should-be-fine"
ground** — ask again, or record `[ASSUMPTION]` / `[GAP]`; **never invent a chart value, a
weight, or a clearance.** **SWL-at-radius and utilisation are READ from the manufacturer's
rated-capacity chart** (transcribed at Q3 and checked against `KB-DATA-LIFT-CATEGORIES`) —
**the skill never computes a crane capacity** (D-08a).

**Jurisdiction paths:** the **UK → LOLER 1998 Reg 8 / BS 7121 branch** (Q6 = UK →
`loler-bs7121.md` + CDM 2015 where the lift is construction works; non-mandatory) and the
**mandatory India → state branch** (Q6 = India → Q6a + `KB-REG-IN-STATEFORMS`, **defers to
`hse-india`, mandatory state detection, literal `[GAP]`, never a minted national form
number**). The **complexity branch** (Q1 = complex / tandem / blind → the appointed-person
**written** plan + contingency / abort section is mandatory) and the **overhead-line branch**
(Q4 = overhead power lines → the exclusion-zones / segregation section is mandatory) tune the
plan.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Lift classification (BS 7121)** | MCQ | Basic / Standard / Complex; a tandem (multi-crane) lift, a blind lift, a lift over the public or an occupied area, a load near the SWL, poor or unknown ground, or overhead-line proximity is **Complex** and mandates an appointed-person WRITTEN plan + contingency / abort (the highest triggered criterion sets the category, per `KB-DATA-LIFT-CATEGORIES`) | ELI-SCOPE / ELI-OUTPUT | always |
| Q2 | **The load (the specificity anchor)** | free-text | "Describe the load: item, **confirmed weight including rigging/lifting accessories**, dimensions, centre of gravity, lifting points (e.g. '12 t packaged AHU + 0.8 t rigging = 12.8 t, 4.2 × 2.1 × 2.4 m, CoG marked, 4 certified lifting points')." — **refuse to plan without a confirmed weight; an unconfirmed weight is a `[GAP]`, never assumed** | ELI-SUBJECT | always |
| Q3 | **The equipment & SWL-at-radius** | free-text | "Crane type & configuration (counterweight, boom, outriggers), and the **SWL at the planned working radius + the utilisation %, READ FROM the manufacturer's rated-capacity chart** (e.g. '50 t mobile, 28 m boom, SWL 14.2 t at 12 m radius per Liebherr LTM-1050 chart 2021 → 12.8 / 14.2 = 90% utilisation'). **Transcribe the chart value — the skill does not compute it.**" — utilisation over the planned safe-utilisation margin → re-select the equipment | ELI-BASELINE / ELI-OBLIGATIONS | always |
| Q4 | **Site & proximity hazards** | MCQ multi-select + free-text | Overhead power lines / Adjacent structures / Public or highway / Poor or unknown ground / Confined radius / SIMOPS (simultaneous operations) / Other (+ detail) — drives the exclusion-zones & segregation section and the HoC controls | ELI-EXPOSURE / ELI-LOCATION | always |
| Q5 | **Personnel & competence** | free-text | "Name the **appointed person** (who plans / supervises the lift), the **crane operator**, and the **slinger / signaller** — each with the competence basis (CPCS / NPORS / appointed-person training). **Name them for the lift-plan record** (a standard / complex lift cannot proceed without a named appointed person)." — never invent an appointment (record `[GAP]`); **do not include any worker's medical-fitness / health note in this record** | ELI-COMPETENCY | always |
| Q6 | **Jurisdiction** | MCQ | UK / USA / India / EU / Unknown — UK → LOLER 1998 Reg 8 / Reg 9 + BS 7121 (+ CDM 2015 if construction works); USA → 29 CFR 1926 Subpart CC; India → Q6a + state crane rules via `hse-india`; Unknown → ask before citing | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; confirm the state before citing any form; emit a literal `[GAP]`, never a minted national form number** | ELI-JURIS | Q6 == India |
| Q7 | **Existing controls / arrangements** | free-text | "What is already in place — ground assessment / outrigger mats, a permit-to-lift, trial-lift / weighing arrangements, communication plan, a banksman?" (seeds the initial-vs-residual baseline) | ELI-BASELINE | always |
| Q8 | **Weather / environmental limits + evidence held** | free-text | "The in-service wind limit (from the chart), any weather constraints, and the evidence you hold — the rated-capacity chart, the ground / outrigger-loading report, the thorough-examination (LOLER Reg 9) certificate, the lifting-accessory certs (or 'none' → I'll flag `[GAP]`)" | ELI-EVIDENCE | always |
| Q9 | **Lift window & review trigger** | free-text | "When is the lift planned, and what triggers a re-plan/re-brief (change of crane, load, radius, ground, or weather beyond the limit)?" | ELI-TEMPORAL | always |

*ELI-INDUSTRY thin-covered (always construction / lifting; Q2/Q4 detail). ELI-OUTPUT is set by Q1 (the category sets the planning depth / artifact).*

**Branch map:** `complex` (Q1 = complex / tandem / blind → the **mandatory** appointed-person
written plan + contingency / abort section); `overhead-line` (Q4 = overhead power lines → the
**mandatory** exclusion-zones / segregation section); `uk-loler` (Q6 = UK → `loler-bs7121.md`
+ the LOLER Reg 8 / BS 7121 basis, + `KB-REG-CDM2015` if construction works; non-mandatory);
`us-osha` (Q6 = USA → `KB-REG-OSHA1926`; non-mandatory); `india-state` (Q6 = India → Q6a +
`KB-REG-IN-STATEFORMS`, **mandatory** state detection, defers to `hse-india`).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before any
analysis: "Lift plan for a **standard** lift: 12.8 t AHU (incl. rigging) onto the level-6
plant deck, 50 t mobile crane, **SWL 14.2 t at 12 m → 90% utilisation (read from the chart)**,
overhead-line + confined-radius proximity, appointed person + operator + slinger named, UK /
LOLER Reg 8 + BS 7121, in-service wind limit per chart, re-plan on crane/load/radius change —
correct?" The residual risk for each hazard is scored on the org's matrix at the
residual-scoring step (the SWL / utilisation are NOT scored — they are read from the chart).

## Refuse-on-vague anchors

- **The GATE:** Q2 (a confirmed load weight incl. rigging), Q3 (the equipment SWL at the
  working radius), and Q5 (a named appointed person for a standard / complex lift) are
  load-bearing — **refuse an unconfirmed weight, an unknown SWL-at-radius, or a "should-be-fine"
  ground**; never invent a chart value, a weight, a clearance, or an appointment (record
  `[GAP]`).
- **SWL-at-radius / utilisation are READ, not computed** — they are transcribed from the
  manufacturer's rated-capacity chart at Q3 and checked against `KB-DATA-LIFT-CATEGORIES`; a
  chart value the user has not supplied is a `[GAP]`, never calculated.

## Domain evidence types (ELI-EVIDENCE)

The manufacturer's **rated-capacity chart** (the SWL-at-radius source) · the **ground /
outrigger-loading report** · the **LOLER Reg 9 thorough-examination certificate** · the
lifting-accessory certificates · any prior lift plan / method statement for this load or area
· the in-service wind limit · prior dropped-load / near-miss history for this crane or task
(de-identified).
