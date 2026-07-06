---
sme-review:
  personas:
    - role: "CDM Principal Designer (chartered, pre-construction-information competent person)"
      expertise: "CDM 2015 Reg 4 pre-construction information; the L153 Appendix-1 PCI content checklist; existing-structure hazard information (asbestos/ACMs, buried & overhead services, ground conditions, structural form, the existing H&S file); brownfield / occupied-building survey practice; the PCI → CPP → H&S File document chain."
      lens: "Is this REAL pre-construction information a designer/contractor could rely on — every existing-structure hazard source-cited, and is EVERY missing source a documented [GAP] with an owner + date, never silently omitted — not a thin checklist that hides what isn't known?"
    - role: "CDM Client Adviser / duty-holder compliance adviser"
      expertise: "The CDM 2015 Reg 4 CLIENT duty — provide the PCI as soon as practicable to everyone appointed or being considered (Reg 4(4)); Reg 4(5)/(6) no construction start without arrangements/CPP; the timing and circulation obligations; India BOCW pre-work site information via hse-india + state form + the OSH-Code transition."
      lens: "Is the client's Reg 4 duty AND its timing stated, is the pack issued (restricted-distribution) to the right parties, and for India is the state resolved before any form is named — never a minted national form number?"
modes:
  pre-construction-information:
    detected_by: "Q1 — Output type (the Regulation 4 pre-construction-information pack)"
    floor:
      - id: pci-gap-discipline-owned
        description: "EVERY existing-structure source the user does not hold is a documented [GAP] with a named owner + due date in an information-gaps register — a silently-omitted missing source is the load-bearing failure (KB-SNIP-PCI-CHECKLIST)"
        anchors: ['information.gaps register', 'never silently omitted']
        min_matches: 1
      - id: pci-asbestos-status-explicit
        description: "Asbestos/ACM status is explicit — present-and-surveyed, presumed-pending-survey, or [GAP] (survey outstanding, owner+date) — never silently absent on a refurbishment/demolition"
        anchors: ['asbestos', 'ACM', 'refurbishment.and.demolition survey|R&D survey']
        min_matches: 1
      - id: pci-services-addressed
        description: "Buried & overhead services are addressed (presence/location or a documented [GAP]); an intrusive survey is required before excavation/lifting (KB-SNIP-PCI-CHECKLIST)"
        anchors: ['buried (&|and) overhead services', 'overhead (lv )?line', 'intrusive survey']
        min_matches: 1
      - id: pci-existing-structure-source-cited
        description: "The existing-structure hazard information is source-cited (survey/drawing/existing H&S file) with [ASSUMPTION]/[GAP] where uncertain; no invented survey result"
        anchors: ['existing.structure hazard', 'as.built']
        min_matches: 1
      - id: pci-client-reg4-duty-timing
        description: "The client's Reg 4 duty AND timing are stated — provided as soon as practicable to everyone appointed/considered (Reg 4(4)); Reg 4(5)/(6) no start without arrangements/CPP (KB-REG-CDM2015)"
        anchors: ['reg(ulation)?\s*4\(4\)', 'as soon as practicable']
        min_matches: 1
      - id: pci-cdm-chain-loose-coupling
        description: "The PCI -> CPP -> H&S File chain (Reg 4 -> 12 -> 12(5)) is cross-referenced without assuming the CPP or H&S File skill ran (KB-SNIP-CONSTRUCTION-CLAUSE-MAP)"
        anchors: ['document chain', 'loose coupl']
        min_matches: 1
      - id: pci-restricted-distribution-deid
        description: "A restricted-distribution flag is set where the pack carries sensitive site/occupier detail; survey-occupier names + health detail scrub to role labels (user-supplied owners stay named)"
        anchors: ['restricted', 'de.identif', 'role label']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The thin checklist that hides what isn't known (canary S7)** — the scope-honesty failure of
  this class: a tidy PCI that lists what is known and silently drops every source that is NOT
  held (asbestos survey, ground investigation), instead of surfacing each as an owned `[GAP]`.
- **The L153 Appendix-1 content set named but not swept (canary S6)** — the pack cites its basis
  (L153 App-1 / Reg 4) yet silently omits content the checklist demands: existing H&S file,
  ground conditions, services, structural form, adjacent-occupier constraints.
- **The occupied/adjacent interaction not carried into design (canary S7)** — the occupied lower
  floors, the public footpath, and an adjacent-occupier vulnerability recorded as design/sequence
  constraints, not two legs that never meet.
- **Record identity & basis absent (canary S8)** — each existing-structure fact cited to its
  survey/drawing/file revision and dated, never asserted without a source.

## Sign-off note
SME review: ran (personas: CDM Principal Designer + CDM Client Adviser); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
