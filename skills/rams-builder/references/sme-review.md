---
sme-review:
  personas:
    - role: "Construction safety manager (CMIOSH / principal-contractor competent person)"
      expertise: "Safe systems of work, sequenced method statements, work-at-height & excavation rescue planning, plant/competency/permit integration, and bidirectional RA↔MS cross-referencing."
      lens: "Is this a REAL safe system of work — sequenced, every method step coupled to the RA, rescue arrangements activity-specific — not stapled paperwork dressed up as a RAMS?"
    - role: "CDM 2015 / BOCW duty-holder compliance adviser"
      expertise: "CDM 2015 Reg 13 (principal contractor) / Reg 15 (contractor) duties + the Construction Phase Plan; India BOCW + state form + the OSH-Code transition; competency-card schemes (CSCS/CPCS/IPAF/PASMA)."
      lens: "Is the right construction-law duty cited for the stated role, the India state resolved before any form is named, and are the named competencies exactly the ones the user actually supplied — never invented?"
modes:
  rams:
    detected_by: "Q-S — Sequence of works (the ordered steps set-up to clear-down; the method-statement spine). Q6 sets the CDM/contractor role and Q5 the matrix; the floor applies to every RAMS."
    floor:
      - id: ra-ms-cross-reference
        description: "The risk assessment and method statement cross-reference bidirectionally — every method step's residual hazards trace to RA rows and every RA hazard is addressed by a step (an orphan either way is the load-bearing miss)"
        anchors: ['method statement', 'risk assessment']
        min_matches: 2
      - id: sequenced-method
        description: "The method statement is genuinely sequenced set-up -> clear-down (intake Q-S) — an unsequenced 'method' is a miss"
        anchors: ['sequence|mobilise', 'step']
        min_matches: 1
      - id: rescue-activity-specific
        description: "Rescue / emergency arrangements are activity-specific (work at height / confined space / excavation) — a generic 'call 999' where a rescue plan is required is a miss"
        anchors: ['rescue', 'emergency']
        min_matches: 2
      - id: hoc-no-ppe-substitute
        description: "Higher-order controls are used where the hazard demands them — PPE + a briefing is never substituted for edge protection / a MEWP / an exclusion zone (intake Q-P)"
        anchors: ['exclusion zone', 'edge protection|mewp|hierarchy of controls', 'residual']
        min_matches: 2
      - id: cdm-role-duty-cited
        description: "The right construction-law duty is cited for the stated role — principal contractor (CDM 2015 Reg 13) vs contractor (Reg 15) vs principal designer; India maps to the BOCW principal-employer/contractor duty (intake Q6)"
        anchors: ['cdm', 'reg 1[35]|principal contractor']
        min_matches: 2
      - id: competencies-as-supplied
        description: "Named competencies appear exactly as the user supplied them (PASMA / IPAF / appointed person), never invented; an unstated card is [GAP] and the briefing table ships with empty signature rows (intake Q-C)"
        anchors: ['pasma|ipaf|competen', 'sign.off|signature']
        min_matches: 2
      - id: per-activity-risk-scored
        description: "Each activity carries an initial and a residual risk score on the org matrix — an un-scored or un-rescored activity is a miss"
        anchors: ['residual']
        min_matches: 1
---

# SME Review & Sign-off — rams-builder

Two distinct professions own two distinct failure modes here — construction-safety / safe-
system-of-work *craft* versus CDM/BOCW *duty compliance* — a construction safety manager
versus a CDM coordinator/compliance adviser. So this skill carries **two** SME lenses, both
specializing the generic **HSE-SME-Reviewer** runtime hook (`KB-SNIP-ARCHETYPES`). The
universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated
actions) are the enforced class and are not restated below.

Note the de-id-vs-named-competent-persons exception: user-supplied competent persons named
for sign-off (Q-C) stay named; evidence names scrub. The briefing/sign-off table still ships
with empty signature rows.

## Domain checklist (the nuanced things only this expert catches)
- [ ] RA↔MS cross-reference is bidirectional and complete — every method step's residual hazards trace to RA rows, AND every RA hazard is addressed by a step; an orphan either way is the load-bearing FLAG.
- [ ] The method statement is genuinely sequenced (set-up → clear-down) — an unsequenced "method" is a FLAG.
- [ ] Rescue/emergency arrangements are activity-specific — a generic "call 999" where a rescue plan is required (work at height, confined space, excavation) is a FLAG.
- [ ] Construction's classic under-control is caught — "PPE + a safe-working briefing" substituted for edge protection / a MEWP / an exclusion zone is a FLAG.
- [ ] The right CDM / role duty is cited — principal contractor (Reg 13) vs contractor (Reg 15) vs principal designer changes the duty; a mismatch is a FLAG.
- [ ] Competencies appear exactly as supplied, never invented — named competent persons stay named for sign-off (the §3.8 exception), but the briefing table ships with empty signature rows; an invented card/ticket → `[GAP]`.
- [ ] India: the state is resolved before any form; BOCW is legacy-first — never a hard-coded national form number; an un-seeded state → `[GAP]`.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The missing rescue leg** (canary S1) — a work-at-height / confined-space / excavation
  RAMS with a full method and controls but a generic "call the emergency services" where an
  activity-specific rescue plan (recovery from a MEWP, suspended-access rescue, trench
  extraction) is required.
- **The two legs that never meet** (canary S7) — an RA and a method statement both present
  but not cross-referenced: a method step with residual hazards absent from the RA, or an RA
  hazard no step controls. Stapled paperwork dressed as a safe system of work.
- **The regime named, its element set unswept** (canary S6) — CDM 2015 (or BOCW) cited but
  the duty-holder's actual obligations (the CPP linkage, the Reg-specific duty for the stated
  role, notification) silently absent.
- **Public / third-party protection assumed** — an occupied building or public footpath in
  the environment but no exclusion zone, no falling-object protection, no traffic/pedestrian
  separation derived for the third party.
- **Invented competence** — a card or ticket (PASMA/IPAF/appointed person) asserted that the
  user never supplied, instead of a `[GAP]` routed to the competent person.

## Sign-off note
SME review: ran (personas: Construction safety manager + CDM/BOCW compliance adviser); this
is **decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
