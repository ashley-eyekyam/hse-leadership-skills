---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}
  branches:
    - {when: Q0, option: Environmental aspects, activates_questions: [Q-E1, Q-E2, Q-E3, Q-E4, Q-E5], activates_kb_row: KB-STD-ISO14001, activates_output_section: env-aspects-register, mandatory: false}
    - {when: Q0, option: Both, activates_questions: [Q-E1, Q-E2, Q-E3, Q-E4, Q-E5], activates_kb_row: KB-STD-ISO14001, activates_output_section: env-aspects-register, mandatory: false}
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — risk-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
intake opens with the **scope gate (Q0)**, then runs the safety questions; the
**environmental-aspects branch (Q-E1…Q-E5)** is asked *only* when Q0 selects
*Environmental aspects* or *Both*. **Refuse to proceed on a vague task (Q3 is the
specificity anchor)** — ask again, or record `[ASSUMPTION]` / `[GAP]`; never invent.

Two load-bearing branches: the **scope-env branch** (Q0 = Environmental aspects / Both →
Q-E1…Q-E5 + the `KB-STD-ISO14001` row + the env-aspects-register section; non-mandatory)
and the **mandatory India→state branch** (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`;
confirm the state before citing any form — never a national form number).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | Scope of this assessment | MCQ | Occupational safety (default) / Environmental aspects / Both | ELI-SCOPE | always |
| Q1 | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown (India → Q1a) | ELI-JURIS | always |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any form** | ELI-JURIS | Q1 == India |
| Q2 | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q3 | **The task/activity being assessed, broken into steps** | free-text | "Describe the exact task and its steps (e.g. 'confined-space entry to clean tank T-402: isolate → purge → gas-test → enter → clean → exit')." — **the specificity anchor; refuse a vague answer** | ELI-SUBJECT | always |
| Q4 | Location / site | free-text | "Which specific site/area/asset?" | ELI-LOCATION | always |
| Q5 | Who is exposed? | MCQ multi-select | Own workers / Contractors / Public-visitors / Nearby community | ELI-EXPOSURE | always |
| Q6 | Existing controls already in place | free-text | "What controls already exist for this task?" (seeds the initial-vs-residual baseline) | ELI-BASELINE | always |
| Q6b | **Evidence you hold for this task** | free-text | "Prior RA/JSA, exposure or monitoring readings, SDS for substances named in Q3, or incident/near-miss history for this task? (or 'none' → I'll flag `[GAP]`)" | ELI-EVIDENCE | always |
| Q6c | **Task-level obligations** | free-text | "Any permits this task needs (confined-space / hot-work / PTW), exposure limits (WEL/OEL) for substances, or standards your org commits to?" | ELI-OBLIGATIONS | always |
| Q7 | Likelihood band (org scale) | MCQ | 1 Rare / 2 Unlikely / 3 Possible / 4 Likely / 5 Almost certain | ELI-SCORING | always |
| Q8 | Severity band (org scale) | MCQ | 1 Negligible / 2 Minor / 3 Moderate / 4 Major / 5 Catastrophic | ELI-SCORING | always |
| Q9 | Org risk-matrix size | MCQ | 3×3 / 4×4 / **5×5 (default)** / Supply our matrix | ELI-SCORING | always |
| Q10 | Assessment type | MCQ | Baseline (whole task) / Issue-based (a change/hazard) / Continuous (review of an existing RA) | ELI-OUTPUT | always |
| Q10b | **Assessor + action owners** | free-text | "Who is the competent person performing this assessment (role), and who will own corrective actions? (named role/person — no 'TBD')" | ELI-COMPETENCY | always |
| Q10c | **Review cycle / next review** | MCQ + free-text | Annual / On change (MoC) / Other (+date) — feeds the validity/review block | ELI-TEMPORAL | always |
| Q-E1 | The activity / product / service under environmental review | free-text | "Describe the exact activity (e.g. 'solvent degreasing line at Plant 3: load → spray → drain → dry')." — the environmental specificity anchor; refuse a vague answer | ELI-SUBJECT | Q0 == Environmental aspects / Both |
| Q-E2 | Environmental aspects | MCQ multi-select + free-text | Emissions to air / Releases to water / Waste generation / Land contamination / Resource use / Energy use / Noise-odour-other | ELI-SUBJECT | Q0 == Environmental aspects / Both |
| Q-E3 | Associated environmental impacts | free-text | "For each aspect, what is the resulting impact? (e.g. solvent vapour → air quality/VOC; spent solvent → water contamination)." | ELI-SUBJECT | Q0 == Environmental aspects / Both |
| Q-E4 | Operating condition | MCQ multi-select | Normal / Abnormal (start-up/shutdown/maintenance) / Emergency (spill/fire/upset) | ELI-EXPOSURE | Q0 == Environmental aspects / Both |
| Q-E5 | Compliance obligations | free-text | "Any environmental permits, consent limits, or obligations (discharge consents, emission limits, waste licences)?" | ELI-OBLIGATIONS | Q0 == Environmental aspects / Both |

**Branch map:** `scope-env` (Q0 = Environmental aspects / Both → Q-E1…Q-E5 +
`KB-STD-ISO14001` + env-aspects-register; non-mandatory); `india-state` (Q1 = India →
Q1a + `KB-REG-IN-STATEFORMS`; **mandatory**).

## Echo-back

After the last applicable question (Q10c, and Q-E5 if the branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing: confined-space entry to tank T-402, Plant 3, Maharashtra, own workers +
contractors, 5×5 matrix, baseline, review annual — correct?" Q7/Q8 establish the org
scale; each hazard **and each environmental aspect** is scored individually at the
scoring step.

## Refuse-on-vague anchors

- Q3 is the specificity anchor — refuse a vague task ("write me a risk assessment");
  ask again or record `[ASSUMPTION]` / `[GAP]`, never invent a step or a hazard.
- On the environmental branch, Q-E1 is the environmental specificity anchor — refuse a
  vague activity.

## Domain evidence types (ELI-EVIDENCE)

Prior RA/JSA for the task · SDS for any substance named in Q3 · exposure/monitoring
readings (noise, dust, gas, fume) · incident/near-miss history for this task/area · the
org risk matrix if non-default.
