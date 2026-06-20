---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-LOCATION, ELI-EXPOSURE, ELI-EVIDENCE, ELI-SCORING]
  omits:
    ELI-JURIS: "dispersion physics is jurisdiction-neutral; the regulatory wrapper (COMAH/Seveso/MSIHC) sits in the target-study skill"
    ELI-INDUSTRY: "process context implied by substance/inventory"
    ELI-BASELINE: "assistive framing tool — no standing controls to baseline"
    ELI-OBLIGATIONS: "obligation locus sits in bowtie-builder/lopa-worksheet/comah-safety-report-assistant"
    ELI-COMPETENCY: "owner locus sits in the downstream target-study skill"
    ELI-TEMPORAL: "scenario framing is point-in-time; no review cadence to elicit"
  branches:
    - {when: Q1, option: bowtie, activates_questions: [Q7]}
    - {when: Q1, option: LOPA, activates_questions: [Q7]}
    - {when: Q5, option: "for-modeller (`[GAP]`)", activates_questions: []}
---

# Structured intake — toxic-release-dispersion-scenario

> **Deliberately the most omit-heavy skill in the family — assistive-only, hands off.
> Its short `omits` list is correct by design, not a coverage failure.**

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a dispersion
distance/concentration). Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What is the scenario framing for — a bowtie, a LOPA, a QRA input, or an emergency-plan/siting study? | MCQ | bowtie / LOPA / QRA-input / emergency-plan-zone | ELI-SCOPE | always |
| Q2 | Released substance + CAS + the inventory at risk (mass). | free-text | substance + mass; refuse "a toxic gas" | ELI-SUBJECT | always |
| Q3 | Physical state + storage pressure/temperature. | MCQ + free-text | gas / liquefied-gas / liquid; P, T | ELI-EVIDENCE | always |
| Q4 | Release scenario. | MCQ | catastrophic (full-bore) / continuous (leak) / instantaneous (puff) | ELI-SUBJECT | always |
| Q5 | Do you hold a release rate / hole size, or should the modeller derive it? | MCQ + free-text | supplied (give value) / for-modeller (`[GAP]`) | ELI-EVIDENCE | always |
| Q6 | Toxicity benchmark you want zoned against. | MCQ | AEGL / ERPG / IDLH / SLOT-SLOD / unknown | ELI-EVIDENCE | always |
| Q7 | Release point + receptor distance/direction + typical weather (wind, stability). | free-text | scenario geometry for the modeller | ELI-LOCATION | always |
| Q8 | Receptors at risk. | MCQ multi-select | on-site workers / public / environment | ELI-EXPOSURE | always |
| Q9 | Output format / reader for the scenario brief. | MCQ | modelling-input brief / siting-study input / emergency-plan-zone framing | ELI-OUTPUT | always |
| Q10 | Org consequence band scheme for the qualitative consequence axis. | MCQ | org scheme / default 5×5 — qualitative band only, NOT a modelled result | ELI-SCORING | always |

**Branch map**
- `Q1 == bowtie` → hand the consequence side to **`bowtie-builder`** (`KB-STD-CCPS-BOWTIE`), name it as downstream owner.
- `Q1 == LOPA` → hand to **`lopa-worksheet`** (`KB-STD-IEC-61511`).
- `Q1 ∈ {QRA-input, emergency-plan-zone}` → frame as an input set, **explicitly not a modelled result**.
- `Q5 == for-modeller` → release rate is `[GAP]`; **never compute from first principles, never run PHAST/ALOHA** (METHODOLOGY step 2/4) — **core rule**.
- `Q7` any quantitative distance/concentration → `[GAP]` unless user-supplied; qualitative `risk_matrix` band only.
- `Q6 == unknown` → `[GAP]`, flag the benchmark for the competent modeller.

## Echo-back
> "**Scenario framing only — this is NOT a quantitative dispersion result.** Substance **{substance/CAS}**, inventory **{mass}**, state **{gas/liquid}** at **{P,T}**; release **{catastrophic/continuous/instantaneous}**; release rate **{supplied / [GAP] for modeller}**; benchmark **{AEGL/ERPG/IDLH}**; geometry **{release point, receptor distance, weather}**; receptors **{on-site/public/env}**; target study **{bowtie/LOPA/QRA}**. I will give a qualitative consequence band, flag every un-modelled value `[GAP]`, and hand the consequence side to **{study skill}**. I will not run PHAST/ALOHA or invent a distance/concentration. Confirm."

Echo the captured facts back and **confirm before any framing** — and re-state that the
output is scenario framing for a competent-person study, not a modelled result.

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "a toxic gas leak" → demand substance + CAS + inventory; **never proceed on a vague subject**.
- Any request for a modelled distance/concentration → refuse; `[GAP]` + hand to competent modeller (assistive, no modelling).
- No invented dispersion figure, ever.

**Domain evidence types (`ELI-EVIDENCE`)**
Inventory mass, storage P/T, physical state, hole-size/leak scenario, toxicity benchmarks (AEGL/ERPG/IDLH/SLOT-SLOD), release point + receptor geometry, site weather/stability data, any user-supplied source-term calc.
