---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-OBLIGATIONS: "Assistive worksheet; the grounding duty is cited via ELI-JURIS only, not a compliance-deadline artefact."
    ELI-TEMPORAL: "A one-off study; there is no recurring review cadence to set."
    ELI-LOCATION: "The bounded scope (procedure / system / operation under study) is the location."
    ELI-EXPOSURE: "Consequences are captured per-line by the team during the What-If sweep, not pre-elicited as a receptor list."
  branches:
    - when: Q1
      option: A specific change
      activates_output_section: moc-cross-pointer
    - when: Q2
      option: What-If-Checklist hybrid
      activates_output_section: checklist-column
    - when: Q6
      option: Incomplete (no full team present)
      activates_questions: [Q7]
      activates_output_section: study-not-performed-banner
    - when: Q9
      option: India
      activates_questions: [Q9a]
      mandatory: true
      activates_kb_row: in-factories-act
---

# Structured intake — whatif-facilitator

> **What-If is an assistive, team-recorded study** (lighter than HAZOP, for procedures and
> simpler systems). A bounded **scope** and the **TEAM** are the load-bearing assistive
> evidence: with no full team the worksheet is structured but marked **"study not yet
> performed"**. Run **one question at a time**, branch on the answers, **echo the captured
> facts back before any analysis**, and **refuse a vague scope**. Canonical runtime
> pattern: `KB-SNIP-INTAKE`. Never invent a consequence or rank → record `[GAP]`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What is the **bounded scope**, and what **kind** is it? | MCQ+free-text | Procedure-SOP / Operation-activity / System-equipment / A specific change ; then name the specific scope | ELI-SCOPE | always |
| Q2 | Run **What-If only**, or **What-If + Checklist** (hybrid)? | MCQ | What-If question set , What-If-Checklist hybrid | ELI-SCOPE | always |
| Q3 | Confirm or extend the **question seeds**. | MCQ multi-select | Loss of utility / Wrong sequence / Wrong material or quantity / Human error or omission / Equipment failure / External event / Start-up-shutdown-abnormal / Other (specify) | ELI-SUBJECT | always |
| Q4 | What **existing safeguards** already apply to this scope? | free-text | The baseline, before the questions are run. | ELI-BASELINE | always |
| Q5 | What **source documents** do you have? | MCQ multi-select | Procedure-SOP / P&ID or sketch / Prior study / None | ELI-EVIDENCE | always |
| Q6 | Who is in the **team** (disciplines + facilitator)? | MCQ | Full team (operations, process, facilitator/scribe) , Incomplete (no full team present) | ELI-COMPETENCY | always |
| Q7 | No full team — structure and mark **"not yet performed"**? | MCQ | Yes (structure only) , No (reconvene) | ELI-COMPETENCY | Q6 == Incomplete |
| Q8 | Which **risk matrix**? | MCQ | Our matrix (paste) , Default 5×5 process-safety descriptors | ELI-SCORING | always |
| Q9 | Which **jurisdiction** for the grounding citation? | MCQ | UK , USA , EU , India , None | ELI-JURIS | always |
| Q9a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory filing; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q9 == India |
| Q10 | What **output**, audience, distribution? | MCQ+free-text | Worksheet / Full report // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |

**Branch map:** Q1 kind = A specific change → **moc-cross-pointer** (recommend the team also run `management-of-change`; seed change-specific questions). Q2 = What-If-Checklist hybrid → **checklist-column** section. Q6 = Incomplete → Q7 → **study-not-performed banner** (mandatory). Q9 = India → Q9a state (mandatory state detection) + `in-factories-act`. Q10 circulated externally → de-identification emphasis (team names → roles).

## Echo-back
Echo the captured facts back and require confirmation **before any analysis** begins:
"What-If on **{scope}** ({kind}), {mode}, question seeds **{seeds}**, team **{disciplines}**, matrix **{matrix}**. I'll prompt each question and record the team's answers. Confirm?"

## Refuse-on-vague anchors
- **Q1 is the specificity anchor:** refuse "run a What-If" with no bounded scope, and refuse "the site" as a scope — require one named procedure / system / operation; never proceed on a vague scope.
- No full team and the user wants a *completed* study (Q6/Q7) → structure only + the "study not yet performed" banner.
- Never invent a consequence or rank → record `[GAP]`.
