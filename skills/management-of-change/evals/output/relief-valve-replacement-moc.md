<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3. -->
# Management of Change (MoC) Package
## Replacement of V-101 Relief Valve — Unit 100, Site-X

| Field | Value |
|---|---|
| MoC reference | [GAP — site MoC register number not supplied; assign from the site register before circulation] |
| Package date | 5 July 2026 |
| Change title | Replace the relief valve on vessel V-101, Unit 100, Site-X |
| Change Owner | Change Owner — accountable-engineer role |
| PSSR authoriser | PSSR Reviewer — pre-start-up-review role |
| Package status | **OPEN — START-UP BLOCKED** (PSSR gate not passed) |
| Prepared under | KB-STD-PSM (PSM elements (l) MoC and (i) PSSR); ISO 45001 clause 8.1.3 |

> ## 🚫 START-UP BLOCKED
> At least one Pre-Start-Up Safety Review (PSSR) item is **open** — the change review records **"PSI updated" as Open**, and no evidence has been supplied that the remaining four PSSR items are closed. **No start-up authorisation is issued by this package, and none may be issued until every PSSR item in Section 7 passes.** This gate has no exceptions and cannot be waived by any signatory.

---

## 1. Change summary (captured facts)

| Intake item | Captured value | Basis |
|---|---|---|
| Exact change | Replace the relief valve on vessel V-101, Unit 100, Site-X | Supplied (change review title) |
| Change type | Equipment / hardware | Derived from the change description |
| Classification | Minor change — reviewed under MoC (not replacement-in-kind) | [ASSUMPTION — see Section 2; the review routes the work through MoC with a PSSR, so it is treated as a change, not an RIK exit] |
| Permanent or temporary | Permanent | [ASSUMPTION — not stated; a valve replacement is treated as permanent. See Section 5 for the temporary-impairment caveat] |
| Technical basis | Not supplied | [GAP — see Section 3; must be completed before PSSR] |
| Sector | Process (pressure-vessel relief system) | [ASSUMPTION — Unit/vessel/relief-valve nomenclature indicates a covered process unit; exact sector (chemicals / O&G / refining) not supplied] |
| Jurisdiction | Not supplied | [GAP — statutory hook unconfirmed; see Section 11. No specific national law is relied on until the jurisdiction is confirmed] |
| Output requested | Full MoC package (management audience) | Supplied ("Build the MoC package") |
| Change Owner | Change Owner — accountable-engineer role | Supplied (role label) |
| Start-up authoriser | PSSR Reviewer — pre-start-up-review role | Supplied (role label) |

Site context (aggregated): 12 recordable injuries this period. Categories with fewer than 5 individuals have been aggregated upward with secondary suppression applied, so suppressed cells cannot be back-calculated from the total. No injury sub-category with fewer than 5 individuals is published in this package.

---

## 2. Change classification and triage

**Replacement-in-kind (RIK) evaluation.** A relief-valve replacement exits MoC as RIK **only** if the replacement is identical to the approved specification in every respect that matters to the relief function: manufacturer/model or approved equivalent, set pressure, orifice designation/relieving capacity, inlet/outlet size and rating, trim and soft-goods materials, and code stamp — all matching the approved relief design basis for V-101.

- The supplied change review does **not** state the replacement valve's specification against the original. **[GAP — replacement-valve datasheet vs. approved relief design basis not supplied.]**
- The review itself routes the work through MoC with a live PSSR checklist, so this package conservatively treats the work as a **change requiring MoC review**, not an RIK exit. [ASSUMPTION]

**Escalation trigger (significant change).** If closure of the [GAP] above shows the replacement valve differs from the design basis in set pressure, relieving capacity, orifice size, valve type (e.g. conventional → pilot-operated), or inlet/outlet configuration, this MoC must be **escalated to a significant change**: the relief-system design basis for V-101 must be re-verified and the relevant process hazard analysis revalidated for the affected node **before** the change proceeds. The Change Owner (role) owns this determination (action A2, Section 9).

**Emergency change.** Not claimed in the supplied review; no retrospective-review branch is activated.

---

## 3. Technical basis for the change

**[GAP — the engineering/operational rationale for replacing the V-101 relief valve was not supplied.]** The MoC cannot pass review, and the PSSR cannot convene, until the Change Owner (role) completes the following fields with site records. No value below has been assumed:

| Required technical-basis element | Status |
|---|---|
| Reason for replacement (e.g. failed bench test, end of service interval, damage, obsolescence) | [GAP] |
| Approved relief design basis reference for V-101 (governing overpressure scenario and required capacity) | [GAP] |
| Replacement valve datasheet: set pressure, orifice designation, capacity, materials, code stamp | [GAP] |
| Sizing verification confirming the replacement meets or exceeds the required relieving capacity | [GAP] |
| Confirmation that inlet/outlet piping, supports, and any bellows/back-pressure provisions are unchanged | [GAP] |
| Bench-test certificate for the replacement valve (certified set pressure, seat tightness) | [GAP] |

---

## 4. Change risk assessment — hazards this change introduces

Scored on the pack's standard 5×5 matrix (likelihood 1–5 × severity 1–5; bands: 1–4 Low, 5–9 Medium, 10–15 High, 16–25 Very High). [ASSUMPTION — the site's own calibrated matrix was not supplied; re-map these scores to the site matrix at competent-person review.] Every control set is ranked per the hierarchy of controls (KB-SNIP-HOC); no hazard is treated with PPE alone.

| # | Hazard introduced by the change | Worst credible consequence | Initial risk (L×S) | Controls (hierarchy tier) | Residual risk (L×S) |
|---|---|---|---|---|---|
| H1 | Wrong valve specification installed — set pressure, orifice/capacity, or trim not matching the V-101 relief design basis | Vessel overpressure beyond design with loss of containment; the relief system fails to protect on demand | 3×5 = 15 (High) | **Engineering:** procure strictly against the approved relief design basis datasheet; certified bench test of set pressure before installation; positive tag/serial verification at the vessel. **Administrative:** independent verification of the datasheet match by a second competent engineer; "equipment as-designed" PSSR line (Section 7) held open until evidenced | 1×5 = 5 (Medium) |
| H2 | Breaking containment during valve removal on a vessel that still holds pressure, process fluid, or vapour | Sudden release of stored energy/process fluid onto the work crew; injury and uncontrolled release | 4×5 = 20 (Very High) | **Elimination:** take V-101 out of service — depressurise, drain, and purge before break-in (removes the stored energy). **Engineering:** positive isolation (blinds or double block and bleed) proven before work starts. **Administrative:** permit to work with isolation certificate and gas test at break-in. **PPE (last resort):** as specified on the permit for residual break-in exposure | 1×5 = 5 (Medium) |
| H3 | Relief path left blocked after reinstatement — inlet/outlet isolation valve left closed, or a test gag/bonnet blank left in the valve | V-101 returned to service with no effective overpressure protection | 3×5 = 15 (High) | **Engineering:** car-seal or lock open every relief-path isolation valve per the relief design basis; physical verification that any test gag or blank is removed. **Administrative:** reinstatement checklist with independent field verification; PSSR walk-down confirms the open relief path before the gate can pass | 1×5 = 5 (Medium) |
| H4 | Incorrect installation — wrong orientation, gasket, bolt torque, or unsealed body/drain connections | Leak at the valve joint in service, or valve fails to lift at set pressure | 3×4 = 12 (High) | **Engineering:** install per the manufacturer's installation manual and the site piping specification; leak test at reinstatement. **Administrative:** defined QA hold points; installation by a competent fitter with records retained | 1×4 = 4 (Low) |
| H5 | Process safety information drift — valve register, PSI datasheet, or P&ID not updated to the as-installed valve | Future operating, maintenance, and relief-review decisions made on wrong data | 4×3 = 12 (High) | **Administrative:** PSI update completed and evidenced **before start-up** — this is PSSR item 1 and is currently OPEN (Section 7); document control sign-off required | 1×3 = 3 (Low) |

**Residual-risk note (ALARP).** H1–H3 retain Medium residual scores because the credible severity of a relief-system failure remains at 5; the controls reduce likelihood only. This is the correct shape for a safeguarding-system change: residual risk rests on the verification controls actually being executed and evidenced, which is exactly what the PSSR gate in Section 7 enforces. No lower-order-only (administrative/PPE) treatment is applied to any severity-5 hazard without an engineering or elimination control above it.

**In-service replacement caveat.** [GAP — the review does not state whether V-101 will be shut down for the replacement or whether an in-service replacement under a temporary relief impairment is intended.] If any period of operation without the installed relief valve is proposed, that impairment is a **separate temporary change** requiring its own MoC, its own risk assessment, compensating measures, and a hard expiry — it is **not** covered by this package.

---

## 5. Temporary-change expiry

Not activated: this change is treated as **permanent** [ASSUMPTION — Section 1]. If the classification changes, or if the in-service impairment described in Section 4 is proposed, a temporary-change record with an explicit expiry condition/date is mandatory before any such condition is created; a temporary change without an expiry is non-conformant and is flagged on sight.

---

## 6. Affected process safety information, documents, and procedures

| Document / PSI element | Affected? | Held on site? | Update status |
|---|---|---|---|
| Relief-valve register / PSI datasheet for V-101 | Yes — confirmed (PSSR item "PSI updated" is open against it) | [GAP — custody not stated] | **OPEN — blocks start-up** |
| P&ID for Unit 100 (V-101 relief line) | Likely — if tag, spec, or configuration annotation changes [ASSUMPTION] | [GAP] | Not evidenced — [GAP] |
| Relief/flare system design basis for V-101 | To be confirmed via the Section 2 RIK determination | [GAP] | Not evidenced — [GAP] |
| Operating procedures (isolation, reinstatement, car-seal register) | [GAP — whether any procedure content changes is not stated] | [GAP] | Not evidenced — [GAP] |
| Training / awareness material for affected operators | [GAP] | [GAP] | Not evidenced — [GAP] |

---

## 7. Pre-Start-Up Safety Review (PSSR) — hard pre-start-up gate

**Gate rule:** every item below must be **CLOSED with evidence** before the PSSR Reviewer (role) may authorise start-up. One open item blocks start-up — no exceptions, no conditional or "punch-listed" start-up for safety-critical items.

| # | PSSR item | Status at 5 July 2026 | Owner (role) | Evidence required to close |
|---|---|---|---|---|
| 1 | PSI updated (valve register, datasheet, P&ID) | **OPEN — blocks start-up** (stated in the change review) | Change Owner (role) | Updated PSI records under document control, referencing the as-installed valve |
| 2 | Operating procedures updated | **OPEN — no evidence supplied** [GAP] | Change Owner (role) | Issued procedure revisions, or a recorded determination that no procedure changes |
| 3 | Training completed for affected personnel | **OPEN — no evidence supplied** [GAP] | Change Owner (role) | Training/communication records for affected operating and maintenance roles |
| 4 | Change-RA controls in place (Section 4) | **OPEN — no evidence supplied** [GAP] | Change Owner (role) | Closed permits, isolation certificates, bench-test certificate, car-seal register entries, independent verification records |
| 5 | Equipment installed as-designed | **OPEN — no evidence supplied** [GAP] | PSSR Reviewer (role) | Field walk-down: tag/serial vs. datasheet, orientation, gag removed, relief-path isolation valves sealed open, leak test passed |

**Gate outcome: START-UP NOT AUTHORISED.** Items 2–5 are recorded as open because no closure evidence was supplied with the change review — an unevidenced item is treated as open, never presumed closed.

---

## 8. Document and training updates before start-up

All document and training updates in Section 6 must be completed and evidenced **before** the PSSR convenes for closure — they are inputs to PSSR items 1–3, not post-start-up clean-up. Post-start-up backfilling of PSI or training records is a non-conformance under KB-STD-PSM element (l).

---

## 9. Action plan (SMART, tracked)

All due dates below are **proposed** [ASSUMPTION — scheduling not supplied; the Change Owner (role) confirms or re-dates each action at review].

| ID | Action | Owner (role) | Due | Done means |
|---|---|---|---|---|
| A1 | Complete the technical basis (all six [GAP] fields in Section 3) and attach the records to this MoC | Change Owner (role) | 10 July 2026 | Section 3 table fully evidenced; no [GAP] remains |
| A2 | Compare the replacement-valve datasheet against the approved V-101 relief design basis; record the RIK / minor / significant determination per Section 2 | Change Owner (role) | 10 July 2026 | Written determination on file; if "significant", PHA revalidation is scheduled before work proceeds |
| A3 | Update the PSI set — valve register, datasheet, P&ID — and route through document control (closes PSSR item 1) | Change Owner (role) | 14 July 2026 | PSSR item 1 evidenced and closed |
| A4 | Determine and issue any operating-procedure changes; deliver and record training/communication to affected roles (closes PSSR items 2–3) | Change Owner (role) | 17 July 2026 | PSSR items 2 and 3 evidenced and closed |
| A5 | Execute the Section 4 control set in the field and compile the evidence pack — permits, isolation certificate, bench-test certificate, car-seal entries, independent verifications, leak test (closes PSSR item 4) | Change Owner (role) | 17 July 2026 | PSSR item 4 evidenced and closed |
| A6 | Convene the PSSR walk-down; verify equipment as-designed (closes PSSR item 5); authorise start-up **only if all five items pass** | PSSR Reviewer (role) | 20 July 2026 | Signed PSSR record with all items closed — or start-up remains withheld with the open items listed |
| A7 | Resolve the shutdown vs. in-service replacement question (Section 4 caveat); if any relief impairment is proposed, open a separate temporary MoC with a hard expiry before creating the condition | Change Owner (role) | 10 July 2026 | Written execution strategy on file; no impairment exists without its own temporary MoC |

---

## 10. Roles and authorisation

| Role | Accountability | Sign-off status at 5 July 2026 |
|---|---|---|
| Change Owner — accountable-engineer role | Owns the change, the technical basis, the risk assessment, and actions A1–A5, A7 | Not signed — package incomplete ([GAP] items open) |
| PSSR Reviewer — pre-start-up-review role | Sole authoriser of start-up; may sign **only** when all five PSSR items are closed with evidence | **Not signed — start-up authorisation withheld** |

This package records role labels only. No personal name, contact detail, or address appears in this document, and it embeds no re-identification key or name-to-label mapping. The re-identification key is held in a separate, access-controlled artifact; keep it apart from this document and restrict access to those who need it.

---

## 11. Regulatory and standards basis

- **KB-STD-PSM** — process safety management framework: element (l) Management of Change (technical basis, safety and health impacts, temporary-change time limits, PSI and procedure updates, training before start-up) and element (i) Pre-Start-Up Safety Review. This package is structured directly on those two elements.
- **ISO 45001 clause 8.1.3** (management of change) — jurisdiction-independent management-system anchor for planned temporary and permanent changes.
- **KB-REG-US-OSHA** — OSHA 29 CFR 1910.119(l) applies **only if** the facility is a US-covered process. [GAP — jurisdiction not supplied; confirm the facility's jurisdiction before relying on any statutory citation. No other national law is cited in this package for that reason.]
- **KB-SNIP-HOC** — hierarchy of controls, applied to every control set in Section 4.

---

## 12. Assumptions and gaps register

| Ref | Type | Item | Consequence until closed |
|---|---|---|---|
| G1 | [GAP] | Site MoC register number not supplied | Assign before circulation |
| G2 | [GAP] | Technical basis — all six Section 3 fields | MoC cannot pass review; PSSR cannot convene |
| G3 | [GAP] | Replacement-valve specification vs. relief design basis | Classification unresolved; possible escalation to significant change (Section 2) |
| G4 | [GAP] | Jurisdiction / statutory hook | Statutory citations withheld pending confirmation (Section 11) |
| G5 | [GAP] | Shutdown vs. in-service replacement strategy | Possible unassessed temporary relief impairment (action A7) |
| G6 | [GAP] | Evidence for PSSR items 2–5 | Items held open; start-up blocked |
| G7 | [GAP] | Custody of the affected PSI documents (Section 6) | Update ownership unconfirmed |
| A-1 | [ASSUMPTION] | Treated as a change under MoC, not replacement-in-kind | Revisit via action A2 |
| A-2 | [ASSUMPTION] | Change treated as permanent | Revisit if any temporary condition is proposed |
| A-3 | [ASSUMPTION] | Scored on the pack's standard 5×5 matrix | Re-map to the site's calibrated matrix at review |
| A-4 | [ASSUMPTION] | Sector treated as process (covered process unit) | Confirm sector at review |
| A-5 | [ASSUMPTION] | All action due dates are proposed | Change Owner (role) confirms dates |

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*

---

**Limitations.** This Management of Change package is decision-support only. It must be reviewed, completed, and approved by a competent person before use; it is not legal advice, and nothing in it constitutes or substitutes for the site's own engineering judgment or statutory obligations. **No start-up authorisation is granted by this document** — start-up may be authorised only by the accountable PSSR role after every PSSR item passes with evidence.
