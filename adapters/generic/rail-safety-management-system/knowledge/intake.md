---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-COMPETENCY, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "the SMS frames the 5x5 risk-control arrangement but the per-hazard scoring is done at the risk-assessment / change-assessment granularity, not in the org-level manual"
    ELI-EXPOSURE: "the manual is org-level, not hazard-level; exposure is elicited per-hazard in the operation's risk assessment, not here"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator + its operation/route scope is the location identity"
  branches:
    - when: Q2
      equals: Transport operator (mainline)
      activates_output_section: route-certificate          # mainline operator -> safety CERTIFICATE
      mandatory: true
    - when: Q2
      equals: Infrastructure manager (mainline)
      activates_output_section: route-authorisation        # IM (mainline) -> safety AUTHORISATION
      mandatory: true
    - when: Q2
      equals: Non-mainline operation (tram or metro or heritage)
      activates_output_section: route-part3-verification    # tram/metro/heritage -> ROGS Part 3 verification
      mandatory: true
    - when: Q4
      equals: India (Railways Act or CRS)
      activates_questions: [Q4a]
      activates_kb_row: KB-REG-IN-RAIL
      activates_output_section: india-deferral
      mandatory: true                                       # state detection is mandatory (CONV-8)
    - when: Q1
      equals: Review
      activates_questions: [Q7r]                            # existing-SMS gap path
    - when: Q1
      equals: Submission
      activates_questions: [Q9]                             # acceptance-submission formatting
---

# Structured intake — rail-safety-management-system

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. The **dutyholder type (Q2)** is the route-determining
question — it cannot be left to free-text, because the whole SMS is framed against the
resulting route (certificate vs authorisation vs Part-3 verification). The **accountable
duty-holder (Q5)** is the defining ROGS appointment; the element set cannot be drafted
without it.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you want this SMS work to do? | MCQ | Build a new SMS; Review; Submission | ELI-SCOPE | always |
| Q2 | What kind of dutyholder is the SMS for? *(this sets the route)* | MCQ | Transport operator (mainline); Infrastructure manager (mainline); Non-mainline operation (tram or metro or heritage); Other (specify) | ELI-INDUSTRY | always |
| Q3 | Name the operator or infrastructure manager and its operation scope. | free-text | "e.g. light-rail passenger; mainline freight; heritage line — name *this* dutyholder; 'a railway' is refused." | ELI-SUBJECT | always |
| Q4 | Which jurisdiction or Safety Authority applies? | MCQ | GB (ROGS or ORR); India (Railways Act or CRS); Other (specify); Unknown | ELI-JURIS | always |
| Q4a | *(India only)* Which Indian operations / state, and which non-railway-depot statutory layer applies? | free-text | state detection is mandatory; defers state-specific content to the `hse-india` engine; exact form is `[GAP]`, never invented (`KB-REG-IN-RAIL`) | ELI-JURIS | Q4==India |
| Q5 | Who is the accountable duty-holder? Which safety-critical roles carry SMS accountabilities? | free-text | role/title only (de-identified to role labels); the accountable duty-holder is the defining ROGS appointment | ELI-COMPETENCY | always |
| Q6 | Does the operation have any significant change in scope (new/altered vehicle, infrastructure, or operation)? | MCQ | Yes — apply the CSM-RA significance test · No · Not sure | ELI-OBLIGATIONS | always |
| Q7 | What existing inputs can the SMS cite? | free-text | existing safety policy, accountabilities, risk-control arrangements, competence/Sentinel records, asset/ECM records — *their* facts, not invented | ELI-BASELINE | Q1∈{Review,Submission} |
| Q7r | *(Review)* Share the existing SMS and tell me which element/gap you want assessed. | free-text | the document + the ROGS element to gap against | ELI-BASELINE | Q1==Review |
| Q8 | What review/revision cadence should the SMS state? | MCQ | Annual · Biennial · On-change-only · Use the Safety Authority's default · Defer to `[GAP]` | ELI-TEMPORAL | always |
| Q9 | Who is the audience and how will it circulate? | MCQ | Internal manual · ORR acceptance submission · Both · Other | ELI-OUTPUT | always |
| Q10 | Has the SMS already been submitted to / accepted by the Safety Authority? | MCQ | Not yet submitted · Submitted, awaiting acceptance · Accepted · Don't know | ELI-EVIDENCE | always |

**Branch map.** `Q2` sets the route: **transport operator (mainline)** → **safety
certificate**; **infrastructure manager (mainline)** → **safety authorisation**;
**non-mainline** (tram / metro / heritage) → **ROGS Part 3 safety verification**.
`Q4==India` → Q4a + `KB-REG-IN-RAIL` + the India deferral section (state detection
mandatory; no national form minted). `Q6==Yes` → the CSM-RA significance-test +
risk-acceptance + AsBo element (`KB-REG-CSM-RA`). `Q1==Review` → Q7r (existing-SMS gap
path), suppress full element-build drafting. `Q1==Submission` → Q9 acceptance-formatting.
**Q10 records the acceptance status as a fact reported back — it never licenses writing
"accepted by ORR" in the SMS body; acceptance is the Safety Authority's act.**

## Echo-back
Echo the captured facts back and ask the user to confirm before any drafting begins:
*"Confirmed: **{named operator}**, dutyholder type **{operator / IM / non-mainline}** →
route **{safety certificate / safety authorisation / Part-3 verification}**, under
**{ORR / CRS}**, accountable duty-holder **{role}**, mode **{build / review / submission}**.
Proceed?"*

## Refuse-on-vague anchors
- Q3 is the specificity anchor: a generic "a railway" / "improve our rail safety" with no
  named operator → **refuse**; never proceed on a vague subject (a generic SMS is the
  indefensible copy-paste output this skill exists to prevent).
- A missing accountable duty-holder → ask, do not invent the appointment.
- An unresolved route (Q2) → ask; never default a certificate where an authorisation is
  required (or vice-versa).
- An unverified statutory reference (India form, ORR clause) → record `[GAP]`; never fabricate.
- An "accepted" status (Q10) → report it as a fact; **never** restate it as "accepted by ORR"
  in the SMS body — the SMS is framed *for acceptance*.
