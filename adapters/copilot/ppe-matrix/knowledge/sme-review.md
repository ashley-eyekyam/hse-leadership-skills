---
sme-review:
  personas:
    - role: "Certified Safety Professional (CSP) / PPE-program lead"
      expertise: "OSHA 29 CFR 1910 Subpart I (1910.132 PPE hazard assessment + the 1910.132(d)(2) written certification) and the body-region sections (.133/.135/.136/.138), the UK/EU PPE at Work Regs 1992 (amended 2022) + EN conformity standards (EN 166/397/149/388/352/ISO 20345), ANSI/ISEA selection standards, the hierarchy of controls with PPE as the residual-only last line, respirator fit-testing and medical-clearance confidentiality, and India Factories Act PPE provisions via hse-india."
      lens: "Did the controls-first gate run for EVERY body-region hazard before any PPE row — is PPE specified only for the residual hazard surviving the higher-order controls, and is a hazard with no higher-order control recorded shown as a controls-first FLAG rather than an invented PPE row? Does every PPE row cite its EN/ANSI conformity standard + year (no asserted protection without the standard)? Is the 1910.132(d)(2) written certification present? Is there ZERO special-category respiratory-clearance / fitness leak (no named clearance note, no <5 health-outcome cell)?"
---

# SME Review & Sign-off — ppe-matrix

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a **Certified Safety Professional (CSP) / PPE-program lead**.
The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated
actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The controls-first gate ran for every hazard** — for each body-region hazard the
      higher-order controls (eliminate / substitute / engineer / administrative) were applied or
      justified BEFORE any PPE row; PPE appears only for the residual hazard surviving them. A
      PPE row for a hazard whose higher-order controls were never considered is a FLAG (the
      headline failure this skill exists to prevent).
- [ ] **A hazard with no higher-order control shows a controls-first flag, not a PPE row** — the
      matrix never invents a PPE row to fill the gate; `controls.validate_treatment` returning
      `ppe_admin_only=True` (or no higher-order control) is surfaced as the flag, the PPE cell
      withheld.
- [ ] **Every PPE row cites its conformity standard + year** — `<PPE type> against <named
      residual hazard>, conforming to <EN/ANSI standard>, <year>`; a protection level asserted
      without the cited standard (`KB-DATA-PPE-STANDARDS`) is a FLAG (and a
      regulatory_citation_accuracy hard-fail).
- [ ] **The written hazard-assessment certification is present** — the 1910.132(d)(2)
      certification block (workplace, certifier role, date); omitting it is a FLAG (and a
      regulatory_citation_accuracy hard-fail). No certifier or date is fabricated — a missing
      input is a `[GAP]`.
- [ ] **Scope is task-specific, not a site-wide sheet** — the matrix names the area/line/role
      set and the tasks; a whole-plant PPE sheet is a FLAG.
- [ ] **Special-category respiratory-clearance / fitness data is protected** — respiratory
      medical-clearance and fitness detail reduced to role level, `<5` health-outcome cells
      suppressed, never circulated with names; a named clearance/fitness note or a `<5` cell is
      a FLAG (and a de_identification hard-fail).

## Sign-off note
SME review: ran (persona: Certified Safety Professional (CSP) / PPE-program lead); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person
review**, and it never outputs the affirmative claim that the work is approved. A FLAG it raises
is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
