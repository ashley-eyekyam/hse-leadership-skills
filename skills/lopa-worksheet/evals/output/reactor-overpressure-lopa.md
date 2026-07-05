<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3. -->
# Layer of Protection Analysis (LOPA) Worksheet

**Scenario: Reactor Overpressure — Unit 200, Site-X**

| Document control | |
|---|---|
| Worksheet ID | LOPA-U200-001 |
| Scenario | Reactor overpressure (single-scenario worksheet) |
| Unit / Site | Unit 200, Site-X |
| Worksheet type | New scenario worksheet [ASSUMPTION — no prior LOPA worksheet for this scenario was referenced; the change-since-last-LOPA section therefore does not apply] |
| Date prepared | 5 July 2026 |
| Revision | 0 (DRAFT — INCOMPLETE) |
| Status | **Open [GAP] items outstanding — residual-gap banding cannot proceed until engineer-supplied values are provided** |
| Values owned by | Lead Engineer — process-safety competency (role) |
| Method basis | IEC 61511 Layer of Protection Analysis (KB-STD-IEC-61511 — the LOPA/SIL method map) |
| Jurisdiction for grounding citation | None — IEC 61511 method basis only [ASSUMPTION — no jurisdiction was supplied; no statutory instrument is cited anywhere in this worksheet] |

---

## 1. Purpose, scope and method basis

This worksheet structures **one** consequence scenario — reactor overpressure at Unit 200 — as a Layer of Protection Analysis to the IEC 61511 method (KB-STD-IEC-61511). One consequence scenario, with one initiating event, per worksheet; any additional overpressure pathway or distinct consequence identified during review must be opened as a separate worksheet.

**Basis of values.** Every frequency, probability of failure on demand (PFD), IPL credit, and SIL target in this worksheet is an **engineer-supplied, engineer-verified input** owned by the Lead Engineer (role). This worksheet records those inputs, tests that an independence judgement has been stated for each protection layer, and bands the residual-risk **gap** against the tolerable criterion once the inputs exist. It does **not** compute any PFD, derive any frequency, or allocate any SIL. Any value not supplied by the engineering team is recorded as a literal **[GAP]** — see the consolidated register in Section 10.

---

## 2. Scenario definition

| Field | Record |
|---|---|
| Consequence scenario (one per worksheet) | Reactor overpressure, Unit 200, Site-X |
| Consequence description (what the overpressure leads to — e.g. loss of containment, vessel damage, release) | **[GAP]** — engineer to state the specific consequence end-point this scenario is credited against |
| Consequence severity category | **[GAP]** — engineer to assign against the confirmed risk matrix (Section 7) |
| Receptors exposed (people / environment / asset) | **[GAP]** — carried with the consequence description above |
| Operating mode in which the scenario applies | **[GAP]** — engineer to state (e.g. normal operation, start-up, upset) |

**Supporting site context (as supplied):** recordable injuries this period: 12. Small categories are aggregated (aggregation floor = 5) with secondary suppression applied, so suppressed cells cannot be back-calculated from the total. No category below 5 individuals is published in this worksheet.

---

## 3. Analysis team and ownership of values

Team members are recorded as role/competency labels only.

| Role | Competency | Responsibility in this LOPA |
|---|---|---|
| Lead Engineer (role) | Process safety | Owns all engineer-supplied values (IE frequency, PFDs, IPL credits, SIL target); accountable for closure of every [GAP] in Section 10 |
| DCS Operator (role) | Operations | Operational input to initiating-event identification, alarm/response screening, and IPL practicability |

Sign-off by a competent person (Section 12) is required before this worksheet is relied on for any design, modification, or SIL-related decision.

---

## 4. Initiating event

| Field | Record |
|---|---|
| Initiating event (IE) description | **[GAP]** — engineer to supply the specific initiating cause of the Unit 200 overpressure scenario |
| IE category (control-loop failure / human error / equipment-mechanical / external event / loss of utility) | **[GAP]** — assigned with the IE description; not assumed here |
| IE frequency (per year), engineer-supplied | **[GAP]** — never computed by this worksheet |
| Frequency provenance (company LOPA table / vendor data / site history) | **[GAP]** — to be recorded alongside the frequency |

No initiating event or frequency was supplied with the scenario notes. The worksheet cannot proceed to residual-gap banding until this row is complete (action A1, Section 9).

### 4.1 Enabling conditions and conditional modifiers

| Item | Record |
|---|---|
| Enabling conditions (e.g. time-at-risk factors) | **[GAP]** — engineer to confirm whether any apply, or record "none" explicitly |
| Conditional modifiers (e.g. probability of ignition, probability of personnel presence) | **[GAP]** — engineer to confirm whether any are claimed, with provenance; none are assumed |

---

## 5. Independent protection layers (IPLs) — inventory and independence tests

An IPL is credited only where the engineering team has stated that it is (a) independent of the initiating event, (b) independent of every other credited IPL, and (c) not double-counted (for example, sharing a sensor, logic solver, or final element with the BPCS or a SIF). The independence judgement belongs to the engineering team; this worksheet records the stated test and flags whatever remains unstated.

### 5.1 IPL inventory (as supplied)

| # | Candidate IPL | Independence test — as stated by the engineering team | PFD (engineer-supplied) | PFD provenance | Credit status |
|---|---|---|---|---|---|
| IPL-1 | Relief valve | Independent of the initiating event — **stated**. Independence from every other IPL, and confirmation of no double-counting (e.g. no shared final element or common process connection with any other credited layer) — **not stated → [GAP]** | **[GAP]** — engineer to supply; not computed by this worksheet | **[GAP]** — company LOPA table / vendor data / site history, to be recorded with the PFD | **Credit pending** — no credit is taken until the PFD is supplied with provenance and the independence test is completed in full |

### 5.2 Candidate layers not yet screened

The supplied notes list a single IPL. Whether further protection layers exist for this scenario — for example a BPCS control layer, an independent alarm with credited operator response, a safety instrumented function (SIF), or other passive/mechanical protection — was **not supplied → [GAP]**. Their existence and qualification are for the engineering team to screen (action A3); none are presumed here.

| Candidate layer class | Exists for this scenario? | Qualifies as an IPL? |
|---|---|---|
| BPCS control layer | **[GAP]** | **[GAP]** |
| Independent alarm + operator response | **[GAP]** | **[GAP]** |
| Safety instrumented function (SIF) | **[GAP]** | **[GAP]** |
| Other passive / mechanical layer | **[GAP]** | **[GAP]** |

---

## 6. IPL credit summary and mitigated event frequency

| Item | Record |
|---|---|
| Total IPL credits claimed | None yet — IPL-1 credit is pending (Section 5.1) |
| Mitigated event frequency (engineer-verified product of IE frequency × credited PFDs) | **[GAP]** — this is the engineering team's verified input; it is recorded here when supplied, never multiplied out by this worksheet |

---

## 7. Residual-risk gap

| Field | Record |
|---|---|
| Tolerable target frequency for this consequence (engineer-supplied) | **[GAP]** |
| Risk matrix used to band the residual gap | Default 5×5 matrix [ASSUMPTION — no company matrix was supplied; to be confirmed or replaced by the pasted company matrix before banding, action A5] |
| Residual-risk gap band | **Cannot be banded at Revision 0.** Gap banding is the only arithmetic this worksheet performs, and it requires the IE frequency (Section 4), the credited PFDs (Section 5), the engineer-verified mitigated event frequency (Section 6), and the tolerable target — all currently [GAP] |

The gap band will be recorded here at the next revision, once actions A1–A5 close.

---

## 8. SIL link

| Field | Record |
|---|---|
| Is a SIF claimed as an IPL for this scenario? | **[GAP]** — pending the Section 5.2 screen |
| SIL target (engineer-supplied) | **[GAP]** — recorded when the engineering team supplies it; **this worksheet does not allocate a SIL**. If the analysis is being used to support SIL determination, the allocation is made by the competent engineering team under their functional-safety procedure (KB-STD-IEC-61511) and recorded here as their input |

---

## 9. Hierarchy-of-controls ranking and recommendations

Protection layers are ranked against the hierarchy of controls (KB-SNIP-HOC). Reliance on a relief valve is an engineering control — a mitigative hardware layer that acts after the demand has occurred. It sits below elimination, substitution, and inherently safer design measures that would remove or reduce the overpressure demand itself. No layer in the current inventory addresses the hazard at a higher order, so recommendation A7 asks the engineering team to record whether inherently safer options were considered before settling the final IPL set.

| Rank (HoC) | Layer / measure | HoC class | Position in this scenario |
|---|---|---|---|
| 1 | Elimination / substitution / inherently safer design of the overpressure demand | Elimination–substitution | Not yet evidenced for this scenario — see action A7 |
| 2 | Engineered prevention layers (BPCS, SIF) acting before the consequence | Engineering control (preventive) | Existence unscreened — **[GAP]**, action A3 |
| 3 | Relief valve (IPL-1) | Engineering control (mitigative) | Sole supplied layer; credit pending (Section 5.1) |
| 4 | Administrative response (alarm + operator action) | Administrative control | Existence unscreened — **[GAP]**, action A3 |

### SMART actions (tracked to closure)

All owners are role labels. Due dates are proposed and subject to confirmation at the next team session.

| # | Action | Owner (role) | Due date | Status |
|---|---|---|---|---|
| A1 | Supply the initiating-event description, category, and engineer-verified frequency (per year) with provenance (Section 4) | Lead Engineer — Process Safety | 19 July 2026 | Open |
| A2 | Supply the engineer-verified PFD and provenance for the relief valve (IPL-1), and complete its independence test — independence from every other IPL and explicit confirmation of no double-counting | Lead Engineer — Process Safety | 19 July 2026 | Open |
| A3 | Screen the candidate layer classes in Section 5.2 for existence and IPL qualification, with the DCS Operator (role) contributing the operational-response assessment | Lead Engineer — Process Safety, with DCS Operator | 26 July 2026 | Open |
| A4 | Supply the tolerable target frequency (and SIL target, if a SIF is claimed) from the company risk criteria | Lead Engineer — Process Safety | 26 July 2026 | Open |
| A5 | Confirm the risk matrix for gap banding — company matrix (paste into Section 7) or the default 5×5 | Lead Engineer — Process Safety | 19 July 2026 | Open |
| A6 | Reconvene the LOPA team, complete Sections 6–8, band the residual gap at Revision 1, and route the worksheet to competent-person review | Lead Engineer — Process Safety | 2 August 2026 | Open |
| A7 | Record whether elimination / substitution / inherently safer design options for the overpressure demand were evaluated before finalising the IPL set (KB-SNIP-HOC) | Lead Engineer — Process Safety | 2 August 2026 | Open |
| A8 | Confirm enabling conditions and conditional modifiers — claim with provenance, or record "none" explicitly (Section 4.1) | Lead Engineer — Process Safety | 26 July 2026 | Open |

---

## 10. Consolidated [GAP] register

Every open value below is an engineer-supplied input awaiting the engineering team. None has been estimated, defaulted, or computed in this worksheet.

| # | [GAP] item | Worksheet section | Closing action |
|---|---|---|---|
| G1 | Consequence description, severity category, receptors, operating mode | 2 | A1 / A5 |
| G2 | Initiating-event description, category, frequency, and provenance | 4 | A1 |
| G3 | Enabling conditions and conditional modifiers (claimed or explicitly none) | 4.1 | A8 |
| G4 | Relief valve PFD and provenance | 5.1 | A2 |
| G5 | Relief valve independence from other IPLs / no-double-count confirmation | 5.1 | A2 |
| G6 | Existence and qualification of further candidate IPLs | 5.2 | A3 |
| G7 | Engineer-verified mitigated event frequency | 6 | A6 |
| G8 | Tolerable target frequency | 7 | A4 |
| G9 | SIF claim status and SIL target (if applicable) | 8 | A3 / A4 |

## 11. Assumptions register

| # | [ASSUMPTION] | Basis | To be confirmed by |
|---|---|---|---|
| AS1 | New scenario worksheet (not a review-update); no change-since-last-LOPA section | No prior worksheet referenced in the supplied scenario | Lead Engineer (role), 19 July 2026 |
| AS2 | Jurisdictional grounding: none — IEC 61511 method basis only; no statutory citation made | No jurisdiction supplied | Lead Engineer (role), 19 July 2026 |
| AS3 | Default 5×5 risk matrix held as placeholder for gap banding | No company matrix supplied | Lead Engineer (role), action A5 |
| AS4 | Internal engineering worksheet; audience: management and the process-safety team | Request was to format the scenario into the site worksheet; no external distribution stated | Lead Engineer (role), before any wider circulation |

---

## 12. Data protection and distribution

- All persons in this worksheet appear as **role/competency labels only** (DCS Operator; Lead Engineer). The document contains no name, government ID, address, phone number, email, or date of birth.
- The re-identification key is held in a **separate, access-controlled artifact** and is not reproduced or referenced in content here. Store the key apart from this document; do not attach it to any circulated copy.
- Injury figures are published only in aggregate: categories with fewer than 5 individuals are aggregated upward, with secondary suppression applied so suppressed cells cannot be back-calculated from the total (Section 2).
- If this worksheet is circulated beyond the site engineering team, re-check Sections 2, 3, and 9 for any role label that could indirectly identify an individual in a small team before release.

## 13. References

| Reference | Used for |
|---|---|
| KB-STD-IEC-61511 | LOPA/SIL method map — worksheet structure, IPL and SIL-link conventions |
| KB-SNIP-HOC | Hierarchy-of-controls ranking of the protection layers and recommendation A7 |

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*

> **Limitations.** This worksheet is decision-support only and is not a completed LOPA: it structures and records engineer-supplied, engineer-verified values, and it does not compute any PFD, derive any event frequency, or allocate any SIL — every unsupplied value stands as a literal [GAP] until the owning engineering team closes it. A competent person must review and approve this output before it is relied upon for any design, modification, safety-instrumented-system, or operational decision.
