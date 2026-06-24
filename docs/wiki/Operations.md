# Operations

`hse-operations` is the cross-sector operations and management-system pack — the artifacts that run an HSE management system in any industry. It covers ISO 45001 gap analysis and certification readiness, ISO 22301 business continuity, the legal / compliance register, regulatory returns, contractor prequalification, emergency-response and site-induction packs, training-needs analysis, and the occupational-health and psychosocial risk assessments. It is a peer of the core pack — install it when your work is the management system itself, not one industry's hazards.

```
/plugin install hse-operations@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### business-continuity-plan
- **Produces:** Produces an ISO 22301 business continuity plan for a named organisation — business impact analysis, recovery objectives (RTO/RPO/MTPD), continuity strategies, and a plan with named recovery roles.
- **For:** M, C, E · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "write a business continuity plan"; "resilience plan"; "to set RTO/RPO recovery objectives"
- **Summary:** Produces an ISO 22301 business continuity plan for a named organisation — business impact analysis, recovery objectives (RTO/RPO/MTPD), continuity strategies, and a plan with named recovery roles. Use this skill whenever a user asks to write a business continuity plan, BCP, BIA, disaster-recovery or resilience plan, or to set RTO/RPO recovery objectives. It runs a BIA to find time-critical activities and their dependencies, derives RTO/RPO within the MTPD (RTO < MTPD, never asserted alone), selects continuity strategies, and documents the plan with named owners, deputies, and review dates — emitted as a branded report. It complements (not duplicates) the emergency-response-plan: ERP handles the incident response; BCP handles continuity of critical activities. Decision-support only; a competent person must review the output.

### construction-phase-plan
- **Produces:** Produces a consultant-grade, risk-proportionate CDM 2015 Construction Phase Plan (CPP) for a named construction project.
- **For:** M, C, F · **Packs:** hse-construction, hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review a Construction Phase Plan"; "a CPP"
- **Summary:** Produces a consultant-grade, risk-proportionate CDM 2015 Construction Phase Plan (CPP) for a named construction project. Use this skill whenever a user asks to build, write, or review a Construction Phase Plan, a CPP, a CDM 2015 Regulation 12 plan, or the principal contractor's pre-start plan. Forces project specificity (refuses 'a building site' — needs the named project, at least one significant activity, and the contractor configuration), sets out management & arrangements, site rules, and significant risks & controls by activity ranked by the hierarchy of controls (work at height leads with collective protection, never PPE), states the F10 / Reg 12 notification duty for a notifiable project, and cross-references the wider CDM document chain (Pre-Construction Information and the Health & Safety File). Grounded in CDM 2015 Reg 12 + HSE L153 in the UK, or 29 CFR 1926 Subpart C in the USA; India BOCW defers to hse-india with state detection. Decision-support only; a competent person must review the output.

### contractor-prequalification
- **Produces:** Produces a risk-tiered contractor prequalification questionnaire (PQQ) and an evidence-based scoring/evaluation of a contractor's HSE capability for a named scope of work.
- **For:** M, C · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "approve a contractor"; "build a PQQ"
- **Summary:** Produces a risk-tiered contractor prequalification questionnaire (PQQ) and an evidence-based scoring/evaluation of a contractor's HSE capability for a named scope of work. Use this skill whenever a user asks to prequalify, vet, or approve a contractor or subcontractor, build a PQQ or contractor-approval questionnaire, score a contractor's safety credentials, or set up contractor HSE management. It tiers the rigour to the work's risk, asks for verifiable evidence (not claims), scores against defined criteria, and produces an approve/conditional/reject recommendation with named conditions and review dates — emitted as a branded report. Decision-support only; a competent person must review the output.

### emergency-response-plan
- **Produces:** Produces a scenario-keyed emergency response plan (ERP) for a named site or facility — call-out tree, muster and evacuation arrangements, scenario response procedures, drill schedule, and external-responder integration.
- **For:** M, C, F · **Packs:** hse-marine-offshore, hse-operations, hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review an emergency plan"; "evacuation plan"
- **Summary:** Produces a scenario-keyed emergency response plan (ERP) for a named site or facility — call-out tree, muster and evacuation arrangements, scenario response procedures, drill schedule, and external-responder integration. Use this skill whenever a user asks to write or review an emergency plan, evacuation plan, emergency procedures, crisis-response plan, or to plan emergency drills for a specific location. It grounds the plan in the site's credible emergency scenarios and the hierarchy of controls (prevention before response), assigns named roles with deputies, and schedules drills — emitted as a branded report. For continuity of critical activities after the emergency is controlled (RTO/RPO/MTPD) use business-continuity-plan; for mine-rescue-specific arrangements use mine-rescue-erp; for offshore use the marine-emergency-response skill. Decision-support only; a competent person must review the output.

### health-risk-assessment
- **Produces:** Produces an occupational-health risk assessment for named tasks or roles — similar-exposure-group definition, hazard-to-OEL comparison, ergonomic scoring (RULA/REBA/NIOSH), and a health-surveillance schedule.
- **For:** M, C, F · **Packs:** hse-manufacturing, hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess occupational-health risk"; "chemical/noise/vibration/ergonomic exposure"; "build similar-exposure groups"
- **Summary:** Produces an occupational-health risk assessment for named tasks or roles — similar-exposure-group definition, hazard-to-OEL comparison, ergonomic scoring (RULA/REBA/NIOSH), and a health-surveillance schedule. Use this skill whenever a user asks to assess occupational-health risk, chemical/noise/vibration/ergonomic exposure, build similar-exposure groups, compare exposures to OELs, set up health surveillance, or run an ergonomics assessment. It groups workers by exposure, compares measured/estimated exposure to occupational exposure limits, scores manual-handling and posture risk with recognised tools, prioritises controls up the hierarchy, and sets an OEL-linked surveillance schedule — emitted as a branded report. Decision-support only; a competent person (occupational hygienist/physician) must review the output.

### induction-pack
- **Produces:** Produces a site-specific health-and-safety induction pack for a named site, project, or contractor cohort, with a competence-verification record and refresher-tracking schedule.
- **For:** M, C, F · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "build a site induction"; "contractor induction"; "orientation pack"
- **Summary:** Produces a site-specific health-and-safety induction pack for a named site, project, or contractor cohort, with a competence-verification record and refresher-tracking schedule. Use this skill whenever a user asks to build a site induction, new-starter or contractor induction, orientation pack, or onboarding safety briefing for a specific location. It grounds the induction in the site's real hazards, emergency arrangements, and rules over the mandatory induction baseline (KB-SNIP-INDUCTION-BASELINE); produces a delivery pack plus a signed competence-verification record proving each inductee understood the content; and schedules refreshers by role-risk — emitted as a branded report. A generic induction with no named site or site-specific hazards is refused. Decision-support only; a competent person must review the output.

### iso45001-gap-analysis
- **Produces:** Produces a clause-by-clause ISO 45001 gap analysis and certification-readiness assessment for a named organisation or site.
- **For:** M, C, E · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess ISO 45001 readiness"; "run a gap analysis against ISO 45001"; "check management-system conformance"
- **Summary:** Produces a clause-by-clause ISO 45001 gap analysis and certification-readiness assessment for a named organisation or site. Use this skill whenever a user asks to assess ISO 45001 readiness, run a gap analysis against ISO 45001, check management-system conformance, prepare for a certification or surveillance audit, or score maturity against the standard's clauses. It scores each clause's conformance from evidence on a 5-level maturity scale, prioritises gaps by risk and certification-blocking severity, and produces a costed remediation roadmap with named owners and dates — emitted as a branded report. Equally adaptable to ISO 14001 / ISO 45003 via the standard selector. Decision-support only; a competent person must review the output.

### legal-compliance-register
- **Produces:** Produces a multi-jurisdiction HSE legal and other-requirements compliance register for a named organisation or site.
- **For:** M, C, E · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "build a legal register"; "compliance obligations register"; "applicable-legislation list"
- **Summary:** Produces a multi-jurisdiction HSE legal and other-requirements compliance register for a named organisation or site. Use this skill whenever a user asks to build a legal register, compliance obligations register, applicable-legislation list, or to evaluate compliance against ISO 45001 clause 6.1.3. It identifies applicable legal and other requirements for the user's jurisdiction(s) and activities, maps each obligation to its applicability and the evidence of compliance, flags gaps with owners and review dates, and emits a branded register. For India, it defers to the hse-india engine for state-specific obligations and never hard-codes national form numbers; state detection is mandatory. Decision-support only; a competent person must review the output.

### psychosocial-risk-assessment
- **Produces:** Produces a consultant-grade psychosocial risk assessment for a named team, role, or function — identifying work-related psychosocial hazards and recommending work-design controls.
- **For:** M, C, E · **Packs:** hse-healthcare, hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess psychosocial risk"; "work-related stress"; "mental-health hazards"
- **Summary:** Produces a consultant-grade psychosocial risk assessment for a named team, role, or function — identifying work-related psychosocial hazards and recommending work-design controls. Use this skill whenever a user asks to assess psychosocial risk, work-related stress, mental-health hazards, burnout, or workload/work-design risks, or to apply ISO 45003 or the HSE Management Standards. It assesses the hazard at source (work design, not the individual), prioritises organisational controls over individual resilience training, protects respondent confidentiality, and assigns owners and dates — emitted as a branded report. Decision-support only; a competent person must review the output.

### regulatory-returns
- **Produces:** Determines and prepares mandatory HSE regulatory returns for a named organisation across jurisdictions — OSHA recordkeeping (Forms 300/300A/301) and electronic submission, UK RIDDOR reports, and EU equivalents.
- **For:** M, C, F · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "which incidents are recordable"; "how to complete OSHA 300/300A/301"; "whether something is RIDDOR-reportable"
- **Summary:** Determines and prepares mandatory HSE regulatory returns for a named organisation across jurisdictions — OSHA recordkeeping (Forms 300/300A/301) and electronic submission, UK RIDDOR reports, and EU equivalents. Use this skill whenever a user asks which incidents are recordable or reportable, how to complete OSHA 300/300A/301, whether something is RIDDOR-reportable, what the reporting deadlines are, or to prepare a periodic statutory return. It applies the jurisdiction's recordability/reportability tests, identifies the correct form and deadline, and prepares a de-identified return with the evidence trail. For India, it defers entirely to the hse-india skills (state forms, accident notices) and never hard-codes national form numbers; state detection is mandatory. Decision-support only; a competent person must review the output.

### training-needs-analysis
- **Produces:** Produces a consultant-grade, role-by-competence Training Needs Analysis (TNA) for a named site, function, or project.
- **For:** M, C, F · **Packs:** hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "identify training gaps"; "build a competence"; "training matrix"
- **Summary:** Produces a consultant-grade, role-by-competence Training Needs Analysis (TNA) for a named site, function, or project. Use this skill whenever a user asks to identify training gaps, build a competence or training matrix, map roles to required competencies, plan a training programme, track certification expiry, or run a TNA grounded in ISO 45001 clause 7.2 (competence). It builds a role×competence matrix, scores current-vs-required competence from evidence, flags single-points-of-failure and expiring certifications, and emits a prioritised, costed training plan with named owners and due dates as a branded report. Decision-support only; a competent person must review the output.
