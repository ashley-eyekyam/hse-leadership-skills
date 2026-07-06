<!-- LOCKED fixture — owner-LOCKED at the SW4 19-05 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Critical Control Management Plan — Underground Fire (Principal Hazard)

**Facility type:** Underground coal mine · **Principal hazard:** Fire / explosion — *underground fire*
**Framework:** ICMM Critical Control Management (CCM) · Bowtie technique referenced to the shared **`bowtie-builder`** facilitator (CCPS/EI barrier method)
**Status:** DRAFT — decision-support / workshop-structuring output · **Issued:** 6 July 2026 · **Next full review due:** 6 July 2027

> **Decision-support notice.** This CCM plan structures the critical-control workshop for a competent mine team; it is **not** an autonomous engineering determination and **not** legal advice. Every critical control, performance requirement, verification activity, threshold and TARP setpoint marked `[GAP]` below must be set, tested and signed off by a **competent person** (Mine Manager / Ventilation Officer / Electrical & Mechanical Engineering Managers as relevant) against the mine's Principal Hazard Management Plan, Gas & Ventilation Management Plan, and the statutory coal-mining regime for the mine's jurisdiction *before* it is relied upon. The mine team owns the engineering judgement and the live verification.

---

## 1. Document control & accountabilities

| Role (accountable) | CCM responsibility |
|---|---|
| **Mine Manager (Senior Site Executive)** | Overall accountability for the underground-fire principal hazard, the critical-control suite, and this plan; approves the plan and any critical-control degradation/override. |
| **Underground Mine Manager** | Day-to-day accountability for control implementation underground; receives daily/shift exception reporting. |
| **Ventilation Officer** | Owns the atmospheric-monitoring, spontaneous-combustion and ventilation critical controls; owns gas-trend interpretation and the TARP. |
| **Electrical Engineering Manager** | Owns explosion-protected electrical equipment and electrical ignition-source controls. |
| **Mechanical Engineering Manager** | Owns conveyor, diesel-plant and fixed fire-suppression critical controls. |
| **Shift Deputy (Statutory Supervisor)** | Line-of-defence 1 verification on shift; enforces ignition-source/hot-work control at the working face. |
| **Control Room Operator (Gas Monitoring Officer)** | Continuous real-time monitoring; first responder to any TARP trigger. |
| **Mine Rescue Superintendent** | Owns emergency response, self-escape and mine-rescue capability. |
| **Technical Services Manager** | Owns the bowtie/CCM record, verification scheduling and assurance reporting. |
| **Board HSE Committee** | Governance oversight; receives quarterly critical-control assurance. |

*Role labels only — no individuals are named. Populate the named holder of each role in the controlled site copy, stored access-controlled and apart from any personal data.*

---

## 2. Material Unwanted Event (MUE)

**MUE:** *Ignition and establishment of an uncontrolled fire in the underground workings* — loss of control over the fire triangle (combustible fuel + oxygen in the ventilation stream + an ignition source) inside the confined underground environment, sustained beyond first-response suppression.

**Why material:** an established underground fire in a gassy coal mine is a credible pathway to **multiple fatalities** through toxic products of combustion, oxygen depletion and — critically — **transition to a methane/coal-dust explosion**. It is the highest-consequence, non-detonation escalation route for the fire/explosion principal hazard in the mining principal-hazard taxonomy.

---

## 3. Bowtie — underground fire

*Structured here for development in the `bowtie-builder` facilitator (this CCM plan does not re-author a bowtie engine). Barrier performance standards are recorded by the team; where the team has not supplied evidence the value is `[GAP]`. Critical controls (those whose failure is material) are marked* **[CC#]** *and carried into §4–§5.*

**Hazard:** Combustible materials (coal, coal fines/dust, diesel, hydraulic oil, FRAS belting, electrical insulation, timber) and flammable methane (firedamp) present in ventilation air, with potential ignition sources.

**Top event:** Ignition and establishment of an uncontrolled fire in the underground workings.

### 3.1 Threat side — causes → preventive controls

| # | Threat (cause of the top event) | Preventive controls (most-effective first) |
|---|---|---|
| **T1** | Spontaneous combustion (self-heating) of coal in goaf, pillars, ribs or standing coal reaching thermal runaway | Mine-planning/extraction to minimise standing coal & seal timeously *(Elimination/design)* · goaf inertisation & timely sealing *(Engineering)* · ventilation to remove heat *(Engineering)* **[CC5]** · **real-time CO / CO-make / Graham's-ratio monitoring [CC1]** *(Engineering)* |
| **T2** | Conveyor belt fire — frictional/mechanical heating (seized idler, drive slip, misalignment) igniting belting and accumulated coal fines | **Fire-resistant anti-static (FRAS) belting + belt-protection trips [CC2]** *(Engineering)* · **fixed automatic drive/gearbox suppression [CC7]** *(Engineering)* · coal-fines / spillage housekeeping *(Administrative)* |
| **T3** | Diesel mobile-equipment fire — fuel/hydraulic fluid onto hot engine/exhaust surface, or engine fault | Approved/temperature-limited engine & exhaust design *(Engineering)* · **engine-bay fixed fire suppression [CC7]** *(Engineering)* · hydraulic-hose & fuel-line standard, planned maintenance *(Engineering/Administrative)* |
| **T4** | Electrical ignition — cable fault, switchgear/transformer failure, arcing, overheating | **Explosion-protected (flameproof / intrinsically safe) certified equipment for the zone + earth-leakage/earth-fault protection [CC3]** *(Engineering)* · thermographic surveys *(Administrative verification)* |
| **T5** | Frictional ignition at the cutting face — picks striking rock/pyrites igniting methane or coal | **Machine-mounted methane monitor with automatic power cut-off + integrated water-spray suppression on the cutting drum [CC4]** *(Engineering)* · **face ventilation adequacy [CC5]** *(Engineering)* · pick condition/maintenance *(Administrative)* |
| **T6** | Hot work / open flame — welding, oxy-cutting, grinding, or unauthorised smoking materials | **Ignition-source & hot-work control: permit + continuous gas test + fire watch + contraband regime [CC6]** *(Administrative — see §5 flag)* |
| **T7** | Methane ignition/deflagration providing the ignition that establishes a sustained fire | **General-body & machine methane monitoring with trips [CC4]** · **primary/auxiliary ventilation dilution [CC5]** *(Engineering)* · statutory gas testing *(Administrative)* |

### 3.2 Consequence side — outcomes → mitigative controls

| # | Consequence (phrased *[damage] due to [event]*) | Mitigative controls (most-effective first) |
|---|---|---|
| **C1** | Multiple fatalities due to asphyxiation / CO & toxic products of combustion / heat, workers unable to escape | **Fire/CO/smoke detection, alarm & mine-wide warning [CC8]** *(Engineering)* · **self-escape system — SCSR, escapeways, lifelines, refuge chambers [CC9]** *(Engineering/Administrative)* |
| **C2** | Catastrophic explosion due to fire→methane/coal-dust transition | **Atmospheric monitoring & TARP-driven withdrawal [CC1]** · stone-dusting / coal-dust management *(Engineering)* · ventilation control **[CC5]** · **pre-planned sealing/inertisation [CC10]** |
| **C3** | Failed egress / entrapment due to loss of tenable atmosphere on escape routes | **Ventilation control-device integrity & escape-route tenability [CC5]** · **detection & warning [CC8]** · **self-escape system [CC9]** |
| **C4** | Loss of the mine / prolonged sealing & inertisation, major asset and community impact | **Emergency response & mine-rescue capability incl. sealing strategy [CC10]** · fixed suppression **[CC7]** |
| **C5** | Environmental release / regulatory prohibition due to combustion products, firewater and sealing | Emergency environmental & firewater-containment plan *(Administrative)* · **emergency response [CC10]** |

---

## 4. Selection of CRITICAL controls

**Criticality test applied to every candidate control:** *"If this control is absent or fails on its own, does the MUE become possible — or does it escalate to a fatality?"* A control passing this test is **critical (material)**; the rest are supporting controls that reduce likelihood or consequence but are not, alone, material.

**Ten critical controls were selected** (six preventive, four mitigative). Each gates a specific threat pathway or consequence escalation:

| CC# | Critical control | Type / HoC level | What it gates | Preventive / Mitigative |
|---|---|---|---|---|
| **CC1** | Real-time mine-atmosphere & spontaneous-combustion monitoring (CO, CO-make, O₂, CH₄, CO₂, Graham's ratio) | Engineering | T1, early detection for all; C2 | Preventive + Mitigative |
| **CC2** | FRAS conveyor belting + belt-protection trips (slip / bearing over-temp / misalignment) | Engineering | T2 | Preventive |
| **CC3** | Explosion-protected certified electrical equipment + earth-leakage/earth-fault protection | Engineering | T4 | Preventive |
| **CC4** | Machine-mounted methane monitor → auto power cut-off + cutting-drum water suppression | Engineering | T5, T7 (face) | Preventive |
| **CC5** | Primary & auxiliary ventilation adequacy + ventilation-control-device integrity | Engineering | T1, T5, T7; C2, C3 | Preventive + Mitigative |
| **CC6** | Ignition-source & hot-work control (permit + continuous gas test + fire watch + contraband regime) | **Administrative — flagged, see below** | T6 | Preventive |
| **CC7** | Fixed automatic fire suppression — conveyor drives/gearboxes & diesel engine bays | Engineering | T2, T3; C4 | Mitigative (at source) |
| **CC8** | Fire/CO/smoke detection, alarm & mine-wide emergency warning/communication | Engineering | C1, C3 | Mitigative |
| **CC9** | Self-escape system — compliant SCSRs, escapeways with lifelines, refuge chambers | Engineering + Administrative | C1, C3 | Mitigative |
| **CC10** | Emergency response & mine-rescue capability incl. pre-planned sealing/inertisation | Administrative / organisational | C1–C5 | Mitigative |

> **Lower-order control flag (KB-SNIP-HOC) — CC6 and CC10 are administrative/organisational.**
> **Justify or escalate:** CC6 (hot-work/ignition-source control) has no full higher-order elimination for *necessary* underground maintenance hot work; reliance is accepted **only** because it is backstopped by higher-order engineering controls (CC1 atmosphere monitoring, CC5 ventilation, CC7 suppression) and a permit that mandates continuous gas testing. CC10 (emergency response) is inherently organisational — it is a recovery barrier of last resort and does **not** substitute for the preventive engineering controls CC1–CC5. Neither is presented as a complete treatment of the hazard.

**Supporting (non-critical) controls** — reduce risk but not, alone, material: coal-fines/spillage housekeeping, stone-dusting, planned maintenance regimes, thermographic surveys, diesel fuel-handling standards, competency/training, workforce fire-response training. These feed the critical controls and appear in the bowtie but are managed through routine systems, not the critical-control verification regime.

---

## 5. Critical Control Register — performance requirement · verification · frequency · accountability

*Each control carries all four CCM attributes. Site-specific numeric setpoints are `[GAP]` — set by the competent person in the site plan; verification activities are real independent checks, never a restatement of the control.*

### CC1 — Real-time atmosphere & spontaneous-combustion monitoring
- **Performance requirement:** Continuous telemetric/tube-bundle monitoring of CO, CO-make, O₂, CH₄, CO₂ at all defined monitoring points, ≥ `[GAP]`% availability; CO-make and Graham's-ratio trends calculated and alarmed at TARP setpoints `[GAP]`; alarms annunciated in the control room within `[GAP]` seconds.
- **Verification activity:** (a) calibration & bump-test of each analyser against certified gas; (b) end-to-end alarm test to the control room; (c) audit of trend/Graham's-ratio calculation against manual sample results.
- **Frequency:** Calibration/bump — **weekly** (or per manufacturer/statutory schedule, whichever is shorter); alarm end-to-end test — **monthly**; trend-calculation audit — **quarterly**; continuous availability monitored **real-time**.
- **Accountable role:** Ventilation Officer · **Verifier:** Control Room Operator (routine) / Technical Services Manager (quarterly audit).

### CC2 — FRAS conveyor belting + belt-protection trips
- **Performance requirement:** All underground belting certified fire-resistant anti-static to the applicable standard; belt-slip, bearing/drive over-temperature and misalignment detection trips the conveyor within `[GAP]` seconds of the defined limit; no unapproved belt in service.
- **Verification activity:** (a) function test of slip/over-temp/misalignment trips by simulated fault; (b) belt-certification/register audit; (c) physical belt-condition inspection.
- **Frequency:** Trip function test — **weekly**; belt-condition inspection — **each shift** (visual) and **monthly** (detailed); certification-register audit — **quarterly**.
- **Accountable role:** Mechanical Engineering Manager · **Verifier:** Shift Deputy (shift visual) / Mechanical supervisor (function test).

### CC3 — Explosion-protected electrical equipment + earth-fault protection
- **Performance requirement:** All electrical apparatus in the hazardous zone certified explosion-protected (flameproof Ex d / intrinsically safe Ex i) appropriate to the gas zone, flameproof enclosure integrity maintained; earth-leakage/earth-fault protection operates within `[GAP]` and de-energises on fault; no defeated interlocks.
- **Verification activity:** (a) flameproof-enclosure integrity inspection (flange gaps, fasteners, glands); (b) earth-leakage/earth-fault trip test; (c) thermographic survey of switchgear/cables; (d) Ex register audit.
- **Frequency:** Enclosure integrity — **monthly**; earth-fault trip test — **monthly**; thermographic survey — **quarterly**; Ex register audit — **annual**.
- **Accountable role:** Electrical Engineering Manager · **Verifier:** Authorised electrical person / independent electrical auditor (annual).

### CC4 — Machine-mounted methane monitor → auto cut-off + drum suppression
- **Performance requirement:** Cutting-machine methane sensor de-energises the machine at `[GAP]`% CH₄ (indicative reference commonly ~1.25–2% general body — confirm against site Gas Management Plan and statutory limit); water-spray suppression on the cutting drum delivers `[GAP]` L/min at each pick bank; cut-off and sprays interlocked to machine operation.
- **Verification activity:** (a) gas-test the machine sensor with certified gas and confirm auto cut-off; (b) spray flow/pressure & nozzle-blockage check; (c) interlock defeat check.
- **Frequency:** Sensor cut-off test — **each shift before production** (statutory-style pre-use) + calibration **weekly**; spray check — **each shift**; interlock audit — **monthly**.
- **Accountable role:** Ventilation Officer (gas) / Mechanical Engineering Manager (sprays) · **Verifier:** Shift Deputy.

### CC5 — Ventilation adequacy + ventilation-control-device integrity
- **Performance requirement:** Air quantity/velocity at every working place ≥ the plan minimum `[GAP]` to dilute methane below `[GAP]`% and remove heat; ventilation-control devices (stoppings, seals, regulators, doors) maintained to design leakage `[GAP]`; primary fan availability ≥ `[GAP]`% with monitored fan-stoppage alarm.
- **Verification activity:** (a) ventilation survey — measured airflow vs plan at defined stations; (b) VCD/stopping integrity & seal inspection; (c) main-fan performance & stoppage-alarm test.
- **Frequency:** Ventilation survey — **weekly** (full) / **each shift** (statutory place inspection airflow check); VCD inspection — **weekly**; main-fan test — **monthly**.
- **Accountable role:** Ventilation Officer · **Verifier:** Shift Deputy (place inspection) / Technical Services (survey).

### CC6 — Ignition-source & hot-work control *(administrative — flagged §4)*
- **Performance requirement:** No hot work underground without an authorised permit; gas tested `[GAP]`% CH₄/O₂ before and continuously during; fire watch posted with charged extinguisher; contraband/smoking-materials search regime in force; 100% permit compliance.
- **Verification activity:** (a) permit-compliance audit against work actually done; (b) unannounced observation of a live hot-work task (gas test + fire watch present); (c) contraband-search records audit.
- **Frequency:** Permit audit — **weekly**; live-task observation — **monthly**; contraband-search audit — **monthly**.
- **Accountable role:** Underground Mine Manager · **Verifier:** Shift Deputy (task) / Technical Services (audit).

### CC7 — Fixed automatic fire suppression (conveyor drives & diesel engine bays)
- **Performance requirement:** Automatic detection-and-suppression on every conveyor drive/gearbox and diesel-engine bay; discharges within `[GAP]` seconds of detection; agent charge/pressure within spec; linked to plant shutdown.
- **Verification activity:** (a) detection-to-discharge function test (test mode); (b) agent charge/pressure & nozzle inspection; (c) shutdown-interlock test.
- **Frequency:** Charge/pressure inspection — **monthly**; function test — **quarterly**; interlock test — **quarterly**.
- **Accountable role:** Mechanical Engineering Manager · **Verifier:** Suppression-system competent technician.

### CC8 — Fire/CO/smoke detection, alarm & mine-wide warning
- **Performance requirement:** Detection at all defined fire-risk locations (belt roads, transformer/switchgear, fuel bays) alarms to the control room within `[GAP]` seconds; mine-wide emergency warning (audible/visual and/or stench-gas or equivalent) reaches all persons underground within `[GAP]` minutes; two-way emergency communication functional on all levels.
- **Verification activity:** (a) end-to-end detector→alarm→warning test; (b) coverage/blind-spot audit; (c) communication-system test on each level.
- **Frequency:** Detector→alarm test — **monthly**; mine-wide warning drill — **quarterly**; communications test — **weekly**.
- **Accountable role:** Ventilation Officer (detection) / Mine Rescue Superintendent (warning & comms) · **Verifier:** Control Room Operator / Emergency-response team.

### CC9 — Self-escape system (SCSR, escapeways, refuge)
- **Performance requirement:** Compliant SCSRs carried/cached to cover every person for the planned egress duration `[GAP]` minutes; two segregated escapeways maintained trafficable with continuous lifeline and directional signage; refuge chambers (where provided) rated for `[GAP]` persons × `[GAP]` hours with life-support serviceable.
- **Verification activity:** (a) SCSR serviceability/expiry & count audit; (b) escapeway walk-through — trafficability, lifeline continuity, signage; (c) refuge-chamber life-support & seal integrity test.
- **Frequency:** SCSR audit — **monthly**; escapeway walk-through — **weekly**; refuge-chamber test — **monthly**; full self-escape drill — **six-monthly**.
- **Accountable role:** Mine Rescue Superintendent · **Verifier:** Shift Deputy (escapeway) / Emergency-response team.

### CC10 — Emergency response & mine-rescue capability (incl. sealing/inertisation)
- **Performance requirement:** Current fire/emergency response plan with pre-planned sealing/inertisation strategy; trained brigade/mine-rescue cover available within `[GAP]`; TARP integrated with withdrawal criteria; incident-management roles rostered 24/7.
- **Verification activity:** (a) desktop/live emergency exercise against the fire scenario; (b) mine-rescue readiness & equipment audit; (c) TARP-and-withdrawal decision drill.
- **Frequency:** Live/desktop exercise — **six-monthly**; rescue-readiness audit — **monthly**; TARP drill — **quarterly**.
- **Accountable role:** Mine Manager (accountable) / Mine Rescue Superintendent (operational) · **Verifier:** Independent exercise assessor.

---

## 6. Consolidated verification schedule

| Frequency | Critical controls verified | Primary verifier | Reports into |
|---|---|---|---|
| **Continuous / real-time** | CC1 (availability), CC5 (fan status), CC8 (alarms) | Control Room Operator | Shift Deputy → Underground Mine Manager (exceptions immediately) |
| **Each shift** | CC2 (visual), CC4 (sensor cut-off + sprays), CC5 (place airflow), CC9 (escapeway) | Shift Deputy | Underground Mine Manager (statutory shift report) |
| **Weekly** | CC1 (calibration), CC2 (trip test), CC5 (survey/VCD), CC6 (permit audit), CC8 (comms), CC9 (escapeway detail) | Function owners | Ventilation Officer → Mine Manager (weekly critical-control summary) |
| **Monthly** | CC1 (alarm), CC3 (enclosure + earth-fault), CC4 (interlock), CC6 (live obs + contraband), CC7 (charge/pressure), CC8 (detector test), CC9 (SCSR + refuge), CC10 (rescue readiness) | Engineering Managers / Mine Rescue Supt | Mine Manager (monthly CCM performance report) |
| **Quarterly** | CC1 (trend audit), CC3 (thermographic), CC7 (function + interlock), CC8 (warning drill), CC10 (TARP drill) + independent CC audit | Technical Services / independent auditor | Board HSE Committee (quarterly assurance) |
| **Six-monthly** | CC9 (self-escape drill), CC10 (emergency exercise) | Mine Rescue Superintendent | Mine Manager → Board HSE Committee |
| **Annual** | CC3 (Ex register), full CCM & bowtie review, management review | Technical Services Manager | Mine Manager + Board HSE Committee |

---

## 7. Reporting, assurance & escalation cadence

**Three lines of defence:**
- **Line 1 — operate & self-verify:** control owners, operators, Shift Deputy (shift/daily checks).
- **Line 2 — functional oversight:** Ventilation Officer, Electrical/Mechanical Engineering Managers, Technical Services (scheduled verification, trend review).
- **Line 3 — independent assurance:** internal audit / external competent auditor and the regulator (quarterly/annual), reporting to the Board HSE Committee.

**Reporting rhythm:**
- **Real-time / shift:** any TARP trigger or failed critical control → **immediate** verbal + logged report from Control Room Operator / Shift Deputy to the Underground Mine Manager; Mine Manager notified for any Level-2+ trigger.
- **Daily:** Ventilation Officer reviews CO-make, Graham's-ratio and methane trends; daily control-status **exception** report to the Underground Mine Manager.
- **Weekly:** critical-control verification-completion summary (green/amber/red per control, overdue verifications, degraded controls) to the Mine Manager.
- **Monthly:** **CCM performance report** to the site leadership team — verification completion %, any critical control found failed/degraded, interim controls in place, TARP activations, overdue actions, trend of leading indicators.
- **Quarterly:** independent critical-control assurance report + material-risk update to the **Board HSE Committee**.
- **Annual:** full CCM/bowtie and management review; statutory/regulator interface.

**Critical-control failure escalation (applies whenever any critical control is found absent, failed or degraded):**
1. **Stop / make safe** the affected activity or area per the relevant TARP action.
2. **Notify** the accountable role + Underground Mine Manager immediately; Mine Manager for any preventive-control failure on a gassy panel.
3. **Interim control** authorised in writing by the Mine Manager (no reliance on a single remaining barrier without explicit risk acceptance).
4. **Log** in the critical-control register; **restore & re-verify** before normal work resumes; **root-cause** and preventive action tracked to closure.

---

## 8. TARP — Trigger Action Response Plan (underground fire)

*Setpoints marked `[GAP]` are site/seam-specific — set by the Ventilation Officer in the site Gas & Ventilation Management Plan and confirmed against the statutory limits for the mine's jurisdiction. Indicative reference values are shown only to illustrate direction and MUST be replaced/confirmed by the competent person; they vary by jurisdiction.*

| Level | Trigger (indicative — confirm & set) | Response action | Responsible role | Escalation |
|---|---|---|---|---|
| **Level 0 — Normal** | All monitored parameters within baseline; all critical controls green | Continue; routine verification & trend logging | Control Room Operator | Daily trend review — Ventilation Officer |
| **Level 1 — Notice / Alert** | CO-make rising above baseline / Graham's ratio trend up `[GAP]`; CH₄ approaching `[GAP]`% (ref. ~1.0–1.25%); belt/bearing temperature elevated; single non-critical control degraded | Increase monitoring frequency; investigate source; brief on-shift crew; verify supporting controls; prepare contingency | Shift Deputy + Ventilation Officer | Notify Underground Mine Manager same shift |
| **Level 2 — Alarm / High** | CH₄ at statutory action level `[GAP]`% (ref. ~1.25–2% — **de-energise / withdraw non-essential**); confirmed heating (CO-make/Graham's ratio at action setpoint `[GAP]`); fire detected & suppressed at source; a preventive critical control failed | De-energise affected electrical/plant; **stop production** in the affected panel; increase/redirect ventilation per plan; deploy first-response fire team; implement interim control; stand up incident room | Underground Mine Manager | **Notify Mine Manager immediately**; regulator per statutory duty |
| **Level 3 — Emergency / Withdraw** | CH₄ at withdrawal level `[GAP]`% (ref. ~2%); established/uncontrolled fire; fire→explosion-risk indicators; loss of ventilation control; failed atmosphere on an escapeway | **Withdraw all persons via escapeways using SCSRs**; account for all personnel; activate mine-rescue and pre-planned sealing/inertisation strategy; full emergency response | Mine Manager (Incident Controller) + Mine Rescue Superintendent | Statutory emergency notification to the regulator; external mutual-aid mine rescue |

---

## 9. Assumptions, gaps & required competent-person input

- **Jurisdiction not stated.** This plan is authored on the jurisdiction-independent ICMM CCM framing only; it cites **no** specific statute. The **statutory overlay** for the mine's country (e.g. the coal-mining safety & health regulations, gas & ventilation management-plan and self-escape requirements — in India the Mines Act / DGMS regime and prescribed forms) **must be added by the competent person** and its limits used as the binding TARP setpoints.
- **All `[GAP]` values** (analyser availability %, CH₄/CO-make/Graham's-ratio setpoints, airflow minimums, discharge/response times, refuge ratings, egress durations) are **site-specific engineering and statutory values** and are deliberately **not fabricated**. They must be populated from the mine's Principal Hazard Management Plan, Gas & Ventilation Management Plan and manufacturer/statutory data before this plan is used operationally.
- **Bowtie ownership.** The bowtie in §3 is structured for development in the `bowtie-builder` facilitator; barrier performance standards are recorded from the team's evidence, not asserted by this plan.
- **This is a workshop-structuring, decision-support artifact.** It does **not** autonomously determine the critical controls; it records the multidisciplinary mine team's CCM decisions for a competent person to test, complete and sign off. It precedes — and never replaces — the competent-person sign-off, and it does not certify the mine as compliant or the controls as adequate.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
