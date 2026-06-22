<!-- CANDIDATE golden output for workplace-violence-prevention (HC-04). Generated from eval case 1's
     scenario (emergency department, evening/overnight reception & triage). It demonstrates the core
     lever: environmental-and-administrative-before-reactive + the hierarchy. The security manager's
     proposed control -- "issue the triage nurses personal alarms and run a self-defence training
     day" -- is a reactive-led treatment of an exposure that could be designed out; it is FLAGGED and
     PUSHED UP the hierarchy (record the worksite analysis + design out the exposure with controlled
     access, sightlines, duress alarms, and staffing first). PHI is the highest tier: any victim,
     assailant, or known-risk patient is referenced by role only, behavioural-health flags are held
     separately, and the WPV incident log is de-identified / aggregated with <5 categories suppressed.
     NOT owner-LOCKED -- the owner reviews + locks in P17. -->

# Workplace-Violence Prevention Program — Emergency Department

*Decision-support only. A competent person (healthcare-security / WPV / occupational-health
professional) must review and sign off this program. No victim, assailant, or known-risk patient is
named; any behavioural-health flag is held confidentially and separately; the re-identification key is
held separately and is not part of this document.*

## 1. Service & exposure

De-identification ran first: the injured worker's name and phone, the assailant patient's identity,
and the behavioural-health flag were scrubbed to role level; no named victim, assailant, or known-risk
patient, no behavioural-health flag, and no `<5` incident cell appears below.

- **Service:** emergency department, evening / overnight reception & triage (service-specific — not
  "a hospital").
- **Exposure:** verbal and physical aggression from patients and visitors at reception / triage.
- **Proposed control (as received):** "issue the triage nurses personal alarms and run a self-defence
  training day". This is assessed against the environmental-and-administrative-first hierarchy below.

## 2. Violence-type taxonomy (type 1-4 — each type drives its control set)

| Type | Aggressor relationship | ED context | Lead control set |
|---|---|---|---|
| Type 1 — Criminal intent | No legitimate relationship to the workplace | Robbery / intrusion at reception | Controlled access, secure design, alarm / duress |
| Type 2 — Customer / patient / client | Receiving a service | Patient / visitor aggression (the dominant type) | Triage sightlines, staffing / skill-mix, de-identified flagging, de-escalation |
| Type 3 — Worker-on-worker | Current / former employee | Internal conflict / bullying | Behavioural standards, no-retaliation reporting |
| Type 4 — Personal relationship | Personal relationship, not the workplace | Domestic violence spilling into work | Access control, workplace safety planning |

Type 2 (patient / visitor) and type 1 (criminal-intent at reception) are in scope for this service.

## 3. Worksite hazard analysis (recorded FIRST — the basis of every control; de-identified)

The worksite analysis draws on the de-identified, aggregated incident log, a walkthrough, and a staff
survey — never a named victim or assailant. A program with no worksite analysis fails.

| High-risk area / task | Source (de-identified) | Findings (walkthrough + survey) | Type |
|---|---|---|---|
| Reception / triage (evening-overnight) | Aggregated incident review + survey | Open desk, no barrier, poor sightlines to waiting area; no duress alarm | Type 2 / Type 1 |
| Waiting area | Aggregated incident review | Crowding + long waits driving verbal aggression; no de-escalation prompts | Type 2 |
| Lone clinical assessment rooms | Staff survey | No line-of-sight, no personal duress, single-staff assessment | Type 2 |
| Ambulance handover bay | Walkthrough | Uncontrolled external access after hours | Type 1 |
| Discharge / car-park route | Staff survey | Lone-working risk on late-shift egress | Type 4 |

## 4. Control gate (the environmental-and-administrative-first lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "issue
personal alarms and run a self-defence training day" is a **reactive-led treatment of an exposure that
could be designed out** — it is a **CONTROLS FLAG** (`ppe_admin_only=True`) **pushed up the
hierarchy**. De-escalation, response training, and personal alarms are the documented last lines,
never the headline control.

| Proposed / existing control | Gate outcome |
|---|---|
| "Issue personal alarms; run a self-defence training day" | **FLAG — reactive-led, no environmental or administrative control.** Pushed up the hierarchy: record the worksite analysis and design out the exposure (controlled access, triage sightlines, duress alarms, staffing) first; personal alarms / training are the residual last line. |

## 5. Hierarchy-ranked controls (worksite analysis → environmental → administrative → reactive last)

| Control | Tier | Owner (role) |
|---|---|---|
| Substitute the exposure where possible — control after-hours external / ambulance-bay access | Substitution | Facilities Lead |
| Environmental — reception barrier + improved triage sightlines, duress / panic alarms, CCTV, waiting-area / queue redesign | Engineering | Estates & Security Lead |
| Administrative — peak staffing / skill-mix, lone-working procedure (assessment rooms + late-shift egress), de-identified known-risk-patient flagging, no-retaliation reporting | Administrative | ED Nurse Manager |
| De-escalation & response training, response team, post-incident support, personal alarms (residual last line) | PPE | WPV Program Lead |

## 6. De-escalation, response & training (residual lines)

- **De-escalation procedure** — recognition of escalation cues, verbal de-escalation, environmental
  separation; trained to all front-of-house staff.
- **Response protocol** — duress activation → response team → security escalation → safe withdrawal;
  rehearsed.
- **Post-incident support** — confidential debrief, occupational-health / EAP referral,
  no-retaliation, return-to-work support.
- **Training plan** — WPV awareness, type-1-4 recognition, de-escalation, reporting; refreshed
  annually with employee involvement (OSHA 3148 element 4).

## 7. Confidential WPV incident log structure (de-identified / aggregated — OSHA 3148 element 5 / Cal-OSHA 8 CCR 3342)

| Type | Location (area) | Antecedents | Controls in place | Cases (aggregated) |
|---|---|---|---|---|
| Type 2 — patient / visitor | Reception / triage | Long wait + intoxication | Pre-changeover open desk | aggregated ≥ 5 |
| Type 2 — patient / visitor | Waiting area | Crowding | Pre-changeover queue design | aggregated ≥ 5 |
| Type 1 — criminal-intent | Ambulance bay | After-hours access | Uncontrolled (pre-changeover) | small cells < 5 suppressed |
| Type 4 — personal-relationship | Discharge route | Lone late-shift egress | No lone-working procedure | small cells < 5 suppressed |

The circulated log is structural / aggregated, never line-level. Categories of fewer than five are
suppressed, with secondary suppression so a suppressed cell cannot be back-calculated from totals.

## 8. Residual risk

After substitution (controlled external access), environmental controls (reception barrier, triage
sightlines, duress alarms, CCTV, queue redesign), and administrative controls (peak staffing,
lone-working procedure, de-identified flagging), the residual violence risk is framed via
`risk_matrix` as **Low–Medium**, with de-escalation / response training and personal alarms as the
last line.

## 9. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Install the reception barrier + duress alarms and improve triage sightlines | P1 | Estates & Security Lead | 2026-08-15 |
| Control after-hours ambulance-bay / external access | P1 | Facilities Lead | 2026-07-31 |
| Implement the lone-working procedure for assessment rooms + late-shift egress | P1 | ED Nurse Manager | 2026-07-20 |
| Deliver de-escalation & response training with employee involvement; stand up the confidential WPV incident log | P2 | WPV Program Lead | 2026-09-30 |

## 10. Assumptions, gaps & sign-off

- WPV incident counts taken from the de-identified, aggregated incident log; categories of fewer than
  five are suppressed — a missing figure is a `[GAP]`, never invented.
- India site (if applicable): state occupational-safety return owed — `[GAP]` (resolve the state via
  `hse-india`; no national form number minted).
- **Regulatory basis:** OSHA Publication 3148 (2016) five program elements (management commitment &
  worker participation, worksite analysis, hazard prevention & control, training, recordkeeping &
  evaluation) enforced under the OSH Act §5(a)(1) General Duty Clause; Cal/OSHA 8 CCR 3342 as the
  binding standard in California; UK HSE work-related-violence guidance + NICE NG10; India via
  `hse-india`; ISO 45001 §6.1.2 (with the ISO 45003 psychosocial link).
- Review trigger: annual program review / on-incident / on-service-change — whichever is first.
- Decision-support only — a competent person (healthcare-security / WPV / occupational-health
  professional) must review before use.
