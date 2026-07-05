---
sme-review:
  personas:
    - role: "Process-hazard-analysis (HAZID) facilitator / lead process-safety engineer"
      expertise: "Broad early-stage hazard identification across process, mechanical, electrical, external/natural, environmental, utilities-loss and neighbouring-installation knock-on categories; risk-ranked hazard registers; life-cycle-stage sweeps (concept / FEED / detailed design / pre-commissioning)."
      lens: "Has the early-stage sweep covered every hazard category — including the external, environmental and domino hazards a narrow node-HAZOP skips — or has a whole category been silently dropped?"
modes:
  register:
    detected_by: "Q9 — What output, for whom? (Hazard register / Full report — both emit the risk-ranked hazard register, the skill's single artifact class)"
    floor:
      - id: bounded-installation-stage
        description: "One named installation at a named life-cycle stage bounds the sweep (intake Q1 specificity anchor — never 'all our hazards')"
        anchors: ['life.?cycle stage|concept|FEED|detailed design|pre.commissioning', 'installation|project']
        min_matches: 2
      - id: category-sweep-complete
        description: "Every selected hazard category addressed or explicitly [GAP]'d — process · mechanical · electrical · external/natural · environmental · utilities loss · neighbouring-installation knock-on (intake Q2; none silently dropped)"
        anchors: ['external|natural hazard', 'utilit', 'knock.on|domino']
        min_matches: 2
      - id: external-natural-site-real
        description: "The external/natural-hazard lines (flood · seismic · wind · lightning) are populated for the ACTUAL site's exposure — HAZID's value over a node HAZOP, not token entries"
        anchors: ['flood', 'seismic', 'lightning|wind']
        min_matches: 2
      - id: environmental-receptors-in-range
        description: "Environmental release pathways carry named receptors (workers, public, watercourses, habitat) — a pathway with no receptor is meaningless (intake Q3)"
        anchors: ['receptor', 'watercourse|habitat|groundwater']
        min_matches: 1
      - id: hazard-row-chain-whole
        description: "Each register row's Hazard → Cause → Consequence → Existing-controls → Recommendation chain is whole; unaddressed cells read [GAP], not blank"
        anchors: ['cause', 'consequence', 'existing control']
        min_matches: 3
      - id: team-disciplines-recorded
        description: "The multidisciplinary team + disciplines are recorded as roles (chair/scribe named as roles); an incomplete team carries the 'study not yet performed' banner (intake Q5/Q6, the assistive evidence)"
        anchors: ['multidisciplinary|disciplines', 'chair|scribe']
        min_matches: 1
      - id: ranked-recommendations-tracked
        description: "Each hazard risk-ranked on the named matrix and each recommendation carries a named role owner + due date tracked to closure (intake Q7; smart_actions discipline)"
        anchors: ['risk rank|risk band', 'named owner|action owner', 'due date']
        min_matches: 2
---

# SME Review & Sign-off — hazid-facilitator

This skill carries **one** specialized SME lens: a lead HAZID facilitator. It narrows the
family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) to the broad
early-stage HAZID sweep; the generic **HSE-SME-Reviewer** hook is the inherited fallback.
The universal hard gates (de-id leak, citation accuracy, HoC / no PPE-or-admin-only without
justification, owned-and-dated actions) are the enforced class and are not restated below.

**HAZID is an assistive, team-recorded study at a stage gate.** The bounded installation +
life-cycle stage and the multidisciplinary team are the assistive evidence: no full team
present → the register is structured and marked **"study not yet performed"**, never
presented as a completed HAZID. HAZID's value over a narrow node-HAZOP is exactly the
external, environmental and domino hazards — so a silently dropped category is the failure
mode this lens guards. A hazard or risk rank the team did not raise is recorded `[GAP]`,
never invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every HAZID category (process · mechanical · electrical · external/natural · environmental · utilities loss · neighbouring-installation knock-on) is addressed or explicitly `[GAP]`'d — none silently dropped.
- [ ] The external & natural-hazard line (flood / seismic / wind / lightning) is genuinely populated for the actual site, not a token entry — this is HAZID's value over a node HAZOP.
- [ ] Domino / knock-on escalation from or to neighbouring installations is assessed where relevant, not omitted.
- [ ] Environmental land/water/air release pathways appear where the installation warrants them, with the receptors named (the environmental category is meaningless without receptors).
- [ ] Each finding's Hazard → Cause → Consequence → Existing-controls → Recommendation chain is whole per row; unaddressed categories read `[GAP]`, not blank.
- [ ] Scope is bounded (one named installation / life-cycle stage) and the team + competencies are named; an incomplete team carries the "study not yet performed" banner, and no hazard the team did not raise appears (FLAG).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A process-only register wearing a HAZID label** — the process/mechanical rows are rich
  while the external-natural, environmental and domino categories are one-liners or
  absent; the register silently degrades into a narrow PHA and loses exactly the value a
  HAZID exists to add at a stage gate.
- **Receptors dropped between pathway and rank** — a release pathway is listed and ranked
  with no receptor in the row, so the consequence rank has no target and cannot be
  defended.
- **Siting context never used** — greenfield/brownfield congestion, met/flood exposure and
  neighbouring installations captured at intake but never reflected in any register row.
- **A completed-looking register from an incomplete team** — full rows, plausible ranks, no
  'study not yet performed' banner; the reader cannot tell no multidisciplinary team ever
  sat.

## Sign-off note
SME review: ran (persona: HAZID facilitator / lead process-safety engineer); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
