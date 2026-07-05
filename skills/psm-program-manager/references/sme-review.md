---
sme-review:
  personas:
    - role: "OSHA-PSM / Seveso process-safety program manager (29 CFR 1910.119, the 14 elements)"
      expertise: "Per-element status assessment (compliant / gap / overdue) with evidence; cycle-date-driven overdue status (triennial audit, 5-yr PHA revalidation); gap-risk banding; element-linked remediation tracking; PSM↔OSHA statute alignment."
      lens: "Is every element's status evidence-based rather than asserted, and does each gap carry a risk-banded, owned, higher-order remediation action?"
modes:
  status-matrix:
    detected_by: "Q10 — What output, for whom? (Status matrix / Gap report / Audit-prep pack — all built on the one 14-element status matrix, the skill's single artifact class)"
    floor:
      - id: covered-process-determination
        description: "The facility + covered process is named with the PSM-covered determination (threshold quantity of a highly hazardous chemical) stated — or the framework-not-statutory note where not covered (intake Q2)"
        anchors: ['covered process', 'threshold quantity|highly hazardous']
        min_matches: 1
      - id: all-elements-or-bounded
        description: "One row per PSM element — all 14, or the in-scope subset explicitly bounded; no element silently omitted (intake Q3; KB-STD-PSM element map)"
        anchors: ['14', 'employee participation|trade secrets']
        min_matches: 2
      - id: status-cites-evidence
        description: "Each element's compliant/gap/overdue status cites its evidence (documents, audit findings, dates); a status with no evidence reads a literal [GAP], never an asserted 'compliant' (intake Q4)"
        anchors: ['evidence', 'compliant']
        min_matches: 2
      - id: overdue-has-cycle-date
        description: "Every 'overdue' status traces to a cycle-date basis — the triennial compliance audit or the 5-yearly PHA revalidation (intake Q5)"
        anchors: ['triennial', '(five|5).?(year|yr)|revalidat']
        min_matches: 1
      - id: gap-risk-banded
        description: "Each gap carries a gap-risk band from the named matrix so remediation is prioritised (intake Q9, risk_matrix output)"
        anchors: ['gap.?risk|risk band', 'prioriti']
        min_matches: 1
      - id: remediation-hoc-smart
        description: "Each gap's remediation is HoC-ranked (a higher-order control, not an administrative reminder) and is a SMART action — named role owner + due date + measure (smart_actions discipline)"
        anchors: ['remediation', 'named owner|action owner', 'due date']
        min_matches: 2
      - id: framework-statute-consistent
        description: "A US covered process cites both KB-STD-PSM (the framework map) and the OSHA statute 29 CFR 1910.119, kept consistent (intake Q8)"
        anchors: ['1910\.119', 'KB-STD-PSM']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A matrix of asserted greens** — every element marked compliant with no evidence
  column, no document names, no dates; the matrix is a mood, not an assessment.
- **The eleven-element '14-element' matrix** — employee participation, trade secrets and
  contractors quietly missing; the omission is invisible unless the reader counts rows.
- **Overdue that never fires** — no audit/PHA cycle dates captured anywhere, so nothing
  can ever show overdue; the program's clock is disconnected.
- **Gaps with remediation theatre** — every gap 'addressed' by a reminder, a toolbox talk
  or 'reinforce awareness'; no higher-order fix, no owner, no date — the backbone
  artifact records intention, not management.

## Sign-off note
SME review: ran (persona: OSHA-PSM / Seveso process-safety program manager); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
