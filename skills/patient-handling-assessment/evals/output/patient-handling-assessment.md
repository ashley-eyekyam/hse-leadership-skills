# Patient Handling (Moving & Handling of People) Assessment — Bed-to-Chair Transfer, Rehab Ward

*Decision-support only. A competent person (moving-and-handling / ergonomics specialist) must review
and sign off this assessment. The patient is assessed by de-identified mobility / dependency / weight
band only; the worker's capability is assessed by role with any fitness / back-condition record held
confidentially and separately; the re-identification key is held separately and is not part of this
document.*

## 1. Care task & setting

De-identification ran first: the patient's name, ward/bay, MRN, and diagnosis, and the handler's name,
phone, and back-condition occupational-health record were scrubbed; the patient is assessed by
mobility/dependency only and the handler by role; no named individual, ward/bay, diagnosis, or `<5`
injury cell appears below.

- **Care task:** bed-to-chair transfer + in-bed repositioning, rehab ward (task-specific — not
  "moving patients").
- **Patient (de-identified):** fully dependent, non-weight-bearing, standard weight band, limited
  cooperation, one IV line attachment.
- **Proposed control (as received):** "two staff lift the patient across, use good lifting technique,
  handlers wear back belts". This is assessed against the avoid-first hierarchy below.

## 2. Lift-avoidance decision (recorded FIRST — the primary control)

The hazardous manual lift **CAN be avoided** — a ceiling-track hoist with the matched sling is
substituted for the full transfer, and a slide sheet for in-bed repositioning. Avoiding the manual
lift is the primary control (MHOR reg 4(1)(a) avoid; ANA SPHM / NIOSH move-toward-zero); the mechanical
aid controls the residual handling. The "two staff lift" instruction is **REJECTED** — a manual lift
is not used where a hoist is reasonably available.

## 3. Avoid-first / control gate (the move-toward-zero lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "two staff
lift + good technique + back belts" is a **manual lift recommended where a mechanical aid is reasonably
available, plus a technique/PPE-led treatment** — it is a **CONTROLS FLAG** (`ppe_admin_only=True`)
**pushed up the hierarchy**. Technique and PPE (a back belt) are the documented last lines, never the
headline control.

| Proposed / existing control | Gate outcome |
|---|---|
| "Two staff lift + good lifting technique + back belts" | **FLAG — manual lift where a hoist is available + technique/PPE-led.** Pushed up the hierarchy: avoid the manual lift and use the ceiling-track hoist first; the back belt is a residual measure only. |

## 4. TILE assessment (Task / Individual / Load / Environment)

| TILE element | Assessment (de-identified) |
|---|---|
| Task | Bed-to-chair transfer + in-bed repositioning; low frequency per shift; static-posture hold risk during positioning; twisting and reaching to be minimised |
| Individual | Two trained, hoist-competent handlers (assessed by role; capability recorded without any name or fitness/back-condition record) |
| Load | Patient by mobility/dependency: fully dependent, non-weight-bearing, limited cooperation, standard weight band, one line attachment (de-identified — no name/diagnosis) |
| Environment | Adequate floor space; ceiling-track hoist available over the bed; bed/chair height adjustable; clear transfer path |

All four elements are assessed — a TILE assessment missing any element is not suitable and sufficient.

## 5. Mobility-and-equipment matrix (dependency level → equipment + handler count)

| Mobility / dependency level | Matched equipment | Handlers | Manual lift? |
|---|---|---|---|
| Independent / supervision only | Stand-by assist; grab rails | 1 | No — no handling required |
| Minimal assist (weight-bearing) | Stand-aid / sit-to-stand hoist; transfer belt (guide only) | 1 | No — mechanical aid |
| Moderate assist (partial weight-bearing) | Active/standing hoist with sling; slide sheet | 1–2 | No — mechanical aid |
| Fully dependent (non weight-bearing) | Mobile or ceiling-track passive hoist + matched sling; slide sheet | 2 | No — hoist; manual lift NOT used |
| Bariatric / fully dependent | Bariatric-rated hoist (verified SWL); bariatric sling; lateral-transfer aid | 2+ | No — bariatric-rated hoist; SWL verified |
| Falls recovery (on floor) | Mobile hoist + floor-recovery sling or inflatable lifting cushion | 2 | No — mechanical floor-recovery aid |

The matrix is the core artifact: each dependency level maps to the matched mechanical aid and handler
count; a manual lift is not recommended where a mechanical aid is reasonably available.

## 6. Hierarchy-ranked controls (eliminate manual lift → mechanical aids → safe systems → technique/PPE last)

| Control | Tier | Owner (role) |
|---|---|---|
| Eliminate the manual lift — ceiling-track hoist + matched sling for the transfer; slide sheet for repositioning | Elimination | Moving-and-Handling Lead |
| Maintained, SWL-verified hoist + sling inventory; adjustable bed/chair; ceiling-track coverage over the bed | Engineering | Estates Lead |
| Safe system of work for the transfer; hoist/sling competency training; the mobility-and-equipment matrix posted at point of care | Administrative | Ward Manager |
| Handling technique + back-care guidance as the residual last line (never the primary control) | PPE | Occupational Health / Back-Care Advisor |

## 7. Bariatric / falls plan

- **Bariatric:** verify the hoist + sling safe-working-load (SWL) against the patient's weight band;
  check environmental floor / ceiling-track loading; allow extended planning time and additional
  handlers.
- **Falls:** a post-fall handling plan uses a mechanical floor-recovery aid (mobile hoist + floor-
  recovery sling or inflatable lifting cushion) — never a manual lift from the floor.

## 8. Handling-injury context (de-identified / aggregated)

Moving-and-handling injuries on the ward this period are reported by area, not by individual:
the total is aggregated to `≥ 5`, with categories of fewer than five suppressed and secondary
suppression applied so a suppressed cell cannot be back-calculated from totals. Individual handler
hoist-competency and any back-condition record are held confidentially and never circulated.

## 9. Residual risk

After avoiding the manual lift (ceiling-track hoist + slide sheet), SWL-verified equipment, the safe
system of work, and competency training, the residual moving-and-handling risk is framed via
`risk_matrix` as **Low–Medium**, with handling technique / back-care as the last line.

## 10. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Confirm ceiling-track hoist coverage + matched sling inventory over the transfer bed; verify SWL | P1 | Estates Lead | 2026-07-15 |
| Withdraw the manual-lift instruction; post the mobility-and-equipment matrix at point of care | P1 | Moving-and-Handling Lead | 2026-07-10 |
| Refresh hoist/sling competency training for the ward handlers | P2 | Ward Manager | 2026-09-30 |
| Verify the bariatric SWL + falls floor-recovery plan are in place and tested | P2 | Occupational Health / Back-Care Advisor | 2026-08-31 |

## 11. Assumptions, gaps & sign-off

- Handling-injury counts taken from the de-identified moving-and-handling record; categories of fewer
  than five are suppressed — a missing figure is a `[GAP]`, never invented.
- India site (if applicable): state factory/occupational-ergonomics provision owed — `[GAP]` (resolve
  the state via `hse-india`; no national form number minted).
- **Regulatory basis:** UK Manual Handling Operations Regulations 1992 (reg 4(1)(a) avoid → 4(1)(b)(i)
  assess (Schedule 1 TILE) → 4(1)(b)(ii) reduce → 4(2) review); ANA SPHM (2021) 8 standards +
  move-toward-zero; NIOSH safe-lifting guidance; ISO/TR 12296:2012; ISO 45001 §6.1.2.
- Review trigger: annual / on-change-of-task-or-patient / on-incident — whichever is first.
- Decision-support only — a competent person (moving-and-handling / ergonomics specialist) must review
  before use.
