# Construction

`hse-construction` is the construction pack — the CDM-2015 lifecycle plus the everyday site artifacts. It covers the Pre-Construction Information pack, the Construction Phase Plan, the Health and Safety File, lift plans (LOLER 1998 / BS 7121), traffic-management plans, permits-to-work, India BOCW compliance, and the construction-grade risk assessment and toolbox talk reused from the core pack.

```
/plugin install hse-construction@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### bocw-compliance -> see [India Compliance](India-Compliance#bocw-compliance)
Assesses India BOCW statutory compliance for construction establishments, so it appears here for India construction projects. Full card on the India Compliance page.

### construction-phase-plan
- **Produces:** Risk-proportionate CDM 2015 Construction Phase Plan (CPP) for a named project.
- **For:** M, C, F · **Grounded in:** CDM 2015 Regulation 12 + HSE L153; 29 CFR 1926 Subpart C for USA equivalents; India BOCW via `hse-india` with mandatory state detection · **Packs:** hse-construction, hse-operations.
- **Use when:** A principal contractor, sole contractor, manager, or consultant needs to build, write, or review the pre-start CPP for a specific construction project.
- **Don't use for:** Pre-tender client information or completion handover records; use [pre-construction-information](#pre-construction-information) for PCI and [health-safety-file](#health-safety-file) for the H&S File.
- **Have ready:** Named project and programme, contractor configuration, notifiability/F10 status, at least one significant activity, PCI status, jurisdiction, existing arrangements, duty-holders, and review triggers.
- **Trigger:** "a user asks to build", "review a Construction Phase Plan", "a CPP".
- **You get:** Project description and programme, management arrangements, site rules, significant risks and hierarchy-ranked controls by activity, notification status, assumptions and `[GAP]` items, SMART actions, and a one-line PCI -> CPP -> H&S File CDM document-chain cross-reference.
- **Pairs well with:** [pre-construction-information](#pre-construction-information), [health-safety-file](#health-safety-file), [risk-assessment](Core#risk-assessment), [traffic-management-plan](#traffic-management-plan), [permit-to-work](Process-Safety#permit-to-work).

### health-safety-file
- **Produces:** CDM 2015 Health and Safety File for a named completed or near-complete structure.
- **For:** M, C · **Grounded in:** CDM 2015 Regulation 12(5)-(9), HSE L153 Appendix 4, and the PCI -> CPP -> H&S File clause map · **Packs:** hse-construction.
- **Use when:** The project is at handover, completion, update, or package-addition stage and the client needs the as-built residual-risk record for future maintenance, cleaning, refurbishment, or demolition.
- **Don't use for:** Pre-tender hazard information or a pre-start construction plan; use [pre-construction-information](#pre-construction-information) for PCI and [construction-phase-plan](#construction-phase-plan) for the CPP.
- **Have ready:** Named structure and use, file purpose, located residual or unusual hazards or a "none beyond the obvious" justification, as-built/services records, hazardous-materials information, future-work scope, jurisdiction, handover duty-holders, and open-item owners.
- **Trigger:** "a user asks to compile", "review a health and safety file", "an H&S file".
- **You get:** As-built and services record, located residual/unusual hazards, hazardous materials left in situ, maintenance/cleaning/refurbishment/demolition safety arrangements, information gaps, revision-control notes, handover duties, and SMART close-out actions.
- **Pairs well with:** [pre-construction-information](#pre-construction-information), [construction-phase-plan](#construction-phase-plan), [risk-assessment](Core#risk-assessment).

### lift-plan
- **Produces:** Site- and lift-specific lifting plan with BS 7121 classification, method, exclusion zones, roles, contingency, and abort criteria.
- **For:** M, C, F · **Grounded in:** LOLER 1998 Regulation 8 and Regulation 9, BS 7121, ISO 45001 clause 6.1.2, manufacturer rated-capacity chart inputs, and 29 CFR 1926 Subpart CC where applicable · **Packs:** hse-construction.
- **Use when:** A team needs to plan, build, classify, or review a real lifting operation, crane lift plan, appointed-person plan, tandem/blind lift, or lift near structures, power lines, public areas, or constrained ground.
- **Don't use for:** Generic task HIRA or construction project-wide planning; use [risk-assessment](Core#risk-assessment) for a general HIRA and [construction-phase-plan](#construction-phase-plan) for the project CPP.
- **Have ready:** Lift category, confirmed load weight including rigging, dimensions/CoG/lifting points, crane configuration, SWL at working radius and utilisation transcribed from the rated-capacity chart, site/proximity hazards, named appointed person for standard/complex lifts, operator/slinger competence, evidence certificates, wind limit, lift window, and re-plan triggers.
- **Trigger:** "a user asks to plan", "review a lifting plan", "a crane lift plan".
- **You get:** Basic/standard/complex lift classification, load and rigging confirmation, SWL-at-radius chart record, ground/proximity controls, exclusion and segregation zones, initial/residual risk scoring, sequenced lift method, named roles, weather limits, contingency and abort criteria, and hold-points where the lift cannot proceed without competent-person review.
- **Pairs well with:** [construction-phase-plan](#construction-phase-plan), [traffic-management-plan](#traffic-management-plan), [permit-to-work](Process-Safety#permit-to-work), [risk-assessment](Core#risk-assessment).

### permit-to-work -> see [Process Safety](Process-Safety#permit-to-work)
Controls high-risk construction work such as hot work, confined-space entry, excavation, and work at height. Full card on the Process Safety page.

### pre-construction-information
- **Produces:** Pre-Construction Information (PCI) pack for a named construction project before construction starts.
- **For:** M, C · **Grounded in:** CDM 2015 Regulation 4, HSE L153 Appendix 1, and the PCI -> CPP -> H&S File clause map · **Packs:** hse-construction.
- **Use when:** The client or consultant needs to compile, write, or review the pre-tender hazard and information set for designers and contractors.
- **Don't use for:** The contractor's construction-phase arrangements or completion handover file; use [construction-phase-plan](#construction-phase-plan) for CPP and [health-safety-file](#health-safety-file) for the H&S File.
- **Have ready:** Named project and client, existing-structure information sources, asbestos/hazardous materials status, as-built and services drawings, ground/structural information, site surroundings, known significant hazards, project stage, jurisdiction, and owners/due dates for information gaps.
- **Trigger:** "a user asks to compile", "review pre-construction information", "a PCI pack".
- **You get:** Project and client brief, existing-structure hazard information, site and surroundings, known significant hazards, information-gaps register, owner/due-date actions, Reg 4 duty/timing notes, and a PCI -> CPP -> H&S File cross-reference.
- **Pairs well with:** [construction-phase-plan](#construction-phase-plan), [health-safety-file](#health-safety-file), [risk-assessment](Core#risk-assessment).

### risk-assessment -> see [Core](Core#risk-assessment)
Provides the core HIRA workflow used before construction tasks and method statements. Full card on the Core page.

### toolbox-talk -> see [Core](Core#toolbox-talk)
Creates the pre-task crew briefing that often follows a construction RAMS, permit, or risk assessment. Full card on the Core page.

### traffic-management-plan
- **Produces:** Construction traffic management plan for a named site with vehicle/pedestrian routes, segregation, deliveries, reversing controls, and public-interface arrangements.
- **For:** M, C, F · **Grounded in:** CDM 2015 Regulation 27 and Schedule 3, HSE HSG144, 29 CFR 1926 Subpart O / 1926.601 / 1926.602 where applicable, and the traffic-segregation hierarchy · **Packs:** hse-construction.
- **Use when:** A site needs a TMP, site traffic plan, construction logistics/access plan, vehicle-pedestrian segregation, delivery/reversing controls, or public/highway interface controls.
- **Don't use for:** General project safety planning or a task HIRA; use [construction-phase-plan](#construction-phase-plan) for the CPP and [risk-assessment](Core#risk-assessment) for task risk assessment.
- **Have ready:** Named site and access points, vehicle and pedestrian types, known conflict points, delivery and reversing profile, public/highway interface, jurisdiction, existing controls, plan window, and review triggers.
- **Trigger:** "a user asks to write", "review a traffic management plan", "a TMP".
- **You get:** Named vehicle and pedestrian routes, conflict-point register, segregation-by-design controls, reversing-elimination and one-way/turning arrangements, loading and delivery rules, speed/signage/lighting controls, public/highway protection, monitoring/review actions, and `[GAP]` flags where layout details are missing.
- **Pairs well with:** [construction-phase-plan](#construction-phase-plan), [lift-plan](#lift-plan), [permit-to-work](Process-Safety#permit-to-work), [toolbox-talk](Core#toolbox-talk).
