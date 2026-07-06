<!-- LOCKED fixture — owner-LOCKED at the SW2 19-03 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Safety Performance Indicator / Safety Performance Target (SPI/SPT) Framework
## Unstabilised Approach & Runway Excursion — A320 Scheduled Operations

**SMS basis:** ICAO Annex 19, Pillar 3 — Safety Assurance (safety performance monitoring & measurement) · DGCA State Safety Programme (SSP) / Acceptable Level of Safety Performance (ALoSP)

### Document control

| Field | Entry |
|---|---|
| Operator | *[GAP — insert AOC-holder legal name and AOC number]* (the "Operator"); DGCA-certificated A320 scheduled passenger operator |
| Document reference | *[GAP — insert Operator SMS document reference]* |
| Version | 0.1 — **Draft for SRB ratification** |
| Date of issue | 5 July 2026 |
| Framework owner (author) | Safety Manager |
| Approving authority | Safety Review Board (SRB), chaired by the Accountable Manager |
| Data owner (flight data) | FDM Programme Manager |
| Applicable fleet / scope | Airbus A320 family, scheduled line operations |
| Focus hazards | Unstabilised approach (UA); runway excursion (RE) |
| Classification | Restricted — Safety (contains FDM-derived aggregate data) |
| Next review | At the first SRB following completion of the data baseline; thereafter **quarterly** (performance) and **annual** (re-baseline) |

> **Status of the numeric thresholds.** This framework defines the SPIs, their formulae, data sources, owners, cadence and the **method** for setting baselines, alert levels and targets. It does **not** state numeric baseline, alert or target *values*: these must be computed from the Operator's own historical FDM and occurrence data and are marked **[GAP]** throughout. No performance figure has been invented. All values are to be populated by the Safety Manager and ratified by the SRB before the framework goes live.

---

## 1. Purpose and scope

This framework establishes how the Operator **monitors and measures** the safety performance of its A320 scheduled operation against its two priority approach-and-landing hazards — **unstabilised approach** and **runway excursion** — using defined Safety Performance Indicators (SPIs) and Safety Performance Targets (SPTs), each with an alert level, a target level, an owning hazard/objective and an accountable role owner.

It is the **Pillar 3 (Safety Assurance)** instrument of the Operator's SMS. It:

- defines a **balanced set of leading and lagging SPIs** for UA and RE;
- specifies each SPI's **measurement basis and data source**;
- sets out the **baseline, alert-level and target-setting method** (statistical, from the Operator's own data);
- defines the **review cadence and accountable owners**; and
- describes how the SPIs **feed the Safety Review Board (SRB)** and, through it, the **DGCA State Safety Programme (ALoSP)**.

**In scope:** the SPI/SPT design, thresholds method, governance and reporting flow for UA and RE.
**Out of scope (handled by sibling SMS artifacts):** the full SMS manual (`aviation-sms-builder`); the hazard register and 5×5 risk classification of UA/RE (`aviation-hazard-register`); the SRB meeting record itself (`aviation-srb-minutes`); the analysis of raw flight data (`aviation-fdm-foqa-analysis`, which is assistive and structures FDM summaries — it does not ingest raw data here); and any individual occurrence investigation (`incident-investigation`).

---

## 2. Regulatory and management-system basis

| Basis | What it requires here | Reference |
|---|---|---|
| **ICAO Annex 19, Pillar 3 — Safety Assurance** | Safety performance is monitored and measured against **defined indicators and targets**, not judged by impression; underperformance drives corrective action and continuous improvement. | ICAO Annex 19 (2nd ed., 2016) + ICAO Doc 9859 *Safety Management Manual* (4th ed.) — element structure; the Operator holds the licensed documents. |
| **DGCA State Safety Programme (SSP) / ALoSP** | The Operator's SPIs/SPTs align to the DGCA SSP's **acceptable level of safety performance (ALoSP)**; aggregated performance is made available to the DGCA under SMS acceptance / continued oversight. | DGCA Civil Aviation Requirements (CAR Section 1 — General, the SMS/SSP series), adopting Annex 19. **Exact CAR Section/number and revision: [GAP]** — confirm against the current live DGCA CAR; do not cite a fixed number. |
| **Rate-computation discipline** | Lagging outcome rates are **computed** to a consistent definition (events × normaliser ÷ exposure), never invented; any external benchmark is quoted with its publishing body, sector and year. | Consistent with the shared `incident_rates` method; benchmark discipline per *BLS SOII / UK HSE / ILO (publishing bodies), methodology year 2026 — resolve the current figure at use time*. Note: aviation SPIs use aviation normalisers (per 1,000 approaches/landings; per 10,000 movements), **not** the OSHA 200,000-hour TRIR base. |

The SPIs close the Pillar-3 loop against Pillar-2 Safety Risk Management: the UA and RE hazards are identified and risk-classified in the hazard register (ICAO 5×5 Risk Classification Scheme); these SPIs test whether the **existing controls remain effective**; a sustained alert breach re-opens the hazard's risk rating and, where a change is involved, triggers management of change.

---

## 3. Definitions

- **SPI (Safety Performance Indicator)** — a measured parameter used to monitor and assess safety performance (leading or lagging).
- **SPT (Safety Performance Target)** — the planned target value/level of an SPI over a defined period; the "green" objective the Operator aims to hold or achieve.
- **Alert level** — the value/trigger at which an SPI's movement is deemed abnormal ("amber/red"), requiring investigation and action; derived statistically from the Operator's own baseline variability.
- **Baseline** — the historical average (and standard deviation, σ) of an SPI over an agreed reference period, from which the alert level and target are derived.
- **Leading (precursor) SPI** — measures conditions/behaviours *before* an outcome (e.g. unstable-approach rate); predictive.
- **Lagging (outcome) SPI** — measures realised outcomes/occurrences (e.g. runway excursions); reactive.
- **Stabilisation gate** — the height by which an approach must meet all stabilised-approach criteria. **[ASSUMPTION]** taken as **1,000 ft AAL in IMC and 500 ft AAL in VMC** per typical A320 SOP — **confirm against the Operator's OM-A / FCOM stabilised-approach policy.**
- **Movement** — one take-off or one landing (used as the RE-family exposure denominator).

---

## 4. Hazards and safety objectives these SPIs serve

Each SPI maps to one owning hazard and to a stated safety objective. The hazards and their ICAO 5×5 classification are owned by the hazard register (`aviation-hazard-register`); the identifiers below are the linking references.

| Ref | Owning hazard (from the hazard register) | Safety objective the SPIs support |
|---|---|---|
| **AV-H-UA** | Unstabilised approach continued below the stabilisation gate → hard/heavy landing, loss of control, or runway excursion. | **SO-UA:** Every approach is stabilised by the gate, or a go-around is flown — 100% compliance with the stabilised-approach / go-around policy. |
| **AV-H-RE** | Runway excursion (overrun or veer-off) on landing or rejected take-off. | **SO-RE:** Zero runway excursions; landing energy and margins kept within policy. |

> An SPI that maps to neither hazard/objective is an orphan indicator and would be flagged. Every SPI in §5 carries an owning reference.

---

## 5. The SPI catalogue

Nine SPIs — **6 leading + 3 lagging**, split across the two hazards. The mix is deliberately **leading-weighted**: UA and RE outcomes are (in a well-run operation) low-frequency, so the monitoring load is carried by FDM-derived precursors, with the lagging outcomes retained as the ultimate test and as any-occurrence triggers. Both hazard families carry both an outcome and its precursors, so the set passes the leading/lagging balance test.

### 5.1 SPI register at a glance

| SPI ID | Title | Class | Owning hazard | Primary data source | Period |
|---|---|---|---|---|---|
| SPI-UA-01 | Unstable approach rate | Leading | AV-H-UA | FDM/FOQA | Monthly, rolling-12 |
| SPI-UA-02 | Go-around policy compliance | Leading | AV-H-UA | FDM + ASR | Monthly, rolling-12 |
| SPI-UA-03 | Approach FDM exceedance rate (composite) | Leading | AV-H-UA | FDM/FOQA | Monthly, rolling-12 |
| SPI-UA-04 | Unstable-approach / hard-landing occurrence rate | Lagging | AV-H-UA | ASR/MOR + maintenance | Monthly, rolling-12 |
| SPI-RE-01 | Long / fast / floated landing rate | Leading | AV-H-RE | FDM/FOQA | Monthly, rolling-12 |
| SPI-RE-02 | Reduced landing-distance-margin ops rate | Leading | AV-H-RE | FDM + dispatch/ops | Monthly, rolling-12 |
| SPI-RE-03 | Deceleration / directional-control exceedance rate | Leading | AV-H-RE | FDM/FOQA | Monthly, rolling-12 |
| SPI-RE-04 | Runway excursion event rate | Lagging | AV-H-RE | MOR/ASR + investigation | Rolling-12 & 36-month |
| SPI-RE-05 | Runway-excursion precursor occurrence rate | Lagging | AV-H-RE | ASR/MOR | Monthly, rolling-12 |

### 5.2 Detailed SPI definitions

Each SPI carries: definition · formula · measurement basis · data source · period · owning hazard/objective · accountable owner. Baseline/alert/target values are set by the method in §7 and are **[GAP]** pending the Operator's data.

---

**SPI-UA-01 — Unstable Approach Rate** *(Leading)*
- **Definition:** approaches assessed by FDM as **not stabilised at the applicable stabilisation gate**, per 1,000 approaches with valid FDM data.
- **Formula:** (FDM-flagged unstable approaches ÷ total approaches with valid FDM data) × 1,000
- **Measurement basis:** FDM stabilised-approach algorithm evaluated at the gate (speed, path, vertical speed, configuration, thrust) **[ASSUMPTION: 1,000 ft IMC / 500 ft VMC — confirm].**
- **Data source:** FDM/FOQA (aggregate, de-identified).
- **Maps to:** AV-H-UA / SO-UA. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** FDM Programme Manager.

**SPI-UA-02 — Go-Around Policy Compliance** *(Leading)*
- **Definition:** of the approaches flagged unstable at/after the gate, the **% where a go-around was flown** rather than continued to a landing. This is the decisive UA→RE barrier. Higher is better; the complement ("continued-to-land while unstable" rate) is the failure mode.
- **Formula:** (unstable approaches with a go-around executed ÷ total unstable approaches at/after the gate) × 100
- **Measurement basis:** FDM go-around detection cross-checked with crew Air Safety Reports.
- **Data source:** FDM/FOQA + ASR.
- **Maps to:** AV-H-UA / SO-UA. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** FDM Programme Manager. **Action delivery:** Chief Pilot (A320 fleet), Nominated Postholder – Crew Training.

**SPI-UA-03 — Approach FDM Exceedance Rate (composite)** *(Leading)*
- **Definition:** rate of the specific approach-phase exceedance events that drive UA — high rate of descent below the gate, glidepath deviation (high/low), high approach energy/speed, and late landing configuration — per 1,000 approaches.
- **Formula:** (sum of defined approach-phase exceedance events ÷ total approaches) × 1,000
- **Measurement basis:** the Operator's FDM event library for the approach phase. **[ASSUMPTION:** the exact event set and trigger thresholds are defined by the FDM programme — **confirm and list them as a sub-schedule].**
- **Data source:** FDM/FOQA.
- **Maps to:** AV-H-UA / SO-UA. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** FDM Programme Manager.

**SPI-UA-04 — Unstable-Approach / Hard-Landing Occurrence Rate** *(Lagging)*
- **Definition:** reported approach-and-landing occurrences attributable to a destabilised approach — hard/heavy landing, tail strike, bounced landing, and unstable-approach ASRs — per 1,000 sectors.
- **Formula:** (relevant ASR/MOR occurrences ÷ sectors flown) × 1,000
- **Measurement basis:** occurrence reporting + maintenance hard-landing inspection triggers.
- **Data source:** ASR/MOR + maintenance records.
- **Maps to:** AV-H-UA / SO-UA. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** Safety Manager.

**SPI-RE-01 — Long / Fast / Floated Landing Rate** *(Leading)*
- **Definition:** FDM-detected high-energy landings — touchdown beyond the touchdown zone / long flare, excess threshold or touchdown speed, extended float — per 1,000 landings.
- **Formula:** (FDM high-energy-landing events ÷ total landings) × 1,000
- **Measurement basis:** FDM landing-phase event set (touchdown point/distance, VAPP excess, flare duration).
- **Data source:** FDM/FOQA.
- **Maps to:** AV-H-RE / SO-RE. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** FDM Programme Manager.

**SPI-RE-02 — Reduced Landing-Distance-Margin Ops Rate** *(Leading)*
- **Definition:** landings conducted on **wet/contaminated runways**, with a tailwind, or where the computed landing-distance margin was **below the Operator's policy threshold**, per 1,000 landings.
- **Formula:** (landings meeting the reduced-margin criteria ÷ total landings) × 1,000
- **Measurement basis:** FDM (touchdown, deceleration) combined with dispatch/ops data (runway condition, OFP / in-flight landing-performance assessment). **[ASSUMPTION:** the margin threshold is per OM-A/OM-B — **confirm].**
- **Data source:** FDM/FOQA + dispatch/operations records.
- **Maps to:** AV-H-RE / SO-RE. **Accountable owner:** Nominated Postholder – Flight Operations. **Contributing owner:** Nominated Postholder – Ground Operations (runway condition reporting/dispatch). **Data monitor:** FDM Programme Manager.

**SPI-RE-03 — Deceleration / Directional-Control Exceedance Rate** *(Leading)*
- **Definition:** FDM-detected late or reduced braking, low/late reverser deployment, high groundspeed approaching the runway-end threshold, or lateral-deviation / veer events, per 1,000 landings.
- **Formula:** (relevant FDM deceleration/directional events ÷ total landings) × 1,000
- **Measurement basis:** FDM landing-roll event set.
- **Data source:** FDM/FOQA.
- **Maps to:** AV-H-RE / SO-RE. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** FDM Programme Manager.

**SPI-RE-04 — Runway Excursion Event Rate** *(Lagging — high-consequence)*
- **Definition:** confirmed runway excursions (overrun or veer-off, including rejected-take-off overruns) per 10,000 aircraft movements.
- **Formula:** (runway excursion events ÷ movements) × 10,000
- **Measurement basis:** MOR/ASR classification confirmed by investigation.
- **Data source:** MOR/ASR + occurrence-investigation records.
- **Trigger discipline:** as a rare, catastrophic-potential outcome, **any single occurrence** triggers a mandatory SRB review and an internal investigation (`incident-investigation`) — this SPI is monitored on an event-trigger basis, not solely on a statistical trend (see §7.4).
- **Maps to:** AV-H-RE / SO-RE. **Accountable owner:** Accountable Manager (through the SRB). **Data monitor:** Safety Manager.

**SPI-RE-05 — Runway-Excursion Precursor Occurrence Rate** *(Lagging)*
- **Definition:** reported RE-precursor occurrences — runway-overrun-risk events, abnormal runway contact / directional-control events, and runway condition found worse than reported — per 10,000 movements.
- **Formula:** (RE-precursor occurrences ÷ movements) × 10,000
- **Measurement basis:** occurrence reporting classified against a defined RE-precursor taxonomy.
- **Data source:** ASR/MOR.
- **Maps to:** AV-H-RE / SO-RE. **Accountable owner:** Nominated Postholder – Flight Operations. **Data monitor:** Safety Manager.

---

## 6. Measurement basis, data sources and data protection

### 6.1 Data sources

| Source | Feeds | Notes |
|---|---|---|
| **FDM/FOQA** (aggregate) | UA-01, UA-02, UA-03, RE-01, RE-02, RE-03 | Primary source for all leading precursors. Requires valid-data coverage rate to be tracked as a data-quality control (a low FDM read-out rate invalidates the leading SPIs). |
| **ASR / MOR** (occurrence reporting) | UA-02 (go-around corroboration), UA-04, RE-04, RE-05 | Reporting-rate itself is monitored (a falling report rate can mask, not improve, performance — anti-gaming guardrail, §7.5). |
| **Dispatch / operations data** | RE-02 (runway condition, tailwind, computed margin) | Runway state and performance-calculation records. |
| **Maintenance records** | UA-04 (hard-landing inspections) | Confirms/hardens self-reported hard landings. |
| **Exposure denominators** | all rates | Approaches, landings, sectors, movements — **[GAP]:** obtain from the Operator's ops/scheduling data; rates cannot be computed without them. |

### 6.2 Data protection and FDM identity handling (mandatory)

FDM data can re-identify individual crews, and identity protection is load-bearing for the whole programme's trust and its just-culture agreement. Therefore:

- The SPI dashboard and all SRB/SSP reporting carry **aggregate rates only** — no crew, flight-number, route, base, registration or date identifiers.
- **Small-number suppression:** any occurrence category with **fewer than 5 events** is not published at a disaggregated level; it is aggregated up, with secondary suppression so suppressed cells cannot be back-calculated from totals.
- Any crew-identifying FDM key is held by the **FDM gatekeeper** under the Operator's FDM/just-culture agreement, **access-controlled and stored separately** from this framework and its dashboards. No name↔event mapping appears in any SPI artifact.
- FDM data is used to monitor **trends and system performance**, not individual performance management.

---

## 7. Baseline, alert-level and target (SPT) setting method

> All numeric outputs of this section are **[GAP]** until computed from the Operator's own historical data. The method is fixed here; the numbers are the Operator's.

### 7.1 Baseline

For each SPI, compute the **baseline** from the Operator's historical monthly values over an agreed reference period:

- **Baseline mean (x̄)** = arithmetic mean of the monthly SPI values over the reference period.
- **Baseline variability (σ)** = standard deviation of those monthly values.
- **Reference period:** the most recent **12 consecutive months** of good-quality data for the higher-frequency leading SPIs; a **longer 24–36-month window** for the low-frequency lagging SPIs (UA-04, RE-04, RE-05), whose monthly values are frequently zero and would otherwise give an unstable σ.

**Baseline values: [GAP]** — populate x̄ and σ per SPI once ≥12 months of data exist. Where a full reference period is not yet available, record the SPI as *baseline-pending* and monitor on the event-trigger basis (§7.4) until the baseline matures.

### 7.2 Alert level (the amber/red trigger)

Alert levels are derived from baseline variability using the **standard "mean + n·σ" method with three out-of-region trigger criteria**, evaluated each measurement period. For a *lower-is-better* SPI, the SPI is in the **alert (amber/red) region** when any of:

- **C1:** a single point exceeds **x̄ + 3σ**; or
- **C2:** two consecutive points exceed **x̄ + 2σ**; or
- **C3:** three consecutive points exceed **x̄ + 1σ**.

For the *higher-is-better* SPI (**SPI-UA-02, go-around compliance**), invert the test: the SPI is in the alert region when performance **falls below** the corresponding **x̄ − 1σ / − 2σ / − 3σ** lines on the same C1–C3 criteria, or below a defined compliance floor.

**Alert-level values: [GAP]** — the x̄ + n·σ lines are computed once the baseline exists.

### 7.3 Target level (SPT)

The **SPT** is the planned performance for the review year, set by the SRB from the baseline:

- **Improvement target** (leading precursor rates and lagging rates): a defined **reduction from baseline** over the review period, ratified by the SRB — *stretch but credible and risk-matched*. **Magnitude: [GAP]** pending baseline (an aspirational target with no baseline is flagged and not set). The SPT must sit at or better than the baseline mean and inside the alert level.
- **Attainment target** (objective-level SPIs, defensible without a baseline number):
  - **SPI-UA-02 (go-around compliance):** SPT = **100% policy compliance** (every unstable approach at/after the gate results in a go-around). The alert *floor* below which compliance is deemed degraded is **[GAP]** pending baseline.
  - **SPI-RE-04 (runway excursions):** SPT = **zero runway excursions** (consistent with SO-RE). Any single occurrence is an alert (§7.4).

### 7.4 Special handling of rare, high-consequence outcomes

For **SPI-RE-04** (and, at the Operator's discretion, UA-04/RE-05), the sigma method is unreliable near a zero mean. These SPIs are therefore monitored on an **event-trigger basis**: **any occurrence** triggers a SAG review and investigation, and the rolling count is trended over the longer window. A discrete alert count over the rolling period may additionally be set by the SRB — **value [GAP].**

### 7.5 Anti-gaming safeguards

- **Never target a raw report count downward.** UA-04, RE-05 and the ASR corroboration of UA-02 are paired with a **reporting-rate / reporting-quality safeguard**, so a fall in reported occurrences is not mistaken for improvement (it may signal under-reporting).
- **FDM valid-data coverage** is tracked as a data-quality gate on every FDM-derived SPI; a leading SPI is not reported "green" on thin data.
- Targets are matched to the SMS/safety-culture maturity and reviewed for credibility at re-baseline.

### 7.6 Performance status and escalation

Each SPI is presented on the dashboard as **green** (at/inside target), **amber** (between target and alert), or **red** (alert level breached per §7.2/§7.4). An amber/red status triggers the escalation in §8.3.

---

## 8. Review cadence, governance and accountable owners

### 8.1 Governance forums and cadence

| Forum | Frequency | Chair / lead (role) | SPI role |
|---|---|---|---|
| **SPI dashboard compilation** | **Monthly** | Safety Manager | Compiles all SPIs from FDM + reporting + ops data; applies de-identification and small-number suppression; assigns green/amber/red status. |
| **Safety Action Group (SAG)** | **Monthly** | Nominated Postholder – Flight Operations (supported by the Safety Manager) | Working-level review; investigates every amber/red SPI; raises and tracks corrective actions with owners and due dates; prepares the SRB brief. |
| **Safety Review Board (SRB)** | **Quarterly (minimum)** | Accountable Manager | Strategic review of SPI performance vs alert/target and vs ALoSP; ratifies baselines, alert levels and SPTs; endorses actions and the DGCA submission; recorded via `aviation-srb-minutes`. |
| **Alert-breach review** | **Event-driven** | SAG (escalating to SRB) | Immediate review on any alert breach or SPI-RE-04 occurrence (§8.3). |
| **Re-baseline** | **Annual** | Safety Manager → SRB | Recomputes baselines/σ; the SRB re-sets alert levels and SPTs. |

### 8.2 Accountable owners (roles)

| Responsibility | Accountable role |
|---|---|
| Overall accountability for safety performance and ALoSP (owns the DGCA relationship) | **Accountable Manager** |
| The SPI/SPT framework — design, monthly compilation, de-identification, alert triggering, re-baseline | **Safety Manager** |
| Operational accountability for the UA and RE SPIs and the corrective actions | **Nominated Postholder – Flight Operations** |
| FDM data quality, FDM-derived SPI values, FDM identity protection | **FDM Programme Manager** |
| Runway-condition / dispatch inputs to RE-02 | **Nominated Postholder – Ground Operations** |
| Training-based corrective actions (stabilised-approach & go-around, energy-management, RE avoidance) | **Nominated Postholder – Crew Training** |
| Fleet-level SOP/technique actions | **Chief Pilot (A320 fleet)** |

> Every SPI in §5 names an accountable owner and a data monitor; a metric that nobody owns would be flagged and is not admitted to the register.

### 8.3 Escalation on an alert breach

1. **Detect** — the Safety Manager flags the SPI red/amber on the monthly dashboard (or an SPI-RE-04 occurrence is reported).
2. **Investigate** — the SAG reviews the underlying data at its next (or an ad-hoc) meeting; for SPI-RE-04, an investigation is opened immediately.
3. **Act** — the SAG raises corrective/preventive actions with a **named role owner and due date** (SMART), routed to Flight Operations / Training / Ground Operations as applicable.
4. **Escalate** — if the trend continues or the action proves ineffective, the Safety Manager escalates to the SRB, which may **re-open the hazard's ICAO 5×5 risk rating** in the hazard register and mandate further mitigation through the hierarchy of controls (design/engineering and procedural barriers before reliance on crew vigilance / awareness alone).
5. **Close** — the action's effectiveness is confirmed by the SPI returning inside its alert level over the following periods; closure is recorded at the SRB.

---

## 9. How the SPIs feed the SRB and the SSP (ALoSP)

### 9.1 Internal flow — into the SRB

```
FDM/FOQA + ASR/MOR + dispatch/ops + maintenance
        │  (aggregate, de-identified; small-number suppression applied)
        ▼
Safety Manager — monthly SPI dashboard (green / amber / red vs alert & target)
        ▼
Safety Action Group (SAG) — monthly analysis, investigates breaches, raises SMART actions
        ▼
Safety Review Board (SRB) — quarterly: reviews performance vs alert/target & ALoSP,
   ratifies baselines/alert levels/SPTs, endorses actions      → recorded in aviation-srb-minutes
        ▼
Accountable Manager — endorses safety performance & the ALoSP position
```

The SPIs are the standing **"safety performance monitoring & measurement"** agenda item at each SRB. The SRB's decisions (target ratification, action endorsement, closures) are captured in the SRB minutes and feed back as the tasking for the next cycle — closing the Pillar-3 continuous-improvement loop.

### 9.2 External flow — into the DGCA SSP / ALoSP

- The Operator's SPTs are set to be **consistent with the DGCA SSP's acceptable-level-of-safety-performance (ALoSP) expectations** for the operation. Where the SSP defines State-level ALoSP indicators/targets for approach-and-landing safety, the Operator's UA/RE SPIs are **mapped to and reconciled against** them.
- **Aggregated SPI performance** (not individual data) is made available to the DGCA under **SMS acceptance and continued oversight**, per the DGCA CAR SMS/SSP framework. The Accountable Manager owns this submission; the SRB endorses it.
- **[GAP] — exact DGCA CAR Section/number and revision** for the SMS/SSP/ALoSP acceptance requirement: confirm against the current live DGCA CAR before citing a clause. Do not rely on a fixed number here; the CAR numbering evolves.
- **[ASSUMPTION]** — that the DGCA SSP publishes State-level ALoSP indicators the Operator can map to: confirm the current State ALoSP expectation and the reporting channel/cadence the DGCA requires, and align this framework's cadence to it.

---

## 10. Assumptions, gaps and data prerequisites (consolidated)

**[GAP] — required before the framework goes live (must be computed/obtained, never invented):**
1. Historical monthly SPI values → **baseline mean (x̄) and σ** for every SPI (§7.1).
2. **Alert levels** (x̄ + n·σ lines / compliance floors) for every SPI (§7.2).
3. **SPT numeric values** — the improvement-target magnitudes (§7.3).
4. **Exposure denominators** — approaches, landings, sectors and movements (§6.1).
5. The **event count / rolling-count alert** for SPI-RE-04 and other rare SPIs (§7.4).
6. The **exact DGCA CAR Section/number and revision** for the SMS/SSP/ALoSP requirement (§2, §9.2).

**[ASSUMPTION] — confirm against the Operator's documents:**
1. Stabilisation gate heights (**1,000 ft IMC / 500 ft VMC**) — per OM-A / FCOM.
2. The **FDM event library and thresholds** for the approach and landing phases (SPI-UA-03, RE-01, RE-03).
3. The **landing-distance-margin policy threshold** (SPI-RE-02).
4. The proposed **review cadence** (monthly SAG / quarterly SRB) and the DGCA reporting cadence.
5. Existence and content of the **DGCA State-level ALoSP indicators** to map to.

---

## 11. Review, sign-off and disclaimer

### 11.1 Internal SME review note

SME review ran under the Aviation Safety-Assurance / SPI-SPT specialist lens (ICAO Annex 19, Pillar 3): every SPI carries a defined alert-level **method** and a target (SPT), each maps to an owning hazard/objective and a named role owner, the leading/lagging mix is balanced, no performance figure has been invented (all values are marked **[GAP]**), and the FDM data-handling protects reporter/crew identity. This is **decision-support only**; it **precedes and does not replace** the human competent-person sign-off below, and it does not itself certify the framework as approved.

### 11.2 Competent-person sign-off (to be completed)

| Role | Name (role-holder) | Signature | Date |
|---|---|---|---|
| Prepared by — Safety Manager | *[to be signed]* | | *[on ratification]* |
| Reviewed by — Nominated Postholder – Flight Operations | *[to be signed]* | | |
| Ratified by — Safety Review Board (chair: Accountable Manager) | *[to be signed]* | | |

### 11.3 Disclaimer

This document is **decision-support** for the Operator's safety management system. It is **not legal advice** and does **not**, by itself, constitute the acceptance or approval of any regulator. It must be reviewed, completed with the Operator's own data, and approved by a **competent person** (an aviation safety-management SME) and the Accountable Manager before it is relied upon. Regulatory references (notably the DGCA CAR clause) are flagged **[GAP]** and must be verified against the current live DGCA documents.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
