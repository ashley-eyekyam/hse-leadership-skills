---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-OBLIGATIONS: "Assistive worksheet; the grounding duty is cited via ELI-JURIS (IEC 61511) only, not a compliance-deadline artefact."
    ELI-TEMPORAL: "Tied to the parent scenario / review, not separately elicited as a cadence."
    ELI-EXPOSURE: "The consequence severity IS the scenario — the exposed receptors are inside it."
    ELI-LOCATION: "The scenario carries its location."
  branches:
    - when: Q1
      option: Review-update
      activates_output_section: change-since-last-LOPA
    - when: Q9
      option: India
      activates_questions: [Q9a]
      mandatory: true
      activates_kb_row: in-factories-act
---

# Structured intake — lopa-worksheet

> **The skill structures engineer-supplied analysis — it never computes a PFD or allocates a
> SIL.** The IPL inventory, each IPL's independence test, and the engineer-supplied PFDs are
> the load-bearing inputs; an unsupplied PFD / credit / SIL target is `[GAP]`, never invented.
> Run **one question at a time**, branch on the answers, **echo the captured facts back
> before any analysis**, and **refuse a multi-scenario worksheet or a "compute the SIL"
> request**. Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **New** LOPA scenario, or **reviewing / updating** an existing worksheet? | MCQ | New , Review-update | ELI-SCOPE | always |
| Q2 | Name the **single consequence scenario** (one per worksheet). | free-text | Refuse a conflated multi-scenario sheet; the specificity anchor. | ELI-SUBJECT | always |
| Q3 | What is the **initiating event** and its **engineer-supplied frequency** (per year)? | MCQ+free-text | Control-loop failure / Human error / Equipment-mechanical / External event / Loss of utility ; then state the frequency per year | ELI-SUBJECT | always |
| Q4 | List each candidate **IPL** and its **independence test** result. | free-text | Independent of the IE *and* of every other IPL; not double-counted. | ELI-BASELINE | always |
| Q5 | **PFD for each IPL** (engineer-supplied) and its **source**. | free-text | Company LOPA table / vendor data / site history / `[GAP]` if absent — never computed by the skill. | ELI-EVIDENCE | always |
| Q6 | What is the **tolerable target frequency / SIL target** (engineer-supplied)? | free-text | The criterion the residual gap is measured against; `[GAP]` if unsupplied. | ELI-SCORING | always |
| Q7 | Which **competent engineer / team** owns these values? | free-text | The assistive-evidence anchor; named (as a role) for defensibility. | ELI-COMPETENCY | always |
| Q8 | Which **risk matrix** bands the residual gap? | MCQ | Our matrix (paste) , Default 5×5 | ELI-SCORING | always |
| Q9 | Which **jurisdiction** for the grounding citation? | MCQ | UK , USA , EU , India , None (IEC 61511 only) | ELI-JURIS | always |
| Q9a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory filing; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q9 == India |
| Q10 | What **output**, audience, distribution? | MCQ+free-text | Worksheet / Full report // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |

**Branch map:** Q1 = Review-update → **change-since-last-LOPA** section. Any PFD / credit / SIL absent (Q5/Q6) → record `[GAP]`, never compute (mandatory). An IPL that fails its independence test (Q4) → flag, exclude from credit, note in the output. Q9 = India → Q9a state (mandatory state detection) + `in-factories-act`. Q10 circulated externally → de-identification emphasis (engineer / team names → roles).

## Echo-back
Echo the captured facts back and require confirmation **before any analysis** begins:
"Scenario **{scenario}**; IE **{IE}** @ **{freq}/yr**; IPLs **{IPL list with independence verdicts}**; tolerable target **{target}**; values owned by **{engineer/team}**. I'll band the residual *gap* only — I won't compute any PFD or allocate a SIL. Confirm?"

## Refuse-on-vague anchors
- **Q2 is the specificity anchor:** refuse multiple scenarios in one worksheet — one consequence scenario with one initiating event; never proceed on a conflated sheet.
- "Calculate the SIL for us" → **decline**; the skill structures engineer-supplied analysis, it does not allocate a SIL.
- An IPL with no independence test stated (Q4) → ask again; any unsupplied PFD / credit / SIL → `[GAP]`, never a fabricated number.
