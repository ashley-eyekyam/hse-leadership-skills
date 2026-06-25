# Manufacturing

`hse-manufacturing` is the manufacturing & plant pack — the occupational-hygiene and machinery-safety artifacts of a production floor. It covers machine-guarding assessment (ISO 12100 / 14120, OSHA 1910 Subpart O), quantified ergonomics (RULA / REBA / NIOSH), occupational-noise exposure and hearing-conservation, the chemical-exposure register, occupational-health risk assessment, the task×hazard PPE matrix, and permits-to-work.

```
/plugin install hse-manufacturing@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### chemical-exposure-register -> see [Chemicals](Chemicals#chemical-exposure-register)
Tracks chemical agents, OELs, similar-exposure groups, and exposure controls for manufacturing lines that use hazardous substances. Full card on the Chemicals page.

### ergonomics-assessment
- **Produces:** Quantified ergonomics and manual-handling assessment for named tasks or workstations.
- **For:** M, C, F · **Grounded in:** NIOSH Lifting Equation, RULA, REBA, ISO 11228, ISO/TR 12296, and the deterministic `ergonomics` engine · **Packs:** hse-manufacturing.
- **Use when:** A manager, frontline lead, or consultant needs to assess manual handling, posture, repetitive strain, lifting risk, workstation/MSD risk, or a RULA/REBA/NIOSH lifting-index task.
- **Don't use for:** Broad occupational-health exposure grouping or surveillance planning; use [health-risk-assessment](Operations#health-risk-assessment) for role/SEG health-risk assessment.
- **Have ready:** Assessment method, named task/workstation and role, method-specific inputs such as NIOSH load geometry or RULA/REBA posture scores, exposure pattern, affected role/SEG and de-identified symptoms, jurisdiction, site/line, competent assessor, action owners, and review trigger.
- **Trigger:** "a user asks to assess ergonomics", "manual handling", "repetitive strain".
- **You get:** Deterministic RULA/REBA/NIOSH metrics and action bands, residual MSD risk, hierarchy-ranked controls that put task or workstation redesign and engineering controls before rotation, training, or PPE, symptom-surveillance cadence by role/SEG, and owned/dated SMART actions.
- **Pairs well with:** [health-risk-assessment](Operations#health-risk-assessment), [risk-assessment](Core#risk-assessment), [ppe-matrix](#ppe-matrix).

### health-risk-assessment -> see [Operations](Operations#health-risk-assessment)
Covers broader occupational-health risk across roles and tasks, including health surveillance planning. Full card on the Operations page.

### machine-guarding-assessment
- **Produces:** Machine-guarding assessment and hazard-zone register for a named machine, line, or cell.
- **For:** M, C, F · **Grounded in:** ISO 12100, ISO 14120, OSHA 29 CFR 1910 Subpart O (1910.212 / 1910.219), PUWER 1998 Regulations 11-12, Factories Act 1948 section 21 where applicable, and LOTO for maintenance interaction · **Packs:** hse-manufacturing.
- **Use when:** A team needs to assess machine guarding, review a guarding survey, select guards or protective devices, check guarding against PUWER/Subpart O, or build a guard-by-hazard-zone register.
- **Don't use for:** Generic "guard all moving parts" advice, PPE selection, or maintenance isolation procedure authoring; use [ppe-matrix](#ppe-matrix) for PPE residuals and the LOTO/permit workflow when isolation controls are the main artifact.
- **Have ready:** Named machine/line/cell, manufacturer/model and function, hazardous motion type, each danger zone, existing guard/device and condition, access frequency, interaction modes including maintenance, energy sources for LOTO where relevant, jurisdiction, site/area, guard owners, verifier, and review cycle.
- **Trigger:** "a user asks to assess machine guarding", "review a guarding survey", "select guards".
- **You get:** Per-zone danger register, existing-safeguarding status, immediate findings for missing/defeated/overridden guards, guard/device selection in fixed -> interlocked -> presence-sensing -> two-hand/hold-to-run -> trip order, maintenance LOTO cross-reference, residual risk, and owned corrective actions.
- **Pairs well with:** [ppe-matrix](#ppe-matrix), [permit-to-work](Process-Safety#permit-to-work), [risk-assessment](Core#risk-assessment).

### noise-exposure-health-surveillance
- **Produces:** Occupational-noise exposure assessment with hearing-conservation and audiometric-surveillance plan for a named area or SEG.
- **For:** M, C, F · **Grounded in:** OSHA 29 CFR 1910.95 85/90 dBA values, Control of Noise at Work Regulations 2005 80/85/87 dB(A) values, ISO 9612, ISO 1999, and the noise-control hierarchy · **Packs:** hse-manufacturing.
- **Use when:** A site needs to assess noise exposure, map exposure zones, compare TWA or L_EX,8h against cited action/limit values, build a hearing-conservation program, or set audiometric surveillance for exposed roles.
- **Don't use for:** Chemical or whole-role occupational-health assessment, or audiometry scheduling from "it seems loud" with no exposure basis; use [chemical-exposure-register](Chemicals#chemical-exposure-register) for chemical OEL work and [health-risk-assessment](Operations#health-risk-assessment) for broader health-risk planning.
- **Have ready:** Exposure-data basis, named area and SEG/roles, measured or estimated 8-hour TWA / L_EX,8h values and peak/C-weighted data if impulsive, noise sources, existing controls, jurisdiction, site/process, competent occupational-hygiene or audiometry role, action owners, and review triggers.
- **Trigger:** "Produces an occupational-noise exposure assessment and a hearing-conservation / audiometric-surveillance plan for a named area", "similar-exposure group (SEG): compares measured", "estimated noise to the cited action and limit values".
- **You get:** Cited exposure-vs-action/limit comparison, exposure-zone map, hierarchy-ranked noise-reduction plan with source and engineering controls before administrative controls and hearing protection, hearing-conservation elements, baseline/annual/STS-trigger audiometry schedule where exposure basis exists, and de-identified health-data handling by SEG/role.
- **Pairs well with:** [health-risk-assessment](Operations#health-risk-assessment), [ppe-matrix](#ppe-matrix), [risk-assessment](Core#risk-assessment).

### permit-to-work -> see [Process Safety](Process-Safety#permit-to-work)
Controls high-risk manufacturing tasks such as hot work, line breaking, confined-space entry, and isolations. Full card on the Process Safety page.

### ppe-matrix
- **Produces:** Task x hazard PPE selection matrix for a named area, line, role set, or task.
- **For:** M, C, F · **Grounded in:** OSHA 29 CFR 1910 Subpart I, OSHA 1910.132(d)(1)-(2), EN/ANSI PPE conformity standards catalog, and the hierarchy-of-controls PPE matrix logic · **Packs:** hse-manufacturing.
- **Use when:** A site needs to build or review a PPE matrix, PPE hazard assessment, PPE selection table, task-by-body-region PPE grid, or OSHA 1910.132(d)(2) written hazard-assessment certification.
- **Don't use for:** Site-wide PPE sheets, the full upstream risk assessment, or selecting PPE before higher-order controls are considered; use [risk-assessment](Core#risk-assessment) for the source HIRA and [machine-guarding-assessment](#machine-guarding-assessment) for machinery engineering controls.
- **Have ready:** Named area/line/role set and tasks, hazards by body region, higher-order controls considered for each hazard, task duration and conditions, respiratory fit/medical-clearance requirement at role level where relevant, existing PPE and standards gaps, jurisdiction, site/area, certifier, action owners, and review cycle.
- **Trigger:** "a user asks to build", "review a PPE matrix", "a PPE hazard assessment".
- **You get:** Controls-first flags, residual-hazard-only PPE rows, cited EN/ANSI conformity standard for each selected PPE item, respiratory data reduced to role labels, OSHA written hazard-assessment certification fields, PPE-gap actions, and SMART owners/dates.
- **Pairs well with:** [risk-assessment](Core#risk-assessment), [machine-guarding-assessment](#machine-guarding-assessment), [noise-exposure-health-surveillance](#noise-exposure-health-surveillance), [chemical-exposure-register](Chemicals#chemical-exposure-register).
