---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE, ELI-BASELINE, ELI-SCORING, ELI-COMPETENCY, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "fixed to GB rail (mainline/non-mainline) — the industry is the skill's domain, so it is not separately elicited; the dutyholder/jurisdiction (ELI-JURIS) carries the variation"
    ELI-EVIDENCE: "the safe-system-of-work is a forward-looking control artifact, not a closed/decided submission; ORR submission/decision status is out of this skill's scope (that is RAIL-02)"
  branches:
    - when: Q1
      equals: Level-crossing risk and remediation
      activates_output_section: crossing-remedial-hierarchy
      mandatory: true
    - when: Q1
      equals: Track-worker (on or near the line) safe system of work
      activates_output_section: trackworker-protection-hierarchy
      mandatory: true
    - when: Q1
      equals: Both (crossing and track work)
      activates_output_section: crossing-and-trackworker
      mandatory: true
    - when: Q4
      equals: Yes - I have an ALCRM band from our licensed model
      activates_output_section: alcrm-band-recorded
      mandatory: true
    - when: Q4
      equals: No - we do not have an ALCRM band
      activates_output_section: alcrm-band-gap
      mandatory: true
    - when: Q6
      equals: India (Railways Act or CRS)
      activates_questions: [Q6a]
      activates_kb_row: KB-REG-IN-RAIL
      activates_output_section: india-deferral
      mandatory: true
---

# Structured intake — level-crossing-track-worker-safety

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. The **task type (Q1)** is the branch-determining
question — the two hierarchies are distinct (crossing remediation vs track-worker
protection) and the rest of the intake branches on it. The **ALCRM band (Q4)** is RECORDED
from the user's licensed model output — **never invented or recomputed**; a missing band is
`[GAP]` and the remedial hierarchy still applies.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What does this assessment cover? *(this sets the hierarchy and the branches)* | MCQ | Level-crossing risk and remediation; Track-worker (on or near the line) safe system of work; Both (crossing and track work) | ELI-SCOPE | always |
| Q2 | Name the specific crossing and/or work site. | free-text | "e.g. the user-worked crossing at [named location/chainage]; the possession/worksite on [named section] — name *this* site. 'A level crossing' / 'the track' is refused." | ELI-SUBJECT | always |
| Q3 | What is the crossing type and/or the activity, and is the line open to traffic during the work? | free-text + MCQ | crossing type (user-worked / automatic half-barrier / manually-controlled / footpath / other) and/or the track activity; line status: Open (trains running); Line blockage / possession (no trains); Don't know | ELI-EXPOSURE | always |
| Q4 | Do you have an ALCRM risk band for this crossing? *(if so, it is RECORDED — never recomputed)* | MCQ | Yes - I have an ALCRM band from our licensed model; No - we do not have an ALCRM band; Not a crossing task | ELI-SCORING | Q1!=track-only |
| Q5 | What controls are in place or proposed today? | free-text | so the method can test whether the lead control is signage-only (crossing) or lookout-only (track work) where a higher order is reasonably practicable; their facts, not invented | ELI-BASELINE | always |
| Q6 | Which jurisdiction / infrastructure manager applies? | MCQ | GB (NR/L2/OHS/019 or ORR); India (Railways Act or CRS); Other (specify); Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which Indian operations / state, and which non-railway-depot statutory layer applies? | free-text | state detection is mandatory; defers state-specific content to the `hse-india` engine; exact form is `[GAP]`, never invented (`KB-REG-IN-RAIL`) | ELI-JURIS | Q6==India |
| Q7 | Is altering this crossing/asset a significant change (new/altered crossing, infrastructure, or operation)? | MCQ | Yes — apply the CSM-RA significance test; No; Not sure | ELI-OBLIGATIONS | Q1!=track-only |
| Q8 | Which safety-critical roles carry site-safety accountabilities? | free-text | role/title only (de-identified to role labels): COSS, lookout, PICOP, engineering supervisor, crossing keeper — never a personal name or Sentinel number | ELI-COMPETENCY | always |
| Q9 | Where exactly is the work? | free-text | the precise crossing / chainage / section, separate from any named person (a location tied to a named person is de-identified) | ELI-LOCATION | always |
| Q10 | Who is the audience and how will it circulate? | MCQ | Gang / site brief; Manager / dutyholder review; Both; Other | ELI-OUTPUT | always |
| Q11 | What target completion / review date applies? | MCQ | A specific date; Use the dutyholder's default review cycle; Defer to `[GAP]` | ELI-TEMPORAL | always |

**Branch map.** `Q1` sets the hierarchy: **crossing** → the remedial hierarchy section
(closure → grade separation → engineering → signage/admin LAST); **track work** → the
protection hierarchy section (separation → SSOW → warning → lookout-only LAST); **both** →
both sections. `Q4==Yes` → **record** the supplied ALCRM individual/collective band to
prioritise the crossing; `Q4==No` → the band is **`[GAP]`** and the remedial hierarchy
still applies — **never invent or compute a band** (D-03). `Q6==India` → Q6a +
`KB-REG-IN-RAIL` + the India deferral section (state detection mandatory; no national form
minted). `Q7==Yes` → the CSM-RA change-evidence limb (significance test + risk-acceptance +
AsBo, `KB-REG-CSM-RA`).

## Echo-back
Echo the captured facts back and ask the user to confirm before any analysis begins:
*"Confirmed: **{named crossing / work site}**, task **{crossing / track work / both}**,
{crossing type / activity}, line **{open / line-blockage-possession}**, ALCRM band
**{recorded value / [GAP]}**, under **{NR/L2/OHS/019 — GB / CRS — India}**, site-safety
roles **{COSS / lookout / PICOP — by role}**, audience **{gang brief / manager review}**.
Proceed?"*

## Refuse-on-vague anchors
- Q2 is the specificity anchor: a generic "a level crossing" / "the track" / "sort out
  level-crossing safety" with no named crossing/work site → **refuse**; never proceed on a
  vague subject.
- A crossing "managed by signage" where closure / grade separation / engineering is
  reasonably practicable → **reject the signage-led treatment**; lead with the higher order
  (`KB-SNIP-LX-HIERARCHY`).
- A track task "covered by a lookout" where separation (green-zone / line blockage /
  possession) is reasonably practicable → **reject the lookout-only-led system**; lead with
  separation.
- A missing ALCRM band → record `[GAP]`; **never invent, recompute, or hard-code a band**
  (the band values are the licensed RSSB/NR model output).
- The NR/L2/OHS/019 issue/date, or any unverified standard reference → record `[GAP]` /
  cite by reference; never fabricate, never reproduce the text.
- A site-safety role given as a personal name or Sentinel number → de-identify to a role
  label before any distributed output.
