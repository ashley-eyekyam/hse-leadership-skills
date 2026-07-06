<!-- LOCKED fixture — owner-LOCKED at the SW3 19-04 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Dust Hazard Analysis (DHA) & Basis of Safety
## Maize-Starch Handling & Milling Line — Food-Processing Site

**Consultant deliverable — decision-support artifact for competent-person review**

---

### Document control

| Field | Detail |
|---|---|
| Document title | Dust Hazard Analysis (DHA) & Explicit Basis of Safety — Maize-Starch Handling & Milling Line |
| Document reference | DHA-MAIZE-001 |
| Version / status | v0.1 — **DRAFT for competent-person review** (not for implementation until signed off) |
| Prepared by | HSE Consultant (role) |
| Prepared for | Site HSE Manager (role) / Plant Operations Manager (role) |
| Date of issue | 6 July 2026 |
| Next review | On receipt of the [GAP] test data (target by 3 August 2026) and on completion of the formal DHA workshop |
| Site / installation identifier | [GAP] — named site/legal entity and full address not supplied; must be recorded before issue |
| Process scope | Maize-starch handling and milling line: hammer mill → pneumatic conveying → cyclone → day silo → bagging station |
| Hazard scope | Combustible dust (deflagration / explosion). Reactive-chemistry pathways screened (see §7). |
| Jurisdiction / framework | United States — NFPA 652 / NFPA 660 (Fundamentals of Combustible Dust / consolidated combustible-dusts standard). Protection standards: NFPA 68 (deflagration venting), NFPA 69 (explosion prevention / isolation). Electrical area classification: NFPA 70 (NEC). ATEX zone scheme quoted for cross-reference only. |
| Confidentiality / data protection | No personal data processed; all duty-holders represented as role labels. |
| SME review status | SME review ran — persona: Combustible-dust / DSEAR–ATEX & reactive-chemistry specialist. This is **decision-support only**; it **precedes and does not replace** the human competent-person sign-off, and does not certify the line as "approved by a competent person." |

> **Safety & scope disclaimer.** This document is decision-support. It frames the DHA and basis-of-safety nodes for a competent-person study; it does **not** constitute an NFPA-compliant DHA of record, an electrical area classification of record, or explosion-protection engineering design. Explosion venting, suppression, isolation and inerting must be designed and certified by a competent explosion-protection engineer against the licensed NFPA standards and validated test data. It is not legal advice.

---

### 1. Executive summary & the load-bearing conclusion

A Dust Hazard Analysis has been framed across the five named process steps of a maize-starch milling and handling line. Maize (corn) starch is a **combustible organic dust**, and held laboratory data confirm the dust is explosible:

- **Kst = 180 bar·m/s → dust explosion class St-1** (Chilworth test report, 2024). The St-1 band spans >0 to 200 bar·m/s under the standard St-class definition (ISO 6184 / VDI 2263). **St-1 is not "safe"** — St-1 dusts routinely cause fatal, building-destroying explosions; the class communicates rate of pressure rise, not acceptability.
- **Pmax = 8.5 bar** (Chilworth, 2024) — an unprotected enclosure not designed to contain ~8.5 bar (≈ 9.5 bar absolute) will rupture.
- **MIE = 30 mJ** (Chilworth, 2024) — a moderate ignition sensitivity: ignitable by electrostatic discharge from isolated (ungrounded) conductors, by mechanical friction/impact sparks, and by hot surfaces/electrical arcs.

**Basis of safety (the load-bearing conclusion).** An explosible dust cloud is present **continuously or for long periods inside every item of process equipment on this line** (that is the process). Ignition-source control alone is therefore **not an adequate sole basis of safety** for St-1 dust in enclosed equipment (NFPA does not accept "no ignition source" as the sole basis where an explosible atmosphere is continuously present). The declared basis of safety is a **combined prevention-plus-protection basis, hierarchy-of-controls ranked**:

1. **Prevention (higher order):** reduce dust generation / inherently-safer handling, plus rigorous **ignition-source control** (verified bonding & earthing, tramp-metal removal, hot-surface limits, hot-work control).
2. **Protection (mitigation, because prevention cannot be the sole basis):** **deflagration venting (NFPA 68) and/or suppression (NFPA 69) on each vessel, PLUS deflagration isolation (NFPA 69) on every interconnection** to break the connected-vessel path.
3. **Inerting (avoid-the-atmosphere basis) is NOT yet available** — it requires the **Limiting Oxygen Concentration (LOC)**, which is **[GAP]** (untested). Inerting cannot be adopted or designed until LOC is measured.

**Housekeeping and PPE are supporting layers only — they are explicitly NOT the basis of safety.** The existing housekeeping regime reduces secondary-explosion fuel but does not control the primary event; the existing bonding/earthing is one necessary prevention layer, not a complete basis of safety.

**Critical gap.** Four explosibility parameters are **not held and have not been invented**: **MIT [GAP]**, **LOC [GAP]**, **particle-size distribution [GAP]**, **moisture [GAP]**. These are routed to testing (Action A1). Without MIT, hot-surface temperature limits cannot be set; without LOC, inerting cannot be designed; without PSD and moisture, the held Kst/Pmax/MIE cannot be confirmed representative of the actual process dust (especially the fines).

**Overall residual risk before the recommended protection is installed is assessed CRITICAL/HIGH at every node** (see §6). Interim risk-reduction and a management-of-change decision on occupancy near unprotected vessels are required immediately (Action A8).

---

### 2. Materials inventory (DHA element 1)

| Material | Combustible-dust status | Basis |
|---|---|---|
| Maize (corn) starch | **Combustible / explosible dust — confirmed** | Held lab data: Kst 180 bar·m/s, Pmax 8.5 bar, MIE 30 mJ (Chilworth, 2024) |

**Held characterisation data (with source + year):**

| Parameter | Value | Source | Drives |
|---|---|---|---|
| Kst (deflagration index) | 180 bar·m/s → **St-1** | Chilworth test report, 2024 | Vent area / suppression sizing; rate of pressure rise |
| Pmax (max explosion pressure) | 8.5 bar | Chilworth test report, 2024 | Containment / vent / suppression design pressure |
| MIE (min ignition energy) | 30 mJ | Chilworth test report, 2024 | Electrostatic & mechanical ignition-source control |

**Data NOT held — recorded as literal [GAP], NOT invented, routed to testing (Action A1):**

| Parameter | Status | Consequence of the gap |
|---|---|---|
| MIT (min ignition temperature, dust cloud) | **[GAP]** | Cannot set maximum permitted hot-surface temperature for equipment in the dust; cannot complete ignition-by-hot-surface assessment. |
| MIT-layer / LIT (layer ignition temperature) | **[GAP]** | Cannot set surface-temperature limits for dust *layers* (self-heating on hot surfaces). |
| LOC (limiting oxygen concentration) | **[GAP]** | **Inerting cannot be adopted or designed** as a basis of safety. |
| Particle-size distribution (PSD) | **[GAP]** | Held Kst/Pmax/MIE may not represent the finest fraction (cyclone/filter fines are typically more explosible and more ignition-sensitive); worst-case may be more severe than tested. |
| Moisture content | **[GAP]** | Moisture strongly influences explosibility and MIE; the tested-sample moisture must match the process dust for the held data to be valid. |

> **[ASSUMPTION]** The Chilworth 2024 test data are assumed to have been obtained on a representative maize-starch sample using standard apparatus (20-L sphere for Kst/Pmax; MIKE-type apparatus for MIE). The test-sample PSD, moisture, and whether MIE was measured with or without added inductance are **not stated** and should be confirmed with the laboratory, because they determine whether the held values bound the actual process dust and how the MIE informs electrostatic control.

---

### 3. Process / equipment review (DHA element 2)

Dust is generated, suspended, conveyed, separated, stored and released across the line. An explosible atmosphere is credibly present **inside** each item during normal operation.

| # | Process step / equipment | Dust state | Explosible atmosphere present? | Notes |
|---|---|---|---|---|
| N1 | **Hammer mill** | Size reduction — high fines generation, suspended cloud | **Yes, continuous during operation** | Highest ignition-source density on the line (mechanical impact, friction, tramp metal). |
| N2 | **Pneumatic conveying line** | Dust in dilute/dense-phase suspension — by design | **Yes, continuous during operation** | The interconnection that carries flame/pressure between vessels → **connected-vessel path** (§8). |
| N3 | **Cyclone** | Separation of conveyed fines; suspended + settling | **Yes, continuous during operation** | Concentrates fines (more explosible / ignition-sensitive per [GAP] PSD). |
| N4 | **Day silo** | Bulk storage; headspace cloud during pneumatic fill | **Yes, during filling; layers at rest** | Large volume → large potential energy; self-heating/smouldering pathway (§7). |
| N5 | **Bagging station** | Open/semi-open handling; release to workroom | **Yes, at the fill point** | **OCCUPIED by operators**; electrostatic ignition from bags/liners; a prime secondary-explosion initiation point via workroom layers. |
| N6 | **Dust collector / bag filter** | *Not listed in scope* | Likely, if present | **[GAP] / [ASSUMPTION]:** a pneumatic conveying + cyclone line normally discharges to a bag/cartridge dust collector, which is typically the **single highest-risk node** (large fines cloud, large volume). Its presence/absence must be confirmed and, if present, added to the DHA as node N6. **Not assumed present in the risk table below.** |

**Ignition-source enumeration (DHA element 3 input; SME-required).** Against the credible scenarios, the following ignition sources are enumerated for the workshop to assess node-by-node:

| Ignition source | Where credible | Status vs held data |
|---|---|---|
| **Electrostatic** (isolated conductors, non-conductive plant, operator/bag charging) | All nodes; acute at N2, N5 | MIE 30 mJ → credible; bonding/earthing in place but **verification [GAP]** (Action A6/A10). |
| **Mechanical friction / impact sparks; tramp metal** | N1 (mill) especially; N3 | Credible; no magnetic separation / metal detection confirmed upstream of mill. |
| **Hot surfaces** (bearings, motors, over-heated components) | N1, N2, N3, N4 | **Cannot be assessed — MIT [GAP]** (surface-temperature limit undefined). |
| **Self-heating / smouldering nest** | N4 (day silo — resident stock) | Credible for stored starch; self-heating/DSC data **[GAP]** (§7). |
| **Hot work** (maintenance cutting/welding) | All nodes | Administrative control (permit) required; see Action A6. |
| **Electrical** (non-rated equipment in a classified area) | All classified locations | Requires electrical area classification + equipment conformity (Action A5). |

---

### 4. Basis of safety — explicit, justified, HoC-ranked (DHA element 4)

The basis of safety is stated **per node** and ranked through the hierarchy of controls. **Elimination/substitution/inherently-safer first; engineering (protection) next; administrative and PPE last and never as the basis of safety.**

**Line-wide prevention layer (necessary, not sufficient):**

- **Reduce dust generation / inherently-safer handling** *(Elimination/Substitution)* — minimise free-fall, transfer velocities and leakage; enclose transfer points; the least dust generated is the most effective control. *(Justify at design/MOC stage.)*
- **Ignition-source control** *(Engineering + Administrative)* — verified bonding & earthing to specification (MIE 30 mJ makes this load-bearing); tramp-metal removal (magnet/metal detector) upstream of the mill; hot-work permit system; hot-surface / bearing temperature monitoring — **hot-surface limit cannot be numerically set until MIT is tested [GAP]**.

**Protection layer (the mitigation basis of safety, because an explosible atmosphere is continuously present):**

| Node | Declared basis of safety (ranked) | Justification |
|---|---|---|
| N1 Hammer mill | **Ignition-source control (prevention) + explosion protection: suppression or venting + isolation (mitigation)** | Highest ignition likelihood + continuous cloud → prevention alone insufficient; mill often best protected by suppression (NFPA 69) where safe venting is impractical. |
| N2 Pneumatic conveying | **Deflagration isolation (NFPA 69) — chemical/mechanical — to prevent flame/pressure transmission** | The conveying line is the flame path between vessels; **isolation is the load-bearing control** to break the connected-vessel path (§8). |
| N3 Cyclone | **Explosion venting (NFPA 68) or suppression (NFPA 69) + isolation** | Continuous fines cloud; vent to a safe location or suppress; isolate inlet/outlet. |
| N4 Day silo | **Explosion venting (NFPA 68) to a safe outdoor location + isolation; self-heating monitoring** | Large volume; venting usually feasible on a silo if a safe discharge path exists; plus thermal monitoring for smouldering (§7). |
| N5 Bagging station | **Inherently-safer + engineering FIRST: enclosure/LEV of the fill point, conductive & bonded containers, then protection** — occupancy-based controls | **Occupied node** — worker protection dominates; venting/suppression of an occupied open station is constrained, so **eliminate the release and control static first**; consider relocating/enclosing. |
| Line-wide (future) | **Inerting (avoid-the-atmosphere) — DEFERRED** | Requires **LOC [GAP]**; cannot be adopted or designed until measured. If LOC testing shows inerting is viable, it may become the higher-order basis for enclosed nodes (N1–N4), potentially displacing some protection hardware. |

> **Lower-order-control flag.** The existing safeguards as they stand — **bonding/earthing (engineering, one layer) + housekeeping (administrative)** — do **not** constitute a complete basis of safety for St-1 dust in continuously-explosible equipment. They must be **supplemented by the engineering protection above**; housekeeping and PPE are retained as supporting layers, never as the basis of safety. This is recorded so it cannot be read as an adequate treatment.

---

### 5. Area classification — justified, never defaulted (DHA element; ATEX/NEC)

**Justification basis:** classification is derived from **release grade** and **ventilation**, not defaulted.

- **Inside process equipment (N1–N5 interiors, and N6 if present):** an explosible dust cloud is present **continuously or for long periods during normal operation** (the cloud *is* the process → a **continuous / primary grade of release** inside the equipment). This justifies the **most onerous classification for equipment interiors**. Derived classification: **NEC (NFPA 70) Class II, Division 1** — equivalently **ATEX Zone 20** (continuous). Equipment must be rated **EPL Da / category 1D** (or the NEC Division-1 equivalent). *This interior classification is defensible from the process description alone.*

- **Immediate vicinity of open/leaking release points (notably N5 bagging fill; any leaking flanges/transfer points):** a **secondary grade of release** in normal operation is credible → provisionally **Class II Division 2 / ATEX Zone 21 or 22**. **However, the release frequency and the local ventilation rate are [GAP]** — so the *extent* and the Division 1-vs-2 (Zone 21-vs-22) call **cannot be finalised** and is **not defaulted**. Routed to Action A5.

- **General workroom / building volume:** classification depends on **measured dust-layer depth and housekeeping effectiveness**, which are **[GAP]** (Action A7 measures them). If layers are held below the standard threshold, areas may be unclassified; this **cannot be assumed** without the layer data. **Not defaulted.**

| Location | Derived class/zone | EPL / equipment category | Confidence |
|---|---|---|---|
| Equipment interiors N1–N5 (+N6 if present) | Class II Div 1 / **Zone 20** | 1D / **EPL Da** | Derived & defensible from process |
| Near-field of open release points (N5 etc.) | Class II Div 2 / **Zone 21–22** (provisional) | 2D–3D / EPL Db–Dc | **[GAP]** — needs release grade + ventilation |
| General workroom | To be determined | To be determined | **[GAP]** — needs layer-depth data |

> **[GAP] → Action A5.** A formal electrical area classification of record must be produced by a competent electrical engineer to the current NEC edition — **NFPA 70 Article 500/502** (Class II Division system) or **Article 506** (Zone 20/21/22 system) — and every electrical/mechanical item within a classified location verified as conforming (dust-ignition-protected, correct T-code once **MIT [GAP]** is resolved). The ATEX zones above are provided for cross-reference; the US installation is governed by the NEC.

---

### 6. Consequence banding & risk register (DHA element; `risk_matrix`)

**Scoring scheme (default 5×5, `risk_matrix` engine — Q13 default).** Severity: Negligible 1 · Minor 2 · Moderate 3 · Major 4 · Catastrophic 5. Likelihood: Rare 1 · Unlikely 2 · Possible 3 · Likely 4 · Almost Certain 5. **Score = L × S.** Bands: **Low 1–4 · Medium 5–9 · High 10–15 · Critical 16–25.**

Severity is banded **Catastrophic (5)** across the line because an St-1 deflagration at Pmax ~8.5 bar in unprotected connected equipment credibly causes vessel rupture, flame, operator fatality and — via the connected-vessel and secondary-explosion paths — potential multiple fatalities and building loss. Likelihood is judged on ignition credibility given only bonding/earthing + housekeeping and **no explosion protection currently fitted**.

| Node | Primary credible scenario | L | S | Score | **Band (pre-protection)** | Target residual¹ |
|---|---|---|---|---|---|---|
| N1 Hammer mill | Impact/friction/tramp-metal spark ignites continuous cloud → primary explosion, propagates | 4 | 5 | **20** | **Critical** — work must not continue until risk reduced | 2×4 = 8 Medium (ALARP) |
| N2 Pneumatic conveying | Flame/pressure transmission between vessels (pressure-piling) | 3 | 5 | **15** | **High** — intolerable; controls before proceeding | 2×4 = 8 Medium |
| N3 Cyclone | Fines cloud ignited (propagated or static) → explosion | 4 | 5 | **20** | **Critical** | 2×4 = 8 Medium |
| N4 Day silo | Headspace cloud during fill / self-heating nest → explosion; large volume | 3 | 5 | **15** | **High** | 2×4 = 8 Medium |
| N5 Bagging station | Static ignition at open fill point; **operator present**; initiates workroom secondary event | 4 | 5 | **20** | **Critical** | 2×3 = 6 Medium |
| Secondary explosion (building) | Primary event lofts settled layers → devastating secondary explosion | 3 | 5 | **15** | **High** (contingent on unverified housekeeping) | 2×4 = 8 Medium |
| N6 Dust collector | *If present* — typically the highest-risk node | — | — | **[GAP]** — confirm presence, then score | — |

¹ **Target residual is contingent** on: (a) the [GAP] test data (Action A1), (b) competent-person explosion-protection design and installation (Actions A3/A4), (c) verified ignition-source control (A6/A10), and (d) a verified combustible-dust housekeeping program (A7). It is a design target, **not a present state**.

---

### 7. Reactive-chemistry / thermal screen (SME-required — not omitted)

Maize (corn) starch is a **combustible organic dust**; it is **not a known self-reactive, oxidizer, water-reactive or energetic/thermally-unstable material** at ambient conditions, so a runaway-reaction (self-reactive/exothermic decomposition) basis of safety is **not indicated by the material class**. Two thermal pathways are nonetheless **retained for the workshop, not dismissed:**

- **Self-heating / smouldering in the day silo (N4):** resident bulk starch can support slow oxidation / microbial heating (moisture-dependent) leading to a smouldering nest that becomes an internal ignition source on disturbance/aeration. **Self-heating / DSC / basket-test data is [GAP]** → routed to testing (Action A1) and to the workshop.
- **Incompatibility:** no reactive incompatibility is flagged for maize starch with the plant materials described; **no incompatibility matrix was supplied [GAP]**. Confirm no incompatible chemicals (e.g. strong oxidisers) are co-stored or used near the line.

There is no self-reactive deflagration/runaway node to hand off beyond the dust-deflagration nodes; the thermal self-heating pathway (N4) is carried into the DHA/HAZOP hand-off (§8).

---

### 8. Connected-vessel & secondary-explosion path (the dominant fatality mechanism)

**Connected-vessel (pressure-piling) path.** The nodes are physically interconnected: **hammer mill → pneumatic conveying → cyclone → (dust collector, if present) → day silo.** A primary deflagration in **any one** vessel drives a flame front and a pressure wave through the pneumatic conveying interconnections into the adjoining vessels. The pre-compression ahead of the flame (**pressure-piling**) can raise the effective pressure and rate of pressure rise in the receiving vessel **above the standalone Pmax**, defeating protection that was sized for an isolated event. **Deflagration isolation (NFPA 69)** on every interconnection — fast-acting chemical/mechanical isolation, and assessment of whether existing **rotary valves** qualify as isolation devices — is the **load-bearing control** that breaks this path. Explosion venting/suppression on individual vessels is **not sufficient without isolation.**

**Secondary-explosion path.** A primary event (or a vent/rupture) lofts **settled dust layers** on beams, ledges, cable trays, ductwork and floors throughout the building into a suspended cloud, which the primary flame then ignites — the **secondary explosion**, historically the mechanism that turns a contained event into a mass-casualty, building-destroying one, and the reason the **occupied bagging station (N5)** and workroom are critical. Controls: **deflagration isolation and containment/venting to a safe location (engineering, primary)** to limit the primary event, **plus a verified combustible-dust housekeeping program (administrative, supporting)** to remove the secondary fuel. **Layer depth is [GAP]** and must be measured (Action A7).

---

### 9. Hand-off to `hazop-facilitator` (structured DHA/HAZOP nodes — this skill frames, does not run, the workshop)

Per the method (`KB-STD-IEC-61882`), the structured deflagration/thermal study is handed to a live, multidisciplinary **DHA/HAZOP workshop** facilitated by the `hazop-facilitator`. This skill **frames** the nodes and candidate deviations; it **does not** run the workshop, does not invent deviations the team did not raise, and records **[GAP]** rather than any fabricated engineering value. The workshop must name its participants and their competencies.

**Nodes to study:** N1 Hammer mill · N2 Pneumatic conveying · N3 Cyclone · N4 Day silo · N5 Bagging station · **N6 Dust collector (confirm presence first).**

**Candidate guideword × parameter deviations to open at each node** (illustrative framing only — the team decides):

| Guideword × parameter | Deviation to explore | Nodes |
|---|---|---|
| MORE temperature | Hot surface / bearing overheat / self-heating → ignition | N1–N4 |
| AS-WELL-AS contamination | Tramp metal / foreign object → impact spark | N1, N3 |
| LESS / NO flow | Blockage, dead-leg accumulation, choked conveying → layer build-up | N2, N3 |
| OTHER-THAN inerting (future) | Loss of inert gas / high O₂ (only if inerting adopted — needs LOC [GAP]) | N1–N4 |
| MORE / REVERSE pressure | Flame/pressure transmission between vessels (pressure-piling) | N2 (all interconnections) |
| PART-OF (charge) | Electrostatic charge accumulation on isolated conductors / bags | N2, N5 |

**Handed to the workshop with each node:** the held explosibility data (Kst 180, Pmax 8.5, MIE 30 — Chilworth 2024), the four **[GAP]** parameters (MIT, LOC, PSD, moisture), the connected-vessel path (§8), and the ignition-source enumeration (§3).

---

### 10. SMART actions register — owned & dated (`smart_actions`)

Role owners only; dates in prose. Today is 6 July 2026.

| ID | Action (Specific, Measurable) | HoC level | Owner (role) | Due | Priority |
|---|---|---|---|---|---|
| **A8** | **Interim risk-reduction & Management-of-Change:** with no explosion protection fitted, formally assess and restrict occupancy near unprotected connected vessels (N1–N4); log an MOC decision and interim safe-operating limits pending protection. | Administrative (interim) + Engineering (occupancy) | Plant Operations Manager (role) | by 13 July 2026 | **Immediate / Critical** |
| **A10** | **Verify bonding & earthing** on all plant handling the dust (continuity + earth-resistance test to specification) — load-bearing given MIE 30 mJ; record results and set a recurring test interval. | Engineering | Electrical Engineer (role) / Maintenance Manager (role) | by 20 July 2026 | High |
| **A7** | **Combustible-dust housekeeping program:** convert the existing regime into a written program with **measured layer-depth thresholds**, no-compressed-air rule, and inspection cadence; measure current layer depths across the building. | Administrative (supporting) | Site HSE Manager (role) | by 27 July 2026 | High |
| **A1** | **Commission laboratory testing** of the four [GAP] parameters — **MIT (cloud & layer), LOC, PSD, moisture** — on representative process samples **including the finest fraction** (cyclone/filter). Confirm the 2024 sample basis (PSD, moisture, MIE inductance) with the lab. | Engineering (data) | Process Safety Engineer (role) + Combustible-Dust Testing Laboratory (role) | commission by 3 August 2026 | **Critical** |
| **A2** | **Run the formal DHA/HAZOP workshop** with `hazop-facilitator` across nodes N1–N6, using the framing in §9; name participants/competencies; produce the DHA of record. | Administrative (study) | DHA Team Lead (role) | by 17 August 2026 | High |
| **A6** | **Ignition-source control package:** install magnetic separation / metal detection upstream of the hammer mill; formalise the hot-work permit system; set hot-surface/bearing temperature monitoring (surface limit to be finalised once **MIT** from A1 is known). | Engineering + Administrative | Maintenance Manager (role) | metal separation by 30 September 2026; permit system by 27 July 2026 | High |
| **A5** | **Electrical area classification of record** per NFPA 70 Art. 500/502 or 506, resolving the [GAP] release-grade/ventilation basis for external zones; verify all equipment in classified locations conforms (correct EPL/T-code). | Engineering | Electrical Engineer (role) | by 14 September 2026 | High |
| **A3** | **Explosion-protection engineering design** (competent vendor/engineer): deflagration **venting (NFPA 68)** and/or **suppression (NFPA 69)** for N1–N4 (and N6 if present), sized to Kst 180 / Pmax 8.5, verified against A1 data. | Engineering (protection) | Process Safety Engineer (role) | design by 30 September 2026; installed by 15 December 2026 | **Critical** |
| **A4** | **Deflagration isolation (NFPA 69)** on all interconnections to break the connected-vessel path; assess whether existing rotary valves qualify as isolation devices. | Engineering (protection) | Process Safety Engineer (role) | design by 30 September 2026; installed by 15 December 2026 | **Critical** |
| **A9** | **Assemble the NFPA combustible-dust compliance dossier** (DHA of record, area classification, basis-of-safety statement, protection design/certification, management systems) and set the periodic review cycle. | Administrative | Site HSE Manager (role) | by 31 October 2026 | Medium |
| **A11** | **Reassess inerting** as a higher-order (avoid-the-atmosphere) basis of safety for enclosed nodes **once LOC (from A1) is known**; if viable, evaluate against the A3/A4 protection design. | Engineering (evaluation) | Process Safety Engineer (role) | within 4 weeks of LOC result (target by 31 August 2026) | Medium |

---

### 11. Open gaps register (honest [GAP] / [ASSUMPTION] summary)

| Item | Type | Routed to |
|---|---|---|
| MIT (cloud & layer) — hot-surface temperature limit undefined | **[GAP]** | Testing (A1) |
| LOC — inerting cannot be designed | **[GAP]** | Testing (A1) → inerting reassessment (A11) |
| Particle-size distribution — held data may not bound the fines | **[GAP]** | Testing (A1) |
| Moisture content — validity of held Kst/Pmax/MIE depends on it | **[GAP]** | Testing (A1) |
| Self-heating / DSC data for stored starch (N4) | **[GAP]** | Testing (A1) + workshop (A2) |
| Dust collector / bag filter — presence not confirmed (likely highest-risk node) | **[GAP] / [ASSUMPTION]** | Process review + DHA (A2) |
| External-area release grade + ventilation (zoning basis) | **[GAP]** | Area classification (A5) |
| Building dust-layer depth (secondary-explosion fuel & workroom zoning) | **[GAP]** | Housekeeping program (A7) |
| Bonding/earthing verified to specification | **[GAP]** (existing but unverified) | A10 |
| Site/legal-entity identifier & address | **[GAP]** | Document control before issue |
| 2024 test-sample basis (PSD, moisture, MIE inductance) | **[ASSUMPTION]** pending confirmation | Confirm with lab (A1) |
| Incompatibility matrix / co-stored oxidisers | **[GAP]** | Confirm (A2, §7) |

---

*Built by Eyekyam · HSE Leadership, operationalised with AI · eyekyam.com*
