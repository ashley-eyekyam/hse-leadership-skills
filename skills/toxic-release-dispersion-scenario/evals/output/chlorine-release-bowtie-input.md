<!-- LOCKED fixture — owner-LOCKED at the SW3 19-04 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Toxic-Release Dispersion Scenario — Bowtie Consequence-Side Input

### Chlorine (CAS 7782-50-5) · Chlorination Building · Catastrophic Release

**SCENARIO FRAMING ONLY — this is NOT a modelled dispersion result.**
Assistive input for a competent-person bowtie / consequence study. No quantitative dispersion (PHAST/ALOHA) was run; no release rate, hazard distance, concentration, or lethality was computed or invented. Every un-modelled value is carried as a literal `[GAP]` for the competent modeller.

---

## 1. Document control

| Field | Entry |
|---|---|
| Title | Toxic-Release Dispersion Scenario — Bowtie Consequence-Side Input |
| Substance | Chlorine (Cl₂), CAS 7782-50-5 |
| Document reference | TRDS-CL2-CHLOR-001 `[ASSUMPTION — internal reference not supplied]` |
| Version / status | 1.0 — **Draft for competent-person review** (not yet signed off) |
| Issue date | 6 July 2026 |
| Target study | **Bowtie** (consequence side) — with **LOPA** noted as a downstream option |
| Prepared by | Process Safety Analyst (role) — decision-support tool output |
| Reviewed (SME pass) | Consequence-modelling / dispersion specialist (role) — see §12 |
| Competent-person sign-off | **Pending** — see Action A6 |
| Classification | Restricted — decision-support |
| Distribution | Consequence Modeller (role); Process Safety Facilitator / `bowtie-builder` (role); LOPA Lead / `lopa-worksheet` (role); Competent Person (role) |
| Data protection | Source facts contained no personal or health identifiers; all owners are shown as role labels. No de-identification key required. |

---

## 2. Purpose and boundary

**Purpose.** To capture the *source term and scenario* for a catastrophic chlorine release at the chlorination building as structured **input to a bowtie** — specifically to frame the **consequence (mitigative) side** — and to hand the quantitative dispersion work to the competent modelling team with every un-modelled value explicitly flagged.

**Boundary (load-bearing).** This artifact:

- **Captures** the source term from the facts supplied — it **does not compute** a release rate from first principles.
- **Does not** run quantitative dispersion modelling (no PHAST, no ALOHA) and **does not** invent any distance, concentration, footprint, or lethality.
- Provides a **qualitative consequence-axis band only** (from the shared `risk_matrix` consequence axis) — this is **explicitly not a modelled severity**.
- Hands the consequence side to **`bowtie-builder`** (grounded in `KB-STD-CCPS-BOWTIE`, CCPS/EI bowtie method, 2026) and notes **`lopa-worksheet`** (grounded in `KB-STD-IEC-61511`) as the downstream owners.

This is **decision-support only** and **precedes — it does not replace** — a competent person's review and sign-off (§13).

---

## 3. Captured facts (echo-back)

> Scenario framing only — **NOT** a quantitative dispersion result. Substance **chlorine (CAS 7782-50-5)**; inventory at risk **1 tonne (≈1000 kg)** in a **liquefied-gas drum at ambient temperature**; release mode **catastrophic (full-bore)**; release rate / hole size **`[GAP]` — for the competent modeller**; toxicity benchmark **AEGL**; geometry **release at the chlorination building, nearest public receptor a residential edge 300 m to the NE, weather held as an `[ASSUMPTION]` (SW wind ≈3 m/s, Pasquill stability D)**; receptors **on-site workers + public**; target study **bowtie** (LOPA noted). A qualitative consequence band is given; every un-modelled value is `[GAP]`-flagged; the consequence side is handed to **`bowtie-builder`** and **`lopa-worksheet`** by name. PHAST/ALOHA were not run and no distance/concentration was invented.

---

## 4. Source term — captured, NOT computed

| Element | Value | Basis / flag |
|---|---|---|
| Substance | Chlorine (Cl₂) | Supplied |
| CAS | 7782-50-5 | Supplied |
| Inventory at risk | 1 tonne (≈1000 kg) — single liquefied-gas ("ton") drum | Supplied |
| Physical state | Liquefied gas under its own vapour pressure | Supplied |
| Storage temperature | Ambient | `[ASSUMPTION]` — exact ambient value not supplied |
| Storage pressure | = chlorine saturated vapour pressure at the storage temperature | **`[GAP]`** — numeric SVP not supplied; **do not compute here** |
| Release mode | **Catastrophic (full-bore)** | Supplied |
| Release rate / mass flow | — | **`[GAP]` for the competent modeller** — not supplied; **must not be computed from first principles here, and PHAST/ALOHA must not be run to derive it** |
| Hole size / breach geometry | — | **`[GAP]`** — not supplied |
| Release duration | — | **`[GAP]`** — follows from rate + inventory; modeller to derive |
| Flash fraction / aerosol rainout | — | **`[GAP]`** — modeller to derive |

**Release-behaviour note (qualitative, for model selection — not a result).** Chlorine stored as a liquefied gas under pressure, released full-bore, is expected to give a **two-phase flashing release** with aerosol formation and rainout, producing a **cold, dense (heavier-than-air) cloud** that slumps and travels near ground level. The modeller should therefore select a **dense-gas dispersion** treatment rather than a neutral/Gaussian model. *This is a qualitative physical-behaviour statement to guide model selection; it is not a dispersion result.*

---

## 5. Toxic endpoint basis — for the modeller

**Benchmark to zone against: AEGL** (US EPA Acute Exposure Guideline Levels framework). `[ASSUMPTION — AEGL framework named per the intake; the substance-specific chlorine values are not held in the project knowledge base and must be read from the authoritative AEGL table by the modeller.]`

Zoning tiers the modeller should map (framework definitions — **not** substance concentrations):

| Tier | Framework definition (qualitative) | Typical zoning use |
|---|---|---|
| AEGL-1 | Notable discomfort / irritation; transient and reversible | Outer awareness zone |
| **AEGL-2** | Irreversible or other serious, long-lasting effects, **or impaired ability to escape** | **Escape-impairment / outer hazard contour** |
| **AEGL-3** | **Life-threatening effects or death** | **Life-threatening / inner hazard contour** |

- **`[GAP]` — numeric endpoint values.** The chlorine **AEGL-2 and AEGL-3 concentrations** and the **averaging time** (10-min / 30-min / 60-min / 4-h / 8-h) to zone against are **not held in the project KB and must not be invented** — resolve from the authoritative AEGL table. Recommend the modeller zone **both** the AEGL-3 (life-threatening) and AEGL-2 (escape-impairment) contours.
- **Do not confuse with occupational limits.** The project KB holds chlorine **ACGIH TLV-TWA 0.5 ppm (8-h)** and **TLV-STEL 1 ppm (15-min)** (*source: ACGIH TLV, 2023*). These are **chronic occupational** limits and are **explicitly NOT** the acute emergency dispersion endpoint — do not substitute them for AEGL in the zoning.

---

## 6. Scenario geometry — for the modeller

| Element | Value | Flag |
|---|---|---|
| Release point | Chlorination building | Supplied |
| Nearest public receptor | Residential edge, **300 m to the NE** | Supplied (receptor location only — **not** a hazard distance) |
| Typical wind | South-westerly, ≈3 m/s | **`[ASSUMPTION]`** — held as stated, not asserted as fact |
| Atmospheric stability | Pasquill class **D** | **`[ASSUMPTION]`** — held as stated |
| Downwind alignment | A SW wind advects the plume **toward the NE** — i.e. **toward the 300 m residential edge** (receptor is downwind under the stated typical weather) | Qualitative geometry note |
| Hazard range to AEGL-2 / AEGL-3 | — | **`[GAP]`** — modeller to compute |
| Concentration at the 300 m residential edge | — | **`[GAP]`** — modeller to compute |
| Footprint area / plume width / touchdown | — | **`[GAP]`** — modeller to compute |

**Weather-sensitivity note (for the modeller, not a result).** The stated D / 3 m/s case is one condition only. Conventionally, **low-wind / stable (e.g. F-class) conditions give the longer hazard ranges** for a dense toxic gas; the modelling team should run a **credible weather set**, not the single typical case, and confirm the worst credible receptor exposure. *No range is asserted here.*

---

## 7. Receptors

- **On-site workers** — chlorination-building operators and the wider site population.
- **Public** — nearest receptor the **residential edge 300 m NE** (downwind of the release under the stated typical weather). Public receptor presence is **confirmed**, not assumed away.
- **Environment** — not nominated in the facts supplied → `[GAP]` if the study requires an environmental receptor (e.g. watercourse, ecological site); route to the study team.

---

## 8. Qualitative consequence-axis band — NOT a modelled severity

Using the shared `risk_matrix` **consequence axis only** (default 5×5, per intake Q10):

> **Consequence band: C5 — Catastrophic** (potential for multiple fatalities / serious off-site public harm).

**Basis for the band (qualitative):** the intrinsic **acute inhalation toxicity** of chlorine, a **large (1-tonne) inventory at risk**, a **catastrophic full-bore** release mode, and a **confirmed downwind public receptor** at 300 m together place the *credible worst-case potential* at the top of the consequence axis.

**What this band is NOT.** It is **not** a modelled severity, **not** a lethality estimate, and **not** a statement that the AEGL-3 contour reaches the residential edge — that determination is a **`[GAP]`** for the modeller (§6). No likelihood axis and no risk rating are assigned here; likelihood belongs to the downstream study once the source term is quantified.

---

## 9. Consequence-side (mitigative) barrier direction — hierarchy-of-controls-ranked INPUT for `bowtie-builder`

Candidate mitigative-barrier **categories**, ranked most-effective-first, as framing input. **These are not declared effective** — under `KB-STD-CCPS-BOWTIE` a barrier is only "effective · independent · auditable" once the team supplies its performance-standard evidence (`[GAP]` until then). `bowtie-builder` owns turning these into barriers; `controls` (A7) owns the HoC ranking.

| HoC level | Candidate barrier (category) | Note |
|---|---|---|
| **Elimination / Substitution / Inherently-safer** | Reduce/eliminate the inventory at risk — smaller unit containers, on-site hypochlorite generation, liquid bleach or UV disinfection in place of gaseous chlorine | **Highest-order lever.** Sits on the *prevention* side / Management of Change, but named here so the study does not jump to lower-order controls. See Action A8. |
| **Engineering (mitigative, post-release)** | Building enclosure with extraction to a **caustic scrubber**; automatic gas **detection + emergency isolation** (excess-flow / emergency shut-off valve on the drum); **water-spray / deluge knockdown** curtain | Reduce the quantity of chlorine reaching receptors |
| **Administrative** | Emergency response plan; toxic-gas alarm and muster; **public warning / shelter-in-place / evacuation** for the residential edge; mutual-aid and authority notification | ⚠ **Lower-order — not a complete treatment on its own.** Justify why engineering knockdown/containment is not reasonably practicable, or escalate. |
| **PPE** | Escape sets / SCBA for on-site workers (last line of defence) | ⚠ **Lower-order — PPE-only is not an acceptable treatment** for a 1-tonne chlorine release; higher-order engineering + substitution must lead. |

---

## 10. Un-modelled values register — every `[GAP]` for the competent modeller

| # | Un-modelled quantity | Owner |
|---|---|---|
| G1 | Release rate / mass flow | Consequence Modeller (role) |
| G2 | Hole size / breach geometry | Consequence Modeller (role) |
| G3 | Release duration | Consequence Modeller (role) |
| G4 | Flash fraction / aerosol rainout fraction | Consequence Modeller (role) |
| G5 | Storage pressure (chlorine SVP at ambient) — numeric | Site Process Engineer (role) |
| G6 | Exact ambient / storage temperature | Site Process Engineer (role) |
| G7 | Chlorine AEGL-2 and AEGL-3 concentrations + averaging time | Consequence Modeller (role) |
| G8 | Downwind hazard range to AEGL-2 and AEGL-3 | Consequence Modeller (role) |
| G9 | Concentration at the 300 m residential edge | Consequence Modeller (role) |
| G10 | Footprint area / plume width / touchdown location | Consequence Modeller (role) |
| G11 | Toxic-load / probit (SLOT–SLOD) lethality, if the study requires it | Consequence Modeller (role) |
| G12 | Environmental receptor identification (if in scope) | Study Team (role) |

**None of G1–G12 has been estimated, interpolated, or invented in this document.**

---

## 11. Downstream ownership — handoff

- **Consequence side of the bowtie → `bowtie-builder`** (role: Process Safety Facilitator), grounded in `KB-STD-CCPS-BOWTIE`. Owns developing the mitigative barriers (effective · independent · auditable, with performance standards) and the "[Damage] due to [Event]" consequence legs. Top event for the bowtie: *loss of containment of chlorine from the chlorination-building drum.*
- **IPL credit, if a layer-of-protection view is needed → `lopa-worksheet`** (role: LOPA Lead), grounded in `KB-STD-IEC-61511`. Owns independent-protection-layer credit and any SIF/SIL determination.
- **Quantitative dispersion → Consequence Modeller (role)** using an appropriate dense-gas model — resolves the entire `[GAP]` register (§10).

This scenario-framing artifact **closes at the handoff**; it does not develop the bowtie or the LOPA itself.

---

## 12. Actions register — owned and dated

| # | Action | Owner (role) | Due |
|---|---|---|---|
| A1 | Derive the quantitative source term (release rate, hole size, mass flow, flash/rainout, duration) for the catastrophic full-bore release | Consequence Modeller (role) | 20 July 2026 |
| A2 | Resolve chlorine AEGL-2 and AEGL-3 concentrations and averaging time from the authoritative AEGL table; select the zoning tier(s) | Consequence Modeller (role) | 20 July 2026 |
| A3 | Run dense-gas dispersion over a credible weather set (including a low-wind / stable case); compute hazard ranges to AEGL-2/AEGL-3 and the concentration at the 300 m residential edge | Consequence Modeller (role) | 27 July 2026 |
| A4 | Confirm storage P/T (ambient value, drum SVP) and exact drum inventory/configuration from asset records | Site Process Engineer (role) | 13 July 2026 |
| A5 | Develop the consequence side of the bowtie (mitigative barriers, effective·independent·auditable, HoC-ranked) from this input, via `bowtie-builder` | Process Safety Facilitator / `bowtie-builder` (role) | 3 August 2026 |
| A6 | Competent-person review and sign-off of this scenario framing before it enters the bowtie/QRA | Competent Person / Process Safety Authority (role) | 13 July 2026 |
| A7 | If independent-protection-layer credit is required, run LOPA against IEC 61511 via `lopa-worksheet` | LOPA Lead / `lopa-worksheet` (role) | 10 August 2026 |
| A8 | Evaluate inherently-safer / substitution and inventory-reduction options (highest-order lever) through Management of Change | Process Safety Manager (role) | 31 August 2026 |

---

## 13. SME review & sign-off note

**SME review: ran** (single-threaded fallback; persona — *Consequence-modelling / dispersion specialist*). Confirmed:

- Source term **captured, not computed** — substance, CAS, 1-tonne inventory, liquefied-gas state, catastrophic release mode recorded from the user; release **rate held as `[GAP]`**, not derived.
- **No invented dispersion distance or concentration** — all quantitative values are `[GAP]`, routed to the modeller (§10); PHAST/ALOHA not run.
- **Weather held as an explicit `[ASSUMPTION]`** (SW ≈3 m/s, Pasquill D) — not asserted as fact.
- **Receptors and the toxic endpoint named, not optimistic** — on-site workers + public (300 m NE residential edge) listed; public receptor not assumed away; **AEGL** named as the endpoint basis for the modeller.
- **Consequence band qualitative only** — C5 Catastrophic on the `risk_matrix` consequence axis, explicitly **not** a modelled severity.
- **Downstream owners named** — consequence side handed to **`bowtie-builder`** and **`lopa-worksheet`** by name; the artifact does not close out the study.

This is **decision-support only** — scenario framing for a competent-person study, **not a modelled result**. It **precedes and does not replace** the human competent-person sign-off (Action A6) and does not certify the work as "approved by a competent person."

---

## 14. Assumptions & gaps summary

- `[ASSUMPTION]` — Storage temperature is "ambient"; exact value not supplied (A4 to confirm).
- `[ASSUMPTION]` — Weather (SW ≈3 m/s, Pasquill D) held as stated for framing; the modeller must test a credible weather set.
- `[ASSUMPTION]` — AEGL framework named per intake; chlorine-specific values not held in the project KB → modeller to read from the authoritative AEGL table.
- `[ASSUMPTION]` — Document reference is a placeholder pending an internal number.
- `[GAP]` — All quantitative source-term and dispersion values (G1–G12, §10), plus storage SVP and any environmental receptor.

---

## 15. Disclaimer

This document is **decision-support only** and must be **reviewed and approved by a competent person** before use. It is **scenario framing, not a modelled dispersion result** — no quantitative release rate, hazard distance, concentration, footprint, or lethality has been produced. It is **not legal advice** and does not discharge any COMAH / Seveso / MSIHC or other statutory duty; those obligations sit with the operator and the target-study skills. All hazard quantification remains with the competent modelling team and the competent person named above.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
