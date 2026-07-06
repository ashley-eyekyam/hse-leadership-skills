<!-- LOCKED fixture — owner-LOCKED at the SW2 19-03 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Hazard Register — Bird Strike on Departure

**SMS Pillar 2 (Safety Risk Management) · ICAO 5×5 Risk Classification Scheme · DGCA-certificated A320 scheduled operator**

---

## Document control

| Field | Value |
|---|---|
| **Register** | Operational Safety Hazard Register — Flight Operations (Aeroplane) |
| **Operator** | «Operator» — DGCA-certificated A320 scheduled passenger operator **[ASSUMPTION: operator name / AOC number not supplied; recorded as a placeholder to be completed on the live record]** |
| **Certificating authority / SSP** | DGCA (India) — operating under the Indian State Safety Programme, which adopts ICAO Annex 19 |
| **SMS framework** | ICAO Annex 19 (2nd ed., 2016), Pillar 2 — Safety Risk Management; scoring per ICAO Doc 9859 (SMM, 4th ed.) risk-classification scheme |
| **Regulatory basis (India)** | DGCA Civil Aviation Requirement mandating an operator SMS — **exact CAR (Section / Series / Part) [GAP]: verify against the current DGCA CAR before issue; do not cite from memory** |
| **This entry** | HR-001 — Bird strike on departure |
| **Register custodian (owner)** | Safety Manager |
| **Accountable for the SMS** | Accountable Manager |
| **Version / status** | v0.1 — DRAFT for competent-person review |
| **Date raised / date of this draft** | 5 July 2026 |
| **Classification** | Internal — Safety (de-identified; safe to circulate within the SMS) |
| **Review cadence** | Live log — reviewed at each Safety Action Group; escalated Intolerable/red entries reviewed at the Safety Review Board (SRB) until residual is achieved |

> **Decision-support notice.** This register is decision-support produced to structure the operator's safety-risk management. It is **not** legal advice and **not** an airworthiness or operational approval. It must be reviewed and signed off by a **competent person (aviation SME — e.g. the Safety Manager and the accountable postholder)** before it is relied upon. Risk bands are computed reproducibly by the shared risk-matrix engine from the operator's own severity/likelihood inputs; the operator remains responsible for those inputs and for the controls adopted.

> **De-identification.** The de-identification scrub was run **before** drafting. The supplied scenario contained **no personal or health identifiers** (no names, crew IDs, rosters, medical detail). All owners in this register are **role labels**, not individuals. If this entry is later evidence-traced to a specific occurrence report, the reporter/crew identities in that report must be scrubbed to role labels before they enter this register (a re-identifying narrative is a de-identification hard-fail, not a flag).

---

## Part A — The register structure this entry sits in

### A.1 What this register is

A living hazard log under Annex 19 **Pillar 2 (Safety Risk Management)**. Every entry runs the same discipline, left to right:

**hazard → credible worst consequence → existing controls (baseline) → initial risk classification (ICAO 5×5) → hierarchy-of-controls mitigation → residual/target risk → owned, dated SMART actions → monitoring/closure.**

Two rules make it defensible:

1. **The band is the engine's, never the assessor's.** Severity and likelihood are the operator's choices on the ICAO 5×5 axes; the *acceptability band* is computed by `risk_matrix.score(...)` against the `AVIATION_5X5` MatrixConfig (`KB-DATA-AVI-RISK-MATRIX`). Two assessors entering the same severity/likelihood get the same band.
2. **Every hazard traces to evidence.** A hazard asserted without a supporting occurrence report, audit finding, or FDM/FOQA trend is carried as a **[GAP]** until evidenced — it is not silently accepted.

### A.2 Column dictionary (the schema every row conforms to)

| Column | Meaning |
|---|---|
| **Hazard ID** | Stable identifier (HR-001…) |
| **Date raised** | When first logged |
| **Hazard (condition)** | The source/condition with potential to cause harm — a state, not an outcome |
| **Consequence (credible worst)** | The credible worst outcome if the hazard is realised |
| **Operation / SMS component** | Where in the operation it arises (e.g. departure — take-off/initial climb) |
| **How surfaced** | Reactive (occurrence) · Proactive (audit/survey) · Predictive (FDM/FOQA, trend) |
| **Evidence ref** | The occurrence report / finding / dataset the hazard traces to |
| **Exposed population** | Who/what is exposed (flight crew, pax, aircraft/asset, third party…) |
| **Existing controls** | The baseline in place today (drives residual, not initial-vs-nothing) |
| **Initial severity / likelihood** | ICAO 5×5 axis choices |
| **Initial risk (score · band)** | Engine output — `severity idx × likelihood idx` → Acceptable / Tolerable-with-mitigation / Intolerable |
| **Additional controls (HoC-ranked)** | New controls, most-effective-first; PPE/admin-only flagged |
| **Residual severity / likelihood** | Post-mitigation axis choices |
| **Residual/target risk (score · band)** | Engine output after mitigation |
| **Risk movement** | `residual_delta` — score change and region change |
| **Actions** | SMART action refs (A-nn) |
| **Action owner (role)** | Role label — validated for owner + date |
| **Target date / review date** | When due / when effectiveness is reviewed |
| **SPI link** | The safety performance indicator that monitors this risk |
| **Status** | Open / In-progress / Residual-achieved / Closed |
| **Entry owner (role)** | Who owns the row (default: Safety Manager) |

### A.3 The scoring engine (fixed, reproducible)

**`AVIATION_5×5` MatrixConfig — `KB-DATA-AVI-RISK-MATRIX` (ICAO Annex 19 RCS):**

- **Severity index** (rows): Negligible = 1 · Minor = 2 · Major = 3 · **Hazardous = 4** · Catastrophic = 5
- **Likelihood index** (cols): Extremely Improbable = 1 · Improbable = 2 · **Remote = 3** · **Occasional = 4** · Frequent = 5
- **Score** = severity index × likelihood index (1–25), mapped to a contiguous band:

| Band | Score | Action |
|---|---|---|
| 🟩 **Acceptable** | 1–4 | Monitor; no further mitigation required |
| 🟨 **Tolerable with mitigation** | 5–12 | Tolerable **only** with mitigation — reduce so far as reasonably practicable before proceeding |
| 🟥 **Intolerable** | 13–25 | Cease / do not proceed until mitigated to acceptable |

> *Source: ICAO Annex 19 (2016) + ICAO Doc 9859 (SMM, 4th ed.). The three-region structure is the ICAO RCS; the numeric cut-offs are the pack's reproducible calibration of that structure over the 5×5 multiply scale, recorded here for competent-person confirmation. The operator's licensed ICAO cell-colouring governs if it differs.*

### A.4 Register-at-a-glance (summary row)

| ID | Hazard | Init. sev × lik | Init. risk | Residual target | Residual risk | Movement | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| **HR-001** | Bird strike on departure | Hazardous × Occasional | **16 · 🟥 Intolerable** | Hazardous × Remote | **12 · 🟨 Tolerable-with-mitigation** | 16 → 12 (▼4; red → amber) | Safety Manager | **OPEN — Intolerable; interim controls pending** |

---

## Part B — Hazard entry HR-001: Bird strike on departure

### B.1 Hazard and mechanism

**Hazard (condition):** Presence of birds (single, flocking, and dawn/dusk/migratory concentrations) in the departure environment — runway, climb-out corridor and low-level airspace — of the aerodromes the A320 fleet operates from.

**Mechanism:** Ingestion into one or (worst-credible) both engines, or impact on windshield/leading edges/radome, during the take-off roll, rotation and initial climb — the highest-energy, lowest-margin phase of flight, where thrust loss is least recoverable and crew workload is highest.

### B.2 Evidence and how surfaced

| Field | Value |
|---|---|
| How surfaced | **[GAP]** — not stated in the tasking. Bird strike is a standing, industry-wide wildlife hazard; a live register entry must be traced to the operator's own evidence. |
| Evidence ref | **[GAP]** — attach: (a) the operator's own bird-strike occurrence reports (rate per 10,000 movements), (b) aerodrome wildlife-strike statistics for each base/destination, (c) DGCA/ICAO national bird-strike data (IBIS), (d) any FDM/FOQA engine-parameter or rejected-take-off events. **Until attached, HR-001 is an evidenced-hazard [GAP] and must not be closed.** |
| Trace discipline | Bird strike is a credible, well-documented hazard class, so it is logged now with an interim risk position; the evidence [GAP] is an open action (see A-08), not a reason to omit the entry. |

### B.3 Exposed population

Flight crew · cabin crew · passengers · aircraft/asset (engines, airframe) · third party/public (in an overrun or forced off-aerodrome landing). **Multiple.**

### B.4 Credible worst consequence and severity

**Credible worst consequence:** Multiple/large-bird ingestion at or after V1 causing significant thrust loss on one — or, worst-credible, both — engines, resulting in a rejected take-off overrun, an engine-failure-after-V1 with degraded climb performance and forced return, or an off-field forced landing; with major engine/airframe damage and potential serious injury.

**Severity — Hazardous (index 4)** *(operator's assessment, recorded as given).* This maps to the ICAO "Hazardous" descriptor topic — a large reduction in safety margins, major equipment damage, and serious injury — short of the "Catastrophic" (hull-loss/multiple-fatality) extreme.

> **[ASSUMPTION / sensitivity]** Severity is fixed at **Hazardous** per the operator. Note the boundary: a *dual*-engine loss of thrust below acceleration altitude with no suitable landing area is rated **Catastrophic** by some assessors. If the operator's route/aerodrome profile makes that outcome credible (e.g. surrounded by water/urban terrain), re-open the severity choice at SRB. This directly affects the target — see B.8.

### B.5 Existing controls (baseline) — and the hierarchy-of-controls evaluation

**Existing control on record:** *a crew briefing card only.*

**HoC classification of the existing control:**

| Existing control | HoC level | What it actually does |
|---|---|---|
| Crew briefing card | **Administrative (information/awareness)** — near the bottom of the hierarchy | Raises crew awareness and prompts a response. It does **not** reduce the number of birds present, does **not** reduce the probability of a strike, and does **not** reduce the credible severity. It acts only on the crew's *reaction after* the hazard is encountered. |

> 🚩 **Lower-order-control flag (mandatory).** The existing treatment of HR-001 is **administrative-only**. For a risk the operator itself classifies as **Intolerable (16)**, a briefing card is **not an adequate treatment** and cannot be accepted as the control set. Higher-order controls are reasonably practicable and are required (see B.6). Under the hierarchy of controls a PPE/administrative-only measure must be justified against, or escalated to, elimination / substitution / engineering — here it is **escalated**. The briefing card is **retained** as one small awareness element, not as the mitigation.

### B.6 Initial risk classification (ICAO 5×5)

```
risk_matrix.score(severity="Hazardous", likelihood="Occasional", matrix=AVIATION_5X5)
  = severity idx 4  ×  likelihood idx 4  =  16
  → band: INTOLERABLE (13–25)
```

| | Value |
|---|---|
| Severity | **Hazardous** (4) |
| Likelihood | **Occasional** (4) *(operator's assessment)* |
| **Initial risk** | **16 · 🟥 INTOLERABLE** |
| Required action | **Cease/do-not-proceed logic does not mean grounding** — the operation continues under existing regulatory airworthiness/wildlife regimes, but the risk is **not tolerable on the current control set**; interim risk reduction is required now and the entry stays open until residual is achieved. |

> **[ASSUMPTION / discipline note]** Likelihood must be assessed against the **Hazardous consequence**, not against *any* bird strike. Minor strikes are Frequent industry-wide; a *Hazardous-outcome* strike is rarer. **Occasional** is therefore a conservative (pessimistic) choice for the Hazardous outcome — recorded as the operator's assessment and to be re-tested once B.2 evidence is attached.

### B.7 Additional controls — hierarchy of controls, most-effective-first

Bird-strike severity is largely **fixed** (aircraft engine bird-ingestion tolerance is type-certificated/OEM). The controls below therefore act principally on **likelihood** (fewer birds, less exposure) and on **consequence-mitigation** (crew response), most-effective-first:

| # | Control | HoC level | Reduces | Notes / interface |
|---|---|---|---|---|
| C1 | Eliminate bird attractants at operator-controlled facilities/bases (standing water, waste/food sources, long grass, roosting sites) | **Elimination** | Likelihood | Directly owned where the operator controls the site. |
| C2 | Drive attractant/habitat elimination at third-party aerodromes through a formal **Wildlife Hazard Management Plan (WHMP) interface** — require and confirm the aerodrome operator's wildlife programme via contract/SLA and joint review | **Elimination (via interface)** | Likelihood | Much of the aerodrome environment is **outside operator control** — this is an interface control, **not** a licence to default to admin. |
| C3 | Substitute exposure — where operationally feasible, adjust departure timing/slots away from peak activity windows (dawn/dusk, migratory season) and select runway/SID with lower wildlife exposure | **Substitution (of exposure)** | Likelihood | A lever the operator *does* control; subject to ATC/slot/performance constraints. |
| C4 | Aircraft engineering assurance — confirm the fleet is to current engine bird-ingestion certification standard and no MEL item degrades engine-out/climb performance on wildlife-exposed departures | **Engineering (verification)** | Severity-limiting / consequence | Largely OEM-fixed; the operator's lever is verification and MEL discipline. |
| C5 | Aerodrome engineering deterrents required via the WHMP interface — bird-detection radar, bio-acoustic/distress-call and pyrotechnic dispersal, netting/spikes, grass-height regime, drainage | **Engineering (via interface)** | Likelihood | Owned by the aerodrome operator; the airline's action is to **require and confirm** presence and effectiveness. |
| C6 | Active bird-activity information loop — obtain and act on bird-activity NOTAMs/ATIS and aerodrome wildlife reports; brief crews on high-activity aerodromes/seasons | **Administrative** | Likelihood/exposure | — |
| C7 | SOPs — crew avoidance/response procedures: hold/delay take-off if birds observed, reject-below-V1 policy, engine-failure-after-V1 and (worst-credible) dual-engine loss-of-thrust handling, landing-light use, speed management where permitted | **Administrative** | Consequence | — |
| C8 | Recurrent simulator training — rejected take-off, engine failure after V1, dual-engine loss of thrust / QRH memory items, threat & error management | **Administrative** | Consequence | — |
| C9 | Mandatory bird-strike reporting into the SMS **and** the national database (DGCA / ICAO IBIS), + FDM/FOQA monitoring of engine parameters and RTOs; trend into SPI and WHMP effectiveness | **Administrative (assurance loop)** | Likelihood (over time) | Closes the loop back to C1–C5. |
| C10 | **Retain** the crew briefing card as one awareness element within C6–C8 | **Administrative** | Consequence (marginal) | Kept, **not** relied upon. |
| — | PPE | **Not applicable** | — | No PPE mitigates bird-strike risk to the aircraft or occupants — recorded explicitly so the hierarchy is walked in full. |

### B.8 Target / residual risk

With C1–C10 implemented and their effectiveness monitored (C9), the **likelihood** of the Hazardous-outcome strike is credibly reduced from **Occasional (4)** to **Remote (3)**. **Severity remains Hazardous (4)** — the controls reduce probability and improve response, but do not change the credible worst outcome.

```
risk_matrix.score(severity="Hazardous", likelihood="Remote", matrix=AVIATION_5X5)
  = 4 × 3 = 12  → band: TOLERABLE WITH MITIGATION (5–12)

risk_matrix.residual_delta(initial=16, residual=12)
  = ▼4 ; region change: INTOLERABLE (🟥) → TOLERABLE-WITH-MITIGATION (🟨)
```

| | Initial | **Target / residual** |
|---|---|---|
| Severity | Hazardous (4) | Hazardous (4) — **unchanged** |
| Likelihood | Occasional (4) | **Remote (3)** |
| Score · band | **16 · 🟥 Intolerable** | **12 · 🟨 Tolerable with mitigation** |
| Movement | — | **▼4; red → amber** |

> **Honest target ceiling — green is not credibly attainable.** Because severity is fixed at **Hazardous (4)**, reaching 🟩 Acceptable (≤4) would require a likelihood of **Extremely Improbable (1)** — which cannot be honestly claimed for a departure bird strike. The defensible target is therefore **amber (Tolerable with mitigation), held ALARP** through the sustained WHMP interface and continuous SPI monitoring, with SRB oversight while the entry remains open.
> - *Stretch:* if a mature WHMP + monitoring demonstrably drives exposure down, likelihood **Improbable (2)** → score **8** (still 🟨 amber) is the realistic best case.
> - **[ASSUMPTION]** The residual is a **modelled** target, **not yet achieved**. It is provisional until C1–C10 are implemented and effectiveness is **verified by the SPI** (B.10). If severity is re-rated Catastrophic (per B.4), residual becomes 5 × 3 = **15 · 🟥 Intolerable**, and the target must be re-worked.

### B.9 SMART action plan

All owners are **role labels**. Each action is specific, has an accountable role, a target date and a review date, and links to the control and SPI it serves.

| Ref | Action (specific, measurable) | Control / HoC | Owner (role) | Target date | Review date | SPI link |
|---|---|---|---|---|---|---|
| **A-01** | Issue an interim Flight Operations bulletin: reinforce bird-activity briefing, hold/delay-for-birds and reject-below-V1 discipline pending the fuller control set; **retain** the briefing card as one element | C6, C7, C10 (Admin) | Head of Flight Operations (Postholder Flight Operations) | 19 July 2026 | 31 August 2026 | SPI-01 |
| **A-02** | Establish/confirm a formal **WHMP interface** with each base/destination aerodrome operator; obtain current wildlife-strike statistics and deterrent/programme status per aerodrome | C2, C5 (Elimination/Engineering via interface) | Head of Ground Operations / Station Management | 30 September 2026 | 31 October 2026 | SPI-02 |
| **A-03** | Audit and remediate bird attractants at operator-controlled facilities/bases (water, waste, grass, roosts); log remediations | C1 (Elimination) | Head of Ground Operations / Station Management | 31 October 2026 | 30 November 2026 | SPI-02 |
| **A-04** | Review departure timing/slots and runway/SID selection at the highest-exposure aerodromes; document feasible exposure-substitution measures | C3 (Substitution) | Head of Flight Operations (Postholder Flight Operations) | 31 October 2026 | 30 November 2026 | SPI-01 |
| **A-05** | Confirm fleet engine bird-ingestion certification standard and MEL discipline for wildlife-exposed departures; record any performance-degrading MEL constraints | C4 (Engineering assurance) | Head of Engineering & Maintenance (CAMO Postholder) | 30 September 2026 | 31 October 2026 | — |
| **A-06** | Update SOPs/QRH usage and briefing content: engine failure after V1, dual-engine loss of thrust, RTO, landing-light/speed management | C7 (Admin) | Fleet Chief Pilot (A320) | 30 November 2026 | 31 December 2026 | SPI-01 |
| **A-07** | Add/confirm recurrent simulator scenarios: bird-strike-driven engine failure after V1, dual-engine loss of thrust, RTO; track completion | C8 (Admin) | Head of Training | 31 December 2026 | 31 March 2027 | SPI-03 |
| **A-08** | **Close the evidence [GAP]:** compile the operator's bird-strike rate (per 10,000 movements), aerodrome and DGCA/ICAO-IBIS data, and any FDM/FOQA events; attach to HR-001 and re-test the Occasional likelihood | C9 (Assurance) — evidence trace | Safety Manager | 31 August 2026 | 30 September 2026 | SPI-01/02 |
| **A-09** | Stand up mandatory bird-strike reporting into the SMS + national database and FDM/FOQA trending; define and baseline SPI-01/02/03 with alert/target levels | C9 (Assurance) | Safety Manager (with FDM/FOQA Manager) | 30 September 2026 | 31 October 2026 | SPI-01/02/03 |
| **A-10** | Table HR-001 (Intolerable) at the Safety Review Board; confirm interim tolerability, endorse the target, and set the re-score date once controls are in place | Governance | Accountable Manager (chair) / Safety Manager | 31 August 2026 | Each SRB until residual achieved | all |

*Actions validated for owner + target date + review date (`smart_actions.validate_register`): **all rows complete** — no ownerless or undated action.*

### B.10 Monitoring, SPI linkage and closure trigger

- **SPI-01 — Bird-strike rate (flight ops):** strikes per 10,000 departures, trended; alert/target levels **[GAP]** — set from the A-08 baseline.
- **SPI-02 — Aerodrome wildlife-management effectiveness:** WHMP interface status and strike rate by aerodrome.
- **SPI-03 — Training assurance:** % flight crew current on the bird-strike/engine-failure-after-V1 recurrent scenarios.
- **Closure trigger:** HR-001 moves to *Residual-achieved* only when C1–C10 are implemented **and** SPI-01/02 demonstrate the likelihood is at/below **Remote** across a defined monitoring window; it is **not** closed on action completion alone. It remains an SRB-tracked entry while Intolerable.

### B.11 Assumptions & gaps carried by this entry

| Flag | Item |
|---|---|
| **[ASSUMPTION]** | Operator name/AOC not supplied — placeholder used. |
| **[ASSUMPTION]** | Severity **Hazardous** and likelihood **Occasional** are the operator's stated assessments, recorded as given; likelihood is for the *Hazardous* outcome and is conservative. |
| **[ASSUMPTION]** | Residual (Remote/12/amber) is a **modelled target, not yet achieved**; provisional until SPI-verified. |
| **[GAP]** | Supporting evidence for the hazard (occurrence reports, strike statistics, FDM/FOQA) — closed by A-08. |
| **[GAP]** | Exact DGCA CAR reference for the SMS obligation — verify before issue; do not fabricate. |
| **[GAP]** | Named bases/destinations and their WHMP/deterrent status — needed to make C2/C5 aerodrome-specific. |
| **[GAP]** | SPI alert/target levels — set from the A-08 baseline. |
| **[GAP]** | Fleet engine bird-ingestion certification standard / MEL status — closed by A-05. |

---

## Part C — Register governance, review and SME sign-off

**Ownership & cadence.** The Safety Manager owns and maintains the register; the Accountable Manager owns the SMS. Live entries are reviewed at the Safety Action Group; **Intolerable/red** entries (incl. HR-001) are escalated to and tracked by the **Safety Review Board** until residual is achieved.

**Links to the wider SMS.** This register is Pillar 2 of the operator's SMS. It connects to: the SMS manual and safety policy (SMS builder), the SPI/SPT framework (SPI-01/02/03 above), the Safety Review Board record, the management-of-change process (for any change to fleet, network or aerodrome mix affecting HR-001), and the confidential reporting scheme (a source of future bird-hazard evidence).

**SME review (decision-support — precedes, does not replace, human sign-off).**

> SME review **ran** — persona: *Aviation SMS Safety Risk Manager / hazard-register custodian* (Annex 19 Pillar 2). Checks applied and passed: (a) the entry runs hazard → consequence → existing controls → 5×5 classification → HoC mitigation → residual, with no stage skipped; (b) the 16 and 12 bands are the engine's arithmetic on the ICAO MatrixConfig, consistent with the severity×likelihood pairs; (c) residual is re-scored and the movement reported; (d) the evidence gap is flagged **[GAP]**, not silently accepted; (e) mitigations are HoC-ranked and the administrative-only existing control is flagged and escalated; (f) no personal-identifier leak (owners are role labels). This is **decision-support only**; it **precedes and does not replace** the human competent-person (aviation-SME) sign-off and does **not** assert "approved by a competent person."

| Review step | Role | Status | Date |
|---|---|---|---|
| Register custodian review | Safety Manager | Pending | — |
| Postholder review | Head of Flight Operations (Postholder Flight Operations) | Pending | — |
| Competent-person / accountable sign-off | Accountable Manager | **Pending — required before reliance** | — |

*Draft prepared 5 July 2026.*

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
