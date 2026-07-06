<!-- LOCKED fixture — owner-LOCKED at the SW4 19-05 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Ventilation, Strata-Control & Blasting Management Plan
## Underground Coal Mine — Drill-and-Blast Development Heading

**Document type:** Site-specific mine plan (ventilation · strata/ground control · blasting) — combined
**Applies to:** A single development heading (dead-end roadway) being advanced by drill-and-blast at an underground coal mine
**Issue date:** 6 July 2026
**Status:** DRAFT for competent-person review and sign-off — **decision-support only, not an approved statutory plan**
**Next scheduled review:** 5 January 2027, or on any material change (seam gassiness reclassification, geotechnical change, blast-design change, ventilation reconfiguration, or a reportable event) — whichever is sooner

---

## 0. How to read this plan (scope, assumptions, and what is deliberately left open)

This is a consultant-grade **draft framework**. It forces the site to state the actual parameters rather than accept a generic template. Where a value is a **statutory or engineered number that cannot be responsibly asserted without the site's own data, the applicable jurisdiction's coal-mining regulations, and a competent person's calculation, it is marked `[GAP]` and routed to the named role owner** — it is not invented. Filling every `[GAP]` and confirming every rating against the mine's own risk matrix is a precondition of sign-off.

**Confirmed context (from the task):**
- Underground **coal** mine (flammable-gas / coal-dust regime — a "gassy" mine environment must be assumed until the seam is formally classified).
- A **development heading** — a dead-end roadway. This is significant: a dead-end cannot be ventilated by through-flow and **requires an engineered auxiliary (forcing/exhausting) ventilation circuit**; and blasting fume accumulates at a blind face and must be positively cleared before re-entry.
- Advance method is **drill-and-blast** (hence the blasting section applies in full).

**Open items requiring resolution before sign-off — `[GAP]`:**

| # | Open item | Route to |
|---|---|---|
| G1 | **Jurisdiction / applicable coal-mine regulation not specified.** Every statutory numeric threshold below (gas action levels, minimum air quantity/velocity, exclusion-zone distances, misfire waiting times, permitted-explosive class, OELs) is jurisdiction-specific and must be set from the governing coal-mining regulations (e.g. the Mines Act/DGMS Coal Mines Regulations regime, or the equivalent national coal-mining safety regulations for the mine's country). | Mine Manager (statutory) + Ventilation Officer |
| G2 | Seam gassiness / firedamp classification (degree of gassiness), gas make/emission data | Ventilation Officer |
| G3 | Geotechnical / strata characterisation of the heading (roof, rib and floor lithology, RQD/RMR, ground stress) | Strata-Control Engineer / Geotechnical Engineer |
| G4 | Heading dimensions, drivage cycle, planned advance per round, ground water/inrush proximity | Under-Manager (Development) |
| G5 | Site risk-matrix bands (the org's 5×5 likelihood×consequence matrix) to confirm the indicative ratings in §4 | Mine Manager |

**No personal data was supplied. De-identification pass complete: no personal, health, or crew-identifying data present in the inputs; all ownership below is by statutory/functional role only.**

---

## 1. Statutory and framework basis

| Basis | What it grounds here | Note |
|---|---|---|
| **Mines Act / mining OH&S statute — ventilation adequacy duty** (`KB-REG-IN-MINES-ACT`) | Duty to maintain an adequate quantity and quality of air underground → this **ventilation plan** | The plan is a site document, **not a numbered statutory form**. Confirm the governing regulation for the mine's jurisdiction (`[GAP] G1`). |
| **Mines Act / mining OH&S statute — strata / ground-control duty** (`KB-REG-IN-MINES-ACT`) | Duty for support and roof/side stability → this **strata-control plan** | As above. |
| **Mines Act / mining OH&S statute — blasting / shotfiring duty** (`KB-REG-IN-MINES-ACT`) | Duty on explosives use, exclusion, and misfire → this **blasting plan** | As above. |
| **ICMM principal-hazard framing** (`KB-STD-ICMM-CCM` / `KB-DATA-MINING-HAZARDS`) | Ground failure, ventilation failure, fire/explosion, respirable dust, inrush treated as **principal hazards** with flagged **critical controls** | Critical controls flagged ★ in §4. |
| **ISO 45001 cl. 6.1.2 (HIRA) + hierarchy of controls** (`KB-STD-ISO45001` / `KB-SNIP-HOC`) | Every hazard risk-rated; every control ranked most-effective-first; no principal hazard left to PPE/admin alone | Applied throughout. |

> Benchmark figures (e.g. mining fatality/injury rates) are not asserted in this plan; if the site wishes to benchmark, resolve from **DGMS annual statistics** or **ICMM benchmarking** with the publishing body + year (`KB-DATA-MINING-HAZARDS`) — never a bare number.

---

## 2. Principal-hazard summary (this heading)

The development heading concentrates the coal-mining principal hazards at a single blind face:

1. **Ground / strata failure** — roof fall or rib failure at or near the freshly-cut, temporarily-supported face.
2. **Fire / explosion** — methane (firedamp) accumulation and/or suspended coal dust meeting an ignition source (blasting, electrical, frictional).
3. **Ventilation failure** — loss of auxiliary ventilation to the dead-end → irrespirable or flammable atmosphere.
4. **Toxic gas exposure** — carbon monoxide (afterdamp / heating indicator) and blasting fume (CO + nitrous fumes NO/NO₂) at the face.
5. **Blasting hazards** — flyrock, premature/uncontrolled initiation, and **misfire**.
6. **Respirable dust** — chronic pneumoconiosis / silicosis exposure (respirable coal dust and respirable crystalline silica).
7. **Inrush / inundation** — water or gas inrush if the heading approaches old/adjacent workings or an aquifer (`[GAP] G4` — confirm proximity).

---

## 3. Roles and responsibilities (functional roles only)

| Role | Accountable for |
|---|---|
| **Mine Manager (statutory)** | Overall adequacy and authorisation of this plan; resolution of `[GAP] G1`; sign-off. |
| **Ventilation Officer** | Ventilation design and air quantity/quality; gas-regime characterisation; monitoring regime; all ventilation `[GAP]` values. |
| **Strata-Control / Geotechnical Engineer** | Support design and density; convergence monitoring; the strata TARP triggers. |
| **Blasting-in-Charge / Shotfirer** | Blast design, charging, exclusion-zone enforcement, gas testing at the face, misfire management. |
| **Under-Manager / Overman / Mining Sirdar** | Shift-level supervision; pre-shift inspection; enforcement of the safe systems below. |
| **Gas-testing officer / competent gas tester** | Statutory gas tests (pre-shift, during-shift, pre-charge, pre-fire, pre-re-entry). |
| **Occupational Hygienist / Environmental Officer** | Respirable-dust monitoring strategy, SEG sampling, OEL resolution, health-surveillance interface. |

---

## 4. Risk register (indicative — confirm bands against the site matrix, `[GAP] G5`)

Likelihood (L 1–5) × Consequence (C 1–5) on the org's 5×5 matrix. Ratings below are the analyst's **indicative** judgement pending confirmation against the site's `risk_matrix` bands; ★ = critical control.

| # | Hazard event | L | C | Indicative rating | Critical controls (see body) |
|---|---|---|---|---|---|
| R1 | Roof/rib fall at supported face | 3 | 5 | **High / Very High** | ★ Primary support to design + FLOS; ★ strata monitoring/TARP; exclusion under unsupported roof |
| R2 | Methane/coal-dust ignition or explosion | 2 | 5 | **High / Very High** | ★ Auxiliary ventilation (dilution); ★ continuous CH₄ monitoring with power/machine trip; ★ stone-dusting; ignition-source control (permitted explosives, flameproof equipment) |
| R3 | Auxiliary ventilation failure at dead-end | 3 | 5 | **High / Very High** | ★ Duplicated/certified auxiliary fans with auto-changeover; ★ fan-stoppage alarm + withdrawal rule |
| R4 | CO / nitrous-fume / O₂-deficiency exposure | 3 | 4 | **High** | ★ Positive fume clearance before re-entry; ★ multi-gas monitoring; test-before-entry rule |
| R5 | Blasting — flyrock / premature initiation | 2 | 5 | **High** | ★ Enforced exclusion zone + sentries; firing from a safe place; competent shotfirer |
| R6 | Blasting — misfire | 3 | 4 | **High** | ★ Misfire procedure + waiting period; no unauthorised return |
| R7 | Respirable dust — pneumoconiosis/silicosis | 4 | 4 | **High** (chronic) | ★ Dust suppression + adequate ventilation (higher-order); monitoring; RPE last |
| R8 | Inrush / inundation | `[GAP] G4` | 5 | Confirm | Standoff/barrier, hydrogeological survey, probe drilling — resolve if applicable |

---

## 5. VENTILATION MANAGEMENT

**Duty grounded in:** ventilation-adequacy duty, `KB-REG-IN-MINES-ACT`. **Owner: Ventilation Officer.**

A development heading is a **dead-end**; it cannot be ventilated by the mine's through-circuit. It must be served by a dedicated **auxiliary ventilation circuit** (forcing, exhausting, or overlap duct-and-fan system) drawing fresh intake air, discharging to return, with **no recirculation**.

### 5.1 Air quantity and velocity requirements

| Parameter | Requirement | Value |
|---|---|---|
| Minimum air **quantity** delivered to the face (m³/s) | Sufficient to dilute the worst-credible gas make below the statutory action level, dilute/clear blasting fume, remove dust, and provide for personnel and diesel (if any) | **`[GAP] G1/G2`** — Ventilation Officer to calculate from seam gas make + statutory minimum; do not assume |
| Minimum / maximum air **velocity** in the heading (m/s) | Minimum to sweep the face and prevent layering/accumulation of methane at the roof; maximum to avoid raising coal dust into suspension | **`[GAP] G1`** — set from the governing coal-mine regulation and dust considerations |
| Duct end **distance from face** (max) | Auxiliary duct outlet kept within a maximum distance of the advancing face so the face is positively swept | **`[GAP] G1`** — per regulation and design |
| Air quantity **per person / per unit of equipment** | Statutory per-capita and per-machine minimums | **`[GAP] G1`** |

> These are the defining parameters of the ventilation plan. **Refusing to state an ungrounded number is deliberate** — an invented air quantity or velocity would be indefensible. Each must be calculated by the Ventilation Officer against (a) the seam's measured gas make and (b) the applicable coal-mine regulation, before sign-off.

### 5.2 Gas management (methane / CO / CO₂ / O₂ / blasting fume)

**Physical basis (chemistry, not a regulatory limit):** methane is flammable in air over an approximate range of **~5%–15% by volume** (most violent near ~9.5%). This is why methane must be kept *well below* the lower flammable limit by dilution — the **statutory action thresholds sit far below 5%** and are jurisdiction-set.

| Gas | Hazard | Statutory / action threshold | Control basis |
|---|---|---|---|
| **Methane (CH₄, firedamp)** | Flammable/explosive; layers at roof | Action levels at which work stops / power is withdrawn / persons are withdrawn — **`[GAP] G1`** (e.g. graduated trip and withdrawal levels in the coal-mine regulation) | Dilution by auxiliary ventilation ★; continuous monitoring with automatic machine/power cut-out ★ |
| **Carbon monoxide (CO)** | Toxic; also a **heating/spontaneous-combustion indicator** and afterdamp component | Occupational exposure limit and heating-alarm level — **`[GAP] G1`** | Ventilation dilution; CO monitoring/trending for early heating detection |
| **Carbon dioxide (CO₂, blackdamp/stythe)** | Asphyxiant; displaces O₂ | Max concentration — **`[GAP] G1`** | Ventilation |
| **Oxygen (O₂)** | Deficiency | Normal atmosphere ≈ 20.9% O₂; statutory minimum — **`[GAP] G1`** | Ventilation; flame-lamp cross-check |
| **Nitrous fumes (NO/NO₂) + CO from blasting** | Acutely toxic post-blast fume | Re-entry limits — **`[GAP] G1`** | Positive fume clearance before re-entry (§7.3) ★ |

**Coal-dust explosion control (distinct from dust health, §8):** maintain **stone-dusting / incombustible-content** of roadway dust to the required incombustible percentage so that any coal-dust cloud cannot propagate an explosion. Incombustible-content percentage and sampling frequency — **`[GAP] G1`** — Ventilation Officer / competent person. This is a **critical control ★** for R2.

### 5.3 Monitoring regime

| Layer | Instrument | What / where | Frequency |
|---|---|---|---|
| **Fixed / telemetric** | Real-time CH₄ (and CO) sensors on the environmental monitoring system | At the face, at the machine, in the return of the heading; **CH₄ sensor interlocked to trip electrical power / cut out the machine** at the action level ★ | Continuous, alarmed to surface control |
| **Portable** | Calibrated multi-gas detector (CH₄, CO, O₂, CO₂; H₂S if credible) | Carried by every statutory official, gas tester and shotfirer | Pre-shift inspection; during-shift at set intervals; **before charging, before firing, before re-entry** |
| **Cross-check** | Flame safety lamp | Independent O₂-deficiency and CH₄ cap check | With each statutory inspection |
| **Personal** | Personal CH₄ / CO monitor | On persons at the face | Continuous while at the face |

- **Calibration and bump-testing** of all detectors on a documented schedule — frequency **`[GAP] G1`** (per manufacturer + regulation).
- **Withdrawal rule:** on a fixed-sensor gas trip, a fan-stoppage alarm, or a portable-detector action-level reading, **persons are withdrawn to fresh air and power is isolated** until the Ventilation Officer authorises return.

---

## 6. STRATA / GROUND-CONTROL MANAGEMENT

**Duty grounded in:** strata/ground-control duty, `KB-REG-IN-MINES-ACT`. **Owner: Strata-Control / Geotechnical Engineer.**

> The support regime **must be derived from the heading's actual geotechnical characterisation** (`[GAP] G3`) — roof/rib/floor lithology, RQD/RMR or equivalent rock-mass rating, bedding, ground stress, and observed ground behaviour. Support type, length and density stated as fixed numbers without that basis would be a generic template and are therefore left `[GAP]`.

### 6.1 Support type and density

| Element | Requirement | Value |
|---|---|---|
| **Primary roof support** | Systematic roof bolting (full-column resin/mechanical anchor, or as designed) with straps/mesh; support pattern and **bolt length, bolt density (bolts/m² or row spacing × in-row spacing), and anchorage/tension** designed to the rock-mass rating | **`[GAP] G3`** — Strata-Control Engineer to design; confirm by pull-testing |
| **Rib (side) support** | Rib bolts and/or mesh where rib condition/height requires | Pattern **`[GAP] G3`** |
| **Face / temporary support (FLOS)** | First Line Of Support at the newly-exposed face before persons work under it; maximum **unsupported span / no-go under unsupported roof** rule | Max exposed span **`[GAP] G3`** — but the **exclusion-under-unsupported-roof rule applies unconditionally ★** |
| **Support cycle** | Cut/muck → support → advance; no advance beyond the supported line | Discipline enforced by Overman/Sirdar |
| **Support verification** | Anchorage/installed-quality checks (pull-test sample rate), install-torque | Sample rate **`[GAP] G3`** |

### 6.2 Convergence and geotechnical monitoring

- **Tell-tales / dual-height roof tell-tales** installed at set intervals along the heading to indicate roof-strata separation (green/amber/red visual bands).
- **Roof-to-floor convergence stations** and, where warranted, **extensometers**, read on a documented cycle.
- **Routine geotechnical mapping** of the exposed face/ribs each advance by the Overman/Sirdar, escalated to the Strata-Control Engineer on any adverse change.
- Reading frequencies and installation intervals — **`[GAP] G3`** — set by the Strata-Control Engineer.

### 6.3 Strata TARP (Trigger Action Response Plan)

Trigger **movement/convergence values are `[GAP] G3`** — the Strata-Control Engineer sets them from ground behaviour. The **response structure** is fixed:

| Trigger level | Indicative trigger (`[GAP]` values) | Response | Actioned by |
|---|---|---|---|
| **GREEN — normal** | Tell-tale within green band; convergence below Level 1 | Routine monitoring; record | Overman / Mining Sirdar |
| **AMBER — elevated** | Movement exceeds Level 1 / enters amber band | Increase monitoring frequency; install secondary/remedial support; notify Strata-Control Engineer | Overman → Strata-Control Engineer |
| **RED — action** | Movement exceeds Level 2 / enters red band, or visible deterioration | **Withdraw persons, barricade the area, no entry** until re-supported and cleared by the Strata-Control Engineer | Under-Manager / Strata-Control Engineer |

---

## 7. BLASTING / SHOTFIRING MANAGEMENT

**Duty grounded in:** blasting/shotfiring duty, `KB-REG-IN-MINES-ACT`. **Owner: Blasting-in-Charge / Shotfirer.**

### 7.1 Explosives and charge design (gassy-coal cross-discipline note)

- Because this is a **coal seam / potentially gassy environment**, only **permitted (flameproof) explosives and the permitted detonator class approved for gassy coal mines** may be used — the specific permitted class (e.g. the graded permitted-explosive series for the seam's gassiness) is **`[GAP] G1/G2`**, resolved by the Ventilation Officer + Blasting-in-Charge from the seam classification and regulation. **Non-permitted explosives must not be used at the coal face.**
- Shot-hole pattern (cut type — e.g. burn/wedge cut), **charge per hole, total charge per round, stemming length, and delay-detonator sequence** — designed by the Blasting-in-Charge to the heading dimensions and confined to the drill-and-blast advance — **`[GAP] G4`** for the site values.
- **Maximum charge / hole and per-round limits** governed by the coal-mine regulation — **`[GAP] G1`**.

### 7.2 Exclusion (danger) zone

- A defined **blast-exclusion zone** must be established and physically enforced for every round: all persons withdrawn beyond the zone, **sentries posted** and **barricades/warning signs** placed on every approach, roadways and adjacent headings guarded, and the shot **fired only from a designated safe place** with a positive check that all persons are accounted for.
- **Exclusion-zone radius / extent, sentry positions, and audible warning signals** — **`[GAP] G1`** — set from the regulation and the charge/geometry by the Blasting-in-Charge; do not assume a distance.
- **Mandatory gas test at the face immediately before charging and again immediately before firing.** If methane at the face or in the general body reaches the statutory no-fire threshold (**`[GAP] G1`**), **firing is prohibited** until ventilation reduces it below the limit. ★

### 7.3 Re-entry and gas/fume clearance

Blasting at a blind face produces **CO and nitrous fumes (NO/NO₂)** plus dust. Re-entry is governed by **positive clearance, not the clock alone**:

1. After firing, **no person re-enters** the heading until the auxiliary ventilation has run and **cleared the fume** from the face.
2. A **competent gas tester advances under ventilation and tests the atmosphere** (CO, NO₂, CH₄, O₂) with a calibrated detector; re-entry to the working face is authorised **only when readings are below the re-entry limits (`[GAP] G1`)**.
3. A **minimum re-entry / smoke-clearance time** may also be stipulated by regulation (**`[GAP] G1`**) — but it is a floor, **not** a substitute for the gas test. The controlling rule is **test-before-entry ★**.
4. Re-entry authorised by the Under-Manager/Overman on the gas tester's confirmation; recorded.

> **Cross-discipline dependency (flagged for the SME lens):** re-entry timing is a function of the §5 auxiliary-ventilation capacity. If ventilation quantity is reduced or the fan is down, re-entry is **prohibited** regardless of elapsed time.

### 7.4 Misfire procedure

A **misfire** (a charge that fails to detonate, wholly or partly) is among the highest-consequence blasting events. The procedure is mandatory:

1. **Do not approach.** After a suspected misfire, **no person returns to the face** until a **statutory waiting period** has elapsed (period **`[GAP] G1`** — set by regulation; longer for electric vs. shock-tube/detonating systems as prescribed).
2. Only the **Blasting-in-Charge / Shotfirer** (with the minimum necessary persons) approaches to investigate, under ventilation and after a gas test.
3. **Search for and identify** the misfired hole(s); **cut off and make safe** the circuit/lead-in.
4. **Deal with the misfire per the prescribed method only** — e.g. charging and firing a fresh relieving hole at the regulation-prescribed minimum distance and parallel to the misfired hole, or washing/blowing out as permitted. **Never redrill into, or extract stemming from, a misfired hole. Never pass over or abandon a misfire without making it safe.**
5. **Account for all explosives.** No shift change or return to normal work until the misfire is resolved and recorded; **hand over in writing** to the next Blasting-in-Charge if unresolved at shift end.
6. Record the misfire and, where the event meets the reportability trigger, treat as a **reportable dangerous occurrence** (notification duty, `KB-REG-IN-MINES-ACT`; confirm threshold under `[GAP] G1`).

---

## 8. RESPIRABLE DUST — HIERARCHY OF CONTROLS (higher-order first)

**Owner: Occupational Hygienist / Environmental Officer, with the Ventilation Officer.** Applies `KB-SNIP-HOC`.

Respirable **coal dust** and **respirable crystalline silica** cause irreversible chronic disease (coal workers' pneumoconiosis, silicosis). **This hazard must be controlled by suppression, ventilation and design — higher-order controls — not by dust masks alone.** A respirator is the *last* line, never the treatment.

| Rank | Control | Applied here |
|---|---|---|
| **1. Elimination / substitution** | Reduce dust generation at source | Water-infusion / pre-wetting of the seam ahead of the face where practicable; optimise blast design and drilling to reduce fines; consider lower-dust drivage where feasible (design decision — Mine Manager + Ventilation Officer) |
| **2. Engineering ★ (primary)** | Suppress and capture dust; dilute and carry it away | **Wet drilling** (water-fed drills — no dry drilling into coal/silica); **water sprays/misting** at mucking, loading and transfer points; **wetting/consolidation of blasted muck** before mucking; **adequate auxiliary ventilation (§5) to dilute and remove airborne dust**; dust scrubber/filtration on the drivage equipment if fitted |
| **3. Administrative** | Reduce exposure duration and verify | **Respirable-dust monitoring** by Similar-Exposure Group (personal gravimetric sampling), with silica analysis; exposure trending against the OEL; job rotation to limit time at highest-exposure positions; competence/awareness; interface with statutory **health surveillance** (periodic medical/chest screening) |
| **4. PPE (last line)** | Protect the individual only after 1–3 | Correctly **fit-tested respiratory protective equipment** of adequate assigned protection factor, as a supplement to — never a substitute for — the controls above |

> **`[GAP] G1`** — the respirable coal-dust and respirable crystalline silica **occupational exposure limits (OELs)** are jurisdiction-specific and are **not asserted here**; the Occupational Hygienist resolves them from the governing regulation and sets the sampling strategy against them.
>
> **Hierarchy flag (`KB-SNIP-HOC`):** any proposal to control this dust exposure by **RPE alone** is a **lower-order-only treatment and must be escalated / justified** — it is not acceptable while suppression and ventilation are reasonably practicable, which for a drill-and-blast coal heading they are.

---

## 9. Cross-discipline interactions (verified against the SME lens)

- **Ventilation ↔ blasting:** re-entry after firing is gated by the §5 ventilation clearing the fume (§7.3); a reduced or failed fan **prohibits re-entry**. Firing is prohibited above the face methane no-fire threshold (§7.2).
- **Gas regime ↔ explosives:** the permitted-explosive/detonator class is a function of seam gassiness (§7.1) — resolve the classification (`[GAP] G2`) before the blast design is finalised.
- **Blasting ↔ strata:** each blast round exposes fresh, unsupported roof/rib; **FLOS and the no-entry-under-unsupported-roof rule (§6.1) apply before anyone works at the new face.**
- **Dust ↔ explosion:** respirable-dust **health** control (§8) is separate from **coal-dust explosion** control (stone-dusting, §5.2) — both are required; neither substitutes for the other.

---

## 10. SMART follow-up actions (owner + due date)

| # | Action | Owner (role) | Due |
|---|---|---|---|
| A1 | Resolve `[GAP] G1`: confirm the mine's jurisdiction and the governing coal-mine regulation; populate all statutory numeric thresholds in §§5–8 | Mine Manager (statutory) | 20 July 2026 |
| A2 | Characterise the seam gas make and confirm the gassiness classification; **calculate the minimum face air quantity and velocity** and the auxiliary-fan duty | Ventilation Officer | 27 July 2026 |
| A3 | Complete the geotechnical characterisation of the heading and **issue the support design** (type, length, density) with pull-test acceptance criteria | Strata-Control / Geotechnical Engineer | 3 August 2026 |
| A4 | Set the **strata TARP trigger values** (amber/red) and install the tell-tale / convergence monitoring array | Strata-Control Engineer | 3 August 2026 |
| A5 | Finalise the **blast design** (permitted-explosive class, charge/round, delays, stemming) and the **exclusion-zone extent + sentry plan** | Blasting-in-Charge / Shotfirer | 27 July 2026 |
| A6 | Issue the written **re-entry gas-clearance procedure** and the **misfire procedure** with the confirmed statutory waiting period; brief all shotfirers | Blasting-in-Charge / Shotfirer | 27 July 2026 |
| A7 | Establish the **respirable-dust monitoring strategy** (SEG gravimetric + silica), resolve the OELs, and confirm the wet-drilling/spray suppression standard | Occupational Hygienist / Environmental Officer | 10 August 2026 |
| A8 | Commission the **fixed CH₄/CO telemetry with power/machine trip** and the fan-stoppage alarm; set the detector calibration/bump-test schedule | Ventilation Officer | 27 July 2026 |
| A9 | Confirm **inrush proximity** (`[GAP] G4`) and, if credible, add the probe-drilling/standoff control before advance | Under-Manager (Development) | 20 July 2026 |
| A10 | Reconcile every indicative risk rating in §4 against the site **risk-matrix bands** and re-rate | Mine Manager | 3 August 2026 |

---

## 11. Review, sign-off and disclaimer

**Review cycle:** formal review by **5 January 2027**, and immediate re-validation on any material change (gassiness reclassification, geotechnical change, blast-design change, ventilation reconfiguration, or a reportable event).

**Sign-off (to be completed on the controlled copy):**

| Discipline | Reviewing competent person (role) | Signature | Date |
|---|---|---|---|
| Ventilation | Ventilation Officer | ________ | ____________ |
| Strata / ground control | Strata-Control / Geotechnical Engineer | ________ | ____________ |
| Blasting | Blasting-in-Charge / Shotfirer | ________ | ____________ |
| Overall authorisation | Mine Manager (statutory) | ________ | ____________ |

> **Decision-support disclaimer.** This document is **decision-support only**. It is a structured draft that a **competent person must review, complete (every `[GAP]`), and sign off** before it is used to authorise work. It does not constitute legal advice, an approved statutory plan, or a certification that any control is adequate. All statutory numeric thresholds are jurisdiction-specific and must be set from the governing coal-mining regulation by the named role owner. Nothing here has been "approved by a competent person" — that approval is the human sign-off above.

---

*SME review (model QA, decision-support): ventilation/strata-control + shotfiring/blasting lenses applied — district-level air quantity and gas regime present (statutory values routed to the Ventilation Officer, not invented); support regime tied to geotechnical basis with a TARP; exclusion zone and a complete misfire + re-entry gas-clearance procedure present; permitted-explosive/gassy-seam and fume-vs-ventilation interactions addressed; respirable dust ranked engineering-before-RPE with an explicit lower-order-only flag. No de-identification leak. FLAGs are non-blocking and recorded above as `[GAP]`/actions.*

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
