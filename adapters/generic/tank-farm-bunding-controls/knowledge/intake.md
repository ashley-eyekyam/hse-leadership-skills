---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION, ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}   # none material
  branches:
    - {when: Q4, option: flammable, activates_questions: [Q7]}
    - {when: Q7, option: watercourse, activates_questions: [Q6]}
    - {when: Q9, option: India, activates_questions: [Q10], mandatory: true}
---

# Structured intake — tank-farm-bunding-controls

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a sizing %).
Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — size/verify a bund, plan secondary containment, or review overfill/segregation controls? | MCQ | bund-sizing / containment-plan / controls-review | ELI-SCOPE | always |
| Q2 | List each stored substance + tank volume; flag the **largest single tank**. | free-text | per-tank volume + largest; refuse "bulk solvents" | ELI-SUBJECT | always |
| Q3 | How many tanks share the bund, and any incompatible pairs? | free-text | drives segregation | ELI-SUBJECT | always |
| Q4 | Substance flashpoint / DG class for each (flammable / toxic / corrosive). | MCQ multi-select + free-text | flammable / toxic / corrosive / inert | ELI-EVIDENCE | always |
| Q5 | Storage configuration. | MCQ | atmospheric / pressurised / refrigerated · single / bunded-group | ELI-SUBJECT | always |
| Q6 | Existing containment + overfill protection + drainage + firewater. | free-text | current bund %, overfill trip, drainage interceptor, firewater retention | ELI-BASELINE | always |
| Q7 | Proximity to watercourse, surface drain, or site boundary? | MCQ + free-text | watercourse / drain / boundary / none — spill-migration receptor | ELI-EXPOSURE | always |
| Q8 | Which containment-sizing rule applies (or should I resolve it)? | MCQ | largest-tank+freeboard / 110% local rule / PESO-OISD / resolve-for-me | ELI-SCORING | always |
| Q9 | Jurisdiction — India? | MCQ | UK/EU / US / India / other | ELI-JURIS | always |
| Q10 | Which Indian state? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — mandatory state detection; confirm before citing any PESO/state form; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | if Q9==India |
| Q11 | PESO/storage licence held + validity, and bund inspection cycle? | free-text | licence + dates | ELI-OBLIGATIONS / ELI-TEMPORAL | always |
| Q12 | Site location / tank-farm layout, and who owns the containment actions? | free-text | site/area + role-label owner | ELI-LOCATION / ELI-COMPETENCY | always |
| Q13 | Industry / sector context for the stored inventory. | MCQ + free-text | O&G terminal / chemicals / fuel depot / general (+ detail) | ELI-INDUSTRY | always |

**Branch map**
- `Q3` incompatible pairs present → activate segregation / separate-bund requirement (METHODOLOGY step 2/4).
- `Q4 == flammable` → activate DSEAR flammable-atmosphere area control (`KB-STD-DSEAR`) + firewater-retention sizing.
- `Q7 ∈ {watercourse, drain}` → activate drainage-containment + firewater-retention (environmental spill-migration) output section.
- `Q8` → resolves the sizing basis **from the rule, never an assumed %** (METHODOLOGY step 3); `resolve-for-me` → cite the applicable rule; unresolved local rule → `[GAP]`.
- `Q9 == India` → Q10 state (**mandatory**) → PESO/state storage licensing pointers (`KB-REG-IN-PESO`, `KB-REG-IN-STATEFORMS`); "Other"/"Unknown" → literal `[GAP]`.

## Echo-back
> "Tank farm **{site}**: substances **{list+volumes}**, largest tank **{vol}**; **{n}** tanks/bund, incompatible pairs **{pairs}**; classes **{flammable/toxic/...}**; configuration **{atmos/press/refrig · single/group}**; existing containment **{detail}**; receptors **{watercourse/drain/boundary}**; sizing rule **{rule}**; jurisdiction **{juris(+state)}**; licence **{detail}**. I will state the containment basis from the rule (not an assumed %), segregate by incompatibility, HoC-rank the controls, and flag any unresolved rule `[GAP]`. Confirm."

Echo the captured facts back and **confirm before stating the containment basis**. The
named action-owner is held as a role label in the echo-back.

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "bulk solvents" → demand named substances + volumes; **never proceed on a vague subject**.
- Sizing % asserted without a rule → resolve from the rule, never an unstated assumed percentage (METHODOLOGY).
- Unresolved local containment rule → `[GAP]`, route to competent person.

**Domain evidence types (`ELI-EVIDENCE`)**
Tank schedule (volumes, largest tank), SDS / DG class / flashpoint per substance, compatibility matrix, existing bund integrity / leak-test records, site drainage plan + receptor proximity, PESO/OISD/local containment rule, PESO licence.
