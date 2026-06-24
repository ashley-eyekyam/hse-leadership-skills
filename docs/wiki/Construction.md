# Construction

`hse-construction` is the construction pack — the CDM-2015 lifecycle plus the everyday site artifacts. It covers the Pre-Construction Information pack, the Construction Phase Plan, the Health and Safety File, lift plans (LOLER 1998 / BS 7121), traffic-management plans, permits-to-work, India BOCW compliance, and the construction-grade risk assessment and toolbox talk reused from the core pack.

```
/plugin install hse-construction@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### bocw-compliance
- **Produces:** Assess India BOCW (Building & Other Construction Workers) statutory compliance for a named construction establishment: establishment registration, the 1% welfare cess, the Form XXV annual return (by 15 Feb), Safety Officer / Safety Committee thresholds, and accident notification — grounded in KB-REG-IN-BOCW with MANDATORY state detection.
- **For:** M, C · **Packs:** hse-construction, hse-india · **Version:** 1.0 · **Jurisdiction:** IN
- **Trigger:** "Assess India BOCW (Building & Other Construction Workers) statutory compliance for a named construction establishment: establishment registration"; "the 1% welfare cess"; "the Form XXV annual return (by 15 Feb)"
- **Summary:** Assess India BOCW (Building & Other Construction Workers) statutory compliance for a named construction establishment: establishment registration, the 1% welfare cess, the Form XXV annual return (by 15 Feb), Safety Officer / Safety Committee thresholds, and accident notification — grounded in KB-REG-IN-BOCW with MANDATORY state detection. Use it to produce a BOCW compliance gap-list for a site in a given state, resolve which Welfare Board return is filed and when, and flag the OSH-Code (BOCW subsumed) transition. State detection is mandatory; state-specific values resolve from the KB row or are [GAP]-flagged, never invented; no hard-coded national form. Decision-support only; a competent person must review the output.

### construction-phase-plan
- **Produces:** Produces a consultant-grade, risk-proportionate CDM 2015 Construction Phase Plan (CPP) for a named construction project.
- **For:** M, C, F · **Packs:** hse-construction, hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review a Construction Phase Plan"; "a CPP"
- **Summary:** Produces a consultant-grade, risk-proportionate CDM 2015 Construction Phase Plan (CPP) for a named construction project. Use this skill whenever a user asks to build, write, or review a Construction Phase Plan, a CPP, a CDM 2015 Regulation 12 plan, or the principal contractor's pre-start plan. Forces project specificity (refuses 'a building site' — needs the named project, at least one significant activity, and the contractor configuration), sets out management & arrangements, site rules, and significant risks & controls by activity ranked by the hierarchy of controls (work at height leads with collective protection, never PPE), states the F10 / Reg 12 notification duty for a notifiable project, and cross-references the wider CDM document chain (Pre-Construction Information and the Health & Safety File). Grounded in CDM 2015 Reg 12 + HSE L153 in the UK, or 29 CFR 1926 Subpart C in the USA; India BOCW defers to hse-india with state detection. Decision-support only; a competent person must review the output.

### health-safety-file
- **Produces:** Produces a CDM 2015 Health and Safety File for a named completed (or near-complete) construction project — the as-built residual-risk record handed to the client for future construction, maintenance, cleaning, refurbishment, and demolition.
- **For:** M, C · **Packs:** hse-construction · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review a health and safety file"; "an H&S file"
- **Summary:** Produces a CDM 2015 Health and Safety File for a named completed (or near-complete) construction project — the as-built residual-risk record handed to the client for future construction, maintenance, cleaning, refurbishment, and demolition. Use this skill whenever a user asks to compile, write, or review a health and safety file, an H&S file, a CDM completion file, or the residual-risk handover information for a structure. It captures the as-built information, the residual and unusual hazards a future worker could not reasonably anticipate, the location of services and hazardous materials, and the cleaning/maintenance safety arrangements — emitting a branded report. Grounded in CDM 2015 Regulation 12(5)–(9). Decision-support only; a competent person must review the output.

### lift-plan
- **Produces:** Creates consultant-grade, site- and lift-specific lifting plans grounded in LOLER 1998 Reg 8 and BS 7121.
- **For:** M, C, F · **Packs:** hse-construction · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review a lifting plan"; "a crane lift plan"
- **Summary:** Creates consultant-grade, site- and lift-specific lifting plans grounded in LOLER 1998 Reg 8 and BS 7121. Use this skill whenever a user asks to plan, build, or review a lifting plan, a crane lift plan, or a lifting operation, to classify a lift as basic / standard / complex per BS 7121, to confirm a crane's SWL at radius and utilisation against the manufacturer's rated-capacity chart, to set exclusion zones near overhead power lines / structures / the public, to sequence a lift method with appointed-person / operator / slinger roles, or to set contingency and abort criteria. Reads SWL-at-radius and utilisation from the rated-capacity chart (transcribed, checked) — never computed. Refuses to plan without a confirmed load weight (incl. rigging), an equipment SWL at the working radius, and at least an appointed person. Enforces the hierarchy of controls (eliminate the lift / reduce the load / engineer an exclusion before PPE) and re-scores residual risk. Decision-support only; competent-person review required.

### permit-to-work
- **Produces:** Produces a permit-to-work package for a named high-risk task (hot work, confined-space entry, line breaking, excavation, working at height) with a dedicated SIMOPS (simultaneous operations) coordination section: it detects concurrent operations in the intake and routes them to permit and coordination controls, applies the hierarchy of controls to every isolation and safeguard, and tracks the permit conditions and actions to closure.
- **For:** M, C · **Packs:** hse-construction, hse-manufacturing, hse-marine-offshore, hse-process · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Produces a permit-to-work package for a named high-risk task (hot work"; "confined-space entry"; "line breaking"
- **Summary:** Produces a permit-to-work package for a named high-risk task (hot work, confined-space entry, line breaking, excavation, working at height) with a dedicated SIMOPS (simultaneous operations) coordination section: it detects concurrent operations in the intake and routes them to permit and coordination controls, applies the hierarchy of controls to every isolation and safeguard, and tracks the permit conditions and actions to closure. SIMOPS is handled as a permit/coordination control within this skill, never as a separate workflow. Decision-support only; a competent person must review the output.

### pre-construction-information
- **Produces:** Produces a Pre-Construction Information (PCI) pack for a named construction project under CDM 2015 — the pre-tender hazard and information set the client must provide to every designer and contractor.
- **For:** M, C · **Packs:** hse-construction · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review pre-construction information"; "a PCI pack"
- **Summary:** Produces a Pre-Construction Information (PCI) pack for a named construction project under CDM 2015 — the pre-tender hazard and information set the client must provide to every designer and contractor. Use this skill whenever a user asks to compile, write, or review pre-construction information, a PCI pack, CDM pre-tender information, or the client's health-and-safety information for a project. It assembles the project, site, and existing-structure hazard information (asbestos, buried services, ground conditions, adjacent occupancies, existing H&S file content), states what is known versus a documented information gap, and emits a branded report that feeds the construction phase plan. Grounded in CDM 2015 Regulation 4. Decision-support only; a competent person must review the output.

### risk-assessment
- **Produces:** Creates consultant-grade, task- and site-specific risk assessments (HIRA / HIRARC).
- **For:** M, C, F · **Packs:** hse-construction, hse-core · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess risk"; "review a risk assessment"; "perform a hazard identification and risk assessment"
- **Summary:** Creates consultant-grade, task- and site-specific risk assessments (HIRA / HIRARC). Use this skill whenever a user asks to assess risk, build or review a risk assessment, perform a hazard identification and risk assessment, score likelihood and severity on a risk matrix, select or rank controls by the hierarchy of controls, or produce a HIRA, HIRARC, or risk register for a specific task, activity, site, or asset. Optionally assesses environmental aspects and impacts (ISO 14001 clause 6.1.2) when the user asks for an environmental risk or aspects/impacts assessment. Grounds the assessment in ISO 45001 clause 6.1.2 (and ISO 14001 6.1.2 for environmental scope), enforces the hierarchy of controls (no PPE-only treatments without justification), re-scores residual risk after controls, and assigns SMART corrective actions with named owners and due dates — emitting a branded report. Decision-support only; a competent person must review the output.

### toolbox-talk
- **Produces:** Produces a short, ready-to-deliver toolbox talk (a pre-task safety briefing / tailgate / pre-start / take-5 / safety moment) plus a sign-off / attendance sheet for a specific crew, task, and site.
- **For:** F, M · **Packs:** hse-construction, hse-core · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Produces a short"; "ready-to-deliver toolbox talk (a pre-task safety briefing / tailgate / pre-start / take-5 / safety moment) plus a sign-off / attendance sheet for a specific crew"; "and site"
- **Summary:** Produces a short, ready-to-deliver toolbox talk (a pre-task safety briefing / tailgate / pre-start / take-5 / safety moment) plus a sign-off / attendance sheet for a specific crew, task, and site. It runs a quick structured intake, grounds the talk in the named task's real hazards and the hierarchy of controls, references a recent relevant incident or near-miss (de-identified, or a clearly-labelled typical example — never a fabricated local event), and gives the supervisor discussion prompts and key takeaways the crew can act on today. Use it for daily / shift safety briefings, tailgate talks, pre-job briefs, and topic safety moments — not for full risk assessments or incident investigations. Decision-support only; a competent person must review the output.

### traffic-management-plan
- **Produces:** Produces a construction traffic management plan for a named site — vehicle and pedestrian routing, segregation, loading/delivery and reversing controls, and the site-access and public-interface arrangements.
- **For:** M, C, F · **Packs:** hse-construction · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review a traffic management plan"; "a TMP"
- **Summary:** Produces a construction traffic management plan for a named site — vehicle and pedestrian routing, segregation, loading/delivery and reversing controls, and the site-access and public-interface arrangements. Use this skill whenever a user asks to write or review a traffic management plan, a TMP, a site traffic plan, vehicle-pedestrian segregation, or construction logistics/access controls for a specific site. It separates people from vehicles by design (one-way systems, segregated routes, eliminating reversing), controls deliveries and the public interface, sets speed and signage rules, and applies the hierarchy of controls — emitting a branded report. Grounded in CDM 2015 Regulation 27 and Schedule 3. Decision-support only; a competent person must review the output.
