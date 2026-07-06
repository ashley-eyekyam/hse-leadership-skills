---
sme-review:
  personas:
    - role: "Quality / CAPA systems lead (ISO 45001 10.2 nonconformity & corrective action)"
      expertise: "CAPA-system management, corrective-vs-preventive discipline, effectiveness-verification design, audit-finding closure, and recognising a 'closed-on-paper, recurs-in-practice' CAPA."
      lens: "Will this CAPA actually STOP RECURRENCE — every action traces to a real cause, preventive ≠ corrective, and each has a scheduled effectiveness check before it can be called 'verified-effective'?"
modes:
  capa-lifecycle:
    detected_by: "Q8 — CAPA scope (Single action close-out / Multi-action register); the single-thread and register fan-out share one lifecycle floor. Q0 sets the source (Audit / Incident / Inspection / Near-miss)."
    floor:
      - id: finding-specific-anchor
        description: "The finding/nonconformity the CAPA addresses is specific and cited to a requirement/clause — never 'general non-compliance' (intake Q2 specificity anchor; ISO 45001 cl. 10.2)"
        anchors: ['finding', 'ISO 45001 cl', 'nonconformity']
        min_matches: 2
      - id: root-cause-linked
        description: "Every action traces to an established root cause; an ingested cause id is reused, never re-keyed to a weaker statement (intake Q3; ISO 45001 cl. 10.2 corrective action)"
        anchors: ['root cause', 'reused']
        min_matches: 1
      - id: corrective-preventive-distinct
        description: "Corrective and preventive actions genuinely differ — at least one preventive per cause, distinct from the corrective (a 'preventive' that restates the corrective is a miss)"
        anchors: ['corrective action', 'preventive action']
        min_matches: 2
      - id: hoc-tiered-actions
        description: "Each action is hierarchy-of-controls-tiered; a physical hazard closed on PPE/admin alone is escalated to a higher-order control (intake Q4)"
        anchors: ['hoc.tier', 'hierarchy of controls']
        min_matches: 1
      - id: effectiveness-check-gated
        description: "A scheduled effectiveness check with a method that tests whether the action WORKED (not just that it was done) gates closure — nothing reaches 'verified-effective' without a recorded check (intake Q7)"
        anchors: ['effectiveness (verification|check)', 'verified.effective']
        min_matches: 2
      - id: smart-owned-dated
        description: "Every action is SMART with a named role owner and a due date — anonymous owners and 'ASAP' dates are refused (intake Q5/Q6; smart_actions)"
        anchors: ['owner', 'due']
        min_matches: 2
      - id: lifecycle-status-board
        description: "A lifecycle status board tracks each action (open / in-progress / pending-verification / verified-effective) so nothing is silently closed"
        anchors: ['lifecycle status', 'pending.verification', 'in.progress']
        min_matches: 2
---

# SME Review & Sign-off — capa-manager

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a CAPA-lifecycle manager that shares one schema/engine with
its sibling producers (the B6→B7 seam: safety-audit emits, capa-manager ingests the verbatim
B5 register schema). The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only,
owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Root-cause → action linkage is genuine, not cosmetic — a corrective action bolted to a vague/symptom-level cause is a FLAG; an ingested cause id is reused, never re-keyed to a weaker statement.
- [ ] Corrective vs preventive genuinely differ — ≥1 preventive per cause, distinct from the corrective; a "preventive" that just restates the corrective is a FLAG.
- [ ] Effectiveness verification is real, scheduled, and gated — a CAPA cannot reach `verified-effective` without a recorded check.
- [ ] The verification method actually tests effectiveness — "re-train and remind" is an action, not a verification; a method that only confirms the action was *done* (not that it *worked*) is a FLAG.
- [ ] An ingested register is re-checked, not assumed clean — silent trust of an upstream audit/incident artifact is a FLAG; the De-identifier re-checks ingested facts.
- [ ] No "general non-compliance" anchor — the finding the CAPA addresses must be specific.
- [ ] Due dates are risk-proportionate — a high-severity NC with a distant due date, or one boilerplate date everywhere, is a FLAG; anonymous owners and "ASAP" dates are refused.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The paper-closed CAPA** — actions marked complete/closed without an effectiveness check
  that tests the CAUSE is still controlled; "re-trained and reminded" recorded as
  verification. Closed-on-paper, recurs-in-practice.
- **Preventive collapse** — the register carries only corrective (fix-this-instance)
  actions; the systemic preventive action that stops the cause recurring elsewhere is
  silently absent.
- **The high-severity action with no bridge** (canary S2) — a serious NC with a distant due
  date and no interim/containment control for the exposure in the meantime, and no ALARP
  statement for the gap period.
- **Ingested-register trust** — an upstream audit/incident register ingested and its
  actions, owners, and de-id accepted without re-check; a stale owner or an un-scrubbed
  identifier rides straight through.
- **Due-date realism** — one boilerplate due date across every action regardless of
  severity, or a due date that is not risk-proportionate to the nonconformity.

## Sign-off note
SME review: ran (persona: Quality / CAPA systems lead); this is **decision-support only**.
It **precedes — and never replaces, never emits — the human competent-person sign-off**, and
it never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
