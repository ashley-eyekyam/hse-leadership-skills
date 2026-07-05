---
sme-review:
  personas:
    - role: "Level-crossing / track-worker safety SME (Network Rail safety-of-people-on-or-near-the-line competent person)"
      expertise: "NR/L2/OHS/019 (Safety of People Working On or Near the Line) practice, the level-crossing remedial hierarchy (closure -> grade separation -> engineering -> sighting/signage/admin), the track-worker protection hierarchy (separation/green-zone/line-blockage/possession -> SSOW -> warning/TOWS -> lookout-only), COSS role and Sentinel competence, ORR level-crossing strategic-risk guidance and the LXRMTK, and how the ALCRM model bands and prioritises crossings (a recorded model output, never recomputed in an artifact)"
      lens: "would a rail safety regulator / Network Rail competent person accept this safe system of work — is the crossing led by closure / grade separation / engineering (NOT new signage where a higher order is reasonably practicable), is the track work led by separation (green-zone / line blockage / possession, NOT a lookout alone), is the ALCRM band RECORDED from the user's licensed model output and never invented/recomputed, and is every COSS / Sentinel / lookout role-holder de-identified to a role label?"
modes:
  crossing-assessment:
    detected_by: "Q1 — What does this assessment cover? (Level-crossing risk and remediation / Both → the crossing-remedial-hierarchy section)"
    floor:
      - id: named-crossing-and-type
        description: "Names THIS crossing (location/chainage) and its crossing type (user-worked / AHB / MCB / footpath) — never 'a level crossing' (intake Q2/Q3 specificity anchor)"
        anchors: ['crossing', 'user.worked|half.barrier|manually.controlled|footpath|chainage']
        min_matches: 2
      - id: remedial-hierarchy-led
        description: "The treatment is led by the crossing remedial hierarchy — closure → grade separation → engineering (barriers / obstacle detection / MSL) → sighting/signage/admin LAST; a signage-led treatment where a higher order is reasonably practicable is rejected (KB-SNIP-LX-HIERARCHY)"
        anchors: ['closure', 'grade separation', 'signage|sighting']
        min_matches: 2
      - id: alcrm-band-recorded-never-computed
        description: "The ALCRM individual/collective band is RECORDED from the user's licensed model output (or a literal [GAP] where none exists) — never invented, recomputed, or hard-coded (intake Q4; KB-DATA ALCRM row, D-03)"
        anchors: ['ALCRM']
        min_matches: 1
      - id: csm-ra-significance-where-changed
        description: "Where altering the crossing/asset is a significant change: the CSM-RA significance test + risk-acceptance principle + independent AsBo evidence appears (intake Q7; KB-REG-CSM-RA)"
        anchors: ['CSM.?RA', 'significan']
        min_matches: 1
      - id: residual-risk-5x5-scored
        description: "Residual risk after the chosen treatment is scored on the 5×5 matrix (risk_matrix output)"
        anchors: ['residual risk', '5.?[x×].?5']
        min_matches: 2
      - id: gaps-closed-smart-role-owned
        description: "Every [GAP] (ALCRM band, standard issue/date, site specifics) is closed with a SMART action carrying a named ROLE owner and a due date — never an invented value"
        anchors: ['named (role )?owner|owner \(role', 'due date']
        min_matches: 1
      - id: crossing-roles-de-identified
        description: "The site-safety roles (crossing keeper, COSS, lookout) appear as role labels with accountabilities — never personal names or Sentinel numbers"
        anchors: ['COSS|crossing keeper', 'role label|\(role\)']
        min_matches: 1
      - id: nr-l2-ohs-019-grounding
        description: "Grounded in NR/L2/OHS/019 + the ORR level-crossing guidance, cited by reference from KB-REG-LX-TRACKWORKER — never reproduced"
        anchors: ['NR/L2/OHS/019', 'KB-REG-LX-TRACKWORKER']
        min_matches: 1
  trackwork-ssow:
    detected_by: "Q1 — What does this assessment cover? (Track-worker (on or near the line) safe system of work / Both → the trackworker-protection-hierarchy section)"
    floor:
      - id: named-worksite-line-status
        description: "Names THIS work site/section, the track activity, and the line status (open / line blockage / possession) — never 'the track' (intake Q2/Q3)"
        anchors: ['possession|line block', 'work.?site|worksite|section']
        min_matches: 2
      - id: separation-led-protection
        description: "Protection is led by separation — green-zone / line blockage / possession → safe systems of work → warning (TOWS) → lookout-only LAST; a lookout-led system where separation is reasonably practicable is rejected (KB-SNIP-LX-HIERARCHY)"
        anchors: ['green.?zone', 'possession', 'lookout']
        min_matches: 2
      - id: red-zone-minimised-justified
        description: "Any red-zone (open-line) working is minimised and carries the 'higher order not reasonably practicable' justification — never the default"
        anchors: ['red.?zone', 'minimis|justif']
        min_matches: 2
      - id: coss-picop-roles-accountable
        description: "COSS / PICOP / engineering supervisor / lookout accountabilities appear as role labels (Sentinel competence framing; no personal names or Sentinel numbers)"
        anchors: ['COSS', 'PICOP|engineering supervisor']
        min_matches: 2
      - id: gang-briefing-arrangements
        description: "The site/gang briefing arrangements for the safe system of work are stated for the named audience (intake Q10)"
        anchors: ['brief']
        min_matches: 1
      - id: residual-risk-5x5-scored
        description: "Residual risk under the chosen protection arrangement is scored on the 5×5 matrix (risk_matrix output)"
        anchors: ['residual risk', '5.?[x×].?5']
        min_matches: 2
      - id: gaps-closed-smart-role-owned
        description: "Every [GAP] and open action is closed with a SMART action carrying a named ROLE owner and a due date"
        anchors: ['named (role )?owner|owner \(role', 'due date']
        min_matches: 1
      - id: nr-l2-ohs-019-grounding
        description: "Grounded in NR/L2/OHS/019 (safety of people working on or near the line), cited by reference from KB-REG-LX-TRACKWORKER"
        anchors: ['NR/L2/OHS/019', 'KB-REG-LX-TRACKWORKER']
        min_matches: 1
---

# SME Review & Sign-off — level-crossing-track-worker-safety

This skill carries **one** SME lens, narrowing the level-crossing / track-safety archetype
(`KB-SNIP-ARCHETYPES`). The crossing-remediation view and the track-worker-protection view
are a lens *within* the same reviewer, so a 2nd persona is not justified. The universal hard
gates (de-id leak, citation accuracy, HoC/no-lower-order-only, owned-and-dated actions) are
the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The level-crossing treatment is led by the remedial hierarchy** — **closure → grade separation → engineering (barriers / obstacle detection / MSL / full-barrier) → sighting / signage / administrative LAST.** Flag any crossing whose *lead* control is new signage / admin while closure, grade separation, or engineering is reasonably practicable — that is the indefensible "controlled it with a sign" failure (`KB-SNIP-LX-HIERARCHY`).
- [ ] **The track-work system is led by separation** — **green-zone working / line blockage / possession → safe systems of work → warning (TOWS) → lookout-only LAST.** Flag any track task whose *lead* control is a lookout alone (red-zone) while separation is reasonably practicable; red-zone working must be minimised, never the default.
- [ ] **The ALCRM band is RECORDED, never invented or recomputed.** The artifact records the user's individual/collective band (or `[GAP]` if none was supplied) and uses it to prioritise the crossing. Flag any artifact that fabricates an ALCRM band, recomputes one, or hard-codes numeric ALCRM thresholds — the band values are the licensed RSSB/NR model output (D-03).
- [ ] **NR/L2/OHS/019 and the ALCRM/LX guidance are cited by reference, not reproduced.** The NR/L2/OHS/019 issue/date is `[ASSUMED A3]` → confirm the current issue/date is correct and citable before LOCK; never paste the standard's text.
- [ ] **The COSS / Sentinel competence framing is present and role-labelled** — the site-safety roles (COSS, lookout, PICOP, engineering supervisor, crossing keeper) are named *as roles* with their accountabilities, never as personal names or Sentinel numbers.
- [ ] **Residual risk is scored on the 5×5 matrix** and every `[GAP]` (the ALCRM band, the issue/date, site specifics) is closed with a SMART action carrying a named **role** owner and a due date — never an invented value.
- [ ] **Site specificity** — names *this* crossing / work site; a generic "a level crossing" artifact is flagged.
- [ ] **India** content cites the Railways Act 1989 / CRS framing and defers state-specific content to `hse-india` after state detection — no national form invented.
- [ ] **Sibling boundary** — the artifact does not rebuild the rail SMS (RAIL-01) or the ROGS application pack (RAIL-02); it references them where relevant (CONV-12).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The hierarchy applied backwards, invisibly** — new signage/sighting works presented as
  the remediation with no record that closure, grade separation or engineering was ever
  tested for reasonable practicability; the artifact looks diligent while leading with
  the LAST-resort order.
- **A lookout system with no separation case** — the SSOW reads complete (briefing, PPE,
  positions) but never shows why a line blockage or possession was not reasonably
  practicable; red-zone by default, undeclared.
- **Prioritisation without the band** — remediation urgency asserted with no recorded
  ALCRM band and no [GAP] admitting its absence; the priority claim has no basis a
  regulator can check.
- **The unchanged-asset assumption** — the works alter the crossing (new equipment,
  changed operation) but the CSM-RA significance question is never asked; the change
  slips past the assessment regime entirely.

## Sign-off note
SME review: ran (persona: Level-crossing / track-worker safety SME — NR/L2/OHS/019 +
ALCRM); this is **decision-support only**. It **precedes — and never replaces, never emits —
the human competent-person (rail-SME / accountable-manager) sign-off**, and it never outputs
the affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
