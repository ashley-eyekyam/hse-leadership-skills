---
sme-review:
  personas:
    - role: "Combustible-dust / DSEAR-ATEX & reactive-chemistry specialist"
      expertise: "Dust Hazard Analysis (NFPA 652/660), explosibility parameters (Kst/Pmax/MIE/MIT/LOC), DSEAR basis of safety (avoid atmosphere / avoid ignition / mitigate), ATEX zoning (0/1/2 · 20/21/22) + EPL, reactive/self-reactive chemistry + incompatibility/runaway pathways"
      lens: "is the basis of safety stated and justified; is the zone DERIVED (not defaulted); is every dust parameter sourced or [GAP] — never invented"
modes:
  dust-hazard-assessment:
    detected_by: "Q1 — Scope (a DHA, a reactive-chemistry review, an ATEX/DSEAR zoning, or a basis-of-safety statement)"
    floor:
      - id: rde-parameters-sourced-or-gap
        description: "Kst / Pmax / MIE / MIT each carry a lab source + year or are a literal [GAP] — a fabricated dust parameter is hard-gate-adjacent, [GAP] + route-to-testing is the honest path (KB-STD-NFPA-652)"
        anchors: ['Kst', 'Pmax', '\bMIE\b']
        min_matches: 1
      - id: rde-area-classification-derived
        description: "The area classification / ATEX zone is DERIVED from release grade + ventilation, never defaulted; the EPL matches the zone (KB-STD-ATEX / KB-STD-DSEAR)"
        anchors: ['area classification|ATEX', 'never defaulted|justified']
        min_matches: 1
      - id: rde-basis-of-safety-stated
        description: "The basis of safety is stated explicitly and is one of avoid-atmosphere / avoid-ignition / mitigate — a control list with no declared basis of safety is a FLAG (KB-STD-DSEAR)"
        anchors: ['basis of safety', 'avoid.ignition|avoid.atmosphere|mitigat']
        min_matches: 1
      - id: rde-ignition-sources-enumerated
        description: "Ignition sources are enumerated against the credible scenarios (electrostatic, mechanical/friction, hot surfaces, self-heating) — a DHA listing consequences with no ignition-source review is a FLAG"
        anchors: ['ignition source', 'electrostatic|friction|hot surface']
        min_matches: 1
      - id: rde-reactive-thermal-screen
        description: "Reactive-chemistry / incompatibility / thermal-runaway pathways are addressed, not omitted where the material warrants (KB-STD-IEC-61882)"
        anchors: ['reactive.chem|incompatib|runaway|self.heat', 'thermal screen|reactive.chemistry']
        min_matches: 1
      - id: rde-controls-hoc-ranked
        description: "Controls are HoC-ranked — inherently-safer/eliminate/substitute before engineering, engineering before admin/PPE; a dust/atmosphere hazard 'controlled' by housekeeping or PPE alone is hard-gate-adjacent (KB-SNIP-HOC)"
        anchors: ['hierarchy of controls', 'HoC.rank']
        min_matches: 1
      - id: rde-hazop-handoff
        description: "The structured reactive/deflagration study is handed to hazop-facilitator (DHA/HAZOP nodes) — an output presenting itself as having run the workshop is a FLAG (KB-STD-IEC-61882)"
        anchors: ['hazop.facilitator', 'IEC.?61882|deflagration']
        min_matches: 1
---

# SME Review & Sign-off — reactive-dust-explosion-assessment

One lens suffices: a combustible-dust / DSEAR-ATEX & reactive-chemistry specialist who insists
the basis of safety is declared, the ATEX zone is derived not defaulted, and every
explosibility parameter is sourced or `[GAP]`. The persona **narrows** the Chemical-Process-
Safety sector slot that extends the generic **HSE-SME-Reviewer** hook (`KB-SNIP-ARCHETYPES`).
The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated
actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Kst / Pmax / MIE / MIT each carry a lab source + year, or are `[GAP]` — a fabricated dust parameter is **hard-gate-adjacent** (escalate); `[GAP]` + route-to-testing is the honest path.
- [ ] ATEX zone derived from release grade + ventilation, **not defaulted** — an unjustified 0/1/2 or 20/21/22 zone is a FLAG; the EPL matches the zone.
- [ ] Basis of safety stated explicitly and is one of avoid-atmosphere / avoid-ignition / mitigate — a control list with no declared basis of safety is a FLAG.
- [ ] Ignition sources enumerated against the credible scenarios — electrostatic, mechanical/friction, hot surfaces, self-heating; a DHA listing consequences but no ignition-source review is a FLAG.
- [ ] Reactive chemistry / incompatibility / runaway pathways addressed, not omitted — incompatible materials, self-reactive/exothermic and thermal-runaway pathways considered where the material warrants; silent omission is a FLAG.
- [ ] Controls HoC-ranked — inherently-safer / eliminate / substitute before engineering, engineering before admin/PPE; a dust/atmosphere hazard "controlled" by housekeeping or PPE alone is **hard-gate-adjacent** (HoC) unless justified-or-escalated.
- [ ] The structured reactive/deflagration study handed to `hazop-facilitator` (DHA/HAZOP nodes, `KB-STD-IEC-61882`) — an output presenting itself as having run the workshop is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The two legs that never meet (canary S7)** — the connected-vessel / secondary-explosion path
  (the dominant fatality mechanism) assessed across linked equipment, not each vessel in
  isolation.
- **The parameter/zone asserted by silence (canary S5)** — an explosibility parameter or an area
  classification stated with no lab source/year or no derivation basis; every missing value a
  literal [GAP], the zone derived not defaulted.
- **The basis of safety that is really housekeeping (canary S6 / scope honesty)** — a control list
  offered as the basis of safety with no declared avoid-atmosphere / avoid-ignition / mitigate
  strategy and no prevention-vs-protection split.
- **Ignition/incident-history silence (canary S3)** — credible ignition sources not enumerated,
  and prior deflagration/flash near-misses neither reviewed nor confirmed absent.

## Sign-off note
SME review: ran (persona: Combustible-dust / DSEAR-ATEX & reactive-chemistry specialist); this
is **decision-support only** — it frames DHA/HAZOP nodes for a competent-person study. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
