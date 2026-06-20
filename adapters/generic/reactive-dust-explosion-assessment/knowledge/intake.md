---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION, ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-TEMPORAL]
  omits:
    ELI-COMPETENCY: "kept light — actions get role-owners via smart_actions; the deep study is handed to hazop-facilitator, where the competent-person locus sits"
  branches:
    - {when: Q3, option: combustible dust, activates_questions: [Q4, Q5]}
    - {when: Q3, option: reactive chemistry, activates_questions: [Q6]}
    - {when: Q1, option: zoning, activates_questions: [Q9]}
---

# Structured intake — reactive-dust-explosion-assessment

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a dust
parameter). Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — a DHA, a reactive-chemistry/incompatibility review, an ATEX/DSEAR zoning, or a basis-of-safety statement? | MCQ | DHA / reactivity-review / zoning / basis-of-safety | ELI-SCOPE | always |
| Q2 | Named process + material(s). | free-text | refuse "some powder" | ELI-SUBJECT | always |
| Q3 | Hazard scope. | MCQ | reactive chemistry / combustible dust / explosive vapour atmosphere / combination | ELI-SUBJECT | always |
| Q4 | List the dust-generating / handling steps + equipment. | free-text | milling/conveying/bagging/dust-collector/silo | ELI-LOCATION | if Q3∈{dust,combination} |
| Q5 | Dust characterisation data held. | MCQ multi-select | Kst / Pmax / MIE / MIT / LOC / particle-size / moisture / none | ELI-EVIDENCE | if Q3∈{dust,combination} |
| Q6 | Reactive-chemistry data held. | MCQ multi-select | DSC/ARC onset / heat-of-reaction / incompatibility matrix / CHETAH screen / none | ELI-EVIDENCE | if Q3∈{reactive,combination} |
| Q7 | Lab source + year for each datum held. | free-text | required for citation; missing → `[GAP]` | ELI-EVIDENCE | if any Q5/Q6 datum |
| Q8 | Existing explosion-protection / safeguards in place. | MCQ multi-select | venting / suppression / isolation / inerting / bonding-earthing / housekeeping / none | ELI-BASELINE | always |
| Q9 | Area/equipment to classify, and adjacent occupied or connected vessels. | free-text | zoning target + secondary-explosion path | ELI-LOCATION / ELI-EXPOSURE | always |
| Q10 | Jurisdiction emphasis. | MCQ | DSEAR-ATEX (UK·EU) · NFPA 652·660 (US) · both | ELI-JURIS | always |
| Q11 | Existing DSEAR risk assessment / explosion-protection document, and its review date? | MCQ + free-text | yes / no + date | ELI-BASELINE / ELI-TEMPORAL | always |
| Q12 | Industry / sector + the statutory obligation set (DSEAR EPD / ATEX EPL / NFPA programme). | MCQ + free-text | food / pharma / wood / metals / chemicals (+ obligation: DSEAR EPD · ATEX EPL · NFPA) | ELI-INDUSTRY / ELI-OBLIGATIONS | always |
| Q13 | Org consequence/priority scheme for the basis-of-safety ranking. | MCQ | org scheme / default 5×5 | ELI-SCORING | always |

**Branch map**
- `Q3 ∈ {combustible dust, combination}` → activate NFPA 652·660 DHA rows + Q4/Q5 dust questions.
- `Q3 ∈ {reactive chemistry, combination}` → activate Q6 reactivity data + **hand reactive/deflagration nodes to `hazop-facilitator`** (`KB-STD-IEC-61882`).
- `Q3 ∈ {explosive vapour, combination}` → activate DSEAR/ATEX zoning rows.
- `Q5/Q6 datum == none` OR Q7 source missing → `[GAP]`, parameter **not invented**, routed to testing — **core rule** (METHODOLOGY step 3).
- `Q10 == DSEAR/ATEX` → ATEX zone (0/1/2 or 20/21/22) + EPL **justified, never defaulted** (an unjustified zone is an SME FLAG, METHODOLOGY step 5).
- `Q10 == NFPA` → NFPA 652·660 DHA framing.

## Echo-back
> "Process **{process}**, material **{material}**; scope **{reactive/dust/vapour}**; dust-handling steps **{list}**; data held **{Kst/Pmax/MIE/MIT/reactivity}** (sources **{lab+year}**), missing **{[GAP] params}**; existing safeguards **{list}**; zoning target **{area}**, adjacent occupied/connected **{detail}**; jurisdiction **{DSEAR/NFPA}**. I will run the DHA, set an explicit HoC-ranked basis of safety, justify (not default) any ATEX zone, hand the reactive/deflagration study to the HAZOP facilitator, and flag every missing parameter `[GAP]`. Confirm."

Echo the captured facts back and **confirm before setting the basis of safety**.

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "some powder is dusty" → demand named material + dust-generating steps; **never proceed on a vague subject**.
- Missing Kst/MIE etc. → `[GAP]`, never invent a dust parameter (METHODOLOGY output discipline).
- Zone requested with no release-grade/ventilation basis → refuse to default; justify or `[GAP]`.

**Domain evidence types (`ELI-EVIDENCE`)**
Dust explosibility test report (Kst, Pmax, MIE, MIT, LOC, particle size, moisture), reactivity screen (DSC/ARC/CHETAH/incompatibility matrix), P&ID + equipment list, existing DSEAR/explosion-protection document, prior incident/near-miss (deflagration/flash).
