---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-COMPETENCY, ELI-TEMPORAL, ELI-EVIDENCE, ELI-INDUSTRY]
  omits:
    ELI-SCORING: "the SRB records hazard 5x5 ratings as decisions but does not itself score; scoring is aviation-hazard-register"
    ELI-EXPOSURE: "not a hazard-analysis artifact"
    ELI-JURIS: "minutes are an internal record; any SSP citation comes pre-resolved from the SPIs/register being reviewed — omit unless the user asks to cite a CAR"
    ELI-OBLIGATIONS: "no external submission deadline attaches to internal minutes"
    ELI-BASELINE: "prior-meeting continuity is captured at ELI-TEMPORAL (Q9), not a separate baseline"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator is the location identity"
  branches:
    - when: Q1
      equals: DraftBlank
      activates_output_section: empty-agenda-attendance-decision-action-tables   # skip Q4/Q6/Q7/Q8 content
    - when: Q1
      equals: Minute
      activates_questions: [Q4, Q8]       # require attendees + actions
    - when: Q5
      equals: SPI
      activates_questions: [Q6]
    - when: Q5
      equals: Hazards
      activates_questions: [Q7]
    - when: Q5
      equals: PriorActions
      activates_questions: [Q9]
---

# Structured intake — aviation-srb-minutes

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. Attendees and any reporter named in a hazard item appear
as **role labels only** — a reporter-identity leak in circulated minutes is a de-id hard-fail.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you want produced? | MCQ | Minute/a held meeting (I have the inputs), DraftBlank/a blank agenda + empty attendance/decision/action tables to run the meeting, Review/tidy an existing draft | ELI-OUTPUT | always |
| Q2 | Which body and meeting? | MCQ | Safety Review Board (SRB) · Safety Action Group (SAG) · Other | ELI-SUBJECT | always |
| Q3 | Name the operator and the meeting date/scope. | free-text | refused if no named operator | ELI-SUBJECT | always |
| Q4 | Who attended? (will appear as role labels) | free-text | chair typically the Accountable Manager; de-identified to roles | ELI-COMPETENCY | Q1==Minute |
| Q5 | Which agenda items does this meeting cover? | MCQ multi-select | PriorActions/review of prior actions, SPI/SPT performance, Hazards/new risk decisions, Audit/inspection findings, Change/MoC review, Training & promotion, AOB | ELI-SUBJECT | always |
| Q6 | For each SPI reviewed: status vs alert/target, trend, breach? | free-text | from `aviation-spi-spt-framework` where it exists | ELI-EVIDENCE | Q5 includes SPI |
| Q7 | For each hazard item: current 5×5 rating and the decision taken? | free-text | record the decision + rationale + accountable person | ELI-COMPETENCY | Q5 includes Hazards |
| Q8 | List each action with owner and due date. | free-text | {action, owner, due} | ELI-COMPETENCY | Q1==Minute |
| Q9 | Any prior-meeting actions to carry forward? | free-text | continuity of the action log | ELI-TEMPORAL | Q5 includes PriorActions |

**Branch map.** `Q1==DraftBlank` → **skip Q4/Q6/Q7/Q8 content**, render the agenda + empty
attendance/decision/action tables (the "minute-the-blank" mode). `Q1==Minute` → require
attendees (Q4) + actions (Q8). `Q5` multi-select → activates only the matching content
questions (SPI→Q6, Hazards→Q7, PriorActions→Q9).

## Echo-back
Echo the captured facts back and ask the user to confirm before any drafting:
*"Confirmed: **{SRB/SAG}** minutes for **{named operator}**, **{date}**, chaired by **{role}**,
agenda **{items}**, **{N}** decisions / **{M}** actions. Every decision will carry a rationale
+ accountable person; no reporter is named. Proceed?"*

## Refuse-on-vague anchors
- Q3 is the specificity anchor: minutes requested with no named operator → **refuse**; never
  proceed on a vague subject.
- A decision with no rationale or no accountable person → flag (cannot enter the decision log).
