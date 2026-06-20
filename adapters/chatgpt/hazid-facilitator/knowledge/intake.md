---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-EXPOSURE, ELI-LOCATION, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-OBLIGATIONS: "An early-stage hazard register produced at a stage gate, not a statutory filing with a compliance deadline."
    ELI-BASELINE: "Existing controls are captured by the team per hazard during the sweep, not pre-elicited per line."
    ELI-TEMPORAL: "A one-off study at a stage gate; there is no recurring review cadence to set."
  branches:
    - when: Q1
      option: Concept
      activates_output_section: siting-hazards
    - when: Q1
      option: FEED
      activates_output_section: siting-hazards
    - when: Q2
      option: Environmental (release to land-water-air)
      activates_questions: [Q3]
      activates_kb_row: KB-STD-ISO14001
    - when: Q5
      option: Incomplete (no full team present)
      activates_questions: [Q6]
      activates_output_section: study-not-performed-banner
    - when: Q8
      option: India
      activates_questions: [Q8a]
      mandatory: true
      activates_kb_row: in-factories-act
---

# Structured intake — hazid-facilitator

> **HAZID is an assistive, team-recorded early-stage sweep.** A bounded **installation /
> stage** and the multidisciplinary **TEAM** are the load-bearing assistive evidence: with
> no full team the register is structured but marked **"study not yet performed"**. Run
> **one question at a time**, branch on the answers, **echo the captured facts back before
> any analysis**, and **refuse an unbounded scope**. Canonical runtime pattern:
> `KB-SNIP-INTAKE`. Never invent a hazard or risk rank → record `[GAP]`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What **installation / project** is this HAZID for, and at what **life-cycle stage**? | MCQ+free-text | Concept / FEED / Detailed-design / Pre-commissioning / Operating-change // name the bounded scope | ELI-SCOPE | always |
| Q2 | Confirm or trim the **hazard categories** to sweep. | MCQ multi-select | Process , Mechanical , Electrical , External-natural (flood-seismic-wind-lightning) , Environmental (release to land-water-air) , Utilities loss , Neighbouring-installation knock-on , Human factors , Security | ELI-SUBJECT | always |
| Q3 | Who/what are the **receptors** in range (external & environmental categories)? | free-text | Workers, public, neighbouring sites, watercourses, protected habitat. | ELI-EXPOSURE | Q2 includes Environmental |
| Q4 | What **site / siting context** do we have? | MCQ multi-select | Plot plan / Siting or QRA study / Met & flood data / Prior HAZID / None yet | ELI-EVIDENCE | always |
| Q4b | What is the **physical environment / siting** of the installation? | free-text | Greenfield vs congested brownfield, neighbouring installations, terrain, met/flood exposure — the location context HAZID weighs. | ELI-LOCATION | always |
| Q5 | Who is in the **HAZID team** (disciplines + chair/scribe)? | MCQ | Full multidisciplinary team (process, project/design, operations, environmental, chair-scribe) , Incomplete (no full team present) | ELI-COMPETENCY | always |
| Q6 | No full team present — structure the register and mark **"not yet performed"**? | MCQ | Yes (structure only) , No (reconvene) | ELI-COMPETENCY | Q5 == Incomplete |
| Q7 | Which **risk matrix**? | MCQ | Our matrix (paste) , Default 5×5 with process-safety descriptors | ELI-SCORING | always |
| Q8 | Which **jurisdiction** for the grounding citation? | MCQ | UK , USA , EU , India , None (structured-study discipline only) | ELI-JURIS | always |
| Q8a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory filing; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q8 == India |
| Q9 | What **output**, for whom, how widely shared? | MCQ+free-text | Hazard register / Full report // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |

**Branch map:** Q1 stage = Concept / FEED → **siting-hazards** section (emphasise external / environmental / siting). Q2 includes Environmental → `KB-STD-ISO14001` row + receptor capture (Q3) mandatory. Q5 = Incomplete → Q6 → **study-not-performed banner** (mandatory). Q8 = India → Q8a state (mandatory state detection) + `in-factories-act`. Q9 circulated externally → de-identification emphasis (team names → roles).

## Echo-back
Echo the captured facts back and require confirmation **before any analysis** begins:
"HAZID for **{installation}** at **{stage}**, sweeping **{categories}**, receptors **{receptors}**, siting **{siting}**, team **{disciplines}**, matrix **{matrix}**. I'll prompt each category and record only what the team raises. Confirm?"

## Refuse-on-vague anchors
- **Q1 is the specificity anchor:** refuse "all our hazards" with no bounded installation / stage — require one named installation at a named life-cycle stage; never proceed on a vague scope.
- Environmental category selected (Q2) but no receptors named (Q3) → ask again; never list a release pathway with no receptor.
- No full team and the user wants a *completed* study (Q5/Q6) → structure only + the "study not yet performed" banner.
- Never invent a hazard or risk rank → record `[GAP]`.
