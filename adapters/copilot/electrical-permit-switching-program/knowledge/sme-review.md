---
sme-review:
  personas:
    - role: "Authorised / Senior Authorised Person (HV) — Chartered Electrical Engineer with operational switching authority (CEng / PE)"
      expertise: "Electrical safety-rules and switching authority for HV/LV apparatus: the ordered switching sequence (isolate → prove dead → earth → sanction → restore) and the safety-document control (permit-to-work for dead work; sanction-to-test for controlled re-energization); NFPA 70E Article 120 (establishing + verifying an electrically safe work condition), Annex K and 120.5; OSHA 29 CFR 1910.269 (T&D — 269(d) lockout/tagout, 269(n) protective grounding, 269(m) de-energizing lines and equipment), 1910.333 (selection and use of work practices), and 1910.147 (the LOTO standard); UK EAWR 1989 regs 12–13 (means of cutting off supply + isolation / working dead) and HSG85 (electricity at work — safe working practices), with the prove-test-prove discipline and protective-earthing requirement by voltage; and India CEA / state electricity rules and line-clearance permit practice via hse-india."
      lens: "Is the program de-energize-led and isolation-first — is the de-energization / isolation decision (the Article 120 ESWC) recorded BEFORE work, and does the ordered switching sequence enumerate every point of isolation? Is every work step gated behind PROVE-DEAD (prove-test-prove) AND protective earthing where the procedure / voltage requires it — is working un-proven or un-earthed flagged rather than authorised? Is the sanction-to-test kept DISTINCT from a permit-to-work (controlled re-energization for testing is never a work-on-dead permit)? Is each switching step authorised at the right level (authorised vs senior authorised person by voltage)? Is the 1910.269 grounding / EAWR reg 12–13 isolation citation accurate, and is restoration controlled (cancel the document, remove earths, remove locks/tags)? Is a prior switching / electrocution incident de-identified to role level with ZERO leak?"
---

# SME Review & Sign-off — electrical-permit-switching-program

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into an **Authorised / Senior Authorised Person (HV)** — a chartered
electrical engineer with operational switching authority. The universal hard gates (de-id leak,
citation accuracy, HoC/no-PPE-led, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The de-energization / isolation decision is recorded FIRST, before work** — the Article 120
      ESWC decision (`KB-SNIP-DEENERGIZE-FIRST`) leads the program and every point of isolation for
      the named apparatus is enumerated; a program that leads with PPE or that cannot enumerate its
      points of isolation is the headline failure (`controls.validate_treatment`).
- [ ] **Every work step is gated behind PROVE-DEAD and protective earthing** — the sequence applies
      the prove-test-prove discipline (`KB-SNIP-SWITCHING-SEQUENCE`) and applies protective earthing
      where the procedure / voltage requires it. **Work authorised on apparatus isolated but not
      proven dead, or with earthing omitted where required, is REJECTED — never the program.**
- [ ] **The sanction-to-test is kept DISTINCT from a permit-to-work** — controlled re-energization
      for testing (sanction-to-test) is never issued as a work-on-dead permit, and vice versa.
      Conflating the two safety documents is a document-discipline failure.
- [ ] **Each switching step is authorised at the right level** — authorised vs senior authorised
      person by operating voltage; an HV step authorised below the required competence is a FLAG.
- [ ] **The grounding / isolation duty is cited correctly** — OSHA **1910.269(d)** (LOTO) /
      **269(n)** (protective grounding) / **1910.147**, EAWR **regs 12–13** + HSG85, NFPA 70E
      **Article 120**. An omitted or wrong citation is a regulatory_citation_accuracy hard-fail.
- [ ] **Restoration is controlled** — on completion the safety document is cancelled, earths are
      removed, and locks/tags are removed under the switching schedule before supply is restored.
- [ ] **A prior switching / electrocution incident is de-identified** — no named injured operator,
      no `<5` injury cell, no embedded re-identification key (a leak is a de_identification
      hard-fail).

## Sign-off note
SME review: ran (persona: Authorised / Senior Authorised Person (HV) — Chartered Electrical
Engineer); this is **decision-support only**. It **precedes — and never replaces — the human
competent-person review**, and it never outputs the affirmative claim that the work is approved. A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
