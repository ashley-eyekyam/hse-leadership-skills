# Logistics & Transport

`hse-logistics-transport` is the transport and warehousing pack — the road, sea, and warehouse-floor artifacts of a logistics operation. It covers the ADR / DOT 49 CFR / IMDG chemical-transport classification cross-walk, driver-fatigue management (schedule/roster-led FRMS), and warehouse racking + MHE / pedestrian-segregation safety.

```
/plugin install hse-logistics-transport@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### chemical-transport-safety -> see [Chemicals](Chemicals#chemical-transport-safety)
Classifies dangerous goods and transport controls for logistics operations moving hazardous substances by road or sea. Full card on the Chemicals page.

### driver-fatigue-management
- **Produces:** Driver-fatigue-management artifact with computed HOS compliance flags and roster-led FRMS control plan for a named fleet or operation.
- **For:** M, C · **Grounded in:** FMCSA Hours of Service 49 CFR 395, EU Regulation (EC) 561/2006, GB drivers' hours read with EU 561, India Motor Transport Workers rules via `hse-india`, and FRMS principles · **Packs:** hse-logistics-transport.
- **Use when:** A user needs to manage driver fatigue, check hours-of-service compliance, assess a duty/driving log, build an FRMS, review rosters, or decide whether a real driver log is compliant.
- **Don't use for:** Dangerous-goods classification or warehouse MHE/racking risk; use [chemical-transport-safety](Chemicals#chemical-transport-safety) for hazardous-substance transport and [warehouse-racking-mhe-safety](#warehouse-racking-mhe-safety) for warehouse traffic/racking controls.
- **Have ready:** Named fleet/route/depot/operation, jurisdiction and rule set, ordered duty-log segments or ELD/tachograph download, multi-day cumulative on-duty and cross-shift rest data, proposed controls, operating setting, depot/route area, output type, action owners, competent reviewer, and review trigger.
- **Trigger:** "a user asks to manage driver fatigue", "check hours-of-service (HOS) compliance", "assess a duty/driving log against FMCSA 49 CFR 395".
- **You get:** Deterministically computed HOS flags for driving/on-duty/break/cycle/rest rules, clearly marked advisory fatigue index, `[GAP]` items for missing multi-day or rest evidence, roster/journey-plan/FRMS redesign controls before alertness advice or in-cab gadgets, de-identified driver/medical data with small-cell suppression where relevant, SMART actions, and competent-person review notes.
- **Pairs well with:** [warehouse-racking-mhe-safety](#warehouse-racking-mhe-safety), [chemical-transport-safety](Chemicals#chemical-transport-safety), [traffic-management-plan](Construction#traffic-management-plan), [risk-assessment](Core#risk-assessment).

### warehouse-racking-mhe-safety
- **Produces:** Warehouse racking plus MHE/pedestrian-segregation safety assessment for a named warehouse, racking installation, and traffic layout.
- **For:** M, C · **Grounded in:** BS EN 15635:2008, SEMA Code of Practice and RAG damage bands, OSHA 29 CFR 1910.178, PUWER 1998, HSE ACOP L117, HSG136, and India MHE duties via `hse-india` · **Packs:** hse-logistics-transport.
- **Use when:** A user needs to assess pallet racking, build a racking inspection regime, classify rack damage using SEMA Red/Amber/Green, plan MHE/forklift and pedestrian segregation, or check warehouse traffic and racking controls.
- **Don't use for:** Driver fatigue/HOS compliance or dangerous-goods transport classification; use [driver-fatigue-management](#driver-fatigue-management) for driver rosters and [chemical-transport-safety](Chemicals#chemical-transport-safety) for hazardous-substance transport.
- **Have ready:** Named warehouse and racking installation, stored goods, rack type/configuration and displayed SWL notices, PRRS status and inspection cadence, damage findings with SEMA RAG classification, MHE inventory, traffic layout and segregation status, jurisdiction, area/bays in scope, output type, action owners, competent reviewer, and review trigger.
- **Trigger:** "Produces a consultant-grade warehouse racking + MHE/pedestrian-segregation safety artifact for a named warehouse", "racking installation", "and traffic layout — never a generic 'inspect carefully'".
- **You get:** SWL/configuration and inspection-regime findings, PRRS and weekly/expert-inspection actions, SEMA RAG remedial priorities with Green = monitor, Amber = repair within 4 weeks and escalate if overdue, Red = immediate off-load and isolate, engineered segregation controls before hi-vis/signage, `[GAP]` items for missing SWL/tolerance/interval data, SMART actions, and competent-person review notes.
- **Pairs well with:** [driver-fatigue-management](#driver-fatigue-management), [chemical-transport-safety](Chemicals#chemical-transport-safety), [traffic-management-plan](Construction#traffic-management-plan), [risk-assessment](Core#risk-assessment).
