# Lone Working Risk Assessment — O&M Technician, Wind Farm WF-7

**Role / site:** O&M Technician (role) · Wind Farm WF-7
**Solitary activity:** ground-level met-mast inspection (alone)
**Jurisdiction:** UK — HSE INDG73 (rev 4) + BS 8484:2022
**Classification:** Internal — competent-person (lone-working / renewables-field SME) review required
**De-identification:** The lone worker is referred to by role label (Lone Worker A (role)); the check-in / escalation responder by role (Site Lead (role)). Personal contact numbers, the shift pattern and the precise work/home location are held in a separate access-controlled operational record; the re-identification key is held separately.

---

## 1. The proposed control — and why it is rejected

The control proposed for this lone met-mast inspection was: *"issue everyone a lone-worker panic-button app — if there's a problem they press the button; there's no mobile signal at the mast base but they can drive to where there is one."*

This is **rejected** on two grounds:

1. **It is device-led.** A BS 8484:2022 lone-worker device supplements — it never replaces — the lone-working procedure. A panic-button app with no scheduled check-in and no defined escalation procedure is not the control; it is a residual supplement on top of one.
2. **It accepts a communication failure as a residual risk.** "No mobile signal at the mast base" is a **control failure**, not an accepted risk. "Drive to where there is signal" leaves the worker uncontactable for the duration of the task — the moment a device is most needed is the moment it cannot raise the alarm.

## 2. Routing gate (work at height / electrical routed, not assessed solo)

The activity assessed here is ground-level and non-electrical. Two routing pointers are recorded:

- **Lone work at height** on the turbine is **not** assessed here — it routes to `wind-turbine-work-at-height-rescue` (REN-01)'s two-person, tested-rescue baseline. A solo turbine climb is not acceptable, and "call 999" is never the rescue plan.
- **Lone electrical** isolation/switching is **not** assessed here — it routes to the cross-listed utilities skills (`arc-flash-assessment` / `live-working-risk-assessment`).

## 3. Control order (eliminate the solitary exposure first)

| Order | Control | Tier | Owner (role) |
|---|---|---|---|
| Lead | Eliminate the solitary exposure — re-schedule the inspection into a paired (two-person) window so the technician is no longer alone | Elimination | O&M Supervisor |
| Then | Where pairing is not reasonably practicable — remote-monitor the task; provide a coverage-checked communication path (satellite messenger where mobile coverage fails) | Substitution / Engineering | Site Lead |
| Then | Scheduled hourly check-in + a defined missed-check-in escalation path | Administrative | Site Lead |
| Residual | BS 8484:2022 lone-worker device + monitored response chain, layered on top of the procedure — never instead of it | Administrative | O&M Supervisor |

Eliminating the solitary exposure is the lead control. The device is the last line, not the headline.

## 4. Communication & check-in / escalation

| Element | Requirement | Status |
|---|---|---|
| Communication coverage | Coverage-checked at the mast base | **[GAP]** — not confirmed; a no-signal finding is a control failure. A satellite messenger is specified pending the coverage check. |
| Scheduled check-in | Hourly | Defined |
| Missed-check-in escalation | Named responder + method + response time | Site Lead (role) attempts contact, then dispatches a second person to the mast **within 30 minutes** — defined |
| Lone-worker device | BS 8484:2022 (device + monitored response chain) | **[GAP]** — specific device/service not supplied; residual supplement only |

The responder and the response time are named, not left open. An undefined responder or time would be recorded `[GAP]`.

## 5. Key findings

| # | Finding | Risk | Evidence |
|---|---|---|---|
| F-1 | Control led with a device, not eliminating the solitary exposure | High | Draft control vs INDG73 / BS 8484 |
| F-2 | No mobile signal at the mast base accepted as residual (worker uncontactable in the interim) | High | Site coverage review — INDG73 reliable-communication duty |
| F-3 | Missed-check-in escalation required a named responder + response time | Medium | INDG73 — now Site Lead (role), 30 min |

## 6. Residual risk (5×5)

| Hazard | Lead control (hierarchy order) | Residual (5×5) | Owner (role) |
|---|---|---|---|
| Worker incapacitated while alone, uncontactable | Eliminate solitary exposure + coverage-checked comms + check-in/escalation | 6 (Medium) once paired / coverage confirmed; **16 (High) until the coverage [GAP] is closed** | Site Lead |
| Missed check-in with no response | Defined responder + 30-min response time | 6 (Medium) | Site Lead |
| Violence to staff / collapse while alone | Pairing / remote monitoring + monitored device | 8 (Medium) | O&M Supervisor |

The comms-coverage `[GAP]` dominates the residual until it is closed.

## 7. Recommendations ([GAP]-closure SMART actions)

| # | Action | Priority | Owner (role) | Due |
|---|---|---|---|---|
| A-1 | Re-schedule the met-mast inspection into a paired (two-person) window; where not practicable, remote-monitor the task | P1 | O&M Supervisor | 2026-07-15 |
| A-2 | Check mobile coverage at the mast base; provide a coverage-checked communication path (satellite messenger if mobile fails) — close the no-signal [GAP] | P1 | Site Lead | 2026-07-10 |
| A-3 | Confirm the scheduled check-in interval and the missed-check-in escalation path (responder / method / response time) in the lone-working procedure | P2 | Site Lead | 2026-07-31 |
| A-4 | Specify the BS 8484:2022 lone-worker device + monitored response chain as a residual supplement; record the device/service ([GAP] → supplied) | P2 | O&M Supervisor | 2026-08-31 |

---

## Regulatory basis

- **HSE INDG73 (rev 4)** — the explicit lone-working risk-assessment duty, reliable coverage-checked communication, scheduled check-ins + a missed-check-in escalation procedure, and the violence + stress/wellbeing considerations.
- **BS 8484:2022** — lone-worker device services (the conformant device + the monitored response chain); a device supplements, never replaces, the procedure.
- **Work at Height Regulations 2005 reg 4** — lone work at height routes to REN-01's two-person / tested-rescue baseline.
- **ISO 45001 cl 6.1.2** — hazard identification & risk assessment; the hierarchy of controls.

*Decision-support only — a competent person must review this assessment before use.*
