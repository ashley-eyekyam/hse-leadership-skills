# Sharps & Needlestick Management — Phlebotomy Round, Day-Ward 4B

*Decision-support only. A competent person (occupational-health / infection-control professional)
must review and sign off this plan. The source patient is referenced by role only; the injured
worker's exposure / PEP medical record is held confidentially and separately; the re-identification /
exposure key is held separately and is not part of this document.*

## 1. Service & sharps inventory

De-identification ran first: the injured worker's name and phone, the source patient's identity and
serostatus, and the worker's PEP medical record were scrubbed to role level; no named worker, no
source-patient serostatus, and no `<5` injury cell appears below.

- **Service:** phlebotomy round, Day-Ward 4B (service-specific — not "a clinic").
- **Sharps in use:** hollow-bore venepuncture needles, winged blood-collection sets, IV cannulae,
  lancets.
- **Proposed control (as received):** "tell staff to take care and wear gloves, and recap the needle
  before binning it". This is assessed against the engineering-first hierarchy below.

## 2. Elimination/substitution decision (recorded FIRST — the primary control)

Unnecessary sharps **CAN be eliminated** — needle-free connectors are substituted on the IV lines,
and recapping by hand is **banned**. Eliminating the sharp is the primary control; the
safety-engineered device controls only the residual sharps that genuinely remain. The "recap before
binning" instruction is **REJECTED** — recapping by hand is not permitted.

## 3. Engineering / control gate (the engineering-first lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "tell staff
to take care and wear gloves" is a **behaviour-led / PPE-led treatment of sharps that could be
eliminated or engineered out** — it is a **CONTROLS FLAG** (`ppe_admin_only=True`) **pushed up the
hierarchy**. PPE and PEP are the documented last lines, never the headline control.

| Proposed / existing control | Gate outcome |
|---|---|
| "Tell staff to take care and wear gloves; recap before binning" | **FLAG — behaviour/PPE-led + recapping by hand.** Pushed up the hierarchy: eliminate unnecessary sharps and fit safety-engineered devices first; recapping by hand is REJECTED. |

## 4. Hierarchy-ranked controls (eliminate → safety-engineered devices → work practices → PPE/PEP last)

| Control | Tier | Owner (role) |
|---|---|---|
| Eliminate unnecessary sharps — needle-free connectors on IV lines; ban recapping by hand | Elimination | IPC Lead |
| Safety-engineered venepuncture needles + winged sets (integrated sharps-injury protection) | Engineering | Procurement Lead |
| Point-of-use sharps containers (fill line marked); no-recapping rule; single-handed scoop where re-sheathing is by design | Administrative | Ward Manager |
| Gloves / eye protection + the confidential PEP pathway (residual last line) | PPE | Occupational Health Lead |

## 5. Documented safer-device consideration (frontline-worker involvement)

| Device | Safety-engineered? | Frontline-input / justification |
|---|---|---|
| Venepuncture needles | Yes — retractable | Selected by the phlebotomy team trial (non-managerial frontline input) |
| Winged blood-collection sets | Yes — shielded | Adopted after frontline evaluation |
| IV cannulae | Yes — passive safety | Frontline evaluation; needle-free connectors substituted on lines |
| Lancets | Yes — single-use auto-retract | Non-engineered alternative withdrawn (no recorded justification to retain) |

The **annual safer-device evaluation with non-managerial frontline-worker input** is recorded (OSHA
1910.1030(c)(1)(iv) / Needlestick Act).

## 6. Sharps Injury Log structure (de-identified / aggregated — OSHA 1910.1030(h)(5))

| Device type | Brand class | Work area | How it occurred | Cases (aggregated) |
|---|---|---|---|---|
| Hollow-bore needle | Conventional (pre-changeover) | Phlebotomy | During / after blood draw | aggregated ≥ 5 |
| Winged set | Conventional (pre-changeover) | Phlebotomy | After use, before disposal | aggregated ≥ 5 |
| IV cannula | Conventional (pre-changeover) | Ward | During insertion / removal | small cells < 5 suppressed |
| Suture needle | Mixed | Minor procedures | Handling / disposal | small cells < 5 suppressed |
| Lancet | Mixed | Ward | Disposal | small cells < 5 suppressed |

The circulated log is structural / aggregated, never line-level. Categories of fewer than five are
suppressed, with secondary suppression so a suppressed cell cannot be back-calculated from totals.

## 7. Confidential post-exposure (PEP) pathway

The source patient is referenced **by role only**; source-patient testing is performed **with
consent**; the injured worker's exposure / PEP medical record is held confidentially and **separately**
(OSHA 1910.1030(f)). No source patient or worker is named here.

- **First aid** — encourage bleeding, wash with soap and water, irrigate mucous membranes / eyes.
- **Confidential report** — logged to the de-identified Sharps Injury Log; the worker is a role label.
- **Consented source-patient testing** — "the source patient" by role only; the serostatus result is
  held in a separate confidential record, never circulated.
- **PEP** — HBV (vaccination-status check + immunoglobulin/booster per protocol), HCV (baseline +
  follow-up testing), HIV (risk-assess + PEP within the protocol window where indicated).
- **Follow-up** — the confidential occupational-health follow-up schedule, held separately.

## 8. HBV-vaccination status

Hepatitis-B vaccination is offered to all staff with occupational sharps exposure (OSHA
1910.1030(f)); uptake is reported in aggregate only. Individual vaccination / serostatus is
special-category health data — held confidentially, never circulated.

## 9. Residual risk

After elimination (needle-free IV connectors), safety-engineered devices, point-of-use disposal, and
the no-recapping rule, the residual sharps-exposure risk is framed via `risk_matrix` as **Low–Medium**,
with the confidential PEP pathway as the last line.

## 10. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Complete the changeover to safety-engineered venepuncture needles + winged sets | P1 | Procurement Lead | 2026-07-15 |
| Withdraw the non-engineered lancet; document the safer-device decision with frontline input | P1 | IPC Lead | 2026-07-10 |
| Run the annual safer-device evaluation with non-managerial frontline-worker input | P2 | Occupational Health Lead | 2026-09-30 |
| Verify the confidential PEP pathway + HBV-vaccination offer are in place and tested | P2 | Occupational Health Lead | 2026-08-31 |

## 11. Assumptions, gaps & sign-off

- Sharps-injury counts taken from the de-identified Sharps Injury Log; categories of fewer than five
  are suppressed — a missing figure is a `[GAP]`, never invented.
- India site (if applicable): state biomedical-waste sharps-segregation return owed — `[GAP]`
  (resolve the state via `hse-india`; BMW Rules 2016; no national form number minted).
- **Regulatory basis:** OSHA 29 CFR 1910.1030 ((c) / (c)(1)(iv) / (d)(2) / (f) / (h)(5)) + the
  Needlestick Safety and Prevention Act; EU Directive 2010/32/EU + the UK Sharps Regulations 2013
  with COSHH; India BMW Rules 2016 via `hse-india`; ISO 45001 §6.1.2.
- Review trigger: annual safer-device review / on-device-change / on-incident — whichever is first.
- Decision-support only — a competent person (occupational-health / infection-control professional)
  must review before use.
