---
sme-review:
  personas:
    - role: "Control-of-work / permit-to-work authority (PTW issuing authority; LOTO & confined-space competent person)"
      expertise: "High-risk-task permits (hot work, confined-space entry, line-breaking, excavation, work-at-height); energy isolation (LOTO) & gas testing; SIMOPS coordination; permit validity & conditions."
      lens: "Are the isolations engineered (not permit-paper alone), and is every concurrent operation in the area actually coordinated rather than left as an uncontrolled clash?"
---

# SME Review & Sign-off — permit-to-work

This skill carries **one** specialized SME lens: a control-of-work / PTW issuing authority.
It narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`)
to the control-of-work / PTW package with its in-skill SIMOPS coordination section; the
generic **HSE-SME-Reviewer** hook is the inherited fallback. The universal hard gates
(de-id leak, citation accuracy, HoC / no PPE-or-admin-only without justification,
owned-and-dated actions) are the enforced class and are not restated below.

**Isolations must be engineered, and SIMOPS must be coordinated.** The failure modes this
lens guards are an isolation relying on the permit (administrative) alone rather than a
physical LOTO/gas-test, and a detected concurrent operation left as an uncontrolled clash.
SIMOPS is handled as a coordination control *within this permit* — never deferred to a
non-existent standalone workflow — and each permit type carries its type-specific mandatory
controls (CS rescue plan, hot-work fire watch, excavation services-scan).

## Domain checklist (the nuanced things only this expert catches)
- [ ] Energy isolation (LOTO) and atmosphere control (gas test) are physical/engineered; an isolation relying on the permit (administrative) alone is flagged.
- [ ] Where concurrent operations exist, the SIMOPS section names the conflicting activities AND the coordination controls (sequencing, exclusion zones, single point of coordination, cross-permit refs) and the authorizing authority — no detected clash left uncoordinated.
- [ ] SIMOPS is a permit/coordination control within this permit — never deferred to a non-existent standalone workflow.
- [ ] The controls match the named high-risk task (hot-work fire watch + combustibles removed, confined-space gas test + attendant + rescue, excavation buried-services scan + shoring) — not a generic permit body.
- [ ] The permit is marked invalid until the isolations and (where SIMOPS exists) the coordination controls are confirmed in place.
- [ ] Permit conditions and a bounded validity period / shift-handover rule are stated; an open-ended permit is flagged (FLAG).

## Sign-off note
SME review: ran (persona: Control-of-work / PTW issuing authority); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
