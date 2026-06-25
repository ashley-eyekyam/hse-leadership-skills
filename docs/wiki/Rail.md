# Rail

`hse-rail` is the rail-safety pack — the ROGS management-system and track-safety artifacts of a rail operator or infrastructure manager. It covers the goal-based rail Safety Management System (ROGS / ORR element set), the ORR safety-authorisation / safety-certificate application pack, level-crossing and track-worker safe systems of work, and management-of-change.

```
/plugin install hse-rail@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### level-crossing-track-worker-safety
- **Produces:** Level-crossing risk/remediation assessment and track-worker safe-system-of-work artifact for a named crossing, possession, or work site.
- **For:** M, C · **Grounded in:** ORR level-crossing guidance, NR/L2/OHS/019 by reference, RSSB/Network Rail ALCRM user-supplied band method, and the level-crossing / track-worker hierarchy snippets · **Packs:** hse-rail.
- **Use when:** You need task- and location-specific controls for a named level crossing, possession, line blockage, or on-or-near-the-line work site.
- **Don't use for:** The rail SMS or ORR application pack; use [rail-safety-management-system](#rail-safety-management-system) for the ROGS SMS and [safety-authorisation](#safety-authorisation) for the submission pack.
- **Have ready:** Task type; named crossing or work site; crossing type or track activity; line status; existing/proposed controls; user-supplied ALCRM band if available; jurisdiction or infrastructure manager; safety-critical role labels; audience and review date.
- **Trigger:** "Build a level-crossing and track-worker safe-system-of-work artifact for a named crossing", "work site".
- **You get:** Crossing remedial hierarchy, track-worker protection hierarchy, ALCRM band recorded or `[GAP]`, site-specific control review, residual 5x5 risk score, role-labelled responsibilities, and SMART actions.
- **Pairs well with:** [rail-safety-management-system](#rail-safety-management-system), [safety-authorisation](#safety-authorisation), and [management-of-change](Process-Safety#management-of-change).

### rail-safety-management-system
- **Produces:** ROGS/ORR goal-based rail Safety Management System element set for a named transport operator, infrastructure manager, or non-mainline dutyholder.
- **For:** M, C · **Grounded in:** Railways and Other Guided Transport Systems (Safety) Regulations 2006, ORR SMS element set, and CSM-RA change-management requirements · **Packs:** hse-rail.
- **Use when:** You need to build, review, or structure a rail SMS with policy, accountabilities, risk controls, CSM-RA interface, competence, asset/ECM maintenance, emergency, monitoring, audit, and improvement elements.
- **Don't use for:** Claiming ORR acceptance or assembling the final submission pack; use [safety-authorisation](#safety-authorisation) for the for-submission application and [level-crossing-track-worker-safety](#level-crossing-track-worker-safety) for site-specific crossing or track-worker controls.
- **Have ready:** Build/review/submission mode; dutyholder type; named operator or infrastructure manager and operation scope; jurisdiction or Safety Authority; accountable duty-holder and safety-critical roles; significant change status; existing SMS inputs; review cadence; audience and submission status.
- **Trigger:** "Build a ROGS goal-based rail Safety Management System (SMS) to the ROGS/ORR element set (policy", "risk-control arrangements", "CSM-RA change interface".
- **You get:** Dutyholder route resolution, ROGS/ORR SMS element structure, accountable role map, hierarchy-ranked risk-control arrangements, CSM-RA interface, competence and asset-maintenance sections, emergency and assurance sections, `[GAP]` list, and SMART actions.
- **Pairs well with:** [safety-authorisation](#safety-authorisation), [level-crossing-track-worker-safety](#level-crossing-track-worker-safety), and [management-of-change](Process-Safety#management-of-change).

### safety-authorisation
- **Produces:** ROGS safety-authorisation, safety-certificate, or Part 3 verification application pack for ORR submission, referencing an existing rail SMS.
- **For:** M, C · **Grounded in:** Railways and Other Guided Transport Systems (Safety) Regulations 2006, ORR application route map, and CSM-RA change-evidence requirements · **Packs:** hse-rail.
- **Use when:** You need to assemble, submission-format, or gap-check a ROGS application for a named infrastructure manager, mainline transport operator, or non-mainline operation.
- **Don't use for:** Granting, accepting, approving, or authorising anything on ORR's behalf; use [rail-safety-management-system](#rail-safety-management-system) if the SMS does not yet exist, and [level-crossing-track-worker-safety](#level-crossing-track-worker-safety) for site-specific controls.
- **Have ready:** Application mode; dutyholder type; SMS input status; named dutyholder and operation scope; jurisdiction or Safety Authority; significant change evidence; accountable duty-holder and safety-critical roles; existing SMS and assurance inputs; audience; ORR decision status; target submission or review date.
- **Trigger:** "Assemble a ROGS safety-authorisation (or safety-certificate) application pack for submission to the Office of Rail and Road (ORR)", "drawing on an existing rail Safety Management System rather than rebuilding it".
- **You get:** Dutyholder route declaration, SMS reference and `[GAP]` if absent, application element checklist, CSM-RA change-evidence section, risk-control summary, competence/Sentinel and asset/ECM assurance pointers, submission-status notes, and SMART gap-closure actions.
- **Pairs well with:** [rail-safety-management-system](#rail-safety-management-system), [level-crossing-track-worker-safety](#level-crossing-track-worker-safety), and [management-of-change](Process-Safety#management-of-change).

### management-of-change -> see [Process Safety](Process-Safety#management-of-change)
Structures change risk review for rail assets, processes, people, or procedures where MOC discipline is needed. Full card on the Process Safety page.
