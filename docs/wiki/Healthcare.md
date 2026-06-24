# Healthcare

`hse-healthcare` is the healthcare HSE pack — the worker-safety and infection-prevention artifacts of a clinical, care, or laboratory setting, each led by engineering and administrative controls before PPE. It covers transmission-based infection-control plans, laboratory biosafety (risk group / BSL), patient (moving-and-handling) assessment, sharps / needlestick exposure control, workplace-violence prevention, and psychosocial risk assessment. Patient and worker data are de-identified to role labels before drafting.

```
/plugin install hse-healthcare@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### infection-control-plan
- **Produces:** Produces a consultant-grade, transmission-based infection prevention and control (IPC) plan for a named healthcare service or unit, driven by the engineering-and-administrative-controls-before-PPE hierarchy.
- **For:** M, C, F · **Packs:** hse-healthcare · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review an infection control plan"; "write an isolation / transmission-based precautions plan"
- **Summary:** Produces a consultant-grade, transmission-based infection prevention and control (IPC) plan for a named healthcare service or unit, driven by the engineering-and-administrative-controls-before-PPE hierarchy. Use this skill when a user asks to build or review an infection control plan, write an isolation / transmission-based precautions plan, select contact / droplet / airborne precautions for a ward or care home, decide device reprocessing by Spaulding classification, or plan de-identified outbreak / HAI surveillance. It forces Standard Precautions for every patient and the route-correct precautions, leads with engineering controls (ventilation, negative-pressure isolation rooms) and administrative controls (cohorting, screening) BEFORE PPE, applies the Spaulding reprocessing decision, and refuses a PPE-only plan (an airborne agent on a respirator alone, no isolation room). Grounded in the CDC isolation guideline + WHO IPC core components + Spaulding. Decision-support only; a competent person must review.

### lab-biosafety-assessment
- **Produces:** Produces a consultant-grade laboratory biosafety risk assessment for a named lab and procedure, determining the agent risk group (RG1-RG4) and biosafety level (BSL-1-BSL-4) with engineering containment before PPE.
- **For:** M, C, F · **Packs:** hse-healthcare · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess laboratory biosafety"; "classify a biological agent's risk group"; "select a biosafety level"
- **Summary:** Produces a consultant-grade laboratory biosafety risk assessment for a named lab and procedure, determining the agent risk group (RG1-RG4) and biosafety level (BSL-1-BSL-4) with engineering containment before PPE. Use this skill whenever a user asks to assess laboratory biosafety, classify a biological agent's risk group, select a biosafety level or biosafety-cabinet class, or write or review a biosafety assessment for a clinical, research, or diagnostic lab handling an infectious agent, recombinant material, or human blood/OPIM. It classifies the risk group first, then selects the BSL with primary containment (cabinet class, airflow, decontamination) before PPE; a respirator-and-gloves plan with no containment is flagged, and an unknown risk group emits [GAP] rather than being invented. Specimen-source-patient and worker health data are scrubbed to role labels before drafting. Grounded in CDC/NIH BMBL 6th ed and WHO Laboratory Biosafety Manual. Decision-support only; a Biological Safety Officer must review.

### patient-handling-assessment
- **Produces:** Produces a consultant-grade moving-and-handling-of-people (patient handling) risk assessment for a named care task — a TILE/SPHM assessment with a mobility-and-equipment matrix and a move-toward-zero-manual-lift control plan.
- **For:** M, C, F · **Packs:** hse-healthcare · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess patient handling"; "manual handling of people"; "moving and handling"
- **Summary:** Produces a consultant-grade moving-and-handling-of-people (patient handling) risk assessment for a named care task — a TILE/SPHM assessment with a mobility-and-equipment matrix and a move-toward-zero-manual-lift control plan. Use this skill whenever a user asks to assess patient handling, manual handling of people, moving and handling, or a hoist / transfer / repositioning / bariatric handling risk assessment on a ward, in a care home, in community care, or in an ambulance. It avoids hazardous manual handling first (substitute a hoist for a lift), assesses the residual with the MHOR Schedule 1 TILE filter (Task, Individual, Load, Environment), ranks controls up the hierarchy (eliminate the manual lift -> mechanical aids -> safe systems -> technique/PPE last), and refuses a manual lift where a mechanical aid is available. The patient is de-identified to mobility / dependency / weight band. Grounded in ANA SPHM (2021), NIOSH, ISO/TR 12296, and UK MHOR 1992. Decision-support only; a competent person must review.

### psychosocial-risk-assessment
- **Produces:** Produces a consultant-grade psychosocial risk assessment for a named team, role, or function — identifying work-related psychosocial hazards and recommending work-design controls.
- **For:** M, C, E · **Packs:** hse-healthcare, hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess psychosocial risk"; "work-related stress"; "mental-health hazards"
- **Summary:** Produces a consultant-grade psychosocial risk assessment for a named team, role, or function — identifying work-related psychosocial hazards and recommending work-design controls. Use this skill whenever a user asks to assess psychosocial risk, work-related stress, mental-health hazards, burnout, or workload/work-design risks, or to apply ISO 45003 or the HSE Management Standards. It assesses the hazard at source (work design, not the individual), prioritises organisational controls over individual resilience training, protects respondent confidentiality, and assigns owners and dates — emitted as a branded report. Decision-support only; a competent person must review the output.

### sharps-needlestick-management
- **Produces:** Produces a consultant-grade sharps-injury prevention package and exposure-control plan for a named healthcare service, driven by the engineering-control-first hierarchy.
- **For:** M, C, F · **Packs:** hse-healthcare · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "prevent needlestick"; "sharps injuries"; "review a bloodborne-pathogen exposure control plan"
- **Summary:** Produces a consultant-grade sharps-injury prevention package and exposure-control plan for a named healthcare service, driven by the engineering-control-first hierarchy. Use this skill whenever a user asks to prevent needlestick or sharps injuries, write or review a bloodborne-pathogen exposure control plan, build a sharps injury log, evaluate safer devices, set a no-recapping rule, or plan post-exposure follow-up for a clinic, ward, lab, dental practice, or ambulance. It forces the engineering-control-first hierarchy (eliminate unnecessary sharps -> safety-engineered devices -> no-recapping / safe-disposal -> PPE last), records the de-identified OSHA Sharps Injury Log, and builds a confidential source-testing / PEP pathway (source patient and worker by role only). It refuses a behaviour-led "be careful" treatment where a sharp could be eliminated or engineered out. Grounded in OSHA 1910.1030 + the Needlestick Act and EU Directive 2010/32/EU. Decision-support only; a competent person must review.

### workplace-violence-prevention
- **Produces:** Produces a consultant-grade workplace-violence-prevention (WPV) program for a named healthcare service — the worksite hazard analysis, the type-1-4 violence taxonomy, environmental and administrative controls, and the confidential incident log.
- **For:** M, C, F · **Packs:** hse-healthcare · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "prevent workplace violence"; "aggression in healthcare"; "build a WPV program"
- **Summary:** Produces a consultant-grade workplace-violence-prevention (WPV) program for a named healthcare service — the worksite hazard analysis, the type-1-4 violence taxonomy, environmental and administrative controls, and the confidential incident log. Use this skill whenever a user asks to prevent workplace violence or aggression in healthcare, build a WPV program or plan, assess violence risk in an ED / mental-health / care setting, design de-escalation or security controls, or set up violence incident reporting. It leads with environmental and administrative design (controlled access, sightlines, alarms / duress, staffing, lone-working) before reactive measures, classifies violence by source (type 1 criminal -> type 4 personal), and records a de-identified worksite analysis with small-cell suppression. It refuses a program headlined by "personal alarms / self-defence training" alone. Grounded in OSHA 3148 + §5(a)(1) and Cal/OSHA 8 CCR 3342. Decision-support only; review by a competent person.
