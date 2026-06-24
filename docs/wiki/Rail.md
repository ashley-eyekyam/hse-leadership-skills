# Rail

`hse-rail` is the rail-safety pack — the ROGS management-system and track-safety artifacts of a rail operator or infrastructure manager. It covers the goal-based rail Safety Management System (ROGS / ORR element set), the ORR safety-authorisation / safety-certificate application pack, level-crossing and track-worker safe systems of work, and management-of-change.

```
/plugin install hse-rail@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### level-crossing-track-worker-safety
- **Produces:** Build a level-crossing and track-worker safe-system-of-work artifact for a named crossing or work site.
- **For:** M, C · **Packs:** hse-rail · **Version:** 1.0 · **Jurisdiction:** UK
- **Trigger:** "Build a level-crossing and track-worker safe-system-of-work artifact for a named crossing"; "work site"
- **Summary:** Build a level-crossing and track-worker safe-system-of-work artifact for a named crossing or work site. Use this skill to assess and control level-crossing risk and on-or-near-the-line track-work risk for a specific crossing, possession, or worksite. It leads level-crossing remediation with closure -> grade separation -> engineering, with sighting / signage / administrative LAST, and leads track-worker protection with separation (green-zone / line blockage / possession) -> safe systems of work -> warning -> lookout-only LAST. It RECORDS the user's All Level Crossing Risk Model (ALCRM) band rather than inventing or recomputing it (a missing band is [GAP]), grounds the work in KB-REG-LX-TRACKWORKER and KB-SNIP-LX-HIERARCHY, scores residual risk on a 5x5 matrix, assigns SMART actions with named role owners and dates, defers India content to hse-india, and de-identifies COSS / Sentinel / lookout role-holders to role labels. Decision-support only; a competent person must review the output.

### management-of-change
- **Produces:** Produces a Management of Change (MoC) package: the technical basis for the change, a risk assessment of the change, temporary-change expiry, the Pre-Start-Up Safety Review (PSSR) as a hard pre-start-up gate, and document/training updates (OSHA 1910.119(l), ISO 45001 8.1.3).
- **For:** M, C · **Packs:** hse-process, hse-rail · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Produces a Management of Change (MoC) package: the technical basis for the change"; "a risk assessment of the change"; "temporary-change expiry"
- **Summary:** Produces a Management of Change (MoC) package: the technical basis for the change, a risk assessment of the change, temporary-change expiry, the Pre-Start-Up Safety Review (PSSR) as a hard pre-start-up gate, and document/training updates (OSHA 1910.119(l), ISO 45001 8.1.3). No start-up authorization is issued until the PSSR checklist passes. Decision-support only; a competent person must review the output.

### rail-safety-management-system
- **Produces:** Build a ROGS goal-based rail Safety Management System (SMS) to the ROGS/ORR element set (policy, accountabilities, risk-control arrangements, CSM-RA change interface, competence/Sentinel, asset/ECM maintenance, emergency, monitoring/audit, continuous improvement) for a named transport operator or infrastructure manager.
- **For:** M, C · **Packs:** hse-rail · **Version:** 1.0 · **Jurisdiction:** UK
- **Trigger:** "Build a ROGS goal-based rail Safety Management System (SMS) to the ROGS/ORR element set (policy"; "risk-control arrangements"; "CSM-RA change interface"
- **Summary:** Build a ROGS goal-based rail Safety Management System (SMS) to the ROGS/ORR element set (policy, accountabilities, risk-control arrangements, CSM-RA change interface, competence/Sentinel, asset/ECM maintenance, emergency, monitoring/audit, continuous improvement) for a named transport operator or infrastructure manager. Use this skill to build or review a rail SMS or structure a ROGS safety-certificate / safety-authorisation submission. Grounds elements in KB-REG-ROGS and the change interface in KB-REG-CSM-RA, resolves the route first (mainline operator -> safety certificate; infrastructure manager -> safety authorisation; non-mainline -> Part 3 verification), names the accountable duty-holder and safety-critical roles, ranks every mitigation through the hierarchy of controls, and de-identifies role-holder names / COSS / Sentinel numbers to role labels. The SMS is for-acceptance: it never claims it is 'accepted by ORR'. Decision-support only; a competent rail-SMS / ORR-aware person must review the output.

### safety-authorisation
- **Produces:** Assemble a ROGS safety-authorisation (or safety-certificate) application pack for submission to the Office of Rail and Road (ORR), drawing on an existing rail Safety Management System rather than rebuilding it.
- **For:** M, C · **Packs:** hse-rail · **Version:** 1.0 · **Jurisdiction:** UK
- **Trigger:** "Assemble a ROGS safety-authorisation (or safety-certificate) application pack for submission to the Office of Rail and Road (ORR)"; "drawing on an existing rail Safety Management System rather than rebuilding it"
- **Summary:** Assemble a ROGS safety-authorisation (or safety-certificate) application pack for submission to the Office of Rail and Road (ORR), drawing on an existing rail Safety Management System rather than rebuilding it. Use this skill to structure and gap-check a ROGS application for a named infrastructure manager or transport operator. It resolves the dutyholder route first (infrastructure manager -> safety authorisation; mainline transport operator -> safety certificate; non-mainline -> Part-3 verification), references the SMS from the sibling skill rail-safety-management-system (RAIL-01) as an input, grounds the pack in KB-REG-ROGS and KB-REG-CSM-RA, names the accountable duty-holder and safety-critical roles, ranks mitigations through the hierarchy of controls, records [GAP] for unsupplied elements, and de-identifies role-holder names / Sentinel numbers to role labels. The pack is for-submission and never claims it is 'authorised by ORR'. Decision-support only; a competent person must review the output.
