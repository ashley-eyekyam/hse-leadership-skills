# Healthcare

`hse-healthcare` is the healthcare HSE pack — the worker-safety and infection-prevention artifacts of a clinical, care, or laboratory setting, each led by engineering and administrative controls before PPE. It covers transmission-based infection-control plans, laboratory biosafety (risk group / BSL), patient (moving-and-handling) assessment, sharps / needlestick exposure control, workplace-violence prevention, and psychosocial risk assessment. Patient and worker data are de-identified to role labels before drafting.

```
/plugin install hse-healthcare@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### infection-control-plan
- **Produces:** Transmission-based infection prevention and control plan for a named healthcare service or unit.
- **For:** M, C, F · **Grounded in:** CDC Guideline for Isolation Precautions, WHO Core Components of IPC Programmes, Spaulding classification, UK Health and Social Care Act 2008 Hygiene Code, OSHA bloodborne-pathogens confidentiality discipline, and India Bio-Medical Waste Management Rules 2016 via `hse-india` · **Packs:** hse-healthcare.
- **Use when:** A user needs to build or review an infection control plan, write isolation or transmission-based precautions, choose contact/droplet/airborne precautions, decide device reprocessing, or plan de-identified outbreak or HAI surveillance.
- **Don't use for:** Sharps exposure-control plans or lab containment classification; use [sharps-needlestick-management](#sharps-needlestick-management) for sharps and [lab-biosafety-assessment](#lab-biosafety-assessment) for risk-group/BSL decisions.
- **Have ready:** Named service or unit, agent(s) and transmission route(s), patient population, current isolation/ventilation/cohorting controls, device reprocessing needs, de-identified surveillance or outbreak data, jurisdiction, site, output type, action owners, competent IPC reviewer, and review trigger.
- **Trigger:** "a user asks to build", "review an infection control plan", "write an isolation / transmission-based precautions plan".
- **You get:** Standard Precautions baseline, route-correct Transmission-Based precautions, engineering and administrative controls before PPE, Spaulding reprocessing decision, de-identified and aggregated surveillance with small-cell suppression for counts under 5, `[GAP]` items, SMART actions, and IPC competent-person review notes.
- **Pairs well with:** [lab-biosafety-assessment](#lab-biosafety-assessment), [sharps-needlestick-management](#sharps-needlestick-management), [workplace-violence-prevention](#workplace-violence-prevention), [risk-assessment](Core#risk-assessment).

### lab-biosafety-assessment
- **Produces:** Laboratory biosafety risk assessment that determines risk group, biosafety level, containment, and exposure-response controls for a named lab and procedure.
- **For:** M, C, F · **Grounded in:** CDC/NIH BMBL 6th ed, WHO Laboratory Biosafety Manual 4th ed, NIH Guidelines for recombinant/synthetic nucleic acids, UK COSHH 2002 with ACDP hazard groups, OSHA 1910.1030 for human blood/OPIM, and India Bio-Medical Waste Management Rules 2016 via `hse-india` · **Packs:** hse-healthcare.
- **Use when:** A user needs to assess laboratory biosafety, classify a biological agent's risk group, select a biosafety level or biosafety-cabinet class, or review containment for a clinical, diagnostic, research, teaching, or public-health lab.
- **Don't use for:** Healthcare unit infection-control precautions or sharps exposure plans; use [infection-control-plan](#infection-control-plan) for clinical IPC and [sharps-needlestick-management](#sharps-needlestick-management) for bloodborne sharps controls.
- **Have ready:** Named laboratory, specific agent/material, procedure and aerosol/sharps/volume details, known or unknown risk group, current BSL and BSC/containment, staff competence, waste/decontamination route, confidential exposure data scrubbed to role labels, jurisdiction, output type, action owners, and Biological Safety Officer reviewer.
- **Trigger:** "a user asks to assess laboratory biosafety", "classify a biological agent's risk group", "select a biosafety level".
- **You get:** Risk-group determination before BSL selection, `[GAP]` route for unknown or unlisted agents, BSL and BSC/engineering-containment controls before PPE, biosecurity/access controls, confidential exposure-response pathway, de-identified lab-incident data with small-cell suppression for counts under 5, SMART actions, and Biological Safety Officer review notes.
- **Pairs well with:** [infection-control-plan](#infection-control-plan), [sharps-needlestick-management](#sharps-needlestick-management), [chemical-exposure-register](Chemicals#chemical-exposure-register), [risk-assessment](Core#risk-assessment).

### patient-handling-assessment
- **Produces:** Patient handling risk assessment with TILE/SPHM analysis, mobility-and-equipment matrix, and move-toward-zero-manual-lift controls.
- **For:** M, C, F · **Grounded in:** ANA Safe Patient Handling and Mobility Interprofessional National Standards 2nd ed. (2021), NIOSH safe-lifting guidance, ISO/TR 12296:2012, UK Manual Handling Operations Regulations 1992 reg 4 and Schedule 1 TILE, and India ergonomics via `hse-india` · **Packs:** hse-healthcare.
- **Use when:** A user needs to assess patient handling, manual handling of people, moving and handling, hoist transfers, repositioning, lateral transfers, falls recovery, bariatric handling, community care, care-home, ambulance, or ward transfers.
- **Don't use for:** General workplace ergonomics or violence/security risk in care settings; use [ergonomics-assessment](Manufacturing#ergonomics-assessment) for non-patient ergonomics and [workplace-violence-prevention](#workplace-violence-prevention) for aggression risk.
- **Have ready:** Named care task and setting, patient de-identified to mobility/dependency/weight band, whether the manual lift can be avoided, available hoists/slides/boards and equipment SWL, TILE factors, handler competence, worker capability data scrubbed to role labels, jurisdiction, output type, action owners, competent reviewer, and review trigger.
- **Trigger:** "a user asks to assess patient handling", "manual handling of people", "moving and handling".
- **You get:** Avoid-the-manual-lift decision, TILE assessment, mobility-and-equipment matrix, mechanical-aid and safe-system controls before technique/PPE, refusal of manual lift where a suitable mechanical aid is available, bariatric/falls controls where relevant, de-identified injury data with small-cell suppression for counts under 5, SMART actions, and moving-and-handling reviewer notes.
- **Pairs well with:** [risk-assessment](Core#risk-assessment), [ergonomics-assessment](Manufacturing#ergonomics-assessment), [workplace-violence-prevention](#workplace-violence-prevention), [toolbox-talk](Core#toolbox-talk).

### psychosocial-risk-assessment -> see [Operations](Operations#psychosocial-risk-assessment)
Assesses work-related psychosocial hazards for healthcare teams while protecting respondent confidentiality. Full card on the Operations page.

### sharps-needlestick-management
- **Produces:** Sharps-injury prevention package and bloodborne-pathogen exposure-control plan for a named healthcare service.
- **For:** M, C, F · **Grounded in:** OSHA 29 CFR 1910.1030, Needlestick Safety and Prevention Act (PL 106-430, 2000), EU Directive 2010/32/EU, UK Sharps Regulations 2013 with COSHH, and India Bio-Medical Waste Management Rules 2016 via `hse-india` · **Packs:** hse-healthcare.
- **Use when:** A user needs to prevent needlestick or sharps injuries, write or review a bloodborne-pathogen exposure-control plan, build a sharps injury log, evaluate safer devices, set no-recapping rules, or plan post-exposure follow-up.
- **Don't use for:** Broad infection-control precautions or lab BSL classification; use [infection-control-plan](#infection-control-plan) for IPC and [lab-biosafety-assessment](#lab-biosafety-assessment) for lab containment.
- **Have ready:** Named service, sharps inventory and procedures, opportunities to eliminate/substitute sharps, safer-device status, no-recapping/disposal arrangements, de-identified injury log, source-patient and worker exposure details scrubbed to role labels, HBV/PEP pathway inputs, jurisdiction, output type, owners, occupational-health or IPC reviewer, and review trigger.
- **Trigger:** "a user asks to prevent needlestick", "sharps injuries", "review a bloodborne-pathogen exposure control plan".
- **You get:** Elimination/substitution decision, safer-device evaluation, no-recapping and point-of-use disposal controls, PPE as last line, confidential post-exposure/PEP pathway, de-identified and aggregated Sharps Injury Log with small-cell suppression for counts under 5, SMART actions, and competent-person review notes.
- **Pairs well with:** [infection-control-plan](#infection-control-plan), [lab-biosafety-assessment](#lab-biosafety-assessment), [chemical-exposure-register](Chemicals#chemical-exposure-register), [toolbox-talk](Core#toolbox-talk).

### workplace-violence-prevention
- **Produces:** Healthcare workplace-violence-prevention program with worksite hazard analysis, type-1-4 taxonomy, controls, and confidential incident-log structure.
- **For:** M, C, F · **Grounded in:** OSHA Publication 3148 (2016), OSH Act Section 5(a)(1), Cal/OSHA 8 CCR 3342, UK HSE management of work-related violence guidance with NICE NG10, and India occupational-safety provisions via `hse-india` · **Packs:** hse-healthcare.
- **Use when:** A user needs to prevent workplace violence or aggression in healthcare, build a WPV program, assess violence risk in an ED, mental-health, care, ambulance, reception, triage, or lone-working setting, design de-escalation/security controls, or set up incident reporting.
- **Don't use for:** Psychosocial work-design stressors or generic emergency response; use [psychosocial-risk-assessment](Operations#psychosocial-risk-assessment) for work-related stress and [emergency-response-plan](Operations#emergency-response-plan) for emergency procedures.
- **Have ready:** Named service and exposure location/time, violence types in scope, de-identified incident log and records review, walkthrough/staff input, current environmental and administrative controls, de-escalation/response arrangements, post-incident support, jurisdiction, output type, action owners, competent WPV/security reviewer, and review trigger.
- **Trigger:** "a user asks to prevent workplace violence", "aggression in healthcare", "build a WPV program".
- **You get:** Worksite hazard analysis, type-1-4 violence classification, environmental and administrative controls before alarms/self-defence training, de-escalation and response protocol, post-incident support, de-identified and aggregated WPV incident log with small-cell suppression for counts under 5, SMART actions, and competent-person review notes.
- **Pairs well with:** [psychosocial-risk-assessment](Operations#psychosocial-risk-assessment), [emergency-response-plan](Operations#emergency-response-plan), [risk-assessment](Core#risk-assessment), [toolbox-talk](Core#toolbox-talk).
