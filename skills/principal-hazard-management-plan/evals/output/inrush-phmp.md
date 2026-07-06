<!-- LOCKED fixture — owner-LOCKED at the SW4 19-05 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Principal Hazard Management Plan (PHMP)
## Principal Hazard: INRUSH / INUNDATION — Underground Coal Mine

| Document control | |
|---|---|
| **Principal hazard** | Inrush / inundation (uncontrolled ingress of water, slurry, or gas from a body of water or waterlogged void) |
| **Mine / operation** | Underground coal mine *(named mine, lease, and seam to be inserted by the operation)* |
| **Commodity / method** | Coal — underground (bord-and-pillar / longwall — confirm at site) |
| **Document type** | Principal Hazard Management Plan — workshop-structured, hierarchy-of-controls ranked, ICMM CCM–linked |
| **Status** | Decision-support draft for competent-person review — **not an approved plan** |
| **Version / date** | v0.1 (draft) — 6 July 2026 |
| **Accountable owner** | Mine Manager |
| **Prepared with** | Technical Services Manager · Hydrology Competent Person · Geotechnical / Strata-Control Engineer · Ventilation Officer · Mine Surveyor |
| **Next scheduled review** | 6 July 2027, or on trigger (see §12) — whichever is sooner |

> **Scope note on this draft:** every site-specific engineering value that has not been supplied by a competent person is marked **`[GAP]`** and routed to the named competent person (Hydrology / Geotechnical). No standoff distance, barrier-pillar dimension, borehole density, or trigger threshold has been invented. This document **structures** the multidisciplinary inrush workshop; the mine team owns the engineering judgement and a competent person signs off before issue.

---

## 1. Purpose & Scope

### 1.1 Purpose
This PHMP defines how the operation identifies, assesses, and controls the **principal hazard of inrush / inundation** — the sudden, uncontrolled entry of water, water-borne solids (slurry, silt, peat, tailings), or accumulated gas from a body of water or a waterlogged void into a working place, such that persons underground may be drowned, entrapped, swept, or asphyxiated. It sets out the control framework (hierarchy-of-controls ranked), the standoff/barrier design basis, the monitoring regime, the Trigger Action Response Plan (TARP), accountabilities, and the assurance/verification schedule.

### 1.2 In scope
- All current and planned underground workings, roadways, and inbye faces of the operation.
- All credible sources of inrush: abandoned/old workings (own and adjacent leases), surface and underground water bodies, water-bearing strata / aquifers, saturated unconsolidated deposits, surface water ingress via shafts/drifts/subsidence, and boreholes/wells as conduits.
- The interface with adjacent leaseholders where old workings may cross a boundary.

### 1.3 Out of scope (managed by linked plans — cross-referenced, not re-authored)
- **Mine dewatering pump/reticulation design & maintenance** → Dewatering / Mine Services plan (a control *input* here).
- **Gas from old workings (stythe/blackdamp CO₂-N₂, firedamp CH₄, CO)** as a *ventilation/atmosphere* hazard → Ventilation Management Plan and the **fire/explosion** and **ventilation-failure** PHMPs (interface only; inrush-borne gas release is covered here as a consequence pathway).
- **Emergency egress, self-escape, and rescue mobilisation** → Mine Emergency Response Plan / mine-rescue ERP (this PHMP defines the *trigger to invoke* it).
- **Tailings-storage-facility failure** as a surface source → TSF management (interface where a TSF overlies or drains toward workings).

---

## 2. Legal & Standards Framework

> **Jurisdiction is not stated in the task and is therefore `[GAP]`.** Per the skill's rule, no specific national statute is cited as authoritative here. The applicable coal-mining inrush statute **must be resolved and applied by the competent person** once the mine's jurisdiction is confirmed. The framework below is the jurisdiction-independent management-system spine plus the *categories* of statutory duty that coal-mining regulators typically impose for inrush.

| Layer | Basis | Applied here |
|---|---|---|
| Management-system spine | **ISO 45001:2018 cl. 6.1.2** (hazard identification & assessment of risk) and **cl. 8.1** (operational control) | HIRA structure, control-of-operations, this PHMP as an operational control |
| Critical-control framing | **ICMM Critical Control Management (CCM)** — material unwanted event → critical control → performance requirement → verification → accountability (jurisdiction-independent, `KB-STD-ICMM-CCM`) | §5–§6, §10 linkage; user holds their licensed ICMM guidance |
| Statutory inrush duties **[GAP — resolve to the mine's regulator]** | Coal-mining statutes commonly impose, in some form: (a) **barrier / standoff against bodies of water and waterlogged workings**; (b) **advance / flank boring (probe drilling) when approaching a water danger zone**; (c) **precautions near surface water bodies, rivers, tanks, and the sea**; (d) **maintenance and inspection of plans of old workings**; (e) **notification / permission to work near water**. The exact provision, the statutory barrier formula, and the mandatory danger-zone width are **jurisdiction-specific and must be inserted by the competent person.** | §2 note, §6 design basis, §9 monitoring |
| Records / plans | Statutory mine plans, abandonment plans, and adjoining-lease plans as the primary evidence base for source location | §4.2 |

**Action `[GAP-LEGAL]`:** Technical Services Manager to record the confirmed jurisdiction and the exact statutory inrush provisions (barrier requirement, danger-zone width, advance-boring duty, notification duty) before this PHMP is issued.

---

## 3. Roles & Required Competencies

| Role (owner label) | PHMP responsibility | Competency basis |
|---|---|---|
| **Mine Manager** | Accountable owner; approves the PHMP; ensures resources; final TARP escalation authority | Statutory mine manager |
| **Technical Services Manager** | Custodian of the PHMP; integrates geotech, hydrology, survey, ventilation inputs; owns the standoff/barrier design register | Mining engineering + management |
| **Hydrology Competent Person** (hydrogeologist) | Owns the water-source model, hydrostatic head, aquifer/recharge assessment, standoff hydraulic basis, and piezometric trigger thresholds | Chartered/registered hydrogeology |
| **Geotechnical / Strata-Control Engineer** | Owns barrier-pillar strength/stability, rock-cover competence, conduit (fault/dyke) assessment, and floor/roof failure pathway to a water source | Chartered/registered geotechnical |
| **Mine Surveyor** | Owns positional accuracy of old-workings plans, boundary barriers, standoff marking underground, and the "as-approached" survey | Registered mine surveyor |
| **Ventilation Officer** | Owns inrush-borne gas (stythe/blackdamp/firedamp/CO) monitoring and refuge/atmosphere interface | Statutory ventilation competency |
| **Undermanager / Deputy (statutory official)** | Shift-level execution of TARP, pre-shift inspection of danger zones, workforce withdrawal authority | Statutory official |
| **Dewatering / Mine Services Engineer** | Owns pump capacity, sumps, standby capacity, and reticulation availability as a mitigative control | Mechanical/mine services |
| **Workforce (competent persons)** | Recognise and report early inrush indicators; comply with danger-zone controls; respond to withdrawal | Task-competent + inrush-awareness inducted |

---

## 4. Hazard Identification & Credible Inrush Scenarios

### 4.1 Material Unwanted Event (MUE)
**MUE:** *Sudden uncontrolled inrush of water, slurry, or accumulated gas into an active working, resulting in drowning, entrapment, being swept, or asphyxiation of persons inbye.*
Inrush is a **catastrophic-consequence** principal hazard: the consequence is largely fixed (multiple fatality potential); the plan therefore **manages likelihood, not consequence** — residual risk is reduced by driving down probability, not by softening the outcome.

### 4.2 The water-source model (evidence base)
The credible-source model is built from, and only as reliable as, the following evidence — **the accuracy and completeness of old-workings plans is itself the single largest inrush risk factor** and is treated as a critical assumption:

- Statutory mine plans, abandonment plans, and **adjoining-lease** plans (own + neighbours).
- Historical dewatering / making-water records and past inrush or making-water events.
- Hydrogeological survey: aquifer horizons, standing water levels, recharge, hydraulic connectivity.
- Geological model: seam floor/roof lithology, faults, dykes, wash-outs, palaeochannels, and old boreholes/shafts as conduits.
- Surface features: water bodies, rivers, tanks/reservoirs, TSFs, wet ground, and subsidence troughs that could pond or connect.

> **Critical assumption `[GAP-PLANS]`:** where old-workings extents or water levels are **unrecorded, approximate, or of unknown datum**, the Hydrology + Geotechnical Competent Persons must treat the void as **water-filled and at worst-credible head** until proven otherwise. Positional uncertainty of the plan is to be quantified by the Mine Surveyor and added to the standoff (§6).

### 4.3 Credible scenarios (each carries its own pathway and controls)

| # | Credible scenario | Inrush mechanism / pathway | Aggravating factors |
|---|---|---|---|
| **S1** | **Approach to old / abandoned workings** (own or adjacent lease) that are, or may be, water- and/or gas-filled | Development or extraction breaches the barrier or holes through into a flooded void; sudden release of impounded water **plus** displaced accumulated gas (stythe/blackdamp, CO₂, CH₄, CO) | Inaccurate/absent plans; unknown water level; pillar robbing; boundary/lease-edge workings; goaf on the adjacent side |
| **S2** | **Surface or underground water body** (river, reservoir/tank, sea, lake, flooded shaft, sub-surface reservoir) above or hydraulically connected to workings | Insufficient rock cover / failed barrier lets the body drain to the working via induced fracturing, caving, or subsidence-connected cracks | Shallow cover; longwall caving to surface; monsoon/flood stage; thin/weak parting to seam above |
| **S3** | **Aquifer / water-bearing strata** (permeable sandstone, fractured/karst limestone, gravels, saturated unconsolidated deposits) | Face or floor intersects a charged, permeable or fractured horizon; pressurised inflow, or floor-heave "blow-up" from an underlying confined aquifer | High hydrostatic head; faults/dykes as conduits; thin floor to a confined aquifer; dewatering-induced gradient changes |
| **S4** | **Surface-water ingress via mine openings** (shaft, drift, decline, borehole, subsidence crack) | Flood/monsoon surface water enters directly through openings or subsidence cracks and reaches workings | Extreme rainfall; blocked surface drainage; low-lying portals; unsealed exploration boreholes |
| **S5** | **Conduit-driven connection** (fault, dyke, unsealed borehole, old shaft) linking any of the above to the working | A geological or man-made conduit short-circuits an otherwise adequate barrier | Poorly located historical boreholes; transmissive faults; mining across a dyke |

### 4.4 Inherent risk rating (default 5×5 — confirm against the org matrix)

Scored on the default 5×5 (D-02 bands: score = Likelihood × Consequence; **Low 1–4 · Medium 5–9 · High 10–15 · Critical 16–25**). **Confirm these bands against the operation's own matrix before issue.**

| Scenario | Consequence (C) | Likelihood (L) — *uncontrolled* | Score | Band |
|---|---|---|---|---|
| S1 Old workings | 5 (Catastrophic — multi-fatality) | 4 (Likely on unmanaged approach) | 20 | **Critical** |
| S2 Water body | 5 | 3 (Possible) | 15 | **High** |
| S3 Aquifer / water-bearing strata | 5 | 3 (Possible) | 15 | **High** |
| S4 Surface-water ingress | 4 (Major) | 3 (Possible) | 12 | **High** |
| S5 Conduit connection | 5 | 3 (Possible) | 15 | **High** |

*Likelihood ratings are indicative for workshop calibration; the workshop and the Hydrology/Geotechnical Competent Persons set the site-specific L for each scenario against the confirmed source model. Consequence is held at catastrophic for the drowning/entrapment pathways and is not discounted.*

---

## 5. Control Framework (Hierarchy of Controls)

Controls are ranked **most-effective first** per `KB-SNIP-HOC` (Elimination → Substitution → Engineering/Isolation → Administrative → PPE). Controls marked **[CC]** are **critical controls** — those that, if absent or failed, allow the MUE to occur or escalate; they are linked to the ICMM CCM in §10 with a performance requirement and verification. **No principal-hazard scenario is left to administrative/PPE controls alone** — where a lower-order control is the last line, the higher-order control it backs up is named.

### 5.1 Elimination
- **E1 — Design workings to avoid the water danger zone entirely.** Lay out development and extraction so no working enters the precautionary/danger zone around a credible water source; leave the source impounded and untouched. *(Most effective control; where geometry allows, this eliminates S1/S2/S5 at the source.)* **[CC]**
- **E2 — Pre-drain / de-water the source before mining approaches** (controlled dewatering of old workings or aquifer to remove the impounded head), where hydrogeologically feasible and the discharge is licensed. Converts a sudden-release hazard into a managed inflow. **[CC]**

### 5.2 Substitution
- **Su1 — Substitute the mining method / sequence** to reduce caving connection to an overlying water body (e.g., method or extraction-height choice that limits the caving/fracture height beneath S2), subject to geotechnical determination of the connective-fracture zone height **`[GAP — value from Geotechnical Competent Person]`**.

### 5.3 Engineering & isolation controls
- **En1 — Barrier pillar / standoff against the water source** left in situ and surveyed, dimensioned to the design basis in §6. **[CC]** *(Primary engineered barrier for S1/S2/S3/S5.)*
- **En2 — Advance & flank probe drilling (boring-in-advance)** ahead of and to the sides/rise/dip of the face when working within the danger zone, to detect and controlled-release water/gas before the face breaks through. Pattern, length, angle, and spacing per §6. **[CC]**
- **En3 — Controlled bleed / borehole drainage** with standpipes, valves, and pressure gauges so any intercepted water is released in a controlled manner rather than by breakthrough. **[CC]**
- **En4 — Dewatering capacity & sumps** sized with standby margin to handle the design inflow and maintain a pumping reserve; independent power/standby to pumps. *(Mitigative — buys withdrawal time; does not replace En1/En2.)*
- **En5 — Surface-water control** for S4: bunds, cut-off drains, sealed/collared boreholes, raised/protected portals, and subsidence-crack grouting to prevent surface water reaching openings.
- **En6 — Sealing / plugging of identified conduits** (old boreholes, shafts, transmissive faults) for S5, where located and accessible.

### 5.4 Administrative controls (backing the engineered barriers — never the sole treatment)
- **A1 — Danger-zone / precautionary-zone demarcation** on plans and physically underground; "no advance without permit" rule inside the zone. *(Backs En1/En2 — controls human breach of the barrier.)*
- **A2 — Inrush / water-danger permit-to-work** and an authority-to-mine sign-off by the Technical Services Manager + competent persons before any working enters the danger zone.
- **A3 — Standard operating procedure for approaching water** (probe-drill-before-advance discipline, maximum advance per drilling cycle, stop-and-report rules).
- **A4 — Survey control & plan maintenance:** up-to-date, correctly-datum'd plans of old workings and the "as-approached" position, re-checked each cycle. *(Backs E1/En1 — the barrier is only real if the source position is right.)*
- **A5 — Pre-shift inspection** of danger-zone workings for early indicators (making water, seepage, wet ribs, gas) by the statutory official.
- **A6 — Inrush-awareness training & drills** so every person recognises and reports early indicators and knows the escape route/muster.
- **A7 — Management of Change** for any layout change, seam/level change, or new information that alters the source model (triggers PHMP review, §12).

### 5.5 PPE (last line — never a treatment of the inrush itself)
- **P1 — Self-rescuers / self-contained self-rescuers (SCSR)** and cap lamps for escape through an inrush-degraded / gas-affected atmosphere; **P2 — lifelines/refuge provisions** per the ERP. *(Facilitates escape only; provides **no** protection against the inrush event and does not reduce its likelihood.)*

> **Lower-order-control flag:** A1–A7 and P1–P2 are recorded as administrative/PPE and are **explicitly not accepted as a standalone treatment** of any inrush scenario. Each is tied above to the higher-order engineering/elimination control it backs up. If, at the workshop, any scenario is found to rely on administrative/PPE controls **only** (e.g., an unlocatable conduit where En6 is not practicable), that reliance must be **justified as not-reasonably-practicable-to-engineer or escalated to the Mine Manager** — it is not signed off silently.

---

## 6. Standoff & Barrier Design Basis

**This section states the design *method and inputs*. It does NOT state a standoff distance, barrier-pillar dimension, or borehole density — those are jurisdiction- and site-specific engineering values that must be determined by the Hydrology and Geotechnical Competent Persons (and the statutory barrier requirement applied). Each such value is `[GAP]` below.**

### 6.1 What the standoff/barrier must achieve (performance intent)
A retained barrier (En1) plus the advance-boring regime (En2) together ensure that: (a) the impounding barrier between the working and the credible water source **cannot fail** under the worst-credible hydrostatic head; and (b) if the working must enter the precautionary zone, water/gas is **detected and controlled-released** by probe drilling **before** the face can break through.

### 6.2 Design inputs (the competent person must quantify each)
| Input | Symbol / description | Value |
|---|---|---|
| Worst-credible hydrostatic head at the source | H — standing water level / potentiometric head relative to the working, at worst credible (e.g., monsoon/recharge) stage | `[GAP — Hydrology Competent Person]` |
| Rock-cover / parting competence | Lithology, strength, and thickness of strata between working and source; presence of weak floor/roof | `[GAP — Geotechnical Competent Person]` |
| Caving / connective-fracture-zone height (S2) | Height above extraction to which caving/fracturing connects to an overlying body | `[GAP — Geotechnical Competent Person]` |
| Geological conduits | Faults, dykes, wash-outs, old boreholes/shafts crossing the barrier | Located + characterised `[GAP — Geotechnical/Survey]` |
| Positional uncertainty of source | Survey error band on old-workings extent / water level (added to standoff) | `[GAP — Mine Surveyor]` |
| Applicable statutory minimum barrier | The regulator's prescribed barrier formula / minimum against water & waterlogged workings | `[GAP — Technical Services Manager, per §2]` |
| Factor of safety | Design factor applied over the greater of the calculated and statutory minimum | `[GAP — competent person]` |

### 6.3 Barrier-pillar dimension (En1)
- **Design rule (method):** the retained barrier width is the **greater of** (a) the geotechnically-calculated width that resists the worst-credible head H with the design factor of safety, and (b) the **statutory minimum barrier** — **plus** the surveyed positional-uncertainty allowance.
- **Barrier width value:** **`[GAP]`** — to be calculated and signed by the Geotechnical + Hydrology Competent Persons and the Technical Services Manager; **not invented here.**
- The barrier, once set, is **surveyed, marked underground, and recorded on the plan as a no-work exclusion**; it is not to be reduced or robbed (linked to A1/A4).

### 6.4 Precautionary ("danger") zone & advance-boring regime (En2/En3)
- **Danger-zone width** (the distance from a credible source within which no advance is permitted without probe drilling): **`[GAP — per statute + competent person]`.**
- **Advance / flank / rise / dip borehole pattern** — number of holes, spacing/fan angle, length ahead of the face, minimum unbored coal to be maintained ahead, and re-drill interval per advance: **`[GAP — density and geometry from the competent person]`. No borehole density or spacing is invented here.**
- **Controlled-release provisions:** standpipes, valves, and pressure gauges (En3) with a defined maximum safe advance per drilling cycle **`[GAP]`**, so intercepted water is bled off, not broken into.

### 6.5 Design record
The completed standoff/barrier design (all `[GAP]` values resolved, calculations attached, statutory basis cited) is held in the **Standoff & Barrier Design Register** owned by the Technical Services Manager, signed by the Hydrology and Geotechnical Competent Persons, and is the controlling document for §10 verification.

---

## 7. Monitoring Regime

Monitoring detects the early indicators of an impending inrush and confirms the barriers are performing. Each activity has an owner and a cadence; **numeric alarm thresholds are set by the Hydrology Competent Person and are `[GAP]` where not yet calibrated** (they must be site-derived, not assumed).

| Monitored parameter | Method | Cadence | Owner | Alarm threshold |
|---|---|---|---|---|
| Making-water rate (inflow into workings) | Pump run-hours / flow metering; V-notch at sumps | Each shift + trend weekly | Dewatering / Mine Services Engineer | `[GAP]` — set rate-of-rise trigger |
| Piezometric head at source / aquifer | Standpipe / vibrating-wire piezometers, monitoring bores | Continuous / weekly read | Hydrology Competent Person | `[GAP]` — set head trigger |
| Water quality / temperature / clarity at face | Field observation + probe | Each advance in danger zone | Undermanager / Deputy | Any change from baseline → report |
| Advance-borehole strike (water/gas) | Probe-drill logging: flow, pressure, gas | Every drilling cycle | Undermanager / Deputy | Any strike → stop & TARP |
| Atmosphere for inrush-borne gas (CH₄, CO, CO₂, O₂ deficiency / stythe) | Fixed + portable gas detection near danger-zone faces | Continuous + pre-shift | Ventilation Officer | Statutory gas limits |
| Roof/floor movement & seepage in danger zone | Visual + convergence / seepage inspection | Pre-shift | Undermanager / Deputy | New seepage / heave → report |
| Rainfall / river / reservoir / TSF stage (S2/S4) | Site + regional gauges; flood warnings | Daily + on warning | Technical Services Manager | Flood-stage trigger `[GAP]` |
| Surface subsidence / crack development | Subsidence survey; visual | Per survey cycle | Mine Surveyor | New connective crack → report |
| Dewatering system availability (mitigative reserve) | Pump/standby/power status check | Each shift | Dewatering / Mine Services Engineer | Loss of standby margin |

**Baseline requirement:** the Hydrology Competent Person establishes the normal baseline for making-water, head, and quality **before** danger-zone work begins, so a *deviation* (not just an absolute value) can trigger the TARP.

---

## 8. Trigger Action Response Plan (TARP)

Three escalating levels. **Triggers escalate on the worst single indicator** — you do not average. Where a numeric threshold is needed it is set by the Hydrology Competent Person and shown `[GAP]` until calibrated; the *qualitative* trigger stands regardless. Actions are cumulative up the levels.

| Level | Trigger (observed condition) | Action | Responsible role |
|---|---|---|---|
| **1 — Green / Alert (heightened monitoring)** | Making-water above baseline but stable (< threshold `[GAP]`); minor new seepage/damp rib in danger zone; rainfall/river approaching watch stage; piezometric head rising slowly within limits | Increase monitoring frequency; verify probe-drilling compliance and pump/standby availability; log and trend; brief oncoming shift; Hydrology Competent Person to review trend within 24 h | Undermanager / Deputy (initiate); Dewatering Engineer; **Hydrology Competent Person** (review) |
| **2 — Amber / Alarm (control face activity)** | Rate-of-rise in making-water above trigger `[GAP]`; sustained piezometric head rise; change in water clarity/temperature/taste at face; probe hole gives increasing flow or gas; rainfall/river/reservoir at warning stage; loss of pump standby margin | **Stop advance in the affected working**; withdraw non-essential persons from inbye of the danger zone; increase probe drilling / reduce max advance; bring standby pumping online; Technical Services Manager + Hydrology + Geotechnical Competent Persons convene to reassess the standoff/barrier basis before any resumption; notify Mine Manager | **Undermanager / Deputy** (stop & withdraw); **Technical Services Manager** (convene reassessment); Mine Manager (notified) |
| **3 — Red / Emergency (withdraw & invoke ERP)** | Sudden increase / uncontrolled inflow of water or slurry; borehole or face breakthrough into a void; sudden gas make (stythe/blackdamp/CH₄/CO) with inflow; pumps overwhelmed / dewatering failure with rising water; flood water entering openings (S4) | **Immediate withdrawal of all persons** to surface / to designated refuge along the pre-planned egress route; **invoke the Mine Emergency Response Plan / mine-rescue ERP**; account for all persons; isolate power as per ERP; make statutory notifications; no re-entry until Mine Manager + competent persons authorise | **Undermanager / Deputy** (order withdrawal); **Mine Manager** (invoke ERP & authorise re-entry); Ventilation Officer (atmosphere); Mine Surveyor/Hydrology (post-event assessment) |

**Standing rule:** any person underground who observes a Level-3 indicator has the **authority and duty to raise the alarm and initiate withdrawal without waiting for instruction** (stop-work authority). Re-entry after any Level-2 stoppage or Level-3 event requires a documented competent-person reassessment and Mine Manager authorisation.

---

## 9. Accountabilities Matrix (RACI)

**R** = Responsible (does the work) · **A** = Accountable (owns the outcome, one per row) · **C** = Consulted · **I** = Informed.

| Activity | Mine Manager | Technical Services Mgr | Hydrology CP | Geotech CP | Mine Surveyor | Ventilation Officer | Undermanager/Deputy | Dewatering Eng. |
|---|---|---|---|---|---|---|---|---|
| Approve & own the PHMP | **A** | R | C | C | C | C | I | I |
| Confirm jurisdiction & statutory inrush duties (§2) | A | **R** | C | C | C | I | I | I |
| Build/maintain water-source model & plans (§4.2) | I | A | R | R | **R** | C | I | I |
| Set standoff/barrier design basis (§6) | A | **R** | R | R | C | I | I | C |
| Resolve `[GAP]` engineering values | I | A | **R** (hydraulic) | **R** (geotech) | C | I | I | C |
| Advance/flank probe-drilling regime (En2/En3) | I | A | C | C | C | I | **R** | I |
| Monitoring regime & thresholds (§7) | I | A | **R** | C | C | R | R | R |
| Execute TARP at the face (§8) | A (L3) | C | C | C | I | R | **R** | R |
| Invoke Emergency Response Plan | **A** | C | C | C | I | R | R | I |
| Assurance / verification (§10) | A | **R** | R | R | R | R | R | R |
| PHMP review & MOC (§12) | A | **R** | C | C | C | C | I | I |

---

## 10. Assurance & Verification Schedule (ICMM CCM linkage)

Each **critical control [CC]** carries a performance requirement and a verification activity + frequency + accountable role, per the ICMM CCM structure (`KB-STD-ICMM-CCM`). This PHMP **links** to the operation's ICMM Critical Control Management register; it does not re-invent it. Performance-requirement values marked `[GAP]` are carried over from the §6 design once resolved.

| Critical control | Performance requirement | Verification activity | Frequency | Accountable role |
|---|---|---|---|---|
| **E1 — Avoid danger zone by design** | No planned working enters the precautionary zone of a credible source without §6 authority | Layout review against source model before each panel/level design | Per panel design + on MOC | Technical Services Manager |
| **E2 — Pre-drainage of source** (where used) | Source head reduced to design target before approach; discharge licensed | Head monitoring vs. target; discharge compliance check | Weekly during drainage | Hydrology Competent Person |
| **En1 — Barrier pillar / standoff** | Barrier ≥ the greater of calculated + statutory min, + survey allowance (value `[GAP]`); surveyed & un-robbed | Independent survey audit of barrier position vs. plan; design re-check | Each cycle in danger zone + quarterly audit | Mine Surveyor / Technical Services Manager |
| **En2 — Advance/flank probe drilling** | Design pattern maintained; minimum unbored coal ahead upheld each advance (value `[GAP]`) | Drilling-log audit vs. design; deputy sign-off per cycle | Every drilling cycle + weekly audit | Undermanager / Deputy |
| **En3 — Controlled bleed / borehole drainage** | Standpipes/valves/gauges fit for worst-credible head; controlled release only | Function test of standpipe/valve; pressure-integrity check | Per installation + before each danger-zone advance | Technical Services Manager |
| **En4 — Dewatering capacity (mitigative)** | Design inflow + standby margin available; independent power | Pump capacity & standby test; power-failover test | Monthly + before danger-zone entry | Dewatering / Mine Services Engineer |

**Layered assurance:**
- **Line 1 (do & check):** deputy/official pre-shift and per-cycle checks (above).
- **Line 2 (oversight):** Technical Services Manager quarterly assurance review of the standoff/barrier register, drilling logs, and monitoring trends.
- **Line 3 (independent):** periodic independent audit of the inrush control set and PHMP effectiveness — cadence set by the operation (e.g., annual), reported to the Mine Manager. Any critical-control failure or "bad actor" trend is a PHMP review trigger (§12).

---

## 11. Residual Risk

With the full control suite verified effective, likelihood is driven down but **consequence remains catastrophic** (drowning/entrapment potential is not softened). Illustrative residual (workshop to confirm on the org matrix):

| Scenario | Residual L (controls effective) | C | Residual score | Band |
|---|---|---|---|---|
| S1 Old workings | 2 (Unlikely) | 5 | 10 | **High** |
| S2 / S3 / S5 | 2 | 5 | 10 | **High** |
| S4 Surface ingress | 2 | 4 | 8 | **Medium** |

Inrush residual risk remaining **High** is expected and honest for a catastrophic-consequence principal hazard: it signals that the controls require **continuous verification**, not that the plan is inadequate. Residual risk is only valid while every critical control is verified in §10.

---

## 12. Review & Management of Change

- **Scheduled review:** annually — **next review 6 July 2027** — by the Mine Manager and competent persons.
- **Triggered review (any of):** a Level-2 or Level-3 TARP event; new information changing the source model (newly discovered old workings, revised water levels, new borehole data); a layout/method/seam change; a critical-control failure or adverse verification trend; a regulatory change to the statutory inrush provisions (§2); or an inrush incident at this or a comparable mine.
- All changes routed through **Management of Change (A7)**; superseded versions retained in document control.

---

## 13. Decision-Support Statement & Open GAPs

**This PHMP is decision-support.** It structures the multidisciplinary inrush workshop and records the team's analysis; it is **not** an approved plan and does **not** substitute for the engineering judgement of the mine's competent persons or the statutory sign-off. It must be reviewed and signed by a competent person (Mine Manager + Hydrology + Geotechnical Competent Persons) before issue. It is not legal advice.

**Open `[GAP]`s to close before issue (all routed to competent persons):**
1. `[GAP-LEGAL]` — confirm jurisdiction and the exact statutory inrush duties (barrier formula, danger-zone width, advance-boring & notification duties) — *Technical Services Manager* (§2).
2. `[GAP-PLANS]` — verify/complete old-workings extents, datums, and water levels; quantify survey uncertainty — *Mine Surveyor + Hydrology CP* (§4.2).
3. `[GAP]` — worst-credible hydrostatic head H; aquifer/recharge model; piezometric trigger thresholds — *Hydrology Competent Person* (§6, §7).
4. `[GAP]` — barrier-pillar width; rock-cover/parting competence; connective-fracture-zone height; factor of safety — *Geotechnical Competent Person* (§6).
5. `[GAP]` — danger-zone width and advance/flank borehole density, spacing, length, angle, and max safe advance per cycle — *Geotechnical + Hydrology CP, per statute* (§6.4).
6. `[GAP]` — making-water and rainfall/river/reservoir alarm thresholds; dewatering design margin — *Hydrology / Dewatering* (§7, §8).
7. Confirm the risk-matrix bands against the operation's own 5×5 (§4.4).

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
