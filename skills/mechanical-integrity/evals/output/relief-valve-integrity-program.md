<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3. -->
# Mechanical Integrity Register — Relief-Valve Population, Crude Unit, Site-X

**Document type:** Criticality-ranked equipment register with deficiency-remediation plan (PSM element (j) — mechanical integrity, KB-STD-PSM)
**Prepared:** 5 July 2026
**Status:** DRAFT — pending competent-person review and closure of the recorded [GAP] items
**Audience:** Site management and asset-integrity function [ASSUMPTION: management audience, internal distribution — not confirmed in the request]
**Source input:** "Integrity Review — Relief-Valve Population (Crude Unit, Site-X)" (de-identified extract supplied by the user)

---

## 1. Scope and basis of this register

| Captured fact | Value | Flag |
|---|---|---|
| Task | Build the integrity register (criticality-ranked equipment register + deficiency-remediation plan) from the attached equipment review | [ASSUMPTION: "build the integrity register" interpreted as register + deficiency plan; the attached review contains one open deficiency, so deficiency management is in scope] |
| Equipment population / unit | Relief-valve population, Crude Unit, Site-X | Supplied |
| Equipment classes in scope | Relief devices — PRVs (activates the relief-device test-interval section, §5) | Supplied |
| Consequence-of-failure / likelihood drivers | Not supplied for any item; only the criticality **band** (High) is supplied for PSV-204 | [GAP] |
| Current ITPM basis (intervals, methods, RBI, IOWs) | Not supplied | [GAP] |
| Inspection / MI records held | The integrity review extract itself. PSV-204's "overdue test" status implies test records exist, but none were supplied | [GAP: underlying test records, thickness/CML data, RBI study, corrosion-rate data — none supplied] |
| Open deficiencies | One: PSV-204 overdue test (High criticality band) | Supplied; interim risk **not** stated → [GAP] |
| Inspection authority / owner of the ITPM basis | Lead Inspector (role) — inspection-competency role per the review | [ASSUMPTION: the Lead Inspector (role) is the inspection authority; the review names this role as remediation owner and inspection-competency holder] |
| Risk matrix | Default 5×5 (consequence of failure × likelihood) | [ASSUMPTION: no site matrix supplied; default adopted. PSV-204's High band is carried **as supplied** and has not been re-scored — the underlying consequence × likelihood score is a [GAP]] |
| Jurisdiction (statutory inspection hook) | Not supplied | [GAP — no jurisdiction-specific law, statutory form, or examination interval is cited anywhere in this register until the jurisdiction is confirmed] |
| Statutory examination obligations and due dates | Not supplied | [GAP] |
| ITPM / re-inspection cadence and next-due dates | Not supplied; only the qualitative status "overdue" for PSV-204 | [GAP] |

**Grounding.** This register implements PSM element (j) — mechanical integrity (KB-STD-PSM): equipment covered by the programme, written ITPM procedures, inspection and testing on a justified basis, deficiency management before further use or with documented interim safeguards, and quality assurance. Every control recommendation in §6 is ranked per the hierarchy of controls (KB-SNIP-HOC).

**Register discipline.** An item with no evidenced integrity basis reads **[GAP]** in this register. It is never recorded as fit-for-service, and no inspection interval, corrosion rate, or fitness conclusion has been invented to fill a blank.

---

## 2. Data protection and de-identification status

The source integrity review detected and pseudonymized the following identifier categories before this register was assembled: two personal names, one phone number, one government identity number, and one home address. All appear in this document only as stable role labels — **Lead Inspector (role)** and **Reliability Engineer (role)**. The re-identification key is held in a separate, access-controlled artifact and is not reproduced or referenced in this document; store it apart from any circulated copy.

The review also reported **12 recordable injuries this period**, with categories of fewer than 5 individuals aggregated and secondary suppression applied so suppressed cells cannot be back-calculated. That figure is outside the scope of an asset-integrity register; it is carried here in aggregate form only and is not analysed further.

This register contains no personal name, government ID, address, phone number, email, date of birth, or name-to-label mapping, and is suitable for internal circulation in its current form. Warn recipients before any wider distribution.

---

## 3. Criticality-ranked equipment register

One row per item. Criticality = consequence of failure × likelihood on the default 5×5 matrix [ASSUMPTION: default matrix — see §1].

| # | Equipment | Class | Service / protected equipment | Consequence × likelihood | Criticality band | Integrity basis held | ITPM method | Test interval | Last test | Next test due | Status | Deficiency ref | Owner (role) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PSV-204 | Relief device (PRV) | [GAP — protected system not identified in the review] | [GAP — drivers not supplied; band carried as given] | **High** (as supplied by the integrity review) | [GAP — no test record or inspection report supplied] | [GAP] | [GAP] | [GAP] | [GAP] | **OVERDUE TEST** (as supplied) | D-001 (open — §6) | Lead Inspector (role) |
| 2 | All other relief devices in the Crude Unit population | Relief devices (PRVs) | [GAP] | [GAP] | [GAP] | [GAP — inventory not supplied] | [GAP] | [GAP] | [GAP] | [GAP] | **[GAP] — not assumed fit-for-service** | — | Reliability Engineer (role) (register completion — action A-04) |

**Register status:** SKELETON. The attached review supplied a one-row deficiency extract, not the population inventory. Until actions A-01 and A-04 (§7) close, this register bounds the population by name only ("relief-valve population, Crude Unit, Site-X") and every unlisted or unevidenced item reads [GAP]. No item in this population is recorded as fit-for-service on the strength of this document.

---

## 4. Integrity-operating-windows (IOW) framing

No IOWs were supplied for the Crude Unit → **[GAP]**. When the population inventory and service data arrive (A-04), define for each protected system the operating parameters whose excursion would invalidate the relief-device sizing or integrity basis (at minimum: operating pressure and temperature limits relative to the relief design basis, and any fouling/corrosive-service indicator that accelerates degradation of the device). Each IOW needs a defined limit, a monitoring route, and a defined response to excursion, owned by a named role. No IOW limit values are proposed here — none can be derived from the supplied inputs.

---

## 5. Relief-device test-interval basis (class branch — PRVs in scope)

No test interval is set or endorsed in this register, because every input that justifies one is missing. The interval for each PRV must be set and documented by the **Lead Inspector (role)** as inspection authority, justified against all four of:

1. **Statutory examination obligations** for the confirmed jurisdiction — [GAP: jurisdiction unconfirmed; no statutory interval or form is cited until it is].
2. **The site's adopted code / recognised-good-engineering-practice basis** for relief-device testing — [GAP: not supplied].
3. **As-found test history** — pass/fail and as-received condition from prior bench tests — [GAP: no test records supplied].
4. **Service severity** — fouling, corrosive, or plugging service that shortens the justified interval — [GAP: service data not supplied].

Any **extension** of a test interval requires documented as-found evidence and the inspection authority's written justification; an extension is never granted by default and never inferred from an absence of failures.

---

## 6. Deficiency management plan

### D-001 — PSV-204: overdue test (open)

| Field | Value |
|---|---|
| Equipment | PSV-204 (relief device, Crude Unit, Site-X) |
| Criticality band | High (as supplied) |
| Deficiency | Test overdue — the overpressure-protection function is currently **unverified** |
| Interim risk | **[GAP]** — not stated in the review. Continued operation of the protected system with an unverified relief device must not be authorized until the interim risk is assessed (action A-02) |
| Remediation owner | Lead Inspector (role) |
| Target closure | 26 July 2026 [ASSUMPTION: proposed target — confirm with the accountable roles] |
| Status | OPEN |

**Remediation controls, ranked per the hierarchy of controls (KB-SNIP-HOC):**

| Rank | Control tier | Control | Owner (role) | Timing |
|---|---|---|---|---|
| 1 | Engineering (restores the protective function — the highest-order control reasonably applicable) | Remove PSV-204 for bench test and recertification, **or** install a certified in-date spare of the correct set pressure and capacity, so that verified overpressure protection is restored | Lead Inspector (role) | By 26 July 2026 [ASSUMPTION: proposed target] |
| 2 | Engineering verification (interim) | Field-verify the relief path is available now: confirm the car-seal/lock-open status of any isolation valves between PSV-204 and the protected equipment, and confirm whether a parallel or spare relief path exists and is in service | Lead Inspector (role) | By 8 July 2026 [ASSUMPTION: proposed target] |
| 3 | Administrative (interim, pending rank 1) | Documented interim risk assessment and deviation authorization for any continued operation; operating restriction holding the protected system within its safe operating envelope with heightened monitoring of operating pressure against the relief design basis | Operations Superintendent (role) [ASSUMPTION: operations-owner role to be confirmed], with the Lead Inspector (role) | Before any continued operation; by 8 July 2026 |
| 4 | PPE | **Not applicable — and no PPE-only treatment is offered.** PPE provides no protection against loss of overpressure protection on process equipment | — | — |

**Hierarchy justification.** Elimination and substitution of the hazard are not reasonably practicable for an overdue protective-device test: the deficiency *is* the degraded engineering control. The highest-order effective response is therefore to restore the engineering control itself (rank 1); the administrative measures at rank 3 are interim only and expire on closure of rank 1. A deficiency of this class closed on administrative controls alone would be flagged as non-conforming.

---

## 7. SMART actions tracked to closure

Due dates are proposed targets [ASSUMPTION — confirm with the accountable roles]; owners are role labels only.

| ID | Action | Owner (role) | Due | Measure of closure (evidence) | Equipment link | Status |
|---|---|---|---|---|---|---|
| A-01 | Retrieve PSV-204 test records; enter last-test date, test method, interval, and interval basis into the register (§3, row 1) | Lead Inspector (role) | 12 July 2026 | Register row 1 [GAP] fields replaced with evidenced values; source records referenced | PSV-204 | Open |
| A-02 | Assess the interim risk of continued operation with PSV-204's test overdue; decide interim measures or shutdown of the protected system; document the deviation authorization | Lead Inspector (role) + Operations Superintendent (role) [ASSUMPTION: role to be confirmed] | 8 July 2026 | Signed interim risk assessment on file; D-001 interim-risk [GAP] closed; interim measures in force or system shut down | PSV-204 | Open |
| A-03 | Bench-test and recertify PSV-204, or install a certified in-date spare; restore verified overpressure protection; update the register and close D-001 | Lead Inspector (role) | 26 July 2026 | Test/recertification certificate on file; D-001 status = CLOSED; register row 1 status updated | PSV-204 | Open |
| A-04 | Compile the full Crude Unit relief-valve inventory with service, protected equipment, consequence-of-failure and likelihood drivers; score criticality for every item on the confirmed matrix; populate §3 one row per item | Reliability Engineer (role) | 26 July 2026 | Register §3 holds one evidenced row per device; no unlisted devices remain | Full population | Open |
| A-05 | Confirm the jurisdiction and enumerate the statutory examination obligations and due dates applying to this population; add the statutory hook to §5 | Lead Inspector (role) | 19 July 2026 | Jurisdiction [GAP] closed; statutory obligations and due dates entered against each device | Full population | Open |
| A-06 | Confirm the site risk matrix (or formally adopt the default 5×5) and the ITPM basis per class, including whether RBI is used and which IOWs apply; document in the MI programme | Reliability Engineer (role) | 2 August 2026 | Matrix and ITPM basis documented and owner-approved; §1 assumptions retired | Full population | Open |

---

## 8. Consolidated gap register

Every [GAP] below is an unevidenced input, not a defect finding. None has been bridged by assumption.

| # | Gap | Consequence while open | Closing action |
|---|---|---|---|
| G-1 | Interim risk of PSV-204 overdue test not stated | Continued operation of the protected system is unauthorized on the evidence held | A-02 |
| G-2 | PSV-204 test records, last-test date, interval, and interval basis not supplied | Register row 1 cannot evidence an integrity basis | A-01 |
| G-3 | Full relief-valve population inventory not supplied | Register is a skeleton; unlisted items are unbounded | A-04 |
| G-4 | Consequence-of-failure and likelihood drivers not supplied for any item | Criticality cannot be scored; PSV-204's High band rests on the source review alone | A-04 |
| G-5 | Jurisdiction unconfirmed | No statutory examination obligation, interval, or form can be cited | A-05 |
| G-6 | Statutory examination obligations and due dates not supplied | Compliance status of the population is unknown | A-05 |
| G-7 | ITPM basis (intervals, methods, RBI usage) not supplied for any class | No interval can be set or endorsed (§5) | A-06 |
| G-8 | IOWs not supplied | §4 framing cannot be populated with limits | A-06 |
| G-9 | Site risk matrix not supplied | Default 5×5 assumed, unconfirmed | A-06 |

## 9. Assumptions register

| # | Assumption | Bearing |
|---|---|---|
| AS-1 | "Build the integrity register" includes the deficiency-remediation plan for D-001 | Scope (§1) |
| AS-2 | Default 5×5 risk matrix pending site confirmation | §3 scoring frame |
| AS-3 | Lead Inspector (role) is the inspection authority / ITPM-basis owner | §5, §6 ownership |
| AS-4 | Management audience, internal distribution | §2 distribution posture |
| AS-5 | All action due dates are proposed targets, not commitments | §7 |
| AS-6 | An operations-owner role exists to hold interim operating restrictions | §6 rank 3, A-02 |

---

## 10. Competent-person review record

| Field | Entry |
|---|---|
| Reviewer (role) | _______________ |
| Competency basis (e.g. authorized inspector / statutory competent person, named as a role) | _______________ |
| Review date | _______________ |
| Outcome (accepted / accepted with amendments / rejected) | _______________ |

---

## Limitations

This register is **decision-support only**. It structures the mechanical-integrity information supplied and flags what is missing; it does not verify any equipment's condition, does not certify fitness-for-service, and does not constitute a statutory examination, an inspection report, or legal advice. Every [GAP] must be closed with evidence and every [ASSUMPTION] confirmed or corrected. **A competent person — the site's inspection authority and, where required, the statutory competent person for the confirmed jurisdiction — must review and approve this output before it is relied on or acted upon.**

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
