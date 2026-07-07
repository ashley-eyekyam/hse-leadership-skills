---
sme-review:
  personas:
    - role: "Industrial toxicologist / GHS-CLP classification SME"
      expertise: "GHS hazard-class structure + EU CLP (incl. Annex VI harmonised entries), bridging principles, cut-off/concentration limits, the 16-section SDS contract"
      lens: "is every assigned class logically forced by the STATED data — and is every absent datum honestly [GAP], never back-filled"
    - role: "Regulatory-affairs / SDS-format specialist"
      expertise: "jurisdictional SDS format + duties — EU REACH (e)SDS + exposure scenarios §15, UK COSHH, US HazCom 29 CFR 1910.1200"
      lens: "does the SDS section set + label match the RESOLVED jurisdiction, not a blurred generic"
modes:
  sds-authoring:
    detected_by: "Q1 — Output scope (author a full 16-section SDS / classify / produce a CLP label / review an existing SDS)"
    floor:
      - id: ghs-all-classes-assessed
        description: "Every applicable hazard class is assessed (physical AND health AND environmental); a class silently skipped rather than [GAP]-marked / recorded NOT classified is a FLAG (KB-STD-GHS)"
        anchors: ['physical hazards?', 'not classified']
        min_matches: 1
      - id: ghs-class-category-consistent
        description: "Class / category / H-statement / pictogram / signal word are mutually consistent; a class/category/H-statement invented on absent data is hard-gate-adjacent (KB-REG-EU-CLP)"
        anchors: ['H31[0-9]', 'pictogram', 'signal word']
        min_matches: 1
      - id: ghs-mixture-method-stated
        description: "The mixture classification method is stated (calculation/summation vs bridging vs test) with the cut-off / concentration limits actually applied — an undocumented method is a FLAG"
        anchors: ['summation', 'calculation', 'concentration limit']
        min_matches: 1
      - id: ghs-clp-annex-vi-checked
        description: "The EU CLP Annex VI harmonised entry is checked where one exists — a self-classification contradicting a harmonised entry is a FLAG (KB-REG-EU-CLP)"
        anchors: ['annex vi', 'harmonised (entry|classification)']
        min_matches: 1
      - id: ghs-section8-hoc-first
        description: "Section 8 exposure controls are HoC-ranked — engineering/LEV/containment ahead of RPE/PPE; a PPE/RPE-first Section 8 is hard-gate-adjacent (HoC) unless justified-or-escalated; any OEL carries source+year (KB-SNIP-HOC)"
        anchors: ['hierarchy.of.controls', 'exposure controls']
        min_matches: 1
      - id: ghs-section14-handed-off
        description: "Section 14 transport is NOT authored here — the transport class/UN/PG cross-walk is handed to chemical-transport-safety; a transport classification invented in-skill is a FLAG"
        anchors: ['handed.off', 'not authored here']
        min_matches: 1
      - id: ghs-draft-not-authoritative
        description: "The output is framed as a decision-support DRAFT, never an authoritative regulatory SDS — a draft presented as the final compliant SDS is a FLAG"
        anchors: ['decision.support draft', 'authoritative']
        min_matches: 1
---

# SME Review & Sign-off — ghs-classification-sds-author

This skill carries the chemicals family's **only** justified 2nd lens (D-06; max 2):
classification competence and jurisdictional SDS-format competence are two distinct
expertises — an industrial toxicologist who forces every hazard class from the stated data,
and a regulatory-affairs specialist who matches the SDS section-set and label to the resolved
jurisdiction. Both **narrow** the Chemical-Process-Safety sector slot that extends the generic
**HSE-SME-Reviewer** hook (`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak,
citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are
not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every applicable hazard class assessed — physical *and* health *and* environmental classes considered; a class silently skipped (not `[GAP]`-marked) is a FLAG.
- [ ] Class ⇄ category ⇄ H-statement ⇄ pictogram ⇄ signal word mutually consistent — e.g. "Danger" with only Category-2 hazards, or a pictogram absent for an assigned class, is a FLAG. A class/category/H-statement invented on absent data is **hard-gate-adjacent** (escalate).
- [ ] Mixture classification method stated — calculation/summation vs bridging vs test data, with the cut-off / concentration limits actually applied; an undocumented method is a FLAG.
- [ ] EU CLP Annex VI harmonised entry checked where one exists — a self-classification contradicting a harmonised entry is a FLAG.
- [ ] §8 exposure controls HoC-ranked — engineering/LEV/containment ahead of RPE/PPE; a PPE/RPE-first §8 is **hard-gate-adjacent** (HoC) unless justified-or-escalated. Any OEL/WEL/PEL in §8 carries source + year (SEG depth deferred to `chemical-exposure-register`).
- [ ] §14 transport **not authored here** — the transport class/UN/packing-group cross-walk is handed to `chemical-transport-safety`; a transport classification invented in-skill is a FLAG.
- [ ] Output framed as a decision-support draft, **never** an authoritative regulatory SDS — a draft presented as the final compliant SDS is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The regime named, its element set unswept (canary S6)** — CLP/REACH cited while the full 16
  SDS sections, the classification method, and the Annex VI / REACH §15 duty set are not actually
  swept; a partial SDS presented as complete.
- **The class asserted with no data basis (canary S5)** — a hazard class/category stated without
  the study/read-across/QSAR basis or the concentration-limit calculation; every untested endpoint
  must be a literal [GAP], never back-filled.
- **The scope overclaim (canary S7)** — a decision-support draft presented as an authoritative
  placed-on-the-market SDS, or a §14 transport classification invented in-skill rather than handed
  to chemical-transport-safety.
- **The Section 8 that leads with PPE (assistive completeness)** — engineering/LEV/containment
  controls omitted so RPE/PPE becomes the §8 headline, with OELs stated without source+year.
- **The cited value with no vintage (19-08 audit, S9 currency)** — an OEL, a harmonised Annex VI
  entry, or a downstream notification duty (UFI / poison-centre / registration number) carried
  without confirming it is the current requirement, or silently omitted from the 16-section set.

## Sign-off note
SME review: ran (personas: Industrial toxicologist / GHS-CLP classification SME + Regulatory-
affairs / SDS-format specialist); this is **decision-support only**. It **precedes — and never
replaces, never emits — the human competent-person sign-off**, and it never outputs "approved
by a competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
