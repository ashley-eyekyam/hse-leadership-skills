---
sme-review:
  personas:
    - role: "OSHA-PSM / Seveso process-safety program manager (29 CFR 1910.119, the 14 elements)"
      expertise: "Per-element status assessment (compliant / gap / overdue) with evidence; cycle-date-driven overdue status (triennial audit, 5-yr PHA revalidation); gap-risk banding; element-linked remediation tracking; PSM↔OSHA statute alignment."
      lens: "Is every element's status evidence-based rather than asserted, and does each gap carry a risk-banded, owned, higher-order remediation action?"
---

# SME Review & Sign-off — psm-program-manager

This skill carries **one** specialized SME lens: an OSHA-PSM / Seveso program manager. It
narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`),
carrying the slot's "PSM element artifacts complete and owner-assigned" check, to the
14-element program backbone; the generic **HSE-SME-Reviewer** hook is the inherited
fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**Status must be evidence-based, not asserted.** The failure modes this lens guards are an
element marked "compliant" with no evidence (recorded instead as `[GAP]`), an element
silently omitted from the matrix, an "overdue" status with no cycle-date basis, and a gap
with no risk band, no higher-order remediation, or no named owner. A US covered process
cites both the PSM framework and the OSHA statute, kept consistent.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each element's compliant/gap/overdue status cites evidence; a status with no evidence reads `[GAP]`, never an asserted "compliant".
- [ ] Every PSM element appears, or the in-scope subset is explicitly bounded — no element silently omitted.
- [ ] An "overdue" status has a cycle-date basis (last compliance audit, last PHA/revalidation) — not asserted without a date.
- [ ] Each gap carries a gap-risk band from `risk_matrix`, so remediation can be prioritised.
- [ ] Each gap's remediation is HoC-ranked with a higher-order control and a named owner; a gap "controlled" by an administrative measure alone is flagged.
- [ ] A US facility cites both KB-STD-PSM (framework) and KB-REG-US-OSHA (statute), kept consistent; one row per element (element · status · evidence · gap-risk band · owner) with no orphan rows (FLAG).

## Sign-off note
SME review: ran (persona: OSHA-PSM / Seveso process-safety program manager); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
