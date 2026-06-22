<!-- CANDIDATE golden output for arc-flash-assessment (UTIL-01). Generated from eval case 1's
     scenario (MCC-2, 480 V motor control centre, Substation 2). It demonstrates the core lever:
     de-energize-first + the hierarchy. The crew's proposed control — "issue a CAT 2 arc-flash suit
     and crack on live, production can't stop" — is a PPE-led treatment of a task that could be
     de-energized AND an energized-work request justified only by economic convenience; it is
     FLAGGED and PUSHED UP the hierarchy (de-energize and establish an ESWC first), and the
     convenience justification is REJECTED. The incident energy (7.51 cal/cm²), the arc-flash
     boundary (1332 mm = distance to 1.2 cal/cm²), and the PPE category (CAT 2) are COMPUTED by the
     arcflash.py IEEE 1584-2018 engine, never narrated. The 130.5(H) label content is authored. The
     prior arc-flash burn incident is de-identified to role level. NOT owner-LOCKED — the owner
     reviews + locks in P17. -->

# Arc-Flash Assessment — MCC-2 480 V Motor Control Centre (Substation 2)

*Decision-support only. A competent person (qualified electrical engineer) must review and sign off
this arc-flash assessment. A prior arc-flash burn incident is cited at role level as context; the
re-identification key is held separately.*

## 1. Equipment & task description

De-identification ran first: the injured worker's name, the incident date, and the medical detail
were scrubbed to role level; no named worker and no `<5` injury cell appears below.

- **Equipment:** MCC-2, 480 V motor control centre, Substation 2 (equipment-specific — not "a
  panel").
- **Task:** bucket replacement + feeder-breaker maintenance at the 480 V bus.
- **Proposed control (as received):** "issue a CAT 2 arc-flash suit and crack on live — production
  can't stop". This is assessed against the de-energize-first hierarchy below.

## 2. De-energization decision (recorded FIRST — the primary control)

The maintenance task **CAN be done de-energized**. An **electrically safe work condition** (NFPA 70E
**Article 120**) is established **before** any reliance on arc-rated PPE. The energized "production
can't stop" request is **REJECTED** — economic convenience alone does not meet OSHA 1910.333(a)(2)
("additional/increased hazard or infeasible") or EAWR reg 14, so no energized-work permit is raised.

| ESWC step (Article 120) | Action | Owner (role) |
|---|---|---|
| Identify sources | Identify all sources feeding MCC-2 (incomer + back-feed) | Authorised Person |
| Disconnect / isolate | Open the upstream feeder breaker; rack out where designed | Authorised Person |
| Lock / tag | Apply lockout/tagout to the isolating device | Authorised Person |
| Test for absence of voltage | Test-before-touch with a proven, tested detector | Authorised Person |
| Ground if required | Apply protective grounds where stored/induced energy is credible | Authorised Person |

## 3. Incident energy @ working distance (IEEE 1584-2018 — COMPUTED, not narrated)

`arcflash.incident_energy(...)` was run on the supplied IEEE 1584 inputs — the cal/cm² value is
**computed by the engine, never asserted**.

| Parameter | Value |
|---|---|
| Open-circuit voltage (V) | 480 |
| Bolted fault current (kA) | 22.6 |
| Conductor gap (mm) | 25 |
| Electrode configuration | VCB |
| Working distance (mm) | 457.2 |
| Arc duration (s) | 0.2 |
| Arcing current (kA) | 18.55 |

- **Incident energy:** **7.51 cal/cm²** at the 457.2 mm working distance.
- **Arc-flash boundary:** **1332 mm** (the distance to **1.2 cal/cm²** — second-degree-burn onset).
- **NFPA 70E PPE category:** **CAT 2** (the 4–8 cal/cm² band).

## 4. Shock approach boundaries (NFPA 70E 130.4)

| Boundary (130.4) | Basis |
|---|---|
| Limited approach | The 480 V system-voltage row of NFPA 70E Table 130.4 (cite the table; cells not pasted) |
| Restricted approach | The same 130.4 row; entry needs a qualified person + permit (only if energized work is later justified) |
| Arc-flash boundary | 1332 mm (computed; distance to 1.2 cal/cm²) |

## 5. Engineering / control gate (the de-energize-first lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "issue a
CAT 2 suit and crack on live" is a **PPE-led treatment of a task that could be de-energized** — it
is a **CONTROLS FLAG** (`ppe_admin_only=True`) **pushed up the hierarchy**. Arc-rated PPE is the
residual-hazard last line, never the headline control.

| Proposed / existing control | Gate outcome |
|---|---|
| "Issue a CAT 2 suit and crack on live (production can't stop)" | **FLAG — PPE-led + convenience-justified energized work.** Pushed up the hierarchy: de-energize and establish an ESWC first; the energized request is REJECTED (fails 1910.333(a)(2) / EAWR reg 14). |

## 6. Hierarchy-ranked controls (de-energize first → arc-rated PPE last)

| Control | Tier | Owner (role) |
|---|---|---|
| De-energize + establish an ESWC (Article 120) — the primary control | Elimination | Authorised Person |
| Commission a maintenance-mode / arc-energy-reduction trip setting (cuts clearing time) | Engineering | Electrical Engineer |
| Mark the 1332 mm arc-flash boundary on the floor + update the panel label | Administrative | HSE Utilities & Power |
| CAT 2 arc-rated PPE as the residual last line during isolation/verification | PPE | Authorised Person |

## 7. NFPA 70E 130.5(H) label content

| Label field (130.5(H)) | Value |
|---|---|
| Nominal system voltage | 480 V |
| Arc-flash boundary | 1332 mm |
| Available incident energy + working distance | 7.51 cal/cm² @ 457.2 mm |
| Required PPE category (alternative) | CAT 2 |
| Study date | stamped at issue |

## 8. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Install the updated arc-flash label (computed boundary + category) | P1 | Electrical Engineer | 2026-07-10 |
| Commission the maintenance-mode arc-energy-reduction trip setting | P2 | Electrical Engineer | 2026-07-31 |
| Refresh the study on any protection or system change | P3 | HSE Utilities & Power | 2026-12-15 |

## 9. Assumptions, gaps & sign-off

- Bolted fault current (22.6 kA) and clearing time (0.2 s) taken from the supplied short-circuit /
  protection study — a missing input would be a `[GAP]`, never an invented value.
- India site (if applicable): state electricity-rule return owed — `[GAP]` (resolve the state via
  `hse-india`; no national form number minted).
- **Regulatory basis:** NFPA 70E (2024) 130.5 / 130.5(G) / 130.5(H) / 130.4 / 130.7(C)(15) /
  Article 120; IEEE 1584-2018; OSHA 29 CFR 1910.333 + 1910.269; UK EAWR 1989 reg 14 + HSG85;
  ISO 45001 §6.1.2.
- Review trigger: on system change / on protection change / 5-yearly — whichever is first.
- Decision-support only — a competent person (qualified electrical engineer) must review before use.
