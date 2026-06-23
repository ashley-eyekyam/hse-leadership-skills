---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-COMPETENCY, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "the application pack summarises the SMS's risk-control arrangements but per-hazard 5x5 scoring is done at the risk-assessment granularity, not in the application"
    ELI-EXPOSURE: "the pack is dutyholder/application-level, not hazard-level; exposure is elicited per-hazard in the operation's risk assessment, referenced not rebuilt"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named dutyholder + its operation/route scope is the application identity"
  branches:
    - when: Q2
      equals: Infrastructure manager (mainline)
      activates_output_section: route-authorisation        # IM (mainline) -> safety AUTHORISATION
      mandatory: true
    - when: Q2
      equals: Transport operator (mainline)
      activates_output_section: route-certificate          # mainline operator -> safety CERTIFICATE (point to RAIL-01)
      mandatory: true
    - when: Q2
      equals: Non-mainline operation (tram or metro or heritage)
      activates_output_section: route-part3-verification    # tram/metro/heritage -> ROGS Part 3 verification
      mandatory: true
    - when: Q3
      equals: No - the SMS does not yet exist
      activates_output_section: sms-gap-route-rail01         # references RAIL-01; never rebuilds the SMS
      mandatory: true                                        # CONV-12: the SMS is an INPUT, not regenerated
    - when: Q5
      equals: India (Railways Act or CRS)
      activates_questions: [Q5a]
      activates_kb_row: KB-REG-IN-RAIL
      activates_output_section: india-deferral
      mandatory: true                                       # state detection is mandatory (CONV-8)
    - when: Q6
      equals: Yes — apply the CSM-RA significance test
      activates_output_section: csm-ra-change-evidence       # the change-evidence limb of the pack
---

# Structured intake — safety-authorisation

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any assembly**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. The **dutyholder type (Q2)** is the route-determining
question — it cannot be left to free-text, because the whole application is framed against
the resulting route (authorisation vs certificate vs Part-3 verification). The **SMS-input
question (Q3)** is the CONV-12 anchor: this skill **references** the SMS (built by RAIL-01),
it never rebuilds it — if the SMS does not exist, route the user to RAIL-01 and record the
SMS as a `[GAP]` input.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you want this application work to do? | MCQ | Assemble a new application pack; Gap-check an existing draft; Submission-format an assembled pack | ELI-SCOPE | always |
| Q2 | What kind of dutyholder is the application for? *(this sets the route)* | MCQ | Infrastructure manager (mainline); Transport operator (mainline); Non-mainline operation (tram or metro or heritage); Other (specify) | ELI-INDUSTRY | always |
| Q3 | Does a rail Safety Management System (SMS) already exist for this dutyholder? *(this skill references it — it does not rebuild it)* | MCQ | Yes - I can supply / reference it; Yes - but only in draft; No - the SMS does not yet exist | ELI-BASELINE | always |
| Q4 | Name the dutyholder and its operation scope. | free-text | "e.g. light-rail infrastructure manager; mainline freight operator — name *this* dutyholder; 'a railway' is refused." | ELI-SUBJECT | always |
| Q5 | Which jurisdiction or Safety Authority applies? | MCQ | GB (ROGS or ORR); India (Railways Act or CRS); Other (specify); Unknown | ELI-JURIS | always |
| Q5a | *(India only)* Which Indian operations / state, and which non-railway-depot statutory layer applies? | free-text | state detection is mandatory; defers state-specific content to the `hse-india` engine; exact form is `[GAP]`, never invented (`KB-REG-IN-RAIL`) | ELI-JURIS | Q5==India |
| Q6 | Is there a significant change in scope (new/altered vehicle, infrastructure, or operation) the application must evidence? | MCQ | Yes — apply the CSM-RA significance test; No; Not sure | ELI-OBLIGATIONS | always |
| Q7 | Who is the accountable duty-holder? Which safety-critical roles carry application accountabilities? | free-text | role/title only (de-identified to role labels); the accountable duty-holder is the defining ROGS appointment | ELI-COMPETENCY | always |
| Q8 | What existing inputs can the application cite? | free-text | the existing SMS, accountabilities, risk-control arrangements, competence/Sentinel and asset/ECM records — *their* facts, not invented | ELI-BASELINE | always |
| Q9 | Who is the audience and how will it circulate? | MCQ | ORR submission · Internal review draft · Both · Other | ELI-OUTPUT | always |
| Q10 | Has the application already been submitted to / decided by ORR? | MCQ | Not yet submitted · Submitted, awaiting decision · Decided · Don't know | ELI-EVIDENCE | always |
| Q11 | What target submission / review date applies? | MCQ | A specific date · Use the Safety Authority's default · Defer to `[GAP]` | ELI-TEMPORAL | always |

**Branch map.** `Q2` sets the route: **infrastructure manager (mainline)** → **safety
authorisation**; **transport operator (mainline)** → **safety certificate** (the same
application pack on the certificate route; point the user to RAIL-01 for the SMS);
**non-mainline** (tram / metro / heritage) → **ROGS Part 3 safety verification**.
`Q3==No` → route to **`rail-safety-management-system`** (RAIL-01) to build the SMS first;
record the SMS as a `[GAP]` input — **never rebuild the SMS in this skill** (CONV-12).
`Q5==India` → Q5a + `KB-REG-IN-RAIL` + the India deferral section (state detection
mandatory; no national form minted). `Q6==Yes` → the CSM-RA change-evidence limb
(significance test + risk-acceptance + AsBo, `KB-REG-CSM-RA`). **Q10 records the ORR
decision status as a fact reported back — it never licenses writing "authorised by ORR" in
the application body; granting the authorisation is the Safety Authority's act.**

## Echo-back
Echo the captured facts back and ask the user to confirm before any assembly begins:
*"Confirmed: **{named dutyholder}**, dutyholder type **{IM / operator / non-mainline}** →
route **{safety authorisation / safety certificate / Part-3 verification}**, under
**{ORR / CRS}**, SMS input **{supplied / draft / [GAP] → build via RAIL-01}**, accountable
duty-holder **{role}**, mode **{assemble / gap-check / submission-format}**. Proceed?"*

## Refuse-on-vague anchors
- Q4 is the specificity anchor: a generic "a railway" / "sort out our ORR submission" with
  no named dutyholder → **refuse**; never proceed on a vague subject.
- A missing SMS (Q3==No) → route to RAIL-01 and record `[GAP]`; **never rebuild the SMS
  here** (CONV-12 — the SMS is an input, not this skill's artifact).
- An unresolved route (Q2) → ask; never default a certificate where an authorisation is
  required (or vice-versa).
- A missing accountable duty-holder → ask, do not invent the appointment.
- An unverified statutory reference (India form, ORR clause) → record `[GAP]`; never fabricate.
- A "decided" status (Q10) → report it as a fact; **never** restate it as "authorised by ORR"
  in the application body — the pack is framed *for submission*.
