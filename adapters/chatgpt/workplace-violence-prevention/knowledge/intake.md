---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A WPV program assesses the named service's current exposure + control state afresh through the worksite hazard analysis (Q3); there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the worksite hazard analysis (Q3) and the current environmental/administrative control state (Q4) are the assessment's starting facts."
    ELI-SCORING: "WPV control is a structured environmental-and-administrative-control-first method, not a calculated score; the residual violence risk is framed qualitatively via risk_matrix after controls, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — workplace-violence-prevention

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named service & exposure (Q1 — the specificity anchor)**, then the **violence type(s) (Q2 —
the type-1-4 taxonomy)**, the **worksite hazard analysis (Q3 — the defensibility anchor)**, the
**environmental & administrative controls (Q4 — asked BEFORE reactive/PPE measures)**, the
**de-escalation / response / training (Q5 — the residual line)**, and the **jurisdiction (Q6)**.
**Refuse to plan for "a hospital": you need the named service + where/when violence occurs (Q1)
and the violence type(s) (Q2) before any control plan. Refuse a reactive-led "issue personal
alarms / run self-defence training" treatment where the exposure could be designed out by
environmental or administrative controls.** The control selection is a structured
environmental-and-administrative-first method — never a calculation — and a missing input is a
`[GAP]`, never an invented incident or count.

**De-identify FIRST** — workplace-violence incident data is special-category health data
(PHI). Before the echo-back drives any analysis, scrub any named victim, assailant, or
known-risk patient and any behavioural-health flag, and apply `<5` small-cell suppression to
every incident category (`references/deid-checklist.md`).

Two load-bearing branches: the **reactive-led FLAG branch** (Q4 = a program that jumps to
"personal alarms / restraint training" without environmental design and staffing → FLAG and
push up the hierarchy via `KB-SNIP-WPV-CONTROLS`; non-mandatory) and the **mandatory
India→state branch** (Q6 = India → Q6a + `hse-india`; confirm the state before citing any
rule — never a national form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named service & exposure** (ED / mental-health unit / reception-triage / community-lone-visit / ambulance / care home + where/when violence occurs) | free-text | "Name the exact unit/service **and where/when violence occurs**. **Refuse 'a hospital' / 'the ward' — the program is service-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Violence type(s)** (the OSHA/NIOSH type-1-4 taxonomy — each type drives a different control set; classify before controlling) | mcqmulti | type 1 criminal-intent · type 2 customer/patient/client (the dominant healthcare type) · type 3 worker-on-worker · type 4 personal-relationship | ELI-SCOPE | always |
| Q3 | **Worksite hazard analysis** (the defensibility anchor) | free-text | "The records/incident review, the walkthrough findings, the employee survey. **Use de-identified, aggregated incident data — never a named victim or assailant.** A program with no worksite hazard analysis fails." | ELI-EVIDENCE | always |
| Q4 | **Environmental & administrative controls** (asked BEFORE reactive/PPE measures) | mcqmulti-select+free-text | controlled access & egress · sightlines/reception design · alarm/duress/panic systems · CCTV · waiting-area design · staffing & skill-mix · lone-working procedures · known-risk-patient flagging (de-identified) — **a program that jumps to "personal alarms / restraint training" without environmental design and staffing is FLAGGED as reactive-led** | ELI-OBLIGATIONS | always |
| Q5 | **De-escalation, response & training (residual)** | free-text | "The de-escalation procedure, the response/security protocol, post-incident support, the training plan — the documented residual lines, **never the headline control**." | ELI-EXPOSURE | always |
| Q6 | **Jurisdiction** | mcq | USA (OSHA 3148 + §5(a)(1); Cal/OSHA 8 CCR 3342 where applicable) / UK (HSE work-related-violence + NICE NG10) / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / care setting | mcq+free-text | Acute hospital / Emergency department / Mental-health / Primary-community care / Ambulance-patient-transport / Care-home / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / unit / area is the service in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full WPV prevention program (consultant) / WPV control summary + incident-log structure (manager) / quick environmental/administrative-controls answer (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the access-control / alarm / staffing / training actions and who is the competent person (healthcare-security / WPV / occupational-health professional) verifying the program (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | annual program review / on-incident / on-service-change / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `reactive-led-flag` (Q4 = reactive-led without environmental/administrative
controls → FLAG + `KB-SNIP-WPV-CONTROLS`; the environmental-and-administrative-before-reactive
push; non-mandatory); `india-state` (Q6 = India → Q6a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q4 / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Building a WPV prevention program for: the emergency department, evening / overnight reception &
triage, Maharashtra; violence types in scope — type 2 patient/visitor + type 1 criminal-intent;
worksite analysis from the de-identified incident log + a walkthrough + a staff survey;
environmental controls — controlled access, triage sightlines, duress alarms; administrative —
staffing/skill-mix, lone-working procedure, de-identified known-risk-patient flagging;
de-escalation/response training as the residual line; full program; review annually — correct?"
The control selection is a structured environmental-and-administrative-first method, never a
calculation; no victim, assailant, or known-risk patient is named.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a hospital" / "the ward"; ask again or record
  `[GAP]`, never invent the service or its exposure.
- **Environmental/administrative first, reactive last** — a reactive-led treatment ("issue
  personal alarms / run self-defence training") with no environmental or administrative control
  is **refused and pushed up the hierarchy**; a reactive measure is the residual line, never the
  primary control where the exposure could be designed out. A program with no worksite hazard
  analysis fails.
- **PHI gate** — the skill **never** writes a named victim, assailant, or known-risk patient, a
  behavioural-health flag, or a sub-five incident count into the circulated artifact; the
  re-identification key is held separately, never co-located and never emitted as a key file.
  **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The worksite hazard analysis (Q3 — de-identified records / incident review, walkthrough,
employee survey) · the violence-type classification (Q2 — type-1-4) · the environmental /
engineering controls (Q4 — controlled access, sightlines, alarms / duress, secure design) · the
administrative controls (Q4 — staffing / skill-mix, lone-working, de-identified
known-risk-patient flagging, reporting culture) · the de-escalation / response protocol + the
training plan + post-incident support (Q5 — the residual lines) · the de-identified / aggregated
WPV incident log structure · a prior violence incident referenced for context (de-identified to
role level — a named victim / assailant / known-risk patient and any behavioural-health flag are
highest-sensitivity PHI).
