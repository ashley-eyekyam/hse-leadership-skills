---
sme-review:
  personas:
    - role: "SEMA-approved racking inspector / Person Responsible for Racking Safety (PRRS)"
      expertise: "BS EN 15635:2008 + the SEMA Code of Practice — the racking inspection regime (weekly visual + ≥12-monthly expert), SWL load-notice duties, damage tolerances, and the SEMA Red/Amber/Green damage-classification and remedial-action map."
      lens: "would a SEMA inspector defend this — every racking control led by the SWL-rated configuration / column protection / the inspection regime (not 'inspect carefully'); every damage finding classified on the correct SEMA RAG band with the matching action (Red = immediate off-load + isolate, never down-rated to 'monitor'; Amber = repair within 4 weeks + auto-escalate); no SWL, tolerance, or inspection interval assumed (every unsupplied value a [GAP]); the Amber off-load nuance confirmed for the site"
    - role: "Warehouse transport / MHE safety practitioner (HSG136 / L117)"
      expertise: "OSHA 1910.178 + PUWER 1998 + HSE ACOP L117 + HSG136 — powered-industrial-truck operation, operator competence/evaluation, and the engineered pedestrian-vehicle segregation hierarchy for workplace transport."
      lens: "would a workplace-transport regulator accept this — MHE/pedestrian conflict controlled by engineered segregation FIRST (barriers, one-way systems, marked and protected walkways/crossings) before hi-vis or 'look out for forklifts'; operator competence + pre-use inspection evidenced; every control owned and dated; zero de-id leak of any prior struck-by incident"
modes:
  racking-assessment:
    detected_by: "Q1/Q9 — the named warehouse + racking installation + the output artifact (full racking + traffic safety report / inspection regime + PRRS pack / SEMA RAG remedial fix-list)"
    floor:
      - id: whr-swl-led-controls
        description: "Every racking control is led by the SWL-rated configuration / column protection / the EN 15635 inspection regime — not 'inspect carefully' or a hi-vis briefing; a hi-vis/inspect-led headline control is pushed up the hierarchy"
        anchors: ['SWL', 'column protection', 'EN 15635', 'load notice']
        min_matches: 2
      - id: whr-en15635-regime-complete
        description: "The EN 15635 inspection regime is complete — a named PRRS, the weekly visual, and the ≥12-monthly expert inspection (6-monthly for high-traffic / 24-7 sites); an absent expert inspection or unappointed PRRS is a high-priority finding"
        anchors: ['PRRS', 'weekly visual', 'expert inspection', '12.month']
        min_matches: 2
      - id: whr-sema-rag-actions
        description: "Every damage finding is on the correct SEMA RAG band with the matching action: Red = immediate off-load + isolate (never down-rated to 'monitor'), Amber = repair within 4 weeks + auto-escalate to Red, Green = log + monitor"
        anchors: ['SEMA', 'Red', 'Amber', 'off.load', 'isolate']
        min_matches: 2
      - id: whr-no-swl-assumed
        description: "No SWL, tolerance, or inspection interval is assumed — every unsupplied site-specific value is a literal [GAP] with a request for the SWL load notice / rack-design drawing"
        anchors: ['\[GAP\]', 'SWL', 'tolerance', 'load notice', 'rack.design']
        min_matches: 2
      - id: whr-engineered-segregation
        description: "MHE/pedestrian conflict is controlled by engineered segregation first (barriers, one-way systems, marked and protected walkways/crossings) before hi-vis or signage; operator competence + pre-use inspection are evidenced"
        anchors: ['segregation', 'barrier', 'one.way', 'walkway', 'pedestrian']
        min_matches: 2
      - id: whr-incident-deid-owned-cited
        description: "Any prior struck-by / rack-collapse incident is de-identified to role labels with <5 cells suppressed; every action has a named owner + date; every citation resolves (EN 15635 / SEMA / 1910.178 / PUWER / L117)"
        anchors: ['de.identif', 'role label', 'owner', 'EN 15635', 'SEMA', 'PUWER', 'L117']
        min_matches: 2
---

# SME Review & Sign-off — warehouse-racking-mhe-safety

Run BOTH personas before any output. The **SEMA-approved racking inspector** owns the racking limb (the
inspection regime, the SWL duties, and the SEMA RAG classification + remedial action); the **warehouse
transport / MHE practitioner** owns the MHE/pedestrian-segregation limb. Both apply the universal hard
gates (no error or unsupported claim, every regulatory trigger caught, no lower-order-only control
without justification, zero de-identification leak).

## Domain checklist (the nuanced things only these experts catch)
- [ ] Every racking control is led by the **SWL-rated configuration / column protection / the EN 15635
      inspection regime** — not "inspect carefully" or a hi-vis briefing; a hi-vis/inspect-led headline
      control is flagged and pushed up the hierarchy.
- [ ] The **EN 15635 inspection regime** is complete: a named **PRRS**, the **weekly visual**, and the
      **≥12-monthly expert** inspection (6-monthly for high-traffic / 24-7 sites) — an absent expert
      inspection or unappointed PRRS is a high-priority finding.
- [ ] Every damage finding is on the **correct SEMA RAG band** with the matching action: **Red =
      immediate off-load + isolate** (never down-rated to "monitor"), **Amber = repair within 4 weeks +
      auto-escalate to Red** (the Amber off-load nuance confirmed for the site), **Green = log +
      monitor**.
- [ ] **No SWL, tolerance, or inspection interval is assumed** — every unsupplied site-specific value
      is a literal `[GAP]` with a request for the SWL load notice / rack-design drawing.
- [ ] MHE/pedestrian conflict is controlled by **engineered segregation first** (barriers, one-way
      systems, marked and protected walkways/crossings) before hi-vis or signage; operator competence +
      pre-use inspection are evidenced.
- [ ] Any **prior struck-by / rack-collapse incident** is de-identified to role labels with `<5` cells
      suppressed; every action has a named owner + date; every citation resolves (EN 15635 / SEMA /
      1910.178 / PUWER / L117).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The Amber damage with no bridge** — an Amber-band finding is scheduled for repair within
  the window but no interim off-load / reduced-SWL / bay-isolation control is stated for the
  period until the repair, and the auto-escalation-to-Red trigger is not wired.
- **The missing emergency / rescue leg** — the report controls MHE and racking but never
  addresses the spill/collapse/struck-by emergency response, the aisle-blockage evacuation
  route, or how a trapped-pedestrian or fallen-load event is managed on this layout.
- **The quantitative basis absent** — a control (aisle width, SWL, segregation clearance,
  inspection interval) is asserted without the displayed load-notice value, the EN 15635
  interval, or the rack-design figure it is measured against, so an unsupplied value is
  asserted rather than honestly [GAP]'d.

## Sign-off note
SME review: ran (personas: SEMA-approved racking inspector + warehouse transport / MHE practitioner);
this is decision-support; competent-person review still required. A FLAG it raises is recorded, never
merge-blocking — it precedes and never replaces the human competent-person review.
