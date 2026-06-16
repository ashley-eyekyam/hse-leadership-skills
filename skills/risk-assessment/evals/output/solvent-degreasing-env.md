# Environmental Aspects & Impacts Register — Solvent Degreasing Line, Plant 3

**Assessment type:** Baseline (Q0 = Both — environmental aspects branch alongside safety scope).
**Activity:** Operating the solvent degreasing line at Plant 3 — load part -> spray degrease -> drain -> dry, using a chlorinated solvent.
**Site:** Plant 3, surface-finishing area. **Jurisdiction:** UK. **Industry:** Manufacturing — surface finishing.
**Operating conditions assessed:** Normal (production spraying) + Abnormal (maintenance drain-down / tank change-out).
**Scoring engine:** the SAME org 5x5 matrix and `risk_matrix.score` engine used for safety — read against environmental consequence descriptors (scale/extent of release, reversibility, duration). No engine fork.
**Standard basis:** environmental aspects determined and significance evaluated per ISO 14001 clause 6.1.2 (environmental aspects). Cross-reference KB-STD-ISO14001 for the clause-to-artifact map.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before use. Not legal advice.

## 1. De-identification status
De-id pass ran FIRST. No personal identifiers present; personnel are carried as role labels only (the line operators, Plant Manager, Environmental Lead, Maintenance Lead).

## 2. Aspect -> impact identification (ISO 14001 clause 6.1.2)

| # | Activity step | Environmental aspect | Associated impact | Condition |
|---|---------------|----------------------|-------------------|-----------|
| E1 | Spray + dry | VOC / chlorinated-solvent vapour emission to air | Air-quality degradation; photochemical-smog (ozone) precursor; permit VOC-limit exceedance | Normal |
| E2 | Drain | Spent solvent + rinse water released to the works drain | Water contamination; trade-effluent consent breach; aquatic toxicity | Normal + Abnormal |
| E3 | Drain-down / tank change-out | Bulk spent-solvent release during maintenance | Acute water/soil contamination; consent breach | Abnormal |

[GAP] Measured VOC mass-emission rate and effluent solvent concentration not supplied in the intake; significance scored on the worst-credible release pending monitoring data (action E-A1). [ASSUMPTION] The site holds a VOC permit limit and a trade-effluent discharge consent (per intake Q-E5); both treated as binding compliance obligations.

## 3. Initial significance (pre-control)

Scored with `risk_matrix.score`, reading Likelihood as probability/frequency of the release and Severity as environmental consequence (scale x reversibility x duration).

| Aspect | Likelihood | Severity | Score (L x S) | Band | Band action |
|--------|-----------|----------|---------------|------|-------------|
| E1 VOC to air (normal) | 4 (Likely) | 3 (Moderate) | 12 | High | Intolerable — stop / additional controls before proceeding |
| E2 Spent solvent to water (normal) | 3 (Possible) | 4 (Major) | 12 | High | Intolerable — stop / additional controls before proceeding |
| E3 Bulk release (abnormal drain-down) | 2 (Unlikely) | 5 (Catastrophic) | 10 | High | Intolerable — stop / additional controls before proceeding |

## 4. Ranked controls — full hierarchy of controls applied to the aspect

Controls ranked highest-order first (Elimination -> Substitution -> Engineering -> Administrative -> PPE) per KB-SNIP-HOC; each is tier-tagged and tied to a named aspect. Each aspect carries at least one Elimination/Substitution/Engineering control — this is NOT a PPE/admin-only treatment.

### E1 — VOC / solvent vapour to air
| Tier | Control |
|------|---------|
| Elimination | Eliminate solvent vapour at source by moving the highest-volume parts to a no-solvent process (mechanical/ultrasonic aqueous clean), removing the VOC aspect for those jobs. |
| Substitution | Substitute an aqueous (water-based) degreaser or a low-VOC modified-alcohol solvent for the chlorinated solvent. |
| Engineering | Enclose the degreasing line and route extraction through carbon-adsorption / VOC abatement (activated-carbon capture) before discharge; freeboard chiller + lip extraction on any retained solvent tank. |
| Administrative | Permit-tracking of VOC mass emission; lid-closed-when-idle procedure; operator training on emission minimisation. |
| PPE | Respiratory protection for operators — occupational control, not an environmental-emission control (recorded under the safety scope). |

### E2 — Spent solvent to water
| Tier | Control |
|------|---------|
| Substitution | Aqueous degreaser whose effluent is consent-compliant, replacing the chlorinated-solvent waste stream. |
| Engineering | Close-loop the solvent: on-site distillation/reclaim so spent solvent is recovered, not discharged; bunded collection; interceptor + isolation valve on the works drain to prevent solvent reaching water. |
| Administrative | Spent-solvent routed to licensed hazardous-waste contractor under consignment; drain-isolation procedure; effluent sampling against the trade-effluent consent. |
| PPE | (Not applicable as an environmental control.) |

### E3 — Bulk release during abnormal drain-down
| Tier | Control |
|------|---------|
| Engineering | Bunded drain-down to a dedicated closed receiver sized for the full tank volume; spill containment with secondary bund; emergency drain-isolation valve. |
| Administrative | Maintenance drain-down permit; spill-response plan + absorbent kit staged at the line; pre-task containment check. |

`controls.ppe_admin_only` clears for every aspect: each has an Elimination/Substitution/Engineering control.

## 5. Residual significance (post-control re-score) — initial -> residual movement

| Aspect | Initial score / band | Residual score / band | Movement |
|--------|----------------------|------------------------|----------|
| E1 VOC to air | 12 High | L2 x S2 = 4 Low | High -> Low (substitution to aqueous + carbon-capture cuts VOC at source) |
| E2 Spent solvent to water | 12 High | L2 x S3 = 6 Medium | High -> Medium (close-loop reclaim + drain isolation; ALARP, residual held by consignment + sampling) |
| E3 Bulk abnormal release | 10 High | L1 x S5 = 5 Medium | High -> Medium (bunded closed-receiver drain-down + spill response; low likelihood, contained) |

Residual scoring uses the same `risk_matrix.score` engine; values are significance scores (band movement), not release counts.

## 6. SMART actions (defensible — named role-label owner + ISO due date + aspect link + review trigger)

| ID | Action | Aspect | Owner (role label) | Due (ISO) | Review trigger |
|----|--------|--------|--------------------|-----------|----------------|
| E-A1 | Commission VOC stack monitoring + effluent solvent sampling to quantify emissions | E1, E2 | Environmental Lead | 31 Aug 2026 | On process change; annual permit review |
| E-A2 | Trial & qualify an aqueous / low-VOC substitute degreaser | E1, E2 | Environmental Lead | 31 Oct 2026 | Substitution-feasibility review |
| E-A3 | Install enclosure + carbon-capture VOC abatement on the line | E1 | Maintenance Lead | 30 Nov 2026 | Post-install emission verification |
| E-A4 | Install close-loop solvent reclaim + works-drain isolation/interceptor | E2 | Maintenance Lead | 30 Nov 2026 | Effluent consent sampling |
| E-A5 | Provide bunded closed-receiver drain-down + spill-response kit for maintenance | E3 | Plant Manager | 30 Sep 2026 | Each drain-down permit; annual drill |

## 7. Environmental aspects/impacts register (report section)
This artifact IS the environmental aspects/impacts register section that the branded report carries: aspect -> impact pairs (section 2), significance scoring on the shared 5x5 engine (sections 3 & 5), ranked controls (section 4), and tracked actions (section 6). A branded `report.json` is emitted and rendered to DOCX + PDF (`generate_report.py --formats docx,pdf`) using the site `brand.yaml` (Eyekyam default where unset).

## 8. Review
Review trigger: on completion of E-A2/E-A3/E-A4 (post-install verification), on any process or solvent change, on permit/consent renewal, and at 12 months. Competent-person sign-off required before circulation.
