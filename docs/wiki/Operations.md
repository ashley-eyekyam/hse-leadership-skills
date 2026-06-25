# Operations

`hse-operations` is the cross-sector operations and management-system pack — the artifacts that run an HSE management system in any industry. It covers ISO 45001 gap analysis and certification readiness, ISO 22301 business continuity, the legal / compliance register, regulatory returns, contractor prequalification, emergency-response and site-induction packs, training-needs analysis, and the occupational-health and psychosocial risk assessments. It is a peer of the core pack — install it when your work is the management system itself, not one industry's hazards.

```
/plugin install hse-operations@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### business-continuity-plan
- **Produces:** ISO 22301 business continuity plan with BIA, MTPD/RTO/RPO objectives, continuity strategies, recovery roles, deputies, exercises, and review dates.
- **For:** M, C, E · **Grounded in:** ISO 22301, BIA method, RTO/RPO guidance, hierarchy of controls. · **Packs:** hse-operations.
- **Use when:** A named organisation, site, or function needs a BCP, BIA, disaster-recovery or resilience plan, or recovery objectives for time-critical activities.
- **Don't use for:** Immediate incident response, muster, evacuation, call-out trees, or drills; use [emergency-response-plan](Operations#emergency-response-plan) for the ERP leg.
- **Have ready:** Named organisation/site/function, critical activities and outputs, disruption scenarios, current recovery capability, dependencies, any MTPD/RTO/RPO basis, recovery role owners/deputies, evidence such as prior BIAs, DR runbooks, dependency maps, SLAs, backup logs, and exercise reports.
- **Trigger:** "a user asks to write a business continuity plan", "resilience plan", "to set RTO/RPO recovery objectives".
- **You get:** BIA summary, critical-activity dependency map, MTPD/RTO/RPO rationale, continuity strategies, recovery role register with deputies, exercise/test schedule, review dates, gaps, and owned actions.
- **Pairs well with:** [emergency-response-plan](Operations#emergency-response-plan) for incident response before continuity recovery, and [iso45001-gap-analysis](Operations#iso45001-gap-analysis) for management-system readiness.

### construction-phase-plan -> see [Construction](Construction#construction-phase-plan)
Creates or reviews a CDM 2015 Construction Phase Plan, so it appears here for management-system users who manage construction projects. Full card on the Construction page.

### contractor-prequalification
- **Produces:** Risk-tiered contractor PQQ and evidence-based approve/conditional/reject scorecard for a named contractor scope.
- **For:** M, C · **Grounded in:** ISO 45001 clause 8.1.4, contractor tier map, evidence-anchored PQQ bank, hierarchy of controls. · **Packs:** hse-operations.
- **Use when:** You need to prequalify, vet, approve, re-approve, or score a contractor/subcontractor for a specific work package and site.
- **Don't use for:** Writing the construction pre-start plan itself; use [construction-phase-plan](Construction#construction-phase-plan) for a CPP, or [induction-pack](Operations#induction-pack) for post-approval site induction.
- **Have ready:** Work scope and highest-risk activities, named contractor and site, affected parties, evidence supplied or missing, required accreditations/permits/client rules, jurisdiction and state where relevant, decision type, scoring threshold, decision owner, and review cadence.
- **Trigger:** "a user asks to prequalify", "approve a contractor", "build a PQQ".
- **You get:** Risk tier, tailored PQQ, evidence register, verified/unverified gap log, score rationale, approve/conditional/reject recommendation, named conditions, owners, and review dates.
- **Pairs well with:** [induction-pack](Operations#induction-pack) for approved contractor onboarding and [legal-compliance-register](Operations#legal-compliance-register) for applicable contractor obligations.

### emergency-response-plan
- **Produces:** Scenario-keyed emergency response plan with call-out tree, muster/evacuation arrangements, response procedures, drill schedule, and external-responder interface.
- **For:** M, C, F · **Grounded in:** ISO 45001 clause 8.2, ERP scenario catalogue, drill-frequency guidance, hierarchy of controls, jurisdiction-specific ERP fragments. · **Packs:** hse-marine-offshore, hse-operations, hse-utilities-power.
- **Use when:** A named site or facility needs an emergency plan, evacuation plan, crisis-response procedure, scenario response, call-out tree, muster arrangement, or drill schedule.
- **Don't use for:** Continuity of critical activities after the emergency is controlled; use [business-continuity-plan](Operations#business-continuity-plan). Use [mine-rescue-erp](Mining#mine-rescue-erp) for mining rescue and [marine-emergency-response](Marine-Offshore#marine-emergency-response) for offshore/marine emergencies.
- **Have ready:** Named site/facility, occupancy and shifts, credible scenarios, site-specific scenario details, on-site response capability, external responder access, isolation points, muster locations, emergency roles and deputies, jurisdiction/state where relevant, drill history, and review cadence.
- **Trigger:** "a user asks to write", "review an emergency plan", "evacuation plan".
- **You get:** Scenario list, prevention-first controls, response procedures, role/deputy register, call-out and muster arrangements, responder interface sheet, dated drill plan, gaps, and owned actions.
- **Pairs well with:** [business-continuity-plan](Operations#business-continuity-plan) for recovery after response and [induction-pack](Operations#induction-pack) to teach site emergency arrangements.

### health-risk-assessment
- **Produces:** Occupational-health risk assessment with SEG definition, cited OEL/WEL/PEL comparison, ergonomics outputs when selected, controls, and surveillance schedule.
- **For:** M, C, F · **Grounded in:** ISO 45001 clause 6.1.2, OEL/exposure-limit data, RULA/REBA/NIOSH ergonomics methods, surveillance-trigger method, hierarchy of controls. · **Packs:** hse-manufacturing, hse-operations.
- **Use when:** Named tasks or roles need assessment for chemical, noise, vibration, ergonomic, thermal, biological, exposure-monitoring, SEG, OEL, or health-surveillance questions.
- **Don't use for:** Individual clinical diagnosis or occupational-health treatment; route individual medical concerns to a competent OH professional, and use [psychosocial-risk-assessment](Operations#psychosocial-risk-assessment) for work-related stress and psychosocial hazards.
- **Have ready:** Hazard type, named tasks/roles and SEGs, exposure data or monitoring gap, OEL source, ergonomics tool inputs if relevant, jurisdiction/state, sector, site/process, exposed population, existing controls and surveillance, report audience, competent assessor, action owners, and review cycle.
- **Trigger:** "a user asks to assess occupational-health risk", "chemical/noise/vibration/ergonomic exposure", "build similar-exposure groups".
- **You get:** SEG register, exposure basis, cited OEL comparison or monitoring-first gap, ergonomics score blocks where selected, initial/residual health risk, hierarchy-ranked controls, OEL-linked surveillance schedule, and SMART action plan.
- **Pairs well with:** [training-needs-analysis](Operations#training-needs-analysis) for competence gaps and [psychosocial-risk-assessment](Operations#psychosocial-risk-assessment) for work-design mental-health risks.

### induction-pack
- **Produces:** Site-specific induction delivery pack with competence-verification record and role-risk refresher schedule.
- **For:** M, C, F · **Grounded in:** ISO 45001 clauses 7.2 and 7.3, induction baseline, competence-level scale, hierarchy of controls, jurisdiction-specific induction duties. · **Packs:** hse-operations.
- **Use when:** A named site, project, asset, visitor group, new-starter group, or contractor cohort needs a safety induction, orientation pack, onboarding briefing, sign-off record, or refresher plan.
- **Don't use for:** A single pre-task briefing; use [toolbox-talk](Core#toolbox-talk). Use [training-needs-analysis](Operations#training-needs-analysis) for a role-by-competence training matrix.
- **Have ready:** Audience/cohort and roles, named site/project/asset, sector and physical environment, site rules, emergency/muster arrangements, first aid/welfare, traffic/PTW/site hazards, evidence sources, delivery mode, jurisdiction/state, verification method, induction owner, role verification level, and refresher cadence.
- **Trigger:** "a user asks to build a site induction", "contractor induction", "orientation pack".
- **You get:** Site-specific induction topics, hazard/control content, emergency and welfare briefing, site rules, delivery pack, verification/sign-off record, role-based competence level, refresher schedule, and gaps where site details are missing.
- **Pairs well with:** [contractor-prequalification](Operations#contractor-prequalification) before contractor induction and [emergency-response-plan](Operations#emergency-response-plan) for emergency arrangements used in the pack.

### iso45001-gap-analysis
- **Produces:** Clause-by-clause ISO 45001 certification-readiness gap analysis with maturity scoring and costed remediation roadmap.
- **For:** M, C, E · **Grounded in:** ISO 45001 clause set 4-10, ISO 14001/ISO 45003 selectors, ISO/IEC 17021-1 audit principles, 5-level maturity scale, gap-prioritisation method, hierarchy of controls. · **Packs:** hse-operations.
- **Use when:** A named organisation/site needs ISO 45001, ISO 14001, ISO 45003, or combined management-system gap analysis, maturity scoring, surveillance prep, or certification readiness assessment.
- **Don't use for:** A scoped inspection/audit finding list; use [safety-audit](Core#safety-audit). Use [legal-compliance-register](Operations#legal-compliance-register) for legal-register obligations under clause 6.1.3.
- **Have ready:** Standard selector, named organisation/site and boundary, sector, site scope, current certification state, evidence by clause group, flagged obligations or mandatory clauses, assessment target, scoring scale, jurisdiction context, competent assessor, remediation owners, and target review/certification date.
- **Trigger:** "a user asks to assess ISO 45001 readiness", "run a gap analysis against ISO 45001", "check management-system conformance".
- **You get:** Clause map, evidence register, 0-4 conformance scores, certification blockers, prioritised gaps, N/A rationales, hierarchy-ranked planning controls, costed SMART remediation roadmap, owners, due dates, and readiness summary.
- **Pairs well with:** [hse-policy-generator](Leadership#hse-policy-generator) for clause 5.2 policy, [legal-compliance-register](Operations#legal-compliance-register) for clauses 6.1.3/9.1.2, and [training-needs-analysis](Operations#training-needs-analysis) for clause 7.2 gaps.

### legal-compliance-register
- **Produces:** Multi-jurisdiction HSE legal and other-requirements compliance register with applicability, evidence, gaps, owners, and review dates.
- **For:** M, C, E · **Grounded in:** ISO 45001 clauses 6.1.3 and 9.1.2, legal-register method, obligation-family lookup, UK/USA/EU regulatory fragments, India hse-india state-detection route. · **Packs:** hse-operations.
- **Use when:** A named organisation/site needs a legal register, obligation register, applicable-legislation list, compliance evaluation, ISO 45001 6.1.3 evidence, due-diligence register, or M&A HSE legal review.
- **Don't use for:** Preparing a statutory incident return or periodic filing; use [regulatory-returns](Operations#regulatory-returns). For India obligations, this card defers to hse-india after mandatory state detection and does not hard-code a national form number.
- **Have ready:** Jurisdiction(s), Indian state if India is in scope, named organisation/site, activities and hazard profile, register purpose, existing register state, compliance evidence, obligation owners, and review cycle.
- **Trigger:** "a user asks to build a legal register", "compliance obligations register", "applicable-legislation list".
- **You get:** Jurisdiction-grouped obligation rows, applicability rationales, inapplicable exclusions, compliance-evidence cells, gap status, owner/review-date cells, India deferral note where relevant, and SMART actions for gaps.
- **Pairs well with:** [regulatory-returns](Operations#regulatory-returns) for statutory filings and [iso45001-gap-analysis](Operations#iso45001-gap-analysis) for management-system conformance.

### psychosocial-risk-assessment
- **Produces:** ISO 45003 / HSE Management Standards psychosocial risk assessment with work-design hazards, triangulated ratings, controls, confidentiality safeguards, and action plan.
- **For:** M, C, E · **Grounded in:** ISO 45003, UK HSE Management Standards, psychosocial indicator bands, ISO 45001 clause 6.1.2, risk_matrix, hierarchy of controls. · **Packs:** hse-healthcare, hse-operations.
- **Use when:** A named team, role, or function needs assessment of work-related stress, psychosocial hazards, burnout, workload, work design, or ISO 45003/HSE Management Standards domains.
- **Don't use for:** Individual clinical diagnosis or naming a person as the risk; route individual cases to a competent OH professional. Use [health-risk-assessment](Operations#health-risk-assessment) for chemical, noise, vibration, ergonomic, or other occupational-health exposure.
- **Have ready:** Named unit or sampling plan, psychosocial domains, at least two data sources, confidentiality threshold, known triggers, exposed group labels, jurisdiction/state, rating scale, report reader, competent assessor, action owners, and review cycle.
- **Trigger:** "a user asks to assess psychosocial risk", "work-related stress", "mental-health hazards".
- **You get:** Confidentiality statement, data-source coverage check, domain findings, work-design hazard descriptions, risk ratings, hierarchy-ranked organisational controls, residual risk, SMART action plan, and suppression of small or identifying cells.
- **Pairs well with:** [safety-culture-assessment](Leadership#safety-culture-assessment) for culture-level diagnosis and [hse-policy-generator](Leadership#hse-policy-generator) for psychosocial policy commitments.

### regulatory-returns
- **Produces:** Recordability/reportability determination and de-identified statutory return package with form, deadline, and evidence trail.
- **For:** M, C, F · **Grounded in:** OSHA 29 CFR 1904, UK RIDDOR 2013, EU member-state equivalents, recordability-test data, returns method, India hse-india state-detection route. · **Packs:** hse-operations.
- **Use when:** A named organisation needs to determine whether an incident is OSHA-recordable, RIDDOR-reportable, electronically submittable, due in a periodic return, or requires a jurisdiction-specific statutory filing.
- **Don't use for:** A standing legal obligations register; use [legal-compliance-register](Operations#legal-compliance-register). For India returns or accident notices, this card defers entirely to hse-india after mandatory state detection and does not hard-code a national form number.
- **Have ready:** Jurisdiction, Indian state if India is in scope, return type, incident facts, work-relatedness and outcome details, days away/restricted, treatment level, organisation size/SIC, reporting period, preparer role, and follow-up action owner.
- **Trigger:** "a user asks which incidents are recordable", "how to complete OSHA 300/300A/301", "whether something is RIDDOR-reportable".
- **You get:** Cited recordability/reportability verdict, correct form or routed India gap, deadline, de-identified return fields, evidence trail, missing-fact gaps, and owned follow-up actions.
- **Pairs well with:** [legal-compliance-register](Operations#legal-compliance-register) for the obligation register and [hse-annual-esg-report](Leadership#hse-annual-esg-report) for annual OH&S disclosure inputs.

### training-needs-analysis
- **Produces:** Role-by-competence Training Needs Analysis with matrix, gap scoring, SPOF and expiry flags, and costed training plan.
- **For:** M, C, F · **Grounded in:** ISO 45001 clauses 7.2 and 7.3, competence-level scale, TNA method, hierarchy of controls, jurisdiction-specific legal competence duties. · **Packs:** hse-operations.
- **Use when:** A named site, function, project, or cohort needs training-gap analysis, a competence/training matrix, role-to-competence mapping, certification expiry tracking, refresher planning, or a costed training programme.
- **Don't use for:** Site-awareness delivery content; use [induction-pack](Operations#induction-pack). Do not use it to treat a hazard with "more training" alone when higher-order controls are available.
- **Have ready:** Scope, named roles and headcounts, competence sources, known current competence, TNA driver, sector, site/asset, jurisdiction/state, legal-required competencies, competence scale, analysis owner, action owners, review cadence, and optional budget/time envelope.
- **Trigger:** "a user asks to identify training gaps", "build a competence", "training matrix".
- **You get:** Role x competence matrix, current/required level gaps, statutory competence flags, single-point-of-failure risks, expiry/refresher tracker, prioritised costed training plan, and SMART actions with owners and due dates.
- **Pairs well with:** [induction-pack](Operations#induction-pack) for awareness/induction and [iso45001-gap-analysis](Operations#iso45001-gap-analysis) for clause 7.2/7.3 readiness gaps.
