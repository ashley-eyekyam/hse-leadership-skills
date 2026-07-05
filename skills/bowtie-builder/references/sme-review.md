---
sme-review:
  personas:
    - role: "Barrier / bowtie-method specialist & critical-control-management (ICMM CCM) practitioner"
      expertise: "Top-event framing; threat & consequence lines; preventive vs mitigative barrier placement; barrier effectiveness / independence / auditability with performance standards; critical-control verification."
      lens: "Is every barrier genuinely effective, independent and auditable with a stated performance standard — or is it an aspirational box on the diagram with no evidence behind it?"
modes:
  bowtie-diagram:
    detected_by: "Q1 — Build a plain bowtie, or a CCM plan? (Bowtie diagram → the threat/barrier/consequence diagram leg; Q12 confirms diagram vs full report)"
    floor:
      - id: single-top-event
        description: "Exactly one named loss-of-control / release top event at the centre, for one named hazard (intake Q3/Q4 specificity anchor — never 'operations')"
        anchors: ['top event', 'loss of (control|containment)']
        min_matches: 1
      - id: threats-preventive-side
        description: "Threats (causes) listed one-per-line on the left with their preventive barriers threat-side (KB-STD-CCPS-BOWTIE method map)"
        anchors: ['threat', 'preventive barrier']
        min_matches: 2
      - id: consequences-damage-due-to-event
        description: "Consequences phrased \"[Damage] due to [Event]\" on the right with their mitigative barriers (KB-STD-CCPS-BOWTIE phrasing rule)"
        anchors: ['due to', 'mitigative barrier']
        min_matches: 2
      - id: barrier-eia-performance-standard
        description: "Every barrier judged effective · independent · auditable with a stated performance standard — a barrier with no performance-standard evidence reads [GAP], never 'effective' (intake Q7, the assistive core)"
        anchors: ['performance standard', 'effective.{0,40}independent.{0,40}auditable']
        min_matches: 1
      - id: barrier-hoc-rank
        description: "Barriers ranked by the hierarchy of controls; an administrative/PPE-only barrier set carries a justification or an escalating recommendation, never passes silently (KB-SNIP-HOC)"
        anchors: ['hierarchy of controls', 'higher.order (control|barrier)']
        min_matches: 1
      - id: barrier-judgement-ownership
        description: "The barrier judgements are owned by a named team/role with a last-reviewed date and the next review due (intake Q9/Q13 — the assistive evidence)"
        anchors: ['barrier judgement', 'last review', 'next review']
        min_matches: 1
      - id: residual-risk-band
        description: "Residual risk banded on the named matrix after the barrier set (intake Q10, risk_matrix engine output)"
        anchors: ['residual risk', 'risk band']
        min_matches: 1
  ccm-plan:
    detected_by: "Q1 — CCM critical-control plan / Both (activates Q8: per-control verification activity, owner and frequency → the critical-control verification table)"
    floor:
      - id: critical-control-selection
        description: "Critical controls selected from the bowtie barriers with the selection rationale stated (ICMM CCM — not every barrier is critical)"
        anchors: ['critical control', 'selection rationale|selected because|criticality']
        min_matches: 1
      - id: ccm-performance-standard
        description: "Each critical control carries a stated, measurable performance standard — mandatory for a critical control (KB-STD-CCPS-BOWTIE / ICMM CCM)"
        anchors: ['performance standard']
        min_matches: 1
      - id: verification-activity-owner-frequency
        description: "A critical-control verification table: per control the verification activity, a named role owner, and the frequency (intake Q8)"
        anchors: ['verification activity', 'frequency', 'verified by']
        min_matches: 2
      - id: failed-verification-response
        description: "The response to a failed verification / degraded critical control is stated (escalation path or interim risk decision), never left implicit"
        anchors: ['failed verification', 'degraded', 'escalat']
        min_matches: 1
      - id: ccm-accountable-owner
        description: "Each critical control carries a named accountable role owner distinct from the verifier where practicable (ICMM CCM accountability)"
        anchors: ['control owner', 'accountab']
        min_matches: 1
---

# SME Review & Sign-off — bowtie-builder

This skill carries **one** specialized SME lens: a barrier / bowtie & ICMM-CCM specialist.
It narrows the family's single **Process-Safety Engineer** archetype
(`KB-SNIP-ARCHETYPES`), directly carrying the slot's barrier/IPL
effective·independent·auditable criteria; the generic **HSE-SME-Reviewer** hook is the
inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**A barrier is not effective until it has a performance standard.** The failure mode this
lens guards is an aspirational barrier — a box on the diagram declared effective with no
evidence. A barrier with no stated performance standard is recorded `[GAP]`, never declared
effective; for a critical control (the CCM path, shared with chemicals and mining) a
performance standard + verification activity + named owner is mandatory. The barrier
judgements are team/owner-supplied (the assistive evidence).

## Domain checklist (the nuanced things only this expert catches)
- [ ] Exactly one loss-of-control / release point as the top event — not a threat or a consequence mislabelled as the centre.
- [ ] Preventive barriers sit threat-side (left) and mitigative barriers consequence-side (right) — no barrier on the wrong side.
- [ ] Each barrier states a performance standard and is judged effective·independent·auditable; a barrier with no evidence reads `[GAP]`, never "effective".
- [ ] Threats are one-per-line; consequences are phrased "[Damage] due to [Event]".
- [ ] For any major-accident barrier, a CCM critical control carries a performance standard + verification activity + named owner — not just a name.
- [ ] Barriers credited on both sides are checked for a shared support system / common-mode failure that would defeat "independent"; the barrier judgements are owned by a named team (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A beautiful diagram with aspirational barriers** — threats, consequences and barrier
  boxes all drawn, but no barrier carries a performance standard or an
  effective·independent·auditable judgement. The diagram reads finished while the barrier
  layer is evidence-free. Check the barrier evidence before admiring the topology.
- **Degradation factors and escalation left off the frame** — the classic bowtie omission:
  the barrier-decay side (what defeats each barrier — the degradation factor and its
  degradation controls) is silently absent, so every barrier is implicitly permanent.
- **Common-mode dependence between credited barriers** — two barriers sharing a support
  system (same power supply, same operator, same logic solver) credited as independent;
  the independence claim is never tested anywhere in the artifact.
- **A CCM plan with no verification loop** — critical controls named but no verification
  activity/owner/frequency table and no stated response to a failed verification; the
  plan manages nothing.

## Sign-off note
SME review: ran (persona: Barrier / bowtie-method & ICMM-CCM specialist); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
