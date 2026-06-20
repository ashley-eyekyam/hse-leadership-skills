---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-LOCATION: "classification is substance-intrinsic, not site-bound"
    ELI-EXPOSURE: "handled by chemical-exposure-register (METHODOLOGY cross-ref)"
    ELI-BASELINE: "an SDS is authored fresh — no standing controls to baseline"
  branches:
    - {when: Q2, option: mixture, activates_questions: [Q3], mandatory: true}
    - {when: Q5, option: acute tox, activates_questions: [Q6]}
    - {when: Q7, option: EU (CLP+REACH), activates_questions: [Q9]}
    - {when: Q7, option: India, activates_questions: [Q8], mandatory: true}
---

# Structured intake — ghs-classification-sds-author

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a hazard
class). Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — classify only, author a full 16-section SDS, produce a CLP label, or review/revise an existing SDS? | MCQ | classify-only / full SDS / label / review existing | ELI-SCOPE | always |
| Q2 | Substance or mixture? Name + CAS/EC. | MCQ + free-text | substance / mixture | ELI-SUBJECT | always |
| Q3 | Full composition: each hazardous component + concentration (and its own classification if known). | free-text | refuse "proprietary blend" without component data | ELI-SUBJECT | if Q2==mixture |
| Q4 | Intended use. | MCQ | manufacture / formulation / industrial / professional / consumer | ELI-INDUSTRY | always |
| Q5 | Which hazard data do you hold? (tick each available endpoint) | MCQ multi-select | physico-chem (flashpoint/oxidising/reactive) / acute tox / skin-eye / sensitisation / CMR / STOT / aspiration / aquatic-env | ELI-EVIDENCE | always |
| Q6 | For each ticked endpoint — study, read-across, or QSAR? | MCQ per endpoint | study / read-across / QSAR / none | ELI-EVIDENCE | per Q5 tick |
| Q7 | Jurisdiction / regime. | MCQ | EU (CLP+REACH) / UK (GB-CLP + UK-REACH) / US (OSHA HazCom) / India / other | ELI-JURIS | always |
| Q8 | Which Indian state? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — mandatory state detection; confirm before citing any form; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | if Q7==India |
| Q9 | REACH registration tonnage band (EU/UK). | MCQ | <1t / 1–10t / 10–100t / 100–1000t / >1000t / N/A | ELI-OBLIGATIONS | if Q7∈{EU,UK} |
| Q10 | Output scope. | MCQ | full 16-section SDS / classification-only / label | ELI-OUTPUT | always |
| Q11 | Author/owner and SDS review/revision date. | free-text | role-label + date | ELI-COMPETENCY / ELI-TEMPORAL | if Q1≠classify-only |
| Q12 | Org rating/priority scheme for residual data-gaps (drives `[GAP]` escalation order). | MCQ | org scheme / default — flag every untested endpoint | ELI-SCORING | always |

**Branch map**
- `Q5/Q6 endpoint == none` for a class → that hazard class is `[GAP]`, **not classified**, routed to testing/competent person — **the core refuse-on-missing-data rule** (METHODOLOGY step 2).
- `Q7 == EU` → activate CLP Annex VI harmonised-entry check + REACH §15 duties output section; Q9 tonnage.
- `Q7 == UK` → activate GB-CLP / UK-REACH divergence note.
- `Q7 == India` → Q8 state (**mandatory**), confirm before citing (activates `KB-REG-IN-STATEFORMS`); "Other"/"Unknown" → literal `[GAP]`.
- `Q2 == mixture` → Q3 component composition (mandatory) → activate bridging-principle / concentration-limit / M-factor logic.
- `output == full SDS` → activate §8 (HoC table via `controls`) + §14 cross-walk to `chemical-transport-safety`.

## Echo-back
> "**{substance/mixture}** ({CAS}); composition **{components/conc}**; use **{use}**; data held for **{ticked endpoints}**, missing for **{untested}**; regime **{juris(+state)}**{; tonnage {band}}; output **{scope}**. I will classify only the endpoints your data supports, flag the rest `[GAP]` for a competent person, render §8 controls HoC-first, and never invent a hazard class. Confirm."

Echo the captured facts back and **confirm before any classification begins**. Any
person/author identity is held as a role label in the echo-back.

## Refuse-on-vague anchors
- Q2/Q3 is the specificity anchor: "proprietary blend" without components → cannot classify a mixture; demand composition; **never proceed on a vague subject**.
- No data for an endpoint → `[GAP]`, never assign that class (METHODOLOGY: "No data → no class").
- "make me an SDS" with no hazard data → refuse, route to testing.

**Domain evidence types (`ELI-EVIDENCE`)**
Per-endpoint study reports, component SDSs + classifications, read-across/QSAR justifications, physico-chem data (flashpoint, BP, oxidising/self-reactive), Annex VI harmonised entry, REACH registration dossier, existing SDS to revise.

**[GAP]** Confirm the licensed GHS/CLP criteria text is available at runtime — the persona must not reconstruct binding criteria from memory; METHODOLOGY:10 routes to "the user's licensed GHS/CLP text" (SME audit `:84-86`). Verification path: confirm the runtime-supplied GHS/CLP source before classifying.
