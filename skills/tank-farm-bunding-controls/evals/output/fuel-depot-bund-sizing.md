<!-- LOCKED fixture — owner-LOCKED at the SW3 19-04 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Secondary Containment Sizing & Controls Review
## Fuel-Depot Tank Farm — Shared-Bund Group (Gasoline + Diesel)

| Document control | |
|---|---|
| **Deliverable** | Secondary containment sizing + containment plan + overfill / segregation controls review |
| **Scope** | Bund sizing · containment plan · controls review (segregation, overfill, firewater/drainage, penetrations/integrity) for one shared bund holding 3 atmospheric tanks |
| **Site** | Fuel-depot tank farm — shared-bund group [GAP: site name/reference not supplied] |
| **Jurisdiction** | UK / EU |
| **Issued** | 6 July 2026 |
| **Revision** | Rev 0 — DRAFT for competent-person review |
| **Prepared by** | HSE Consultant (role), Eyekyam |
| **SME review** | Ran — persona: Bulk-storage / secondary-containment engineer (decision-support; does **not** replace human competent-person sign-off) |
| **Competent-person sign-off** | ☐ Pending — required before use |
| **Personal data** | None present; all owners shown as role labels |
| **Status** | Decision-support only — not legal advice; must be reviewed by a competent person |

---

## 1. Echo-back of captured facts (basis of this assessment)

Tank farm: **fuel depot**, one shared bund holding **3 atmospheric-storage tanks**:

| Tank | Substance | Volume | Hazard class (as supplied) |
|---|---|---|---|
| T1 | Diesel | 500 m³ | Combustible liquid (higher flashpoint) |
| T2 | Diesel | 500 m³ | Combustible liquid (higher flashpoint) |
| **T3** | **Gasoline** | **750 m³** | **Flammable — flashpoint < 23 °C; DSEAR dangerous substance / flammable atmosphere** |

- **Largest single tank:** T3 gasoline, **750 m³**.
- **Aggregate inventory in the shared bund:** 1,750 m³.
- **Existing secondary containment:** bund **net capacity 620 m³**; each tank fitted with a high-level overfill trip; bund drainage runs to an **interceptor**; **no firewater-retention sizing** in place.
- **Receptor:** a **surface watercourse 40 m** from the site boundary (sensitive environmental receptor; primary pollution pathway).
- **Sizing rule to apply (as instructed):** **110 % of the largest tank + freeboard + firewater allowance.**

---

## 2. Containment sizing basis — stated *from the rule* (not an assumed %)

**Basis of the required volume (from the stated rule):** the secondary containment must retain **110 % of the largest single tank, plus freeboard, plus a firewater allowance**. This basis is stated directly from the rule instructed for this site — it is not an assumed percentage.

**Governing tank:** the largest single tank is the **750 m³ gasoline tank (T3)**.

| Component of the required volume | Value | Note |
|---|---|---|
| 110 % of largest tank (750 m³) | **825 m³** | Deterministic from the rule |
| + Freeboard | **[GAP]** | Freeboard allowance not supplied — must not be invented; competent person to specify (wall-height margin above retained liquid) |
| + Firewater allowance | **[GAP]** | Not supplied and **not currently sized** — requires fire-engineering assessment (application rate × duration + foam) for a gasoline tank fire |
| **Required net retained volume** | **≥ 825 m³** (825 + freeboard + firewater) | The 825 m³ is the *floor*; the true requirement is materially higher once the two [GAP] components are added |

### 2.1 Required vs existing — the shortfall

| | Volume |
|---|---|
| **Required (base, 110 % largest tank)** | **825 m³** |
| **Existing net capacity** | **620 m³** |
| **Deficit against the base figure** | **–205 m³** |
| **Existing capacity as % of base requirement** | **75 %** (620 ÷ 825) |

> **FINDING F1 — FAIL against the stated rule (headline).** The bund holds only **75 %** of the base 110 %-largest-tank requirement — a deficit of **at least 205 m³** *before* freeboard and the firewater allowance are added. Because both of those required components are unquantified [GAP] and neither is currently provided, the **true deficit is materially greater than 205 m³**. A full-tank loss of the gasoline tank (750 m³) alone would leave 130 m³ of product with nowhere to go inside the bund, migrating toward the 40 m watercourse. **Containment is non-compliant with the instructed basis.**

### 2.2 Multi-tank cross-check (flagged — competent person to confirm)

For a bund serving **several** tanks, common UK guidance (**CIRIA C736**, *Containment systems for the prevention of pollution*) sizes the bund to the **greater of** 110 % of the largest tank **or 25 % of the aggregate stored volume**. **[ASSUMPTION — verify]** Applying that greater-of test illustratively: 25 % × 1,750 m³ = **437.5 m³**, which is **less than** the 825 m³ from the 110 %-largest-tank leg. **The 110 %-largest-tank figure therefore governs (825 m³) even under the multi-tank check** — the shortfall in §2.1 stands. This cross-check is offered for the competent person to confirm against the site's applicable standard; the binding basis for this deliverable remains the instructed **110 % largest tank + freeboard + firewater**.

---

## 3. Segregation of incompatible substances

**Chemical compatibility:** gasoline and diesel are both hydrocarbons — **chemically compatible / miscible; there is no reactive incompatibility** driving a mandatory separate bund. This is stated plainly rather than inventing a reaction hazard that does not exist.

**The real segregation driver is fire escalation, not chemistry:**

| Pair | Chemical reactivity | Fire-hazard segregation |
|---|---|---|
| Gasoline (T3) ↔ Diesel (T1/T2) | Compatible — no reaction | **Concern** — a gasoline release inside the shared bund creates a **flammable vapour atmosphere and pool-fire risk that engulfs the diesel tanks**, driving fire escalation / domino across the whole group |

> **FINDING F2 — Shared bund places a flammable (gasoline) with combustibles (diesel) with no sub-division.** A gasoline spill/pool fire in the common bund exposes both diesel tanks. Recommended engineering control: **provide intermediate bund division walls (compartmentation) so the gasoline tank drains to its own sub-cell**, or provide the gasoline tank with **dedicated secondary containment**, so a flammable release is contained separately and does not engulf the adjacent diesel tanks. This is an **engineering** control (higher order than administrative separation-distance rules).

---

## 4. Overfill protection — independence of the high-level trip

Each tank is fitted with a **high-level overfill trip**. The instructed test — and the load-bearing lesson of the **Buncefield fuel-depot overfill and vapour-cloud explosion (2005)**, which involved exactly this kind of atmospheric **gasoline** tank at a fuel depot — is that the overfill protection must be a **fully independent protection layer**, separate from the operating (servo/radar) level gauge.

**Verification against IEC 61511 independent-protection-layer principles:**

| Independence test | Status |
|---|---|
| Overfill trip uses a **separate level sensor** from the operating gauge (not the same transmitter) | **[GAP] — not evidenced in the inputs** |
| Separate logic solver / trip amplifier from the gauge/control system | **[GAP] — not evidenced** |
| **Independent final element** (dedicated shutoff valve / pump trip), not shared with normal filling control | **[GAP] — not evidenced** |
| Automatic action on high-high level (not reliant on operator response alone) | **[GAP] — not evidenced** |
| Proof-tested at a defined interval; SIL target set by LOPA if required | **[GAP] — not evidenced** |

> **FINDING F3 — Overfill-trip independence is unverified (FLAG).** The inputs confirm a trip exists but do **not** establish that it is independent of the level gauge. **If the trip derives its signal from the same instrument as the operating level gauge, it is a single point of failure and is not a valid independent overfill-prevention system.** Given a low-flashpoint gasoline tank at a fuel depot 40 m from a watercourse, an **automatic high-level overfill-prevention system, independent of the tank gauging system** (separate sensor, logic and final element), is required. **[ASSUMPTION — verify]** The governing UK framework for this is the post-Buncefield fuel-storage-site guidance (Process Safety Leadership Group, *Safety and environmental standards for fuel storage sites*); the competent person must confirm the current edition/status and the required SIL from a LOPA. This standard is outside the skill's loaded knowledge base and is flagged for confirmation, not asserted with a clause number.

---

## 5. Firewater + contaminated-drainage containment (watercourse protection)

The **40 m watercourse** is the controlling environmental receptor. Two release pathways are currently open:

1. **Drainage default routing.** Bund drainage runs to an **interceptor**. An interceptor (oil–water separator) is designed for **routine minor drainage** (rainwater with trace hydrocarbon) — it is **not** firewater retention and will be **overwhelmed by a bulk spill or a firefighting-water surge**, discharging contaminated water to the watercourse.
2. **No firewater retention.** The stated sizing rule **requires** a firewater allowance; none is sized. In a gasoline tank fire, applied firewater + foam would **overtop the already-undersized bund** and migrate off-site.

> **FINDING F4 — No firewater/contaminated-drainage containment; direct pathway to the watercourse (FLAG — environmental-release omission).** Required controls:
> - **Normally-closed, fail-safe (fail-closed) penstock / isolation valve on the bund outfall**, so bund contents (spill + firewater) are **retained by default** and are **not** routed to the interceptor/watercourse unless positively opened by an authorised person after a check for contamination.
> - **Sized firewater-retention capacity** — either the bund upsized to include the firewater + foam volume, or **remote/tertiary containment** (catchment/lagoon) sized from the fire-engineering firewater assessment.
> - **Positive isolation of contaminated drainage** from the surface-water/interceptor route; spill/firewater directed to containment, then to controlled disposal.
> - **Interceptor** confirmed to be a last-line polisher for clean runoff only — never the primary containment for a spill.

---

## 6. Bund penetrations, wall & integrity

The inputs do not describe bund construction, penetrations, joints or leak-test status → **[GAP]**. Volume alone does not equal containment; a permeable or breached bund fails regardless of its rated capacity.

> **FINDING F5 — Bund integrity / penetrations unreviewed (FLAG).** Competent person to verify:
> - **Pipe penetrations** (fill/draw lines, drainage) through the bund wall are **sealed to the bund's containment rating** — every penetration is a potential leak path.
> - **Bund wall and floor are impermeable and hydrocarbon-resistant** (compatible with gasoline) — lining condition, joint sealant, and any cracking.
> - **Valves through the bund wall** (the drainage penstock) are **fail-safe closed**, accessible and outside the pool footprint.
> - **Integrity/leak-test records and inspection cycle** — **[GAP]** (bund inspection cycle and PESO/permit data not supplied; not applicable jurisdictionally here but the inspection cycle is still required).

---

## 7. Flammable-atmosphere area control (DSEAR)

Gasoline's flashpoint **< 23 °C** means a **flammable atmosphere is credible at ambient temperature**; the tank, its vents/fill points, and the bund (where a spill could pool) fall under **DSEAR 2002** (KB-STD-DSEAR: *risk assessment → basis of safety → area classification → control of ignition sources*).

- **Basis of safety** (DSEAR, HoC order): avoid the flammable atmosphere → control ignition sources → mitigate. For fixed bulk storage the practicable basis is **control of ignition sources within the classified area** plus containment/vapour management.
- **Area classification (ATEX zones)** around the gasoline tank vents, fill points and the bund pool footprint is a **competent-person engineering judgement** (Zone 0/1/2 per KB-STD-ATEX). The bund, when holding a gasoline pool, may itself become a classified area during/after a spill. **This deliverable structures the requirement; it does not decide the zone.** → route to a **DSEAR competent person**.

> **FINDING F6 — DSEAR area classification and ignition-source control for the gasoline inventory to be confirmed** (not evidenced in inputs). Zoning **must not be defaulted**; it is justified from release grade, substance properties and ventilation.

---

## 8. Consequence banding

Applied conceptually via the shared `risk_matrix` engine; the **deterministic `risk_matrix.score()` should be re-run by the competent person with the site's calibrated 5×5 descriptors** — the descriptors here are **[ASSUMPTION]** pending the site matrix, so the band is indicative.

| Scenario | Severity (indicative) | Likelihood (indicative) | Band |
|---|---|---|---|
| Loss of containment of the gasoline tank overtops the undersized bund; product + firewater reach the 40 m watercourse (with pool-fire potential) | **Major → Catastrophic** (large environmental harm + fire escalation) | **Possible → Likely** while the bund is 205 m³+ short and firewater is unretained | **HIGH / Intolerable — interim controls required now** |

Because the bund is already non-compliant and the receptor is close, **interim risk reduction is required before the permanent engineering fixes are delivered** (see Action A1–A3).

---

## 9. Controls — hierarchy-of-controls ranked

Per KB-SNIP-HOC, most-effective first. No hazard is treated by administrative/PPE measures alone without a higher-order control or a justification.

| # | Hazard addressed | Control | HoC level | Note |
|---|---|---|---|---|
| C1 | Loss of containment overtopping an undersized bund | **Upsize secondary containment to ≥ 825 m³ + freeboard + firewater allowance** (110 % largest tank per the stated rule) | **Engineering** | Closes F1 |
| C2 | Contaminated spill/firewater reaching the watercourse | **Normally-closed, fail-closed penstock on bund outfall** + **sized firewater retention** (upsized bund or remote catchment) | **Engineering** | Closes F4 |
| C3 | Gasoline pool fire engulfing diesel tanks | **Bund compartmentation / dedicated gasoline sub-cell** (division walls) or dedicated gasoline bund | **Engineering** | Closes F2 |
| C4 | Tank overfill (Buncefield-type) | **Automatic high-level overfill-prevention system independent of the level gauge** (separate sensor/logic/final element; SIL per LOPA) | **Engineering** | Closes F3 |
| C5 | Flammable atmosphere ignition | **DSEAR area classification + ignition-source control / suitable equipment by zone** | **Engineering** | Closes F6 |
| C6 | Leak path through bund fabric | **Seal/upgrade penetrations; impermeable hydrocarbon-resistant bund lining; integrity testing** | **Engineering** | Closes F5 |
| C7 | *Interim, pending C1–C2:* uncontrolled default drainage | **Keep bund penstock locked closed; open only under a checked, authorised drain-down procedure** | Engineering + Administrative | Interim — **lower-order component flagged**: the administrative locking procedure is an interim wrap around the engineering penstock, **not** a substitute for C1/C2 |
| C8 | *Interim, pending C1:* gasoline tank inventory exceeds available containment | **Cap gasoline tank working volume so 110 % of the working level ≤ 620 m³ (i.e. ≤ ~560 m³ working) until the bund is upsized** | **Administrative** | **Lower-order control — flagged:** justified only as a short-term interim because the engineering upsizing (C1) cannot be delivered immediately; it does **not** address freeboard/firewater and must not be treated as compliance. Escalate to C1. |
| C9 | Spill reaching receptor before isolation | **Site spill-response + emergency plan; spill kit; watercourse-protection drill; regulator notification route** | Administrative | Supports, does not replace, C1–C2 |

**Elimination / substitution** were considered: the fuel-storage function cannot be eliminated, but the competent person should test **inventory reduction / relocation of the gasoline tank away from the watercourse** as an inherently-safer option before committing to a purely additive containment upgrade.

---

## 10. Actions register (owned and dated)

Validated as SMART (owner + target date). Dates are targets for the competent person to confirm; owners are role labels.

| ID | Action | HoC | Owner (role) | Target date | Priority |
|---|---|---|---|---|---|
| **A1** | Lock the bund outfall penstock **closed**; issue an authorised, checked drain-down procedure so nothing routes to the interceptor/watercourse by default (interim C7) | Eng+Admin | Site Manager (role) | **13 July 2026** | Immediate |
| **A2** | Cap the gasoline tank (T3) working volume to ≤ ~560 m³ so 110 % of the working inventory sits within the existing 620 m³, as an interim measure pending A6 (interim C8 — flagged lower-order) | Admin | Terminal Operations Supervisor (role) | **13 July 2026** | Immediate |
| **A3** | Confirm the emergency/spill-response plan protects the 40 m watercourse (containment booms, drain seals, spill kit, regulator-notification route); brief the shift | Admin | Environmental Manager (role) | **13 July 2026** | Immediate |
| **A4** | Verify whether the high-level overfill trip is **independent** of the tank gauging system (separate sensor/logic/final element); document the finding; if not independent, initiate the independent overfill-prevention upgrade and set the SIL from a LOPA | Eng | Instrumentation & Control Engineer (role) | **20 July 2026** | High |
| **A5** | Confirm the 620 m³ is a **net** capacity (post-displacement by the other tanks/foundations to bund crest); re-state the deficit if it is gross | Eng | Mechanical Integrity Engineer (role) | **27 July 2026** | High |
| **A6** | Commission the **fire-engineering firewater assessment** (application rate × duration + foam) to size the firewater allowance and the required total containment volume | Eng | Fire Safety Engineer (role) | **3 August 2026** | High |
| **A7** | **Bund integrity & penetration survey** — impermeability/lining, wall & floor condition, all pipe/valve penetrations, leak-test; set the recurring inspection cycle | Eng | Mechanical Integrity Engineer (role) | **10 August 2026** | High |
| **A8** | **DSEAR / ATEX area classification** of the gasoline tank vents, fill points and bund pool footprint; ignition-source control; equipment suitability by zone | Eng | DSEAR Competent Person (role) | **17 August 2026** | High |
| **A9** | **Design the permanent containment upgrade** to ≥ 825 m³ + freeboard + firewater allowance (from A6), **plus fail-closed penstock and firewater retention** (upsized bund or remote catchment) | Eng | Chartered Civil/Process Engineer (role) | **14 September 2026** | High |
| **A10** | **Design bund compartmentation** — dedicated gasoline sub-cell / division walls so a gasoline spill/fire does not engulf the diesel tanks | Eng | Chartered Civil/Process Engineer (role) | **14 September 2026** | Medium |
| **A11** | Re-run the deterministic `risk_matrix.score()` with the site's calibrated 5×5 descriptors and record the banded residual for each finding | — | Process Safety Engineer (role) | **21 September 2026** | Medium |
| **A12** | **Competent-person review and sign-off** of this assessment and the remediation design before implementation | — | HSE Competent Person (role) | **28 September 2026** | High |
| **A13** | Implement A9/A10 and revalidate containment against the stated rule | Eng | Project Engineer (role) | **[GAP — set on completion of A9/A10 design and funding approval]** | High |

---

## 11. Open items / gaps register

| Ref | Gap | Impact | Routed to |
|---|---|---|---|
| G1 | **Freeboard allowance** not specified | Required containment volume understated; 825 m³ is a floor, not the final figure | Competent person (A9) |
| G2 | **Firewater allowance** not sized (and none provided) | Governing shortfall is larger than 205 m³; watercourse exposure | Fire Safety Engineer (A6) |
| G3 | **Overfill-trip independence** not evidenced | Possible single point of failure on a Buncefield-type hazard | I&C Engineer (A4) |
| G4 | **Bund construction/penetrations/leak-test status** not supplied | Containment integrity unverified | Mechanical Integrity Engineer (A7) |
| G5 | **Net vs gross** basis of the 620 m³ not confirmed | Deficit may be larger | Mechanical Integrity Engineer (A5) |
| G6 | **Applicable UK containment standard/edition** (CIRIA C736 greater-of test; PSLG fuel-storage overfill guidance) not in the skill's loaded KB | Cross-check and overfill standard to be pinned to the current edition | Competent person (A9/A4) |
| G7 | **Site name/reference, tank-farm layout, inspection cycle, licence/permit data** not supplied | Document-control completeness | Site Manager (role) |
| G8 | **Site 5×5 risk-matrix descriptors** not supplied | Consequence band is indicative pending calibrated run | Process Safety Engineer (A11) |

---

## 12. Bottom line

- **The bund fails the stated sizing rule.** Required base volume is **825 m³** (110 % of the 750 m³ gasoline tank); existing net capacity is **620 m³** — a deficit of **at least 205 m³ (only 75 % of the base requirement)**, and **larger** once the required-but-unquantified freeboard and firewater allowance are added. **[FINDING F1]**
- **The firewater/contaminated-drainage pathway to the 40 m watercourse is open** — an interceptor is not firewater retention; a fail-closed penstock and sized firewater retention are required. **[FINDING F4]**
- **Overfill-trip independence is unverified** on a gasoline fuel-depot tank — the exact Buncefield failure mode; confirm an independent high-level overfill-prevention system. **[FINDING F3]**
- **Gasoline shares an undivided bund with diesel** — not a chemical incompatibility, but a fire-escalation risk; compartmentation or a dedicated gasoline bund is required. **[FINDING F2]**
- **Interim controls (A1–A3) are required now** while the engineering upgrades (A6–A13) are delivered.

**Controls are hierarchy-of-controls ranked; the only administrative-only measures (A2/interim locking) are explicitly flagged as short-term interim measures pending the engineering fixes, not as compliance.**

---

> **Disclaimer.** This is **decision-support only** and **not legal advice**. It must be reviewed and signed off by a **competent person** before use. The containment basis is stated from the rule instructed for this site; freeboard and firewater allowance are unquantified and flagged **[GAP]**, not invented. Standard references outside the skill's loaded knowledge base (CIRIA C736; the PSLG fuel-storage overfill guidance; the site's ATEX zoning) are flagged for confirmation of the current edition rather than cited with fabricated clause numbers. The SME-persona review (bulk-storage / secondary-containment engineer) has run as an internal quality gate; it **precedes and does not replace** the human competent-person sign-off.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
