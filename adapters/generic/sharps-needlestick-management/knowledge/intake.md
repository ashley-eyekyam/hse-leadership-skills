---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A sharps program assesses the named service's current sharps inventory + control state afresh; there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the elimination/substitution decision (Q2) and the current device/work-practice state (Q3/Q4) are the assessment's starting facts."
    ELI-SCORING: "Sharps control is a structured engineering-control-first method, not a calculated score; the residual sharps-exposure risk is framed qualitatively via risk_matrix after controls, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: "no", activates_questions: [Q3], activates_kb_row: KB-SNIP-SHARPS-HIERARCHY, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-BMW2016, mandatory: true}
---

# Structured intake — sharps-needlestick-management

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named service & sharps inventory (Q1 — the specificity anchor)**, then — **first among the
controls** — the **elimination/substitution decision (Q2)** (eliminating the sharp is the primary
control, not the safety device), the **safety-engineered-device process (Q3)**, the **work
practices & disposal (Q4)**, the **exposure-response pathway (Q5)**, and the **jurisdiction (Q6)**.
**Refuse to plan for "a clinic": you need the named service + its real sharps inventory (Q1) and
the elimination/substitution decision (Q2) before any control plan. Refuse a behaviour-led "staff
to take care / wear gloves" treatment where the sharp could be eliminated or a safety-engineered
device fitted.** The control selection is a structured engineering-first method — never a
calculation — and a missing input is a `[GAP]`, never an invented device or count.

**De-identify FIRST** — bloodborne-pathogen exposure data is special-category health data
(PHI). Before the echo-back drives any analysis, scrub the source-patient identity + serostatus,
the injured worker's identity + PEP record, and apply `<5` small-cell suppression to every
sharps-injury category (`references/deid-checklist.md`).

Two load-bearing branches: the **engineering-controls branch** (Q2 = no → Q3, the
safety-engineered-device process; non-mandatory) and the **mandatory India→state branch** (Q6 =
India → Q6a + `hse-india`; BMW Rules 2016 sharps segregation; confirm the state before citing any
rule — never a national form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named service & sharps inventory** (ward / phlebotomy round / dental surgery / ambulance / lab + the sharps actually used) | free-text | "Name the exact unit/service + the sharps actually used (hollow-bore needles, lancets, scalpels, IV cannulae, suture needles, phlebotomy, dental). **Refuse 'a clinic' / 'the ward' — the plan is service-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Can any sharp be eliminated or substituted?** (asked FIRST among the controls — eliminating the sharp is the primary control; yes → the plan leads with elimination / needle-free substitution; no → branch to engineering controls, Q3) | mcq | yes / no | ELI-SCOPE | always |
| Q3 | *(if not eliminated)* **Safety-engineered devices + frontline selection** | free-text | "Which devices have an integrated sharps-protection mechanism, which do not, and the frontline-worker selection process? **A non-engineered device still in use without a recorded justification is FLAGGED** — OSHA mandates a documented annual safer-device evaluation with non-managerial frontline-worker input." | ELI-OBLIGATIONS | Q2 == no |
| Q4 | **Work practices & disposal** | mcq+free-text | no-recapping rule · point-of-use sharps containers (fill line, location) · safe-disposal route · single-handed/scoop technique — **a plan permitting recapping by hand fails** | ELI-EXPOSURE | always |
| Q5 | **Exposure-response pathway** | free-text | "The post-exposure pathway: immediate first aid → **confidential** incident report → **source-patient testing with consent and confidentiality** → PEP timing for HBV/HCV/HIV → follow-up → the Sharps Injury Log entry. **Refuse to draft a pathway that names a source patient or worker in the circulated plan.**" | ELI-EVIDENCE | always |
| Q6 | **Jurisdiction** | mcq | USA / EU / UK / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; BMW Rules 2016 sharps segregation; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / care setting | mcq+free-text | Acute hospital / Primary-community care / Dental / Ambulance-patient-transport / Laboratory / Care-home / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / unit / room is the service in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full sharps prevention & exposure-control package (consultant) / sharps-control summary + log structure (manager) / quick safer-device + no-recapping answer (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the device-changeover / training / log-implementation / vaccination actions and who is the competent person (occupational-health / IPC professional) verifying the plan (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | annual safer-device review / on-device-change / on-incident / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `engineering-controls` (Q2 = no → Q3 + `KB-SNIP-SHARPS-HIERARCHY`; the
safety-engineered-device + frontline-selection process; non-mandatory); `india-state` (Q6 = India →
Q6a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q3 / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Building a sharps prevention & exposure-control package for: the phlebotomy round, Day-Ward 4B,
Maharashtra; sharps in use — hollow-bore needles + IV cannulae; some sharps eliminated (needle-free
connectors on IV lines); safety-engineered cannulae adopted with frontline input; no-recapping +
point-of-use bins; confidential PEP pathway with consented source-testing; full package; review
annually — correct?" The control selection is a structured engineering-first method, never a
calculation; the source patient and the injured worker are referenced by role only.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a clinic" / "the ward"; ask again or record `[GAP]`,
  never invent the service or its device list.
- **Elimination first, PPE/behaviour last** — a behaviour-led / PPE-led treatment ("staff to take
  care / wear gloves") with no elimination or safety-engineered-device step is **refused and pushed
  up the hierarchy**; a behaviour rule is administrative, never the primary control where the sharp
  could be eliminated or engineered out. A plan permitting recapping by hand fails.
- **PHI gate** — the skill **never** writes a source-patient identity, a worker's name, a
  serostatus, or a sub-five injury count into the circulated artifact; the re-identification /
  exposure key is held separately, never co-located and never emitted as a key file. **Never proceed
  on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The elimination/substitution decision (Q2) · the safety-engineered-device process + the documented
annual safer-device consideration with frontline-worker involvement (Q3) · the work-practice &
disposal controls (Q4 — no-recapping, point-of-use bins, safe-disposal route) · the confidential
post-exposure (PEP) pathway (Q5 — first-aid, consented source-testing, PEP timing for HBV/HCV/HIV,
follow-up) · the de-identified/aggregated Sharps Injury Log structure · the HBV-vaccination status ·
a prior sharps/needlestick exposure referenced for context (de-identified to role level — the
source-patient serostatus and the worker's PEP record are highest-sensitivity PHI).
