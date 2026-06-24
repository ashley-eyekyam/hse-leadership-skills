---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "risk is external QRA, recorded not computed — the skill does not run a matrix or compute MAH frequencies"
    ELI-BASELINE: "folded into the SEMS / CMAPP / SCE measures the duty-holder supplies, not pre-elicited"
  branches:
    - {when: Q3, option: EU Offshore Safety Directive, activates_questions: [Q3a], activates_kb_row: eu-osh, activates_output_section: member-state-transposition}
    - {when: Q5, option: Help determine the safety-case element set, activates_output_section: element-determination}
    - {when: Q6, option: SCE verification scheme, activates_questions: [Q7], mandatory: true}
---

# Structured intake — offshore-safety-case

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where
it is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague installation** and record `[GAP]` for any unsupplied element, figure,
or barrier-effectiveness claim, never inventing it. Canonical runtime pattern:
`KB-SNIP-INTAKE`.

This skill **structures** the Offshore Safety Case argument and **records** the
duty-holder's content for each SI 2015/398 Schedule 6/7 element of `KB-REG-OFFSHORE-SCR`;
the safety-case elements it assembles are the ones that fragment enumerates — **MAH
identification · SEMS · CMAPP (major-accident-prevention policy) · ALARP demonstration ·
the SCE register + performance standards + the independent verification scheme · emergency
response (the EER element)** — so the intake elicits the inputs for each (it does not
re-enumerate the element set from scratch). **QRA / consequence-modelling / ALARP figures
and any barrier/SCE-effectiveness claim are external** (the skill records, never computes
or asserts); an unsupplied element or figure is `[GAP]`, never invented. **SI 2015/398 is
the current regime; SCR 2005 is named only as the superseded legacy reference.**

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need? | MCQ | Full safety-case argument structure · A single safety-case element · Review/revision of an existing safety case | ELI-SCOPE | always |
| Q2 | Name the **installation**. | free-text | the specific named installation (not "our assets") — the specificity anchor; refuse a vague answer | ELI-SUBJECT | always |
| Q3 | Which **regime**? | MCQ | UK SCR 2015 (SI 2015/398) / EU Offshore Safety Directive | ELI-JURIS | always |
| Q3a | *(EU only)* Which **member state** transposes the Offshore Safety Directive? | free-text | the member-state transposition the safety case must satisfy | ELI-JURIS | Q3 == EU Offshore Safety Directive |
| Q4 | What **installation type** frames the safety case? | MCQ | Fixed production platform · Mobile drilling rig (MODU) · FPSO / floating production · Support / accommodation installation · Other | ELI-INDUSTRY | always |
| Q5 | Which **safety-case elements** to assemble? | MCQ multi-select | MAH identification / SEMS / CMAPP / ALARP demonstration / SCE register + performance standards / Independent verification scheme / Emergency response (EER) / Help determine the safety-case element set | ELI-OBLIGATIONS | always |
| Q6 | What is the **SCE / barrier basis**? | MCQ | SCE register supplied (with performance standards) / SCE verification scheme / Barriers cited but no performance standard yet (→ `[GAP]`) | ELI-EVIDENCE | always |
| Q7 | *(verification scheme)* Who is the **independent verifier** and what are the **verifier findings**? | free-text | the independent verification body + its findings; unsupplied → `[GAP]` | ELI-COMPETENCY | Q6 == SCE verification scheme |
| Q8 | Where do the **QRA / consequence-modelling / ALARP numbers** come from? | free-text | external; the skill records with provenance, never computes; unsupplied → `[GAP]` | ELI-EVIDENCE | always |
| Q9 | What **major-accident hazards & receptors** apply (hydrocarbon release, fire & explosion, structural, environmental; the environs / sensitive receptors)? | free-text | the MAH set + receptors for the MAH-identification element; from the duty-holder's PHA/HAZID, not a generic substance-class list | ELI-EXPOSURE | always |
| Q10 | Confirm the **installation's physical setting / field & water depth** for the establishment description. | free-text | field, water depth, neighbouring installations, pipeline/host ties, ERRV coverage | ELI-LOCATION | always |
| Q11 | Who is the **duty-holder / operator / safety-case author / QRA provider**? | free-text | the assistive-evidence anchor (de-identified to roles) | ELI-COMPETENCY | always |
| Q12 | Is there a **submission deadline or revision trigger** (material change, thorough review, end-of-life)? | free-text | the temporal obligation | ELI-TEMPORAL | always |
| Q13 | What **output**, for whom (competent-authority submission vs internal draft)? | MCQ + free-text | Full safety case · Element · Argument-map extract // competent authority vs internal // M / C | ELI-OUTPUT | always |

**Branch map:** Q3 = EU Offshore Safety Directive → ask the member state (Q3a); `eu-osh`
row + member-state-transposition note; UK → `KB-REG-OFFSHORE-SCR` (SI 2015/398). Q5 = Help
determine the element set → element-determination section (resolve against the SI 2015/398
Schedule 6/7 element set in `KB-REG-OFFSHORE-SCR`). Q6 = SCE verification scheme → elicit
the verifier + findings (Q7) mandatory. Any element/figure/barrier-effectiveness claim
unsupplied (especially ALARP / QRA / an SCE performance standard) → `[GAP]`, never invented;
no barrier/SCE is asserted effective without a cited performance-standard evidence reference
(mandatory). The EER element is **cross-referenced** to the sibling MAR-03
`marine-emergency-response` plan, never rebuilt here. For India offshore work, state
detection is mandatory before any shore-base statutory cite, which defers to `hse-india`
(CONV-8) — no national form is minted.

## Echo-back

Echo the captured facts back and ask the user to confirm before any assembly begins:
"Installation **{installation}** ({installation type}) under **{regime}**. Elements:
**{elements}**. SCE/barrier basis: **{sce basis}**. QRA/ALARP source: **{source}**
(external — I record with provenance, never compute). MAH set: **{mah}**. Author
**{author}**, deadline **{deadline}**. Unsupplied elements/figures/barrier claims →
`[GAP]`. The EER element is cross-referenced to the marine-emergency-response plan, not
rebuilt. Correct before I assemble?"

## Refuse-on-vague anchors

- Q2 is the specificity anchor: **refuse a vague installation** ("our assets", "the
  field"); never proceed without a single named installation.
- Refuse to assemble an ALARP demonstration with no external numbers → record `[GAP]`,
  never invent a scenario, QRA result, consequence distance, or ALARP figure.
- Refuse to assert any barrier / SCE effective without a cited performance-standard
  evidence reference → record `[GAP]`.
- Never emit "accepted / approved / authorised" — acceptance is the competent authority's
  act; this output is the structured argument that PRECEDES it.
