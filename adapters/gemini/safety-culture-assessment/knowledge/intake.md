---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-EXPOSURE, ELI-BASELINE,
           ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "Safety-culture maturity (ownership of safety, how information flows, the espoused-vs-enacted gap) is assessed identically across sectors; industry is captured only as free-text context in Q1, never a branch. The skill is industry: [All]."
    ELI-LOCATION: "The unit of assessment is an organisation / site / business unit as a culture-bearing POPULATION, not a physical place with a location-specific hazard set; site is captured as free-text context within Q1 where relevant, never a location branch."
  branches:
    - {when: Q2, option: Schein three-levels, activates_questions: [Q2a], activates_kb_row: KB-SNIP-CULTURE-MODELS, mandatory: false}
    - {when: Q5, option: India, activates_questions: [Q5a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — safety-culture-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. This is a
**culture assessment of the organisation** (ownership of safety, how information flows,
whether espoused values are enacted) — it never assesses or names an individual.

**Two hard refuse-on-vague anchors:** **Q1** (a named organisation / site / unit, and a
confirmation that the user wants a culture assessment and not a sibling skill — refuse
"the whole company" without a named scope or sampling plan) and **Q3** (**at least two
data sources** — never produce a maturity *rating* on a single survey). The
**model-selection Q2** offers the Schein three-levels lens as a 4th, *selectable and
combinable* option; the **mandatory India→state branch** (Q5 = India → Q5a +
`KB-REG-IN-STATEFORMS`) resolves the state before citing any obligation and never mints a
national form number.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Unit in scope + sibling disambiguation** (named organisation / site / business unit) | free-text | "Which specific organisation, site, or business unit are we assessing the culture of? (e.g. 'the Northgate distribution centre'). **Refuse 'the whole company' without a named scope or sampling plan.** Confirm you want a *culture assessment* — not a behaviour-observation programme (`bbs-program-designer`), a single leadership walk (`safety-walk-gemba`), or a KPI set (`leading-lagging-kpi-framework`)." — **the specificity anchor; refuse a vague answer** | ELI-SUBJECT | always |
| Q2 | **Model / lens** | MCQ | DuPont Bradley Curve / Hudson ladder / Westrum typology / Schein three-levels / Combined — a diagnostic lens (Schein is a diagnosis not a ladder rating; Combined layers Schein over a chosen ladder) | ELI-SCOPE | always |
| Q2a | *(if Schein selected/combined)* **Schein lens scope** | MCQ | Standalone Schein diagnosis (named espoused-vs-enacted gaps, no maturity rating) / Schein as a triangulation lens layered over the chosen ladder | ELI-SCOPE | Q2 == Schein three-levels |
| Q3 | **Data sources** (the triangulation gate) | MCQ + free-text | Validated culture/climate survey / Leadership-walk or observation data / Records (reporting rate, participation, turnover, audit findings) / Focus groups — **at least two required; never rate on a single survey** | ELI-EVIDENCE | always |
| Q3b | **Confidentiality threshold per cohort** | MCQ + free-text | Minimum respondent cell to publish (default **≥5 respondents**; smaller cohorts are suppressed with secondary suppression) + who may see raw responses + whether verbatim quotes are permitted (default: paraphrase only) | ELI-OBLIGATIONS | always |
| Q4 | **Baseline / known context** | free-text | "Any current context or recent events? (a recent merger/restructure, a serious incident, a previous culture score, a new leadership team)." (seeds the current-state baseline) | ELI-BASELINE | always |
| Q4b | **Cohorts compared** | MCQ multi-select | Whole organisation / by site / by function or department / by level (leadership vs front-line) / by shift — **role/group/cohort labels only, never named individuals; any cohort <5 is suppressed** | ELI-EXPOSURE | always |
| Q5 | **Jurisdiction** | MCQ | UK / USA / EU / India / Other / Unknown (India → Q5a) | ELI-JURIS | always |
| Q5a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; never a national form number** | ELI-JURIS | Q5 == India |
| Q6 | **Banding scale** | MCQ | The model's own bands (Bradley 4 stages / Hudson 5 rungs / Westrum 3 types — default) / Schein gap signals (no bands) / Supply our scale | ELI-SCORING | always |
| Q7 | **Output artifact + reader** | MCQ | Full culture-assessment report + advancement roadmap (consultant) / Leadership summary (board/exec) / Survey design only / Schein gap diagnosis only — and its audience (M / C / E) | ELI-OUTPUT | always |
| Q8 | **Assessor + roadmap owners** | free-text | "Who is the competent person performing this assessment (role), and who will own the advancement actions? (named **role**, no 'TBD')" | ELI-COMPETENCY | always |
| Q9 | **Review cycle / next assessment** | MCQ + free-text | Annual / Biennial / On change (post-restructure / post-incident) / Other (+date) | ELI-TEMPORAL | always |

**Branch map:** `schein-lens` (Q2 = Schein three-levels → Q2a + `KB-SNIP-CULTURE-MODELS`;
optional — selectable/combinable, D-05) and `india-state` (Q5 = India → Q5a +
`KB-REG-IN-STATEFORMS`; **mandatory**). The model choice (Q2) activates the relevant
descriptor/probe set in `KB-SNIP-CULTURE-MODELS`.

## Echo-back

After the last applicable question (Q9, and Q2a / Q5a if those branches ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing: safety culture for the Northgate distribution centre, model = Hudson ladder
combined with a Schein espoused-vs-enacted lens, sources = climate survey + leadership-walk
data + reporting-rate records (≥5-respondent cohort threshold, paraphrase-only quotes),
context = post-restructure, UK, review annual — correct?" Confirm the **model + named
population + ≥2 data sources** before any rating.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "rate our culture" for an unnamed scope;
  require a named organisation/site/unit (or an explicit sampling plan). Record
  `[ASSUMPTION]` / `[GAP]`, never invent a scope. Also disambiguate from the three sibling
  skills before proceeding.
- **Q3 is the triangulation gate** — **refuse to produce a maturity rating on a single
  survey or a single source.** A rating requires a named model + a named population + ≥2
  triangulated data sources; with only one source, flag `[GAP]`, ask for corroborating
  observation/records, and offer a Schein *diagnosis* of named gaps instead of a rating.
- **Never name an individual as the "culture problem"** — the assessment is of the
  organisation's culture; a finding is always attributed to a role/group/system, never a
  person, and no verbatim quote is reproduced in a way that identifies the speaker in a
  small cohort.

## Domain evidence types (ELI-EVIDENCE)

Validated culture/climate survey (banded against `KB-DATA-CULTURE-MATURITY` with
source+year) · leadership-walk / observation data · records (near-miss reporting rate,
participation, turnover, audit findings) · aggregated focus-group themes. All are
**sensitive personnel data** in a small population — apply the reinforced
`references/deid-checklist.md` (<5 cohort suppression, secondary suppression, no
identifying verbatim quote, no individual named) before any analysis.
