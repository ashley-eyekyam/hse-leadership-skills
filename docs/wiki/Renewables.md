# Renewables

`hse-renewables` is the renewables pack — the work-at-height, electrical, and point-of-work artifacts of a wind or renewables site. It covers wind-turbine work-at-height and rescue planning, the weather-dynamic point-of-work risk assessment (named numeric thresholds → hold/stop/evacuate), arc-flash and live-working assessment, and lone-working assessment (HSE INDG73 / BS 8484).

```
/plugin install hse-renewables@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### lone-working-assessment
- **Produces:** Lone-working risk assessment and check-in/escalation procedure for a named role, site, and specific solitary activity.
- **For:** M, C · **Grounded in:** HSE INDG73 rev 4, BS 8484:2022, and the check-in / missed-check-in escalation control spine · **Packs:** hse-renewables.
- **Use when:** You need to assess lone or solo work, set scheduled check-ins, define missed-check-in escalation, verify communication coverage, or evaluate a lone-worker device as a supplement.
- **Don't use for:** App-only control sets, solo turbine work at height, or lone electrical work; use [wind-turbine-work-at-height-rescue](#wind-turbine-work-at-height-rescue) for turbine WAH rescue and [live-working-risk-assessment](Utilities-Power#live-working-risk-assessment) or [arc-flash-assessment](Utilities-Power#arc-flash-assessment) for electrical hazards.
- **Have ready:** Scope; named role and site; jurisdiction; specific solitary activity; communication coverage at the work location; check-in interval; missed-check-in responder, method, and response time; proposed controls; owner and verifier roles; review trigger.
- **Trigger:** "Produce a consultant-grade lone-working risk assessment for a named role/site and the specific solitary activity", "grounded in HSE INDG73 (rev 4) and BS 8484:2022".
- **You get:** Role/site-specific lone-working assessment, routing notes for WAH or electrical work, eliminate-first control order, coverage gap findings, scheduled check-in and escalation path, BS 8484 device supplement notes, residual risk, and SMART actions.
- **Pairs well with:** [wind-turbine-work-at-height-rescue](#wind-turbine-work-at-height-rescue), [weather-dynamic-risk-assessment](#weather-dynamic-risk-assessment), [arc-flash-assessment](Utilities-Power#arc-flash-assessment), and [live-working-risk-assessment](Utilities-Power#live-working-risk-assessment).

### weather-dynamic-risk-assessment
- **Produces:** Point-of-work dynamic weather risk assessment with numeric thresholds, hold/stop/evacuate actions, and mandatory reassessment triggers.
- **For:** M, C · **Grounded in:** Work at Height Regulations 2005, BS 7121-1:2016 7 m/s man-riding anchor, NFPA 780 lightning practice, weather-threshold data points, and the dynamic-RA threshold/action/reassessment method · **Packs:** hse-renewables.
- **Use when:** You need weather working limits for turbine, blade, tower, crane, man-riding, switching, or outdoor renewables work, especially where the current control is only "monitor the weather."
- **Don't use for:** Writing the turbine work-at-height rescue plan itself; use [wind-turbine-work-at-height-rescue](#wind-turbine-work-at-height-rescue) for WAH and rescue controls and [lone-working-assessment](#lone-working-assessment) for solitary field work.
- **Have ready:** Named site and activity; jurisdiction; weather-sensitive task and equipment; measurement point; wind, lightning, ice, visibility, and temperature thresholds; threshold source; action at each threshold; reassessment trigger; action owner and verifier roles; review cycle.
- **Trigger:** "Produce a consultant-grade point-of-work DYNAMIC weather risk assessment for a named renewables site/activity", "led by NAMED NUMERIC thresholds -> a hold/stop/evacuate ACTION -> a MANDATORY re-assessment TRIGGER. Use this skill to set weather working limits for turbine/blade/tower", "outdoor renewables work".
- **You get:** Weather-parameter matrix, numeric threshold list, hub-height measurement check, hold/stop/evacuate actions, reassessment triggers, `[GAP]` entries for unsupplied site/manufacturer/lightning-service values, residual risk, and SMART actions.
- **Pairs well with:** [wind-turbine-work-at-height-rescue](#wind-turbine-work-at-height-rescue), [lone-working-assessment](#lone-working-assessment), and [arc-flash-assessment](Utilities-Power#arc-flash-assessment).

### wind-turbine-work-at-height-rescue
- **Produces:** Wind-turbine work-at-height plan and mandatory tested rescue plan for a named turbine/site and WAH activity.
- **For:** M, C · **Grounded in:** Work at Height Regulations 2005 regs 4, 6, 7, and 12; GWO WAH / First Aid / ART competence requirements; and the rescue-plan spine · **Packs:** hse-renewables.
- **Use when:** You need a turbine WAH risk assessment, nacelle/hub/blade/tower rescue plan, two-person climb-team baseline, or suspended-worker recovery plan.
- **Don't use for:** "Call emergency services" as the rescue plan, solo climbs, or owning weather thresholds; use [weather-dynamic-risk-assessment](#weather-dynamic-risk-assessment) for weather limits and [lone-working-assessment](#lone-working-assessment) for non-WAH lone-working procedure.
- **Have ready:** Scope; named turbine/site; jurisdiction; specific WAH activity and access method; avoidance test; collective and personal fall-protection arrangement; tested rescue method and recovery time; climb-team manning and GWO competence; weather threshold names; owner and verifier roles; review trigger.
- **Trigger:** "Produce a consultant-grade wind-turbine work-at-height + rescue plan for a named turbine/site and the specific WAH activity (nacelle/hub/blade/tower). Use this skill to plan work at height on a wind turbine", "build a turbine WAH risk assessment", "specify a mandatory tested rescue plan for a suspended worker".
- **You get:** Avoid/prevent/mitigate WAH control order, collective-before-personal check, two-person team and ground-support baseline, tested rescue plan with recovery-time evidence or `[GAP]`, GWO competence notes, weather-threshold cross-reference, residual risk, and SMART actions.
- **Pairs well with:** [weather-dynamic-risk-assessment](#weather-dynamic-risk-assessment), [lone-working-assessment](#lone-working-assessment), and [live-working-risk-assessment](Utilities-Power#live-working-risk-assessment).

### arc-flash-assessment -> see [Utilities & Power](Utilities-Power#arc-flash-assessment)
Assesses incident energy and arc-flash controls for renewables electrical equipment. Full card on the Utilities & Power page.

### live-working-risk-assessment -> see [Utilities & Power](Utilities-Power#live-working-risk-assessment)
Justifies and controls live or energized work only when de-energized work is not reasonably practicable. Full card on the Utilities & Power page.
