---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-LOCATION, ELI-BASELINE, ELI-EVIDENCE, ELI-COMPETENCY, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "the permit is control-driven, not matrix-ranked — controls are HoC-ranked instead of scored"
    ELI-EXPOSURE: "the task + the SIMOPS detection define who is exposed; no separate receptor list"
  branches:
    - {when: Q1, option: Confined-space entry, activates_questions: [Q4], activates_output_section: gas-test-attendant-rescue, mandatory: true}
    - {when: Q1, option: Hot work, activates_questions: [Q4], activates_kb_row: psm}
    - {when: Q1, option: Excavation or ground disturbance, activates_questions: [Q4]}
    - {when: Q5, option: "Yes", activates_questions: [Q6], activates_output_section: simops-coordination, mandatory: true}
    - {when: Q9, option: India, activates_questions: [Q9a], mandatory: true, activates_kb_row: in-factories-act}
---

# Structured intake — permit-to-work

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo task + isolations + concurrent-ops back before
drafting**; **refuse a vague task** ("some welding") and **never issue a confined-space
entry with no gas test / rescue plan**. Canonical runtime pattern: `KB-SNIP-INTAKE`.

Two load-bearing branches: the **permit-type gate** (Q1 → Q4) wires the type-specific
mandatory controls (confined-space gas test + attendant + rescue; hot-work fire watch +
combustibles removed; excavation buried-services scan + shoring; line-break
drain/flush/depressurise); and **SIMOPS detection** (Q5 = Yes → Q6) builds the in-skill
**SIMOPS coordination section** — the permit is **not valid** until concurrent operations
are coordinated (never deferred to a separate workflow).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Which **permit type**? | MCQ multi-select | Hot work / Confined-space entry / Line breaking or breaking containment / Excavation or ground disturbance / Working at height / Electrical or HV / General | ELI-SCOPE | always |
| Q2 | Name the **task** and its **exact location**. | free-text | specific equipment/area, not "the plant" — the specificity anchor | ELI-SUBJECT | always |
| Q3 | What **energy sources to isolate (LOTO)** and the **atmosphere/gas-test** requirement? | free-text | per task; confined-space / hot work → gas test | ELI-BASELINE | always |
| Q4 | **Type-specific gate:** confirm the mandatory controls. | MCQ multi-select | (CS) gas test + attendant + rescue plan / (Hot work) fire watch + combustibles removed + extinguisher / (Excavation) buried-services scan + shoring or benching / (Line break) drain or flush or depressurise + double-isolation / (Height) fall arrest or edge protection | ELI-BASELINE | branch on Q1 |
| Q5 | **SIMOPS detection:** are other operations running simultaneously in the same area? | MCQ | No / Yes | ELI-SCOPE | always |
| Q6 | *(SIMOPS)* The **conflicting activities**, **coordination controls**, and the **authorising authority**. | free-text | sequencing, exclusion zones, single point of coordination, cross-permit refs — the SIMOPS coordination section | ELI-OBLIGATIONS | Q5 == Yes |
| Q7 | Who are the **permit issuer**, **performing authority**, **gas-tester**, and (CS) **rescue team**? | free-text | competency / authority (de-identified to roles) | ELI-COMPETENCY | always |
| Q8 | What **permit conditions** must hold, and the **validity period / shift-handover** rule? | free-text | conditions + validity: single shift / 24h / task-duration | ELI-TEMPORAL | always |
| Q9 | **Jurisdiction** (statutory hook)? | MCQ | UK / USA (PSM hot-work (k)) / EU / India / None | ELI-JURIS | always |
| Q9a | *(India only)* Which **state** is the site in? | MCQ + free-text | Tamil Nadu / Karnataka / Maharashtra / Delhi/Central / Gujarat / Other / Unknown — confirm the state before citing any state-specific obligation; never silently assume | ELI-JURIS | Q9 == India |
| Q10 | What **output**, for whom, and which **sector**, **physical environment**? | MCQ + free-text | Permit form / Permit + SIMOPS plan — for M or C — sector + setting (plant / construction / confined space / height) | ELI-OUTPUT | always |
| Q11 | Which **sector** and **physical environment** frame the task? | MCQ | Process plant / Construction / Oil & Gas / Utilities / Other | ELI-INDUSTRY | always |
| Q12 | Confirm the **physical work environment** for the named permit. | free-text | confined space, height, ATEX/zoned area, excavation, live plant | ELI-LOCATION | always |
| Q13 | What **source documents** support the isolations and SIMOPS coordination? | MCQ multi-select | Isolation/LOTO register / P&ID for line-break isolation points / Buried-services drawings / Concurrent-permit register / Rescue plan / None yet | ELI-EVIDENCE | always |

**Branch map:** Q1 = Confined-space entry → gas-test + attendant + rescue-plan section (Q4 CS items + Q7 rescue team mandatory). Q1 = Hot work → fire-watch + combustibles + extinguisher; `psm` hot-work element (k). Q1 = Excavation → buried-services scan + shoring mandatory. Q5 = Yes (SIMOPS) → simops-coordination section; Q6 mandatory; the permit is **not valid** until coordination controls are in place. Q9 = India → **mandatory state branch** (Q9a) + `in-factories-act`.

## Echo-back

Echo task + isolations + concurrent-ops back and confirm before drafting the permit:
"{Permit type(s)} for **{task}** at **{location}**. Isolations **{LOTO}**, gas test
**{y/n}**, type-specific controls **{controls}**. SIMOPS: **{Yes/No}**{ → coordinating
authority …}. Issuer **{issuer}**, PA **{PA}**, gas-tester **{tester}**{, rescue
**{team}**}. Validity **{period}**. Correct before I draft the permit?"

## Refuse-on-vague anchors

- Q2 is the specificity anchor: refuse "a permit for some welding" with no exact location.
- **Never** issue a confined-space entry with no gas test or no rescue plan.
- SIMOPS detected but no coordinating authority → the permit is **not valid**; never
  proceed.
