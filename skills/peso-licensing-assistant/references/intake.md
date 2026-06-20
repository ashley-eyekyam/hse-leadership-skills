---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-LOCATION, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL, ELI-COMPETENCY]
  omits:
    ELI-SCORING: "licensing / compliance resolver, not a risk-ranking artefact — the MAH plan references scenarios it does not compute"
    ELI-BASELINE: "only on the MAH on-site-emergency-plan branch; not a general intake field"
    ELI-EXPOSURE: "only on the MAH on-site-emergency-plan branch; not pre-elicited"
  branches:
    - {when: Q4a, option: India, activates_questions: [Q5], mandatory: true, activates_kb_row: in-state-forms, activates_output_section: state-confirm-before-citing}
    - {when: Q3, activates_kb_row: in-peso, activates_output_section: osh-code-transition-note}
    - {when: Q4, option: Yes (MAH — on-site emergency plan in scope), activates_kb_row: in-msihc, activates_output_section: msihc-onsite-emergency-plan}
    - {when: Q1, option: Renewal or amendment, activates_questions: [Q7], activates_output_section: renewal-timeline}
    - {when: Q1, option: Compliance check, activates_questions: [Q7], activates_output_section: renewal-timeline}
---

# Structured intake — peso-licensing-assistant

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse to assume the state** and refuse a capacity-less installation. Canonical runtime
pattern: `KB-SNIP-INTAKE`.

This skill is **India statutory** (`jurisdiction: [IN]`): **state detection is mandatory**
wherever an obligation is state-specific — ask, or infer from the address and then
**confirm** before citing anything, never silently assume. Every form is cited **from the
matched KB row** (`KB-REG-IN-PESO` / `KB-REG-IN-STATEFORMS`), never a hard-coded national
number. Any unverified PESO form-id (e.g. Form E, Form F, LS-1A) stays literal **`[GAP]`**
with a verification path — never invented (GATE-06).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What's the **task**? | MCQ | New licence application / Renewal or amendment / Compliance check / MSIHC on-site emergency plan | ELI-SCOPE | always |
| Q2 | Name the **installation** and its **capacity**. | free-text | petroleum storage class / explosives / gas-cylinder filling / pressure vessel + quantity — the specificity anchor; refuse a capacity-less installation | ELI-SUBJECT | always |
| Q3 | Which **PESO instrument** applies? | MCQ | Petroleum Rules 2002 · Explosives Rules 2008 · Gas Cylinder Rules 2016 · SMPV(U) Rules 2016 · Not sure (help me resolve) | ELI-OBLIGATIONS | always |
| Q4 | Is the installation a **Major Accident Hazard** (MSIHC thresholds)? | MCQ | Yes (MAH — on-site emergency plan in scope) / No / Not sure (check thresholds) | ELI-JURIS | always |
| Q4a | Confirm the **jurisdiction** for this licensing artefact. | MCQ | India / Other (non-India — out of scope; PESO is the Indian statutory regulator) | ELI-JURIS | always |
| Q5 | **Which state** is the site in? *(mandatory — state detection)* | MCQ + free-text | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — or infer from the address then **confirm**; never silently assume the state before citing any state-specific form | ELI-LOCATION | always (mandatory where state-specific) |
| Q6 | What **documents** do you hold? | MCQ multi-select | Site/plot plan · Capacity / MAWP / design calcs · Existing licence · NOC (fire/pollution/local) · None yet | ELI-EVIDENCE | always |
| Q7 | What is the **current licence validity / renewal deadline** (if any)? | free-text | surfaces the temporal obligation | ELI-TEMPORAL | Q1 in [Renewal or amendment, Compliance check] |
| Q8 | Who is the **licensed competent person / point of contact** for the authority? | free-text | the competency anchor (de-identified to a role) | ELI-COMPETENCY | always |
| Q9 | What **output**, for whom, and what **sector** frames it? | MCQ + free-text | Full licence package · Form + checklist · MSIHC on-site emergency plan · Compliance gap report // M / C // sector (petroleum · explosives · industrial gases · chemicals) | ELI-OUTPUT | always |
| Q10 | Which **sector / installation type** frames the licence? | MCQ | Petroleum / fuel storage · Explosives · Industrial / compressed gases · Chemicals · Other | ELI-INDUSTRY | always |

**Branch map:** Q4a = India → **mandatory state branch**: activate Q5 (state detection), `in-state-forms` row, state-confirm-before-citing section — ask before citing any state-specific obligation; infer-from-address → confirm; never assume. Q3 selected → `in-peso` (resolve rule → form → authority); append the OSH-Code transition note always. Q4 = Yes (MAH) → msihc-onsite-emergency-plan; pull MSIHC scenario references (records, not computes). Q1 = Renewal or amendment or Compliance check → Q7 mandatory; renewal-timeline section. **Form-number discipline:** every form cited from the matched KB row; any unverified form-id (Form E / Form F / LS-1A) → literal **`[GAP]`** + verification path, never a hard-coded national number.

## Echo-back

Echo the captured facts back and ask the user to confirm before resolving anything:
"**{Task}** for **{installation}** ({capacity}) under **{instrument}** in **{state}**.
MAH: **{Yes/No}**. I'll cite the form from the matched KB row (no hard-coded number; an
unverified form stays `[GAP]`) and append the OSH-Code transition note. **Confirm the
state** before I resolve?"

## Refuse-on-vague anchors

- Q5 is the mandatory state anchor: a state-specific obligation with an unknown state →
  **ask, never assume**; confirm an inferred state before citing.
- Q2 is the specificity anchor: an installation with no capacity → refuse (capacity gates
  the licence class).
- Never use a national form number that is not resolved from a KB row; an unverified
  form-id stays `[GAP]`, never invented.
