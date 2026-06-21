# Process Safety

The **hse-process** pack is the process-safety-management toolbox: the PHA/barrier workshop facilitators (HAZID, HAZOP, What-If, LOPA, bow-tie), the PSM/COMAH program backbones, and the permit, change, and asset-integrity controls that keep a major-accident-hazard facility safe. Install it if you run or advise an O&G, refining, or process plant — `/plugin install hse-process@hse-leadership-skills`. This page is the **home of the five shared PHA/barrier tools** (◆ below): they appear as full cards here and as one-line cross-reference stubs on the Chemicals and Mining pages they are also bundled into.

> ◆ = a **shared** skill. Its full card lives here on Process Safety; its **Packs** line shows its true multi-pack membership.

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### bowtie-builder
- **Produces:** A bow-tie / critical-control diagram for a named top event — threats with preventive barriers, consequences with mitigative barriers, each barrier carrying a performance standard.
- **For:** M, C · **Grounded in:** CCPS/EI bow-tie method; ICMM Critical Control Management · **Packs:** hse-process, hse-chemicals, hse-mining
- **Use when:** You need to map the barriers around a named hazard / top event ("build a bowtie for loss of containment of LPG", "set up the critical controls for the underground-fire principal hazard") — the most broadly shared assistive tool (◆ shared; bundled into chemicals and mining). 
- **Don't use for:** Identifying hazards from scratch (use [hazid-facilitator](#hazid-facilitator)) or a quantified protection-layer gap (use [lopa-worksheet](#lopa-worksheet)).
- **Have ready:** The specific top event, the bowtie-vs-CCM scope, the sector frame, and the team's barrier judgements with their performance-standard evidence.
- **Trigger:** "build a bowtie", "set up the critical controls", "critical-control diagram for this top event".
- **You get:** A structured bow-tie/CCM register — threats, preventive and mitigative barriers, each with a stated performance standard or a recorded `[GAP]` where the team's evidence is absent — plus a branded report.
- **Pairs well with:** [hazid-facilitator](#hazid-facilitator) (feeds the top events) and [icmm-critical-control-management](Mining#icmm-critical-control-management) in the mining pack.

### comah-safety-report-assistant
- **Produces:** A structured COMAH / Seveso III Safety Report argument — MAPP, the safety management system, establishment description, major-accident scenarios, the ALARP demonstration framing, and the internal emergency plan.
- **For:** M, C · **Grounded in:** COMAH Regulations / Seveso III Directive (UK, EU) · **Packs:** hse-process
- **Use when:** A UK/EU upper-tier duty-holder needs to structure or assemble its Safety Report ("structure our COMAH Safety Report", "set out the MAPP and SMS sections", "frame the ALARP demonstration").
- **Don't use for:** QRA or consequence modelling (done externally and fed in), or jurisdictions outside the COMAH/Seveso regime (use [psm-program-manager](#psm-program-manager) for OSHA PSM).
- **Have ready:** The named upper-tier establishment and tier, the duty-holder's content for each element, and any external QRA/ALARP numbers — unsupplied elements are recorded `[GAP]`.
- **Trigger:** "structure our COMAH Safety Report", "set out the MAPP and SMS sections", "frame the ALARP demonstration".
- **You get:** The assembled Safety Report argument by element, with `[GAP]` recorded for any unsupplied input, in a branded report — the skill never produces the report autonomously.
- **Pairs well with:** [psm-program-manager](#psm-program-manager) (the program backbone) and the PHA facilitators that supply the major-accident scenarios.

### hazid-facilitator
- **Produces:** A facilitated early-stage HAZID hazard register — hazard, cause, consequence, existing controls, risk rank, and recommendations tracked to closure, deliberately including external and environmental hazards.
- **For:** M, C · **Grounded in:** HAZID method (broad early-stage hazard identification) · **Packs:** hse-process, hse-chemicals
- **Use when:** You need to facilitate or write up a broad HAZID for a named installation / project phase ("structure a HAZID for the new tank farm", "set up our HAZID register for the FEED stage") — surfaces external, environmental, and process hazards (◆ shared; bundled into chemicals).
- **Don't use for:** A node-by-node deviation study (use [hazop-facilitator](#hazop-facilitator)) or a single-scenario protection-layer count (use [lopa-worksheet](#lopa-worksheet)).
- **Have ready:** The named installation and life-cycle stage, the workshop team, and the team's hazard identifications — the skill never invents hazards or fabricates a risk rank, recording `[GAP]` instead.
- **Trigger:** "structure a HAZID", "set up our HAZID register", "facilitate an early-stage hazard identification".
- **You get:** A structured HAZID register (hazard / cause / consequence / existing controls / risk rank / recommendations to closure) plus a branded report.
- **Pairs well with:** [hazop-facilitator](#hazop-facilitator) and [bowtie-builder](#bowtie-builder) (the top events HAZID surfaces flow into both).

### hazop-facilitator
- **Produces:** A node-based HAZOP worksheet — the guideword × parameter matrix and the deviation / cause / consequence / safeguard / recommendation record, with risk-ranked recommendations tracked to closure.
- **For:** M, C · **Grounded in:** IEC 61882 (HAZOP) · **Packs:** hse-process, hse-chemicals
- **Use when:** You need to facilitate or write up a HAZOP for a named node / P&ID section ("structure a HAZOP on the reactor feed line", "set up the guideword matrix for Node 4") — the live multidisciplinary team supplies the engineering judgement (◆ shared; bundled into chemicals).
- **Don't use for:** A broad first-pass hazard sweep (use [hazid-facilitator](#hazid-facilitator)) or a lighter procedure-level study (use [whatif-facilitator](#whatif-facilitator)).
- **Have ready:** The specific node, the parameters and guidewords, the P&ID, and the competent team — vague "do a HAZOP" requests are refused until the node is named.
- **Trigger:** "structure a HAZOP", "format our HAZOP worksheet", "set up the guideword matrix for this node".
- **You get:** The completed HAZOP worksheet (deviation / cause / consequence / safeguard / recommendation), risk-ranked recommendations to closure, and a branded report — `[GAP]` recorded rather than a fabricated engineering value.
- **Pairs well with:** [lopa-worksheet](#lopa-worksheet) (takes HAZOP scenarios deeper) and [management-of-change](#management-of-change).

### lopa-worksheet
- **Produces:** A single-scenario Layer of Protection Analysis worksheet — initiating event, independent protection layers with their independence tests, the residual-risk gap, and the SIL link.
- **For:** M, C · **Grounded in:** IEC 61511 (LOPA / functional safety) · **Packs:** hse-process, hse-chemicals
- **Use when:** You need to lay out one LOPA scenario for a named hazard ("set up a LOPA for the reactor high-pressure scenario", "lay out our IPL credits and residual gap") — one scenario at a time (◆ shared; bundled into chemicals).
- **Don't use for:** Computing PFD values or allocating a SIL (engineer-supplied and engineer-verified — the skill declines "calculate the SIL"), or multi-scenario screening (use [hazop-facilitator](#hazop-facilitator)).
- **Have ready:** The named scenario, the engineer's PFD values and IPL independence judgements, and the target SIL — unsupplied values are recorded `[GAP]`, never invented.
- **Trigger:** "set up a LOPA", "lay out our IPL credits", "structure the protection-layer gap for this scenario".
- **You get:** The structured LOPA worksheet with each IPL's independence tested and stated, the residual-risk gap, and a branded report.
- **Pairs well with:** [hazop-facilitator](#hazop-facilitator) (supplies the scenarios) and [bowtie-builder](#bowtie-builder).

### management-of-change
- **Produces:** A Management of Change (MoC) package — the technical basis for the change, a risk assessment of it, temporary-change expiry, the Pre-Start-Up Safety Review (PSSR) gate, and document/training updates.
- **For:** M, C · **Grounded in:** OSHA 1910.119(l) management of change; ISO 45001 8.1.3 · **Packs:** hse-process
- **Use when:** You need to prepare or review an MoC for a named, specific change ("MoC for replacing the relief valve on V-101", "risk-assess this temporary bypass", "build the PSSR checklist before start-up").
- **Don't use for:** A vague "a change" (the intake forces the exact change) or a standalone risk assessment unrelated to a change (use [risk-assessment](Core#risk-assessment)).
- **Have ready:** The exact change and its technical basis, any temporary-change duration, and the PSSR inputs — no start-up authorization is issued until the PSSR checklist passes.
- **Trigger:** "build an MoC", "risk-assess this change", "build the PSSR checklist before start-up".
- **You get:** The MoC package with the technical basis, change risk assessment, temporary-change expiry, the hard PSSR pre-start-up gate, and document/training updates, in a branded report.
- **Pairs well with:** [mechanical-integrity](#mechanical-integrity) and [psm-program-manager](#psm-program-manager) (MoC is a PSM element).

### mechanical-integrity
- **Produces:** A criticality-ranked equipment register with inspection/test/preventive-maintenance (ITPM) schedules, a hierarchy-of-controls deficiency-remediation plan, and SMART actions tracked to closure.
- **For:** M, C · **Grounded in:** OSHA PSM element (j) mechanical integrity; integrity-operating-windows framing · **Packs:** hse-process
- **Use when:** You need to build or review a mechanical-integrity program for a named equipment population / unit ("rank our pressure-vessel criticality", "set ITPM intervals for the Crude Unit", "manage these integrity deficiencies").
- **Don't use for:** A single change to one item (use [management-of-change](#management-of-change)) or the whole-program status view (use [psm-program-manager](#psm-program-manager)).
- **Have ready:** The named equipment population, the integrity basis, criticality inputs, and any deficiencies to manage.
- **Trigger:** "rank our equipment criticality", "set ITPM intervals", "manage these integrity deficiencies".
- **You get:** The criticality-ranked equipment register, ITPM schedules, integrity-operating-windows framing, a HoC-ranked deficiency-remediation plan, and SMART actions to closure, in a branded report.
- **Pairs well with:** [psm-program-manager](#psm-program-manager) (element (j)) and [management-of-change](#management-of-change).

### permit-to-work
- **Produces:** A permit-to-work package for a named high-risk task with a built-in SIMOPS (simultaneous operations) coordination section, every isolation and safeguard HoC-ranked, and conditions/actions tracked to closure.
- **For:** M, C · **Grounded in:** Permit-to-work and isolation practice; hierarchy of controls · **Packs:** hse-process
- **Use when:** You need to prepare or review a permit for a named high-risk task ("hot-work permit for welding on the pipe rack while the unit is running", "confined-space entry permit for Tank-3", "coordinate SIMOPS for the shutdown").
- **Don't use for:** A generic task risk assessment (use [risk-assessment](Core#risk-assessment)) or a pre-task crew briefing (use [toolbox-talk](Core#toolbox-talk)).
- **Have ready:** The specific task (hot work, confined-space entry, line breaking, excavation, working at height), the isolations, and any concurrent operations — SIMOPS is detected in the intake and routed to permit/coordination controls.
- **Trigger:** "hot-work permit", "confined-space entry permit", "coordinate SIMOPS".
- **You get:** The permit package with the isolations and safeguards HoC-applied, the SIMOPS coordination section, and the conditions and actions tracked to closure, in a branded report.
- **Pairs well with:** [job-safety-analysis](Core#job-safety-analysis) and [toolbox-talk](Core#toolbox-talk).

### peso-licensing-assistant
- **Produces:** An India PESO petroleum/explosives/pressure-vessel licensing package and the MSIHC Major Accident Hazard on-site emergency plan — installation and licence type resolved to the matched rule, form, and authority, legacy-first.
- **For:** M, C · **Grounded in:** India PESO licensing rules; MSIHC Rules (jurisdiction IN) · **Packs:** hse-process
- **Use when:** You need to prepare or check an India PESO licensing package ("what PESO licence do we need for an LPG bottling plant", "prepare the SMPV(U) Form LS-1A package", "draft the MSIHC on-site emergency plan for our MAH installation").
- **Don't use for:** Non-India process licensing, or factory/BOCW state returns (use [factories-act-returns](India-Compliance#factories-act-returns) / [bocw-compliance](India-Compliance#bocw-compliance)).
- **Have ready:** The installation and licence type, and the site state where the obligation is state-specific — the skill asks before citing if the state is unknown and never uses a hard-coded national form number.
- **Trigger:** "what PESO licence do we need", "prepare the SMPV(U) package", "draft the MSIHC on-site emergency plan".
- **You get:** The resolved rule → form → authority pathway cited from the KB row, the licensing package, the MSIHC on-site emergency plan, HoC-ranked controls and actions, and the OSH-Code transition note, in a branded report.
- **Pairs well with:** [india-msihc-mah-pack](Chemicals#india-msihc-mah-pack) and [comah-safety-report-assistant](#comah-safety-report-assistant).

### process-safety-kpi
- **Produces:** API RP 754 process-safety performance indicators — Tier-1 and Tier-2 Process Safety Event (PSE) counts and normalized rates, plus Tier-3/Tier-4 leading indicators.
- **For:** M, C · **Grounded in:** API RP 754 (process-safety performance indicators) · **Packs:** hse-process
- **Use when:** You need to count or frame process-safety KPIs for a named facility and reporting period ("compute our Tier-1 PSE rate for Q2", "frame our API RP 754 leading indicators").
- **Don't use for:** Occupational injury rates (TRIR/LTIFR/DART — use [incident-rate-calculator](Core#incident-rate-calculator)); the PSE pyramid is a distinct metric family.
- **Have ready:** The named facility, the reporting period, the PSE event facts, and the work-hours denominator — a missing or zero hours denominator is recorded `[GAP]`, never guessed.
- **Trigger:** "compute our Tier-1 PSE rate", "frame our API RP 754 leading indicators", "process-safety KPI for this period".
- **You get:** The Tier-1/Tier-2 PSE counts and normalized rates with fail-loud denominator discipline, the Tier-3/Tier-4 leading indicators, and a branded report.
- **Pairs well with:** [psm-program-manager](#psm-program-manager) and [board-safety-report](Core#board-safety-report).

### psm-program-manager
- **Produces:** An OSHA PSM 14-element status matrix — per element: status (compliant / gap / overdue), evidence, gap-risk band, and owner — with a HoC remediation plan and SMART actions tracked to closure.
- **For:** M, C · **Grounded in:** OSHA PSM, 29 CFR 1910.119 (14 elements) · **Packs:** hse-process
- **Use when:** You need to set up or review a PSM program for a named facility / covered process ("build our PSM 14-element status matrix", "where are our PSM gaps", "track our PHA / MoC / mechanical-integrity element status") — the program backbone the other process skills implement element-by-element.
- **Don't use for:** The UK/EU Safety Report regime (use [comah-safety-report-assistant](#comah-safety-report-assistant)) or a single element's detailed build (use the element-specific skill).
- **Have ready:** The named facility / covered process, the elements in scope, and the per-element evidence.
- **Trigger:** "build our PSM 14-element status matrix", "where are our PSM gaps", "track our PSM element status".
- **You get:** The 14-element status matrix (status / evidence / gap-risk band / owner), the HoC-ranked gap-remediation plan, and SMART actions to closure, in a branded report.
- **Pairs well with:** [management-of-change](#management-of-change), [mechanical-integrity](#mechanical-integrity), and [process-safety-kpi](#process-safety-kpi).

### whatif-facilitator
- **Produces:** A disciplined What-If question-set workshop record — What-If question, hazard/consequence, existing safeguards, risk rank, and recommendations tracked to closure.
- **For:** M, C · **Grounded in:** What-If analysis method (structured 'What if …?' question set) · **Packs:** hse-process, hse-chemicals
- **Use when:** You need to facilitate or write up a What-If analysis for a named process / operation ("run a What-If on the loading procedure", "structure our What-If question set for the start-up sequence") — lighter than a HAZOP, suited to procedures and simpler systems (◆ shared; bundled into chemicals).
- **Don't use for:** A rigorous node-by-node study (use [hazop-facilitator](#hazop-facilitator)) or a quantified protection-layer count (use [lopa-worksheet](#lopa-worksheet)).
- **Have ready:** The named process/operation, the scope, and the workshop team — the team supplies the answers; the skill never invents a consequence or fabricates a risk rank, recording `[GAP]` instead.
- **Trigger:** "run a What-If", "structure our What-If question set", "facilitate a What-If on this procedure".
- **You get:** The What-If record (question / hazard-consequence / existing safeguards / risk rank / recommendations to closure) and a branded report.
- **Pairs well with:** [hazop-facilitator](#hazop-facilitator) and [bowtie-builder](#bowtie-builder).
