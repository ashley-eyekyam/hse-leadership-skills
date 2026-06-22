# Behaviour-Based Safety Programme — Order-Picking Crew, Leeds DC

**Programme type:** Non-punitive behaviour-based-safety (BBS) observation programme — design.
**Scope:** Order-picking crew, Leeds DC — a named crew (≈18 pickers across day, night and weekend-relief shifts). Voluntary peer observation; no individual recorded.
**Method:** ABC (antecedent–behaviour–consequence) analysis; non-punitive observation card; defined metrics (percent-safe / participation / trend-by-category); at-risk behaviours trended to systemic causes and routed to hierarchy-ranked system fixes via the controls engine.
**Standard basis:** ISO 45001:2018 clause 5.4 (consultation and participation of workers), via the leadership clause cross-walk. The BBS method is cited as method (ABC / peer-observation), not law.
**Jurisdiction:** UK — worker-participation duty under the Safety Representatives and Safety Committees framework.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before roll-out. Not legal advice.

## 1. De-identification & non-punitive status

De-id pass ran **FIRST**. Identifiers detected in the raw card log (two worker names, one home address, one phone number) were pseudonymised to **role/group labels**; no re-identification key is reproduced here. The programme is **non-punitive by design**: every observation card is **role-labelled or anonymous**, **voluntary**, and its data is used for **trending and learning, never individual discipline**. **No card records a nameable individual**, and no card feeds a disciplinary process. Any sub-team breakdown of fewer than 5 is **suppressed** with **secondary suppression**.

## 2. ABC analysis (design the consequence for the safe behaviour)

| Antecedent (real trigger) | Observable behaviour (safe) | Consequence to engineer | Target task/area |
|---|---|---|---|
| Rack-pick above shoulder height under pick-rate pressure | Uses the provided step + keeps the load below shoulder height | Immediate positive peer acknowledgement; pick-rate target adjusted so the safe method is not penalised | Manual handling — racking |
| Reversing MHE crosses the pick aisle | Picker waits at the marked hold point until the driver makes eye contact | Soon/certain: driver signals thanks; no near-miss | Line-of-fire — conveyor/MHE aisle |
| Spillage or banding offcut left on the pick line | Picker clears the walkway immediately and reports the source | Positive recognition; housekeeping audit score visible to the crew | Housekeeping — pick line |

**Design principle:** the system is shaped so the **safe** behaviour carries the **soon / certain / positive** consequence. An at-risk behaviour is treated as a signal of a **system gap**, not a bad worker.

## 3. Observation card (non-punitive, observable)

- **Observable, site-specific items only** — e.g. "load kept below shoulder height on the rack pick", "waits at the marked hold point for reversing MHE", "walkway clear of spillage/offcuts". **No non-observable slogan** ("work safely", "be careful") is on the card.
- **Role-labelled or anonymous** — the card records the task/area and the behaviour, **never a nameable individual**.
- **Voluntary** participation; **two-way, immediate feedback** (the observer discusses both safe and at-risk behaviours on the spot, in the picker's own terms).
- Data is used for **trending and learning, never individual sanction**.

## 4. Defined metrics (KB-DATA-BBS-METRICS; trended by category, never by person)

| Metric | Formula | Notes |
|---|---|---|
| Percent-safe | (safe observations ÷ total observations) × 100 | trended by behaviour category, never by person |
| Participation | (active observers ÷ trained pool of 18) × 100 | role/group level |

Breakdowns are reported by **behaviour category** (manual handling / line-of-fire / housekeeping). The **`<5` small-cell suppression** applies: a percent-safe for the weekend-relief group (n = 4) is **suppressed** and aggregated into the parent crew figure, with secondary suppression so it cannot be back-calculated.

## 5. At-risk behaviours trended to systemic causes → SYSTEM fixes

| At-risk category (trended) | Systemic driver (not "the worker") | System fix (hierarchy of controls) | Tier | Owner |
|---|---|---|---|---|
| Above-shoulder rack picks | Slow-moving stock stored above shoulder height; pick-rate target penalises the step | **Engineer:** re-slot fast-movers to the golden zone; **Administrative:** adjust pick-rate target to credit the safe method | Engineering + Administrative | Warehouse Operations Manager |
| Picker in the MHE line of fire | No marked hold points; mixed pedestrian/MHE aisle | **Engineer:** segregated pedestrian walkway + marked hold points; **Substitute:** re-route reversing moves | Engineering / Substitution | SHEQ Lead |
| Walkway obstructed by offcuts | No bin at the banding station; offcuts accumulate | **Eliminate:** auto-collection chute at the bander; **Administrative:** end-of-cycle sweep | Elimination + Administrative | Shift Team Leader (role) |

**No at-risk category is routed to "retrain the worker", "be more careful", or discipline.** Each is routed to a hierarchy-ranked **system fix** (controls.rank_controls / controls.validate_treatment cleared — no admin/PPE-only treatment left unjustified).

## 6. SMART action plan (owned + dated)

| Action | Priority | Owner (role label) | Due |
|---|---|---|---|
| Re-slot fast-moving SKUs into the golden zone on racks 1–6; re-baseline the pick-rate target to credit the step method | High | Warehouse Operations Manager | 15 Aug 2026 |
| Install the segregated pedestrian walkway and marked MHE hold points in the pick aisle | High | SHEQ Lead | 30 Sep 2026 |
| Fit an offcut-collection chute at the banding station and add the end-of-cycle sweep to the shift routine | Medium | Shift Team Leader (role) | 29 Aug 2026 |
| Train the voluntary peer-observer pool on observable-behaviour cards and two-way feedback | Medium | SHEQ Lead | 8 Aug 2026 |

Every action has a named **role-label** owner, an ISO due date, and a measure (`smart_actions.validate_register` passes). No anonymous actions, no "ASAP".

## 7. Observer-feedback loop & review cycle

observe → discuss (two-way, positive + at-risk, on the spot) → record card (de-identified, role-labelled) → aggregate / trend **by behaviour category** → feed **systemic fixes** via the controls engine + owned/dated actions → close the loop back to observers and the crew. **Percent-safe and participation reviewed monthly; the card reviewed quarterly.** The programme's purpose is systemic improvement, not a tally of individuals.

## 8. Provenance

ABC / behaviour-based-safety method (`KB-SNIP-BBS-METHOD`) · defined metrics + `<5` guardrail (`KB-DATA-BBS-METRICS`) · ISO 45001 clause 5.4 worker participation (`KB-SNIP-LEADERSHIP-CLAUSE-MAP`) · hierarchy of controls applied to every at-risk-behaviour treatment (`KB-SNIP-HOC`). Branded report.json → DOCX + PDF via the shared report engine.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
