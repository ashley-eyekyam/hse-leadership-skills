---
sme-review:
  personas:
    - role: "Chartered / Professional Electrical Engineer (NFPA 70E / IEEE 1584 arc-flash-study competent; CEng / PE)"
      expertise: "NFPA 70E (2024) 130.4 (shock risk assessment + limited/restricted approach boundaries), 130.5 (arc-flash risk assessment), 130.5(G) (the incident-energy analysis method), 130.5(H) (equipment label content), 130.7(C)(15) (the PPE-category table alternative), Article 120 (establishing + verifying an electrically safe work condition), and Annex J (the energized electrical work permit); the IEEE 1584-2018 incident-energy + arc-flash-boundary model (208 V – 15 kV) and its required inputs (bolted fault current, protective-device clearing time, electrode configuration, gap, working distance); OSHA 29 CFR 1910.333(a)(2) (de-energize-first + the additional-hazard/infeasibility test) and 1910.269 (utility T&D approach distances); UK EAWR 1989 reg 14 (the dead-working default + the three-part live-working test) + HSG85; and India CEA / state electricity rules via hse-india."
      lens: "Is the assessment de-energize-led — is the de-energization decision (the Article 120 ESWC) recorded BEFORE any PPE, and is any energized work justified against OSHA 1910.333(a)(2) or EAWR reg 14 rather than on convenience/production grounds? Is the incident energy, the arc-flash boundary, and the PPE category COMPUTED by the IEEE 1584-2018 engine and traced to its inputs — never narrated, and never built on an invented fault current or clearing time (a missing input is a [GAP])? Is arc-rated PPE the documented last line rather than the headline control? Is >40 cal/cm² flagged as energized work prohibited, and is the 1.2 cal/cm² arc-flash-boundary threshold and the 130.5(H) label content correct? Is a prior arc-flash burn / electrocution incident de-identified to role level with ZERO leak?"
modes:
  assessment:
    detected_by: "Q = the requested deliverable (an arc-flash assessment for the named equipment/task) — single-output skill; this mode is always active"
    floor:
      - id: de-energization-decision-first
        description: "The de-energization decision (the NFPA 70E Article 120 ESWC) is recorded FIRST, before any PPE"
        anchors: ['de-energiz|de-energis|eswc|article 120', 'first|primary|decision|before']
        min_matches: 2
      - id: energized-work-justified
        description: "Energized work is justified against OSHA 1910.333(a)(2) / EAWR reg 14, never assumed on convenience/production grounds"
        anchors: ['energized work|energised work|1910.333|eawr', 'justif']
        min_matches: 1
      - id: incident-energy-computed
        description: "The incident energy (cal/cm2) is COMPUTED via IEEE 1584-2018, never narrated or invented"
        anchors: ['incident energy|cal/cm|ieee 1584', 'comput']
        min_matches: 2
      - id: thresholds-label-correct
        description: "The arc-flash boundary + approach boundaries and the NFPA 70E 130.5(H) label content are correct"
        anchors: ['arc.flash boundary|approach boundar|70e', 'label|130.5|boundary']
        min_matches: 2
      - id: arc-rated-ppe-last-line
        description: "Arc-rated PPE is the documented LAST line of defence, never the primary control"
        anchors: ['arc.rated', 'ppe|last']
        min_matches: 2
      - id: prior-incident-deidentified
        description: "A prior arc-flash burn / electrocution incident is de-identified — no named injured person"
        anchors: ['de-identif|role label', '\[gap|injured|incident|de-id']
        min_matches: 1
---

# SME Review & Sign-off — arc-flash-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **Chartered / Professional Electrical Engineer** (NFPA 70E / IEEE
1584 arc-flash-study competent). The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-led, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The de-energization decision is recorded FIRST, before any PPE** — the Article 120 ESWC
      decision (`KB-SNIP-DEENERGIZE-FIRST`) leads the assessment; an arc-flash treatment that
      **leads with arc-rated PPE when the task could be de-energized** is the headline failure,
      surfaced by `controls.validate_treatment` (`ppe_admin_only=True`) and pushed up the hierarchy.
- [ ] **Energized work is justified, never assumed** — where Q2 = no, the justification meets OSHA
      1910.333(a)(2) ("additional/increased hazard or infeasible") **or** EAWR reg 14; a bare
      "production can't stop / it's quicker" is **rejected** (economic convenience is not a
      justification) and an energized-work permit (Annex J) is triggered.
- [ ] **The incident energy is COMPUTED, never narrated** — the cal/cm² value, the arc-flash
      boundary, and the PPE category come from the IEEE 1584-2018 engine (`arcflash.py`) and trace
      to their inputs; an invented fault current or clearing time, or a free-text "looks like CAT 2"
      guess, is the failure mode this skill exists to prevent. A missing required input is a `[GAP]`.
- [ ] **The thresholds + label content are correct** — the arc-flash boundary is the distance to
      **1.2 cal/cm²**; `>40 cal/cm²` flags energized work as **prohibited** (blast, not just
      thermal); the **NFPA 70E 130.5(H)** label content (nominal voltage, boundary, available
      incident energy + working distance *or* PPE category, study date) is present. A wrong
      threshold or omitted clause is a regulatory_citation_accuracy hard-fail.
- [ ] **Arc-rated PPE is the documented last line** — never the primary control; it is the
      residual-hazard protection after de-energization, engineering, and approach control.
- [ ] **A prior arc-flash burn / electrocution incident is de-identified** — no named injured
      worker, no `<5` injury cell, no embedded re-identification key (a leak is a de_identification
      hard-fail).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The narrated incident energy (S5)** — a cal/cm² value stated in prose rather than computed via
  IEEE 1584-2018 from the supplied parameters is fabricated rigour; compute it or [GAP] the missing
  parameter.
- **The de-energize-first lever skipped (assistive boundary)** — the ESWC de-energization decision
  is the primary control and is recorded before any PPE; a plan that jumps to arc-rated PPE without
  the de-energize evaluation inverts the hierarchy.
- **The burn-response leg dropped (S1)** — arc-flash controls set out but no emergency/first-aid
  response for a burn/electrocution casualty, and no rescue-from-contact arrangement.
- **The label with no basis** — an NFPA 70E 130.5(H) label whose boundary/PPE figures are not
  traced to the computed incident energy is a sticker, not a control.

## Sign-off note
SME review: ran (persona: Chartered / Professional Electrical Engineer); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person
review**, and it never outputs the affirmative claim that the work is approved. A FLAG it raises
is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
