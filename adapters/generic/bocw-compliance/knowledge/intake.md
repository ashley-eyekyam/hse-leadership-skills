---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE, ELI-BASELINE, ELI-COMPETENCY, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "no severity scoring — the accident-notice check here is a duty-check, not an RCA"
    ELI-EVIDENCE: "a gap-list, not an assembled filing — registration certs etc. are captured under ELI-BASELINE"
    ELI-LOCATION: "the construction site (named establishment + state) is the location; no separate environment elicitation"
  branches:
    - when: Q1
      option: India
      activates_questions: [Q1a]
      mandatory: true
      activates_kb_row: KB-REG-IN-STATEFORMS
    - when: Q2
      activates_questions: [Q4]
    - when: Q3
      activates_questions: []
    - when: Q2
      activates_questions: [Q8]
    - when: Q7
      activates_questions: []
---

# Structured intake — bocw-compliance

Building & Other Construction Workers (RE&CS) Act 1996 + Welfare Cess Act 1996 + state BOCW
Rules — registration, 1% cess, Form XXV annual return, Safety-Officer/Committee thresholds,
accident notice. Run ONE question at a time, MCQ where the answer space is enumerable and
free-text where it is open; branch on the answers; **echo the captured facts back before any
gap-list**; **refuse to proceed on a vague or unconfirmed state** (BOCW is run by state Welfare
Boards — a wrong state is a wrong return/portal; record `[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`.

**MANDATORY state detection (the family spine).** The Indian state is the FIRST, BLOCKING,
infer-then-confirm gate — the BOCW return and portal are administered by the **state Welfare
Board**, so they are state-specific. You may infer the state from a supplied site address, but
echo it back and confirm before citing. Unseeded/Unknown state → state-specific values =
`[GAP]` (Safety-Officer headcount, accident-notice form/timing, cess due date), route to the
state Board; the Form XXV (~15 Feb) anchor stays citable. State MCQ set: `Tamil Nadu ·
Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown` (GJ first-class).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Which **jurisdiction** is the construction site in? *(India-default skill; a non-India jurisdiction is out of scope.)* | MCQ | India, Other / Unknown — India activates the mandatory state gate (Q1a) | ELI-JURIS | always |
| Q1a | **Which state** is the construction site in? *(BOCW is run by state Welfare Boards — the return/portal is state-specific; infer-from-address allowed, I confirm.)* | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown | ELI-JURIS | iff Q1 = India — **BLOCKING** |
| Q2 | Which BOCW obligation(s) do you want checked? | MCQ multi | Establishment registration · Beneficiary registration · 1% cess · Form XXV annual return · Safety-Officer/Committee · Accident notice · Full gap-list | ELI-OBLIGATIONS | always |
| Q3 | **How many building workers** on site (peak)? *(≥10 triggers establishment registration; the notified threshold triggers a Safety Officer / committee.)* | free-text | peak headcount | ELI-EXPOSURE | always |
| Q4 | **Total cost of construction** of the project? *(drives the 1% welfare cess.)* | free-text | cost figure | ELI-EXPOSURE | iff Q2 includes cess or full |
| Q5 | Are workers **direct or through contractors** (contract-labour split)? | MCQ | Mostly direct · Mostly contract labour · Mixed | ELI-EXPOSURE | always |
| Q6 | Who is the **principal employer / establishment** registering — and is there a separate contractor? | free-text → role | role labels | ELI-COMPETENCY | always |
| Q7 | **What's already in place** — establishment registered? beneficiaries registered? cess paid? Form XXV filed before? | MCQ multi | Establishment registered · Beneficiaries registered · Cess paid · Form XXV filed · None yet | ELI-BASELINE | always |
| Q8 | Where are you in the **filing cycle** (Form XXV is due ~15 Feb)? | MCQ | Upcoming · Overdue · Not sure | ELI-TEMPORAL | iff Q2 includes Form XXV or full |
| Q9 | Nature of the construction work + who the gap-list is for. | free-text | scope + audience | ELI-INDUSTRY / ELI-OUTPUT | always |

## Branch map (state detection prominent)

- **`state-detection`** (THE spine — `when: Q1 / option: India`, `mandatory: true`,
  `activates_questions:[Q1a]`, `activates_kb_row: KB-REG-IN-STATEFORMS` + `KB-REG-IN-BOCW`).
  Sub-branches: any seeded/known state → resolve the **state Welfare Board** return/portal;
  Form XXV (~15 Feb) is the **verified central anchor**; Unknown/unseeded → state-specific
  values = `[GAP]` (Safety-Officer headcount, accident-notice form/timing, cess due date),
  route to the state Board, Form XXV anchor still citable.
- **`obligation-focus`** (`when: Q2`, multi) — each selection activates its duty walk + the
  matching questions (cess → Q4; Form XXV → Q8).
- **`exposure-thresholds`** (`when: Q3`) — ≥10 → registration finding; > notified threshold →
  Safety-Officer/Committee finding; cost → 1% cess finding. **The numbers drive which duties
  fire.**
- **`baseline-gap`** (`when: Q7`) — the gap-list = duty set MINUS what's already in place; each
  gap gets a cited rule + a HoC-ranked control + a role-owner + a date.

## Echo-back

*"Confirming: a **{nature}** site in **{state}** with **{peak n}** workers ({direct/contract}),
construction cost **{₹x}**, principal employer **{role}**. Already in place: **{baseline}**.
Checking **{obligations}** against `KB-REG-IN-BOCW`. Note: state-specific values not in the KB
will be flagged `[GAP]` to verify with the **{state}** Welfare Board. Correct?"* — echo the
captured facts back and wait for confirmation before any gap-list.

## Refuse-on-vague anchors

- **State is the specificity anchor:** no state → no Welfare-Board return/portal cited; refuse
  to proceed on a vague or inferred-but-unconfirmed state.
- Cite **Form XXV + 1% cess as verified anchors** but **`[GAP]` every state-specific value the
  KB doesn't verify** (Safety-Officer headcount, accident-notice form/timing, cess due date) —
  never invent.
- No headcount / cost → can't fire the threshold/cess duties → ask, don't assume.
- Every corrective control HoC-ranked (engineering/admin before PPE); every gap with a
  role-owner + a date.
