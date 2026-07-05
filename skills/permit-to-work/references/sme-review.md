---
sme-review:
  personas:
    - role: "Control-of-work / permit-to-work authority (PTW issuing authority; LOTO & confined-space competent person)"
      expertise: "High-risk-task permits (hot work, confined-space entry, line-breaking, excavation, work-at-height); energy isolation (LOTO) & gas testing; SIMOPS coordination; permit validity & conditions."
      lens: "Are the isolations engineered (not permit-paper alone), and is every concurrent operation in the area actually coordinated rather than left as an uncontrolled clash?"
modes:
  permit-package:
    detected_by: "Q10 — What output, for whom? (Permit form / Permit + SIMOPS plan — the one permit-to-work package; the SIMOPS section is a leg of it, never a separate workflow)"
    floor:
      - id: type-specific-mandatory-controls
        description: "The type-specific mandatory controls for the named permit type(s) are present — hot work: fire watch + combustibles removed + extinguisher; confined space: gas test + attendant + rescue plan; excavation: buried-services scan + shoring; line break: drain/flush/depressurise + double isolation (intake Q1/Q4 gate); the gas test names WHICH gases — flammable (LEL) AND the stream's credible toxic/asphyxiant species AND oxygen where enrichment/depletion is possible — a flammable-only 'pass' is false assurance (19-02 canary fold-back)"
        anchors: ['fire watch', 'combustible', 'gas test|rescue plan|buried.services']
        min_matches: 2
      - id: isolations-engineered-loto
        description: "Energy isolations are physical/engineered — LOTO points listed and proven — never the permit paper (administrative) alone (intake Q3)"
        anchors: ['isolation', 'LOTO|lock.?out|locked and tagged']
        min_matches: 2
      - id: simops-clash-coordinated
        description: "Concurrent operations are detected and coordinated IN this permit — conflicting activities named + coordination controls (sequencing, exclusion zones, single coordination point, cross-permit refs) + the authorising authority; or SIMOPS explicitly ruled absent (intake Q5/Q6)"
        anchors: ['SIMOPS|simultaneous operations', 'exclusion zone|single point of coordination|cross.permit']
        min_matches: 2
      - id: permit-roles-authorities
        description: "The permit issuer, performing authority, gas tester and (confined space) rescue team are named as roles/authorities (intake Q7, de-identified)"
        anchors: ['permit issuer|issuing authority', 'performing authority']
        min_matches: 2
      - id: validity-conditions-handover
        description: "Permit conditions plus a bounded validity period and the shift-handover rule are stated — no open-ended permit (intake Q8); including the permit-holder-absence rule — work stops or an authorised deputy takes over, stated on the permit (19-02 canary fold-back)"
        anchors: ['validity', 'handover|single shift|24.?h']
        min_matches: 2
      - id: not-valid-until-confirmed
        description: "The permit is explicitly not valid until the isolations and (where present) the SIMOPS coordination controls are confirmed in place"
        anchors: ['not valid until|invalid until', 'confirmed in place|verified in place']
        min_matches: 1
      - id: controls-hoc-ranked
        description: "Every safeguard on the permit is hierarchy-of-controls ranked; a PPE/admin-only safeguard for a high-risk step carries a justification (KB-SNIP-HOC)"
        anchors: ['hierarchy of controls', 'engineered (control|isolation)|higher.order isolation']
        min_matches: 1
      - id: ptw-statutory-hook
        description: "The jurisdiction's control-of-work hook is cited — OSHA PSM hot-work element (k) / 1910.119 for a US covered process; the UK/EU/India frame per intake Q9"
        anchors: ['1910\.119|hot.work permit', 'PSM']
        min_matches: 1
---

# SME Review & Sign-off — permit-to-work

This skill carries **one** specialized SME lens: a control-of-work / PTW issuing authority.
It narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`)
to the control-of-work / PTW package with its in-skill SIMOPS coordination section; the
generic **HSE-SME-Reviewer** hook is the inherited fallback. The universal hard gates
(de-id leak, citation accuracy, HoC / no PPE-or-admin-only without justification,
owned-and-dated actions) are the enforced class and are not restated below.

**Isolations must be engineered, and SIMOPS must be coordinated.** The failure modes this
lens guards are an isolation relying on the permit (administrative) alone rather than a
physical LOTO/gas-test, and a detected concurrent operation left as an uncontrolled clash.
SIMOPS is handled as a coordination control *within this permit* — never deferred to a
non-existent standalone workflow — and each permit type carries its type-specific mandatory
controls (CS rescue plan, hot-work fire watch, excavation services-scan).

## Domain checklist (the nuanced things only this expert catches)
- [ ] Energy isolation (LOTO) and atmosphere control (gas test) are physical/engineered; an isolation relying on the permit (administrative) alone is flagged.
- [ ] Where concurrent operations exist, the SIMOPS section names the conflicting activities AND the coordination controls (sequencing, exclusion zones, single point of coordination, cross-permit refs) and the authorizing authority — no detected clash left uncoordinated.
- [ ] SIMOPS is a permit/coordination control within this permit — never deferred to a non-existent standalone workflow.
- [ ] The controls match the named high-risk task (hot-work fire watch + combustibles removed, confined-space gas test + attendant + rescue, excavation buried-services scan + shoring) — not a generic permit body.
- [ ] The permit is marked invalid until the isolations and (where SIMOPS exists) the coordination controls are confirmed in place.
- [ ] Permit conditions and a bounded validity period / shift-handover rule are stated; an open-ended permit is flagged (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A permit that describes the work but never gates it** — task, hazards and controls all
  listed, yet nothing states the permit is invalid until isolations are proven and
  coordination is in place; a checklist wearing a permit's clothes.
- **The invisible neighbour** — the crane lift, the running unit, the adjacent trade never
  appear; SIMOPS is the deadliest omission on a live plant because each permit is
  individually correct and the clash lives between them.
- **Paper isolation** — 'isolate at the panel' with no lock, no tag, no proving step; the
  isolation exists only as an instruction to be careful.
- **The permit that never ends** — no validity bound, no shift-handover rule, no
  re-validation trigger on conditions change (weather, gas re-test); the permit outlives
  the conditions it was written for.
- **The flammable-only gas test** *(19-02 canary fold-back)* — 'gas test: pass' scoped to
  LEL alone on a live unit; the toxic/asphyxiant species (an H2S IDLH sits orders of
  magnitude below its LEL) and oxygen enrichment go silently untested, so the permit's
  cleanest-looking control gives false assurance.
- **Technique-blind controls** *(19-02 canary fold-back)* — the canonical hot-work set
  (fire watch, combustibles, extinguisher) present while the technique's own hazards go
  unnamed: welding return-current path across flanged joints, in-service pipe wall
  thickness (UT) + WPS before the arc strikes, insulation smoulder beyond the fire-watch
  window, a numeric wind limit for elevated open-air work.
- **The permit with no emergency leg** *(19-02 canary fold-back)* — every control listed,
  yet no alarm response, assembly point, or control-room notification; the crew knows how
  to stop the work but not what to do when the plant does.
- **Closure that skips return-to-service** *(19-02 canary fold-back)* — the Area Authority
  signs off the worksite while nothing requires the inspection authority to release the
  work (post-weld inspection / NDE / leak test) before pressure is restored; the permit
  ends but the line's fitness was never gated.

## Sign-off note
SME review: ran (persona: Control-of-work / PTW issuing authority); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
