---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-COMPETENCY, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "the SMS-builder frames the 5x5 RCS but does not itself score hazards; scoring lives in aviation-hazard-register / aviation-change-safety-assessment"
    ELI-EXPOSURE: "the manual is org-level, not hazard-level; exposure is elicited per-hazard in the register skill"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator/airport/AMO is the location identity"
  branches:
    - when: Q4
      equals: India
      activates_questions: [Q4a]
      activates_kb_row: KB-REG-IN-DGCA
      activates_output_section: dgca-ssp-alignment
      mandatory: true
    - when: Q4
      equals: FAA
      activates_questions: [Q4b]          # ask for the reference; never fabricate a clause
      activates_output_section: ask-reference-no-fabrication
    - when: Q4
      equals: EASA
      activates_questions: [Q4b]
      activates_output_section: ask-reference-no-fabrication
    - when: Q1
      equals: Review
      activates_questions: [Q7r]          # existing-manual gap path
    - when: Q1
      equals: Submission
      activates_questions: [Q6, Q9]       # CAA acceptance status + acceptance formatting
---

# Structured intake — aviation-sms-builder

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. The two defining Annex 19 appointments — the
**Accountable Manager** and the **Safety Manager** — are discrete questions, not buried in
free-text; the four pillars cannot be drafted without them.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you want this SMS work to do? | MCQ | Build/a new SMS manual, Review/gap-assess an existing one, Submission/structure an SMS-acceptance pack for the CAA | ELI-SCOPE | always |
| Q2 | What kind of organisation is the SMS for? | MCQ | Aircraft operator · Airport/aerodrome · Approved Maintenance Org (AMO) · Approved Training Org (ATO) · Other (specify) | ELI-INDUSTRY | always |
| Q3 | Name the operator/airport/AMO and its operation type. | free-text | "e.g. scheduled passenger / cargo / GA / ground handling — name *this* org; 'an airline' is refused." | ELI-SUBJECT | always |
| Q4 | Which State Safety Programme / certificating authority applies? | MCQ | India/DGCA SSP, FAA/USA, EASA/EU, Other CAA (specify), Unknown | ELI-JURIS | always |
| Q4a | *(India only)* Which Indian operations / where is the AOC held, and which State Safety Programme layer applies? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); the exact CAR number is `[GAP]` to verify, never invented | ELI-JURIS | Q4==India |
| Q4b | Give the FAA/EASA reference you want the four pillars aligned to. | free-text | (Q4∈{FAA,EASA,Other}) — recorded `[GAP]` if absent; never fabricated | ELI-OBLIGATIONS | Q4∈{FAA,EASA,Other} |
| Q5 | Who is the Accountable Manager? Who is the Safety Manager? | free-text | role/title only (de-identified to role labels); the two defining Annex 19 appointments | ELI-COMPETENCY | always |
| Q6 | Is an SMS already accepted by the CAA, and at what implementation phase? | MCQ | Not yet submitted · Submitted, awaiting acceptance · Accepted (Phase 1–4) · Don't know | ELI-EVIDENCE | always |
| Q7 | What existing inputs can the manual cite? | free-text | existing safety policy, key-personnel appointments, hazard data, SPIs — *their* facts, not invented | ELI-BASELINE | Q1∈{Review,Submission} |
| Q7r | *(Review)* Share the existing manual and tell me what gap you want assessed. | free-text | the document + the target standard/clause to gap against | ELI-BASELINE | Q1==Review |
| Q8 | What review/revision cadence should the manual state? | MCQ | Annual · Biennial · On-change-only · Use regulator's default · Defer to `[GAP]` | ELI-TEMPORAL | always |
| Q9 | Who is the audience and how will it circulate? | MCQ | Internal manual · CAA acceptance submission · Both · Other | ELI-OUTPUT | always |

**Branch map.** `Q4==India` → Q4a + `KB-REG-IN-DGCA` + DGCA-SSP-alignment output section (the
mandatory India follow-up resolves the State Safety Programme layer; exact CAR number stays
`[GAP]`). `Q4∈{FAA,EASA,Other}` → Q4b — **no fabricated clause** (`[GAP]` if the reference is
absent). `Q1==Review` → Q7r (existing-manual gap path), suppress full build-pillar drafting.
`Q1==Submission` → Q6 acceptance-status + Q9 acceptance-formatting are mandatory.

## Echo-back
Echo the captured facts back and ask the user to confirm before any drafting begins:
*"Confirmed: {org type} **{named operator}**, operation **{type}**, under **{SSP/CAA}**,
Accountable Manager **{role}**, Safety Manager **{role}**, mode **{build/review/submission}**.
Proceed?"*

## Refuse-on-vague anchors
- Q3 is the specificity anchor: a generic "an airline" / "improve our safety" with no named
  operator → **refuse**; never proceed on a vague subject.
- A missing Accountable Manager or Safety Manager → ask, do not invent the appointment.
- An FAA/EASA/Other clause not supplied → record `[GAP]`; never fabricate a CAR / AC number.
