# Lift Plan — 12.8 t AHU to the level-6 plant deck (LOLER Reg 8 / BS 7121)

De-identification pass complete BEFORE drafting. Identifiers detected and listed up front: one
crane-operator name, a medical-fitness note, lifting-incident injury counts — the
incident-derived name and the medical-fitness detail were scrubbed to role labels / removed, the
injury counts aggregated, and the re-identification key is held in a SEPARATE access-controlled
artifact (not reproduced here).

## 1. Lift classification (BS 7121)

**STANDARD** lift per BS 7121 (`KB-DATA-LIFT-CATEGORIES`): single crane, load a significant
fraction of the SWL-at-radius (90% utilisation), with overhead-line and confined-radius
proximity. A **named appointed person** and a **documented lift plan** are required. (Had the
lift been tandem / multi-crane, blind, or over an occupied area, it would be **complex** and
mandate an appointed-person **written** plan with contingency / abort criteria.)

## 2. Load & rigging (CONFIRMED before planning)

| Item | Confirmed weight (incl. rigging) | Dimensions | CoG / lifting points |
|---|---|---|---|
| Packaged AHU + rigging | **12.8 t** (12.0 t load + 0.8 t rigging) — CONFIRMED | 4.2 × 2.1 × 2.4 m | CoG marked; 4 certified lifting points |

The load weight was **confirmed before planning** — an unconfirmed weight would be a `[GAP]` and
a stop, never assumed.

## 3. Equipment selection & SWL / utilisation (READ from the rated-capacity chart, not computed)

| Parameter | Value (transcribed) | Source (chart / standard, year) |
|---|---|---|
| Crane | 50 t mobile, 28 m boom, on outriggers | Site selection |
| SWL at 12 m radius | **14.2 t** | Liebherr LTM-1050 rated-capacity chart, 2021 |
| Utilisation | **90%** (12.8 / 14.2) | Checked vs `KB-DATA-LIFT-CATEGORIES` utilisation test |
| In-service wind limit | 9.8 m/s | Rated-capacity chart, 2021 |

The SWL-at-radius and utilisation are **read from the manufacturer's rated-capacity chart and
checked against the BS 7121 thresholds — not computed** (this skill carries no lifting
calculator). At 90% the lift is within margin; had utilisation exceeded the planned safe margin
the plan would flag **re-selection of the crane** (larger crane / shorter radius).

## 4. Ground & proximity

- Ground / outrigger bearing assessed against the outrigger loads and the site ground report;
  outrigger mats sized accordingly.
- **11 kV overhead line** within the slew radius — controlled by the exclusion zone below.
- Confined working radius adjacent to the occupied building elevation.

## 5. Exclusion zones & segregation — the overhead-line gate

> **Overhead-line control LEADS with elimination / engineered exclusion, NOT PPE.** The lift is
> re-positioned so no part of the crane or load enters the GS6 minimum-clearance envelope of the
> 11 kV line; goal-posts and a barriered exclusion zone enforce the boundary, with a dedicated
> banksman. The site's proposed **"operatives to take care and wear PPE"** near the line is
> **rejected as a PPE-only control** (`controls.ppe_admin_only = True`, no higher-order control
> and no justification) and pushed up the hierarchy.

| Zone | Basis | Control (tier) |
|---|---|---|
| Overhead-line exclusion | GS6 minimum clearance from the 11 kV line | Re-route + goal-posts + barriered exclusion + banksman (**Elimination / Engineering**) |
| Load swing / drop zone | Slew radius + load footprint | Barriered; no persons under a suspended load (**Administrative**) |
| Public / building segregation | Occupied elevation adjacent | Hard barrier + signage; lift timed outside occupancy where practicable (**Administrative**) |

## 6. Sequenced lift method

1. **Rig** the load to the 4 certified lifting points; check accessory certificates and the CoG.
2. **Trial-lift / weigh** — lift clear by 150 mm, confirm load stability and the chart weight.
3. **Travel / slew** within the planned arc only — banksman in continuous communication.
4. **Place** onto the level-6 plant deck at the planned set-down point.
5. **De-rig** and clear the exclusion zone.

## 7. Roles & competence (named duty-holders — legitimate competence record)

| Role | Competence basis |
|---|---|
| Appointed Person (plans & supervises) | Appointed-person trained to BS 7121 |
| Crane Operator | CPCS A66 mobile crane (current medical certificate held at role level; no health detail circulated) |
| Slinger / Signaller | CPCS A40 slinger / signaller |

*(The appointed person, operator, and slinger are named in the issued plan as a deliberate
competence record. No worker's medical-fitness / health detail is carried — fitness is recorded
only as "current medical certificate held" at role level.)*

## 8. Contingency & abort criteria

- **ABORT** on loss of communication between operator and slinger / signaller.
- **ABORT** if in-service wind exceeds 9.8 m/s (chart limit).
- **ABORT** on any unplanned obstruction or any person entering an exclusion zone.
- On abort: land the load at the nearest safe set-down, secure, and re-plan.

## 9. Weather limits

Lift suspended if the in-service wind limit (9.8 m/s, from the rated-capacity chart) is forecast
or measured at the boom tip, or in conditions that impair the slinger / signaller's visibility of
the load.

## 10. Residual risk (re-scored via `risk_matrix` after controls)

| Hazard | Initial | Residual | Movement |
|---|---|---|---|
| Overhead-line contact | High (16) | **Medium (8)** | re-route + engineered exclusion + banksman |
| Load instability / dropped load | High (12) | **Low (4)** | trial-lift / weigh + certified accessories |

A residual High / Critical risk would flag a **hold-point (do-not-lift)**; both residuals are at
or below Medium with the controls applied.

## 11. Review & sign-off

| Action | Owner | Due |
|---|---|---|
| Confirm the ground / outrigger-loading report against the chart outrigger loads before set-up | Appointed Person | 25 Jun 2026 |
| Re-plan and re-brief on any change of crane, load, radius, ground, or weather beyond the limit | Appointed Person | On change |

**Injury history (aggregated, small cells suppressed):** lifting-incident injuries on this site
this quarter are reported by role, aggregated = 6 (cells fewer than five suppressed; secondary
suppression applied). No `<5` injury cell and no named operator's detail is published.

## Regulatory basis

- **LOLER 1998 Reg 8** — lifting operation planned by a competent person, supervised, carried out
  safely.
- **LOLER 1998 Reg 9** — thorough examination of the crane and lifting accessories.
- **BS 7121** *Safe Use of Cranes* — lift categorisation (basic / standard / complex).
- **ISO 45001 clause 6.1.2 / 8.1.2** — hazard ID and the hierarchy of controls.
- **CDM 2015** — where the lift is part of construction works, the lifting operation sits under
  the Construction Phase Plan (loosely coupled).

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
