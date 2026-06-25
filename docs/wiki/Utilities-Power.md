# Utilities & Power

`hse-utilities-power` is the electrical-safety pack for power and utilities work — every artifact driven by the de-energize-first hierarchy. It covers arc-flash risk assessment (IEEE 1584-2018 / NFPA 70E), HV/LV switching programs (isolation → prove-dead → earthing → sanction-to-test), the live-working (energized-work) risk assessment and statutory justification, and the scenario-keyed emergency-response plan.

```
/plugin install hse-utilities-power@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### arc-flash-assessment
- **Produces:** Consultant-grade arc-flash risk assessment and NFPA 70E label content for named electrical equipment.
- **For:** M, C · **Grounded in:** NFPA 70E (2024) 130.5 / 130.5(G) / 130.5(H), IEEE 1584-2018, NFPA 70E Article 120, OSHA 1910.333(a)(2), and EAWR 1989 reg 14 · **Packs:** hse-renewables, hse-utilities-power.
- **Use when:** A user needs to perform an arc-flash assessment or hazard analysis, run an incident-energy study, calculate the arc-flash boundary, determine the PPE category, or produce labels for specific equipment.
- **Don't use for:** Live-work justification without the incident-energy computation; use [live-working-risk-assessment](#live-working-risk-assessment) for the energized-work permit and statutory live-working gate.
- **Have ready:** Named equipment, task/de-energization decision, energized-work justification if dead work is not reasonable, nominal voltage, bolted fault current, clearing time, electrode configuration, enclosure/gap dimensions, working distance, PPE-selection method, jurisdiction, site, output type, action owner, verifier, and review trigger.
- **Trigger:** "a user asks to perform an arc-flash assessment", "hazard analysis", "run an incident-energy study".
- **You get:** De-energization decision, IEEE 1584 input register, computed incident energy, computed arc-flash boundary, PPE category or incident-energy method result, hierarchy-ranked controls with de-energize first and arc-rated PPE last, NFPA 70E 130.5(H) label content, `[GAP]` items for missing parameters, SMART actions, and competent-person review notes.
- **Pairs well with:** [live-working-risk-assessment](#live-working-risk-assessment), [electrical-permit-switching-program](#electrical-permit-switching-program), [permit-to-work](Process-Safety#permit-to-work), [risk-assessment](Core#risk-assessment).

### electrical-permit-switching-program
- **Produces:** HV/LV switching program with ordered switching schedule, isolation/earthing register, and safety-document plan.
- **For:** M, C · **Grounded in:** NFPA 70E Article 120 / 120.5, OSHA 1910.269 / 1910.333 / 1910.147, EAWR 1989 regs 12-13, HSG85, and the ordered isolate -> prove-dead -> earth -> sanction -> restore method · **Packs:** hse-utilities-power.
- **Use when:** A user needs to build a switching program or switching schedule, plan an isolation, write a permit-to-work or sanction-to-test, or take named HV/LV apparatus to a proven safe working condition and back.
- **Don't use for:** Arc-flash incident-energy calculation or live-working justification; use [arc-flash-assessment](#arc-flash-assessment) for incident energy and [live-working-risk-assessment](#live-working-risk-assessment) for energized work.
- **Have ready:** Named apparatus, operating voltage/system, every supply and point of isolation, protective-earthing locations, work activity, safety-document type, de-energization decision, live-work justification if proposed, jurisdiction, site, switching authority, verifier, output type, and review cycle.
- **Trigger:** "a user asks to build a switching program", "switching schedule", "plan an isolation".
- **You get:** Ordered switching sequence with per-step authorisation, isolation and earthing register, prove-dead and prove-test-prove hold points, permit-to-work and sanction-to-test separation, restore sequence, `[GAP]` items for missing apparatus or isolation data, SMART actions, and competent-person review notes.
- **Pairs well with:** [live-working-risk-assessment](#live-working-risk-assessment), [arc-flash-assessment](#arc-flash-assessment), [permit-to-work](Process-Safety#permit-to-work), [risk-assessment](Core#risk-assessment).

### emergency-response-plan -> see [Operations](Operations#emergency-response-plan)
Builds the scenario-keyed site emergency plan that utilities and power facilities need alongside electrical work controls. Full card on the Operations page.

### live-working-risk-assessment
- **Produces:** Live-working risk assessment and energized-work permit with statutory justification for a named task near energized conductors.
- **For:** M, C · **Grounded in:** NFPA 70E Article 120, 110.5 / 130.2 / 130.4 / Annex J, OSHA 1910.333(a)(2), OSHA 1910.269, EAWR 1989 reg 14, HSG85, and HSR25 · **Packs:** hse-renewables, hse-utilities-power.
- **Use when:** A user needs to assess live or energized electrical work, justify working live, build an energized electrical work permit, or set limited/restricted approach boundaries for a specific task and apparatus.
- **Don't use for:** Computing incident energy or writing the isolation sequence; use [arc-flash-assessment](#arc-flash-assessment) for the computed cal/cm2 result and [electrical-permit-switching-program](#electrical-permit-switching-program) for switching and prove-dead/earthing discipline.
- **Have ready:** Named task and live conductors/apparatus, operating voltage, whether the task can be done dead, statutory live-working justification if not, approach distances and precautions, arc-flash result from [arc-flash-assessment](#arc-flash-assessment), energized-work permit status, jurisdiction, site, output type, action owner, competent authority, and review trigger.
- **Trigger:** "a user asks to assess live", "energized electrical work", "justify working live".
- **You get:** De-energize-first decision, statutory live-working test record, convenience-justification refusal where applicable, limited/restricted approach boundaries, controls ranked before arc-rated PPE, arc-flash cross-reference without recomputation, NFPA 70E Annex J permit content, `[GAP]` items, SMART actions, and competent-person review notes.
- **Pairs well with:** [arc-flash-assessment](#arc-flash-assessment), [electrical-permit-switching-program](#electrical-permit-switching-program), [permit-to-work](Process-Safety#permit-to-work), [risk-assessment](Core#risk-assessment).
