# HIRA — Confined-Space Entry, Tank T-402 (Plant 3, Maharashtra)

**Assessment type:** Baseline (first formal HIRA for this tank).
**Activity:** Confined-space entry to clean tank T-402 — isolate -> purge -> gas-test -> enter -> clean -> exit.
**Site:** Plant 3, tank farm, bay 2. **Jurisdiction:** India — Maharashtra. **Industry:** Chemicals / manufacturing.
**Exposed parties:** Own workers (the authorised entrant, the standby attendant) + the contractor cleaning crew.
**Scoring engine:** org 5x5 matrix (multiply, score 1-25; bands Low 1-4 / Medium 5-9 / High 10-15 / Critical 16-25), per `risk_matrix.score`.
**Standard basis:** planning of controls per ISO 45001 clause 6.1.2 (actions to address risks and opportunities). State statutory record resolved via KB-REG-IN-STATEFORMS for Maharashtra — no national form number is asserted.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before use. Not legal advice.

## 1. De-identification status
De-id pass ran FIRST. No personal identifiers were present in the intake; all personnel are carried as role labels only (the entrant, the standby attendant, the contractor cleaning crew, Plant Manager, Maintenance Lead). No names, contact details, IDs, addresses, or small injury cells appear in this record.

## 2. Hazard identification (per task step)

| # | Step | Hazard | Mechanism |
|---|------|--------|-----------|
| H1 | Purge | Oxygen deficiency | Nitrogen purge displaces O2 in the tank; asphyxiation on entry to an un-tested atmosphere. |
| H2 | Gas-test / Enter | Residual hydrocarbon vapour | Flammable / toxic vapour from incompletely purged product; fire / toxic exposure. |
| H3 | Clean | Engulfment by residual sludge | Entrant sinks / is trapped in settled sludge at the tank base. |

[ASSUMPTION] Tank previously held a hydrocarbon product; confirm last-contained substance from the tank log before entry — recorded as action A1.
[GAP] Intake did not state whether a rescue tripod/winch is available; treated as absent until verified (action A2).

## 3. Initial risk score (pre-control, existing controls only)

Existing controls credited: generic confined-space permit, portable single-gas O2 monitor, supplied-air on request.

| Hazard | Likelihood | Severity | Score (L x S) | Band | Band action |
|--------|-----------|----------|---------------|------|-------------|
| H1 Oxygen deficiency | 4 (Likely) | 5 (Catastrophic) | 20 | Critical | Intolerable — work must not start or continue until risk is reduced |
| H2 Hydrocarbon vapour | 3 (Possible) | 5 (Catastrophic) | 15 | High | Intolerable — stop / additional controls before proceeding |
| H3 Engulfment | 3 (Possible) | 4 (Major) | 12 | High | Intolerable — stop / additional controls before proceeding |

## 4. Ranked controls — full hierarchy of controls

Controls ranked highest-order first (Elimination -> Substitution -> Engineering -> Administrative -> PPE) per KB-SNIP-HOC; each control is tier-tagged and tied to a named hazard. Each hazard carries at least one Engineering-or-higher control.

### H1 — Oxygen deficiency
| Tier | Control |
|------|---------|
| Elimination | Where the cleaning method allows, clean-in-place / no-entry external lance so no human enters the tank atmosphere (eliminate the entry). |
| Substitution | Substitute a breathable-air sweep for the inert nitrogen purge once the LEL is cleared, so the residual atmosphere trends to normoxic rather than inert. |
| Engineering | Continuous forced-air ventilation of the tank during entry + a fixed multi-gas (O2/LEL/toxic) monitor with audible alarm at the entry. |
| Administrative | Confined-space entry permit specific to T-402; standby attendant at the manway; entrant/attendant briefed on the inert-atmosphere hazard. |
| PPE | Supplied-air breathing apparatus (SABA) for the entrant as the last line, not the primary control. |

### H2 — Residual hydrocarbon vapour
| Tier | Control |
|------|---------|
| Elimination | No-entry external cleaning removes exposure to the vapour entirely (shared with H1). |
| Substitution | Replace the residual-product solvent wash with a lower-volatility / lower-hazard cleaning agent for the sludge removal step. |
| Engineering | Pre-entry gas-test to <10% LEL with the fixed multi-gas monitor; mechanical extraction at the manway; bonding/earthing of equipment to remove ignition sources. |
| Administrative | Hot-work prohibition during entry; gas-test record signed before each entry and re-tested after any break. |
| PPE | Appropriate respiratory protection where transient vapour cannot be fully engineered out. |

### H3 — Engulfment by sludge
| Tier | Control |
|------|---------|
| Engineering | Remove bulk sludge by external vacuum tanker BEFORE any entry; rescue tripod/winch + full-body harness rigged at the manway for retrieval. |
| Administrative | Limit the depth of manual cleaning per entry; attendant maintains continuous voice/visual contact; non-entry rescue plan rehearsed. |
| PPE | Full-body harness with retrieval line (engineering-assisted PPE for rescue). |

No hazard is PPE-only; every hazard has an Engineering-or-higher control, so `controls.ppe_admin_only` clears for this assessment.

## 5. Residual risk (post-control re-score) — initial -> residual movement

| Hazard | Initial score / band | Residual score / band | Movement |
|--------|----------------------|------------------------|----------|
| H1 Oxygen deficiency | 20 Critical | L2 x S5 = 10 High | Critical -> High (further controls + permit hold until A1/A2 closed before entry) |
| H2 Hydrocarbon vapour | 15 High | L2 x S4 = 8 Medium | High -> Medium (ALARP after gas-test + extraction) |
| H3 Engulfment | 12 High | L2 x S3 = 6 Medium | High -> Medium (ALARP after external de-sludge + retrieval rig) |

Residual scoring uses the same `risk_matrix.score` engine; deltas are risk scores, not injury counts. Entry remains gated until the Critical->High actions (A1, A2, A3) are verified complete.

## 6. SMART actions (defensible — named role-label owner + ISO due date + hazard link + review trigger)

| ID | Action | Hazard | Owner (role label) | Due (ISO) | Review trigger |
|----|--------|--------|--------------------|-----------|----------------|
| A1 | Confirm last-contained substance from the tank log; update the entry permit | H1, H2 | Maintenance Lead | 15 Aug 2026 | Before first entry; re-review on product change |
| A2 | Procure & rig rescue tripod/winch + retrieval harness at the T-402 manway | H1, H3 | Plant Manager | 22 Aug 2026 | Before first entry; annual rescue-equipment inspection |
| A3 | Install fixed multi-gas (O2/LEL/toxic) monitor + forced-air ventilation at the entry | H1, H2 | Maintenance Lead | 31 Aug 2026 | Before first entry; on monitor calibration lapse |
| A4 | Trial external no-entry cleaning method to eliminate routine entry | H1, H2, H3 | Plant Manager | 30 Sep 2026 | Method-feasibility review |
| A5 | Issue T-402-specific confined-space entry permit + brief entrant/attendant | H1, H2, H3 | Plant Manager | 31 Aug 2026 | Each entry; on procedure change |

## 7. Branded report
A branded `report.json` is emitted and rendered to DOCX + PDF via the report engine (`generate_report.py --formats docx,pdf`), using the site `brand.yaml` (Eyekyam default where unset). The aspects above populate the HIRA register section; the SMART-action table populates the action-tracker section.

## 8. Review
Whole-assessment review trigger: before first entry, on any change to the contained substance or cleaning method, and at 12 months — whichever is first. Competent-person sign-off required prior to circulation.
