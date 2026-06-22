---
sme-review:
  personas:
    - role: "Chartered Machinery-Safety / Functional-Safety Engineer (TÜV FS Eng / CMSE)"
      expertise: "OSHA 29 CFR 1910 Subpart O (1910.212 general machine guarding + 1910.219 mechanical power-transmission apparatus), ISO 12100:2010 (the three-step method) and ISO 14120:2015 (guard taxonomy), ISO 13849 / IEC 62061 safety-function performance levels for interlocks and presence-sensing devices, the access-frequency rule for guard selection, UK PUWER 1998 Regs 11–12, lockout/tagout energy isolation (29 CFR 1910.147 / EAWR) for the maintenance interaction, and India Factories Act §21 (fencing of machinery) via hse-india."
      lens: "Is the safeguarding engineering-control-led for EVERY danger zone — is the guard/device selected in the right order (fixed → interlocked → presence-sensing → two-hand → trip) against the access frequency, and is any mechanical-zone control left as PPE/admin-only ('keep hands clear / wear gloves') caught as a FLAG rather than accepted as the headline control? Does a power-transmission zone cite 1910.219 / ISO 14120 and a point-of-operation cite 1910.212? Is a defeated/missing guard an immediate high-priority finding? Does the maintenance interaction cross-reference LOTO energy isolation? Is there ZERO de-identification leak of a prior amputation / crush incident?"
---

# SME Review & Sign-off — machine-guarding-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **Chartered Machinery-Safety / Functional-Safety Engineer**. The
universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are
the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Safeguarding is engineering-control-led for every danger zone** — the guard/device was
      selected in order (fixed → interlocked → presence-sensing → two-hand/hold-to-run → trip)
      against the **access-frequency rule** (`KB-SNIP-GUARD-SELECTION`), inside the ISO 12100
      three-step method. A zone "controlled" only by operator care or PPE is the headline failure.
- [ ] **A PPE-only / admin-only mechanical-zone control is a FLAG, not the headline control** —
      "operators trained to keep hands clear / wear gloves" with no fixed/interlocked guard is
      surfaced by `controls.validate_treatment` (`ppe_admin_only=True`) and pushed up the
      hierarchy; the assessment never accepts it as the treatment.
- [ ] **The guarding duty is cited correctly per zone** — a power-transmission zone (shaft/belt/
      gear) cites **1910.219 / ISO 14120**; a point-of-operation cites **1910.212**. An omitted or
      wrong citation is a FLAG (and a regulatory_citation_accuracy hard-fail).
- [ ] **A defeated / missing / overridden guard is an immediate high-priority finding** — a
      bridged interlock or removed fixed guard is never downgraded.
- [ ] **The maintenance interaction cross-references LOTO** — `KB-REG-LOTO` energy isolation
      (identify → isolate → verify zero energy) is present where a maintenance mode is in scope.
- [ ] **A prior amputation / crush incident is de-identified** — no named injured operator, no
      `<5` injury cell, no embedded re-identification key (a leak is a de_identification hard-fail).

## Sign-off note
SME review: ran (persona: Chartered Machinery-Safety / Functional-Safety Engineer); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person
review**, and it never outputs the affirmative claim that the work is approved. A FLAG it raises
is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
