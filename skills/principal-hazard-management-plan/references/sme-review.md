---
sme-review:
  personas:
    - role: "principal-hazard / major-hazard management specialist (mining PHMP facilitator)"
      expertise: "principal-hazard taxonomy (strata/inrush/fire-explosion/ventilation/mobile-plant/fall-from-height/hazardous-energy/respirable-dust), HIRA structure, hierarchy-of-controls suites, critical-control linkage, performance/monitoring regimes"
      lens: "For this named principal hazard, is the hazard analysis structured, the control suite genuinely higher-order-led, the critical controls linked to a live CCM with performance + verification, and monitoring owned and dated — or a generic risk register relabelled 'PHMP'?"
modes:
  phmp:
    detected_by: "Q1 — Develop a full PHMP or structure the workshop; Q3 selects the principal hazard. The floor applies to every PHMP output."
    floor:
      - id: structured-hazard-analysis
        description: "The principal hazard has a structured hazard analysis (HIRA / credible scenarios / pathway) with a risk rating — not a bare control list (intake Q3/Q4)"
        anchors: ['hazard identif|hira|credible scenario', 'risk rat|risk matrix']
        min_matches: 2
      - id: hoc-higher-order-led
        description: "The control suite is hierarchy-of-controls-ranked and higher-order-led — elimination/substitution/engineering before admin/PPE; a PPE/admin-only treatment of a PRINCIPAL hazard is escalated/justified, never accepted"
        anchors: ['hierarchy of controls', 'elimination|engineering']
        min_matches: 2
      - id: critical-controls-ccm-linked
        description: "Critical controls are linked to the ICMM CCM with performance + verification carried over — the PHMP does not re-invent CCM (intake Q5)"
        anchors: ['critical control', 'ccm|verification|performance']
        min_matches: 2
      - id: monitoring-owned-dated
        description: "Each monitoring/performance trigger is owned and dated — a role owner + due date / review cadence / TARP trigger (intake Q5/Q7)"
        anchors: ['monitoring', 'owner|review|tarp']
        min_matches: 2
      - id: gap-values-not-fabricated
        description: "Performance requirements / engineering values are a literal [GAP] when un-supplied and routed to the competent person, never fabricated (intake Q5)"
        anchors: ['\[GAP\]', 'competent person']
        min_matches: 2
      - id: named-principal-hazard-scoped
        description: "The named principal hazard is from the recognised taxonomy and scoped to the specific mine — not a generic 'general safety' plan (intake Q3/Q4)"
        anchors: ['principal hazard', 'inrush|strata|inundation']
        min_matches: 2
      - id: standoff-barrier-basis
        description: "The standoff / barrier design basis (performance intent + design inputs) is stated where the hazard demands an engineered barrier, with quantities the competent person must confirm"
        anchors: ['standoff|barrier', 'design']
        min_matches: 2
---

# SME Review & Sign-off — principal-hazard-management-plan

Single specialized persona, narrowing the **Mine Manager** archetype slot
(`KB-SNIP-ARCHETYPES`, archetypes:291-326 — its HoC bullet, archetypes:312-314, plus
the critical-control linkage to ICMM-CCM). This is an **assistive** (Tier-4,
`status: assistive`) skill that *builds on* `icmm-critical-control-management`, so the
persona additionally holds the autonomy boundary test.

> **Overlap note (D-04):** this skill shares ~80% of its surface with
> `icmm-critical-control-management` and carries its critical controls into a live
> ICMM CCM linkage (`KB-STD-ICMM-CCM`). Each skill ships its **own self-contained**
> `references/sme-review.md` (no shared fragment); the CCM-linkage check below (item 3)
> is the seam most likely to be skipped and is this persona's highest-value catch.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each principal hazard has a structured hazard analysis + risk rating, not a bare control list — HIRA structure + `risk_matrix` rating; FLAG a PHMP with controls but no analysed hazard pathway.
- [ ] Control suite is HoC-ranked, higher-order-led — elimination/substitution/engineering before admin/PPE; a PPE/admin-only treatment of a *principal* hazard is escalated/justified, never accepted; FLAG any principal hazard left to PPE/admin alone.
- [ ] Critical controls are linked to ICMM CCM with performance + verification carried over — the PHMP does not re-invent CCM; FLAG a critical control named in the PHMP with no CCM performance/verification linkage.
- [ ] Monitoring/performance triggers are owned and dated — each monitoring activity has a role owner + due date / review trigger; FLAG monitoring with no owner or no review cadence.
- [ ] Performance requirements / engineering values are `[GAP]` when un-supplied, never fabricated; FLAG any invented engineering/performance value.
- [ ] The named principal hazard is from the recognised taxonomy and scoped to the specific mine — not a generic "general safety" plan; FLAG a PHMP whose hazard is mis-scoped or not a true principal hazard.
- [ ] **Assistive autonomy test:** reads as structured workshop output the mine team owns, not an autonomously authored plan (archetypes:316-326).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The relabelled risk register** — controls listed with no structured hazard analysis or
  credible-scenario pathway behind them; a "PHMP" that never analysed how the principal
  hazard is realised.
- **PPE/admin treating a principal hazard** — a principal hazard left to administrative
  controls or PPE without the higher-order (elimination/isolation/engineering) barrier that a
  major hazard demands, or without an explicit escalation/justification.
- **The critical control with no CCM link** — a control named "critical" in the PHMP with no
  performance standard or verification linked to the ICMM CCM, so it is asserted, not assured.
- **The design basis asserted, not quantified** — a standoff distance or barrier density
  stated as fact where a competent geotech/hydrology person must quantify it; an invented
  engineering value instead of a `[GAP]`.
- **Monitoring with no owner or trigger** — monitoring activities listed with no role owner,
  no review cadence, and no TARP trigger that converts a reading into an action.

## Sign-off note
Reviewed-as: principal-hazard / major-hazard management specialist — model QA
(decision-support); workshop-structuring only, FLAGs non-blocking. This review
precedes — and never replaces, never emits — the mine team's engineering judgement
and the competent person who signs off; it never outputs "approved by a competent
person".
