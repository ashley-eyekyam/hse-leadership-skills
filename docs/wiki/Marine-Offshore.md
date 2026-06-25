# Marine & Offshore

`hse-marine-offshore` is the marine and offshore pack — the major-accident-hazard and emergency artifacts of an offshore installation or vessel. It covers the Offshore Safety Case (SI 2015/398), the marine emergency-response plan (muster / POB / TEMPSC / MOB / helideck), DROPS dropped-objects prevention, permits-to-work, and the scenario-keyed emergency-response plan.

```
/plugin install hse-marine-offshore@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### dropped-objects-prevention
- **Produces:** DROPS survey, dropped-object register, reliable-securing controls, and exclusion-zone plan for a named offshore installation, vessel, or at-height area.
- **For:** M, C · **Grounded in:** DROPS Recommended Practice 2017, IADC HSE Guidelines Section 16, API RP 2D & RP 54, and the public `m x g x h` impact-energy method · **Packs:** hse-marine-offshore.
- **Use when:** You need to run or review a DROPS survey, build a static/dynamic dropped-object register, set reliable-securing standards, or define exclusion zones below at-height work.
- **Don't use for:** Generic "wear hard hats below" controls; use [offshore-safety-case](#offshore-safety-case) for the safety-case argument and [marine-emergency-response](#marine-emergency-response) for muster, POB, and EER arrangements.
- **Have ready:** Exact installation, vessel, or area; survey scope; at-height items; static/dynamic object type; primary fixing and secondary retention status; user-supplied mass and fall height; any user-held DROPS Calculator band; jurisdiction; action owner and verifier roles.
- **Trigger:** "Produces a consultant-grade dropped-objects-prevention artifact for a named offshore installation", "at-height area — a DROPS survey + dropped-object register + reliable-securing controls + exclusion zones per the DROPS Recommended Practice (2017) / IADC HSE Guidelines Section 16 / API RP 2D & 54".
- **You get:** Survey scope, static/dynamic register, securing-condition findings, impact-energy calculation with user-supplied inputs, recorded DROPS band or `[GAP]`, reliable-securing controls, exclusion zones, residual risk, and SMART actions.
- **Pairs well with:** [offshore-safety-case](#offshore-safety-case), [marine-emergency-response](#marine-emergency-response), and [permit-to-work](Process-Safety#permit-to-work).

### marine-emergency-response
- **Produces:** Marine/offshore emergency-response and EER plan covering muster, POB accounting, temporary refuge, evacuation/escape/rescue, TEMPSC, MOB recovery, and helideck response where applicable.
- **For:** M, C · **Grounded in:** PFEER 1995, SOLAS Chapter III / LSA Code, and the EER muster-to-temporary-refuge control spine · **Packs:** hse-marine-offshore.
- **Use when:** You need an offshore EER plan, station bill, TEMPSC or survival-craft plan, ERRV or standby-vessel recovery arrangement, MOB response, helideck response, or temporary-refuge plan for a named installation or vessel.
- **Don't use for:** A general land-based ERP; use [emergency-response-plan](Operations#emergency-response-plan) for general site ERP structure and [offshore-safety-case](#offshore-safety-case) for the safety case that cross-references the EER plan.
- **Have ready:** Named installation or vessel; installation type; POB count; emergency scenario set; muster stations and POB accounting method; temporary-refuge endurance basis; TEMPSC/survival-craft capacity; ERRV, MOB, rescue, and helideck arrangements; drill and competence records; jurisdiction.
- **Trigger:** "Produce a consultant-grade marine/offshore emergency-response (EER) plan for a named installation", "vessel: muster + persons-on-board (POB) accounting", "temporary-refuge integrity".
- **You get:** Scenario-keyed response chains, muster and role-labelled station bill, POB accounting, temporary-refuge integrity checks, evacuation/escape/rescue hierarchy, TEMPSC capacity check or `[GAP]`, MOB/ERRV/helideck sections, drills, competence notes, and SMART gap-closure actions.
- **Pairs well with:** [offshore-safety-case](#offshore-safety-case), [emergency-response-plan](Operations#emergency-response-plan), and [dropped-objects-prevention](#dropped-objects-prevention).

### offshore-safety-case
- **Produces:** Assistive offshore safety-case claim-argument-evidence structure for MAH identification, SEMS, CMAPP, ALARP framing, SCE performance standards, and verification scheme.
- **For:** M, C · **Grounded in:** Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 (SI 2015/398), Offshore Safety Directive 2013/30/EU, and the marine/offshore clause map · **Packs:** hse-marine-offshore.
- **Use when:** You need to structure, assemble, or gap-check an offshore safety-case argument for a named installation using duty-holder-supplied evidence.
- **Don't use for:** Competent-authority acceptance, approval, authorisation, QRA, or consequence modelling; use [marine-emergency-response](#marine-emergency-response) for the EER plan the safety case records.
- **Have ready:** Named installation; installation type; UK or EU regime; selected safety-case elements; MAH set and receptors; SEMS and CMAPP inputs; SCE register, performance standards, and independent verification details; QRA/ALARP source and provenance; EER cross-reference; duty-holder and author roles; deadline or revision trigger.
- **Trigger:** "Structures the Offshore Safety Case argument under the Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 (SI 2015/398) — major-accident-hazard (MAH) identification", "the Safety & Environmental Management System (SEMS)", "the corporate major-accident-prevention policy (CMAPP)".
- **You get:** Safety-case element map, claim-argument-evidence structure, MAH and SEMS/CMAPP sections, ALARP provenance gaps, SCE and verification argument, EER cross-reference, `[GAP]` list, and owned gap-closure actions.
- **Pairs well with:** [marine-emergency-response](#marine-emergency-response), [dropped-objects-prevention](#dropped-objects-prevention), and [permit-to-work](Process-Safety#permit-to-work).

### emergency-response-plan -> see [Operations](Operations#emergency-response-plan)
Provides the general site ERP structure that marine and offshore plans build on or cross-reference. Full card on the Operations page.

### permit-to-work -> see [Process Safety](Process-Safety#permit-to-work)
Controls high-risk offshore work such as hot work, confined-space entry, line breaking, and simultaneous operations. Full card on the Process Safety page.
