---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A patient-handling assessment assesses the named care task's current handling and equipment state afresh; there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the avoid-the-manual-lift decision (Q2) and the TILE assessment of the residual (Q3) are the assessment's starting facts."
    ELI-SCORING: "The TILE assessment and the mobility-and-equipment matrix are a structured assessment frame, not a calculated score; the residual moving-and-handling risk is framed via the standard risk_matrix 5x5 after controls (NOT a NIOSH-equation engine), so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: "no-or-partly", activates_questions: [Q3], activates_kb_row: KB-SNIP-TILE-PEOPLE, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-UK-MHOR, mandatory: true}
---

# Structured intake — patient-handling-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named care task & setting (Q1 — the specificity anchor)**, then — **first among the
controls** — the **avoid-the-manual-lift decision (Q2)** (avoiding the manual lift is the primary
control, not the technique), the **four-element TILE assessment of the residual (Q3)**, the
**mobility-and-equipment matrix (Q4)**, the **bariatric / falls branch (Q5)**, and the
**jurisdiction (Q6)**. **Refuse to assess "moving patients": you need the named care task + setting
(Q1) and the avoid-the-manual-lift decision (Q2) before any control plan. Refuse a "use good
technique / wear a back belt" treatment where the manual lift could be avoided with a mechanical
aid.** The TILE assessment is a structured frame — never a calculation — and a missing input is a
`[GAP]`, never an invented task, weight band, or count.

**De-identify FIRST** — patient mobility data and a worker's musculoskeletal record are
special-category health data (PHI). Before the echo-back drives any analysis, assess the patient by
de-identified mobility / dependency / weight band (never a name, ward/bay, or diagnosis), role-label
the worker (the worker's back-condition / OH record held separately), and apply `<5` small-cell
suppression to every handling-injury category aggregated across the unit (`references/deid-checklist.md`).

Two load-bearing branches: the **TILE-assessment branch** (Q2 = no/partly → Q3, the four-element TILE
assessment of the residual; non-mandatory) and the **mandatory India→state branch** (Q6 = India →
Q6a + `hse-india`; factory/occupational ergonomics; confirm the state before citing any rule — never a
national form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named care task & setting** (bed-to-chair transfer / repositioning / lateral transfer / falls recovery / bariatric move / ambulance loading + setting) | free-text | "Name the exact handling task + the setting (ward / care home / community / ambulance). **Refuse 'moving patients' / 'the ward' — the assessment is task-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Can the manual lift be avoided?** (asked FIRST among the controls — avoiding the manual lift is the primary control; yes → the assessment leads with a ceiling/mobile hoist, slide sheet, or transfer board; no/partly → branch to a TILE assessment of the residual, Q3) | mcq | yes / no-or-partly | ELI-SCOPE | always |
| Q3 | *(if not fully avoided)* **TILE assessment of the residual handling** | free-text | "Assess the unavoidable handling against the MHOR Schedule 1 TILE filter — **Task** (frequency, posture, distance, twisting) · **Individual** (the worker's capability, training, number of handlers — never the worker's medical record in the circulated copy) · **Load** (the patient's weight band, dependency, cooperation, attachments — de-identified) · **Environment** (space, floor, bed/chair height, ceiling-track availability). **A TILE assessment missing any of the four elements is not suitable and sufficient — refused.**" | ELI-OBLIGATIONS | Q2 != yes |
| Q4 | **Mobility-and-equipment matrix** | free-text | "The patient's mobility / dependency level → the matched equipment + the number of handlers (the matrix is the core artifact). **A 'two-person manual lift' recommended where a hoist or slide aid is reasonably available is FLAGGED** and pushed up the hierarchy." | ELI-EVIDENCE | always |
| Q5 | **Bariatric / special** | mcq | bariatric (→ equipment SWL, environmental loading, extended planning) / falls (→ post-fall handling plan) / routine | ELI-EXPOSURE | always |
| Q6 | **Jurisdiction** | mcq | UK / USA / International / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; factory/occupational ergonomics; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / care setting | mcq+free-text | Acute hospital / Rehab / Care-home / Community-home care / Ambulance-patient-transport / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / unit / area is the care task in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full patient-handling risk assessment (consultant) / handling-assessment summary + matrix (manager) / quick mechanical-aid + handler-count answer (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the equipment-provision / training / environmental-modification actions and who is the competent person (moving-and-handling / ergonomics specialist) verifying the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | annual / on-change-of-task-or-patient / on-incident / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `tile-assessment` (Q2 = no/partly → Q3 + `KB-SNIP-TILE-PEOPLE`; the four-element TILE
assessment of the residual; non-mandatory); `india-state` (Q6 = India → Q6a + `hse-india`;
**mandatory**).

## Echo-back

After the last applicable question (Q11, and Q3 / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Building a patient-handling risk assessment for: the bed-to-chair transfer on the rehab ward, UK;
manual lift avoided (ceiling hoist substituted) where reasonably practicable; TILE assessed on the
residual repositioning (all four elements); mobility-and-equipment matrix by dependency level;
bariatric SWL addressed; full assessment; review annually — correct?" The TILE assessment is a
structured frame, never a calculation; the patient is referenced by de-identified mobility/dependency/
weight band and the worker by role only.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "moving patients" / "the ward"; ask again or record
  `[GAP]`, never invent the care task or its setting.
- **Avoid the manual lift first, technique/PPE last** — a "use good technique / wear a back belt"
  treatment with no avoid-the-manual-lift / mechanical-aid step is **refused and pushed up the
  hierarchy**; technique is administrative and a back belt is PPE, never the primary control where the
  manual lift could be avoided. A "two-person manual lift" recommended where a hoist or slide aid is
  reasonably available is flagged. A TILE assessment missing any of the four elements is refused.
- **PHI gate** — the skill **never** writes the patient's name, ward/bay, diagnosis, or care-plan
  detail, the worker's name or back-condition record, or a sub-five handling-injury count into the
  circulated artifact; the re-identification key is held separately, never co-located and never
  emitted as a key file. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The avoid-the-manual-lift decision (Q2) · the four-element TILE assessment of the residual handling
(Q3 — Task / Individual / Load / Environment) · the mobility-and-equipment matrix (Q4 — dependency
level → equipment + handler count) · the bariatric / falls plan (Q5 — equipment SWL, environmental
loading, post-fall handling) · the de-identified handling-injury data aggregated across the unit (with
`<5` suppression) · the patient assessed by de-identified mobility / dependency / weight band · the
worker's capability under TILE Individual (de-identified to role level — the worker's back-condition /
OH record is highest-sensitivity PHI, held separately).
