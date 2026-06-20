---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE, ELI-EVIDENCE, ELI-BASELINE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "no severity scoring — accidents are tallied for the return, not RCA-scored"
    ELI-LOCATION: "the registered factory (named establishment) is the location; no separate environment elicitation"
    ELI-OBLIGATIONS: "the obligation IS the subject (Q1); the citing clause/penalty is output, not separately elicited"
  branches:
    - when: Q0
      option: India
      activates_questions: [Q2]
      mandatory: true
      activates_kb_row: KB-REG-IN-STATEFORMS
    - when: Q1
      activates_questions: [Q1a]
    - when: Q3
      activates_questions: []
    - when: Q5
      activates_questions: []
---

# Structured intake — factories-act-returns

Assembles the filled Factories-Act **state** return / register for a detected state (vs the
finder, which only locates it). Run ONE question at a time, MCQ where the answer space is
enumerable and free-text where it is open; branch on the answers; **echo the captured facts
back before any assembly**; **refuse to proceed on a vague or unconfirmed state, and never
fabricate a return field or a form value** (record `[GAP]`). Canonical runtime pattern:
`KB-SNIP-INTAKE`.

**MANDATORY state detection (the family spine).** The Indian state is the FIRST, BLOCKING,
infer-then-confirm gate — a wrong state is a wrong statutory form. You may infer the state from
a supplied address, but echo it back and confirm before assembling. Unseeded/Unknown state →
`[GAP]` + a refusal to assemble a national form. State MCQ set: `Tamil Nadu · Karnataka ·
Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown` (GJ first-class; the GJ
annual-return form value is `[GAP]`).

> **[GAP] — MH annual-return form-id (GATE-06).** The legacy MH annual-return form is carried
> forward as a literal `[GAP]`: `KB-REG-IN-STATEFORMS` seeds MH **only for accident-notice**
> (Form 24 / 24A) — there is **no seeded MH annual-return row**, and the citation grader is
> row-blind (it checks the fragment id resolves, not that a form value is real). **Reason:**
> a fabricated MH annual-return number would pass the automated gate but fail a regulator.
> **Verification path:** verify the MH annual-return form against `KB-REG-IN-STATEFORMS` (seed
> the row) or the live Maharashtra Factory Rules 1963 before asserting. Do **not** assert a
> number here.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | Which **jurisdiction** is the factory registered in? *(India-default skill; a non-India jurisdiction is out of scope.)* | MCQ | India, Other / Unknown — India activates the mandatory state gate (Q2) | ELI-JURIS | always |
| Q1 | What are you producing? | MCQ | Annual return · Half-yearly return · A statutory register | ELI-SCOPE / ELI-SUBJECT | always (first) |
| Q1a | Which **half-year period**? | MCQ | 1st (Jan–Jun) · 2nd (Jul–Dec) | ELI-TEMPORAL | iff Q1 = half-yearly |
| Q1b | For which **return year**? | free-text | e.g. CY2025 | ELI-TEMPORAL | always |
| Q2 | **Which state** is the factory registered in? *(infer-from-address allowed; I confirm before assembling — a wrong state is a wrong form.)* | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown | ELI-JURIS | iff Q0 = India — **BLOCKING** |
| Q3 | Is it a **hazardous-process** factory (Sch. I / Sec. 2(cb))? | MCQ | Yes · No · Not sure | ELI-INDUSTRY | always |
| Q4 | **Worker employment figures** for the period — average & max workers, man-days worked. | free-text (structured) | "avg 240, max 310, man-days 71,200" | ELI-EXPOSURE | always |
| Q5 | **Accident / dangerous-occurrence tally** for the period (counts by class — fatal / reportable / minor). I will aggregate any cell < 5. | free-text (structured) | counts only, no names | ELI-EVIDENCE | iff the return form requires it |
| Q6 | **Leave-with-wages / welfare** figures the form requires (if applicable). | free-text | per the form's schedule | ELI-EVIDENCE | iff applicable to the form |
| Q7 | **OSH appointments** held — Safety Officer, factory medical officer, welfare officer? | MCQ multi | Safety Officer · FMO · Welfare Officer · None | ELI-EVIDENCE | always |
| Q8 | Have you **filed this return before** (is this an original or a correction)? | MCQ | First filing · Routine annual · Correction/revised | ELI-BASELINE | always |
| Q9 | Who is the **occupier / factory manager** signing this return? (role label — I de-identify the person.) | free-text → role | "Occupier" / "Factory Manager" | ELI-COMPETENCY | always |
| Q10 | Establishment name + who the assembled return is for. | free-text | name + audience | ELI-SUBJECT / ELI-OUTPUT | always |

## Branch map (state detection prominent)

- **`state-detection`** (THE spine — `when: Q0 / option: India`, `mandatory: true`,
  `activates_questions:[Q2]`, `activates_kb_row: KB-REG-IN-STATEFORMS`). Sub-branches: TN/KA/DL →
  seeded annual-return rows; **MH → `[GAP]` for annual-return** (no seeded MH annual row — see
  the GATE-06 note above) — do **not** silently emit a form value; GJ → assemble verified fields,
  render `form = [GAP]`; Other/Unknown → `[GAP]` + refuse a national form.
- **`obligation`** (`when: Q1`) — half-yearly → Q1a + the half-yearly vs annual field schedule.
- **`hazardous-process`** (`when: Q3`) — Yes activates the additional hazardous-process
  declarations / on-site emergency-plan reference.
- **`accident-tally`** (`when: Q5`) — when the form requires accident figures: activates the
  accident tally + the <5 aggregation rule (de-id).

## Echo-back

*"Confirming: **{state}** factory ({hazardous?}), assembling the **{obligation}** for
**{period}**, signed by the **{occupier/manager}**. Worker figures: avg {x}/max {y}/{man-days}.
Accident tally: {…, aggregated <5}. Resolving the form from `KB-REG-IN-STATEFORMS`. Correct?"* —
echo the captured facts back and wait for confirmation before any assembly.

## Refuse-on-vague anchors

- **State is the specificity anchor:** no state → no return; refuse to proceed on a vague or
  inferred-but-unconfirmed state.
- **Never invent a form value the KB doesn't seed** (incl. MH annual-return → `[GAP]` until
  verified, and GJ → `[GAP]`).
- Any return field the user can't supply = literal `[GAP]`, never fabricated.
- Accident cells < 5 aggregated before they enter the return.
