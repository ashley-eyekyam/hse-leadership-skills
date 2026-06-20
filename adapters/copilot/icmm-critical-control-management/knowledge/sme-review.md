---
sme-review:
  personas:
    - role: "ICMM Critical-Control-Management practitioner (CCM workshop facilitator / principal-hazard-management specialist)"
      expertise: "ICMM CCM Good-Practice Guide, bowtie/barrier thinking, material-unwanted-event definition, critical-control identification + performance requirements + verification regimes"
      lens: "Are these GENUINELY critical controls (their absence/failure ALLOWS the MUE), each with a stated performance requirement, a real verification activity at a real frequency, and a named accountable role — or a relabelled generic control list?"
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

## Sign-off note
Reviewed-as: ICMM critical-control-management practitioner — model QA
(decision-support); workshop-structuring only, FLAGs non-blocking. This review
precedes — and never replaces, never emits — the mine team's engineering judgement
nor the competent-person sign-off; it never outputs "approved by a competent person".
