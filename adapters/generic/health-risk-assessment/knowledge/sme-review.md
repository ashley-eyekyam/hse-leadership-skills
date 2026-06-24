---
sme-review:
  personas:
    - role: "Occupational Hygienist / Occupational Health Physician"
      expertise: "Similar-exposure-group (SEG) definition, exposure characterisation and comparison to a cited OEL/WEL/PEL (EH40 WELs, OSHA PELs, ACGIH TLVs), ergonomics scoring (RULA / REBA / NIOSH lifting equation, ISO 11228 / ISO/TR 12296), OEL-linked health-surveillance regimes (COSHH / Control of Noise / Control of Vibration / OSHA 1910.95), and special-category health-data confidentiality."
      lens: "Is every SEG named and specific, every exposure compared to a CITED OEL (source+year), every ergonomic score from the engine (not narrated), are controls driven up the hierarchy ABOVE PPE and ABOVE surveillance, is the surveillance schedule OEL-linked — and is there ZERO special-category health leak (no named surveillance result, no <5 health-outcome cell)?"
---

# SME Review & Sign-off — health-risk-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into an **Occupational Hygienist / Occupational Health
Physician**. The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only,
owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **SEGs are specific** — each SEG names the task/role and the agent it is exposed to; a generic SEG ("all staff", "the workforce") is a FLAG.
- [ ] **Every exposure is compared to a CITED OEL** — measured/estimated exposure vs the binding OEL/WEL/PEL with source+year (from `KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS`); an exposure with no cited limit, or a fabricated limit, is a FLAG. No data → a monitoring strategy is recommended, not a fabricated comparison.
- [ ] **Ergonomic scores come from the engine** — RULA/REBA/NIOSH figures are the `ergonomics` engine's output (tool-named), not narrated prose; a free-text "high RULA risk" with no engine score is a FLAG.
- [ ] **Controls beat the hazard, above PPE AND above surveillance** — substitution/engineering precede PPE; a noise plan offering only hearing protection, or "controlled by surveillance", is a FLAG. Surveillance is monitoring, not a control.
- [ ] **The surveillance schedule is OEL-linked** — cadence is triggered by the exposure-vs-action-level/OEL comparison (audiometry / lung-function / HAV), not asserted; a surveillance schedule with no OEL linkage is a FLAG.
- [ ] **Special-category health data is protected** — surveillance/exposure results reported by SEG/role, `<5` health-outcome cells suppressed, never circulated with names; a named audiometry/biological-monitoring result or a `<5` cell is a FLAG (and a de_identification hard-fail).

## Sign-off note
SME review: ran (persona: Occupational Hygienist / Occupational Health Physician); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person
sign-off**, and it never outputs the affirmative claim "approved by a competent person". A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
