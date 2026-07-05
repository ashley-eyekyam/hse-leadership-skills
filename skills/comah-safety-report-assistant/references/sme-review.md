---
sme-review:
  personas:
    - role: "COMAH / Seveso III major-hazard Safety Report author (CDOIF / process-safety lead)"
      expertise: "MAPP & SMS argument; establishment & environs description; major-accident scenario set; ALARP demonstration framing; internal emergency plan; KB-REG-UK-COMAH element completeness."
      lens: "Is the Safety Report argument complete against the six COMAH elements, and is the ALARP demonstration genuinely a demonstration — not an unevidenced assertion or an AI-invented QRA number?"
    - role: "Quantitative-risk-assessment (QRA) provenance reviewer"
      expertise: "Consequence/likelihood modelling provenance; ALARP cost-benefit framing; distinguishing fabricated from externally-supplied quantitative results."
      lens: "Is every quantitative figure traceable to an external, competent QRA — never computed or invented by the skill — and is an absent number an honest [GAP] rather than a guess?"
modes:
  safety-report:
    detected_by: "Q5 — Confirm the tier (Upper-tier (full Safety Report) → the six-element report leg; Q6 selects the elements to assemble)"
    floor:
      - id: tier-determination-stated
        description: "The lower/upper-tier determination is stated from the named dangerous substances and quantities against the COMAH thresholds (intake Q4/Q5; KB-REG-UK-COMAH threshold gate)"
        anchors: ['upper.tier', 'threshold', 'dangerous substance']
        min_matches: 2
      - id: six-element-coverage
        description: "All six COMAH Safety-Report elements present or explicitly [GAP]'d — MAPP · SMS description · establishment & environs · major-accident-scenario identification · ALARP demonstration · internal emergency plan (KB-REG-UK-COMAH element map)"
        anchors: ['MAPP', 'internal emergency plan', 'establishment']
        min_matches: 2
      - id: alarp-demonstration-not-assertion
        description: "ALARP is a demonstration — risk reduced ALARP via the measures actually taken, with the argument shown; a bare 'risks are ALARP' assertion fails"
        anchors: ['ALARP', 'demonstrat']
        min_matches: 2
      - id: qra-external-provenance
        description: "Every quantitative figure (QRA result, consequence distance, cost-benefit) is recorded as externally produced by a named competent provider (as a role); an absent number is a literal [GAP], never computed"
        anchors: ['QRA', 'consequence model', 'externally']
        min_matches: 1
      - id: scenarios-establishment-specific
        description: "The major-accident scenarios trace to THIS establishment's substances, units and PHA inputs — not a generic substance-class list"
        anchors: ['major.accident scenario', 'loss of containment|release|BLEVE|fire|explosion']
        min_matches: 2
      - id: environs-receptors-named
        description: "The establishment & environs description names the receptors in range — population, environment/watercourses, neighbouring establishments (intake Q7/Q13)"
        anchors: ['receptor', 'neighbouring', 'population']
        min_matches: 2
      - id: emergency-plan-scenario-linked
        description: "The internal emergency plan responds to the identified major-accident scenarios for this site (alarm, muster, escalation, liaison) — not boilerplate"
        anchors: ['emergency', 'muster|alarm|escalation']
        min_matches: 2
  mapp:
    detected_by: "Q5 — Confirm the tier (Lower-tier (MAPP only) → the mapp-only leg; Q1 'MAPP only' selects it directly)"
    floor:
      - id: mapp-policy-commitments
        description: "The Major Accident Prevention Policy states the duty-holder's prevention commitments proportionate to its major-accident hazards"
        anchors: ['major.accident prevention policy', 'MAPP']
        min_matches: 1
      - id: mapp-sms-delivery
        description: "The MAPP describes the safety-management arrangements that deliver each policy commitment — no commitment left unsupported"
        anchors: ['safety management system', 'SMS']
        min_matches: 1
      - id: mapp-tier-basis
        description: "The lower-tier determination (named substances/quantities against the thresholds) is recorded as the MAPP's basis"
        anchors: ['lower.tier', 'threshold']
        min_matches: 1
      - id: mapp-review-trigger
        description: "The MAPP records its review/revision trigger (material change / periodic review) and the accountable role"
        anchors: ['(review|revis).{0,50}(MAPP|policy|report)', 'material change']
        min_matches: 1
---

# SME Review & Sign-off — comah-safety-report-assistant

Two distinct competencies own two failure modes on a Safety Report: the **argument's
completeness against the COMAH elements** (the major-hazard report author) and the
**provenance of every quantitative figure** (the QRA reviewer). So this skill carries
**two** SME lenses. Both specialize the family's single **Process-Safety Engineer**
archetype (`KB-SNIP-ARCHETYPES`), narrowed here to the COMAH/Seveso Safety Report —
the first lens carries the slot's element-completeness remit, the second carries its
"team-recorded, not autonomous AI judgement" check applied to the externally-done
QRA/consequence modelling. The generic **HSE-SME-Reviewer** hook is the inherited
fallback. The universal hard gates (de-id leak, citation/clause accuracy, HoC / no
PPE-or-admin-only without justification, every action owned-and-dated) are the enforced
class and are deliberately not restated below.

**The six COMAH elements are CONFIRMED in the KB.** `KB-REG-UK-COMAH`
(`knowledge-base/regulatory/uk-comah.md`) enumerates them as a duty→element map:
**MAPP**, **Safety Management System (SMS) description**, **establishment & environs
description**, **major-accident-scenario identification**, **ALARP demonstration**, and
the **internal (on-site) emergency plan** (with the lower/upper-tier determination
gating which apply). The checklist below leans on that confirmed enumeration; a missing
element is recorded as `[GAP]`, never invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] All six COMAH elements present and credited from `KB-REG-UK-COMAH` — MAPP · SMS description · establishment & environs description · major-accident-scenario identification · ALARP demonstration · internal emergency plan — each populated or explicitly `[GAP]`'d; the lower/upper-tier determination is stated so the right element set applies (lower-tier = MAPP only).
- [ ] ALARP is a demonstration, not an assertion: the framing shows risk reduced to ALARP via the measures actually taken; "risks are ALARP" with no supporting argument is flagged.
- [ ] Every quantitative result (QRA, consequence distance, ALARP cost-benefit figure) is recorded as externally produced by a competent person — none computed or invented by the skill; an absent number reads `[GAP]`, never a fabricated value.
- [ ] The major-accident scenarios trace to the PHA inputs (HAZID/HAZOP) for this establishment — not a generic substance-class list.
- [ ] The SMS description actually delivers the policy commitments made in the MAPP — no MAPP policy claim left unsupported by a corresponding SMS element.
- [ ] The internal emergency plan responds to the identified major-accident scenarios for this site, not boilerplate — and the whole report reads as duty-holder-supplied, structured work, not an autonomously authored Safety Report (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A structured report with an asserted ALARP** — every element heading present, prose
  polished, but the ALARP section asserts "risks are as low as reasonably practicable"
  with no measures-taken argument and no gross-disproportion reasoning. The report's
  centre of gravity is hollow. Read the ALARP section as a demonstration first.
- **Quantitative figures with no provenance** — consequence distances or frequencies that
  appear authoritative but name no external QRA provider, no study reference, no date;
  indistinguishable from invented numbers to a regulator.
- **Environs without receptors** — a site description (boundary, access, layout) standing
  in for the environs element while the population, watercourses and neighbouring
  establishments in range are never named.
- **MAPP↔SMS disconnect** — policy commitments in the MAPP with no corresponding SMS
  arrangement delivering them (and vice-versa); each element reads fine alone, the
  argument between them is missing.

## Sign-off note
SME review: ran (personas: COMAH/Seveso major-hazard Safety Report author + QRA-provenance
reviewer); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class owned by the automated harness.
