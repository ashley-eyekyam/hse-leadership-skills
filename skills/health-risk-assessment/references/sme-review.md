---
sme-review:
  personas:
    - role: "Occupational Hygienist / Occupational Health Physician"
      expertise: "Similar-exposure-group (SEG) definition, exposure characterisation and comparison to a cited OEL/WEL/PEL (EH40 WELs, OSHA PELs, ACGIH TLVs), ergonomics scoring (RULA / REBA / NIOSH lifting equation, ISO 11228 / ISO/TR 12296), OEL-linked health-surveillance regimes (COSHH / Control of Noise / Control of Vibration / OSHA 1910.95), and special-category health-data confidentiality."
      lens: "Is every SEG named and specific, every exposure compared to a CITED OEL (source+year), every ergonomic score from the engine (not narrated), are controls driven up the hierarchy ABOVE PPE and ABOVE surveillance, is the surveillance schedule OEL-linked — and is there ZERO special-category health leak (no named surveillance result, no <5 health-outcome cell)?"
modes:
  health-risk-assessment:
    detected_by: Q11 — Output artifact wanted + its reader (full HRA report / SEG surveillance schedule / single-hazard check — all render the single HRA at the reader's depth)
    floor:
    - id: hra-named-seg
      description: Named tasks/roles and their similar-exposure groups (SEGs); a generic SEG ('all staff', 'the workforce') is refused (intake Q2, the specificity anchor)
      anchors:
      - similar.exposure group|\bSEG\b
      - task|role
      - exposure group
      min_matches: 1
    - id: hra-exposure-vs-oel
      description: An exposure-vs-OEL comparison per SEG/agent against a cited limit with source + year (intake Q3/Q4; KB-DATA-OEL-LIMITS / KB-DATA-EXPOSURE-LIMITS)
      anchors:
      - OEL|WEL|PEL|TLV
      - exposure
      - source.{0,6}year|20[0-9][0-9]
      min_matches: 1
    - id: hra-exposure-basis-honest
      description: The exposure figure is evidence-based and never fabricated — measured/sampled data cited to a source, or where no data exists a monitoring strategy is set FIRST (intake Q3; never invent an exposure or a limit)
      anchors:
      - measured|sampl|monitoring strateg|monitoring plan|exposure data
      - cited|source|EH40|reference period
      - not fabricat|never invent|\[GAP\]|no.{0,4}data
      min_matches: 1
    - id: hra-controls-hierarchy
      description: Exposure controls ranked up the hierarchy (elimination / substitution to engineering to administrative to RPE/PPE last), with the initial-vs-residual baseline (intake Q10)
      anchors:
      - hierarchy of controls|elimination|substitut
      - engineering
      - residual
      min_matches: 1
    - id: hra-health-surveillance-deid
      description: Health surveillance appropriate to each hazard (audiometry, lung function, HAVS) reported de-identified by SEG — special-category data (intake ELI-EVIDENCE)
      anchors:
      - health surveillance|surveillance
      - audiometry|lung function|HAVS
      - de.identif|by SEG
      min_matches: 1
    - id: hra-vulnerable-and-owner
      description: The exposed population per SEG including vulnerable groups (young / new-or-expectant, contractors, agency), plus the competent assessor (occupational hygienist / OH physician role) + action owners + a review cycle (intake Q9/Q12/Q13)
      anchors:
      - vulnerable|new.or.expectant|contractor|agency
      - occupational hygien|OH physician|competent person|assessor
      - review
      min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **An OEL comparison fabricated where there is no exposure data** — with Q3 = none-yet the artifact must recommend a monitoring strategy first and record `[GAP]`, never invent an exposure or a limit; a confident exposure-vs-OEL table on no data is the signature failure.
- **The OEL cited without source + year, or the wrong SEG granularity** — a generic 'all staff' SEG, or a limit with no jurisdiction WEL/PEL/TLV source and year, strands the comparison's defensibility.
- **Vulnerable groups and health surveillance dropped** — young / new-or-expectant workers, contractors and agency staff in the exposed population, and the hazard-appropriate surveillance (audiometry / lung function / HAVS) reported de-identified by SEG, are quietly omitted from otherwise clean HRAs.

## Sign-off note
SME review: ran (persona: Occupational Hygienist / Occupational Health Physician); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person
sign-off**, and it never outputs the affirmative claim "approved by a competent person". A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
