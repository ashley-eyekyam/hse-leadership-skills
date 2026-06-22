---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-OBLIGATIONS: "Ergonomics scoring is grounded in the method's published action bands (NIOSH / RULA / REBA / ISO 11228), not a substance-OEL obligation; the regulatory leg (UK MHO/DSE Regs 1992, OSHA general duty, India Factories Act via hse-india) is resolved from the Q6 jurisdiction, so a dedicated obligations question is not asked."
  branches:
    - {when: Q1, option: NIOSH lifting, activates_questions: [Q3a], activates_kb_row: KB-STD-ISO11228, mandatory: false}
    - {when: Q1, option: RULA upper-limb, activates_questions: [Q3b], activates_kb_row: KB-STD-ISO11228, mandatory: false}
    - {when: Q1, option: REBA whole-body, activates_questions: [Q3b], activates_kb_row: KB-STD-ISO11228, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — ergonomics-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**assessment type (Q1)**, which branches to that method's required parameters, then captures
the **named task/workstation (Q2 — the specificity anchor)**, the **task parameters (Q3,
method-driven)**, the exposure pattern, the affected population, and the jurisdiction.
**Refuse to produce a score until the assessment method (Q1), the named task/workstation (Q2),
and the method's required input parameters (Q3) are captured** — ask again, or record `[GAP]`;
**never invent a posture angle or a load weight.**

Two load-bearing branch families: the **per-method parameter branch** (Q1 = NIOSH → Q3a lift
geometry; Q1 = RULA/REBA → Q3b joint angles + force/repetition; the `KB-STD-ISO11228` row +
the `ergonomics` engine; non-mandatory); and the **mandatory India→state branch** (Q6 = India
→ Q6a + `hse-india`; confirm the state before citing any rule — never a national form number,
emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Assessment type** (the scoring method — manual lifting & lowering, upper-limb & whole-body posture, push-pull, repetitive, or DSE; branch to that method) | mcq multi-select | NIOSH lifting / RULA upper-limb / REBA whole-body / ISO 11228-2 push-pull / ISO 11228-3 repetitive / DSE-workstation | ELI-SCOPE | always |
| Q2 | **The named task / workstation & role** | free-text | "Name the exact task, the role doing it, and the workstation (e.g. 'despatch-bay carton lift, line-2 packer, pallet→conveyor'). **Refuse a generic task ('general handling') — this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q3 | **Task parameters** (method-driven) | mcq+free-text | "Which captured parameters do you have for the selected method?" — branches to Q3a (NIOSH) or Q3b (RULA/REBA) | ELI-EVIDENCE | always |
| Q3a | *(NIOSH only)* Lift geometry & load | free-text(ints) | "Provide load weight (kg), horizontal & vertical origin/destination (cm), asymmetry angle (degrees), frequency (lifts/min), coupling (good/fair/poor), duration (h) so the `ergonomics` engine computes the RWL + Lifting Index. **A missing required parameter is a `[GAP]`, not a guess.**" | ELI-SCORING | Q1 == NIOSH |
| Q3b | *(RULA/REBA only)* Joint scores & force | free-text(ints) | "Provide the observed joint angles/scores (upper arm, lower arm, wrist, trunk, neck, legs), the force/load score, and muscle-use/repetition so the `ergonomics` engine computes the grand/final score deterministically. **A missing joint score is a `[GAP]`, not an invented angle.**" | ELI-SCORING | Q1 == RULA or REBA |
| Q4 | **Exposure pattern** | mcq | occasional / regular / continuous shift-long — sets the NIOSH frequency multiplier and the surveillance linkage | ELI-EXPOSURE | always |
| Q5 | **Affected population & reported symptoms** | free-text→role | "Which role/SEG does this task, and are there reported MSD symptoms? **Reported symptoms and fitness detail are special-category health data — de-identify to role/SEG; small cells (<5) are suppressed.**" | ELI-BASELINE | always |
| Q6 | **Jurisdiction** | mcq | India / UK / USA / EU / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Manufacturing / Warehousing-Logistics / Construction / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site/area/line is the task performed in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full ergonomics assessment report (consultant) / single-task score + controls (manager) / quick RULA-REBA check (frontline) | ELI-OUTPUT | always |
| Q10 | **Assessor + action owners** | free-text | "Who is the competent person (ergonomist / occupational-health professional role) performing this, and who owns the redesign & surveillance actions? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-task-change / on-symptom-trigger / annual / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `niosh-parameters` (Q1 = NIOSH → Q3a + `KB-STD-ISO11228` + the engine;
non-mandatory); `posture-parameters` (Q1 = RULA/REBA → Q3b + `KB-STD-ISO11228` + the engine;
non-mandatory); `india-state` (Q6 = India → Q6a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q3a/Q3b, Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing: despatch-bay carton lift (line-2 packer SEG), Plant 3, Maharashtra, NIOSH method,
load 16 kg / H 30 cm / V-origin 40 cm / V-dest 150 cm / asymmetry 30° / 4 lifts-min / fair
coupling / 2 h, regular pattern, full report, review on task-change — correct?" Each task is
scored by the engine individually at the scoring step.

## Refuse-on-vague anchors

- **Q2 is the specificity anchor** — refuse a generic task ("general handling", "the line") or
  an unnamed workstation; ask again or record `[GAP]`, never invent a task.
- **No score without the required parameters** — if Q1 (method), Q2 (named task) and Q3 (the
  method's required parameters) are not all captured, **do not produce a score**; a missing
  required parameter is a `[GAP]`, never a guessed posture angle or load weight. **Never
  proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The ergonomics-engine inputs (lift geometry for NIOSH; observed joint angles + force/repetition
for RULA/REBA) · the exposure pattern / lift frequency · any prior reported MSD symptoms
(**special-category health data, de-identified by role/SEG**) · the org risk matrix if
non-default · photos/video of the posture (de-identified — no faces, no name).
