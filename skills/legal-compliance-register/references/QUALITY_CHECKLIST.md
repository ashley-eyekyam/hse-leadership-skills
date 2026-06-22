# Pre-output Quality Checklist — legal-compliance-register

Before producing any output, validate the draft against this gate. A failure here is a
defect the Critic/QA and SME passes must catch before the register is presented.

## Applicability rigour (the core-value lever)
- [ ] **Every listed obligation is confirmed APPLICABLE** to a named in-scope activity — it carries a one-line applicability rationale; no inapplicable regulation is listed (e.g. no construction/confined-space reg for a pure office).
- [ ] No obligation is listed for a jurisdiction or activity **not captured in the intake** — the register's scope matches Q1 (jurisdictions) + Q3 (activity profile).

## India deferral (D-04)
- [ ] India obligations **defer to `hse-india`** — the leg names `india-state-form-finder` / `factories-act-returns` and routes after **state detection** (Q1a / `KB-REG-IN-STATEFORMS`).
- [ ] **No national India form number is minted** — an unverified state-specific form reads `[GAP]`; the legacy state form is the primary answer with the OSH-Code transition flagged.
- [ ] The India leg **never hard-blocked** the rest of the register (graceful degradation held).

## Completeness + evidence (9.1.2)
- [ ] **Every obligation row is complete** — applicability rationale + compliance-evidence cell + named (role-label) owner + review date.
- [ ] **Compliance is evaluated** — each obligation marked Compliant / Gap / [GAP-evidence]; every gap has an owner + a target date + a `KB-SNIP-HOC`-ranked SMART action (validated by `smart_actions`).

## Citation accuracy
- [ ] Every UK/US/EU obligation cites the correct jurisdiction's instrument (UK HSWA/MHSWR · US OSH Act/specific 29 CFR standard · EU 89/391 + member-state transposition); no invented or mis-jurisdiction citation.

## De-identification
- [ ] De-identification pass complete BEFORE drafting; named compliance owners + any enforcement/disciplinary detail are role-labelled in the shared register; no identifier leak and no re-identification key embedded.
