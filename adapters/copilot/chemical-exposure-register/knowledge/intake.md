---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION, ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}   # none material; ELI-LOCATION kept light (SEG work-area, not a tank/route)
  branches:
    - {when: Q1, option: monitoring-plan-only, activates_questions: [Q15]}
    - {when: Q7, option: carcinogen, activates_questions: [Q9, Q11], mandatory: true}
    - {when: Q8, option: none, activates_questions: [Q9]}
    - {when: Q12, option: India, activates_questions: [Q13], mandatory: true}
---

# Structured intake — chemical-exposure-register

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — build a new exposure register, add agents to an existing one, or plan a monitoring/surveillance schedule from an existing register? | MCQ | new register / extend register / monitoring-plan-only | ELI-SCOPE | always |
| Q2 | Name the site and the similar-exposure groups (SEGs) / tasks to cover. | free-text | "e.g. Packing line operators; Drum decanting; Lab analysts" — refuse "all workers" | ELI-SUBJECT | always |
| Q3 | For each SEG, the chemical agents present + CAS. | free-text | agent + CAS per SEG; refuse "various solvents" | ELI-SUBJECT | always |
| Q4 | Approx. number of workers in each SEG. | free-text | integer per SEG (drives <5 suppression + surveillance threshold) | ELI-EXPOSURE | always |
| Q5 | Exposure route(s) for each agent. | MCQ multi-select | inhalation / dermal / ingestion / injection | ELI-EXPOSURE | always |
| Q6 | Task duration & frequency per shift. | free-text | "e.g. 2h decanting × 3/shift" — drives TWA vs STEL framing | ELI-EXPOSURE | per SEG |
| Q7 | Any agent a known carcinogen, mutagen, repro-toxin, respiratory/skin sensitiser, or RCS/lead/asbestos? | MCQ multi-select | carcinogen / mutagen / reprotoxin / sensitiser / RCS / lead / asbestos / none | ELI-EVIDENCE | always |
| Q8 | Do you hold exposure-monitoring data? | MCQ | measured (personal) / measured (static) / modelled / none | ELI-EVIDENCE | always |
| Q9 | Sampling method/standard and metric. | free-text | "e.g. MDHS 14/4, 8-hr TWA + STEL" | ELI-EVIDENCE | if Q8≠none |
| Q10 | Existing controls already in place per SEG. | MCQ multi-select + free-text | LEV / enclosure / substitution / RPE programme / none | ELI-BASELINE | always |
| Q11 | Is health surveillance already running for any agent? | MCQ | yes / no / partial | ELI-OBLIGATIONS | always |
| Q12 | Jurisdiction (sets which OEL/WEL/PEL applies). | MCQ | UK (WEL/COSHH) / EU (REACH/DNEL) / US (OSHA PEL / ACGIH TLV) / India / other | ELI-JURIS | always |
| Q13 | Which Indian state? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — mandatory state detection; confirm before citing any form; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | if Q12==India |
| Q14 | Risk-matrix to band exposure. | MCQ | org matrix / default 5×5 | ELI-SCORING | always |
| Q15 | Who owns the monitoring/surveillance actions, and what review cycle? | free-text | role-label owner + interval | ELI-COMPETENCY / ELI-TEMPORAL | always |
| Q16 | Industry / sector + work environment for the SEG. | MCQ + free-text | manufacturing / O&G / chemicals / pharma / general (+ work-area detail: packing hall, lab, decant bay) | ELI-INDUSTRY / ELI-LOCATION | always |

**Branch map**
- `Q1 == monitoring-plan-only` → skip register-build questions, require an existing register as input → activates the monitoring-schedule output section (Q15).
- `Q7 ∈ {carcinogen, sensitiser, RCS, lead, asbestos}` → activates statutory-surveillance obligation questions (Q9 sampling depth, Q11 surveillance status) + flags surveillance **mandatory** (activates the jurisdiction's KB-REG row).
- `Q8 == none` → `[GAP]` band-confidence reduced + a monitoring action auto-raised (Q9 skipped).
- `Q12 == India` → Q13 state (**mandatory**); referenced OEL flagged **non-statutory** (no Indian statutory OEL list) per METHODOLOGY step 2; "Other"/"Unknown" state → literal `[GAP]`.
- `Q11 == no` AND Q7 triggers surveillance → flag a surveillance-gap finding.

## Echo-back
> "Site **{site}**; SEGs **{list}**; agents **{agent/CAS list}**; routes **{routes}**; carcinogen/sensitiser flags **{flags}**; monitoring data **{measured/modelled/none}**; existing controls **{list}**; surveillance **{status}**; jurisdiction **{juris(+state)}**; matrix **{5×5/org}**. I will band each (SEG×agent) against its cited OEL (source+year), HoC-rank the controls, and suppress any per-worker cell <5. Confirm before I proceed."

Echo the captured facts back and **confirm before any analysis begins**. De-identify
worker names to SEG/role labels in the echo-back (no personal identifiers).

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "all workers" / "the whole plant" → demand named SEGs; **never proceed on a vague subject**.
- "various solvents" / "chemicals" → demand agent + CAS (Q3).
- No OEL resolvable → cite most-protective referenced value, flag non-statutory, never invent (METHODOLOGY).

**Domain evidence types (`ELI-EVIDENCE`)**
SDS per agent, composition %, monitoring reports (personal/static, TWA/STEL, sampling standard), DNEL/DMEL (EU), CMR/sensitiser classification, existing LEV test (LEV/TExT) records, prior surveillance outcomes (aggregated).

**[GAP]** Confirm which limits file is canonical — the KB carries both `data-points/oel-limits.md` (KB-DATA-OEL-LIMITS, cited here) **and** `data-points/exposure-limits.md`; resolve so the persona checks against the intended source and the two do not drift (SME audit `:255-257`). Verification path: reconcile `knowledge-base/data-points/_registry.yaml`.
