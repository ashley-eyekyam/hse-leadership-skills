---
sme-review:
  personas:
    - role: "DROPS / dropped-objects-prevention SME (offshore at-height securing specialist)"
      expertise: "The DROPS Recommended Practice (2017) + DROPS Reliable Securing, IADC HSE Guidelines Section 16, API RP 2D (offshore crane O&M) / API RP 54 (drilling & servicing); dropped-object survey method, static vs dynamic taxonomy, the reliable-securing hierarchy (primary fixing + secondary retention), exclusion-zone control, and the licensed-vs-public boundary of the DROPS Calculator consequence-band table."
      lens: "would a DROPS practitioner accept this — is every at-height item surveyed and reliably secured (not 'hard hats below'), does every consequence band trace to its user-supplied m·g·h inputs (no invented mass/height, no reproduced licensed threshold table), and is the prior struck-by/fatality context de-identified"
modes:
  assessment:
    detected_by: "Q = the requested deliverable (a dropped-objects / DROPS assessment for the named at-height area) — single-output skill; this mode is always active"
    floor:
      - id: reliable-securing-led
        description: "The lead posture is reliable securing of at-height items, never 'hard hats below' as the primary control"
        anchors: ['reliable securing|reliably secured', 'hard hat|below']
        min_matches: 1
      - id: static-dynamic-taxonomy
        description: "Every register entry is classified static (falling potential) vs dynamic (in-motion/handled) — an unclassified entry is a FLAG"
        anchors: ['static', 'dynamic']
        min_matches: 2
      - id: consequence-band-traces-mgh
        description: "Every consequence band traces to the user-supplied mass·gravity·height inputs — no invented mass/height, no reproduced licensed threshold table"
        anchors: ['consequence', 'mass|height|kinetic']
        min_matches: 2
      - id: dropped-object-register
        description: "A dropped-object register surveys the at-height items with their securing method — a survey-less assessment is a FLAG"
        anchors: ['register', 'at.height|item|survey']
        min_matches: 2
      - id: residual-rescored-after-securing
        description: "Residual risk is re-scored after reliable securing + exclusion zones — an unre-scored residual is a FLAG"
        anchors: ['residual', 're-scored|exclusion zone']
        min_matches: 2
      - id: citations-resolve-india-defer
        description: "DROPS RP / IADC / API RP citations resolve; unverified thresholds are [GAP] and India defers, never a fabricated value"
        anchors: ['drops|iadc|api rp|regulatory', '\[gap|cited|defer']
        min_matches: 1
      - id: smart-actions-owned
        description: "Every action is a SMART action with a role-label owner and a date"
        anchors: ['smart|action', 'owner|role|date']
        min_matches: 2
---

# SME Review & Sign-off — dropped-objects-prevention

The reviewer adopts the **DROPS / dropped-objects-prevention SME** persona above. It applies the
universal hard gates (no unsupported claim, every regulatory/practice trigger caught, no
lower-order-only control without justification, ZERO de-identification leak) PLUS the domain
checklist below. A FLAG it raises is recorded; it precedes and never replaces the human
competent-person review, and it never emits sign-off language.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Reliable-securing-led, not "hard hats below"** — every at-height item has the survey +
  reliable-securing (primary fixing + secondary retention) + exclusion-zone control as the
  headline; a "hard hats for the people below" treatment is FLAGGED and pushed up the hierarchy
  (`KB-SNIP-DROPS-SECURING`), never accepted as the primary control. An at-height item with no
  recorded securing standard is an immediate high-priority finding.
- [ ] **Static vs dynamic taxonomy complete** — every register entry is classified static (falls
  from a static position) or dynamic (knocked/swung/dropped during an operation) per `KB-REG-DROPS`;
  the DROPS survey covers the named area's at-height structures, not a generic checklist.
- [ ] **Consequence band traces to m·g·h, never invented or licensed** — every consequence band
  traces to its **user-supplied** mass + fall height via the public `E ≈ m·g·h` method
  (`KB-DATA-DROPS-IMPACT`); no mass/height is invented, and the **licensed DROPS Calculator
  threshold VALUES are NOT reproduced** — the user's band is recorded and the thresholds stay
  `[GAP]` / user-confirmed (A1 `[ASSUMED]`).
- [ ] **Citations resolve; India deferral honored** — DROPS RP / IADC §16 / API RP 2D & RP 54 are
  cited by topic (never the practice text reproduced); an India installation defers to `hse-india`
  with state detection (`KB-REG-IN-OFFSHORE`), emitting `[GAP]`, never a national form number.
- [ ] **De-identification holds (lower tier)** — asset/installation data dominates, but any prior
  struck-by / fatality dropped-object context is de-identified to role label; no named worker, no
  `<5` injury cell, no re-identification key in the circulated output. Every action has a named
  role owner + a review date.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The exclusion-zone / emergency leg dropped (S1)** — reliable securing is set out but the
  dropped-object exclusion zones, barricading, and the response if an object does fall (stop work,
  area check) are silently omitted; the plan controls the cause but not the consequence.
- **The invented mass/height (S5)** — a consequence band asserted without the user-supplied
  m·g·h inputs, or with a reproduced licensed threshold table, is fabricated rigour. Trace each
  band to its inputs or [GAP] it.
- **The unclassified register entry** — an at-height item logged with no static/dynamic
  classification and no securing method is a row that proves nothing.
- **The un-owned action** — a securing/inspection action with no role owner and no date is a
  finding, not a fix.

## Sign-off note
SME review: ran (persona: DROPS / dropped-objects-prevention SME); this is decision-support;
competent-person review still required. A FLAG it raises is recorded, never merge-blocking — it
precedes and never replaces the human competent-person review.
