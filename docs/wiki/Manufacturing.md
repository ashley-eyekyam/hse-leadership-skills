# Manufacturing

`hse-manufacturing` is the manufacturing & plant pack — the occupational-hygiene and machinery-safety artifacts of a production floor. It covers machine-guarding assessment (ISO 12100 / 14120, OSHA 1910 Subpart O), quantified ergonomics (RULA / REBA / NIOSH), occupational-noise exposure and hearing-conservation, the chemical-exposure register, occupational-health risk assessment, the task×hazard PPE matrix, and permits-to-work.

```
/plugin install hse-manufacturing@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### chemical-exposure-register
- **Produces:** Build an OEL/WEL/PEL-linked chemical hazard and exposure register, organised by similar-exposure group (SEG), banding each exposure with the risk matrix and flagging where health surveillance or air monitoring is due.
- **For:** M, C · **Packs:** hse-chemicals, hse-manufacturing · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Build an OEL/WEL/PEL-linked chemical hazard and exposure register"; "organised by similar-exposure group (SEG)"; "banding each exposure with the risk matrix and flagging where health surveillance"
- **Summary:** Build an OEL/WEL/PEL-linked chemical hazard and exposure register, organised by similar-exposure group (SEG), banding each exposure with the risk matrix and flagging where health surveillance or air monitoring is due. Use it to build a chemical exposure register, link agents to occupational exposure limits, assess inhalation/dermal exposure risk by SEG, or plan a monitoring schedule. Every limit is cited with its source and year; controls are hierarchy-of-controls ranked; worker exposure data is de-identified to role/SEG labels before drafting. Decision-support only; a competent person (e.g. occupational hygienist) must review the output.

### ergonomics-assessment
- **Produces:** Produces a quantified ergonomics / manual-handling assessment for named tasks or workstations — posture scoring with RULA/REBA, manual-lifting evaluation with the NIOSH lifting equation, and a hierarchy-ranked control plan.
- **For:** M, C, F · **Packs:** hse-manufacturing · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess ergonomics"; "manual handling"; "repetitive strain"
- **Summary:** Produces a quantified ergonomics / manual-handling assessment for named tasks or workstations — posture scoring with RULA/REBA, manual-lifting evaluation with the NIOSH lifting equation, and a hierarchy-ranked control plan. Use this skill whenever a user asks to assess ergonomics, manual handling, posture, repetitive strain, lifting risk, a workstation/MSD risk, or to run a RULA, REBA, or NIOSH lifting-index assessment for a specific task or role. It scores each task with the recognised deterministic method, compares the result against the method's action bands, prioritises engineering and task-redesign controls above PPE/training, and emits a branded report with an owned/dated action plan. Grounded in the NIOSH Lifting Equation, RULA/REBA, and ISO 11228. Decision-support only; a competent person (ergonomist / occupational-health professional) must review the output.

### health-risk-assessment
- **Produces:** Produces an occupational-health risk assessment for named tasks or roles — similar-exposure-group definition, hazard-to-OEL comparison, ergonomic scoring (RULA/REBA/NIOSH), and a health-surveillance schedule.
- **For:** M, C, F · **Packs:** hse-manufacturing, hse-operations · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess occupational-health risk"; "chemical/noise/vibration/ergonomic exposure"; "build similar-exposure groups"
- **Summary:** Produces an occupational-health risk assessment for named tasks or roles — similar-exposure-group definition, hazard-to-OEL comparison, ergonomic scoring (RULA/REBA/NIOSH), and a health-surveillance schedule. Use this skill whenever a user asks to assess occupational-health risk, chemical/noise/vibration/ergonomic exposure, build similar-exposure groups, compare exposures to OELs, set up health surveillance, or run an ergonomics assessment. It groups workers by exposure, compares measured/estimated exposure to occupational exposure limits, scores manual-handling and posture risk with recognised tools, prioritises controls up the hierarchy, and sets an OEL-linked surveillance schedule — emitted as a branded report. Decision-support only; a competent person (occupational hygienist/physician) must review the output.

### machine-guarding-assessment
- **Produces:** Produces a consultant-grade machine-guarding assessment for a named machine or line — guard-by-hazard-zone per ISO 12100/14120 and OSHA 1910 Subpart O (1910.212/.219).
- **For:** M, C, F · **Packs:** hse-manufacturing · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "assess machine guarding"; "review a guarding survey"; "select guards"
- **Summary:** Produces a consultant-grade machine-guarding assessment for a named machine or line — guard-by-hazard-zone per ISO 12100/14120 and OSHA 1910 Subpart O (1910.212/.219). Use this skill whenever a user asks to assess machine guarding, review a guarding survey, select guards or protective devices for a danger zone, check guarding against PUWER or Subpart O, or build a hazard-zone register — not a generic 'guard all moving parts'. It is engineering-control-led: each danger zone walks the selection order (fixed, interlocked, presence-sensing, two-hand, trip) against the access-frequency rule, and a mechanical-zone control left as PPE-only or admin-only ('keep hands clear / wear gloves') is flagged and pushed up the hierarchy. It refuses 'a machine' or 'looks guarded' without a named machine plus motion/hazard type plus safeguarding status, cross-references the existing lockout/tagout map for maintenance, and emits a branded hazard-zone register. Decision-support only; a competent person must review the output.

### noise-exposure-health-surveillance
- **Produces:** Produces an occupational-noise exposure assessment and a hearing-conservation / audiometric-surveillance plan for a named area or similar-exposure group (SEG): compares measured or estimated noise to the cited action and limit values, maps exposure zones, ranks noise-reduction controls up the hierarchy (source → engineering → administrative → hearing protection LAST), and sets an audiometry schedule (baseline / annual / standard-threshold-shift triggers).
- **For:** M, C, F · **Packs:** hse-manufacturing · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Produces an occupational-noise exposure assessment and a hearing-conservation / audiometric-surveillance plan for a named area"; "similar-exposure group (SEG): compares measured"; "estimated noise to the cited action and limit values"
- **Summary:** Produces an occupational-noise exposure assessment and a hearing-conservation / audiometric-surveillance plan for a named area or similar-exposure group (SEG): compares measured or estimated noise to the cited action and limit values, maps exposure zones, ranks noise-reduction controls up the hierarchy (source → engineering → administrative → hearing protection LAST), and sets an audiometry schedule (baseline / annual / standard-threshold-shift triggers). Use this skill to assess noise exposure, build a hearing-conservation program, set up audiometric surveillance, compare a TWA / L_EX,8h to the 85/90 dBA (OSHA) or 80/85/87 dB(A) (UK) action and limit values, or plan noise reduction for an area or task. It transcribes measured levels (no dosimetry computed), cites each action level / limit with authority and year, refuses a schedule on a vague basis, and treats standard-threshold-shift audiometry as special-category health data reported by SEG/role. Decision-support only; a competent person must review it.

### permit-to-work
- **Produces:** Produces a permit-to-work package for a named high-risk task (hot work, confined-space entry, line breaking, excavation, working at height) with a dedicated SIMOPS (simultaneous operations) coordination section: it detects concurrent operations in the intake and routes them to permit and coordination controls, applies the hierarchy of controls to every isolation and safeguard, and tracks the permit conditions and actions to closure.
- **For:** M, C · **Packs:** hse-construction, hse-manufacturing, hse-marine-offshore, hse-process · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Produces a permit-to-work package for a named high-risk task (hot work"; "confined-space entry"; "line breaking"
- **Summary:** Produces a permit-to-work package for a named high-risk task (hot work, confined-space entry, line breaking, excavation, working at height) with a dedicated SIMOPS (simultaneous operations) coordination section: it detects concurrent operations in the intake and routes them to permit and coordination controls, applies the hierarchy of controls to every isolation and safeguard, and tracks the permit conditions and actions to closure. SIMOPS is handled as a permit/coordination control within this skill, never as a separate workflow. Decision-support only; a competent person must review the output.

### ppe-matrix
- **Produces:** Produces a task×hazard→PPE selection matrix for a named area, line, or role set, driven by the controls-first gate: PPE is specified only for the residual hazard surviving the higher-order controls, never as the headline control.
- **For:** M, C, F · **Packs:** hse-manufacturing · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review a PPE matrix"; "a PPE hazard assessment"
- **Summary:** Produces a task×hazard→PPE selection matrix for a named area, line, or role set, driven by the controls-first gate: PPE is specified only for the residual hazard surviving the higher-order controls, never as the headline control. Use this skill whenever a user asks to build or review a PPE matrix, a PPE hazard assessment, a PPE selection table, or the OSHA 1910.132(d)(2) written hazard-assessment certification for a specific task, line, area, or role — not a site-wide sheet. It runs the hierarchy of controls before any PPE row (a hazard with no recorded higher-order control triggers a controls-first flag, not a PPE row), selects each PPE type against the named residual hazard with its cited conformity standard (EN / ANSI), reduces respiratory medical-clearance data to role labels, and emits a branded matrix report with the written hazard-assessment certification. Grounded in the OSHA PPE standard (29 CFR 1910.132) + the hierarchy of controls. Decision-support only; a competent person must review the output.
