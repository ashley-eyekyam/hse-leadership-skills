---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE]
  omits:
    ELI-SCORING: "A toolbox talk briefs already-understood hazards; it does not score risk on a matrix."
    ELI-OBLIGATIONS: "Permits are referenced from the upstream RA/JSA, not resolved here."
    ELI-COMPETENCY: "The delivering supervisor signs the attendance sheet at delivery; eliciting it at intake would break the 'leanest defensible intake' contract (Decision 2)."
    ELI-TEMPORAL: "A same-day briefing; the delivery date lands on the sign-off sheet, not the intake."
  branches:
    - {when: Q7, option: India, activates_questions: [Q7], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}  # light-touch: India→state mandatory ONLY if a statutory point is raised; Q7 itself carries the (which state?) prompt
    - {when: Q5, activates_output_section: labelled-typical-example, mandatory: false}  # Q5 blank → a clearly-labelled typical example; NEVER fabricate a local event
    - {when: Q6, activates_output_section: named-language-talk, mandatory: false}  # Q6 = Other language → deliver in the named language
    - {when: Q1, activates_kb_row: KB-DATA-hazard-facts, mandatory: false}  # Q1 topic (non-Other) → the data-points/ hazard-fact fragment
---

# Structured intake — toolbox-talk

B3 runs the **leanest defensible intake in the pack** (Decision 2) — ~6–7 questions,
MCQ-heavy, with only **two** free-text prompts (the task/site and the optional recent
incident). Run it following `KB-SNIP-INTAKE` — **one question at a time**, branch on the
answers, **echo the captured facts back** before assembling, and **never invent** a fact.
The cut is *quantity of questions*, never *specificity*: every surviving question is
load-bearing for a defensible talk.

The load-bearing discipline: **Q3 (site/area & the specific task today) is the specificity
anchor** — refuse a vague answer ("general site work"); `[GAP]` if absent; never proceed
generic. And **Q5 (a recent incident) is never fabricated** — a de-identified real event, or
a clearly-labelled *typical* example only; **never a fabricated 'last week on this site'
local event** (Decision 6). Q7 jurisdiction is light-touch: India → resolve the state
(mandatory) **only if a statutory point is actually raised**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Topic / primary hazard** of this talk | MCQ + free-text | Working at height / Confined space / Manual handling / Electrical-LOTO / Hot work / Mobile plant-vehicles / Hazardous substances / Slips-trips-housekeeping / Lifting operations / Heat-cold stress / Other (free-text) — drives the `data-points/` hazard-fact lookup | ELI-SUBJECT / ELI-SCOPE | always |
| Q2 | **Trade / crew** receiving the talk | MCQ + free-text | Construction-general / Maintenance / Electrical / Mechanical-fitters / Operators-process / Drivers-logistics / Cleaners-housekeeping / Mixed crew / Other (free-text) — calibrates language + which controls are foregrounded | ELI-EXPOSURE / ELI-INDUSTRY | always |
| Q3 | **Site / area & the specific task today** | free-text | "Name the site/area and the exact task — e.g. 're-roofing Bay 3, cherry-picker out of service, working off the leading edge'." — **the load-bearing specificity anchor; refuse a vague answer** ("general site work") — ask again or record `[GAP]`; never proceed generic | ELI-SUBJECT / ELI-LOCATION | always |
| Q4 | **Duration target** for the talk | MCQ | **<5 min (default)** / 5–10 min / 10–15 min — caps script length; <5 min is the frontline norm | ELI-OUTPUT | always |
| Q5 | **A recent relevant incident / near-miss** | free-text (optional) | "Optional — a recent near-miss/incident relevant to this hazard, on this site or in your org. Leave blank and a clearly-labelled *typical* example is used instead." — if supplied, **de-id scrub before use** (Decision 6); if blank, a labelled illustrative example, **never a fabricated local event** | ELI-EVIDENCE | always |
| Q6 | **Reading level / language** for the crew | MCQ | Plain-simple English (default) / Standard / ESL-friendly (short sentences) / Other language (name it, free-text) | ELI-OUTPUT | always |
| Q7 | **Jurisdiction** (light-touch) | MCQ | India ; (which state?) / UK / USA / EU / **Not jurisdiction-specific (default)** — used only if the talk must name a local rule; India → ask the state (mandatory state detection) only if a statutory point is actually raised | ELI-JURIS | always |

**Branch map:** `india-state` (Q7 = India AND a statutory point is raised → resolve the state
via `KB-REG-IN-STATEFORMS`; **mandatory** — light-touch, Q7 itself carries the *which state?*
prompt); `no-incident` (Q5 blank → labelled-typical-example, never fabricate a local event);
`other-language` (Q6 = Other → named-language talk); `hazard-fact` (Q1 selected, non-Other →
`KB-DATA-hazard-facts`).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
assembling:
"Talk on: working at height — re-roofing Bay 3, cherry-picker out of service, mixed crew,
<5 min, plain English — correct?"

## Refuse-on-vague anchors

- **Q3 (site/area & the specific task today) is the load-bearing anchor** — refuse "general
  site work"; `[GAP]` if absent, never proceed generic.
- **On Q5: never fabricate a local incident** — a de-identified real one or a clearly-labelled
  *typical* example only; never a fabricated "last week on this site" local event (Decision 6).

## Domain evidence types (ELI-EVIDENCE)

A recent de-identified incident/near-miss relevant to the hazard (Q5) · the `data-points/`
hazard-fact fragment for the Q1 topic · the named task's controls (foregrounded from Q1/Q3) ·
any ESL/other-language need (Q6).
