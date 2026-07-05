<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3. -->
# MSIHC Major Accident Hazard On-Site Emergency Plan

## LPG Bottling Plant — Gujarat

| Document field | Value |
|---|---|
| Document type | On-site emergency plan (Major Accident Hazard installation, MSIHC framework — KB-REG-IN-MSIHC) |
| Installation | LPG bottling plant (bulk LPG storage, transfer, and cylinder filling) |
| State (detected and confirmed) | Gujarat — state-specific obligations resolved via KB-REG-IN-STATEFORMS |
| Prepared | 5 July 2026 |
| Status | DRAFT — pending competent-person review and Occupier sign-off |
| Classification | De-identified working copy — role labels only; see §15 Document Control & Data Protection |
| Next scheduled review | 5 January 2027, or earlier on any trigger in §13.3 |

---

## 1. Scope, Basis and Captured Facts

This plan covers the on-site emergency response arrangements for a major accident at the LPG bottling plant in Gujarat. It is prepared legacy-first under the current MSIHC framework (KB-REG-IN-MSIHC), with the PESO licensing context resolved from KB-REG-IN-PESO and state-specific obligations resolved from the Gujarat row of KB-REG-IN-STATEFORMS. The OSH-Code transition note is appended at §16.

**Captured facts (derived from the supplied installation notes):**

| # | Intake item | Captured value | Flag |
|---|---|---|---|
| 1 | Task | MSIHC on-site emergency plan (drafting) | — |
| 2 | Installation | LPG bottling plant: bulk LPG storage vessels, transfer system, cylinder filling and despatch | Activity mix beyond "bottling plant" is inferred from the installation class — [ASSUMPTION] |
| 3 | Capacity / inventory | Not supplied | **[GAP-01]** — total LPG inventory (vessel water capacity and maximum stored quantity) is unrecorded. Capacity gates the licence class, the licensing-authority tier, and the MAH threshold confirmation. Obtain from the design dossier / existing licence before filing. |
| 4 | PESO instrument | SMPV(U) Rules 2016 (storage vessels), per the KB-REG-IN-PESO row cited in the notes | Gas Cylinder Rules 2016 likely also engaged for the cylinder-filling activity — [ASSUMPTION], confirm from the KB-REG-IN-PESO rows |
| 5 | MAH status (MSIHC thresholds) | Treated as **Yes** — the request is for the MAH on-site emergency plan | [ASSUMPTION] — MAH status must be confirmed against the MSIHC threshold schedule once the LPG inventory ([GAP-01]) is documented; see §4 |
| 6 | State | **Gujarat** — detected and confirmed | — |
| 7 | Documents held | Not supplied | **[GAP-02]** — site/plot plan, capacity/design calculations, existing licence, and NOCs (fire / pollution / local) are unconfirmed; each is listed as a plan annexure at §17 |
| 8 | Licence validity / renewal deadline | Not supplied | **[GAP-03]** — obtain the current SMPV(U) licence validity date; the renewal timeline drives Action A-09 |
| 9 | Competent person / authority contact | Occupier (accountable-occupier role); Emergency Controller (on-site emergency-response role) | Role labels only — see §15 |
| 10 | Output and audience | Full on-site emergency plan; managers and external consultant reviewers; sector: industrial gases (LPG) | — |

---

## 2. Regulatory and Licensing Context (Legacy-First)

Every obligation below is cited from its matched KB row. No national form number is hard-coded; any form-id not verified against the KB row at drafting time is a literal [GAP] with a verification path.

| Obligation | Instrument | Form | Authority | KB source | Status |
|---|---|---|---|---|---|
| On-site emergency plan for a MAH installation | MSIHC framework | Plan document (this artifact); the specific rule reference and any prescribed submission format | State enforcement authority for MAH installations in Gujarat | KB-REG-IN-MSIHC + KB-REG-IN-STATEFORMS (Gujarat row) | **[GAP-04]** — verify the exact MSIHC rule reference, the prescribed plan-submission route, and the Gujarat authority designation from the KB rows before filing |
| Storage-vessel licence (bulk LPG vessels) | SMPV(U) Rules 2016 | **[GAP-05]** — form-id (e.g. LS-1A) unverified; cite only from the KB-REG-IN-PESO SMPV(U) row and confirm against the current PESO online system before filing | PESO — licensing-authority tier depends on vessel capacity, which is [GAP-01] | KB-REG-IN-PESO (SMPV(U) row) | Form-id and authority tier to be resolved from the KB row once capacity is documented |
| Cylinder-filling licence | Gas Cylinder Rules 2016 | **[GAP-06]** — form-id unverified; cite only from the KB-REG-IN-PESO Gas Cylinder row | PESO | KB-REG-IN-PESO (Gas Cylinder row) | [ASSUMPTION] that filling activity engages this instrument — confirm applicability and form from the KB row |
| State-specific siting / consent interactions | Gujarat state requirements | State forms per the Gujarat row | Gujarat state authority per the KB row | KB-REG-IN-STATEFORMS (Gujarat row) | **[GAP-07]** — enumerate the applicable Gujarat consents (fire NOC, pollution consent, local-body NOC) from the KB row and reconcile against documents held ([GAP-02]) |

**Discipline note:** this plan is a decision-support draft of the on-site emergency plan itself; it *references* the licensing pathway but does not substitute for the licence applications above.

---

## 3. Installation Profile

| Element | Detail | Flag |
|---|---|---|
| Installation class | LPG bottling plant: bulk storage vessels → pump/compressor transfer → cylinder filling → cylinder storage and despatch | Activity chain inferred from installation class — [ASSUMPTION] |
| Bulk receipt mode | Not supplied (road tanker / rail / pipeline) | **[GAP-08]** — receipt mode determines the transfer-area scenario set (S-01) and unloading controls; confirm before finalizing §8 |
| LPG inventory | Not supplied | [GAP-01] (see §1) |
| Site layout | Site/plot plan not held in the working file | [GAP-02] — the approved plot plan is Annexure A when available |
| Workforce | Headcount, shift pattern, and contractor presence not supplied | **[GAP-09]** — required to size assembly accounting (§9), first-aid cover (§10), and 24×7 emergency-controller coverage (§6) |
| Neighbouring land use | Not supplied | **[GAP-10]** — required for the off-site interface (§12) and for wind-direction assembly logic (§9) |
| Injury summary (aggregated) | 12 recordable injuries this period. Category-level detail is withheld wherever any category holds fewer than 5 individuals; those cells are aggregated upward and secondary suppression is applied so suppressed cells cannot be back-calculated from totals. | — |

---

## 4. MAH Determination

The installation is treated as a **Major Accident Hazard installation** for the purposes of this plan, consistent with the request and the installation notes. [ASSUMPTION]

This determination is **provisional**: the confirming comparison of the site's maximum LPG inventory against the MSIHC threshold schedule cannot be completed because the inventory is unrecorded ([GAP-01]). The threshold quantities themselves are not restated here — they must be read from KB-REG-IN-MSIHC at verification time, not from memory. **Action A-01** assigns this confirmation.

If the confirmed inventory falls below the MAH threshold, the statutory on-site-plan obligation changes character; the plan remains good practice but the filing pathway in §2 must be re-resolved.

---

## 5. Major Accident Scenario Register

This plan **references** major accident scenarios; it does not compute consequence results. Consequence classes below are qualitative placeholders pending the consequence-assessment study (**Action A-02**). No dispersion distance, thermal-radiation figure, or overpressure value appears in this plan and none may be added except from the completed study.

| ID | Scenario | Typical initiators | Detection route | Consequence class (qualitative) | Study reference |
|---|---|---|---|---|---|
| S-01 | LPG release during bulk transfer/unloading | Hose or coupling failure, drive-away, overfill | Fixed gas detection at transfer bay; operator observation | Potentially site-wide; escalation potential | **[GAP-11]** — consequence study not yet held |
| S-02 | Leak from storage vessel or associated pipework → flash fire or vapour cloud explosion | Flange/valve failure, corrosion, impact | Fixed gas detection; inventory monitoring | Potentially site-wide with off-site potential | [GAP-11] |
| S-03 | Fire impingement on a storage vessel → escalation up to BLEVE | Unmitigated S-01/S-02 pool or jet fire | Fire/flame detection; visual | Severe, with off-site potential | [GAP-11] |
| S-04 | LPG release in the filling hall | Filling-connection failure, valve passing, cylinder defect | Fixed gas detection in the filling hall | Localized to building; escalation potential | [GAP-11] |
| S-05 | Fire in cylinder storage / despatch yard | External ignition, vehicle incident | Visual; patrol; fire detection | Localized; escalation potential to bulk area | [GAP-11] |

The scenario set assumes the standard LPG-bottling activity chain ([ASSUMPTION], see §3) and must be re-baselined once the receipt mode ([GAP-08]) and plot plan ([GAP-02]) are confirmed.

---

## 6. Emergency Organisation and Responsibilities

All accountabilities are role labels. Named individuals are recorded only in the separate, access-controlled emergency contact register (§15) — never in this document.

| Role (label) | Emergency accountability |
|---|---|
| **Occupier (accountable-occupier role)** | Overall accountability for the plan's existence, adequacy, resourcing, statutory filing, and review. Authorizes mutual-aid agreements and off-site notifications policy. |
| **Emergency Controller (on-site emergency-response role)** | Takes command on plan activation: declares the emergency level, directs response teams, orders evacuation/assembly, authorizes plant shutdown beyond automatic action, initiates external notifications, and declares the all-clear. |
| **Deputy Emergency Controller (role — to be designated)** | Assumes the Emergency Controller's duties when that role-holder is absent or incapacitated. **[GAP-12]** — designation outstanding; 24×7 coverage across shifts cannot be confirmed until the shift pattern ([GAP-09]) is documented. Action A-03. |
| **Incident Controller (role — to be designated)** | Forward control at the incident scene; directs the fire/emergency team; reports to the Emergency Controller. [GAP-12] |
| **Fire & Emergency Team (roles)** | First-response firefighting and release control within trained limits; operates fixed systems under the Incident Controller. |
| **First-Aiders (roles)** | Casualty triage and first aid at the designated first-aid point; hand-off to external medical services. |
| **Security / Gate Controller (role)** | Controls site access, holds the gate log for assembly accounting, marshals external emergency services to the rendezvous point. |
| **Communications Coordinator (role)** | Executes the external notification sequence (§7.3) on the Emergency Controller's instruction; logs all notifications with times. |

**Succession:** Emergency Controller → Deputy Emergency Controller → senior-most trained shift role-holder present. The succession chain below deputy level is [GAP-12] pending shift-pattern confirmation.

---

## 7. Detection, Alarm and Communication

### 7.1 Detection (engineering controls — see §8 for the HoC-ranked register)

- Fixed flammable-gas detection covering the transfer bay, storage-vessel area, and filling hall, interlocked to **automatic isolation** of the LPG inventory (per the installation notes).
- Detection coverage adequacy against the S-01–S-05 scenario set is unverified — **[GAP-13]**; the coverage map is Action A-04.

### 7.2 Alarm stages

| Stage | Meaning | Signal | Triggered by |
|---|---|---|---|
| Alert | Confirmed gas detection or minor incident; response teams mobilize, no general evacuation | Distinct audible alert tone | Automatic on detection, or Emergency Controller |
| Site emergency | Major release/fire; general evacuation to assembly | Continuous site-wide siren | Emergency Controller |
| All-clear | Hazard controlled and verified | Distinct all-clear tone | Emergency Controller only |

Alarm audibility across all occupied areas (including despatch yard and any high-noise zones) is unverified — **[GAP-14]**; audibility test is folded into the first drill (Action A-06).

### 7.3 External notification sequence

On declaration of a site emergency, the Communications Coordinator notifies, in order: fire services → police → the Gujarat state enforcement authority for MAH installations → the district authority holding the off-site emergency plan → mutual-aid partners (§12). The authority designations and any statutorily prescribed notification timelines must be resolved from KB-REG-IN-STATEFORMS (Gujarat row) and KB-REG-IN-MSIHC — **[GAP-15]**. The live contact register is a separate access-controlled annexure (§15); no contact number appears in this document.

---

## 8. Scenario Response — Controls Register (Hierarchy of Controls)

Controls are ranked per the hierarchy of controls (KB-SNIP-HOC). No scenario is treated with PPE alone; PPE appears only as the final layer supporting higher-order controls.

| HoC tier | Control | Scenarios served | Status |
|---|---|---|---|
| Elimination / substitution | Inventory minimization — hold no more bulk LPG than the despatch schedule requires; eliminate redundant small-container storage in work areas | S-01–S-05 | Proposed — Action A-05; note that for an LPG installation the hazardous substance itself cannot be eliminated, which is the justification for the engineering-led profile below |
| Engineering | Fixed gas detection interlocked to **automatic isolation** of LPG inventory | S-01, S-02, S-04 | **In place** (per installation notes) |
| Engineering | Remotely operable / emergency shutdown isolation on vessel outlets and transfer lines | S-01–S-03 | **[GAP-16]** — installed scope unverified; verify against P&IDs (Action A-04) |
| Engineering | Fixed water spray / cooling on storage vessels (BLEVE prevention for S-03) | S-03 | **[GAP-17]** — presence and capacity unverified; verify (Action A-04) |
| Engineering | Earthing and bonding at transfer and filling points; ignition-source control by area classification | S-01, S-04 | [GAP-16] — verification within Action A-04 |
| Administrative | Transfer/unloading only under a written procedure with a dedicated attendant; drive-away prevention protocol | S-01 | Proposed — Action A-05 |
| Administrative | Permit-to-work for all hot work and line-breaking within the licensed area | S-02, S-03 | Proposed — Action A-05 |
| Administrative | Emergency drills and scenario exercises (§13) | All | Programmed — Action A-06 |
| PPE (last layer) | Flame-retardant workwear for transfer/filling operators; escape sets at defined points — supporting, never substituting, the layers above | All | **[GAP-18]** — current PPE issue standard unverified |

**Response actions per scenario (summary):** on any confirmed detection (S-01, S-02, S-04): automatic isolation actuates; Alert stage sounds; Fire & Emergency Team deploys upwind under the Incident Controller; escalation to Site Emergency on the Emergency Controller's judgment. On fire impingement of a vessel (S-03): immediate Site Emergency, general evacuation, external services notification, no re-entry until the Emergency Controller's all-clear. Detailed per-scenario action cards are Annexure C — **to be authored once [GAP-13]/[GAP-16]/[GAP-17] verification returns the true installed-control baseline** (Action A-07).

---

## 9. Evacuation, Assembly and Accounting

| Element | Detail | Control (HoC-ranked) |
|---|---|---|
| Primary assembly | Designated assembly area (per installation notes) | Engineered gas detection + automatic isolation protect the evacuation window; assembly siting itself is an administrative control |
| Secondary (cross-wind) assembly | Required so that assembly is never downwind of the release | **[GAP-19]** — location undesignated; requires the plot plan ([GAP-02]) and prevailing-wind data; Action A-08 |
| Wind indication | Windsocks visible from all occupied areas | [GAP-19] — count/placement with Action A-08 |
| Accounting | Roll-call against the gate log held by the Security / Gate Controller; visitors and contractors badge in/out and are escorted to assembly by their host role-holder | Administrative; depends on headcount data ([GAP-09]) |
| Unaccounted persons | Reported immediately to the Emergency Controller; search only by the Fire & Emergency Team under Incident Controller direction — no ad-hoc re-entry | Administrative |

---

## 10. Medical Response

- First-aid point at the assembly area, staffed by the First-Aiders (roles); first-aid cover per shift is sized once [GAP-09] resolves.
- Burn-injury capability is the priority competency for this installation class.
- Pre-arranged receiving hospital and ambulance response arrangement: **[GAP-20]** — not supplied; the Occupier (role) is to conclude and document the arrangement (Action A-08), with the hospital named only in the access-controlled contact register.

---

## 11. Shutdown and Utilities Isolation

- **Automatic:** gas detection actuates automatic isolation of LPG inventory (in place, per notes).
- **Commanded:** the Emergency Controller may order full plant shutdown — cease transfer and filling, isolate vessel outlets, trip non-essential electrical supply in the affected zone while preserving emergency lighting, firewater, and communications.
- Firewater supply autonomy (tank capacity and pump redundancy): **[GAP-21]** — unverified; folded into Action A-04.
- Post-isolation ignition-source sweep (vehicles stopped, no switching in the classified area) is an administrative standing order.

---

## 12. Mutual Aid and Off-Site Interface

- This on-site plan interfaces with the **district off-site emergency plan**; the preparing district authority for the site's district, the information the Occupier must furnish to it, and the furnishing timeline resolve from KB-REG-IN-MSIHC and KB-REG-IN-STATEFORMS (Gujarat row) — **[GAP-15]** (Action A-09).
- Mutual-aid agreements with neighbouring industrial units: **[GAP-22]** — none evidenced in the notes; the Occupier (role) to establish or document (Action A-08).
- External emergency services rendezvous point: the main gate, marshalled by the Security / Gate Controller; a site-familiarization visit for the local fire service is programmed with the first full drill (Action A-06).

---

## 13. Training, Drills and Plan Maintenance

### 13.1 Training

| Audience | Content | Frequency (plan design) |
|---|---|---|
| All persons on site (incl. contractors, at induction) | Alarm stages, assembly, accounting, role of the Emergency Controller | At induction + annual refresh |
| Fire & Emergency Team | LPG release/fire response within trained limits; fixed-system operation | Quarterly practical session |
| Emergency Controller / Deputy / Incident Controller (roles) | Command, escalation, external notification sequence, all-clear discipline | Twice yearly tabletop |

### 13.2 Drill programme (plan design)

Quarterly tabletop exercises rotating through scenarios S-01–S-05, and a full-site evacuation drill twice yearly, the first incorporating the alarm-audibility test ([GAP-14]) and a fire-service familiarization visit. **The statutory minimum drill frequency for MAH installations must be verified from KB-REG-IN-MSIHC — [GAP-23]; if the statutory minimum exceeds this programme, the statutory minimum governs.**

### 13.3 Plan review triggers

Review and re-issue on: any major accident or relevant near-miss; any change to inventory, plant, or organization ([GAP-01] resolution is itself a trigger); drill learnings; a change in the statutory framework (including the OSH-Code transition, §16); and in any case by 5 January 2027. The statutory plan-update interval must be verified from KB-REG-IN-MSIHC — folded into [GAP-23].

---

## 14. Action Tracker (SMART)

| ID | Action | HoC tier | Owner (role) | Due | Status |
|---|---|---|---|---|---|
| A-01 | Document the maximum LPG inventory and vessel water capacities; confirm MAH status against the MSIHC threshold schedule (KB-REG-IN-MSIHC) — closes [GAP-01] | — (verification) | Occupier (role) | 19 July 2026 | Open |
| A-02 | Commission the consequence-assessment study for scenarios S-01–S-05 — closes [GAP-11] | — (study) | Process Safety Engineer (role) | 30 September 2026 | Open |
| A-03 | Designate and train the Deputy Emergency Controller and Incident Controller (roles); confirm 24×7 succession against the shift pattern — closes [GAP-12], part of [GAP-09] | Administrative | Occupier (role) | 2 August 2026 | Open |
| A-04 | Verify the installed engineering baseline: gas-detection coverage map, ESD/remote isolation scope, vessel water-spray capacity, earthing/bonding, firewater autonomy — closes [GAP-13], [GAP-16], [GAP-17], [GAP-21] | Engineering (verification) | Site Engineering Lead (role) | 16 August 2026 | Open |
| A-05 | Issue the transfer/unloading procedure, permit-to-work standard, and inventory-minimization rule | Elimination + administrative | HSE Lead (role) | 30 August 2026 | Open |
| A-06 | Run the first full-site evacuation drill incl. alarm-audibility test and fire-service familiarization — addresses [GAP-14] | Administrative | Emergency Controller (role) | 27 September 2026 | Open |
| A-07 | Author per-scenario action cards (Annexure C) from the verified control baseline | Administrative | Emergency Controller (role) | 11 October 2026 | Open — sequenced after A-04 |
| A-08 | Designate the secondary cross-wind assembly area and windsocks; conclude the hospital/ambulance arrangement and mutual-aid agreements — closes [GAP-19], [GAP-20], [GAP-22] | Administrative | Occupier (role) | 30 August 2026 | Open |
| A-09 | Resolve from the KB rows: MSIHC rule reference and submission route ([GAP-04]), SMPV(U) and Gas Cylinder form-ids ([GAP-05], [GAP-06]), Gujarat consents ([GAP-07]), off-site-plan authority and notification timelines ([GAP-15]), statutory drill/review intervals ([GAP-23]); confirm current licence validity ([GAP-03]) | — (regulatory verification) | Regulatory Compliance Lead (role) | 2 August 2026 | Open |
| A-10 | Compile the access-controlled emergency contact register and file it separately from this plan | Administrative | Communications Coordinator (role) | 19 July 2026 | Open |

---

## 15. Document Control and Data Protection

- This plan uses **role labels only**. The mapping of role labels to individuals, and all contact details, live exclusively in the separate access-controlled emergency contact register (Action A-10). That register, and the re-identification key for the source notes, are stored apart from this document under restricted access and are never to be merged into any circulated copy.
- Injury data in §3 is aggregated: no category with fewer than 5 individuals is published, and secondary suppression prevents back-calculation from totals.
- Distribution: Occupier (role), Emergency Controller (role) and deputies, the statutory authority per §2 on filing, and the district authority per §12. Wider circulation (noticeboards, inductions) uses the §7.2 alarm table and §9 assembly instructions only — never this full document.

---

## 16. OSH-Code Transition Note (Legacy-First)

This plan is prepared **legacy-first**: it is drafted, and should be filed, under the MSIHC framework and the PESO instruments as they currently apply and as resolved from KB-REG-IN-PESO, KB-REG-IN-MSIHC, and KB-REG-IN-STATEFORMS (Gujarat row). The OSH Code is expected to subsume elements of this legacy framework on a state-notified timetable. Until the relevant provisions are brought into force and notified for Gujarat: file the forms the authority accepts **today**; do not adopt any anticipated new form numbering; and re-verify the instrument→form→authority resolution from the KB rows at every renewal and at each plan review (§13.3). The OSH-Code transition itself is tracked under Action A-09's verification sweep.

---

## 17. Consolidated Gap and Assumption Register

| Ref | Item | Verification path |
|---|---|---|
| [GAP-01] | LPG inventory / vessel capacities | Design dossier + existing licence; then MSIHC threshold check (A-01) |
| [GAP-02] | Documents held (plot plan, design calcs, licence, NOCs) | Occupier's licence file; annexe on receipt |
| [GAP-03] | Current licence validity / renewal date | Licence file (A-09) |
| [GAP-04] | MSIHC rule reference, plan submission route | KB-REG-IN-MSIHC (A-09) |
| [GAP-05] | SMPV(U) form-id (e.g. LS-1A — unverified) | KB-REG-IN-PESO SMPV(U) row + current PESO online system (A-09) |
| [GAP-06] | Gas Cylinder Rules form-id | KB-REG-IN-PESO Gas Cylinder row (A-09) |
| [GAP-07] | Gujarat state consents | KB-REG-IN-STATEFORMS Gujarat row (A-09) |
| [GAP-08] | Bulk receipt mode | Site confirmation; re-baseline S-01 |
| [GAP-09] | Headcount / shift pattern / contractors | HR and gate records (feeds A-03, §9, §10) |
| [GAP-10] | Neighbouring land use | Plot plan + district off-site plan interface |
| [GAP-11] | Consequence assessment results | Commissioned study (A-02) |
| [GAP-12] | Deputy EC / Incident Controller designation and succession | Occupier designation (A-03) |
| [GAP-13], [GAP-16], [GAP-17], [GAP-21] | Installed engineering baseline (detection coverage, isolation scope, vessel cooling, firewater) | Field verification vs P&IDs (A-04) |
| [GAP-14] | Alarm audibility | First drill test (A-06) |
| [GAP-15] | Off-site-plan authority, notification designations/timelines | KB-REG-IN-MSIHC + KB-REG-IN-STATEFORMS Gujarat row (A-09) |
| [GAP-18] | PPE issue standard | HSE Lead review within A-05 |
| [GAP-19], [GAP-20], [GAP-22] | Secondary assembly, hospital arrangement, mutual aid | Occupier arrangements (A-08) |
| [GAP-23] | Statutory drill frequency and plan-review interval | KB-REG-IN-MSIHC (A-09) |

Key assumptions: MAH status Yes pending A-01; standard LPG-bottling activity chain; Gas Cylinder Rules 2016 applicability to the filling activity.

---

## Limitations

This document is **decision-support only**. It is a draft prepared from the supplied installation notes with the gaps and assumptions recorded above; it is not legal advice and does not constitute a statutory filing. A **competent person** — and for this installation, the Occupier (role) with appropriately licensed/qualified support — must review, complete (closing every [GAP]), and approve this plan before it is relied upon, filed with any authority, or used in an emergency.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
