<!-- LOCKED fixture — owner-LOCKED at the SW4 19-05 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# CAPA Management Record — NC-07 (Emergency Lighting, Bay 3)

**CAPA ID:** CAPA-NC-07  ·  **Source:** Management-system audit finding (ingested / re-checked)  ·  **Framework:** ISO 45001:2018 cl. 10.2
**Record date:** 6 July 2026  ·  **Lifecycle status:** **OPEN — in progress** (nothing closed verified-effective)
**Classification:** Internal — competent-person review required

---

## De-identification statement (applied before drafting)

Inputs were scrubbed and re-checked before any analysis. **Identifiers detected: none.** All personnel appear as **role labels only** (Facilities Lead, Maintenance Manager, HSE Manager). No name, address, employee/ID number, contact detail, exact personal date, or health detail appears in this record. No re-identification key is embedded (none was required — the ingested finding was already role-labelled and is confirmed clean). No injury/illness data is present, so no small-number aggregation applies.

---

## 1. Finding — the anchor (ISO 45001 cl. 8.2)

| Field | Detail |
|---|---|
| **Finding** | **NC-07** — the emergency (life-safety) lighting serving **Bay 3** was **not tested at the documented test interval**. |
| **Detected** | During a management-system audit. |
| **Requirement breached** | ISO 45001 **cl. 8.2** (emergency preparedness & response — emergency lighting is an emergency-response provision that must be maintained and tested), read with **cl. 7.5** (documented information — the organisation's own documented test interval and retained test records) and the applicable **local fire-safety / emergency-lighting rule**. |
| **Nonconformity type** | Lapse in maintenance/testing of a life-safety system — a compliance and functional-reliability gap, not a design gap. |
| **Severity note** | Life-safety system. Until tested, there is **no evidence** the Bay 3 emergency lighting will function or hold its rated duration in a power failure or evacuation — hence the containment action below is treated as urgent. |

> **[GAP] — jurisdiction / governing standard not stated.** The specific *local fire rule* and its mandated test interval were not supplied. Confirm the governing standard and interval with a competent person before adopting any test frequency or duration below. Depending on jurisdiction the likely references are BS 5266-1 / EN 50172 (UK/EU), NFPA 101 & NFPA 111 (US), or IS 3646 (India) — **none is adopted here as fact.** The organisation's *own* documented interval (cl. 7.5) is the immediate benchmark and must be enforced regardless.

---

## 2. Root cause (established at intake — reused, not re-investigated)

| ID | Root-cause statement | Type | Evidence |
|---|---|---|---|
| **RC-1** | **No preventive-maintenance (PM) schedule exists for the life-safety lighting systems.** Testing was performed ad hoc, with no owned trigger, so a lapse of the documented interval went unnoticed. | **Systemic — procedural / management-system gap** (not individual error). | Audit finding NC-07; absence of any scheduled/owned PM record for the asset class. |

RC-1 reaches a **systemic** factor (an absent process), so each action below can trace to it. Every action carries `links_to_cause: RC-1`.

---

## 3. Action plan — correction · corrective · preventive (each HoC-tiered)

Three action classes are split per consultant practice and ISO 45001 cl. 10.2: **correction** (control/fix *this* occurrence) → **corrective action** (eliminate *the cause* so it does not recur) → **preventive action** (eliminate the cause of *potential* similar failures across the wider life-safety estate). Every action is ranked on the **hierarchy of controls** (ISO 45001 **cl. 8.1.2**).

### 3a. Correction / containment — control this occurrence now

| # | Action | HoC tier | Owner | Due | Effectiveness measure | Cause |
|---|---|---|---|---|---|---|
| **COR-1** | Immediately perform the **overdue functional + full-rated-duration test** of every Bay 3 emergency luminaire and illuminated exit sign; rectify or **replace** any luminaire, battery, or sign that fails; restore full rated duration. | **Correction — Administrative** (perform the test) **+ Engineering** (replace/rectify failed units) | Facilities Lead | **13 July 2026** | Signed, dated test record shows **100%** of Bay 3 emergency luminaires + exit signs function-tested and duration-tested to the standard's rated duration; **all** defects rectified and re-tested pass. | RC-1 |
| **COR-2** | Pending COR-1 completion, put an **interim risk control** on Bay 3: deploy temporary/portable emergency luminaires **or** restrict Bay 3 occupancy/operations during hours of darkness, and log the measure. | **Correction — Administrative (interim)** | Facilities Lead | **8 July 2026** | Interim control deployed and **recorded within 48 h**; Bay 3 not occupied after dark without a working emergency-lighting provision until COR-1 passes. | RC-1 |

### 3b. Corrective action — eliminate the cause so NC-07 does not recur

| # | Action | HoC tier | Owner | Due | Effectiveness measure | Cause |
|---|---|---|---|---|---|---|
| **CA-1** | Establish a **documented PM schedule for the life-safety lighting** in the CMMS, with **auto-generated, owner-assigned work orders** at the documented interval (routine function test + periodic full-duration test) and **automatic escalation of any missed test** to the HSE Manager. This removes the ad-hoc dependency that caused NC-07. | **Administrative** (documented, scheduled procedure) — hardened by **automated triggers/escalation** that remove reliance on memory | Maintenance Manager | **31 August 2026** | PM schedule live in CMMS covering **100%** of life-safety lighting assets; work orders auto-generate at the documented interval; **first cycle completed on time** with retained records; **zero** missed tests in cycle 1. | RC-1 |
| **CA-2** | Back-populate / reconstruct the **test-record set** for the life-safety lighting, and add **"life-safety lighting testing interval"** as a standing line item in the **internal audit scope** so the interval is independently verified. | **Administrative** (verification / assurance layer) | HSE Manager | **15 September 2026** | Records for the current period reconstructed and retained (cl. 7.5); life-safety lighting interval confirmed present in the internal audit checklist and scheduled for the next audit. | RC-1 |

### 3c. Preventive action — eliminate the cause of potential similar failures

| # | Action | HoC tier | Owner | Due | Effectiveness measure | Cause |
|---|---|---|---|---|---|---|
| **PA-1** | **Engineer out** the reliance on manual scheduling: specify and phase-in **self-testing (automatic-test) emergency luminaires with central/addressable monitoring** for the life-safety lighting, so function and duration tests run automatically and any failure is flagged without a human remembering to test. | **Engineering / Substitution** — highest-order control in this set (substitutes the manual regime with an engineered self-test) | Facilities Lead / Maintenance Manager | Approved spec + budgeted phased plan **30 September 2026**; first install milestone **31 March 2027** | Approved specification + phased installation plan issued by 30 Sep 2026; **% of life-safety luminaires converted to automatic-test/central-monitored** tracked against milestones; converted units self-report and flag failures. | RC-1 |
| **PA-2** | Extend the **same CMMS PM discipline to the wider life-safety / critical-safety asset estate** (e.g. fire detection, extinguishing systems, automatic-opening vents) so no other life-safety asset class relies on ad-hoc testing. | **Administrative** (systemic process extension) | Maintenance Manager | **31 October 2026** | Every life-safety/critical-safety asset class has an owned PM schedule in the CMMS with a defined interval; **0** asset classes on ad-hoc testing at review. | RC-1 |

**Hierarchy-of-controls justification (required check).** The action set is **not** PPE/admin-only: it contains an **Engineering/Substitution** control (**PA-1**). Emergency lighting cannot itself be *eliminated* — it *is* the safeguard — so the highest reasonably practicable control is to **engineer out reliance on manual testing** via automatic-test luminaires (PA-1), backed by an automated administrative scheduling/escalation layer (CA-1). PPE is not an applicable control for this failure mode. Where administrative controls are used (CA-1, CA-2, PA-2), a higher-order engineering option is either applied in parallel (PA-1) or not reasonably practicable for that specific assurance function.

---

## 4. Effectiveness verification schedule (the lifecycle step — floor: method + due + status)

No action is closed on completion of the *task*; each carries a scheduled **effectiveness check**, and the **overall CAPA** cannot move to *verified-effective* until the effectiveness review below is recorded.

| For | Verification method | Due | Owner | Status |
|---|---|---|---|---|
| COR-1 | Physical re-inspection **+** review of signed test record | **20 July 2026** | HSE Manager | **Scheduled** |
| COR-2 | Confirm interim control deployed and logged | **10 July 2026** | HSE Manager | **Scheduled** |
| CA-1 | CMMS compliance report after first full PM cycle (work orders generated & completed on time) | **30 September 2026** | HSE Manager | **Scheduled** |
| CA-2 | Internal audit re-check that records exist and the interval line item is in scope | **31 October 2026** | HSE Manager | **Scheduled** |
| PA-1 | Review of approved spec/plan, then sample of self-test logs at first install milestone | **31 March 2027** | Facilities Lead | **Scheduled** |
| PA-2 | Sample audit across other life-safety asset classes for an owned PM schedule | **30 November 2026** | HSE Manager | **Scheduled** |

**No verification is past due** (all dates fall after today, 6 July 2026).

### Overall CAPA effectiveness check — the gate to closure

| Field | Detail |
|---|---|
| **Method** | Re-audit + CMMS compliance report + physical sampling. |
| **Pass criteria** | After **≥2 completed function-test cycles** under the new PM schedule and at the **next internal audit**: CMMS shows **100%** of scheduled life-safety lighting tests completed **within the documented interval**, **zero** missed intervals; **Bay 3 plus ≥3 sampled areas** physically confirmed tested with records retained; and **no repeat finding** of a missed interval (a re-occurrence window is used as the effectiveness test). |
| **Fail handling** | Any missed interval or repeat finding → mark **verified-ineffective**, re-open the CAPA, and escalate PA-1 (engineering control) as the corrective for the failed administrative layer. |
| **Effectiveness review date** | **29 January 2027** |
| **Owner** | HSE Manager |
| **Current status** | **Scheduled — NOT yet verified-effective** |

---

## 5. Lifecycle status board

| Item | Status |
|---|---|
| COR-1 · overdue test + rectify Bay 3 | **In progress** |
| COR-2 · interim risk control | **In progress** |
| CA-1 · CMMS PM schedule + auto-escalation | **Open** |
| CA-2 · records back-load + audit scope | **Open** |
| PA-1 · self-testing luminaires (engineering) | **Open** |
| PA-2 · extend PM discipline to all life-safety assets | **Open** |
| **CAPA-NC-07 (overall)** | **OPEN / IN PROGRESS — pending effectiveness verification. Not closed, not verified-effective.** |

No item is marked `verified-effective` or `closed`; no effectiveness check has yet been recorded (per instruction and per ISO 45001 cl. 10.2 — a CAPA cannot be called effective without a recorded review).

---

## 6. Deterministic validation summary (QA gate)

- **SMART register completeness:** all **6** actions carry a named (role) owner **+** a due date **+** a measurable effectiveness measure **+** `links_to_cause` → **0 invalid**; `all_traced_to_cause = true` (every action → RC-1).
- **No anonymous owners; no "ASAP"/open-ended dates.**
- **Control ranking:** highest-order control in set = **Engineering / Substitution** (PA-1); **PPE/admin-only = false** → HoC gate passes.
- **Corrective/preventive split:** present for RC-1 (correction + corrective + preventive all populated).
- **Effectiveness check:** every action + the overall CAPA carry a `{method, due, status}`; none marked verified-effective.
- **De-identification:** re-checked, 0 residual identifiers.

---

## 7. Regulatory grounding

- **ISO 45001:2018 cl. 10.2** — incident, nonconformity & corrective action (react → correct → evaluate the need to eliminate the cause so it does not recur → implement corrective + preventive action → review effectiveness → retain documented evidence). *(Source: ISO 45001:2018.)*
- **ISO 45001:2018 cl. 8.1.2** — hierarchy of controls, applied to every action above. *(Source: ISO 45001:2018.)*
- **ISO 45001:2018 cl. 8.2** — emergency preparedness & response (the requirement NC-07 is against). **cl. 7.5** — documented information (the documented interval and retained test records).
- **Local fire-safety / emergency-lighting rule and its mandated test interval — [GAP], to be confirmed with a competent person** (jurisdiction not stated; see §1). No specific statute or national standard is cited as fact here.

---

## 8. Limitations & disclaimer

This CAPA record is **decision-support**, not legal advice or a regulatory determination. It must be **reviewed and signed off by a competent person** before it is relied upon or closed. Test intervals, rated durations, and the applicable local fire rule must be confirmed against the governing standard for the site's jurisdiction. This record does not itself constitute the audit (see `safety-audit`) or a full incident investigation (see `incident-investigation`); it manages the CAPA lifecycle for the supplied finding only, within this single invocation.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
