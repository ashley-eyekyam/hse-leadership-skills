---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-OBLIGATIONS: "Assistive diagram for grounding only, not a compliance filing with a statutory deadline."
    ELI-EXPOSURE: "The consequence lines carry the exposed receptors per branch, not a pre-elicited receptor list."
    ELI-LOCATION: "The hazard / top-event scopes it; the diagram is asset-agnostic above the named hazard."
  branches:
    - when: Q1
      option: CCM critical-control plan
      activates_questions: [Q8]
      activates_output_section: critical-control-verification-table
    - when: Q1
      option: Both
      activates_questions: [Q8]
      activates_output_section: critical-control-verification-table
    - when: Q2
      option: Mining (principal hazard)
      activates_output_section: principal-hazard-framing
    - when: Q11
      option: India
      activates_questions: [Q11a]
      mandatory: true
      activates_kb_row: in-factories-act
---

# Structured intake — bowtie-builder

> The barrier judgements are the load-bearing assistive evidence: the **team / owner**
> supplies them and **no barrier is declared effective without a stated performance
> standard** (otherwise → `[GAP]`). Run **one question at a time**, branch on the answers,
> **echo the captured facts back before any analysis**, and **refuse a vague hazard / top
> event**. Canonical runtime pattern: `KB-SNIP-INTAKE`. Never invent a threat, consequence,
> or barrier → record `[GAP]`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Build a **plain bowtie**, or a **Critical Control Management (ICMM CCM)** plan? | MCQ | Bowtie diagram / CCM critical-control plan / Both | ELI-SCOPE | always |
| Q2 | Which **sector** frames this? | MCQ | Process / Chemicals / Mining (principal hazard) / Aviation / Other | ELI-INDUSTRY | always |
| Q3 | Name the **hazard** (the energy / material with potential to harm). | free-text | Specific, not "operations"; the specificity anchor. | ELI-SUBJECT | always |
| Q4 | Name the **top event** (the loss-of-control / release point — the centre). | free-text | One top event per bowtie. | ELI-SUBJECT | always |
| Q5 | List the **threats** (causes that release the top event), one per line. | free-text | Left side of the bowtie. | ELI-SUBJECT | always |
| Q6 | List the **consequences**, phrased "[Damage] due to [Event]". | free-text | Right side of the bowtie. | ELI-SUBJECT | always |
| Q7 | For each **barrier** (preventive + mitigative): is it **effective · independent · auditable**, and what is its **performance standard**? | free-text | The team's judgement; `[GAP]` if no evidence — never declared effective without a performance standard. | ELI-BASELINE | always |
| Q8 | For each **critical control**: the **verification activity**, **owner**, and **frequency**. | free-text | CCM defensibility — the critical-control verification table. | ELI-EVIDENCE | Q1 == CCM critical-control plan |
| Q9 | Who is the **team / owner** supplying the barrier judgements, and how recent are they? | free-text | The assistive-evidence anchor (named role for defensibility) + last-reviewed date. | ELI-COMPETENCY | always |
| Q10 | Which **risk matrix** for the residual band? | MCQ | Our matrix (paste) , Default 5×5 | ELI-SCORING | always |
| Q11 | Which **jurisdiction** for the grounding citation? | MCQ | UK , USA , EU , India , None | ELI-JURIS | always |
| Q11a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory filing; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q11 == India |
| Q12 | What **output**, for whom, how widely shared? | MCQ+free-text | Bowtie diagram / CCM plan / Full report // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |
| Q13 | When was this barrier set **last reviewed / verified**, and when is the next review due? | free-text | The performance-standard verification cadence (CCM). | ELI-TEMPORAL | always |

**Branch map:** Q1 = CCM critical-control plan / Both → Q8 (mandatory) → **critical-control-verification-table** section. Q2 = Mining (principal hazard) → **principal-hazard-framing** (frame the top event as a principal hazard; CCM strongly recommended). Q7 barrier with no performance standard → record `[GAP]`, never declare effective (mandatory). Q11 = India → Q11a state (mandatory state detection) + `in-factories-act`. Q12 circulated externally → de-identification emphasis (owner names → roles).

## Echo-back
Echo the captured facts back and require confirmation **before any analysis** begins:
"{Bowtie/CCM} for hazard **{hazard}**, top event **{top event}**, **{n}** threats, **{m}** consequences, sector **{sector}**, barrier judgements owned by **{team}**. I'll record only barriers with a stated performance standard; the rest are `[GAP]`. Confirm?"

## Refuse-on-vague anchors
- **Q3/Q4 are the specificity anchor:** refuse "a bowtie for the plant" with no specific hazard / top event — require one named hazard and one loss-of-control top event; never proceed on a vague subject.
- A barrier asserted effective with no performance-standard evidence (Q7) → record `[GAP]`, never declared effective.
- Never invent a threat, consequence, or barrier → record `[GAP]`.
