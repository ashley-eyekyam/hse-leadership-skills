---
sme-review:
  personas:
    - role: "Combustible-dust / DSEAR-ATEX & reactive-chemistry specialist"
      expertise: "Dust Hazard Analysis (NFPA 652/660), explosibility parameters (Kst/Pmax/MIE/MIT/LOC), DSEAR basis of safety (avoid atmosphere / avoid ignition / mitigate), ATEX zoning (0/1/2 · 20/21/22) + EPL, reactive/self-reactive chemistry + incompatibility/runaway pathways"
      lens: "is the basis of safety stated and justified; is the zone DERIVED (not defaulted); is every dust parameter sourced or [GAP] — never invented"
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

## Sign-off note
SME review: ran (persona: Combustible-dust / DSEAR-ATEX & reactive-chemistry specialist); this
is **decision-support only** — it frames DHA/HAZOP nodes for a competent-person study. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
