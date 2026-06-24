---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-EXPOSURE, ELI-BASELINE,
           ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "Psychosocial work-design hazards (demands/control/support/relationships/role/change) are cross-sector and assessed identically regardless of industry; sector is captured only as free-text context in Q1, never a branch. The skill is industry: [All]."
    ELI-LOCATION: "The unit of assessment is a team/role/function (a work-design population), not a physical place; there is no location-specific hazard set the way a confined-space RA has. Site is captured as free-text context within Q1 where relevant."
  branches:
    - {when: Q5, option: India, activates_questions: [Q5a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — psychosocial-risk-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. This is
an ISO 45003 / HSE Management Standards assessment of **work design, not the
individual** — it never produces a clinical or individual-diagnosis output.

**Two hard refuse-on-vague anchors:** **Q1** (a named unit — refuse "the whole company"
without a sampling plan) and **Q3** (**at least two data sources** — never build the
assessment on a single anecdote). The **mandatory India→state branch** (Q5 = India →
Q5a + `KB-REG-IN-STATEFORMS`) resolves the state before citing any obligation, and never
mints a national form number.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Unit in scope** (named team / role / function) | free-text | "Which specific team, role, or function are we assessing? (e.g. 'night-shift contact-centre advisers, Site B'). **Refuse 'the whole company' without a sampling plan** — name the unit, with any relevant sector/site context." — **the specificity anchor; refuse a vague answer** | ELI-SUBJECT | always |
| Q2 | **Psychosocial domains to assess** | MCQ multi-select | Demands / Control / Support / Relationships / Role / Change (HSE Management Standards — branch per selected domain; default: all six) | ELI-SCOPE | always |
| Q3 | **Data sources** (the triangulation gate) | MCQ multi-select | Validated survey (e.g. HSE Indicator Tool) / Focus groups / Sickness-absence & turnover data / Grievance & incident data — **at least two required; never rate on a single anecdote** (branch: each source carries its confidentiality threshold) | ELI-EVIDENCE | always |
| Q3b | **Confidentiality threshold per source** | MCQ + free-text | Minimum response cell to publish (default **≥5 respondents**; smaller breakdowns are suppressed) + who may see the raw responses | ELI-OBLIGATIONS | always |
| Q4 | **Known triggers** | free-text | "Any known triggers or recent context? (restructuring, workload spikes, redundancy programme, bereavement clusters, a critical incident)." (seeds the baseline / current-state) | ELI-BASELINE | always |
| Q4b | **Exposed group** | MCQ multi-select | Whole unit / a sub-team or shift / a role band / managers vs front-line — **role/group labels only, never named individuals** | ELI-EXPOSURE | always |
| Q5 | **Jurisdiction** | MCQ | UK / USA / EU / India / Other / Unknown (India → Q5a) | ELI-JURIS | always |
| Q5a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; never a national form number** | ELI-JURIS | Q5 == India |
| Q6 | **Risk-rating scale** | MCQ | 3×3 / 4×4 / **5×5 (default — same matrix as the physical RA)** / Supply our matrix | ELI-SCORING | always |
| Q7 | **Output artifact + reader** | MCQ | Full ISO 45003 RA report (consultant) / Management summary (leadership) / Action plan only — and its audience (M / C / E) | ELI-OUTPUT | always |
| Q8 | **Assessor + action owners** | free-text | "Who is the competent person performing this assessment (role), and who will own the work-design actions? (named **role**, no 'TBD')" | ELI-COMPETENCY | always |
| Q9 | **Review cycle / next review** | MCQ + free-text | Annual / On change (MoC — e.g. after restructure) / Other (+date) | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q5 = India → Q5a + `KB-REG-IN-STATEFORMS`; **mandatory**).
Domain branches (Q2) activate the per-domain hazard+control walk in
`KB-SNIP-HSE-MGMT-STANDARDS` for each selected domain.

## Echo-back

After the last applicable question (Q9, and Q5a if the India branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing: psychosocial risk for the night-shift contact-centre advisers (Site B),
domains demands + control + support, sources = HSE Indicator survey + focus groups +
sickness-absence (each ≥5-respondent threshold), trigger = recent restructure, 5×5
matrix, UK, review annual — correct?" Confirm the **≥2 data sources** before any rating.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "assess the whole company's stress" or any
  unnamed unit; require a named team/role/function (or an explicit sampling plan). Record
  `[ASSUMPTION]` / `[GAP]`, never invent a unit.
- **Q3 is the triangulation gate** — **refuse to produce a rating on a single data source
  or a single anecdote.** Require at least two sources for the named unit; if only one is
  available, flag `[GAP]` and ask for corroborating data before rating.
- **Never name an individual as the "risk"** — the assessment is of the work design; a
  finding is always attributed to a role/group, never a person.

## Domain evidence types (ELI-EVIDENCE)

Validated psychosocial survey (HSE Indicator Tool or equivalent, banded against
`KB-DATA-PSYCHOSOCIAL-INDICATORS` with source+year) · focus-group themes (aggregated) ·
sickness-absence & turnover trends · grievance/incident patterns. All are
**special-category health data** — apply the reinforced `references/deid-checklist.md`
(<5 suppression, secondary suppression, no individual named) before any analysis.
