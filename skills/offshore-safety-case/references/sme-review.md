---
sme-review:
  personas:
    - role: "Offshore safety-case author / process-safety lead (SI 2015/398)"
      expertise: "MAH identification; SEMS & CMAPP argument; ALARP demonstration framing; the SCE register + performance standards; the independent verification scheme; SI 2015/398 Schedule 6/7 element completeness."
      lens: "Is the safety-case argument complete against the Schedule 6/7 element set, and is the ALARP demonstration genuinely a demonstration — not an unevidenced assertion or an AI-invented QRA number — and is every barrier/SCE claim backed by a cited performance standard rather than asserted effective?"
    - role: "QRA-provenance & SCE-verification reviewer"
      expertise: "Consequence/likelihood-modelling provenance; ALARP cost-benefit framing; SCE performance-standard verification; distinguishing fabricated from externally-supplied quantitative results."
      lens: "Is every quantitative figure traceable to an external, competent QRA — never computed or invented by the skill — is every SCE/barrier-effectiveness claim tied to a verifier finding or performance standard, and is an absent number/claim an honest [GAP] rather than a guess? And is there NO 'accepted/approved/authorised' language anywhere (acceptance is the competent authority's act)?"
---

# SME Review & Sign-off — offshore-safety-case

Two distinct competencies own two failure modes on an offshore safety case: the **argument's
completeness against the SI 2015/398 Schedule 6/7 elements** (the safety-case author) and the
**provenance of every quantitative figure and every barrier/SCE-effectiveness claim** (the
QRA-provenance & verification reviewer). So this skill carries **two** SME lenses. Both
specialize the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`),
narrowed here to the Offshore Safety Case — the first lens carries the element-completeness
remit, the second carries its "team-recorded, not autonomous AI judgement" check applied to
the externally-done QRA/consequence modelling and the SCE verification. The generic
**HSE-SME-Reviewer** hook is the inherited fallback. The universal hard gates (de-id leak,
citation/clause accuracy, HoC / no PPE-or-admin-only without justification, every action
owned-and-dated) are the enforced class and are deliberately not restated below.

**The Schedule 6/7 elements are CONFIRMED in the KB.** `KB-REG-OFFSHORE-SCR`
(`knowledge-base/regulatory/offshore-scr.md`) enumerates them as a duty→element map:
**MAH identification**, **SEMS**, **CMAPP**, **ALARP demonstration**, the **SCE register +
performance standards**, the **independent verification scheme**, and **emergency response**.
The checklist below leans on that confirmed enumeration; a missing element is recorded as
`[GAP]`, never invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] All Schedule 6/7 elements present and credited from `KB-REG-OFFSHORE-SCR` — MAH identification · SEMS · CMAPP · ALARP demonstration · SCE register + performance standards · independent verification scheme · emergency response — each populated or explicitly `[GAP]`'d; the element set matches the SI 2015/398 (current) regime, with SCR 2005 named only as the superseded legacy reference.
- [ ] ALARP is a demonstration, not an assertion: the framing shows risk reduced to ALARP via the measures actually taken; "risks are ALARP" with no supporting argument is flagged.
- [ ] Every quantitative result (QRA, consequence distance, ALARP cost-benefit figure, MAH frequency) is recorded as externally produced by a competent person WITH provenance — none computed or invented by the skill; an absent number reads `[GAP]`, never a fabricated value.
- [ ] No barrier / SCE is asserted effective without a cited performance-standard evidence reference or a verifier finding; an un-evidenced "barrier is effective" claim is flagged and downgraded to `[GAP]`.
- [ ] The MAH scenarios trace to the PHA inputs (HAZID/HAZOP/bowtie) for this installation — not a generic substance-class list — and the SEMS delivers the CMAPP policy commitments (no policy claim unsupported by an SMS element).
- [ ] The EER element is **cross-referenced** to the sibling `marine-emergency-response` (MAR-03) plan, not rebuilt; and the whole output reads as duty-holder-supplied, structured work, not an autonomously authored safety case — and carries NO "accepted / approved / authorised" language (FLAG).

## Sign-off note
SME review: ran (personas: offshore safety-case author / process-safety lead + QRA-provenance
& SCE-verification reviewer); this is **decision-support only**. It **precedes — and never
replaces, never emits — the human competent-person sign-off**, and it never outputs "approved
by a competent person" nor any "accepted / approved / authorised by the regulator" status
(acceptance is the competent authority's — HSE + OPRED — act). A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted
score below threshold) are a separate enforcement class owned by the automated harness.
