---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-OBLIGATIONS: "PPE selection is grounded in the body-region duty map (OSHA 1910.132 + Subpart I sections, EN/ANSI conformity standards), not a substance-exposure-limit obligation; the regulatory leg (UK/EU PPE at Work Regs 1992, OSHA 1910.132, India Factories Act via hse-india) is resolved from the Q6 jurisdiction, so a dedicated obligations question is not asked."
  branches:
    - {when: Q2, option: respiratory, activates_questions: [Q4a], activates_kb_row: KB-DATA-PPE-STANDARDS, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — ppe-matrix

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named scope (Q1 — the specificity anchor)**, captures the **body-region hazards (Q2)**, then
runs the **controls-first gate (Q3)** per hazard, and finishes with conditions, existing PPE,
and the jurisdiction. **Refuse to emit any PPE row until the named scope (Q1), the body-region
hazards (Q2), and — for each hazard — the higher-order controls considered (Q3) are captured.**
A hazard with no higher-order control recorded is a **controls-first FLAG, never an invented
PPE row**; never fabricate a PPE selection to fill the gate.

Two load-bearing branch families: the **respiratory-fit branch** (Q2 = respiratory → Q4a fit /
medical-clearance need, role-level only; non-mandatory) and the **mandatory India→state branch**
(Q6 = India → Q6a + `hse-india`; confirm the state before citing any rule — never a national
form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named scope** (the area / line / role set + the tasks performed) | free-text | "Name the exact area, line, or role set and the tasks (e.g. 'line-3 fettling cell — fettler + grinder roles, manual grinding + deburring'). **Refuse a generic or site-wide PPE sheet ('PPE for the whole plant') — the matrix is task-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Hazards by body region** (per OSHA Subpart I; per task in scope) | mcqmulti-select | eye/face / head / hearing / respiratory / hand-arm / foot-leg / body-torso | ELI-SCOPE | always |
| Q3 | **Higher-order controls considered** (**the controls-first gate, per hazard, MANDATORY**) | free-text(structured) | "For EACH Q2 hazard, what elimination / substitution / engineering / administrative controls are in place or justified? **PPE is selected only for the residual hazard surviving those controls. A hazard with NO higher-order control recorded triggers a controls-first FLAG, NOT a PPE row** — never invent a PPE row to fill the gate." | ELI-EVIDENCE | always |
| Q4 | **Task duration & conditions** | mcq+free-text | occasional / regular / continuous shift-long (+ environment: heat / confined-space / IDLH) — sets respiratory-fit & clearance needs | ELI-EXPOSURE | always |
| Q4a | *(respiratory only)* Fit & medical-clearance need | free-text→role | "Is respirator fit-testing + medical clearance required for this role, and what is the residual respiratory hazard? **Report the requirement at role level — never a named worker's clearance result (special-category health data, `<5` suppression).**" | ELI-BASELINE | Q2 == respiratory |
| Q5 | **Existing PPE & gaps** | free-text | "What PPE is issued today, and where does it not match the residual hazard or carry no cited conformity standard?" | ELI-SCORING | always |
| Q6 | **Jurisdiction** | mcq | India / UK / USA / EU / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Manufacturing / Warehousing-Logistics / Construction / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site/area/line is the task performed in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full PPE matrix report + certification (consultant) / task×hazard→PPE grid (manager) / quick per-task PPE list (frontline) | ELI-OUTPUT | always |
| Q10 | **Certifier + action owners** | free-text | "Who is the competent person (named role) certifying the PPE hazard assessment (1910.132(d)(2)), and who owns the PPE-gap & controls-first actions? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-task-change / on-PPE-change / annual / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `respiratory-fit` (Q2 = respiratory → Q4a + `KB-DATA-PPE-STANDARDS`; role-level
only; non-mandatory); `india-state` (Q6 = India → Q6a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q4a / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Building the PPE matrix for: line-3 fettling cell (fettler + grinder roles), Plant 3,
Maharashtra; hazards eye/face + hearing + hand-arm + respiratory; higher-order controls recorded
per hazard (LEV on the grinding bench → engineering); residual hazards only → PPE; continuous
shift-long; full report + 1910.132(d)(2) certification; review on task-change — correct?" Each
hazard runs the controls-first gate individually at the gate step.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse a generic or site-wide PPE sheet ("PPE for the whole
  plant", "the factory"); ask again or record `[GAP]`, never invent a scope.
- **No PPE row without the controls-first gate** — if, for a given hazard, Q3 records no
  higher-order control considered/justified, **do not emit a PPE row**: emit a **controls-first
  FLAG** ("higher-order controls not considered — assess and apply before specifying PPE") and
  withhold the PPE cell. A missing input is a `[GAP]`, never a fabricated PPE selection. **Never
  proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The per-task body-region hazards (Q2) · the higher-order controls in place or justified per
hazard (Q3 — the controls-first gate inputs) · the task duration / conditions (Q4) · the
existing PPE issued and its cited conformity standard (Q5) · any respiratory fit / medical-
clearance requirement (**role-level only, special-category health data, `<5` suppression**) ·
photos of the task / PPE (de-identified — no faces, no name).
