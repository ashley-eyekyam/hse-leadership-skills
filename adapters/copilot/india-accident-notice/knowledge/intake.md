---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-SCORING, ELI-TEMPORAL, ELI-EXPOSURE, ELI-COMPETENCY, ELI-EVIDENCE]
  omits:
    ELI-BASELINE: "a notice is event-triggered, not a periodic baseline — no prior-filing position to capture"
    ELI-LOCATION: "the establishment + (for a mine) the DGMS region is the location; no separate environment elicitation"
    ELI-OBLIGATIONS: "the obligation is fixed (notify); the clause/penalty is output, not separately elicited"
  branches:
    - when: Q0
      option: India
      activates_questions: [Q1]
      mandatory: true
      activates_kb_row: KB-REG-IN-STATEFORMS
    - when: Q2
      option: Mine
      activates_questions: [Q2a]
      mandatory: true
      activates_kb_row: KB-REG-IN-MINES-ACT
    - when: Q3
      activates_questions: []
    - when: Q4
      activates_questions: []
---

# Structured intake — india-accident-notice

Assembles the filled statutory accident / dangerous-occurrence notification for a detected
state — including the mine/DGMS layer. Run ONE question at a time, MCQ where the answer space is
enumerable and free-text where it is open; branch on the answers; **echo the captured facts back
before any assembly**; **refuse to proceed on a vague or unconfirmed state (and, for a mine, an
unresolved DGMS region), and never invent a notice form or deadline** (record `[GAP]`).
Canonical runtime pattern: `KB-SNIP-INTAKE`.

**MANDATORY state detection (the family spine) — and a SECOND mandatory gate for a mine.** The
Indian state is the FIRST, BLOCKING, infer-then-confirm gate. For a **mine**, the **DGMS
region/zone** is resolved FIRST as a second blocking gate — a mine notice routes through DGMS,
NOT the state factory department. You may infer the state from a supplied address, but echo it
back and confirm before citing. Unseeded/Unknown state → `[GAP]` + a refusal to invent a
national form. State MCQ set: `Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat ·
Other (specify) · Unknown` (GJ first-class).

> **[GAP] — TN / DL accident-notice form-ids (GATE-06).** The TN accident-notice form (and the
> DL accident-notice form) are carried forward as literal `[GAP]`: `KB-REG-IN-STATEFORMS` seeds
> **only the MH accident-notice row** (Form 24 / 24A) — there is **no seeded TN or DL
> accident-notice row**, and the citation grader is row-blind. **Reason:** a fabricated TN or DL
> form number would pass the automated gate but fail a regulator. **Verification path:** verify
> the TN and DL accident-notice forms against `KB-REG-IN-STATEFORMS` (seed the rows) or the live
> state Factory Rules before asserting. The mine **Form J** / DGMS 24h-notice form id is likewise
> `[GAP]` until verified. Do **not** assert a number here.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | Which **jurisdiction** did the incident occur in? *(India-default skill; a non-India jurisdiction is out of scope.)* | MCQ | India, Other / Unknown — India activates the mandatory state gate (Q1) | ELI-JURIS | always |
| Q1 | **Which state** did the incident occur in? *(infer-from-address allowed; I confirm before citing the notice form.)* | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown | ELI-JURIS | iff Q0 = India — **BLOCKING** |
| Q2 | What **kind of establishment**? | MCQ | Factory, Construction site, Mine, Other (specify) | ELI-INDUSTRY | always |
| Q2a | Which **DGMS region/zone** is the mine in? *(a mine notice resolves through DGMS, not the state factory dept.)* | free-text / MCQ-if-enumerable | DGMS zone | ELI-JURIS | iff Q2 = mine — **BLOCKING** |
| Q3 | **Severity / class** of the event (this sets the form and the deadline). | MCQ | Fatal · Serious bodily injury · Dangerous occurrence (no injury) · Reportable disease | ELI-SCORING | always |
| Q4 | **When did it happen** (date & time)? *(this starts the statutory clock — e.g. the 24-hour notice.)* | free-text (date-time) | exact date-time of the event | ELI-TEMPORAL | always |
| Q5 | **How many persons** were injured / killed? (counts only — I de-identify identities; I aggregate any cell < 5 in wider distribution.) | free-text | counts by outcome | ELI-EXPOSURE | always |
| Q6 | **What happened** — incident particulars (I will scrub names, exact location detail, and health detail). | free-text | narrative | ELI-SUBJECT | always |
| Q7 | Who is the **statutory notifier / signatory** (occupier, factory manager, mine manager/agent)? | free-text → role | role label | ELI-COMPETENCY | always |
| Q8 | What **records** do you already hold (medical/first-aid record, witness statements, prior register entry)? | MCQ multi | Medical record · Witness statements · Register entry · None yet | ELI-EVIDENCE | always |
| Q9 | Who is the assembled notice **for**, and how will it circulate? | MCQ | Internal record · Filed with the inspectorate / DGMS · Client/consultant memo | ELI-OUTPUT | always |

## Branch map (state detection prominent)

- **`state-detection`** (THE spine — `when: Q0 / option: India`, `mandatory: true`,
  `activates_questions:[Q1]`, `activates_kb_row: KB-REG-IN-STATEFORMS` accident-notice rows). Per
  the seeded rows: **MH → Form 24 within 24h + Form 24A**; **TN / DL accident-notice forms are
  `[GAP]`** (not seeded — see the GATE-06 note); other states' rows where seeded, else `[GAP]`.
- **`establishment-type → mine-DGMS`** (`when: Q2 / option: Mine`, `mandatory: true`,
  `activates_questions:[Q2a]`, `activates_kb_row: KB-REG-IN-MINES-ACT` + `KB-REG-IN-DGMS` — 24h
  notice + **Form J** register; unverified DGMS form id = `[GAP]`). **A mine does NOT use a
  Factories form — a hard branch.**
- **`severity`** (`when: Q3`) — maps option → form + deadline (fatal/serious → the 24h
  immediate-notice path; dangerous occurrence → Form 24A).
- **`temporal-clock`** (`when: Q4`) — derives "already overdue?" + the filing deadline; **Q4's
  exact date-time is a PRESERVED fact, not scrubbed** (de-id exception for the statutory event
  timestamp — injured-party identities still scrubbed).

## Echo-back

*"Confirming: **{fatal/serious/DO}** event at a **{type}** in **{state}** {DGMS region if mine}
at **{date-time}**, **{n}** person(s) affected, notifier = **{role}**. Statutory clock: the
**24-hour** notice → due by **{date-time + 24h}**. Assembling under the `KB-REG-IN-STATEFORMS`
accident-notice row. Correct?"* — echo the captured facts back and wait for confirmation before
any assembly.

## Refuse-on-vague anchors

- **State (and, for a mine, the DGMS region) is the specificity anchor:** no state (and no DGMS
  region for a mine) → no notice form; refuse to proceed on a vague or unconfirmed state.
- **Never invent a notice form or deadline** the KB / DGMS layer doesn't supply → `[GAP]` (incl.
  the TN / DL accident-notice forms and the mine Form J).
- Preserve the **exact incident date-time** (clock-critical) while scrubbing injured-party PII;
  aggregate injury cells < 5 in wider distribution.
- Does **not** run the RCA — points to `incident-investigation`.
