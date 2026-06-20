---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-OBLIGATIONS: "Assistive worksheet, not a compliance-deadline artefact — the grounding duty is cited only via ELI-JURIS (IEC 61882; OSHA PSM / COMAH where a regulatory frame applies)."
    ELI-EXPOSURE: "Consequences are captured per-line by the team during the guideword sweep, not pre-elicited as a receptor list."
    ELI-LOCATION: "The node IS the location — the bounded P&ID section under study carries it (ELI-SUBJECT)."
  branches:
    - when: Q1
      option: Revalidation (cyclical re-study)
      activates_output_section: revalidation-delta
    - when: Q5
      option: Standard-plus-custom
      activates_questions: [Q5a]
    - when: Q8
      option: Incomplete (no full team present)
      activates_questions: [Q9]
      activates_output_section: study-not-performed-banner
    - when: Q11
      option: India
      activates_questions: [Q11a]
      mandatory: true
      activates_kb_row: in-factories-act
---

# Structured intake — hazop-facilitator

> **HAZOP is an assistive, team-recorded study.** The bounded **node** and the
> multidisciplinary **TEAM** are the load-bearing assistive evidence: with no full team
> present the worksheet is structured but marked **"study not yet performed"**, never
> presented as a completed HAZOP. Run **one question at a time**, branch on the answers,
> **echo the captured facts back before any analysis**, and **refuse a vague node**.
> Canonical runtime pattern: `KB-SNIP-INTAKE`. Never invent a deviation, cause,
> consequence, or severity the team did not raise → record `[GAP]`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Facilitating a **new** HAZOP, **revalidating** an existing one, or **writing up** a completed session? | MCQ | New / Revalidation (cyclical re-study) / Write-up (completed session) | ELI-SCOPE | always |
| Q2 | Name the **single node / P&ID section** under study. | free-text | One bounded node — **refuse "the plant" / "the whole unit"**; the specificity anchor. | ELI-SUBJECT | always |
| Q3 | What is the node's **design intent** (normal flow, pressure, temperature, level, composition, phase)? | free-text | Deviations are meaningless without a stated normal intent. | ELI-SUBJECT | always |
| Q4 | Which **parameters** apply to this node? | MCQ multi-select | Flow / Pressure / Temperature / Level / Composition / Reaction / Phase / Utilities-services / Other (specify) | ELI-SCORING | always |
| Q5 | Use the **standard guideword set**, or add custom guidewords? | MCQ | Standard (No/More/Less/Reverse/As-well-as/Part-of/Other-than) , Standard-plus-custom | ELI-SUBJECT | always |
| Q5a | Specify the **custom guidewords**. | free-text | Only when extending the set. | ELI-SUBJECT | Q5 == Standard-plus-custom |
| Q6 | What **existing safeguards** already protect this node (before we examine deviations)? | free-text | BPCS, alarms, relief, SIS, procedures — the baseline. | ELI-BASELINE | always |
| Q7 | What **source documents** do you have? | MCQ multi-select | Current P&ID / Line list & stream data / Prior HAZOP-PHA / Cause & Effect & SIS spec / Relief-system basis / None yet | ELI-EVIDENCE | always |
| Q8 | Who is in the **HAZOP team** right now (disciplines + chair/scribe)? | MCQ | Full multidisciplinary team (process, operations, instrumentation/SIS, mechanical, chair-scribe) , Incomplete (no full team present) | ELI-COMPETENCY | always |
| Q9 | No full team present — structure the worksheet and mark the study **"not yet performed"**? | MCQ | Yes (structure only) , No (reconvene first) | ELI-COMPETENCY | Q8 == Incomplete |
| Q10 | Which **risk matrix** ranks consequences? | MCQ | Our matrix (paste) , Default 5×5 with process-safety descriptors (loss-of-containment / escalation) | ELI-SCORING | always |
| Q11 | Which **jurisdiction / regulatory frame** for the grounding citation? | MCQ | UK , USA (OSHA PSM) , EU , India , None (IEC 61882 only) | ELI-JURIS | always |
| Q11a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory PHA filing; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q11 == India |
| Q12 | What **output** do you need, for whom, and how widely shared? | MCQ+free-text | Worksheet only / Full report / Recommendation register // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |

**Branch map:** Q1 = Revalidation → **revalidation-delta** section (what changed since the last study / prior-recommendation status — the already-resolved scope, no new gap). Q5 = Standard-plus-custom → custom-guideword capture (Q5a). Q8 = Incomplete → Q9 → **study-not-performed banner** (mandatory). Q11 = India → Q11a state (mandatory state detection) + the `in-factories-act` KB row (state form only if a statutory PHA filing applies). Q12 circulated externally → de-identification emphasis (team names → roles).

## Echo-back
Echo the captured facts back and require confirmation **before any analysis** begins:
"Node **{node}**, intent **{intent}**, parameters **{params}**, guidewords **{gw}**, team **{disciplines}**, matrix **{matrix}**, grounding **{frame}**. I'll prompt each guideword × parameter cell and record only what the team raises. Confirm before we start?"

## Refuse-on-vague anchors
- **Q2 is the specificity anchor:** refuse "do a HAZOP" with no node, and refuse "the plant" / "the whole unit" as a node — require one bounded P&ID section; never proceed on a vague subject.
- No design intent (Q3) → cannot judge deviations; ask again.
- No full team and the user wants a *completed* study (Q8/Q9) → structure only + the "study not yet performed" banner — never present it as a performed HAZOP.
- Never invent a deviation, cause, consequence, or severity → record `[GAP]`.
