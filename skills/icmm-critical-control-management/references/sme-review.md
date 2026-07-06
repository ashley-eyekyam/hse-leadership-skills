---
sme-review:
  personas:
    - role: "ICMM Critical-Control-Management practitioner (CCM workshop facilitator / principal-hazard-management specialist)"
      expertise: "ICMM CCM Good-Practice Guide, bowtie/barrier thinking, material-unwanted-event definition, critical-control identification + performance requirements + verification regimes"
      lens: "Are these GENUINELY critical controls (their absence/failure ALLOWS the MUE), each with a stated performance requirement, a real verification activity at a real frequency, and a named accountable role — or a relabelled generic control list?"
modes:
  ccm:
    detected_by: "Q1 — Set up CCM for one event or structure a full CCM workshop; Q3 selects the material unwanted event. The floor applies to every CCM output."
    floor:
      - id: criticality-gates-mue
        description: "Each critical control genuinely gates the MUE — it passes 'if absent or failed, does the material unwanted event become possible?'; a critical-labelled control that does not gate the MUE, or a genuine gating control omitted, is a miss (intake Q3/Q5)"
        anchors: ['critical control', 'mue|material unwanted event']
        min_matches: 2
      - id: four-ccm-attributes
        description: "Every critical control carries all four CCM attributes — performance requirement + verification activity + verification frequency + accountability (role); a control with no frequency is not under management (intake Q6/Q7)"
        anchors: ['performance', 'verification', 'frequency', 'accountab']
        min_matches: 3
      - id: bowtie-referenced
        description: "The bowtie is referenced (threat side -> top event -> consequence side) to bowtie-builder, not re-authored — no self-authored bowtie engine or invented barrier-performance standard"
        anchors: ['bowtie', 'threat', 'consequence']
        min_matches: 2
      - id: hoc-critical-not-ppe-only
        description: "A PPE/admin-only item is not dressed up as a CRITICAL control for a principal hazard — a higher-order critical control exists, or the reliance is explicitly justified/escalated"
        anchors: ['administrative|higher.order|hierarchy', 'ppe']
        min_matches: 1
      - id: gap-performance-not-fabricated
        description: "Un-supplied engineering/performance evidence (PFD, barrier-performance figure) is a literal [GAP], never fabricated (intake Q6)"
        anchors: ['\[GAP\]']
        min_matches: 1
      - id: escalation-tarp
        description: "A reporting/assurance/escalation cadence and a Trigger Action Response Plan (TARP) close the management loop"
        anchors: ['escalation|assurance', 'tarp']
        min_matches: 2
      - id: self-escape-emergency-response
        description: "Where the MUE demands it, self-escape (SCSR / escapeway / refuge) and emergency-response / mine-rescue capability appear as mitigative critical controls (the emergency leg)"
        anchors: ['self.escape|escapeway|refuge', 'emergency response|mine.rescue']
        min_matches: 1
---

# SME Review & Sign-off — icmm-critical-control-management

Single specialized persona, narrowing the **Mine Manager** archetype slot
(`KB-SNIP-ARCHETYPES`, archetypes:291-326 — its "critical controls real, not
generic … real verification activities + frequencies + accountabilities" bullet,
archetypes:307-309) to an ICMM CCM practitioner. This is an **assistive** (Tier-4,
`status: assistive`) skill, so the persona additionally holds the autonomy boundary
test.

> **Overlap note (D-04):** this skill shares ~80% of its surface with
> `principal-hazard-management-plan`, and is the ICMM-CCM linkage target a PHMP carries
> its critical controls into (`KB-STD-ICMM-CCM`). Each skill ships its **own
> self-contained** `references/sme-review.md` (no shared fragment); when reviewing a
> PHMP that links here, confirm the performance + verification regime is the same one
> this skill's critical-control checklist demands.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Criticality justified against the MUE — each control passes *"if absent or failed, does the MUE become possible?"*; FLAG a critical-labelled control that does not gate the MUE, and any genuine MUE-gating control omitted.
- [ ] Every critical control carries all four CCM attributes — performance requirement + verification activity + verification **frequency** + **accountability (role)**; FLAG any missing one (a control with no frequency is not under management).
- [ ] Verification activity is a real check, not a restatement of the control (e.g. "monthly pull-test of the anchor" not "anchor is maintained"); FLAG tautological verification.
- [ ] A PPE/admin-only item is not dressed up as a *critical* control for a principal hazard — confirm a higher-order critical control exists, or the reliance is explicitly justified-or-escalated.
- [ ] The bowtie is *referenced* to `bowtie-builder`, not re-authored; FLAG any self-authored bowtie engine or invented barrier-performance standard.
- [ ] Un-supplied engineering/performance evidence is `[GAP]`, never fabricated; a fabricated PFD/performance figure is a FLAG.
- [ ] **Assistive autonomy test:** output reads as structured, team-recorded CCM workshop output, not autonomous AI engineering of critical controls (archetypes:316-326); an output that *autonomously decided* the critical controls is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The relabelled generic control** — an ordinary control list dressed up as "critical
  controls" where the criticality test (does its failure ALLOW the MUE?) was never applied,
  so a genuinely MUE-gating control is missing and a non-gating one is over-weighted.
- **The control with no frequency** — a critical control with a performance requirement and
  an owner but no verification frequency; it is named, not managed, and drifts unverified.
- **Tautological verification** — "the anchor is maintained" recorded as the verification of
  "the anchor is maintained"; a real check (a dated pull-test, a monitored reading) is absent.
- **The missing emergency leg** (canary S1) — a fire/inrush/strata MUE whose mitigative side
  omits self-escape (SCSR/escapeway/refuge) and mine-rescue capability; prevention listed,
  survival not.
- **Autonomous engineering** — the output autonomously decided the critical controls or
  invented a barrier-performance/PFD figure, instead of structuring the team's workshop record
  and marking un-supplied values `[GAP]`.

## Sign-off note
Reviewed-as: ICMM critical-control-management practitioner — model QA
(decision-support); workshop-structuring only, FLAGs non-blocking. This review
precedes — and never replaces, never emits — the mine team's engineering judgement
nor the competent-person sign-off; it never outputs "approved by a competent person".
