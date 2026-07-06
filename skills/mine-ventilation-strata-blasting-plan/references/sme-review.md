---
sme-review:
  personas:
    - role: "DGMS-competent mine-plans engineer (ventilation officer / strata-control engineer with shotfiring/blasting competency)"
      expertise: "mine ventilation network design + gas regime (CH4/CO/CO2/O2), air quantity/quality, district splitting, strata/geotech support regimes, ICMM principal-hazard framing; explosive selection, blast design, blast-exclusion zone, initiation sequence, misfire/abandonment procedure, fume/flyrock/vibration control, statutory shotfiring duties"
      lens: "For the plan type selected, is it site-specific and adequate — gas regime correctly characterised and ventilation quantity/quality ADEQUATE for the districts and worst-credible gas make; the strata support regime competent for the ground conditions; the blast-exclusion zone defined and enforced with a complete misfire procedure and explosives matched to the strata/gas regime — and are the cross-discipline interactions (e.g. fume re-entry vs ventilation clearance, permitted explosives in a gassy seam) addressed, not a generic template?"
modes:
  mine-plan:
    detected_by: "Q1 — Which plan + new/review (ventilation / strata-ground-control / blasting-shotfiring); Q2 sets the commodity + mine type. The floor applies to whichever plan leg(s) are in scope."
    floor:
      - id: ventilation-adequacy-districts
        description: "The gas regime and air quantity/quality are characterised for the ACTUAL districts and worst-credible gas make — not a generic air figure (intake Q4V)"
        anchors: ['ventilation', 'air quantity', 'gas']
        min_matches: 2
      - id: strata-support-geotech
        description: "The strata/ground-control support regime (type + density/spacing) is tied to the stated geotechnical ground conditions, not a default (intake Q4S)"
        anchors: ['strata|support', 'geotech|convergence']
        min_matches: 2
      - id: blast-exclusion-misfire
        description: "The blast-exclusion (danger) zone is defined, sized and enforced, with a complete misfire/abandonment procedure — the two highest-consequence blasting omissions (intake Q4B)"
        anchors: ['exclusion', 'misfire']
        min_matches: 2
      - id: discipline-interactions
        description: "Cross-discipline interactions are addressed — blast-fume re-entry depends on ventilation clearance; permitted explosives where the seam is gassy (intake Q2/Q4B)"
        anchors: ['re.entry|fume', 'clearance|gassy|permitted explosive']
        min_matches: 1
      - id: hoc-critical-controls
        description: "Critical controls are hierarchy-of-controls-ranked for each principal hazard — elimination/engineering ahead of admin/PPE; no principal hazard (incl. respirable dust) left to PPE/admin alone (intake Q5)"
        anchors: ['hierarchy of controls', 'respirable dust|principal hazard']
        min_matches: 1
      - id: site-specific-or-gap
        description: "Plan parameters are real and site-specific; an un-supplied value is a literal [GAP], never residual template language ('typical', 'as appropriate')"
        anchors: ['\[GAP\]']
        min_matches: 1
      - id: monitoring-tarp
        description: "A monitoring regime and Trigger Action Response Plan (TARP) triggers govern the live plan (gas monitoring, convergence, re-entry gas-clearance)"
        anchors: ['monitoring', 'tarp']
        min_matches: 2
---

# SME Review & Sign-off — mine-ventilation-strata-blasting-plan

Single specialized persona, narrowing the **Mine Manager** archetype slot
(`KB-SNIP-ARCHETYPES`, archetypes:291-326 — its "plan is site-specific + adequate"
bullet, archetypes:305-307, and the HoC bullet, archetypes:312-314). This skill
spans three engineering disciplines (ventilation, strata/ground control, blasting)
routed by the plan-type MCQ; the persona carries all three competencies and applies
**only the matching discipline(s)** to the plan type the user actually selected — it
does not review a discipline the artifact does not contain.

> **Matching-lens scoping:** when the user selects only one plan type (ventilation OR
> strata OR blasting), apply only the matching discipline checks below; the
> cross-discipline interaction check applies whenever the selected plan touches an
> adjacent discipline (e.g. a blasting plan in a gassy/ventilated district).

## Domain checklist (the nuanced things only this expert catches)
- [ ] Gas regime + ventilation adequacy reasoned to the actual districts — air quantity/quality and gas make characterised for the real plan parameters, not a generic air figure; FLAG a ventilation plan with no district-level air quantity or no gas-regime statement.
- [ ] Strata/ground-control support regime is competent for the stated geotech — support type/spacing tied to ground conditions, not a default; FLAG a strata plan with no geotechnical basis.
- [ ] Blast-exclusion zone is defined, sized, and enforced, with a complete misfire/abandonment procedure; FLAG a blasting plan missing the exclusion zone or the misfire procedure (the two highest-consequence blasting omissions).
- [ ] Discipline interactions are addressed — blasting fume re-entry timing depends on ventilation clearance; permitted explosives where the seam is gassy; FLAG a blasting plan that ignores the ventilation/gas interaction.
- [ ] Critical controls flagged and HoC-ranked for each principal hazard — `controls` ranks elimination/engineering ahead of admin/PPE; FLAG any principal hazard left to PPE/admin alone.
- [ ] Plan parameters are real, not a generic template; FLAG residual template language ("typical", "as appropriate") where a site-specific value is required.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The generic air figure** — a ventilation plan with a single headline air quantity and no
  district-level breakdown or gas-regime statement for the actual seam gassiness.
- **Strata support with no geotechnical basis** — a support type/density stated as a default
  with no tie to the ground conditions, roof/highwall, or convergence data.
- **The blasting plan missing its two load-bearing controls** — no defined/sized exclusion
  zone, or no complete misfire/abandonment procedure; the highest-consequence blasting gaps.
- **The interaction ignored** (canary S6/S7) — a blasting plan that ignores ventilation/gas:
  re-entry timing not tied to fume clearance, or non-permitted explosives specified for a
  gassy seam.
- **Template residue** — "typical", "as appropriate", "to be confirmed" left where a
  site-specific value is required, instead of a `[GAP]` routed to the competent person.

## Sign-off note
Reviewed-as: DGMS-competent mine-plans engineer (ventilation/strata-control +
shotfiring/blasting) — model QA (decision-support); recorded, FLAGs non-blocking.
This review precedes — and never replaces, never emits — the competent person who
owns the engineering judgement and signs off; it never outputs "approved by a
competent person".
