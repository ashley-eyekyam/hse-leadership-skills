# Mining

The **Mining pack** (`hse-mining`) gives mine safety teams, statutory mine managers, and HSE consultants a focused set of mining-specific skills — India Mines Act / DGMS statutory work, ICMM Critical Control Management, principal-hazard and mine-plan documents, mine-rescue emergency planning, and sector-tuned incident investigation. It grounds in the DGMS legacy-first regulatory framing and the ICMM CCM / principal-hazard taxonomy, and it bundles in the shared bow-tie/barrier tool from Process Safety. Install it with:

```
/plugin install hse-mining@hse-leadership-skills
```

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### dgms-statutory-pack
- **Produces:** The prescribed DGMS legacy form for a mine's resolved region — the 24-hour accident / dangerous-occurrence notice, Form J accident register, Form B employee register, the ~20 January annual return, or statutory Manager / officials appointment letters — with the OSH-Code transition note appended.
- **For:** M, C · **Grounded in:** India Mines Act 1952 / DGMS (`KB-REG-IN-MINES-ACT`, `KB-REG-IN-DGMS`); region-resolved via `KB-REG-IN-STATEFORMS`; jurisdiction IN · **Packs:** hse-mining
- **Use when:** A mine must determine which DGMS form to file, draft a statutory mine notice / return / register entry, or check a statutory appointment for a named mine in a resolved region.
- **Don't use for:** Investigating the mine accident itself (use `mine-incident-investigation`), or non-mining Factories Act state returns (use `factories-act-returns`).
- **Have ready:** The obligation you need to meet (the runtime gate), the mine's DGMS region/zone (a mandatory gate confirmed before any form is cited), and the per-obligation follow-up facts.
- **Trigger:** "which DGMS form must this mine file", "draft a 24-hour mine accident notice", "Form J accident register entry".
- **You get:** A branded DOCX + PDF: the resolved obligation, the prescribed legacy form drafted (citing only the five verified DGMS anchors as values; any unverified form id recorded as `[GAP]`, never invented), and the OSH-Code transition note. Decision-support only — a competent (DGMS-qualified) person reviews it.
- **Pairs well with:** `mine-incident-investigation` (which overlays the same DGMS 24h-notice + Form-J reportability path) and `india-state-form-finder` for non-mine establishments.

### icmm-critical-control-management
- **Produces:** An ICMM CCM register for a material unwanted event in a mine — the identified critical controls, their performance requirements, verification activities + frequencies, and accountabilities, hierarchy-ranked with critical controls flagged.
- **For:** M, C · **Grounded in:** ICMM Critical Control Management (`KB-STD-ICMM-CCM`), the principal-hazard taxonomy (`KB-DATA-MINING-HAZARDS`), CCPS bow-tie technique (`KB-STD-CCPS-BOWTIE`); jurisdiction All · **Packs:** hse-mining
- **Use when:** You need to set up critical-control management for a mining principal hazard, structure a CCM workshop, or define verification activities for critical controls for a named material unwanted event.
- **Don't use for:** Drawing the bow-tie diagram itself (it points you at `bowtie-builder` by name) or building the wider PHMP (use `principal-hazard-management-plan`).
- **Have ready:** The commodity / mine type (sets the candidate MUE set + control families), the nominated critical controls and their performance/verification evidence, and the verification accountability role.
- **Trigger:** "set up critical control management for this mine", "structure an ICMM CCM workshop", "define verification for critical controls".
- **You get:** A branded DOCX + PDF CCM register: the material unwanted event, the critical controls (those that, if absent/failed, allow the event), per-control performance + verification activity + frequency + accountability, and a reference to `bowtie-builder` for the bow-tie itself. Assistive — it structures the workshop; a competent mine team owns the engineering judgement and live verification.
- **Pairs well with:** `bowtie-builder` (for the bow-tie diagram) and `principal-hazard-management-plan` (which links its critical controls back to this CCM).

### mine-incident-investigation
- **Produces:** A sector-tuned mining incident investigation — a de-identified, ICAM-led root-cause analysis with cause→evidence and CAPA→cause traceability, a hierarchy-of-controls CAPA, and the DGMS reportability overlay (24-hour accident notice + Form J entry).
- **For:** M, C · **Grounded in:** the B5 investigation flagship + DGMS overlay (`KB-REG-IN-DGMS`, region-resolved via `KB-REG-IN-STATEFORMS`); jurisdiction IN / All · **Packs:** hse-mining
- **Use when:** You need to investigate a mine accident, run an RCA on a mining incident, build a CAPA from a mining event, or determine DGMS reportability for a specific mining incident.
- **Don't use for:** Routine DGMS form filing with no investigation (use `dgms-statutory-pack`), or general non-mining incidents (use the core `incident-investigation`).
- **Have ready:** The event class + datetime, the DGMS region/zone (a mandatory gate), the involved-persons counts (drives <5-cell suppression), and the RCA method (ICAM is the default). De-identification runs FIRST and the intake echo-back shows personnel as role labels only.
- **Trigger:** "investigate this mine accident", "run an RCA on a mining incident", "is this mine event DGMS-reportable".
- **You get:** A branded DOCX + PDF: the de-identified timeline + evidence log, the ICAM RCA reaching organisational factors, the resolved DGMS reportability path (24h notice + Form J; only verified anchors cited, others `[GAP]`), and the HoC-tagged CAPA with named owners + due dates (incident-rate context only). Decision-support only — a competent (DGMS-qualified) person reviews it.
- **Pairs well with:** `dgms-statutory-pack` (shares the DGMS reportability path) and `capa-manager` for tracking the corrective actions to closure.

### mine-rescue-erp
- **Produces:** A mine-rescue emergency response plan for a specific mine — scenario-ranked emergencies, the rescue-team mobilisation sequence, mutual-aid / rescue-station links with credible timing, NDMA / DGMS alignment, and a drills schedule.
- **For:** M, C · **Grounded in:** the Mines Act / DGMS emergency-preparedness duty (`KB-REG-IN-MINES-ACT`) and the mining principal-hazard library (`KB-DATA-MINING-HAZARDS`); jurisdiction IN / All · **Packs:** hse-mining
- **Use when:** You need to draft or review a mine-rescue ERP, an emergency-preparedness plan for a mine, or a rescue-mobilisation procedure for a named mine.
- **Don't use for:** Investigating an emergency after the fact (use `mine-incident-investigation`) or building the underlying hazard/control plan (use `mine-ventilation-strata-blasting-plan` / `principal-hazard-management-plan`).
- **Have ready:** The rescue-team capability (trained-rescuer count, apparatus, certification — the realism anchor), the station + mutual-aid links with travel timing, the drill cadence + last-drill date, and (for India) the DGMS region/state.
- **Trigger:** "build a mine-rescue ERP", "draft an emergency-preparedness plan for this mine", "write a rescue-mobilisation procedure".
- **You get:** A branded DOCX + PDF: each emergency scenario ranked on the org matrix, the mobilisation sequence (team → station → mutual-aid → NDMA/DGMS) with credible timing, and a drills schedule with owner + date. It forces a realistic mobilisation (an aspirational placeholder is rejected; an unknown timing is `[GAP]`). The ERP is a draft for a competent person's sign-off.
- **Pairs well with:** `mine-ventilation-strata-blasting-plan` and `principal-hazard-management-plan` (which define the hazards the ERP responds to).

### mine-ventilation-strata-blasting-plan
- **Produces:** A site-specific ventilation plan, strata- (ground-) control plan, or blasting plan for a named mine — hazard-ranked on the org risk matrix, with a hierarchy-ranked control suite (critical controls flagged) and SMART follow-up actions.
- **For:** M, C · **Grounded in:** the Mines Act / DGMS plan duties (`KB-REG-IN-MINES-ACT`) and ICMM principal-hazard framing (`KB-STD-ICMM-CCM`, `KB-DATA-MINING-HAZARDS`); jurisdiction IN / All · **Packs:** hse-mining
- **Use when:** You need to draft or review a mine ventilation plan, a strata / ground-control plan, or a blasting / shotfiring plan for a specific opencast or underground mine.
- **Don't use for:** The broader principal-hazard management plan or CCM (use `principal-hazard-management-plan` / `icmm-critical-control-management`), or the emergency response (use `mine-rescue-erp`).
- **Have ready:** The plan type (which activates exactly one of the ventilation / strata / blasting parameter sets — the parameters are the plan), the commodity / mine type, the DGMS region/state (for India), and the sign-off competent-person role.
- **Trigger:** "build a mine ventilation plan", "draft a strata / ground-control plan", "write a blasting / shotfiring plan".
- **You get:** A branded DOCX + PDF: each hazard ranked on the org matrix, the control suite hierarchy-ranked (PPE/admin-only treatment of a principal hazard escalated), and follow-up actions with owner + due date. It forces site specificity — the actual commodity, method, and real parameters, never a generic template; a missing engineering value is `[GAP]`. A draft for a competent person's sign-off.
- **Pairs well with:** `principal-hazard-management-plan` (the parent hazard structure) and `mine-rescue-erp` (the emergency response to these hazards).

### principal-hazard-management-plan
- **Produces:** A principal-hazard management plan (PHMP) for a named mining principal hazard — a HIRA-structured hazard analysis risk-rated on the org matrix, a hierarchy-ranked control suite (critical controls flagged) with critical-control linkage to ICMM CCM, and monitoring with named owners + dates.
- **For:** M, C · **Grounded in:** ICMM CCM and the principal-hazard taxonomy (`KB-STD-ICMM-CCM`, `KB-DATA-MINING-HAZARDS`); jurisdiction All · **Packs:** hse-mining
- **Use when:** You need to develop a PHMP for a mine's principal hazard (ground/strata failure, inrush, fire/explosion, ventilation failure, mobile-plant interaction, fall from height, hazardous energy, respirable dust) or structure the PHMP workshop for a named principal hazard.
- **Don't use for:** The standalone critical-control workshop (use `icmm-critical-control-management`, which it builds on) or the concrete ventilation/strata/blasting plan documents (use `mine-ventilation-strata-blasting-plan`).
- **Have ready:** The commodity / mine type (sets the hazard mechanisms + control families), the named principal hazard + mine scenario, and the existing controls + monitoring data.
- **Trigger:** "develop a PHMP for this mine", "structure a principal-hazard management plan workshop", "manage ground/strata failure for this mine".
- **You get:** A branded DOCX + PDF PHMP: the HIRA-structured hazard analysis risk-rated on the org matrix, the hierarchy-ranked control suite (PPE/admin-only treatment of a principal hazard flagged), critical controls linked to the ICMM CCM with performance + verification carried over, and monitoring with owner + due date (gaps recorded as `[GAP]`, never fabricated). Assistive — it structures the multidisciplinary workshop; the mine team owns the engineering judgement.
- **Pairs well with:** `icmm-critical-control-management` (the critical-control linkage) and `mine-ventilation-strata-blasting-plan` (the concrete plan documents under the PHMP).

### bowtie-builder → see [Process Safety](Process-Safety#bowtie-builder)
Barrier (bow-tie) analysis for a major-accident hazard. Full card on the Process Safety page.
