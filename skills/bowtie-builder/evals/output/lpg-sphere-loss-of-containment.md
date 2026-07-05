<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3 with the reconvened workshop's team-supplied barrier judgements. -->
# Bowtie Diagram & Barrier Register — Loss of Containment of LPG
## Storage Sphere, Site-X

| Document control | |
|---|---|
| Artifact | Bowtie diagram + barrier register (CCPS/EI bowtie method — KB-STD-CCPS-BOWTIE) |
| Basis | Bowtie workshop and reconvened workshop, barrier judgements dated 28 June 2026 |
| Prepared | 5 July 2026 |
| Status | DRAFT — for competent-person review before use or circulation |
| Barrier-judgement owners | Process Safety Engineer (role) · Sphere Operator (role) |
| Next scheduled barrier review | 28 June 2027 |
| Sector | Process / chemicals — [ASSUMPTION: process-sector framing; the installation is an LPG storage sphere and no mining principal-hazard framing was requested] |
| Scope | Plain bowtie diagram with barrier register — [ASSUMPTION: the request was to format the workshop notes into the diagram; a full ICMM Critical Control Management plan was not requested and is offered as a follow-on (see Action A8)] |
| Risk matrix | Default 5×5 (team-selected) |
| Jurisdiction | UK — COMAH establishment (team-supplied) |
| Classification | De-identified; internal circulation — [ASSUMPTION: internal management audience; no wider distribution was specified] |

---

## 1. Data protection statement

This record is de-identified. All workshop participants appear as role/competency labels only; no name, contact detail, government identifier, address, phone, email, or date of birth appears in this document. The re-identification key is held in a separate, access-controlled artifact and is not reproduced or referenced further here — it must be stored apart from this document with access restricted to those who need it. Injury figures supplied with the notes are carried at the aggregation level supplied: categories containing fewer than 5 individuals have been aggregated, with secondary suppression applied so suppressed cells cannot be back-calculated from totals.

---

## 2. Scope and definitions

**Hazard:** LPG held under pressure in the storage sphere at Site-X — a pressurised, liquefied, flammable gas inventory.

**Top event (one per bowtie):** Loss of containment of LPG from the storage sphere.

**Site context supplied with the notes (not an input to the barrier judgements; retained for record completeness):** 12 recordable injuries this period, reported at the aggregation level described in §1.

**Assistive basis:** the threats, consequences, barriers, performance standards, and residual-risk bands recorded below are the workshop team's judgements, as supplied on 28 June 2026. This document structures and records those judgements; it adds no barrier, threat, or consequence of its own. Where the team supplied no evidence, a literal [GAP] is recorded — no barrier is declared effective without a stated performance standard.

---

## 3. Workshop participants and competencies (role labels)

| Role label | Competency | Contribution |
|---|---|---|
| Process Safety Engineer (role) | Process-safety / barrier judgement | Co-owner of the barrier judgements |
| Sphere Operator (role) | Operations | Co-owner of the barrier judgements; operational barrier knowledge |
| Critical-Control Owner (role) | Barrier verification | Verification activities and test regimes |

Barrier judgements were made on 28 June 2026; the next review is due 28 June 2027.

---

## 4. Bowtie diagram

```
 THREATS              PREVENTIVE BARRIERS                                      MITIGATIVE BARRIERS                     CONSEQUENCES

 T1 ──▶ [PB1] ──▶ ┐                                                ┌──▶ [MB1] ─▶ [MB3] ─▶ [MB4] ──▶  C1  Flash fire
 T2 ──▶ [PB2] ──▶ ┤                                                │
 T3 ──▶ [PB3] ──▶ ┼──▶  ◆ TOP EVENT: Loss of containment of  ──▶ ──┼──▶ [MB2] ─▶ [MB3] ─▶ [MB4] ──▶  C2  BLEVE
 T4 ──▶ [PB4] ──▶ ┤       LPG from the storage sphere              │
 T5 ──▶ [PB5] ──▶ ┘                                                └──▶ [MB3] ─▶ [MB2] ─▶ [MB4] ──▶  C3  Jet fire

 HAZARD: LPG held under pressure in the storage sphere (Site-X)
```

**Legend**

| ID | Threat / consequence / barrier |
|---|---|
| T1 | Line break on connected transfer pipework |
| T2 | Overfilling during receipt |
| T3 | External corrosion of shell/nozzles |
| T4 | Vehicle impact on sphere legs |
| T5 | Overpressure from fire impingement |
| C1 | Flash fire due to delayed ignition of a dispersing cloud |
| C2 | BLEVE due to prolonged fire impingement on the sphere |
| C3 | Jet fire due to immediate ignition of a pressurised leak |
| PB1–PB5 | Preventive barriers (§5) |
| MB1–MB4 | Mitigative barriers (§6) |

**Mapping note — [ASSUMPTION]:** the team supplied the threat list, consequence list, and barrier inventory, but not an explicit barrier-to-line mapping. The threat-side mapping (PB1↔T1 … PB5↔T5) follows directly from each barrier's stated function. The consequence-side ordering (which mitigative barriers sit on which consequence line, and in what sequence) is the facilitator's structuring of the team-supplied inventory and must be confirmed by the team at or before the next review (Action A7).

---

## 5. Threat lines (prevention — left side)

| Line | Threat | Preventive barrier | Barrier ID |
|---|---|---|---|
| L1 | T1 — Line break on connected transfer pipework | Excess-flow valves | PB1 |
| L2 | T2 — Overfilling during receipt | High-level trip on receipt | PB2 |
| L3 | T3 — External corrosion of shell/nozzles | Coating + external inspection programme | PB3 |
| L4 | T4 — Vehicle impact on sphere legs | Vehicle barriers around sphere legs | PB4 |
| L5 | T5 — Overpressure from fire impingement | Pressure relief to flare | PB5 |

**Observation (for the team, not a declared inadequacy):** every threat line currently carries a single preventive barrier. Single-barrier lines on a major-accident bowtie warrant an explicit team decision on barrier adequacy/redundancy at the next review. No additional barrier has been assumed or added here.

---

## 6. Barrier register (consolidated)

Each barrier is recorded with the team's performance standard (PS) and verification activity. A barrier is carried as *team-judged* only where the team supplied that judgement; nothing is declared effective without a stated performance standard.

### 6.1 Preventive barriers

| ID | Barrier | HoC tier | Performance standard (team-supplied) | Verification activity & frequency | Effective · independent · auditable |
|---|---|---|---|---|---|
| PB1 | Excess-flow valves | Engineering | Closes within 2 seconds at rated flow on line break | Quarterly function test | **Team-judged effective · independent · auditable** (28 June 2026) |
| PB2 | High-level trip on receipt | Engineering | Trips at 85% level | Proof test six-monthly | PS stated; verification auditable — explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |
| PB3 | Coating + external inspection programme | Engineering (coating) with administrative inspection element | Full visual inspection every 12 months; thickness survey five-yearly | Inspection programme per PS | PS stated; verification auditable — explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |
| PB4 | Vehicle barriers around sphere legs | Engineering | Rated to site vehicle impact — rating value not stated → **[GAP]** (Action A5) | Annual integrity check | PS partially stated; explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |
| PB5 | Pressure relief to flare | Engineering | Set at design pressure | Statutory test interval — interval value / written-scheme reference not stated → **[GAP]** (Action A4) | PS stated; explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |

*Record note:* the reconvened workshop's performance standard for PB1 (closes within 2 seconds at rated flow) supersedes the earlier register extract's unquantified "closes within rated time"; the quarterly function test is common to both records.

### 6.2 Mitigative barriers

| ID | Barrier | HoC tier | Performance standard (team-supplied) | Verification activity & frequency | Effective · independent · auditable |
|---|---|---|---|---|---|
| MB1 | Gas detection — alarm at 20% LEL | Engineering (detection) with administrative response element | Alarm at 20% LEL. The operator response action that completes this detect-decide-act barrier is not defined → **[GAP]** (Action A6) | Quarterly bump test | PS stated for the detection element only; explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |
| MB2 | Water deluge on the sphere | Engineering (automatic initiation; manual back-up is an administrative element) | Activates at 68 °C quartzoid bulb or manual | Annual full-flow test | PS stated; explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |
| MB3 | Remotely-operated isolation valve | Engineering (hardware) with administrative initiation (control-room action) | Closes from control room in under 10 seconds | Six-monthly stroke test | PS stated; explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |
| MB4 | Site emergency response team | Administrative | 5-minute muster | Muster drill quarterly | PS stated; explicit E·I·A determination not individually minuted → **[GAP]** (Action A1) |

---

## 7. Hierarchy-of-controls review (KB-SNIP-HOC)

**Elimination / substitution — considered and recorded.** The team considered inventory reduction (elimination-tier) and rejected it as not reasonably practicable this cycle. The team recorded a justification for that rejection; the justification text was not supplied to this document → **[GAP]** (Action A2). The rejection stands as a team decision to be revisited no later than the next review.

**Ranking of the credited barrier set.** All credited barriers were ranked through the hierarchy by the team, with the engineering barriers leading:

| Tier | Barriers |
|---|---|
| Elimination / substitution | None credited (inventory reduction considered and rejected — recorded above) |
| Engineering | PB1, PB2, PB3 (coating), PB4, PB5, MB1 (detection element), MB2, MB3 |
| Administrative | PB3 (inspection programme element), MB1 (response element — [GAP], Action A6), MB2 (manual-activation element), MB3 (control-room initiation element), MB4 |
| PPE | None credited |

**Hierarchy finding:** this is not an administrative/PPE-only barrier set — every threat line and every consequence line leads with an engineering barrier. No lower-order-only treatment requires justification. The administrative elements embedded in MB1–MB4 (operator response, manual activation, control-room initiation, ERT performance) are dependency points the verification regime in §6 must continue to exercise.

---

## 8. Residual risk (default 5×5, team-judged, barriers credited)

| Consequence | Residual band (team judgement, 28 June 2026) |
|---|---|
| C2 — BLEVE due to prolonged fire impingement on the sphere | **Medium** |
| C1 — Flash fire due to delayed ignition of a dispersing cloud | **Medium-Low** |
| C3 — Jet fire due to immediate ignition of a pressurised leak | **Medium-Low** |

The underlying likelihood × severity coordinates on the default 5×5 were not supplied → **[GAP]** (Action A3). The unmitigated (barriers-not-credited) risk position was not assessed or supplied → **[GAP]**; without it, the risk-reduction claim of the barrier set cannot be demonstrated quantitatively in this record.

---

## 9. Barrier-verification and gap-closure actions

Owners are role labels. No target dates earlier than the next scheduled review were supplied, so all actions fall due at the next barrier review — [ASSUMPTION: the team may reasonably choose to close A1, A4, and A6 sooner, as they bear directly on barrier defensibility].

| ID | Action (SMART) | Owner (role) | Due | Done when |
|---|---|---|---|---|
| A1 | Minute the explicit effective · independent · auditable determination for PB2–PB5 and MB1–MB4 (currently minuted only for PB1) | Process Safety Engineer (role) | 28 June 2027 | Each barrier row in §6 carries a dated team E·I·A determination |
| A2 | Append the recorded justification for rejecting inventory reduction to this document's record | Process Safety Engineer (role) | 28 June 2027 | §7 carries the justification text verbatim from the workshop record |
| A3 | Record the likelihood × severity coordinates behind each residual band on the default 5×5 | Process Safety Engineer (role) | 28 June 2027 | §8 shows L×S per consequence |
| A4 | Cite the statutory examination interval / written-scheme reference for PB5 (pressure relief to flare) | Critical-Control Owner (role) | 28 June 2027 | PB5's verification column names the interval and its source |
| A5 | Record the design impact rating of the vehicle barriers (PB4) against the site vehicle envelope | Critical-Control Owner (role) | 28 June 2027 | PB4's PS states the rating |
| A6 | Define the operator response action (and its performance standard) that completes the gas-detection barrier MB1 | Process Safety Engineer (role) | 28 June 2027 | MB1's PS covers detect → decide → act, not the alarm alone |
| A7 | Confirm or correct the mitigative-barrier-to-consequence mapping shown in §4 | Process Safety Engineer (role) | 28 June 2027 | The team has signed the mapping into the workshop record |
| A8 | Decide whether to designate critical controls from this barrier set and build the ICMM CCM verification table (critical-control designation was not performed in this workshop) | Critical-Control Owner (role) | 28 June 2027 | A documented decision, and a CCM verification table if adopted |

---

## 10. Gaps and assumptions register

| Ref | Type | Item |
|---|---|---|
| G1 | [GAP] | Explicit E·I·A determinations not individually minuted for PB2–PB5, MB1–MB4 (Action A1) |
| G2 | [GAP] | Justification text for rejecting inventory reduction not supplied to this document (Action A2) |
| G3 | [GAP] | Likelihood × severity coordinates behind the residual bands not supplied (Action A3) |
| G4 | [GAP] | Statutory test interval value / written-scheme reference for PB5 not stated (Action A4) |
| G5 | [GAP] | Vehicle-barrier design impact rating for PB4 not stated (Action A5) |
| G6 | [GAP] | Operator response element completing MB1 not defined (Action A6) |
| G7 | [GAP] | Unmitigated (barriers-not-credited) risk position not assessed or supplied |
| G8 | [ASSUMPTION] | Mitigative-barrier-to-consequence mapping in §4 is facilitator structuring, pending team confirmation (Action A7) |
| G9 | [ASSUMPTION] | Plain bowtie scope (not a full ICMM CCM plan); process-sector framing; internal management audience |
| G10 | [ASSUMPTION] | Gap-closure due dates set to the next scheduled review in the absence of supplied targets |

---

## 11. Review and revalidation

Barrier judgements were made by the Process Safety Engineer (role) and Sphere Operator (role) on 28 June 2026. The next barrier review is due **28 June 2027**. This bowtie must also be revisited on any modification to the sphere, its pipework, its instrumented protection, or the site vehicle envelope, and after any loss-of-containment event or barrier-test failure — whichever comes first.

---

## 12. Jurisdiction note

The team identified the installation as a UK **COMAH establishment**. This bowtie and barrier register can support the establishment's major-accident-hazard documentation, but no specific statutory citation is made here; the competent person reviewing this output should confirm alignment with the establishment's safety documentation and current UK requirements. Method grounding: CCPS/EI bowtie and barrier method with the ICMM Critical Control Management map (KB-STD-CCPS-BOWTIE); control ranking per the hierarchy of controls (KB-SNIP-HOC).

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*

---

## Limitations

This document is **decision-support only**. It structures and records the workshop team's own barrier judgements; it does not independently verify any barrier, and no barrier is declared effective here without the team's stated performance-standard evidence. It is not legal advice. A **competent person must review this output** — including the barrier judgements, the [GAP] and [ASSUMPTION] entries, the residual-risk bands, and the jurisdiction note — before it is relied upon, circulated, or used to support any regulatory demonstration.
