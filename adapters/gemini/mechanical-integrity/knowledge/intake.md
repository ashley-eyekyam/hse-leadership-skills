---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL, ELI-OBLIGATIONS]
  omits:
    ELI-EXPOSURE: "Folded into the consequence-of-failure scoring — the exposed receptors are inside the criticality consequence band."
    ELI-LOCATION: "The named unit is the location; the equipment population carries it."
  branches:
    - when: Q1
      option: Manage integrity deficiencies
      activates_questions: [Q7]
    - when: Q3
      option: Relief devices-PRVs
      activates_output_section: prv-test-interval
    - when: Q10
      option: India (Factories Act statutory examination)
      activates_questions: [Q10a]
      mandatory: true
      activates_kb_row: in-factories-act
    - when: Q10
      option: USA (PSM element j)
      activates_kb_row: us-osha
---

# Structured intake — mechanical-integrity

> An item with **no integrity basis** is never assumed fit-for-service → it reads `[GAP]`.
> The equipment population, the inspection / MI records, and the **inspection authority /
> owner** are the load-bearing inputs. Run **one question at a time**, branch on the answers,
> **echo the captured facts back before any analysis**, and **refuse a vague equipment
> population**. Canonical runtime pattern: `KB-SNIP-INTAKE`. Never assume fit-for-service
> without an integrity basis → record `[GAP]`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What's the **task**? | MCQ | Rank equipment criticality / Set-justify ITPM intervals / Manage integrity deficiencies / Build full MI programme | ELI-SCOPE | always |
| Q2 | Name the **equipment population / unit**. | free-text | Refuse "our equipment"; the specificity anchor. | ELI-SUBJECT | always |
| Q3 | Which **equipment classes** are in scope? | MCQ multi-select | Pressure vessels , Piping , Relief devices-PRVs , Storage tanks , Rotating equipment , Heat exchangers , Instruments-SIS , Fired equipment | ELI-SUBJECT | always |
| Q4 | What is the **consequence of failure** and the **likelihood drivers** (age, service, corrosion, damage mechanism)? | free-text | For the `risk_matrix` criticality scoring. | ELI-SCORING | always |
| Q5 | What is the **current ITPM basis** per class — intervals, methods, **RBI** if used, and **IOWs**? | free-text | Class-specific (vessels → thickness/CML; relief → test interval; tanks → API 653). | ELI-BASELINE | always |
| Q6 | What **inspection / MI records** do you hold? | MCQ multi-select | Inspection history-reports , Thickness-CML data , RBI study , Corrosion-rate data , PRV test records , None | ELI-EVIDENCE | always |
| Q7 | What **open deficiencies** exist and their **interim risk**? | free-text | Each gets a HoC-rank + named owner + due date. | ELI-SUBJECT | Q1 == Manage integrity deficiencies |
| Q8 | Who is the **inspection authority / owner** of the ITPM basis? | free-text | e.g. API-authorised inspector, statutory competent person (named as a role). | ELI-COMPETENCY | always |
| Q9 | Which **risk matrix** for criticality? | MCQ | Our matrix (paste) , Default 5×5 | ELI-SCORING | always |
| Q10 | Which **jurisdiction** (statutory inspection hook) for the grounding citation? | MCQ | USA (PSM element j) , UK , EU , India (Factories Act statutory examination) , None | ELI-JURIS | always |
| Q10a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory examination form; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q10 == India |
| Q11 | What **statutory inspection / examination obligations** apply (and their due dates)? | free-text | e.g. pressure-vessel statutory examination interval, PRV test due date — the compliance hook. | ELI-OBLIGATIONS | always |
| Q12 | What is the **ITPM / re-inspection cadence** and the next due date per class? | free-text | The temporal driver behind "overdue" / trend status. | ELI-TEMPORAL | always |
| Q13 | What **output**, for whom, how widely shared? | MCQ+free-text | Criticality register / ITPM schedule / Deficiency plan / Full report // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |

**Branch map:** Q1 = Manage integrity deficiencies → Q7 (mandatory; criticality only as interim-risk context). Q3 includes Relief devices-PRVs → **prv-test-interval** question; tanks → API 653 settlement / inspection. Any item with no integrity basis (Q5) → `[GAP]`, never "fit for service" (mandatory). Q10 = India → Q10a state (mandatory state detection) + `in-factories-act` (statutory pressure-vessel examination); Q10 = USA → `us-osha` (PSM element j). Q13 circulated externally → de-identification emphasis (inspector names → roles).

## Echo-back
Echo the captured facts back and require confirmation **before any analysis** begins:
"Task **{task}**, equipment **{population}**, classes **{classes}**, criticality drivers **{drivers}**, ITPM basis **{basis}**, records held **{records}**, inspection owner **{owner}**, matrix **{matrix}**. Any item with no integrity basis I'll mark `[GAP]`, not fit-for-service. Confirm?"

## Refuse-on-vague anchors
- **Q2 is the specificity anchor:** refuse "our equipment" with no named population / unit — require a bounded equipment population; never proceed on a vague subject.
- Assuming an item is fit-for-service with no integrity basis (Q5) → record `[GAP]`, never "assumed fit".
- Never invent an inspection interval, corrosion rate, or fitness conclusion → record `[GAP]`.
