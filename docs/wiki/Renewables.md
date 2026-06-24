# Renewables

`hse-renewables` is the renewables pack — the work-at-height, electrical, and point-of-work artifacts of a wind or renewables site. It covers wind-turbine work-at-height and rescue planning, the weather-dynamic point-of-work risk assessment (named numeric thresholds → hold/stop/evacuate), arc-flash and live-working assessment, and lone-working assessment (HSE INDG73 / BS 8484).

```
/plugin install hse-renewables@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### arc-flash-assessment
- **Produces:** Produces a consultant-grade arc-flash risk assessment for named electrical equipment, driven by the de-energize-first hierarchy.
- **For:** M, C · **Packs:** hse-renewables, hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "perform an arc-flash assessment"; "hazard analysis"; "run an incident-energy study"
- **Summary:** Produces a consultant-grade arc-flash risk assessment for named electrical equipment, driven by the de-energize-first hierarchy. Use this skill whenever a user asks to perform an arc-flash assessment or hazard analysis, run an incident-energy study, calculate the arc-flash boundary, determine the PPE category, or produce arc-flash labels for electrical equipment. It computes incident energy and the boundary with the IEEE 1584-2018 method (the cal/cm² value is COMPUTED, never narrated), records whether the task can be done de-energized first (an electrically safe work condition per NFPA 70E Article 120), justifies any energized work against OSHA 1910.333(a)(2) or EAWR reg 14 (convenience is refused), ranks controls up the hierarchy (de-energize first, arc-rated PPE last), and emits a branded report with NFPA 70E 130.5(H) label content. It refuses a PPE-led treatment with no de-energization decision. Grounded in NFPA 70E (2024) and IEEE 1584-2018. Decision-support only; a competent person must review.

### live-working-risk-assessment
- **Produces:** Produces a consultant-grade live-working (energized-work) risk assessment and statutory justification for a named task on or near energized conductors, driven by the de-energize-first default and the EAWR reg-14 / OSHA 1910.333(a)(2) three-part live-working test.
- **For:** M, C · **Packs:** hse-renewables, hse-utilities-power · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess live"; "energized electrical work"; "justify working live"
- **Summary:** Produces a consultant-grade live-working (energized-work) risk assessment and statutory justification for a named task on or near energized conductors, driven by the de-energize-first default and the EAWR reg-14 / OSHA 1910.333(a)(2) three-part live-working test. Use this skill when a user asks to assess live or energized electrical work, justify working live, build an energized electrical work permit, or set the approach boundaries near live conductors. It applies the de-energize-first default (an ESWC, NFPA 70E Article 120 first), forces the statutory test (unreasonable to be dead + reasonable to work live + suitable precautions), states the approach distances (NFPA 70E 130.4), keeps arc-rated PPE last, and cross-references the arc-flash incident energy from arc-flash-assessment without recomputing it. It refuses a convenience justification and emits a branded NFPA 70E Annex J energized-work permit. Grounded in NFPA 70E, OSHA 1910.333, EAWR 1989 reg 14. Decision-support only; a competent person must review.

### lone-working-assessment
- **Produces:** Produce a consultant-grade lone-working risk assessment for a named role/site and the specific solitary activity, grounded in HSE INDG73 (rev 4) and BS 8484:2022.
- **For:** M, C · **Packs:** hse-renewables · **Version:** 1.0 · **Jurisdiction:** UK
- **Trigger:** "Produce a consultant-grade lone-working risk assessment for a named role/site and the specific solitary activity"; "grounded in HSE INDG73 (rev 4) and BS 8484:2022"
- **Summary:** Produce a consultant-grade lone-working risk assessment for a named role/site and the specific solitary activity, grounded in HSE INDG73 (rev 4) and BS 8484:2022. Use this skill to assess lone or solo working, build a lone-working risk assessment, set up scheduled check-ins and a missed-check-in escalation path, specify a coverage-checked communication plan, or evaluate a lone-worker device/app for renewables and field work. It leads with ELIMINATING the solitary exposure first (pair up, re-schedule, remote monitoring), then a reliable scheduled check-in with a defined missed-check-in escalation path; a BS 8484 device SUPPLEMENTS but never replaces the procedure, and 'no mobile signal' is a control failure, not an accepted risk. It routes lone work at height to wind-turbine-work-at-height-rescue (REN-01) and lone electrical work to the cross-listed utilities skills, and de-identifies lone-worker contact / shift / location to role labels. Decision-support only; competent-person review required.

### weather-dynamic-risk-assessment
- **Produces:** Produce a consultant-grade point-of-work DYNAMIC weather risk assessment for a named renewables site/activity, led by NAMED NUMERIC thresholds -> a hold/stop/evacuate ACTION -> a MANDATORY re-assessment TRIGGER.
- **For:** M, C · **Packs:** hse-renewables · **Version:** 1.0 · **Jurisdiction:** UK
- **Trigger:** "Produce a consultant-grade point-of-work DYNAMIC weather risk assessment for a named renewables site/activity"; "led by NAMED NUMERIC thresholds -> a hold/stop/evacuate ACTION -> a MANDATORY re-assessment TRIGGER. Use this skill to set weather working limits for turbine/blade/tower"; "outdoor renewables work"
- **Summary:** Produce a consultant-grade point-of-work DYNAMIC weather risk assessment for a named renewables site/activity, led by NAMED NUMERIC thresholds -> a hold/stop/evacuate ACTION -> a MANDATORY re-assessment TRIGGER. Use this skill to set weather working limits for turbine/blade/tower or outdoor renewables work, decide when to hold, stop or evacuate for wind, lightning, ice, visibility or temperature, or replace a vague 'monitor the weather' arrangement with defensible numeric triggers. Wind is measured at HUB HEIGHT, not base-of-tower (a base-of-tower reading is a control failure). It OWNS the weather thresholds wind-turbine-work-at-height-rescue (REN-01) only names: BS 7121-1 (2016) 7 m/s man-riding ceiling is the verified anchor, the hub-height cut-off ~=15 m/s is [ASSUMED A4] proposed-and-user-confirms, and every other threshold is user-confirmed or [GAP] -- never invented. De-identifies prior weather-incident context to role labels. Decision-support only; competent-person review required.

### wind-turbine-work-at-height-rescue
- **Produces:** Produce a consultant-grade wind-turbine work-at-height + rescue plan for a named turbine/site and the specific WAH activity (nacelle/hub/blade/tower).
- **For:** M, C · **Packs:** hse-renewables · **Version:** 1.0 · **Jurisdiction:** UK
- **Trigger:** "Produce a consultant-grade wind-turbine work-at-height + rescue plan for a named turbine/site and the specific WAH activity (nacelle/hub/blade/tower). Use this skill to plan work at height on a wind turbine"; "build a turbine WAH risk assessment"; "specify a mandatory tested rescue plan for a suspended worker"
- **Summary:** Produce a consultant-grade wind-turbine work-at-height + rescue plan for a named turbine/site and the specific WAH activity (nacelle/hub/blade/tower). Use this skill to plan work at height on a wind turbine, build a turbine WAH risk assessment, specify a mandatory tested rescue plan for a suspended worker, or set the two-person-minimum climb-team baseline. Control leads with the Work at Height Regulations 2005 reg-6 hierarchy (avoid work at height -> prevent a fall, collective before personal -> mitigate/arrest), and a tested rescue plan is mandatory before work begins: a suspended worker is recovered within minutes by the team's own two-person-minimum capability -- 'call 999' is NEVER the rescue plan. It cites GWO competence as a requirement (cite-only; licensed module/cert detail is [GAP]), names the weather thresholds weather-dynamic-risk-assessment (REN-03) owns, and de-identifies worker names + GWO certificate numbers to role labels. Decision-support only; competent-person review required.
