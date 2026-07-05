---
sme-review:
  personas:
    - role: "Asset-integrity / inspection engineer (API 510 pressure vessels / 570 piping / 580 RBI; PSM element (j))"
      expertise: "Equipment criticality ranking; risk-based inspection (RBI) interval defensibility; ITPM scheduling; integrity-operating-windows (IOWs); deficiency / fitness-for-service management."
      lens: "Is the inspection strategy genuinely risk-based with defensible intervals, and is no item silently assumed fit-for-service without an integrity basis?"
modes:
  program-register:
    detected_by: "Q13 — What output, for whom? (Criticality register / ITPM schedule / Deficiency plan / Full report — all legs of the one criticality-ranked integrity program register)"
    floor:
      - id: bounded-equipment-population
        description: "A named equipment population/unit with its in-scope classes stated (vessels, piping, relief devices, tanks…) — never 'our equipment' (intake Q2/Q3 specificity anchor)"
        anchors: ['equipment population|equipment register', 'relief|vessel|piping|tank']
        min_matches: 2
      - id: criticality-cof-x-likelihood
        description: "Criticality per item = consequence-of-failure × likelihood drivers (age, service, corrosion, damage mechanism) banded on the named matrix — not nameplate size or age alone (intake Q4)"
        anchors: ['criticality', 'consequence of failure|damage mechanism']
        min_matches: 2
      - id: itpm-interval-basis
        description: "Each class's ITPM interval/method carries its stated basis — RBI (damage mechanism + rate), code (API 510/570/653), or statutory; an interval with no basis is flagged (intake Q5)"
        anchors: ['ITPM|inspection interval', 'RBI|API 5']
        min_matches: 2
      - id: no-fit-without-integrity-basis
        description: "No item is assumed fit-for-service without an integrity basis — a basis-less item reads a literal [GAP], never 'assumed fit' (the skill's core discipline)"
        anchors: ['fit.for.service', 'integrity basis']
        min_matches: 1
      - id: deficiency-interim-risk-owned
        description: "Each open deficiency carries an interim-risk judgement + a HoC-ranked remediation (higher-order control, not monitoring alone) + a named role owner + due date (intake Q7)"
        anchors: ['deficien', 'interim risk']
        min_matches: 2
      - id: iow-degradation-windows
        description: "Integrity operating windows (IOWs) are framed for items whose process conditions drive degradation (intake Q5)"
        anchors: ['integrity.operating.window|IOW']
        min_matches: 1
      - id: statutory-examination-dates
        description: "Statutory inspection/examination obligations and their due dates are recorded per the jurisdiction hook — PSM element (j) / Factories Act examination (intake Q10/Q11/Q12)"
        anchors: ['statutory (examination|inspection)', '1910\.119|Factories Act']
        min_matches: 1
      - id: inspection-authority-role
        description: "The inspection authority / owner of the ITPM basis is named as a role (API-authorised inspector, statutory competent person) (intake Q8)"
        anchors: ['inspection authority', 'owner of the ITPM|ITPM basis owner|authori[sz]ed inspector']
        min_matches: 1
---

# SME Review & Sign-off — mechanical-integrity

This skill carries **one** specialized SME lens: an asset-integrity / inspection engineer.
It narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`)
to the asset-integrity / PSM element (j) program; the generic **HSE-SME-Reviewer** hook is
the inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**No item is fit-for-service without an integrity basis.** The failure mode this lens
guards is an item silently assumed fit with no inspection basis behind it — recorded
instead as `[GAP]`, never "fit for service". Risk-based intervals must trace to a stated
RBI basis (damage mechanism + rate); a class-specific inspection strategy (vessels →
thickness/CML, relief devices → test interval, tanks → API 653) applies. The inspection
authority / owner of the ITPM basis is the assistive-evidence anchor.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each item's criticality reflects consequence-of-failure × likelihood (age, service, corrosion, damage mechanism) — not nameplate size or age alone.
- [ ] Where risk-based intervals are used, they trace to a stated RBI basis (damage mechanism + rate); an interval with no basis is flagged.
- [ ] Any item lacking an integrity basis reads `[GAP]`, never "assumed fit".
- [ ] Integrity-operating-windows (IOWs) are defined for items whose process conditions drive degradation.
- [ ] Each open deficiency carries an interim-risk judgement AND a higher-order remediation control; a deficiency "controlled" by monitoring/administration alone is flagged.
- [ ] Every row carries equipment · criticality band · ITPM interval · deficiency status · named owner — no orphan rows (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **Intervals without a basis** — a tidy ITPM schedule whose intervals trace to nothing
  (no damage mechanism, no rate, no code clause); the register looks managed but every
  date in it is arbitrary.
- **Deficiencies managed by watching** — open deficiencies each 'controlled' by increased
  monitoring or an operator check, with no higher-order remediation and no interim-risk
  judgement; deferral dressed as management.
- **The silently-fit item** — rows whose fitness column is populated by absence: no
  inspection history, no thickness data, yet nothing reads [GAP]; the most dangerous
  items are the quietest ones.
- **Statutory dates missing from a 'risk-based' register** — RBI logic present but the
  statutory examination clock (PSM (j) audits aside, the pressure-vessel legal interval)
  never appears; a legally-overdue vessel can hide in a green register.

## Sign-off note
SME review: ran (persona: Asset-integrity / inspection engineer, API 510/570/580); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
