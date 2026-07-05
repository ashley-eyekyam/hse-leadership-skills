<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3 with the full team session record. -->
# HAZOP Worksheet — Node 4: Reactor Feed Line

**Crude Unit, Site‑X** · Node‑based HAZOP study to IEC 61882 (KB‑STD‑IEC‑61882) · OSHA PSM — Process Hazard Analysis element (USA)

---

## Document control

| Field | Entry |
|---|---|
| Study type | New HAZOP — write‑up of a completed team session (formatting of the session record; no new analysis performed) |
| Node under study | **Node 4 — Reactor Feed Line**, surge drum to reactor inlet, Crude Unit, Site‑X |
| Method | IEC 61882 guideword × parameter examination (KB‑STD‑IEC‑61882) |
| Risk matrix | Default 5×5 with process‑safety descriptors (loss‑of‑containment / escalation) — as selected by the team |
| Jurisdiction / regulatory frame | USA — recorded by the team as an OSHA PSM‑covered process; this study forms part of the PSM Process Hazard Analysis element for this node |
| Workshop session date | **[GAP]** — not stated in the supplied session record; insert from the scribe record |
| Worksheet issued | 5 July 2026 |
| Source documents (P&ID no./rev, line list, prior PHA, relief basis) | **[GAP]** — not recorded in the supplied extract; attach the document register before sign‑off |
| Distribution | De‑identified; internal circulation **[ASSUMPTION — distribution list not stated; confirm before wider circulation]** |
| Status | Recorded — **pending competent‑person review** (see Limitations) |
| Participants | Recorded as role/competency labels only; the re‑identification key is held in a separate access‑controlled artifact and is not reproduced in this document |

---

## 1. Node definition and design intent

**Node 4** is the bounded P&ID section from the **surge drum outlet to the reactor inlet** (reactor feed line), Crude Unit, Site‑X.

| Design‑intent parameter | Normal condition (as stated by the team) |
|---|---|
| Service | Continuous crude feed, surge drum → reactor inlet |
| Flow | 120 m³/h |
| Pressure | 12 barg |
| Temperature | 180 °C |

Deviations in Section 4 are judged against this stated intent.

**Parameters examined:** Flow · Pressure · Temperature · Composition
**Guidewords:** Standard IEC 61882 set — No / More / Less / Reverse / As‑well‑as / Part‑of / Other‑than

---

## 2. HAZOP team (roles and competencies)

The session record confirms a **full multidisciplinary team present** (process, operations, instrumentation/SIS, mechanical, chair/scribe). This worksheet therefore stands as the record of a performed study; no "study not yet performed" banner applies.

| Discipline | Participant (role label) | Competency / basis in the record |
|---|---|---|
| Chair / Scribe | HAZOP Chair–Scribe (role) | Facilitation and recording; discipline confirmed present |
| Process | Process Engineer (role) | Process‑safety competency (per record); owner R1, R5, R6 |
| Operations — panel | Panel Operator (role) | Operations competency (per record) |
| Operations — line management | Operations Superintendent (role) | Owner R3 — **[ASSUMPTION:** attending as the operations line representative; confirm in the attendance record**]** |
| Instrumentation / SIS | Instrument Engineer (role) | Owner R2 — **[ASSUMPTION:** the attending instrumentation/SIS representative; confirm in the attendance record**]** |
| Mechanical | Mechanical Engineer (role) | Owner R4 — **[ASSUMPTION:** the attending mechanical representative; confirm in the attendance record**]** |

---

## 3. Guideword × parameter examination record

| Guideword | Flow | Pressure | Temperature | Composition |
|---|---|---|---|---|
| No | **D3** | † | † | † |
| More | † | **D1** | **D5** | † |
| Less | **D2** | † | † | † |
| Reverse | **D4** | † | NC — justified | † |
| As‑well‑as | † | † | † | **D6** |
| Part‑of | † | NC — justified | † | † |
| Other‑than | † | † | † | † |

**NC — justified:** closed **"not credible — justified"** by the team in session (Reverse × Temperature; Part‑of × Pressure).

**† :** The team's record states that **every guideword × parameter cell was examined** and that cells with no credible deviation were closed "not credible — justified", naming the two closures above **plus five further cells so closed**. The identities of those five cells — and the per‑cell disposition of the remaining combinations — were not included in the supplied session extract. **[GAP:** attach the scribe's full cell‑by‑cell record before study sign‑off; † cells must not be treated as closed until it is on file**]**.

**Examination summary:** 6 deviations recorded (D1–D6) · 2 named + 5 unnamed cells closed not credible · 6 recommendations raised (R1–R6, all open) · 0 safeguard sets relying on PPE.

---

## 4. Deviation worksheet — as recorded by the team

HoC key (classification convention per KB‑SNIP‑HOC): **E** = engineering control (hardwired trip, relief device, mechanical device, automatic control) · **A** = administrative control (alarm requiring operator response, procedure, routine).

| Ref | Guideword × Parameter | Deviation | Cause | Consequence | Existing safeguards (HoC) | Team risk rank (5×5) | Rec. |
|---|---|---|---|---|---|---|---|
| **D1** | More × Pressure | High pressure | Blocked outlet | Line overpressure / loss of containment | PSV‑401 relief valve, sized for the blocked‑outlet case (E) · High‑pressure alarm (A) · High‑pressure trip (E) | **High** before safeguards → **Medium** residual | R1 |
| **D2** | Less × Flow | Low feed flow | Feed pump degradation | Reactor upset | Low‑flow alarm (A) · Standby pump auto‑start (E) | **Medium** — single rank as recorded (see §6 note) | R2 |
| **D3** | No × Flow | No feed flow | Pump trip / feed valve fails closed | Thermal excursion | Trip alarm (A) · Standby pump (E) · Operating procedure (A) | **High** → **Medium** residual | R3 |
| **D4** | Reverse × Flow | Reverse flow | Pump stop | Backflow to surge drum | Discharge check valve (E) | **Medium‑Low** — single rank as recorded (see §6 note) | R4 |
| **D5** | More × Temperature | High feed temperature | Preheater control failure | Feed above design temperature (intent: 180 °C) | TI alarm (A) · Preheater trip (E) | **Medium** — single rank as recorded (see §6 note) | R5 |
| **D6** | As‑well‑as × Composition | Water present in feed (composition as‑well‑as) | Water carry‑over from the surge drum | Water slug to the hot circuit | Drum level control (E) · Low‑point drain routine (A) — **the team judged this administrative routine insufficient for the consequence severity** | **[GAP]** — no matrix rank recorded in session; team to rank at record review | R6 |

---

## 5. Hierarchy‑of‑controls review of existing safeguards (KB‑SNIP‑HOC)

| Line | Highest‑order existing safeguard | Admin/PPE‑only? | Team adequacy judgement and HoC action raised |
|---|---|---|---|
| D1 | Engineering (PSV‑401; high‑pressure trip) | No | Residual Medium accepted subject to R1 (sizing‑basis verification) |
| D2 | Engineering (standby pump auto‑start) | No | Alarm‑dependent detection; R2 evaluates a **low‑flow trip interlock — a higher‑order engineering control** |
| D3 | Engineering (standby pump) | No | R3 verifies the auto‑start's proof‑test interval |
| D4 | Engineering (discharge check valve) | No | R4 places the check valve under mechanical‑integrity assurance |
| D5 | Engineering (preheater trip) | No | R5 verifies the trip setpoint against the design limit |
| D6 | Engineering (drum level control) | No | The team judged the **administrative** low‑point drain routine insufficient for the consequence severity; R6 evaluates **automatic water draw‑off (engineering control)** to replace reliance on it |

No deviation line relies on an administrative‑ or PPE‑only safeguard set; no PPE‑order safeguards appear anywhere on this node. No elimination‑ or substitution‑order measures were raised by the team for this node. Where the team judged an administrative safeguard inadequate (D6), the recommendation raised moves **up** the hierarchy, consistent with KB‑SNIP‑HOC.

---

## 6. Risk‑ranking record

Ranks are the team's judgements on the **default 5×5 matrix with process‑safety descriptors (loss‑of‑containment / escalation)**, as selected in session. This worksheet records them; it does not re‑score them.

- **Before/after split recorded:** D1 (High → Medium) and D3 (High → Medium residual).
- **Single rank recorded:** D2 (Medium), D4 (Medium‑Low), D5 (Medium). The record does not state whether these are before or after existing safeguards — **[GAP:** team to confirm at record review; until confirmed, treat conservatively as unmitigated**]**.
- **No rank recorded:** D6 — **[GAP]** (Section 4).

---

## 7. Recommendation register — tracked to closure

All six recommendations carry a role owner, a due date, and a node link, and per the session record are entered in the site action‑tracking system. Register validated for completeness of owner + due date + node link + closure measure.

| Ref | Recommendation (as recorded) | HoC character of the action | Owner (role) | Due date | Node link | Status | Closure evidence required |
|---|---|---|---|---|---|---|---|
| **R1** | Verify PSV‑401 sizing basis against the current feed case | Verification of an existing engineering control | Process Engineer (role) | 30 July 2026 | Node 4 / D1 | Open | Documented sizing‑basis check against the current feed case |
| **R2** | Evaluate a low‑flow trip interlock | Engineering — higher order than the existing alarm | Instrument Engineer (role) | 15 August 2026 | Node 4 / D2 | Open | Documented evaluation with an accept/reject decision |
| **R3** | Confirm the standby‑pump auto‑start proof‑test interval | Verification of an existing engineering control | Operations Superintendent (role) | 30 July 2026 | Node 4 / D3 | Open | Confirmed proof‑test interval on record |
| **R4** | Include the discharge check valve in the mechanical‑integrity programme | Assurance of an existing engineering control | Mechanical Engineer (role) | 15 August 2026 | Node 4 / D4 | Open | Check valve listed in the MI programme scope |
| **R5** | Verify the preheater trip setpoint against the design limit | Verification of an existing engineering control | Process Engineer (role) | 30 July 2026 | Node 4 / D5 | Open | Setpoint‑versus‑design‑limit verification record |
| **R6** | Evaluate automatic water draw‑off | Engineering — replaces reliance on an administrative routine | Process Engineer (role) | 29 August 2026 | Node 4 / D6 | Open | Documented evaluation with an implementation decision |

---

## 8. Gaps and assumptions register

| Ref | Type | Item | Action to close |
|---|---|---|---|
| GAP‑1 | [GAP] | Workshop session date not in the supplied record | Insert from the scribe record |
| GAP‑2 | [GAP] | Source documents (P&ID number/revision, line list, prior PHA, cause & effect / SIS spec, relief‑system basis) not recorded | Attach the document register before sign‑off |
| GAP‑3 | [GAP] | Identities of the five additional "not credible — justified" closures, and per‑cell dispositions of the remaining matrix cells (§3) | Attach the full cell‑by‑cell scribe record |
| GAP‑4 | [GAP] | D6 carries no risk rank | Team to rank D6 at record review |
| GAP‑5 | [GAP] | D2 / D4 / D5 single ranks — before/after‑safeguards basis not stated | Team to confirm at record review |
| A‑1 | [ASSUMPTION] | Recommendation owners (Instrument Engineer, Operations Superintendent, Mechanical Engineer — roles) are the attending discipline representatives | Confirm against the attendance record |
| A‑2 | [ASSUMPTION] | Internal, de‑identified distribution to a management/consultant audience | Confirm the distribution list; re‑check de‑identification before any wider circulation |

---

## 9. Regulatory and standards basis

- **Method:** IEC 61882 node‑based HAZOP — guideword × parameter examination, deviation/cause/consequence/safeguard/recommendation record (KB‑STD‑IEC‑61882).
- **Regulatory frame:** USA — the team records this unit as an **OSHA PSM‑covered process**; this worksheet forms part of the Process Hazard Analysis element of the site's PSM programme for Node 4. Recommendation tracking to closure (Section 7) supports that element.
- **Control selection:** hierarchy of controls applied to every safeguard and recommendation per KB‑SNIP‑HOC.

## 10. Data protection statement

Participants appear in this worksheet as role/competency labels only. Identifiers detected in the source session record — two participant names, one phone number, one government ID, and one home address — were replaced with the role labels used throughout this document. The re‑identification key is held in a **separate, access‑controlled artifact**; it is not reproduced here, and no name‑to‑label mapping appears in this document. No injury, illness, or other health detail is included in this worksheet.

---

## Limitations

This worksheet is **decision‑support only**. The AI skill structured and recorded the workshop; the hazard identification, causes, consequences, safeguards, risk ranks, and recommendations are the findings of the multidisciplinary team named in Section 2, and unsupplied values are marked **[GAP]** rather than estimated. This document does not constitute — and must not be presented as — competent‑person approval. A **competent person** (the HAZOP chair / site process‑safety authority) must review this output, including the gaps and assumptions register in Section 8, before it is relied upon, filed as part of the PSM PHA record, or actioned.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
