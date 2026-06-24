---
sme-review:
  personas:
    - role: "CDM Principal Designer (chartered, health-and-safety-file competent person)"
      expertise: "CDM 2015 Reg 12(5)–(9) — the principal designer's duty to prepare and maintain the Health & Safety File and hand it over to the client at completion; the L153 Appendix-4 H&S-file content list; the residual & unusual hazard 'could-not-reasonably-anticipate' test; as-built & services information, hazardous materials in situ (asbestos register), and maintenance/cleaning/refurb/demolition safety arrangements; the PCI → CPP → H&S File document chain; revision control on a living file."
      lens: "Is this a REAL as-built residual-risk record a future maintenance / cleaning / refurbishment / demolition worker could rely on — only the residual & unusual hazards they could NOT reasonably anticipate, each LOCATED, hazardous materials in situ recorded — and NOT a general-spec dump? Is preparation correctly the principal designer's duty (Reg 12(5)) and is the handover duty stated (Reg 12(6)–(9))? Does an update APPEND, never overwrite?"
---

# SME Review & Sign-off — health-safety-file

This skill carries **one** SME lens — a **CDM Principal Designer** — specializing the generic
**HSE-SME-Reviewer** runtime hook (`KB-SNIP-ARCHETYPES`). The H&S File's load-bearing failure
modes (a general-spec dump instead of residual-only content; preparation attributed to the
wrong duty-holder; the handover duty omitted; an update that overwrites) are exactly the things
a principal designer catches. The universal hard gates (de-id leak, citation accuracy,
owned-and-dated actions, no unjustified PPE/admin-only control) are the enforced class and are
not restated below.

Note the de-id-vs-named-owners exception: the user-supplied principal designer / client
duty-holders and the owners of open completion items named for the record stay named;
commissioning/survey-record names and any health detail scrub to role labels.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Residual-only discipline holds** — only residual & unusual hazards a future worker could NOT reasonably anticipate are recorded; the full general specification dumped in place of the residuals is the load-bearing FLAG.
- [ ] **Every residual hazard is LOCATED** (where in the structure) — not a generic hazard list.
- [ ] **Hazardous materials in situ are recorded with locations** — asbestos register / coatings / insulation; an outstanding survey is presumed-present-pending-survey `[GAP]` + a hold-point, never silently absent.
- [ ] **The as-built & services information is source-cited** — key as-built drawings, services & isolation-point locations; `[GAP]` where a record (e.g. a commissioning record) is missing; no invented as-built detail.
- [ ] **Future-work controls are HoC-ranked** — the maintenance/cleaning/refurb/demolition arrangements prefer a higher-order future-work control over a PPE/admin-only treatment (a designed-in control before "wear a harness").
- [ ] **Preparation is the principal designer's duty (Reg 12(5))** — attributing it to the wrong duty-holder is a citation hard-fail, not a FLAG; **the handover duty (Reg 12(6)–(9)) is stated**.
- [ ] **An update APPENDS, never overwrites** — prior residual-risk content is preserved under revision control.
- [ ] **Loose coupling holds** — the one-line PCI → CPP → H&S File (Reg 4 → 12 → 12(5)) cross-reference is present WITHOUT assuming the PCI or CPP skill ran.
- [ ] **India: the state is resolved before any form**; defers to `hse-india` / `bocw-compliance`; an un-seeded state → `[GAP]`, never a minted national form number.
- [ ] **Restricted-distribution flag** set where the file carries security-sensitive structural/services detail; **no worker health detail** in the file; commissioning/survey names scrub to role labels (the user-supplied duty-holders stay named).

## Sign-off note
SME review: ran (persona: CDM Principal Designer); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score
below threshold) are a separate enforcement class.
