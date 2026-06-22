<!-- CANDIDATE golden output for infection-control-plan (HC-02). Generated from eval case 1's
     scenario (Respiratory Unit, Ward 4B; airborne TB + droplet ILI + contact MDRO). It demonstrates
     the core lever: engineering/administrative controls before PPE + the hierarchy. The unit
     manager's proposed control -- "give the staff N95 respirators and tell them to keep the door
     shut" -- is a PPE-led treatment of an airborne agent with no airborne-infection isolation room or
     ventilation provision; it is FLAGGED and PUSHED UP the hierarchy (an AIIR / negative pressure is
     the engineering control, PPE the residual barrier). PHI is the highest tier: patients are
     referenced by role / cohort only, no infection status is attributed to a named person, and the
     surveillance is de-identified / aggregated with <5 clusters suppressed. NOT owner-LOCKED -- the
     owner reviews + locks in P17. -->

# Infection Control Plan — Respiratory Unit, Ward 4B

*Decision-support only. A competent person (infection-prevention & control professional) must review
and sign off this plan. Patients are referenced by role / cohort only; no infection status is
attributed to a named person; the re-identification key is held separately and is not part of this
document.*

## 1. Unit, agents & transmission routes

De-identification ran first: the staff name and contact, the index patient's identity and infection
status, and the case counts were scrubbed to role / aggregate level; no named patient, no infection
status tied to a person, and no `<5` cluster on a named ward appears below.

- **Service:** Respiratory Unit, Ward 4B (service-specific — not "a hospital").
- **Agents & routes:** suspected pulmonary tuberculosis (**airborne**), influenza-like illness
  (**droplet**), multidrug-resistant organism (**contact**).
- **Proposed control (as received):** "give the staff N95 respirators and tell them to keep the door
  shut" (for the airborne TB case). This is assessed against the engineering-and-administrative-first
  hierarchy below.

## 2. Engineering / control gate (the controls-before-PPE lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "give staff
N95 respirators and keep the door shut" is a **PPE-led treatment of an airborne agent with no
airborne-infection isolation room (AIIR), negative-pressure, or ventilation provision** — it is a
**CONTROLS FLAG** (`ppe_admin_only=True`) **pushed up the hierarchy**. PPE is the documented residual
barrier, never the headline control.

| Proposed / existing control | Gate outcome |
|---|---|
| "Give staff N95 respirators; keep the door shut" (airborne TB) | **FLAG — PPE-led, no AIIR / negative pressure / ventilation.** Pushed up the hierarchy: provide an airborne-infection isolation room (negative pressure) + restricted entry first; the fit-tested respirator is the residual barrier. |

## 3. Transmission-based precautions by route (Standard Precautions for every patient)

| Transmission route | Engineering / administrative control (first) | Patient placement | Residual PPE | Owner (role) |
|---|---|---|---|---|
| Standard (every patient) | Hand-hygiene programme; safe injection; environmental cleaning | Routine placement | PPE by anticipated exposure | Ward Manager |
| Contact (MDRO) | Dedicated equipment; cohorting; enhanced terminal cleaning | Single room or cohort | Gown + gloves | IPC Lead |
| Droplet (ILI) | Spatial separation; respiratory etiquette; signage | Single room / spatial separation | Surgical mask within range | IPC Lead |
| Airborne (TB) | Airborne-infection isolation room (negative pressure); restricted entry; ventilation | AIIR (negative pressure) | Fit-tested respirator | Estates Lead |
| Environmental | Terminal-clean protocol; ATP-swab assurance | n/a | Task PPE | Domestic Lead |

Standard Precautions apply to every patient; the Transmission-Based precautions above are layered by
the identified route, with engineering and administrative controls ahead of PPE.

## 4. Hierarchy-ranked controls (engineering → administrative → PPE last)

| Control | Tier | Owner (role) |
|---|---|---|
| Airborne-infection isolation room (negative pressure, monitored air changes per hour) for the TB case; ventilation upgrade where rooms are inadequate | Engineering | Estates Lead |
| Single rooms / spatial separation (droplet); single room or cohort + dedicated equipment (contact) | Engineering | IPC Lead |
| Cohorting, early screening / triage, isolation signage, restricted entry, hand-hygiene audit | Administrative | Ward Manager |
| Route-appropriate PPE as the residual barrier (gown+gloves contact; surgical mask droplet; fit-tested respirator airborne) | PPE | Occupational Health Lead |

## 5. Spaulding reprocessing decision (device → required level)

| Spaulding class | Contact with | Required reprocessing | Example device |
|---|---|---|---|
| Critical | Sterile tissue / bloodstream | Sterilization | Biopsy forceps, surgical instruments |
| Semi-critical | Mucous membranes / non-intact skin | High-level disinfection (sterilization where feasible) | Flexible endoscopes, laryngoscope blades |
| Non-critical | Intact skin | Low-level disinfection | BP cuffs, stethoscopes |

A **critical** device must be **sterilized** — high-level disinfection of a critical device is a
Spaulding mis-application and is rejected.

## 6. WHO IPC programme structure (core components)

- IPC programme with a trained team and clear governance.
- Evidence-based IPC guidelines + education and training.
- Surveillance of healthcare-associated infection — de-identified and aggregated.
- Multimodal improvement strategy + monitoring / audit and feedback.
- Workload, staffing, bed-occupancy and the built environment / materials.

## 7. Surveillance (de-identified / aggregated — small cells suppressed)

The surveillance is reported at unit / aggregate level only. Any case category of fewer than five
individuals is suppressed, and a second category is suppressed (or aggregated up) so a suppressed value
cannot be back-calculated from a published total. No outbreak is reported on a named ward in a way that
re-identifies a patient.

| Indicator | Reported value |
|---|---|
| Respiratory-isolation cases this period (aggregated) | aggregated ≥ 5 (small cells fewer than five suppressed) |
| Hand-hygiene compliance | below the 95% target (improvement plan in §9) |
| Isolation-room negative-pressure verification | daily log; weekend gaps tracked at unit level |

## 8. Residual risk

After the engineering controls (AIIR / negative pressure, single rooms, ventilation), administrative
controls (cohorting, screening, hand-hygiene audit) and route-appropriate residual PPE, the residual
transmission risk is framed via `risk_matrix` as **Low–Medium**, with PPE as the documented last line.

## 9. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Commission daily negative-pressure verification with an automated alarm + log for the AIIR | P1 | Estates Lead | 2026-07-15 |
| Confirm the Spaulding reprocessing matrix per device class; sterilize all critical devices | P1 | IPC Lead | 2026-07-10 |
| Reinstate night-shift hand-hygiene audit + feedback | P2 | Ward Manager | 2026-08-05 |
| Run the WHO IPC core-component self-assessment and close the gaps | P2 | IPC Lead | 2026-09-30 |

## 10. Assumptions, gaps & sign-off

- Surveillance counts taken from the de-identified aggregated record; categories of fewer than five
  are suppressed — a missing figure is a `[GAP]`, never invented.
- India site (if applicable): state biomedical-waste / IPC return owed — `[GAP]` (resolve the state
  via `hse-india`; BMW Rules 2016; no national form number minted).
- **Regulatory basis:** the CDC Guideline for Isolation Precautions (Standard + Transmission-Based);
  the WHO Core Components of IPC; the Spaulding classification; the UK Hygiene Code; the OSHA
  bloodborne pathogens standard (confidential health-data handling); India BMW Rules 2016 via
  `hse-india`; ISO 45001 §6.1.2 / §8.1.2.
- Review trigger: annual IPC review / on-outbreak / on-guideline-change — whichever is first.
- Decision-support only — a competent person (infection-prevention & control professional) must review
  before use.
