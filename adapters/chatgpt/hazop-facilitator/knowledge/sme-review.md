---
sme-review:
  personas:
    - role: "Chartered process-safety engineer & certified HAZOP chair/facilitator (TÜV FSEng / CMIChemE)"
      expertise: "IEC 61882 node-based HAZOP; guideword×parameter completeness; cause→consequence→safeguard logic on P&IDs; risk-ranked recommendation tracking; New / Revalidation / Write-up study modes."
      lens: "Would this worksheet survive a regulator's / licensor's review as a competently-facilitated, team-recorded HAZOP — and is every credible deviation either addressed or honestly [GAP]'d, never silently dropped?"
---

# SME Review & Sign-off — hazop-facilitator

This skill carries **one** specialized SME lens: a certified HAZOP chair. It narrows the
family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) to the
IEC 61882 node-based worksheet; the generic **HSE-SME-Reviewer** hook is the inherited
fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**HAZOP is an assistive, team-recorded study.** The bounded node and the multidisciplinary
team are the assistive evidence: no full team present → the worksheet is structured and
marked **"study not yet performed"**, never presented as a completed HAZOP. The
**New / Revalidation / Write-up** study-mode branch is in scope for v1.0 (a revalidation
adds the change-delta / prior-recommendation-status view); it is the already-resolved
scope, not a new gap. A deviation, cause, consequence, or severity the team did not raise
is recorded `[GAP]`, never invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every defined node has every relevant guideword×parameter cell analysed or explicitly `[GAP]`/"not credible — justified" — no silently empty cells.
- [ ] Each deviation traces a sound Deviation → Cause → Consequence → Existing-safeguard → Recommendation chain; a consequence with no credible cause (or a cause with no consequence) is flagged incomplete.
- [ ] No unmitigated high-consequence deviation: any high-severity deviation lacking a safeguard AND a closing recommendation is surfaced.
- [ ] Recommendations are actionable (specific change + node link + named owner + due date), not "review further" / "consider".
- [ ] Each node carries its normal-operation design intent, and deviations are judged against that stated intent — not against an unstated one.
- [ ] The worksheet names the multidisciplinary team + competencies (process, operations, instrumentation/SIS, mechanical, chair/scribe) and reads as team-recorded; an incomplete team carries the "study not yet performed" banner, and no deviation the team did not raise appears (FLAG).

## Sign-off note
SME review: ran (persona: Chartered process-safety engineer & certified HAZOP chair); this
is **decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
