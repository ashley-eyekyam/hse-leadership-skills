---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "risk is external QRA, recorded not computed — the skill does not run a matrix"
    ELI-BASELINE: "folded into the SMS / measures the duty-holder supplies, not pre-elicited"
  branches:
    - {when: Q3, option: EU Seveso III, activates_questions: [Q3a], activates_kb_row: eu-osh, activates_output_section: member-state-transposition}
    - {when: Q5, option: Lower-tier (MAPP only), activates_output_section: mapp-only}
    - {when: Q5, option: Upper-tier (full Safety Report), activates_questions: [Q6, Q7], mandatory: true}
    - {when: Q10, activates_output_section: review-revision-basis}
---

# Structured intake — comah-safety-report-assistant

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where
it is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague establishment** and record `[GAP]` for any unsupplied element, never
inventing it. Canonical runtime pattern: `KB-SNIP-INTAKE`.

This skill **structures** the COMAH / Seveso III Safety Report argument and **records**
the duty-holder's content for each element of `KB-REG-UK-COMAH`; the six Safety-Report
elements it assembles are the ones that fragment enumerates — **MAPP · SMS · establishment
& environs description · major-accident-scenario identification · ALARP demonstration ·
internal emergency plan** — so the intake elicits the inputs for each (it does not
re-enumerate the element set from scratch). QRA / consequence-modelling / ALARP figures
are **external** (the skill records, never computes); an unsupplied element or figure is
`[GAP]`, never invented.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need? | MCQ | Full Safety Report structure · MAPP only (lower-tier) · A single element/section · Review/revision of an existing report | ELI-SCOPE | always |
| Q2 | Name the **establishment**. | free-text | the specific named site (not "our sites") — the specificity anchor; refuse a vague answer | ELI-SUBJECT | always |
| Q3 | Which **regime**? | MCQ | UK COMAH 2015 / EU Seveso III | ELI-JURIS | always |
| Q3a | *(EU Seveso III only)* Which **member state** transposes it? | free-text | the member-state transposition the report must satisfy | ELI-JURIS | Q3 == EU Seveso III |
| Q4 | What **dangerous substances** are present and in what **quantities** (tier determination)? | free-text | named substances + quantities drive lower-tier vs upper-tier | ELI-OBLIGATIONS | always |
| Q5 | Confirm the **tier**. | MCQ | Lower-tier (MAPP only) / Upper-tier (full Safety Report) / Help determine from Q4 | ELI-SCOPE | always |
| Q6 | Which **Safety-Report elements** to assemble? | MCQ multi-select | MAPP · SMS · Establishment & environs description · Major-accident-scenario identification · ALARP demonstration · Internal emergency plan | ELI-OBLIGATIONS | Q5 == Upper-tier (full Safety Report) |
| Q7 | What **receptors** are in the environs (population, environment, neighbouring establishments)? | free-text | for the establishment & environs description | ELI-EXPOSURE | Q5 == Upper-tier (full Safety Report) |
| Q8 | Where do the **QRA / consequence-modelling / ALARP numbers** come from? | free-text | external; the skill records, never computes; unsupplied → `[GAP]` | ELI-EVIDENCE | always |
| Q9 | Who is the **duty-holder / competent author / QRA provider**? | free-text | the assistive-evidence anchor (de-identified to roles) | ELI-COMPETENCY | always |
| Q10 | Is there a **submission deadline or review/revision trigger** (5-yearly, material change)? | free-text | the temporal obligation | ELI-TEMPORAL | always |
| Q11 | What **output**, for whom (regulator submission vs internal draft), and what **sector** frames it? | MCQ + free-text | Full report · Element · MAPP // regulator vs internal // M / C // sector (chemicals · O&G · storage · other) | ELI-OUTPUT | always |
| Q12 | Which **sector / installation type** frames the establishment? | MCQ | Chemicals · Oil & Gas · Bulk storage · Explosives · Other | ELI-INDUSTRY | always |
| Q13 | Confirm the **establishment's physical setting / surroundings** for the environs description. | free-text | site boundary, neighbouring land use, watercourses, populated areas | ELI-LOCATION | always |

**Branch map:** Q3 = EU Seveso III → ask the member state (Q3a); `eu-osh` row + member-state-transposition note; UK → `uk-comah`. Q5 = Lower-tier → MAPP only (mapp-only section); skip Q6/Q7. Q5 = Upper-tier → full element set (Q6) + environs receptors (Q7) mandatory. Q8 any element unsupplied (especially ALARP / QRA) → `[GAP]`, never invented (mandatory). Q10 review trigger → review-revision-basis section. The six assembled elements are credited from `KB-REG-UK-COMAH`, not re-derived.

## Echo-back

Echo the captured facts back and ask the user to confirm before any assembly begins:
"Establishment **{establishment}** under **{regime}**, **{tier}** based on substances
**{substances/quantities}**. Elements: **{elements}**. QRA/ALARP source: **{source}**
(external — I record, never compute). Author **{author}**, deadline **{deadline}**.
Unsupplied elements → `[GAP]`. Correct before I assemble?"

## Refuse-on-vague anchors

- Q2 is the specificity anchor: **refuse a vague establishment** ("our sites", "the
  business"); never proceed without a single named establishment.
- Refuse to assemble an ALARP demonstration with no external numbers → record `[GAP]`,
  never invent a scenario, QRA result, or ALARP figure.
