---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-EVIDENCE, ELI-EXPOSURE,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "A leadership engagement walk is cross-sector — the felt-leadership / open-prompt method is identical regardless of industry; sector is captured only as free-text context within Q-subject (Q2), never a branch. The skill is industry: [All]."
    ELI-LOCATION: "The walk IS anchored to a physical area, but that area is captured as the specificity subject in Q2 (the named area/task/shift), not as a separate hazard-driving location dimension the way a confined-space RA needs; no distinct location branch is required."
    ELI-BASELINE: "This skill does not score initial-vs-residual risk — it runs an engagement conversation and converts commitments to tracked actions; there is no existing-controls baseline to capture for a re-score. Existing controls surface naturally within the control-verification prompt family (Q3)."
    ELI-OBLIGATIONS: "The walk is an engagement act, not a compliance artifact against permits/consent-limits; the only legal angle (the consultation/participation duty) is resolved through ELI-JURIS (Q5), so no separate obligations dimension is elicited."
    ELI-SCORING: "There is no risk-matrix or rating scheme in a gemba walk — the only quantitative output is the commitment count and closure-rate (a leading indicator, not a scored risk). No matrix configuration is captured."
  branches:
    - {when: Q5, option: India, activates_questions: [Q5a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — safety-walk-gemba

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the answers;
**echo the captured facts back for confirmation before any analysis**. This is an
**engagement** walk (felt leadership / *genchi-genbutsu*) — **open conversation, not a
tick-box inspection**.

**Hard refuse-on-vague anchors:** **Q1** (this is an engagement walk, and which skill — a
closed yes/no checklist request is **refused**) and **Q2** (a **named area / task / shift** —
refuse a vague "do a site walk"). The **mandatory India→state branch** (Q5 = India → Q5a +
`KB-REG-IN-STATEFORMS`) resolves the state before citing any consultation duty, and never
mints a national form number.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Purpose + which skill (disambiguation)** | mcq | Engagement gemba walk (this skill) / Tick-box inspection or audit → `safety-audit` / Behaviour-observation programme → `bbs-program-designer` / Culture-maturity survey → `safety-culture-assessment` / KPI framework → `leading-lagging-kpi-framework` — **if the user wants a closed yes/no checklist, refuse: a gemba walk is open prompts, not a tick-box** | ELI-SCOPE | always |
| Q2 | **Named area / task / shift in scope** | free-text | "Which specific area, task, or shift is the walk on? (e.g. 'night-shift warehouse pick-face', 'line-2 changeover'). **Refuse a vague 'do a site walk'** — name the area/task, with any relevant sector/site context." — **the specificity anchor; refuse a vague answer** | ELI-SUBJECT | always |
| Q3 | **Walk purpose → prompt family** | mcqmulti-select | Felt-leadership / engagement / Hazard-spotting / Verification of a specific control / Post-incident reassurance — selects the open prompts from `KB-SNIP-GEMBA-PROMPTS` (default: felt-leadership) | ELI-EVIDENCE | always |
| Q4 | **Exposed group (who's on the walk's path)** | mcqmulti-select | Whole crew / a specific shift / a role band / contractors on site — **role/group labels only, never named individuals** | ELI-EXPOSURE | always |
| Q5 | **Jurisdiction** | mcq | UK / USA / EU / India / Other / Unknown (India → Q5a) — resolves only any consultation/participation legal duty | ELI-JURIS | always |
| Q5a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; never a national form number** | ELI-JURIS | Q5 == India |
| Q6 | **Output artifact + reader** | mcq | Walk plan with open prompts (leadership, pre-walk) / Walk record + tracked commitments (post-walk) / Both — and its audience (M / E / F) | ELI-OUTPUT | always |
| Q7 | **Walk leader + commitment owners** | free-text | "Who is leading the walk (role), and who will own the commitments it produces? (named **role**, no 'TBD' — every commitment needs an owner)" | ELI-COMPETENCY | always |
| Q8 | **Closure cadence / next walk** | mcq+free-text | When are walk commitments reviewed to closure, and when is the next walk? (e.g. weekly close-out review; monthly walk cycle) (+date) | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q5 = India → Q5a + `KB-REG-IN-STATEFORMS`; **mandatory**).
Purpose branches (Q3) activate the matching open-prompt family in `KB-SNIP-GEMBA-PROMPTS`.

## Echo-back

After the last applicable question (Q8, and Q5a if the India branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Designing an engagement gemba walk on the night-shift warehouse pick-face, purpose =
felt-leadership + hazard-spotting, exposed group = night-shift crew (role labels only),
UK, output = walk plan + tracked commitments for the Shift Manager, weekly close-out review —
correct?" Confirm this is an **open-prompt engagement walk, not a tick-box checklist**,
before any drafting.

## Refuse-on-vague anchors

- **Q1 disambiguates and refuses a tick-box** — if the user asks for a closed yes/no
  checklist, **refuse**: a gemba walk is open prompts, not a tick-box; steer them to the open
  prompt bank, or to `safety-audit` if they truly want an inspection. Record `[GAP]`, never
  invent.
- **Q2 is the specificity anchor** — refuse "do a site walk" or any unnamed area; require a
  named area / task / shift (the prompt families are selected per area).
- **Never name an individual** — worker concerns are captured role-labelled; a finding is
  always attributed to a role/group, never a person (psychological safety).
