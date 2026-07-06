<!-- LOCKED fixture — owner-LOCKED at the SW2 19-03 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Flight Data Monitoring (FDM/FOQA) — Quarterly Safety Analysis
## SMS Pillar 3 (Safety Assurance) · Approach & Landing Exceedance Review

| Document control | |
|---|---|
| **Artifact** | FDM/FOQA quarterly exceedance analysis → SMS findings & actions |
| **Operator / fleet** | **[GAP — operator legal name & AOC not supplied]** — referred to as *"the Operator"*; Airbus A320 fleet, scheduled passenger operations |
| **Certificating authority / SSP** | DGCA (India) — State Safety Programme, ICAO Annex 19 adoption |
| **SMS framework** | ICAO Annex 19 — Pillar 3, *Safety Assurance* (operational-data monitoring) `KB-STD-ICAO-ANNEX19` |
| **Reporting period** | This quarter (single period) — **exact dates [GAP]** |
| **Data basis** | User-supplied exceedance/event **summary counts only** (21 events). No raw flight data ingested or analysed. |
| **Prepared** | 5 July 2026 |
| **Status** | **Decision-support DRAFT** — assistive structuring; must be reviewed and validated by the competent person / FDM team before use |
| **Classification** | FDM/FOQA — **PROTECTED**. De-identified. Not to be used for any punitive or disciplinary purpose (data-protection / just-culture principle). |

---

## 0. Basis, boundary & de-identification statement (read first)

**Assistive boundary (stated up front).** This analysis **structures the exceedance summaries the Operator's FDM team supplied**. It does **not** ingest, replay, or analyse raw flight-data parameters, and it does **not** invent any exceedance count, threshold, or value. Every figure below traces to a supplied summary item. Anything not supplied is recorded as **[GAP]** and routed to the competent FDM team — never fabricated. The professional interpretation, hazard linkage, risk ranking and actions are the value added here; the underlying data analysis remains the FDM team's.

**Echo-back of confirmed intake (please confirm before this is relied upon):**
> Confirmed: an FDM/FOQA **single-period structuring** for **the Operator's A320 scheduled fleet**, under the **DGCA** SSP; **four finding classes / 21 events** drawn from supplied summaries; period **this quarter (exact dates [GAP])**; audience **internal FDM team + Safety Review Board (SRB)**. No trend baseline was supplied, so trend *direction* cannot yet be established (see §4). Crew detail de-identified; nothing computed from raw data.

**De-identification pass (run before drafting).** The supplied input is **aggregated exceedance counts** — it contains **no** crew names, flight numbers, tail numbers, dates, routes, bases, or health/personal identifiers. There was therefore nothing to scrub. Two principles nonetheless govern everything downstream:
- **Role labels only.** All owners below are role-based. No individual is named. FDM/FOQA data is doubly sensitive — it can identify a specific crew on a specific sector — so event-level handling must stay de-identified, held by the FDM gatekeeper, with any re-identification key access-controlled and held separately from this document.
- **Non-punitive use.** Consistent with the FDM data-protection foundation and a just-culture policy, this analysis and its source data must **never** feed a disciplinary process. That protection is what makes the programme work.

**Disclaimer.** This is decision-support only, not legal, airworthiness, or operational-approval advice. It **precedes and does not replace** sign-off by a competent person (aviation SME / the FDM team). It does not, and must not be read to, certify any approach, aircraft, or crew as compliant.

---

## 1. Executive summary

The quarter's monitoring surfaced **21 approach-and-landing exceedances across four metrics**, dominated by **unstabilised approaches (12)**. Read together, the four metrics do **not** look like four unrelated problems — they read as **one systemic approach-energy-management signal** expressing itself through four instruments:

> **high-and-fast approach → high rate of descent to recapture the profile → EGPWS sink-rate / "too-low-flap" cautions → late flap selection at high speed → flap-limit-speed exceedance.**

That common causal thread is the central finding (F-01, and the assurance view F-05). It is significant because **unstabilised approach continued to landing is the single most-cited precursor to runway excursions and approach-and-landing accidents** industry-wide (Flight Safety Foundation ALAR body of work — cited as context; exact statistics [GAP/verify]). Runway excursion remains the highest-frequency accident category for commercial jets.

**What we can conclude now:** the pattern, the hazard linkages, the risk ranking, and the interventions below.
**What we cannot conclude yet (honest limits):**
- **No trend direction.** One quarter is a *snapshot*, not a trend. A trend needs ≥2 periods of the same metrics (**[GAP] — prior-quarter series not supplied**).
- **No normalised rate.** 12 exceedances on 2,000 sectors is a very different signal from 12 on 20,000 sectors. The **exposure denominator (sectors/approaches flown) is [GAP]** and must be supplied before any rate, SPI, or acceptability judgement is finalised.
- **The most safety-critical single unknown** is whether the 12 unstable approaches were **continued to landing or resulted in a go-around** (**[GAP]**). A go-around is the safety system *working*; a continued approach is a *go-around-policy non-compliance* and a materially more serious finding.

**Risk-ranked headline:** F-01 (unstable approaches) is **Priority 1**; F-02 (high ROD) **Priority 2**; F-03 (EGPWS soft alerts) **Priority 3**; F-04 (flap-overspeed) **Priority 4 by volume but carries an immediate, non-deferrable airworthiness action** (inspection verification). F-05 (assurance-programme gaps: denominator, go-around linkage, baseline) is a systemic enabler that must be closed for the SMS to *measure* any of this.

---

## 2. Data basis — the supplied summary (verbatim counts)

The skill works **only** from these figures. Nothing here is inferred or computed.

| Ref | Exceedance / event class | Count (supplied) | Qualitative detail (supplied) |
|---|---|---:|---|
| D-1 | Unstabilised-approach exceedances | **12** | Predominantly **high-and-fast below 1,000 ft AAL**; **several with late configuration** |
| D-2 | High-rate-of-descent events **below 2,000 ft** | **4** | — |
| D-3 | GPWS/EGPWS **soft** alerts | **3** | "Soft" taken as **caution-level** alerts, not hard "PULL UP" warnings [ASSUMPTION — confirm event taxonomy] |
| D-4 | Flap-limit speed (V<sub>FE</sub>) exceedances | **2** | — |
| | **Total events this period** | **21** | |

**Not supplied (and therefore [GAP], not assumed):** the exposure denominator (sectors/approaches), the prior-period series, per-event severity band (Level 1/2/3), go-around outcomes, airport/runway/day-night/IMC-VMC/wind context, EGPWS alert sub-types, and V<sub>FE</sub>-inspection status. All are enumerated in the **[GAP] register (§8)** and routed to the FDM team.

---

## 3. Analysis — the systemic thread and per-metric interpretation

### 3.1 The systemic reading (the consultant insight)
The four metrics are **mechanically coupled** on a high-energy approach. This is presented as an **analytic hypothesis** to be confirmed by cross-tabulation (Action A-01), **not** an established fact:

- A **high-and-fast** state below 1,000 ft AAL (D-1) forces either an **increased descent rate** to recapture the vertical profile (→ D-2) or **late configuration** to add drag/decelerate.
- A high descent rate near the ground can trip **EGPWS Mode 1 "SINK RATE"**; late configuration can trip **"TOO LOW FLAP/GEAR"** (→ D-3).
- Selecting flap while still fast, to configure late, drives the aircraft through the **flap-limit speed** (→ D-4).

**Implication for treatment:** if the coupling holds, then fixing the **upstream energy state on approach** is the highest-leverage intervention — it drains all four metrics at once. Treating each metric in isolation (e.g., "brief crews about flap speeds") would be lower-order and incomplete. This drives the hierarchy-of-controls logic in §7.

### 3.2 Per-metric operational interpretation

**D-1 — Unstabilised approaches (12).** The dominant signal and the systemic root. Against a typical stabilised-approach gate (on-speed, in landing configuration, on profile, stabilised thrust, checklists complete by **1,000 ft AAL in IMC / 500 ft AAL in VMC** — *the Operator's own SOP gate governs and is [GAP]*), a "high-and-fast with late configuration" profile is the classic **energy-management** failure mode. Consequence hazards: long/fast/hard landing, **runway excursion (overrun)**, tail strike, and — where a low-energy recovery is mishandled — approach-and-landing accident. The decisive, missing datum is **go-around compliance** (§8, G-04): a non-stabilised approach that went around is a barrier success; one continued to landing is a policy breach.

**D-2 — High rate of descent below 2,000 ft (4).** A near-terrain high-energy state with a reduced margin for recovery and an elevated CFIT/hard-landing precursor profile. Most likely **correlated** with the D-1 "high-and-fast → dive to recapture" pattern; the overlap must be measured (A-06), not assumed.

**D-3 — GPWS/EGPWS soft alerts (3).** These are the **last automated barrier** before a warning. That the barrier fired is simultaneously reassuring (it works) and concerning (the flight path reached it). "TOO LOW FLAP" would tie **directly** to the late-configuration signal; "SINK RATE" ties to D-2. Two things must be checked: the **alert sub-types** and whether the **prescribed EGPWS response was flown** (A-07). Terrain-database/config currency is an airworthiness check.

**D-4 — Flap-limit speed exceedances (2).** Low count, but a **structural-airworthiness** matter: a V<sub>FE</sub> exceedance is the mechanical consequence of configuring late at high speed and typically triggers a **mandatory flap/slat inspection per the AMM/OEM**. This carries an **immediate action** (verify each inspection was raised and closed — A-08) that does **not** wait for the trend work.

### 3.3 What the pattern most likely points at (to be tested, not asserted)
- **Environmental clustering** — high-and-fast approaches frequently concentrate at particular airfields/runways (terrain-driven or ATC-driven high/tight descent profiles, short or non-precision runways, tailwind). **Airport/runway clustering is [GAP]** and is *not* crew-identifying — it is often the fastest route to a higher-order fix (A-01).
- **Automation/technique** — managed-mode vs selected-mode usage, autothrust engagement, and FMS descent-profile management on approach.
- **ATC profile** — "slam-dunk"/kept-high descents that leave insufficient track miles to decelerate and configure.

---

## 4. Trend assessment — honest limits (single-period data)

The request asked to "analyse the trends." **A trend cannot be established from one quarter.** Per the FDM discipline, a trend requires **≥2 periods** of the same metric. What is and is not possible now:

| Question | Answerable now? | Basis |
|---|---|---|
| Within-quarter **distribution / clustering** | **Yes** | The 12/4/3/2 split and the "high-and-fast below 1,000 ft" concentration are supplied |
| **Cross-metric correlation** (the systemic thread) | **Hypothesis only** | Requires the cross-tabulation in A-01/A-06 |
| **Normalised event rate** (per 1,000 sectors) | **No — [GAP]** | Exposure denominator not supplied (G-02) |
| **Trend direction** (improving / worsening / stable) | **No — [GAP]** | Requires the prior 3–4 quarters of the same metrics (G-03) |
| **Acceptability vs SPI alert/target level** | **No — [GAP]** | No SPI alert/target levels supplied (G-11) |

**Treat this quarter as a baseline snapshot.** Trend direction, rate normalisation, and SPI status are deferred to the FDM team via the [GAP] register and Actions A-10/A-13.

---

## 5. Findings register (risk-ranked)

Priority is an **indicative** severity × exposure ranking for tasking. **Formal ICAO 5×5 Risk Classification Scheme scoring is not performed in this skill** — it is assigned downstream in `aviation-hazard-register` once the exposure denominator and severity bands are available. That routing is itself an action (A-14).

| Ref | Finding | Events | Primary hazard / credible outcome | Indicative severity | Indicative likelihood basis | **Priority** |
|---|---|---:|---|---|---|:---:|
| **F-01** | Unstabilised approaches — high-and-fast <1,000 ft AAL, several late-config; **systemic energy-management root** | 12 | Runway excursion / long-fast-hard landing / tail strike / ALA | **Major–Hazardous** | Dominant class; 12 this period (rate pending G-02) | **P1** |
| **F-02** | High rate of descent <2,000 ft AAL | 4 | Near-terrain high energy; CFIT/hard-landing precursor; EGPWS Mode 1 | **Major–Hazardous** | 4 this period; likely correlated with F-01 | **P2** |
| **F-03** | GPWS/EGPWS soft (caution) alerts | 3 | Last-barrier activation; terrain-clearance / configuration margin erosion | **Major** | 3 this period; barrier fired | **P3** |
| **F-04** | Flap-limit speed (V<sub>FE</sub>) exceedances | 2 | Flap/slat structural overstress; airworthiness | **Minor–Major (structural)** | 2 this period | **P4** *(volume)* + **immediate airworthiness action** |
| **F-05** | **Assurance-programme systemic gap** — no exposure denominator, no go-around-outcome linkage, no prior-period baseline → the four signals cannot yet be normalised, trended, or judged against an SPI | n/a | The SMS cannot *measure* or *close the loop* on the above | **Systemic** | Enabler for F-01–F-04 | **Cross-cutting — resolve first** |

**Note on F-04:** its *trend* priority is P4, but a V<sub>FE</sub> exceedance is a **structural-inspection trigger** — Action A-08 is time-critical and independent of the trend work.

---

## 6. Hazard linkage (finding → SMS hazard → barrier that failed/held)

| Finding | Links to SMS hazard (register) | Barrier state |
|---|---|---|
| F-01 | *Unstable approach / approach-and-landing excursion* | Stabilised-approach gate + go-around policy — **effectiveness [GAP] pending go-around outcomes (G-04)** |
| F-02 | *Controlled flight toward terrain / high-energy near ground* | Descent-rate gate + EGPWS — EGPWS **held** in F-03 cases |
| F-03 | *Reduced terrain-clearance / configuration margin* | **EGPWS last barrier fired** (caution) — crew-response compliance **[GAP] (G-07)** |
| F-04 | *Flap/slat structural overstress* | Flap-speed schedule discipline — **breached**; airworthiness net = AMM inspection (A-08) |
| F-05 | *Ineffective safety assurance / unmeasurable SPI* | Monitoring loop incomplete — denominator + baseline + outcome linkage missing |

---

## 7. SMART actions — hierarchy-of-controls ranked

Actions are ranked **most-effective-first** per `KB-SNIP-HOC`. **Aviation note:** for flight-path safety hazards the effective barriers sit at **substitution/engineering (procedure design, automation, system barriers)** and **administrative (SOP, training, go-around policy, monitoring)**; classic **PPE is not the relevant last line** here — that is stated, not left as a gap. **Recurrent training alone (administrative) is explicitly *not* accepted as a complete treatment of F-01** — it is paired with higher-order substitution/engineering barriers below, or the reason a higher-order barrier is not reasonably practicable must be recorded at the SRB.

All owners are **role-based**. All dates in `D Month YYYY`.

| ID | Action (specific + measurable) | HoC level | Finding | Owner (role) | Due |
|---|---|---|---|---|---|
| **A-01** | Cross-tabulate the 12 F-01 events by **airport/runway, approach type, day/night, IMC/VMC, wind**; where they cluster, mandate the **precision/RNP approach** where available, publish an **airfield-specific high-energy briefing card**, and evaluate **continuous-descent / low-drag** profiles for the affected arrivals | **Substitution / Engineering** | F-01 | Flight Data Monitoring Analyst *(analysis)* → Head of Flight Operations / A320 Fleet Manager *(mitigation)* | Analysis **19 July 2026**; mitigation design **3 September 2026** |
| **A-02** | Review **automation & energy policy** on approach — autothrust + managed-speed usage, FMS descent-profile management, and speed/config-gate discipline; assess whether an **approach-energy-awareness aid** is reasonably practicable | **Engineering** | F-01 | A320 Fleet Manager / Chief Pilot | **3 September 2026** |
| **A-03** | Reinforce the **mandatory go-around gate** and a **no-fault, blame-free go-around policy** — the go-around is the expected outcome of a non-stabilised approach; issue an **Ops Notice** and brief the fleet | **Administrative** *(paired with A-01/A-02 — not admin-only)* | F-01 | Head of Flight Operations | **4 August 2026** |
| **A-04** | Deliver a **targeted recurrent sim module**: approach energy management, avoiding late configuration, and **go-around execution/decision-making** | **Administrative** | F-01 | Head of Training | Next recurrent cycle — **3 October 2026** |
| **A-05** | Reinforce **PM (pilot-monitoring) callout discipline** — "SPEED", "SINK RATE", "UNSTABLE" — and the "call and expect a response" standard | **Administrative** | F-01 | Chief Pilot | **4 August 2026** |
| **A-06** | **Overlap analysis** — cross-tab the 4 F-02 ROD events against the F-01 set; if correlated, fold into the F-01 mitigation; reinforce descent-rate awareness at the 1,000/500 ft gate | **Administrative / Engineering** | F-02 | Flight Data Monitoring Analyst + A320 Fleet Manager | **3 September 2026** |
| **A-07** | Review the **3 EGPWS soft alerts** by sub-type; confirm the **prescribed EGPWS response was flown**; verify **terrain-database & EGPWS config currency**; reinforce the mandatory-response SOP | **Administrative / Engineering** | F-03 | Flight Data Monitoring Analyst + A320 Fleet Manager + Head of Continuing Airworthiness *(database currency)* | **3 September 2026** |
| **A-08** | **IMMEDIATE — airworthiness.** Confirm each of the 2 V<sub>FE</sub> exceedances triggered the required **flap/slat structural inspection** per AMM/OEM, that findings are recorded, and each is **closed** | **Engineering / Airworthiness** | F-04 | Head of Continuing Airworthiness (CAMO) | **19 July 2026** |
| **A-09** | Address the **root** of F-04 (late config at high speed) via the F-01 energy interventions; reinforce the **flap-extension speed schedule** in briefings | **Administrative** *(root fix via A-01/A-02)* | F-04 | A320 Fleet Manager | Cross-ref F-01 — **3 September 2026** |
| **A-10** | Supply the quarter's **exposure denominator** (sectors/approaches); **normalise** each metric to a per-1,000-sectors rate; establish these as **SPIs with alert/target levels** aligned to the SSP ALoSP *(route to `aviation-spi-spt-framework`)* | **Engineering (data)** | F-05 | Flight Data Monitoring Analyst + Safety Manager | **4 August 2026** |
| **A-11** | Link each F-01 event to its **go-around outcome** (continued-to-land vs go-around); report **go-around-policy compliance** as an SPI | **Administrative** | F-05 | Flight Data Monitoring Analyst | **4 August 2026** |
| **A-12** | Table this analysis + action set at the next **Safety Review Board**; record **risk acceptance/rejection with rationale**; resource the interventions | **Administrative (governance)** | F-05 | Safety Manager *(table)* / Accountable Manager *(resource & accept)* | Next SRB — **[GAP: date]**; target **3 September 2026** |
| **A-13** | Compile the **prior 3–4 quarters** of the same four metrics to build the **longitudinal trend baseline** the single quarter cannot provide | **Administrative** | F-05 | Flight Data Monitoring Analyst | **4 August 2026** |
| **A-14** | Pass the validated, denominator-normalised findings to **`aviation-hazard-register`** for formal **ICAO 5×5 Risk Classification Scheme** scoring and register entry | **Administrative (governance)** | F-01–F-04 | Safety Manager | **3 September 2026** |

---

## 8. [GAP] register — routed to the competent FDM team (never fabricated)

| # | Missing datum | Why it matters | Owner to resolve |
|---|---|---|---|
| G-01 | Operator legal name, AOC number, A320 tail count | Document identity / scope | Safety Manager |
| G-02 | **Exposure denominator** — sectors/approaches flown this quarter | No normalised rate or acceptability judgement without it | FDM Analyst |
| G-03 | **Prior-period series** (previous 3–4 quarters, same metrics) | Required for *any* trend-direction statement | FDM Analyst |
| G-04 | **Go-around outcomes** for the 12 F-01 events (continued-to-land vs go-around) | Distinguishes barrier success from policy breach — most safety-critical unknown | FDM Analyst |
| G-05 | Per-event **severity band** (Level 1/2/3 / high-med-low) — were any Level 3? | Severity weighting of the ranking | FDM Analyst |
| G-06 | **Airport/runway, day/night, IMC/VMC, wind** per event | Environmental clustering → higher-order fix (A-01) | FDM Analyst |
| G-07 | **EGPWS alert sub-types** + crew-response compliance (3 events) | Confirms which barrier and whether response was correct | FDM Analyst / Fleet Manager |
| G-08 | **V<sub>FE</sub> inspection status** (raised/closed) for the 2 events | Airworthiness closure (A-08) | Head of Continuing Airworthiness |
| G-09 | **Exact DGCA CAR** Section/Series/number for the FDM/FDA requirement | Regulatory citation accuracy | Safety Manager |
| G-10 | **Exact ICAO Annex 6, Part I** clause for the FDA-programme requirement (>27,000 kg MCTOM) | Regulatory citation accuracy | Safety Manager |
| G-11 | Operator's **stabilised-approach SOP gate** + current **SPI alert/target levels** | Baseline against which events are judged | Fleet Manager / Safety Manager |
| G-12 | **Aircraft/base recurrence** (same tail/base — *not* crew) | Non-crew clustering signal | FDM Analyst |

---

## 9. Assumptions register

| # | Assumption | To confirm |
|---|---|---|
| A/1 | The four metrics share a common **approach-energy-management** root (the §3.1 thread) — a *hypothesis*, not a fact | Confirmed/refuted by A-01/A-06 cross-tabulation |
| A/2 | "**Soft**" GPWS/EGPWS alerts = caution-level, not hard "PULL UP" warnings | Operator's event taxonomy (G-07) |
| A/3 | The Operator runs a **mandatory go-around** at its stabilised-approach gate | Operator SOP (G-11) |
| A/4 | A V<sub>FE</sub> exceedance triggers a **mandatory AMM flap/slat inspection** | Operator AMM/MEL procedure (G-08) |
| A/5 | Standard gate ≈ **1,000 ft AAL (IMC) / 500 ft AAL (VMC)** | Operator's own SOP gate governs (G-11) |

---

## 10. Regulatory & framework anchors

- **ICAO Annex 19 — Pillar 3 (Safety Assurance):** FDM/FOQA is an *operational-data monitoring input* to safety performance monitoring & measurement. This analysis is a Pillar-3 assurance product feeding the SPI framework and the SRB. *(Topic cited per `KB-STD-ICAO-ANNEX19`; ICAO text not reproduced — the Operator holds the licensed documents.)*
- **DGCA State Safety Programme (India):** The DGCA operates the SSP and **accepts** the Operator's SMS under its CAR framework adopting Annex 19; the **Accountable Manager** and **Safety Manager** are named SMS roles. **The exact DGCA CAR Section/Series/number mandating flight-data monitoring is [GAP] (G-09) — verify against the live DGCA CAR; not fabricated here.** *(`KB-REG-IN-DGCA`.)*
- **ICAO Annex 6, Part I — Flight Data Analysis Programme:** an FDA programme is required for aeroplanes above **27,000 kg MCTOM**; the A320 (MTOM well above this) is in scope. **Exact clause number is [GAP] (G-10) — verify against the licensed Annex 6.**
- **Hierarchy of controls** (`KB-SNIP-HOC`) applied to every action in §7; the lower-order-only justification requirement is recorded against F-01.

---

## 11. SME review & sign-off note

**SME review: ran.** Personas: **FDM/FOQA analyst** (analytic lens) with an **SME line-pilot / fleet reviewer** lens (operational lens) — ICAO Annex 19 Pillar 3, `status: assistive`. Checks applied:

- ✅ **Assistive boundary holds** — no exceedance count/value invented; every figure (12/4/3/2) traces to the supplied summary; all absent data recorded as **[GAP]** and routed to the FDM team.
- ✅ **Not autonomous raw-data analysis** — no result is presented as computed from raw parameters; the §3.1 coupling is flagged as a *hypothesis* for cross-tabulation.
- ✅ **Thresholds sensible** — the stabilised-approach gate, EGPWS caution taxonomy, and V<sub>FE</sub>/AMM linkage are line-plausible; operator-specific gate values flagged [GAP], not asserted.
- ✅ **Trend vs one-off discriminated** — a single quarter is **not** reported as a trend; trend direction explicitly deferred pending ≥2 periods (§4).
- ✅ **Crew de-identification protected** — input carried no crew identifiers; role labels only; non-punitive-use principle stated. **Zero de-id leak.**
- ✅ **Findings reach systemic SMS actions** — HoC-ranked, role-owned, dated; no crew-blame conclusion; F-01 not treated by training alone.
- ✅ **Citations not invented** — DGCA CAR and Annex 6 clause numbers held as **[GAP]** for verification.

This is **decision-support only**. It **precedes and does not replace** the human competent-person / FDM-team sign-off, and it does not assert "approved by a competent person." Any FLAG is recorded, not merge-blocking; the de-identification and citation-accuracy gates are hard blocks and passed.

**Competent-person sign-off (to be completed by the Operator):**

| Role | Name | Signature | Date |
|---|---|---|---|
| Flight Data Monitoring Analyst / Manager | | | |
| Safety Manager | | | |
| Accountable Manager (risk acceptance) | | | |

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
