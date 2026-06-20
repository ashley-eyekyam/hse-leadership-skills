---
sme-review:
  personas:
    - role: "COMAH / Seveso III major-hazard Safety Report author (CDOIF / process-safety lead)"
      expertise: "MAPP & SMS argument; establishment & environs description; major-accident scenario set; ALARP demonstration framing; internal emergency plan; KB-REG-UK-COMAH element completeness."
      lens: "Is the Safety Report argument complete against the six COMAH elements, and is the ALARP demonstration genuinely a demonstration — not an unevidenced assertion or an AI-invented QRA number?"
    - role: "Quantitative-risk-assessment (QRA) provenance reviewer"
      expertise: "Consequence/likelihood modelling provenance; ALARP cost-benefit framing; distinguishing fabricated from externally-supplied quantitative results."
      lens: "Is every quantitative figure traceable to an external, competent QRA — never computed or invented by the skill — and is an absent number an honest [GAP] rather than a guess?"
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

## Sign-off note
SME review: ran (personas: COMAH/Seveso major-hazard Safety Report author + QRA-provenance
reviewer); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class owned by the automated harness.
