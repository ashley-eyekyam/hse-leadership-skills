---
sme-review:
  personas:
    - role: "CDM Principal Designer (chartered, pre-construction-information competent person)"
      expertise: "CDM 2015 Reg 4 pre-construction information; the L153 Appendix-1 PCI content checklist; existing-structure hazard information (asbestos/ACMs, buried & overhead services, ground conditions, structural form, the existing H&S file); brownfield / occupied-building survey practice; the PCI → CPP → H&S File document chain."
      lens: "Is this REAL pre-construction information a designer/contractor could rely on — every existing-structure hazard source-cited, and is EVERY missing source a documented [GAP] with an owner + date, never silently omitted — not a thin checklist that hides what isn't known?"
    - role: "CDM Client Adviser / duty-holder compliance adviser"
      expertise: "The CDM 2015 Reg 4 CLIENT duty — provide the PCI as soon as practicable to everyone appointed or being considered (Reg 4(4)); Reg 4(5)/(6) no construction start without arrangements/CPP; the timing and circulation obligations; India BOCW pre-work site information via hse-india + state form + the OSH-Code transition."
      lens: "Is the client's Reg 4 duty AND its timing stated, is the pack issued (restricted-distribution) to the right parties, and for India is the state resolved before any form is named — never a minted national form number?"
---

# SME Review & Sign-off — pre-construction-information

Two distinct professions own two distinct failure modes here — the **PCI craft** (is the
existing-structure hazard information real, source-cited, and gap-disciplined?) versus the
**CDM Reg 4 client-duty compliance** (is the client duty + timing + circulation right?) — a
CDM principal designer versus a CDM client adviser. So this skill carries **two** SME lenses,
both specializing the generic **HSE-SME-Reviewer** runtime hook (`KB-SNIP-ARCHETYPES`). The
universal hard gates (de-id leak, citation accuracy, owned-and-dated actions) are the
enforced class and are not restated below.

Note the de-id-vs-named-owners exception: user-supplied gap-action owners and client/principal-
designer duty-holders named for the record stay named; survey-occupier names and health detail
scrub to role labels.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Gap discipline holds** — EVERY existing-structure source the user does not have is a documented `[GAP]` with a named owner + ISO due date; a silently-omitted missing source (e.g. a dropped asbestos survey) is the load-bearing FLAG.
- [ ] **Asbestos status is explicit** — present-and-surveyed, presumed-pending-survey, or `[GAP]` (survey outstanding, owner + date) — never silently absent on a refurbishment/demolition.
- [ ] **Buried & overhead services are addressed** — their presence/location or a documented `[GAP]`; a PCI silent on services is a FLAG.
- [ ] **The existing-structure hazard information is source-cited** — each cited to its survey/drawing/file, with `[ASSUMPTION]` / `[GAP]` where uncertain; no invented survey result.
- [ ] **The client's Reg 4 duty AND timing are stated** — provided as soon as practicable to everyone appointed/considered (Reg 4(4)); omitting the duty/timing is a citation hard-fail, not a FLAG.
- [ ] **Loose coupling holds** — the one-line PCI → CPP → H&S File (Reg 4 → 12 → 12(5)) cross-reference is present WITHOUT assuming the CPP or H&S File skill ran.
- [ ] **India: the state is resolved before any form**; defers to `hse-india` / `bocw-compliance`; an un-seeded state → `[GAP]`, never a minted national form number.
- [ ] **Restricted-distribution flag** set where the pack carries sensitive site / occupier detail; survey-occupier names + health detail scrub to role labels (the user-supplied owners stay named).

## Sign-off note
SME review: ran (personas: CDM Principal Designer + CDM Client Adviser); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
