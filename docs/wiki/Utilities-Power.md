# Utilities & Power

`hse-utilities-power` is the electrical-safety pack for power and utilities work — every artifact driven by the de-energize-first hierarchy. It covers arc-flash risk assessment (IEEE 1584-2018 / NFPA 70E), HV/LV switching programs (isolation → prove-dead → earthing → sanction-to-test), the live-working (energized-work) risk assessment and statutory justification, and the scenario-keyed emergency-response plan.

```
/plugin install hse-utilities-power@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### arc-flash-assessment
- **Produces:** Produces a consultant-grade arc-flash risk assessment for named electrical equipment, driven by the de-energize-first hierarchy.
- **For:** M, C · **Packs:** hse-renewables, hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "perform an arc-flash assessment"; "hazard analysis"; "run an incident-energy study"
- **Summary:** Produces a consultant-grade arc-flash risk assessment for named electrical equipment, driven by the de-energize-first hierarchy. Use this skill whenever a user asks to perform an arc-flash assessment or hazard analysis, run an incident-energy study, calculate the arc-flash boundary, determine the PPE category, or produce arc-flash labels for electrical equipment. It computes incident energy and the boundary with the IEEE 1584-2018 method (the cal/cm² value is COMPUTED, never narrated), records whether the task can be done de-energized first (an electrically safe work condition per NFPA 70E Article 120), justifies any energized work against OSHA 1910.333(a)(2) or EAWR reg 14 (convenience is refused), ranks controls up the hierarchy (de-energize first, arc-rated PPE last), and emits a branded report with NFPA 70E 130.5(H) label content. It refuses a PPE-led treatment with no de-energization decision. Grounded in NFPA 70E (2024) and IEEE 1584-2018. Decision-support only; a competent person must review.

### electrical-permit-switching-program
- **Produces:** Produces a consultant-grade HV/LV switching program (a switching schedule + safety-document plan) for named electrical apparatus, driven by the de-energize-first hierarchy and the isolation → prove-dead → earthing → sanction-to-test discipline.
- **For:** M, C · **Packs:** hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "build a switching program"; "switching schedule"; "plan an isolation"
- **Summary:** Produces a consultant-grade HV/LV switching program (a switching schedule + safety-document plan) for named electrical apparatus, driven by the de-energize-first hierarchy and the isolation → prove-dead → earthing → sanction-to-test discipline. Use this skill whenever a user asks to build a switching program or switching schedule, plan an isolation, write a permit-to-work or sanction-to-test, take HV/LV equipment to a safe working condition and back, or sequence the points of isolation, prove-dead, and protective earthing. It refuses to author a program for "the substation" without the named apparatus, voltage, and points of isolation/earthing; it records the ordered switching sequence with per-step authorisation, gates work behind prove-dead AND protective earthing where required (un-proven or un-earthed work is flagged), and keeps the sanction-to-test distinct from a work permit. Grounded in NFPA 70E Article 120, OSHA 1910.269/.333/.147, and EAWR 1989. Decision-support only; a competent person must review.

### emergency-response-plan
- **Produces:** Produces a scenario-keyed emergency response plan (ERP) for a named site or facility — call-out tree, muster and evacuation arrangements, scenario response procedures, drill schedule, and external-responder integration.
- **For:** M, C, F · **Packs:** hse-marine-offshore, hse-operations, hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review an emergency plan"; "evacuation plan"
- **Summary:** Produces a scenario-keyed emergency response plan (ERP) for a named site or facility — call-out tree, muster and evacuation arrangements, scenario response procedures, drill schedule, and external-responder integration. Use this skill whenever a user asks to write or review an emergency plan, evacuation plan, emergency procedures, crisis-response plan, or to plan emergency drills for a specific location. It grounds the plan in the site's credible emergency scenarios and the hierarchy of controls (prevention before response), assigns named roles with deputies, and schedules drills — emitted as a branded report. For continuity of critical activities after the emergency is controlled (RTO/RPO/MTPD) use business-continuity-plan; for mine-rescue-specific arrangements use mine-rescue-erp; for offshore use the marine-emergency-response skill. Decision-support only; a competent person must review the output.

### live-working-risk-assessment
- **Produces:** Produces a consultant-grade live-working (energized-work) risk assessment and statutory justification for a named task on or near energized conductors, driven by the de-energize-first default and the EAWR reg-14 / OSHA 1910.333(a)(2) three-part live-working test.
- **For:** M, C · **Packs:** hse-renewables, hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess live"; "energized electrical work"; "justify working live"
- **Summary:** Produces a consultant-grade live-working (energized-work) risk assessment and statutory justification for a named task on or near energized conductors, driven by the de-energize-first default and the EAWR reg-14 / OSHA 1910.333(a)(2) three-part live-working test. Use this skill when a user asks to assess live or energized electrical work, justify working live, build an energized electrical work permit, or set the approach boundaries near live conductors. It applies the de-energize-first default (an ESWC, NFPA 70E Article 120 first), forces the statutory test (unreasonable to be dead + reasonable to work live + suitable precautions), states the approach distances (NFPA 70E 130.4), keeps arc-rated PPE last, and cross-references the arc-flash incident energy from arc-flash-assessment without recomputing it. It refuses a convenience justification and emits a branded NFPA 70E Annex J energized-work permit. Grounded in NFPA 70E, OSHA 1910.333, EAWR 1989 reg 14. Decision-support only; a competent person must review.
