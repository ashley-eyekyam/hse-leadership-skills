<!-- LOCKED fixture — owner-LOCKED at the SW2 19-03 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Change Safety Assessment (Management of Change)
### ICAO Annex 19, Pillar 2 — Safety Risk Management · Addition of a Hot-and-High Destination to the Scheduled A320 Network

---

## 0. Document control

| Field | Entry |
|---|---|
| Document title | Change Safety Assessment — Addition of a hot-and-high, terrain-constrained destination to the A320 scheduled network |
| Assessment type | Management of Change (MoC) — ICAO Annex 19 Pillar 2 / DGCA State Safety Programme (SSP) accepted SMS procedure |
| Operator | **[GAP — operator legal name & DGCA AOC number not supplied]** ("the Operator") |
| Change reference | MoC-A320-HOTHIGH-001 |
| Assessment date | 5 July 2026 |
| Status | **DRAFT — decision recorded below is a safety-function recommendation; pending competent-person (aviation-SME) sign-off and Accountable Manager ratification** |
| Certificating authority | India — DGCA (State Safety Programme) |
| Classification | Restricted — Safety |
| Prepared by (role) | Safety Manager (SMS Pillar 2 assessment), supported by Flight Operations Postholder |
| Distribution (roles) | Accountable Manager · Safety Manager · Flight Operations Postholder · Chief Pilot / Fleet Manager (A320) · Head of Training · Safety Review Board |

---

## 1. Disclaimer

This document is **decision-support only**. It is **not** legal or airworthiness advice and does **not** constitute a competent-person approval. Every finding, score and recommendation herein must be reviewed, validated and signed off by a **competent person** (a qualified aviation SME / postholder) before the change is authorised. Risk inputs (severity/likelihood) are provisional expert judgement and must be re-scored on the engineering evidence commissioned in the action register. Nothing here authorises revenue operations.

---

## 2. Data protection & de-identification statement

De-identification was applied **before** drafting. The inputs contained **no personal or health identifiers** — no individual names, employee/Aadhaar/SSN numbers, contacts, exact personal dates, photos or medical detail. The one actor referenced in the brief ("the change sponsor") is a **role**, retained as a role label. All owners in this document are **role-based** (e.g. "Flight Operations Postholder"); no individual is named. No re-identification key is required for this assessment. If, during execution, any crew-specific data (currency records, individual training results) is attached, pseudonymise to role labels and hold the key access-controlled, apart from this document.

---

## 3. Executive summary

The Operator proposes to add a new **hot-and-high** destination — aerodrome elevation ~6,500 ft AMSL with high ambient temperatures, served by a **terrain-constrained approach** — to its DGCA-certificated A320 scheduled network. The change sponsor has proposed **a single mitigation: a crew briefing card.**

**Headline decision: DECLINE the change as proposed.** A crew briefing card is a **single administrative (lower-order) control** and is not an adequate treatment for a change that introduces **ten new or changed hazards, seven of which are initially Intolerable (red) on the ICAO 5×5**, several with a **credible catastrophic outcome** (controlled flight into terrain, runway overrun, one-engine-inoperative terrain contact). A briefing card informs crew of hazards it cannot physically remove or bound; it does nothing to alter aircraft performance, obstacle clearance, approach path geometry, dispatch weight limits or diversion capability. Accepting it as the sole mitigation is precisely the failure mode this assessment exists to prevent.

**The change may proceed only under a conditional-approval package** (Section 12) that applies **higher-order controls** — elimination/substitution/engineering — ahead of, and in addition to, administration: a validated aerodrome-specific performance analysis with an engineered engine-out escape procedure (EOSID); an RNP AR approach with vertical guidance and a validated missed-approach gradient; hard, system-enforced dispatch weight/payload limits; a driftdown/depressurisation escape study; time-of-day/temperature and day-VMC operating limitations; special crew qualification with simulator LOFT on the actual terrain; a non-revenue validation (route-proving) flight; and a **phased entry with a mandatory review-after-trial**. Under that package, residual risk moves down to **Tolerable-with-mitigation (amber), held to ALARP** — it does **not** reach the green "Acceptable" band, because the credible worst outcome for the dominant hazards remains catastrophic. The change therefore remains a **monitored, gated** operation, never a "briefed-and-forgotten" one.

Regulatory note: adding a **Category C aerodrome**, an **RNP AR (PBN) approach**, and hot-and-high performance operations to the fleet very likely requires **specific DGCA operational approvals** in addition to SMS acceptance — see Section 4 and the [GAP] on exact CAR/approval references.

---

## 4. Confirmed intake (echo-back) & assessment basis

**Confirmed facts** (per the structured intake; open items flagged):

- **Operator:** [GAP — legal name/AOC not supplied]; DGCA-certificated scheduled operator, A320.
- **Change type:** New route / destination (Q2 → prompts the technical/performance/terrain hazard set).
- **Specific change:** Add a scheduled destination at aerodrome elevation ~6,500 ft AMSL, high ambient temperature, terrain-constrained approach, operated by in-fleet A320. **[GAP]** aerodrome ICAO/IATA identity, exact elevation, runway length/slope/surface, published procedures, RFF category, and diversion field data not supplied.
- **Effective date / mode:** **[GAP]** — not supplied. **[ASSUMPTION]** this assessment mandates a **phased/trial entry with a review-after-trial trigger** (Q4 trial branch) rather than immediate permanent adoption; the sponsor's target date is unconfirmed.
- **Jurisdiction:** India / DGCA (Q5) → India follow-up (Q5a) engaged; alignment via `KB-REG-IN-DGCA`.
- **New/changed hazards identified by the sponsor:** three (unstabilised approach; reduced OEI climb; reduced runway margin at high density altitude). **This assessment identifies seven further new/changed hazards the proposal omitted** (Section 6). Zero-new-hazard failure mode: **not triggered** — hazards are enumerated.
- **Named approval authority:** **[GAP]** — the brief names only "the change sponsor" (a role in the change-proposal, not the safety-decision authority). Per SMS governance, the approve/decline authority is the **Accountable Manager, on the recommendation of the Safety Manager and Flight Operations Postholder**; recorded as such below.

**Assessment basis:**
- Framework: ICAO Annex 19 four-pillar SMS, Pillar 2 (Safety Risk Management → Management of Change) — `KB-STD-ICAO-ANNEX19`.
- Risk scoring: ICAO 5×5 Risk Classification Scheme via the shared `risk_matrix.score()` engine with the `AVIATION_5X5` MatrixConfig — `KB-DATA-AVI-RISK-MATRIX` (severity Negligible=1 … Catastrophic=5 × likelihood Extremely Improbable=1 … Frequent=5; multiply; bands **1–4 Acceptable / 5–12 Tolerable-with-mitigation / 13–25 Intolerable**). No forked matrix.
- Control ranking: hierarchy of controls — `KB-SNIP-HOC`.
- India layer: DGCA operates the **State Safety Programme** and **accepts** the operator SMS; **management of change** is an accepted SMS procedure under DGCA CAR Section 1 (SMS/SSP series). **[GAP]** exact CAR Section/number & revision — verify against the live DGCA CAR; **never** use a fabricated CAR number.
- **Regulatory triggers to verify (do not assume covered by SMS acceptance):** specific DGCA **operational approval** is likely required for (a) **RNP AR APCH / PBN**, (b) operation into a **Category C aerodrome**, and (c) any **special aerodrome/route** designation. Exact approval references **[GAP]** — confirm with the live DGCA CAR/AIC and obtain the approvals before entry-into-service.

---

## 5. Description of the change

The Operator's A320 scheduled network is extended to a new aerodrome characterised by the combination that makes the change hazardous — **elevation + heat + terrain, acting together**:

- **High elevation (~6,500 ft AMSL)** and **high ambient temperature** produce a high **density altitude (DA)**. Air density falls, so engine thrust, wing lift and climb gradient all degrade, while **true airspeed and groundspeed for a given indicated airspeed rise** — lengthening take-off, acceleration, flare and landing rolls and flattening every climb path.
- **Terrain-constrained approach** — surrounding high ground compresses the usable approach, missed-approach and departure corridors, and raises minimum safe/en-route altitudes and the consequences of any path deviation.
- **A320, scheduled service** — a performance-limited operation at the margins of the type's hot-and-high envelope, flown by crews on **first exposure** to the aerodrome.

The hazard is not any one factor but their **interaction** (Section 9), and it is worst in specific combined states (night, tailwind, high temperature, one engine inoperative, go-around).

---

## 6. Hazard identification — new & changed hazards

The sponsor listed H1–H3. The assessment adds H4–H10 (marked ★ where the proposal omitted them). A change of this class is dominated by **latent and combined-state** hazards, not steady-state ones.

| ID | New / changed hazard | Credible worst outcome | Newly exposed |
|---|---|---|---|
| **H1** | Unstabilised approach into the terrain-constrained approach (steep/curved path, black-hole / sloping-terrain visual illusions, energy high) | CFIT / approach-and-landing accident / runway excursion | Flight crew, passengers, public |
| **H2** | Reduced one-engine-inoperative (OEI) climb performance — net take-off flight path & OEI missed approach fail to clear terrain at high DA | CFIT on departure / OEI go-around | Flight crew, passengers, public |
| **H3** | Reduced runway margins at high DA — take-off (accelerate-stop) and landing distances erode | Runway overrun / excursion | Flight crew, passengers |
| **H4** ★ | Elevated true airspeed / groundspeed at high DA on approach & landing — higher energy, longer float, compressed decision time | Excursion / hard landing / high-energy CFIT | Flight crew, passengers |
| **H5** ★ | En-route driftdown & depressurisation escape over high terrain — single-engine driftdown ceiling and depressurisation descent may not clear terrain; O₂/fuel escape route unproven | Terrain contact / hypoxia during escape | Flight crew, passengers |
| **H6** ★ | Missed-approach / balked-landing (all-engine and OEI) climb-gradient shortfall in the terrain-constrained go-around | CFIT during go-around | Flight crew, passengers, public |
| **H7** ★ | Crew first-exposure, competency & visual illusions — unfamiliar terrain, high-elevation/black-hole night approach, no aerodrome categorisation | Loss of control / CFIT / excursion | Flight crew, passengers |
| **H8** ★ | Diversion / alternate & fuel planning — scarce performance-validated alternates in a hot-and-high, terrain region; high MSA; contingency erosion | Fuel exhaustion / pressured continuation to an unsafe landing | Flight crew, passengers |
| **H9** ★ | Commercial payload pressure / normalisation of deviance — a performance-limited destination forces payload restrictions; recurring pressure to erode margins | Systematic erosion of take-off/landing margins → excursion / obstacle contact | Passengers, asset, organisation |
| **H10** ★ | Cut-over / transition hazard — first-of-station operation with unvalidated performance data, EFB performance module / RNP procedure / terrain database not loaded or validated, NOTAM/chart currency | Dispatch on wrong performance limits → any of H1–H8 | Flight crew, passengers |

> **Interaction / latent-transition flag (experienced-assessor check):** the change can be *tolerable in steady state yet hazardous during cut-over and in combined states*. The dominant residual risk lives at the intersections — e.g. **OEI + go-around + high DA + night** (H2×H6×H7), and **wrong performance data at entry-into-service** (H10 feeding all others). These are treated explicitly in Sections 9 and 12, not left to crew airmanship.

---

## 7. Initial risk assessment (ICAO 5×5, before mitigation)

Scores via `risk_matrix.score(severity, likelihood, matrix=AVIATION_5X5)`. Severity/likelihood are provisional expert-judgement inputs **pending the engineering studies** (Actions A1, A2, A7) and must be re-scored on real performance data.

| ID | Severity | Likelihood | Score | Band |
|---|---|---|---|---|
| H1 | Catastrophic (5) | Occasional (4) | **20** | **Intolerable (red)** |
| H2 | Catastrophic (5) | Remote (3) | **15** | **Intolerable (red)** |
| H3 | Hazardous (4) | Occasional (4) | **16** | **Intolerable (red)** |
| H4 | Major (3) | Occasional (4) | **12** | Tolerable with mitigation (amber) |
| H5 | Catastrophic (5) | Remote (3) | **15** | **Intolerable (red)** |
| H6 | Catastrophic (5) | Remote (3) | **15** | **Intolerable (red)** |
| H7 | Hazardous (4) | Occasional (4) | **16** | **Intolerable (red)** |
| H8 | Hazardous (4) | Occasional (4) | **16** | **Intolerable (red)** |
| H9 | Hazardous (4) | Occasional (4) | **16** | **Intolerable (red)** |
| H10 | Catastrophic (5) | Remote (3) | **15** | **Intolerable (red)** |

**Seven of ten hazards are Intolerable.** Under ICAO RCS discipline an Intolerable risk means **cease / do not proceed until mitigated to acceptable.** This alone is dispositive of the sponsor's proposal.

---

## 8. Evaluation of the sponsor's proposed mitigation (the briefing card)

**Proposed mitigation:** a crew briefing card, as the *only* control.
**Hierarchy-of-controls classification:** **Administrative (Level 4)** — a lower-order control.

> **Lower-order control — justify why higher-order controls (elimination / substitution / engineering) are not reasonably practicable, or escalate.** They are practicable here (Section 9), so the recommendation is **escalated**.

Why a briefing card **cannot** be the treatment:

- It **changes what crews know, not what the aircraft can do.** It cannot add climb gradient (H2, H6), shorten a runway requirement (H3), lower true airspeed (H4), create a driftdown escape route (H5), or manufacture a diversion field (H8).
- It **relies on the last line of defence** (human performance under high workload, first exposure, at night, possibly OEI) to compensate for physics — the opposite of defence-in-depth.
- It **does nothing about cut-over data integrity** (H10) or **organisational payload pressure** (H9); a card cannot enforce a weight limit.
- Retaining it as the sole control would leave residual risk **equal to initial risk** — seven Intolerable hazards unchanged.

A briefing card **is** a legitimate *component* of the administrative layer — issued **after**, and **on top of**, the higher-order controls (Action A12). It is never the assessment's answer to a hazardous change.

---

## 9. Risk treatment — controls ranked by hierarchy (per hazard)

Controls are ranked most-effective-first and tied to the named hazard. The change is made tolerable by **engineering and substitution controls first**, with administration and the briefing card layered on last.

**Elimination (remove the hazard / bound the operation out of the dangerous state)** — addresses H1, H3, H4, H6, H7
- Prohibit the highest-risk states outright at entry-into-service: **no night operations, no circling approaches, no operations above a defined temperature/DA cap, no operations outside defined wind/contamination limits.** Removing the black-hole night approach and the DA extremes eliminates the worst credible combined states rather than merely warning about them.
- If the higher-order controls below cannot be delivered and validated, the ultimate elimination control is to **not add the destination** (decline).

**Substitution (replace with a less hazardous alternative)** — addresses H1, H2, H3, H4, H6
- **Approach type:** substitute a **precision-like RNP AR APCH with vertical guidance** (stabilised, coded, repeatable path with a defined engineered missed approach) for any non-precision/circling procedure — directly attacks H1 and H6. *(Requires DGCA PBN/RNP AR operational approval — regulatory trigger, Section 4.)*
- **Time of day / temperature window:** schedule arrivals/departures into the **cool part of the day** to lower density altitude — a direct substitution of operating conditions that recovers climb gradient and runway margin (H2, H3, H4).
- **Aircraft capability:** where the fleet mix allows, allocate the **highest hot-and-high-capable A320 variant** (thrust rating / sharklets / weight variant) to the sector. **[GAP]** variant/engine data not supplied.

**Engineering controls (technical barriers, physically enforced)** — addresses H2, H3, H5, H6, H9, H10
- **Aerodrome-specific take-off & landing performance analysis** (all-engine and OEI), founded on an **obstacle survey**, producing a validated **EOSID / engine-out escape procedure** and weight limits (A1). This is the primary defence for H2/H6.
- **Driftdown & depressurisation escape study** with terrain clearance, O₂ and fuel (A7) — the defence for H5.
- **Hard, system-enforced dispatch limits:** temperature/QNH/DA-indexed **maximum take-off and landing weights coded into the EFB performance module and locked in the load-control system** (A5) — converts H3/H9 from a judgement call into a computed limit that cannot be overridden at the load sheet.
- **Validated aeronautical data & terrain database:** RNP procedure coded and flight-validated; **EGPWS/TAWS terrain database confirmed current** for the area; charts/NOTAM currency gate (A10) — the defence for H10.

**Administrative controls (procedures, competency, limits)** — addresses H1, H4, H7, H8, H9, H10
- **Aerodrome categorisation (Category C) and special crew qualification**; **simulator LOFT on the actual terrain/approach** including OEI go-around and rejected take-off (A3, A4) — H7.
- **Stabilised-approach gate policy with mandatory go-around at the gate**, reinforced by a **no-fault go-around / just-culture** stance (A9) — H1.
- **Entry-into-service operating limitations:** day-VMC only, **experienced-crew pairing** (route-qualified Captain; both pilots not simultaneously first-exposure), tailwind cap, temperature/DA cap, no circling (A6) — H1, H4, H7.
- **Fuel & alternate policy:** designate **performance-validated alternates**, contingency/tanker policy, high-MSA fuel (A8) — H8.
- **Non-revenue route-proving / validation flight** before scheduled service, debrief fed back into this assessment (A11) — H10 and validation of H1/H2.
- **Crew briefing card** — retained as **one** administrative element (destination brief, terrain, threats, gates, limitations), issued **only after A1–A11 are complete**, explicitly **not** a standalone control (A12).

**PPE (last line)** — not a primary treatment for an operational change; standard crew oxygen for the depressurisation-escape case (H5) is assured within A7. No hazard here is adequately treated by PPE, and none is offered as such.

---

## 10. Residual risk (re-scored after the Section 9 controls)

Movement reported via `risk_matrix.residual_delta()`. Residual scores assume the **full** control package is delivered and validated (they do **not** apply to the briefing-card-only proposal, whose residual = initial).

| ID | Initial | Residual (Sev × Like) | Residual score | Residual band | Movement |
|---|---|---|---|---|---|
| H1 | 20 Intolerable | Catastrophic (5) × Improbable (2) | **10** | Tolerable w/ mitigation | ↓ 2 regions, Δ −10 |
| H2 | 15 Intolerable | Catastrophic (5) × Improbable (2) | **10** | Tolerable w/ mitigation | ↓ 1 region, Δ −5 |
| H3 | 16 Intolerable | Hazardous (4) × Improbable (2) | **8** | Tolerable w/ mitigation | ↓ 1 region, Δ −8 |
| H4 | 12 Tolerable | Major (3) × Improbable (2) | **6** | Tolerable w/ mitigation | same region, Δ −6 |
| H5 | 15 Intolerable | Catastrophic (5) × Extremely Improbable (1) | **5** | Tolerable w/ mitigation | ↓ 1 region, Δ −10 |
| H6 | 15 Intolerable | Catastrophic (5) × Improbable (2) | **10** | Tolerable w/ mitigation | ↓ 1 region, Δ −5 |
| H7 | 16 Intolerable | Hazardous (4) × Improbable (2) | **8** | Tolerable w/ mitigation | ↓ 1 region, Δ −8 |
| H8 | 16 Intolerable | Hazardous (4) × Improbable (2) | **8** | Tolerable w/ mitigation | ↓ 1 region, Δ −8 |
| H9 | 16 Intolerable | Hazardous (4) × Improbable (2) | **8** | Tolerable w/ mitigation | ↓ 1 region, Δ −8 |
| H10 | 15 Intolerable | Catastrophic (5) × Extremely Improbable (1) | **5** | Tolerable w/ mitigation | ↓ 1 region, Δ −10 |

**Honest limitation — residual does not reach green.** For the dominant hazards the **credible worst outcome remains Catastrophic/Hazardous**; the controls reduce *likelihood*, not the *severity* of terrain contact or overrun. Under the ICAO multiply matrix these hazards therefore settle in the **Tolerable-with-mitigation (amber)** region at best and are **accepted only on an ALARP basis with layered defences and active monitoring** — never "closed". This is why the change must remain **gated and reviewed**, not merely briefed.

---

## 11. Interaction effects & cut-over (transition) hazards

- **Combined-state worst case:** OEI go-around, at high DA, at night, near terrain (H2 × H6 × H7). The engineered EOSID/missed-approach (A1, A2), the **day-VMC-only** entry limitation (A6) and simulator LOFT (A4) exist specifically to break this chain. The night prohibition is an **elimination** control precisely because administration alone cannot manage this state.
- **Data-integrity cut-over (H10):** the single most likely path to an accident on a new station is dispatching the first flights on **unvalidated performance/nav data**. The validation flight (A11), the data-validation gate (A10) and locked EFB limits (A5) are hard pre-conditions, not best-effort.
- **Organisational drift (H9):** the load-control lockout (A5) plus SPI monitoring (A13) convert "commercial pressure" from a cultural risk into a system-enforced boundary with a visible metric.

---

## 12. Decision & recorded rationale

**Decision on the change as proposed (briefing card as the only mitigation): DECLINE.**

**Rationale (recorded):** The change introduces ten new/changed hazards, seven Intolerable on the ICAO 5×5, several with a credible catastrophic outcome. The sole proposed control is a single administrative measure that reduces neither the severity nor, materially, the likelihood of those outcomes; residual risk under it equals initial risk and remains Intolerable. Under ICAO Annex 19 Pillar 2 and the DGCA-accepted SMS MoC procedure, an Intolerable risk must not proceed until mitigated to acceptable. Approving on a briefing card alone would be indefensible to the regulator and to a subsequent investigation.

**Decision on a properly controlled change: CONDITIONAL APPROVAL — the change may proceed to a phased trial only when ALL of the following pre-conditions are met and evidenced, and only then ratified by the Accountable Manager:**

1. Validated aerodrome-specific take-off/landing performance analysis with obstacle survey and engineered **EOSID** (A1) — **completed and accepted**.
2. **RNP AR APCH** (or equivalent vertically-guided procedure) coded, flight-validated, with a validated missed-approach gradient (A2), **and the required DGCA PBN/RNP AR operational approval held** (Section 4).
3. Driftdown/depressurisation escape study (A7) — **completed**.
4. Hard, system-enforced dispatch weight/payload limits in EFB + load control (A5) — **live**.
5. Aerodrome categorised **Category C**; crews specially qualified via simulator LOFT on the actual terrain (A3, A4) — **completed**; **DGCA Cat C aerodrome approval held**.
6. Entry-into-service operating limitations in force: **day-VMC only, experienced-crew pairing, temperature/DA cap, tailwind & contamination limits, no circling** (A6).
7. Fuel & alternate policy with performance-validated alternates (A8) — **published**.
8. Aeronautical data / terrain database / NOTAM validation gate (A10) — **passed**.
9. Non-revenue **route-proving flight** flown and debriefed into this assessment (A11) — **satisfactory**.
10. Crew briefing card issued as a supporting element only (A12).
11. SPIs/SPTs defined and monitoring live (A13).
12. **Mandatory review-after-trial** scheduled at the Safety Review Board (A14).

**If any pre-condition cannot be met, the change does not proceed** (elimination/decline). This is a **provisional safety-function recommendation**; it requires **competent-person (aviation-SME) sign-off** and **Accountable Manager ratification** (Section 15) before it has effect. This assessment does not, and cannot, state that the change is "approved by a competent person".

---

## 13. SMART action register (conditional-approval package)

All owners are **role-based**. Target dates assume a phased trial; the entry-into-service date is **[GAP]** and the review trigger (A14) is expressed relative to it. Owner/date completeness validated (`smart_actions.validate_register()`).

| # | Action | Owner (role) | Target date | HoC level | Hazards |
|---|---|---|---|---|---|
| A1 | Commission & accept aerodrome-specific take-off/landing performance analysis (all-engine + OEI) with obstacle survey and engineered EOSID | Performance Engineering (Flight Ops Engineering) | 1 August 2026 | Engineering | H2, H3, H6 |
| A2 | Design, code & flight-validate RNP AR APCH with vertical guidance and validated missed-approach gradient; secure DGCA PBN approval | Navigation / Aeronautical Data Manager w/ Flight Operations Postholder | 15 August 2026 | Substitution/Engineering | H1, H6 |
| A3 | Categorise aerodrome (Cat C); define special crew-qualification standard; secure DGCA Cat C approval | Head of Training | 15 August 2026 | Administrative | H7 |
| A4 | Simulator LOFT on actual terrain/approach — day & (for later phases) night, OEI go-around, rejected take-off | Head of Training | 29 August 2026 | Administrative | H1, H2, H6, H7 |
| A5 | Code temperature/QNH/DA-indexed max weights into EFB performance module and lock in load-control system | Performance Engineering w/ Ground Operations / Load-Control Manager | 22 August 2026 | Engineering | H3, H9 |
| A6 | Publish entry-into-service operating limitations: day-VMC only, experienced-crew pairing, temp/DA cap, tailwind & contamination limits, no circling | Flight Operations Postholder | 22 August 2026 | Elimination/Administrative | H1, H3, H4, H7 |
| A7 | Driftdown / OEI en-route terrain-clearance + depressurisation escape-route study (O₂, fuel) | Performance Engineering | 15 August 2026 | Engineering | H5 |
| A8 | Fuel & alternate policy — designate performance-validated alternates, contingency/tanker/high-MSA fuel | Flight Operations Postholder w/ OCC / Dispatch Manager | 22 August 2026 | Administrative | H8 |
| A9 | Stabilised-approach gate policy with mandatory go-around; reinforce no-fault go-around via just culture | Chief Pilot / Fleet Manager (A320) | 22 August 2026 | Administrative | H1 |
| A10 | Aeronautical data/chart/NOTAM currency & validation gate; confirm EGPWS/TAWS terrain database current for the area | Navigation / Aeronautical Data Manager | 22 August 2026 | Engineering/Administrative | H10 |
| A11 | Non-revenue route-proving / validation flight before scheduled service; debrief into this assessment | Flight Operations Postholder | 29 August 2026 | Administrative | H1, H2, H10 |
| A12 | Issue crew briefing card as a supporting element (terrain, threats, gates, limitations) — only after A1–A11 complete; not a standalone control | Chief Pilot / Fleet Manager (A320) | 29 August 2026 | Administrative | All |
| A13 | Define & activate SPIs/SPTs: unstable-approach rate, go-around rate, EGPWS alerts, excursion precursors, OEI events, payload-limit override attempts | Safety Manager | 29 August 2026 | Assurance (Pillar 3) | H1–H10 |
| A14 | **Review-after-trial** at the Safety Review Board — confirm / extend / withdraw the change | Safety Manager / SRB Chair | Entry-into-service **+ 90 days** or first 300 sector-cycles, whichever first **[date GAP — pending EIS]** | Governance | All |
| A15 | Ratify the conditional-approval package and confirm resources before entry-into-service | Accountable Manager | 5 September 2026 | Governance | All |

---

## 14. Safety assurance & monitoring (Pillar 3 feedback loop)

The change is not "closed" at approval. The SPIs/SPTs in A13 feed the operator's Safety Assurance so residual amber hazards are watched, not assumed. Recommended alert triggers for early SRB escalation: any EGPWS/TAWS warning on the sector, any unstable-approach continued past the gate, any go-around for terrain/energy, any dispatch at a temperature/DA above plan, or any load-limit override attempt. Any exceedance re-opens the relevant hazard for re-scoring. This links Pillar 2 (this assessment) to Pillar 3 (assurance) and to the SRB (A14).

---

## 15. Approval & sign-off

| Role | Function in this decision | Status |
|---|---|---|
| Safety Manager | Prepared the Pillar 2 assessment; recommends **DECLINE-as-proposed / CONDITIONAL-APPROVAL** package | Recommended — 5 July 2026 |
| Flight Operations Postholder | Owns operational feasibility & limitations | Pending |
| Chief Pilot / Fleet Manager (A320) | Owns crew procedures & training standard | Pending |
| **Competent person (aviation-SME)** | **Independent competent-person sign-off — required before the recommendation has effect** | **Pending — not given by this document** |
| Accountable Manager | Ratifies the conditional-approval package and commits resources (A15) | Pending |

*This assessment is decision-support that **precedes and never replaces** the human competent-person sign-off. It does not and will not state that the change has been "approved by a competent person".*

---

## 16. Open items — [GAP] / [ASSUMPTION] log

- **[GAP]** Operator legal name and DGCA AOC number.
- **[GAP]** Aerodrome identity (ICAO/IATA), exact elevation, runway length/slope/surface, published approach/departure procedures, RFF category, diversion-field data — performance conclusions are qualitative pending A1/A2/A7.
- **[GAP]** Effective date / entry-into-service and trial vs permanent status. **[ASSUMPTION]** phased trial with review-after-trial (A14).
- **[GAP]** Exact DGCA CAR Section/number & revision for the SMS/MoC procedure; and the specific DGCA operational-approval references for **PBN/RNP AR**, **Category C aerodrome**, and any **special aerodrome/route** designation — verify against the live DGCA CAR/AIC; do not fabricate.
- **[GAP]** A320 variant / engine thrust rating / sharklets / MEL status — material to hot-and-high performance.
- **[ASSUMPTION]** "hot-and-high" implies density altitudes materially above 6,500 ft; specific temperatures not quantified — A1/A5 must use the real temperature/QNH envelope.
- **[GAP]** Named safety-decision authority — inferred as Accountable Manager on Safety Manager recommendation, per SMS governance.
- **[ASSUMPTION]** All severity/likelihood inputs are provisional expert judgement; re-score on the evidence from A1, A2 and A7 before ratification.

---

## 17. References

- `KB-STD-ICAO-ANNEX19` — ICAO Annex 19 four-pillar SMS; Pillar 2 Safety Risk Management / Management of Change (source: ICAO Annex 19, 2nd ed., 2016 + Doc 9859, 4th ed.; user holds the licensed documents).
- `KB-DATA-AVI-RISK-MATRIX` — ICAO 5×5 Risk Classification Scheme (`AVIATION_5X5` MatrixConfig) for `risk_matrix.score()` (source: ICAO Annex 19, 2016 / Doc 9859).
- `KB-SNIP-HOC` — hierarchy of controls (source: ISO 45001 8.1.2 / NIOSH / EU general principles of prevention, 2026).
- `KB-REG-IN-DGCA` — India DGCA State Safety Programme & operator SMS acceptance; management of change (source: DGCA CAR Section 1 SMS/SSP series + Annex 19 adoption; CAR numbering evolves — verify live).

---

### SME review & sign-off note

SME review ran (persona: **Aviation Management-of-Change safety assessor** — Annex 19 Pillar 2). Verified: new **and** changed hazards explicitly enumerated (10, including 7 the proposal omitted); each 5×5-scored (initial + residual) via the shared engine, not narratively dismissed; the change is concrete and named (vagueness confined to flagged [GAP]s, none reaching a conclusion); an explicit **approve/decline decision with recorded rationale** and named approval authority closes the assessment; mitigations HoC-ranked with the briefing-card-only proposal flagged as lower-order and escalated; interaction/latent cut-over hazards flagged (H10, combined-state); DGCA CAR/PBN/Cat C references cited as topics with exact clauses held as [GAP], never invented; zero de-identification leak. This is **decision-support only** — it **precedes and never replaces** the human competent-person (aviation-SME) sign-off.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
