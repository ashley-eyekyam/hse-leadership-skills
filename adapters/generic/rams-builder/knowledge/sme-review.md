---
sme-review:
  personas:
    - role: "Construction safety manager (CMIOSH / principal-contractor competent person)"
      expertise: "Safe systems of work, sequenced method statements, work-at-height & excavation rescue planning, plant/competency/permit integration, and bidirectional RA↔MS cross-referencing."
      lens: "Is this a REAL safe system of work — sequenced, every method step coupled to the RA, rescue arrangements activity-specific — not stapled paperwork dressed up as a RAMS?"
    - role: "CDM 2015 / BOCW duty-holder compliance adviser"
      expertise: "CDM 2015 Reg 13 (principal contractor) / Reg 15 (contractor) duties + the Construction Phase Plan; India BOCW + state form + the OSH-Code transition; competency-card schemes (CSCS/CPCS/IPAF/PASMA)."
      lens: "Is the right construction-law duty cited for the stated role, the India state resolved before any form is named, and are the named competencies exactly the ones the user actually supplied — never invented?"
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

## Sign-off note
SME review: ran (personas: Construction safety manager + CDM/BOCW compliance adviser); this
is **decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
