<!-- LOCKED fixture — owner-LOCKED at the SW1 19-02 review (CONV-5, 5 July 2026); do NOT edit without a new owner LOCK. Provenance: captured 5 July 2026 via local claude -p (Phase 19 / 19-02 SW1, D-01); scenario: evals.json case 3. -->
# Permit-to-Work Package — Hot Work (with SIMOPS Coordination)

## Pipe Rack, Unit 100 — Site-X

| Document control | |
|---|---|
| **Permit type** | Hot Work (welding) — with in-permit SIMOPS coordination section |
| **Permit number** | HW-U100-[GAP: serial to be assigned from the site permit register at issue] |
| **Task** | Welding on the pipe rack, Unit 100, Site-X |
| **Prepared** | 5 July 2026 |
| **Requested validity** | Day shift, 5 July 2026 — [ASSUMPTION] single-shift validity adopted as the conservative default; the site validity/shift-handover rule was not supplied |
| **Permit status** | **DRAFT — NOT VALID.** This permit is not valid until every pre-issue condition in Section 13 is confirmed in place: isolations confirmed, gas test passed, hot-work gate controls in place, and SIMOPS coordination controls confirmed (Sections 4–7). |
| **Audience** | Site management / permit office (M) — [ASSUMPTION] |
| **Sector / setting** | Process plant, live operating unit — [ASSUMPTION derived from "Unit 100" and "live unit" in the job notes] |
| **Jurisdiction** | [GAP: not supplied. No jurisdiction-specific statutory citations are made in this package; the competent person must confirm the jurisdiction and attach the applicable statutory hot-work requirements before issue.] |

**Data protection note:** all persons in this package are recorded as role labels only. The role-to-person assignment (re-identification key) is held in a separate, access-controlled artifact and must never be attached to, or circulated with, this document.

---

## 1. Permit scope summary (captured facts)

| # | Intake item | Captured value |
|---|---|---|
| 1 | Permit type | Hot work (welding) |
| 2 | Task and exact location | Welding on the pipe rack, Unit 100, Site-X. [GAP: the specific line/joint/equipment identifier to be welded, and the welding process (arc / oxy-fuel), were not supplied — record on the permit face before issue] |
| 3 | Energy isolations (LOTO) | [GAP: no isolation points or LOTO register extract supplied — see Section 10; permit cannot be issued until isolations are identified, applied, and recorded] |
| 4 | Atmosphere / gas test | Required — hot work adjacent to a live process unit (Section 6). [GAP: site gas-test acceptance criteria and retest frequency not supplied] |
| 5 | Type-specific hot-work gate | Fire watch + combustibles removed + extinguisher — mandatory (Section 5) |
| 6 | SIMOPS detected? | **Yes** — crane lift over the live unit, concurrent with the hot work (Section 7) |
| 7 | Coordinating / authorising authority | Area Authority (authorizing-authority role) |
| 8 | Permit parties | Permit Holder — task-supervisor role (performing authority); Area Authority — authorizing-authority role (issuer). [GAP: Authorized Gas Tester not yet assigned] |
| 9 | Permit conditions / validity | [ASSUMPTION] single shift, day shift 5 July 2026; revalidation required at any shift handover |
| 10 | Jurisdiction | [GAP: not supplied] |
| 11 | Source documents supplied | SIMOPS coordination extract only. [GAP: isolation/LOTO register, P&ID for isolation points, concurrent-permit register, and buried-services/lift-plan documents not supplied] |

---

## 2. Task and exact location

Hot work — welding — on the **pipe rack in Unit 100, Site-X**, while the unit remains **live** (in operation). The concurrent crane lift passes over the live unit in the same area.

- [GAP] The specific pipe, joint, or structural member to be welded is not identified in the job notes. The permit face must name the exact work piece (line number / rack bay / elevation) before issue — "the pipe rack" alone does not meet the specificity requirement of this permit system.
- [GAP] It is not stated whether the weld is on **in-service process piping**. If it is, this becomes a combined **hot work + line-breaking** scope and the line-break gate applies in full: drain / flush / depressurise plus double isolation, confirmed before any hot work starts.
- [GAP] Work position on the rack is not stated. If the welding position is above ground level, working-at-height controls (fall arrest or edge protection) and any site height-permit requirement must be added before issue.
- [GAP] Hot work over a live unit normally requires an elimination/substitution decision to be recorded: state why a cold-work alternative (bolted, clamped, or deferred-to-shutdown work) is not reasonably practicable before authorising welding over live plant (see Section 4).

---

## 3. Permit parties and competency (role labels only)

| Role | Function on this permit | Competency requirement | Status |
|---|---|---|---|
| Area Authority (authorizing-authority role) | Permit issuer; single point of coordination for SIMOPS (Section 7.4) | Authorised to issue hot-work permits for Unit 100; current in the site control-of-work system | Assigned |
| Permit Holder (task-supervisor role) | Performing authority; supervises the welding crew; owns worksite compliance with permit conditions | Competent task supervisor; briefed on this permit and the SIMOPS interlock | Assigned |
| Authorized Gas Tester (role) | Performs the initial and repeat gas tests; records results in Section 6 | Current gas-tester authorisation | **[GAP: not yet assigned — mandatory before issue]** |
| Fire Watch (role) | Continuous fire watch during hot work and for the site-standard period after last hot work | Trained fire watch; extinguisher at hand; no concurrent duties | **[GAP: not yet assigned — mandatory before issue]** |
| Lifting Operation Performing Authority (role) | Counterpart authority for the concurrent crane lift (cross-permit) | Per the lift permit | [GAP: cross-permit reference not supplied — Section 7.5] |

---

## 4. Hazard identification, isolations, and safeguards (hierarchy-of-controls ranked)

Every control below is ranked against the hierarchy of controls (KB-SNIP-HOC). Per the methodology for this permit system, **any isolation that relies on permit paperwork alone (administrative) without an engineered isolation is flagged** — and because no isolation register extract was supplied, **no engineered isolation is currently evidenced for this task. The permit is therefore not valid** (see Sections 10 and 13).

| # | Hazard | Control | HoC tier | Status / owner |
|---|---|---|---|---|
| H-1 | Ignition of flammable atmosphere or hydrocarbon release from the live unit by welding arc, sparks, or spatter | **First decision — elimination/substitution:** record why cold work (bolted/clamped repair, or deferral to shutdown) is not reasonably practicable before authorising hot work over live plant | Elimination / Substitution | **[GAP: justification not supplied — record before issue]** — Area Authority (role) |
| H-2 | Loss of containment at the work piece (if weld is on in-service piping) | Positive engineered isolation of the affected line: drain / flush / depressurise + double isolation, verified at the isolation points on the P&ID | Engineering | **[GAP: in-service status and isolation points not supplied]** — Area Authority (role) |
| H-3 | Stored/live energy at the work piece and adjacent services | Energy isolation (LOTO) applied, locked, tagged, and recorded in Section 10 | Engineering | **[GAP: LOTO points not supplied — permit invalid until confirmed]** — Area Authority (role) |
| H-4 | Sparks and hot slag falling to lower rack levels and grade — igniting combustibles or striking persons/equipment below | Physical spark containment: fire-resistant blankets/screens/habitat around and below the work point; drains and openings within the protected zone covered | Engineering | Open — Permit Holder (role) |
| H-5 | Combustible materials at or near the work point | Combustibles removed from the work area, or protected where removal is impracticable, before hot work starts; clearance radius per site standard [GAP: site-standard radius not supplied] | Administrative (supported by the engineered containment at H-4) | Open — Permit Holder (role) |
| H-6 | Undetected flammable atmosphere developing during the work | Gas test before issue plus repeat/continuous monitoring per Section 6; automatic stop-work on any gas alarm | Administrative (detection/monitoring) | Open — Authorized Gas Tester (role) |
| H-7 | Delayed ignition / smouldering after hot work ends | Fire watch maintained during hot work and for the site-standard period after last hot work [GAP: duration per site standard — not supplied]; extinguisher at the work point | Administrative | Open — Fire Watch (role) |
| H-8 | Suspended load over the hot-work crew and live plant; dropped objects from the concurrent crane lift | SIMOPS coordination controls — exclusion zone, sequencing, single point of coordination, cross-permit reference (Section 7) | Engineering + Administrative (see 7.3) | Open — Area Authority (role) |
| H-9 | Fall from the pipe rack (if work is at elevation) | Fall arrest or edge protection per the working-at-height gate | Engineering (edge protection preferred over fall arrest) | **[GAP: work elevation not supplied — resolve before issue]** — Permit Holder (role) |
| H-10 | Welder exposure: arc radiation, fumes, electric shock, hot surfaces | Welding screens; fume control appropriate to the work position; welding set inspected and earthed; welder PPE (helmet, gloves, flame-resistant clothing) | Engineering + PPE | Open — Permit Holder (role) |

**HoC discipline note:** no hazard above is treated with PPE alone. PPE appears only at H-10, layered beneath engineered and administrative controls. The dominant residual weakness in this package is the absence of evidenced engineered isolation (H-2/H-3) — that gap blocks issue; it is not compensable by administrative controls or PPE.

---

## 5. Hot-work mandatory control gate

All of the following are **mandatory** for a hot-work permit in this system. The permit must not be issued until each is confirmed:

| Gate item | Requirement | Confirmed (initial/date) |
|---|---|---|
| Fire watch | Trained Fire Watch (role) posted at the work point for the full duration of hot work, and for the site-standard period after last hot work [GAP: duration not supplied]; no concurrent duties | ______ |
| Combustibles | Combustible materials removed from the work area or protected where removal is impracticable; drains/openings covered [GAP: site-standard clearance radius not supplied] | ______ |
| Extinguisher | Appropriate fire extinguisher at the work point, inspected and in date | ______ |
| Gas test | Initial gas test passed and recorded (Section 6) before issue; repeat/continuous monitoring in place | ______ |
| Spark containment | Fire-resistant blankets/screens/habitat in place around and below the work point (H-4) | ______ |

Grounding: hot-work permit and coordination controls per KB-STD-PSM (process safety management standard — hot work element (k); permit & coordination controls).

---

## 6. Gas testing requirements and record

Hot work adjacent to a live process unit: a gas test by the Authorized Gas Tester (role) is **mandatory before issue**, with repeat or continuous monitoring for the life of the permit.

- [GAP] The site's numeric acceptance criteria (flammable-gas limits) were not supplied and are **not invented here**. The Authorized Gas Tester must apply the site gas-testing standard and record the acceptance criteria alongside the results below.
- [GAP] Retest frequency / continuous-monitoring requirement per site standard — not supplied; to be entered at issue.
- Any gas alarm during the work: **stop work immediately, withdraw, and suspend the permit** (Section 15). Re-entry only after re-test and revalidation by the Area Authority (role).

| Test # | Date | Time | Location(s) tested | Instrument ID / calibration due | Result | Acceptance criteria applied (site standard) | Gas Tester (role, initials) |
|---|---|---|---|---|---|---|---|
| Initial | 5 July 2026 | ______ | Work point + surrounding rack bays + below-rack grade | ______ | ______ | ______ | ______ |
| Repeat | ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| Repeat | ______ | ______ | ______ | ______ | ______ | ______ | ______ |

---

## 7. SIMOPS coordination section

SIMOPS was detected in intake: **a crane lift passes over the live unit concurrently with this hot work.** SIMOPS is handled here, inside this permit, as a permit/coordination control — it is never deferred to a separate workflow. **This permit is not valid until every coordination control in 7.3 is confirmed in place and the cross-permit reference in 7.5 is entered.**

### 7.1 Concurrent operations register

| # | Concurrent activity | Location / interaction zone | Owning authority | Permit reference |
|---|---|---|---|---|
| S-1 | Crane lift | Lift path over the live unit, in the same area as the Unit 100 pipe-rack hot work | Lifting Operation Performing Authority (role) | **[GAP: lift permit / lift plan reference not supplied — mandatory before issue]** |

[GAP] The concurrent-permit register for the area was not supplied. The Area Authority (role) must check it before issue and add any further concurrent operations to this register — this table currently reflects only what the job notes disclose.

### 7.2 Conflict analysis

| Conflict | Consequence if uncoordinated |
|---|---|
| Suspended load travels over the live unit while the hot-work crew is on the rack | Dropped object strikes the crew, the live plant, or in-service piping — potential injury and loss of containment with an active ignition source (the welding arc) present |
| Hot work in progress during a lift pass | Crew unable to withdraw promptly; sparks/hot work continue beneath a suspended load; two high-risk activities share one exposure zone with no single controlling mind |

### 7.3 Coordination controls (HoC-ranked)

| Control | Detail | HoC tier |
|---|---|---|
| Sequencing | Hot work and lift passes are **mutually exclusive in time** over the interaction zone: hot work is suspended and the crew withdrawn before any lift pass over the area; lifts do not commence while hot work is live. Sequencing is agreed between both authorities before issue and re-briefed at any change | Administrative — but it removes the simultaneous exposure entirely when enforced, which is why it is paired with the physical controls below rather than relied on alone |
| Exclusion zone | Physical barriers and signage establishing an exclusion zone beneath the lift path; no entry during lift operations [GAP: zone dimensions per the lift plan — not supplied] | Engineering (physical barrier) + Administrative (zone rules) |
| Single point of coordination | One named coordinating mind — the Area Authority (role) — controls the interaction: holds both permit references, authorises each transition between hot work and lifting, and is the sole channel for go/stop decisions | Administrative |
| Cross-permit reference | This hot-work permit and the lift permit each carry the other's reference number, so neither can be issued, suspended, or closed without the interaction being visible to both authorities | Administrative |

**HoC discipline note:** SIMOPS coordination is inherently administrative-heavy. That is acceptable here **only because** (a) the exclusion zone is physically barriered, (b) sequencing removes the temporal overlap rather than merely managing it, and (c) stop-work authority (Section 15) backstops every control. Any weakening of these three — an unbarriered zone, "concurrent but careful" working, or diffuse coordination — invalidates the permit.

### 7.4 Single point of coordination and authorising authority

The **Area Authority (authorizing-authority role)** is the single point of coordination and the authorising authority for the SIMOPS interaction. Specifically, the Area Authority:

1. Holds this permit and the lift permit reference together and verifies neither proceeds without the other's status known.
2. Authorises every transition: hot work start, hot-work suspension for a lift pass, lift commencement, lift completion, and hot-work resumption.
3. Confirms the exclusion zone is established and the rack crew withdrawn before authorising any lift over the interaction zone.
4. Re-briefs both crews on the sequencing rule at shift start and after any suspension.

### 7.5 Cross-permit references

| This permit | References |
|---|---|
| HW-U100-[GAP: serial] (this hot-work permit) | Lift permit: **[GAP: reference not supplied — the Area Authority must enter it before issue; the permit is not valid without it]** |

### 7.6 SIMOPS validity interlock

This permit is **not valid** unless all of the following hold, and it is **automatically suspended** if any ceases to hold:

- The cross-permit reference (7.5) is entered and current.
- The exclusion zone is physically established.
- The sequencing rule is briefed to both crews and in force.
- The Area Authority (role) is present/contactable as the single point of coordination.

---

## 8. Permit conditions

The following conditions must hold for the life of the permit. Breach of any condition = stop work and suspend (Section 15).

1. All Section 5 hot-work gate controls remain in place continuously.
2. Gas-test results remain within the site acceptance criteria; monitoring per Section 6 is maintained.
3. All Section 10 isolations remain applied, locked, and tagged.
4. The SIMOPS validity interlock (7.6) holds continuously.
5. Only the task named in Section 2 is performed — no scope creep to other welds, lines, or rack bays without a new or amended permit.
6. The Permit Holder (role) remains at the worksite while hot work is in progress.
7. Weather or plant-upset conditions that could carry sparks beyond the protected zone, or that trigger unit alarms, suspend the permit. [GAP: site-standard wind/weather limits for elevated hot work not supplied — enter at issue.]

---

## 9. Validity, revalidation, and shift handover

- **Validity:** day shift, 5 July 2026 only — [ASSUMPTION] single-shift validity adopted as the conservative default because the site validity rule was not supplied. The permit expires at end of shift on 5 July 2026.
- **Shift handover:** this permit does **not** carry over a shift change. If work continues beyond the shift, the incoming Area Authority (role) and Permit Holder (role) must revalidate: fresh gas test, physical re-verification of isolations, hot-work gate, and SIMOPS interlock, and re-signature in Section 14.
- **Revalidation after suspension:** any suspension (Section 15) requires the same full revalidation before restart.

---

## 10. Isolation confirmation record

[GAP: no isolation/LOTO register extract or P&ID was supplied with the job notes. The table below must be completed from the site isolation register and the P&ID before issue — **this permit is not valid while this table is empty.** Per the methodology, an isolation that exists only as permit paperwork, without an engineered isolation applied and verified in the field, is flagged and does not count.]

| Isolation point ID (from register/P&ID) | Energy source / line | Isolation method (lock/tag/blind/double-block) | Applied by (role) | Verified by (role) | Date/time |
|---|---|---|---|---|---|
| [GAP] | [GAP] | [GAP] | ______ | ______ | ______ |
| [GAP] | [GAP] | [GAP] | ______ | ______ | ______ |

---

## 11. Action tracker (to closure)

| ID | Action (specific, measurable) | Owner (role) | Due | Status |
|---|---|---|---|---|
| A-01 | Identify the exact work piece (line number / rack bay / elevation) and enter it on the permit face | Permit Holder (role) | 5 July 2026 — pre-issue | Open |
| A-02 | Confirm whether the weld is on in-service piping; if yes, apply the line-break gate (drain/flush/depressurise + double isolation) and record it in Section 10 | Area Authority (role) | 5 July 2026 — pre-issue | Open |
| A-03 | Complete the isolation confirmation record (Section 10) from the isolation register and P&ID; apply and field-verify all LOTO | Area Authority (role) | 5 July 2026 — pre-issue | Open |
| A-04 | Record the elimination/substitution justification for performing hot work over live plant (H-1) | Area Authority (role) | 5 July 2026 — pre-issue | Open |
| A-05 | Assign the Authorized Gas Tester (role); perform and record the initial gas test with the site acceptance criteria (Section 6) | Area Authority (role) | 5 July 2026 — pre-issue | Open |
| A-06 | Remove/protect combustibles, cover drains and openings, and rig spark containment below and around the work point (H-4, H-5) | Permit Holder (role) | 5 July 2026 — pre-issue | Open |
| A-07 | Post the trained Fire Watch (role) with an in-date extinguisher at the work point | Permit Holder (role) | 5 July 2026 — pre-issue | Open |
| A-08 | Enter the lift-permit cross-reference (7.5) and verify the lift plan's exclusion-zone dimensions; establish physical barriers and signage | Area Authority (role) | 5 July 2026 — pre-issue | Open |
| A-09 | Brief both crews (hot work + lifting) on the sequencing rule and the single point of coordination; record attendance by role | Area Authority (role) | 5 July 2026 — pre-issue | Open |
| A-10 | Resolve the work-at-height question (H-9); if elevated, add fall protection controls and any site height permit | Permit Holder (role) | 5 July 2026 — pre-issue | Open |
| A-11 | Confirm the jurisdiction and attach applicable statutory hot-work requirements to this package | HSE Advisor (role) | 5 July 2026 — pre-issue | Open |
| A-12 | Maintain post-work fire watch for the site-standard duration after last hot work; record start/finish times | Fire Watch (role) | 5 July 2026 — at completion | Open |
| A-13 | Close the permit: final area inspection, isolations removed under the Area Authority's control, cross-permit closure noted on the lift permit, permit returned to the register | Area Authority (role) | 5 July 2026 — end of shift | Open |

---

## 12. Assumptions and gaps register

**Assumptions (conservative, flagged inline where applied):**

| # | Assumption | Basis |
|---|---|---|
| AS-1 | Single-shift validity (day shift, 5 July 2026) | Site validity rule not supplied; single shift is the most conservative of the standard options |
| AS-2 | Process-plant setting, management audience | Derived from "Unit 100", "live unit", and pipe-rack context in the job notes |

**Gaps (unsupplied values recorded as [GAP] — none fabricated):**

| # | Gap | Where it appears | Blocks issue? |
|---|---|---|---|
| G-1 | Exact work piece (line/joint/bay/elevation) and welding process | Sections 2, 11 (A-01) | **Yes** |
| G-2 | In-service status of the weld line; isolation points; LOTO register extract | Sections 2, 4, 10 (A-02, A-03) | **Yes** |
| G-3 | Authorized Gas Tester assignment; site gas-test acceptance criteria and retest frequency | Sections 3, 6 (A-05) | **Yes** |
| G-4 | Lift-permit cross-reference and exclusion-zone dimensions | Section 7.5 (A-08) | **Yes** |
| G-5 | Jurisdiction | Document control, Section 11 (A-11) | Statutory annex blocked; competent person to resolve |
| G-6 | Site-standard combustibles clearance radius; post-work fire-watch duration; weather limits | Sections 5, 7, 8 | To be entered at issue from site standards |
| G-7 | Work-at-height status of the welding position | Section 2, H-9 (A-10) | **Yes** — until resolved |
| G-8 | Concurrent-permit register check for further SIMOPS beyond the disclosed crane lift | Section 7.1 | **Yes** |
| G-9 | Permit serial number | Document control | Assigned at issue |
| G-10 | Elimination/substitution justification for hot work over live plant | H-1 (A-04) | **Yes** |

---

## 13. Pre-issue validity checklist

The Area Authority (role) must confirm **every** line before this permit becomes valid:

- [ ] Exact work piece named on the permit face (G-1 closed)
- [ ] In-service status resolved; line-break gate applied if required (G-2)
- [ ] Section 10 isolation record complete; all LOTO applied and field-verified (G-2)
- [ ] Elimination/substitution justification recorded (G-10)
- [ ] Initial gas test passed and recorded against site acceptance criteria (G-3)
- [ ] Hot-work gate: fire watch posted, combustibles cleared/protected, extinguisher in place, spark containment rigged (Section 5)
- [ ] Work-at-height question resolved; controls added if elevated (G-7)
- [ ] SIMOPS: cross-permit reference entered; exclusion zone physically established; sequencing briefed to both crews; single point of coordination confirmed (Section 7)
- [ ] Concurrent-permit register checked for further simultaneous operations (G-8)
- [ ] Jurisdictional statutory requirements attached (G-5)
- [ ] Validity window and handover rule entered (Section 9)

---

## 14. Sign-off

| Sign-off | Role | Signature | Date | Time |
|---|---|---|---|---|
| Permit issue — all Section 13 items confirmed | Area Authority (authorizing-authority role) | ______ | 5 July 2026 | ______ |
| Permit acceptance — conditions understood and will be enforced at the worksite | Permit Holder (task-supervisor role) | ______ | 5 July 2026 | ______ |
| Gas test — Section 6 initial test recorded | Authorized Gas Tester (role) | ______ | 5 July 2026 | ______ |
| SIMOPS coordination — Section 7 interlock confirmed in place | Area Authority (authorizing-authority role) | ______ | 5 July 2026 | ______ |
| Revalidation (if any) — Section 9 | Area Authority (role) / Permit Holder (role) | ______ | ______ | ______ |
| Closure and handback — Section 15 | Area Authority (authorizing-authority role) | ______ | 5 July 2026 | ______ |

---

## 15. Suspension, stop-work, and closure

**Stop-work authority:** any person on either crew may stop the work without sanction. Work stops immediately on: any gas alarm; any breach of the exclusion zone; any unplanned lift deviation; any plant alarm or upset in Unit 100; loss of the Fire Watch or the single point of coordination; any permit condition ceasing to hold.

**Suspension:** on any stop, the Area Authority (role) suspends this permit and notifies the Lifting Operation Performing Authority (role) via the cross-permit reference. Restart requires full revalidation (Section 9).

**Closure/handback:** at completion — last hot work logged; post-work fire watch completed for the site-standard duration and recorded (A-12); final area inspection by the Permit Holder (role) and Area Authority (role); isolations removed under the Area Authority's control; the lift permit annotated that the SIMOPS interaction is closed; permit signed off (Section 14) and returned to the site permit register. Open actions in Section 11 that survive closure transfer to the site action-tracking system with their owners and dates intact.

---

## 16. References

- KB-STD-PSM — process safety management standard: hot work element (k); permit & coordination controls (grounding for the hot-work gate and the SIMOPS coordination pattern in this permit).
- KB-SNIP-HOC — hierarchy of controls, applied to every isolation and safeguard in Sections 4, 5, and 7.
- Jurisdiction-specific statutory references: **none cited** — jurisdiction not supplied (G-5). To be attached by the competent person before issue.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*

---

**Limitations.** This permit-to-work package is decision-support only. It is not a valid permit until every pre-issue condition is physically confirmed, and it is not legal advice. A competent person — the site's authorised permit issuer and, where required, the responsible engineer — must review, complete the flagged [GAP] items, and sign off this output before it is used to authorise any work.
