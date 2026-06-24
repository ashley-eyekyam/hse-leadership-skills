---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "Transmission-based IPC is a structured route-driven precaution-selection method, not a calculated score; the residual transmission risk is framed qualitatively via risk_matrix after controls, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: airborne, activates_questions: [Q3], activates_kb_row: KB-SNIP-IPC-PRECAUTIONS, mandatory: false}
    - {when: Q7, option: India, activates_questions: [Q7a], activates_kb_row: KB-REG-IN-BMW2016, mandatory: true}
---

# Structured intake — infection-control-plan

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named service & unit (Q1 — the specificity anchor)**, then the **agent(s) and their
transmission route(s) (Q2 — the routing anchor)** which drive the precautions, the **engineering
controls available (Q3 — asked BEFORE PPE)**, the **administrative controls (Q4)**, the **Spaulding
reprocessing decision (Q5)**, the **surveillance (Q6)**, and the **jurisdiction (Q7)**. **Refuse to
plan for "a hospital": you need the named service (Q1) + the agent(s) and their transmission route(s)
(Q2) before any precaution plan. Refuse a PPE-only treatment — an airborne agent managed by a
respirator alone with no airborne-infection isolation room or ventilation provision is rejected and
pushed up the hierarchy.** The precaution selection is a structured route-driven method — never a
calculation — and a missing input is a `[GAP]`, never an invented agent, route, or count.

**De-identify FIRST** — healthcare infection data is special-category health data (PHI). Before the
echo-back drives any analysis, scrub any patient's infection / colonisation status (never attributed
to a named person) and any outbreak / cluster detail (reported aggregated), and apply `<5` small-cell
suppression to every case / cluster category — a 3-case cluster on a named ward re-identifies
patients (`references/deid-checklist.md`).

Two load-bearing branches: the **airborne-engineering branch** (Q2 = airborne → Q3, the AIIR /
ventilation provision; non-mandatory) and the **mandatory India→state branch** (Q7 = India → Q7a +
`hse-india`; BMW Rules 2016 segregation; confirm the state before citing any rule — never a national
form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named service & unit** (ward / clinic / care home / dental surgery / ambulance / lab) | free-text | "Name the exact unit/service. **Refuse 'a hospital' / 'the ward' — the plan is service-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **The agent(s) and their transmission route(s)** (the routing anchor — the route drives the precautions) | mcq+free-text | contact / droplet / airborne / combination (+ the suspected/confirmed agent) | ELI-SCOPE | always |
| Q3 | *(if airborne)* **Engineering controls available** (asked BEFORE PPE) | free-text | "Ventilation, single rooms, negative-pressure / airborne-infection isolation room (AIIR), safer devices. **An airborne agent with no AIIR or ventilation provision controlled by a respirator alone is FLAGGED and pushed up the hierarchy.**" | ELI-BASELINE | Q2 == airborne |
| Q4 | **Administrative controls** | mcq+free-text | cohorting · early screening / triage · isolation signage · restricted entry · hand-hygiene programme + audit — **these precede PPE** | ELI-EXPOSURE | always |
| Q5 | **Device reprocessing (Spaulding)** | free-text | "Which devices contact sterile tissue/bloodstream (critical → **sterilization**), mucous membranes / non-intact skin (semi-critical → **high-level disinfection**), or intact skin (non-critical → low-level)? **High-level disinfection of a critical device is a Spaulding mis-application and fails.**" | ELI-OBLIGATIONS | always |
| Q6 | **Surveillance** | free-text | "HAI / outbreak / cluster monitoring. **Reported de-identified and aggregated; every `<5` case category suppressed (with secondary back-calc guard). Refuse to report an outbreak on a named ward in a way that re-identifies a patient.**" | ELI-EVIDENCE | always |
| Q7 | **Jurisdiction** | mcq | USA / UK / EU / India / Other / Unknown | ELI-JURIS | always |
| Q7a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; BMW Rules 2016 segregation; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q7 == India |
| Q8 | Industry / care setting | mcq+free-text | Acute hospital / Primary-community care / Care-home / Dental / Ambulance-patient-transport / Laboratory / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q9 | Location / site / area | free-text | "Which specific site / unit / room is the service in?" | ELI-LOCATION | always |
| Q10 | Output artifact wanted + its reader | mcq | full IPC plan + programme structure (consultant) / IPC plan summary + surveillance structure (manager) / quick route-precautions answer (frontline) | ELI-OUTPUT | always |
| Q11 | **Action owner(s) + verifier** | free-text | "Who owns the engineering / cohorting / reprocessing / surveillance actions and who is the competent person (infection-prevention & control professional) verifying the plan (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q12 | **Review cycle / next review** | mcq+free-text | annual IPC review / on-outbreak / on-guideline-change / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `airborne-engineering` (Q2 = airborne → Q3 + `KB-SNIP-IPC-PRECAUTIONS`; the AIIR /
ventilation provision; non-mandatory); `india-state` (Q7 = India → Q7a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q12, and Q3 / Q7a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Building an infection control plan for: the respiratory unit, Ward 4B, Maharashtra; agents — a
contact MDRO + a droplet influenza-like illness + a suspected airborne pulmonary TB; engineering
controls — a negative-pressure AIIR for the airborne agent + single rooms; administrative — cohorting
+ screening + hand-hygiene audit; Spaulding — endoscopes high-level-disinfected, surgical instruments
sterilized; surveillance de-identified + aggregated; full plan; review annually — correct?" The
precaution selection is a structured route-driven method, never a calculation; patients are referenced
by role / cohort only and no infection status is attributed to a named person.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a hospital" / "the ward"; ask again or record `[GAP]`,
  never invent the service.
- **Engineering/administrative controls first, PPE last** — a PPE-only treatment (an airborne agent
  managed by a respirator alone with no AIIR / ventilation provision) is **refused and pushed up the
  hierarchy**; a respirator is the residual control, never the primary control where the route demands
  an engineering control.
- **PHI gate** — the skill **never** attributes an infection status to a named patient, never reports a
  sub-five case/cluster cell, and never reports an outbreak on a named ward in a way that
  re-identifies a patient; the re-identification key is held separately, never co-located and never
  emitted as a key file. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The agent(s) and transmission route(s) (Q2) · the engineering controls available — ventilation, AIIR
/ negative pressure, single rooms (Q3) · the administrative controls — cohorting, screening, signage,
hand-hygiene audit (Q4) · the Spaulding reprocessing decision per device class (Q5) · the
de-identified / aggregated HAI / outbreak / cluster surveillance (Q6) · a prior outbreak referenced
for context (de-identified and aggregated — a patient's infection status and any small cluster are
highest-sensitivity PHI, suppressed against re-identification).
