# Incident Investigation — Fall from Height, Mezzanine Bay, UK Distribution Centre

**Classification:** Injury · lost-time / specified injury (one person) · UK jurisdiction
**Method:** SCAT (Systematic Cause Analysis Technique) — selected to link to the management-system control failure
**Status:** De-identification pass completed FIRST; role labels only throughout.

> De-identification: identifiers detected and pseudonymised before any drafting. The injured
> party is referred to as Worker C (stock handler); the shift lead as Witness W-3. No names,
> contact details, IDs, addresses, or small injury cells appear below. Any re-identification
> key is held in a separate controlled artifact, not in this report.

---

## 1. What happened

Worker C fell approximately 3 m from an unguarded mezzanine edge at a stock-transfer point
in a UK distribution centre while moving stock, sustaining a fractured wrist that required
hospital treatment. The edge protection had been removed for a delivery and was not
reinstated before stock movement resumed at the open edge.

## 2. Evidence log

- **E-1** — Statement: edge protection had been removed for a delivery and not reinstated.
- **E-2** — Photograph: open mezzanine edge at the stock-transfer point, no guardrail.
- **E-3** — Document: the permit authorising removal of edge protection has NO reinstatement
  check-back step before work resumes.

## 3. SCAT analysis (Loss → Contact → Immediate → Basic → Lack of Control)

- **Loss:** specified injury (fractured wrist, hospital treatment) to Worker C; lost time.
- **Contact (energy/condition):** fall from height — gravity, ~3 m, onto a lower level.
- **Immediate causes:**
  - IC-1 — Unguarded mezzanine edge at the active transfer point *(E-2)*.
  - IC-2 — Stock moved at an open edge with no edge protection in place *(E-1)*.
- **Basic / underlying causes:**
  - BC-1 — Edge protection removed for a delivery and not reinstated; no trigger forced
    its return before work resumed *(E-1)*.
- **Lack of control (management-system failure — the SCAT systemic reach):**
  - LOC-1 — The permit-to-remove-edge-protection has no mandatory reinstatement
    check-back / sign-off step, so a removed barrier could stay removed undetected *(E-3)*.

SCAT reaches the management system: `rca.validate(method="scat", …)` returns
`reaches_systemic = True` and `valid = True` because both `basic_causes` (BC-1) and
`lack_of_control` (LOC-1) are populated alongside the immediate causes.

## 4. Root / contributing causes (the CAPA anchors)

- **RC-1** — *Lack of control:* permit lacks a reinstatement check-back step (LOC-1, E-3) —
  the systemic root.
- **RC-2** — *Basic cause:* no engineered/standing edge protection independent of the
  removable barrier; the mezzanine edge relies on a barrier that can be taken away (BC-1, E-1).
- **RC-3** — *Contributing:* no real-time detection that an open edge existed at an active
  transfer point (IC-1/IC-2, E-2).

## 5. Hierarchy-of-controls CAPA register (ranked Elimination → … → PPE)

Controls were ranked with the `controls.rank_controls` hierarchy and validated with
`smart_actions.validate_register`. Every action carries a role-label owner, an ISO due date,
a measure, and a `links_to_cause` (RC-n) — so `all_traced_to_cause = True`. The register is
**not** PPE/admin-only: it contains an Engineering control and an Elimination option above
the admin layer, so `controls.rank_controls` does NOT raise the PPE/admin-only flag.

| ID | Action | hoc_tier | links_to_cause | Owner (role) | Due (ISO) | Measure |
|----|--------|----------|----------------|--------------|-----------|---------|
| A1 | Eliminate the at-height manual transfer at this bay — re-route stock so the open mezzanine edge is no longer a working transfer point | **Elimination** | RC-2 | Operations Manager | 2026‑08‑30 | No stock-transfer task scheduled at the mezzanine edge; flow re-routed and verified on the layout |
| A2 | Install a FIXED guardrail with a self-closing safety gate at the transfer point (standing protection independent of any removable barrier) | **Engineering** | RC-2 | Facilities Lead | 2026‑07‑31 | Fixed guardrail + self-closing gate installed and load-checked to the edge-protection standard |
| A3 | Add a mandatory reinstatement check-back + sign-off step to the edge-protection-removal permit; work may not resume until edge protection is signed back in | **Administrative** | RC-1 | HSE Manager | 2026‑07‑15 | Revised permit in use; 100% of audited permits show a completed reinstatement sign-off |
| A4 | Stand up a shift-start open-edge visual check at all mezzanine transfer points and log it | **Administrative** | RC-3 | Shift Lead (role) | 2026‑07‑10 | Open-edge check logged every shift; zero unguarded-edge findings left open >24 h |
| A5 | Issue and require fall-arrest harness + anchor for any residual unavoidable work near an open edge during the guardrail install window | **PPE** | RC-2 | HSE Manager | 2026‑07‑12 | Harness/anchor issued and recorded; interim-only, retired once A2 guardrail is live |

**Higher-order coverage (hierarchy_of_controls):** the register leads with an **Elimination**
option (A1) and a permanent **Engineering** control (A2, a fixed guardrail / self-closing
gate). PPE (A5) appears ONLY as a time-boxed interim measure during the install window, not
as the primary treatment — there is no PPE/admin-only treatment of any root cause, so no
`ppe_admin_only` justification is required.

## 6. Residual risk re-scoring (initial → residual after CAPA)

Scored on the org 5×5 matrix (`risk_matrix` engine; bands Low 1–4, Medium 5–9, High 10–15,
Critical 16–25).

| Hazard | Initial (L×S) | Initial band | After CAPA | Residual band | Movement |
|--------|---------------|--------------|------------|---------------|----------|
| Fall from unguarded mezzanine edge | 4 × 4 = 16 | **Critical** | 1 × 4 = 4 | **Low** | 16 → 4 |
| Open edge undetected after barrier removal | 4 × 4 = 16 | **Critical** | 2 × 3 = 6 | **Medium** | 16 → 6 |

Severity stays high (a fall from ~3 m can still be serious), but the FIXED guardrail (A2,
Engineering) plus the permit reinstatement gate (A3) and elimination of the transfer (A1)
collapse the likelihood — moving the fall hazard from **Critical (16) → Low (4)** and the
detection gap from **Critical (16) → Medium (6)**. Residual risk is As Low As Reasonably
Practicable once A1–A3 are complete; A4/A5 cover the interim and the detection layer.

## 7. Reportability verdict (UK)

**Verdict: REPORTABLE.** Under the UK RIDDOR 2013 regulations (Reporting of Injuries,
Diseases and Dangerous Occurrences Regulations), a fracture other than to fingers, thumbs or
toes is a **specified injury**. Worker C's fractured wrist is therefore a specified injury and
is reportable to the enforcing authority (HSE). Specified injuries must be reported without
delay (by the quickest practicable means, and a report submitted within the RIDDOR
timeline), and a record of the injury retained.

Regulatory basis resolved against the knowledge base: **KB-REG-UK-HSWA** (UK HSWA / RIDDOR
reporting row). No national form number is invented; the verdict cites the resolvable KB row,
not a fabricated citation.

## 8. Assumptions / gaps

- **[GAP]** Exact incident date withheld in intake (Q2) — the RIDDOR reporting clock runs
  from the actual incident date on file; set the report timeline against that date.
- **[ASSUMPTION]** Residual likelihood scores assume A1–A3 are completed and verified; until
  then the interim residual remains elevated and A5 PPE applies.

## 9. Report output

A branded `report.json` is emitted to the report engine and rendered to DOCX and PDF
(Eyekyam default brand unless a user `brand.yaml` overrides), carrying §1 narrative, the §3
SCAT analysis, the §5 ranked CAPA register, the §6 residual re-scoring, and the §7
reportability verdict. De-identification holds end-to-end: role labels only.

---
*Decision-support output. Must be reviewed by a competent person before use. Not legal advice.*
