---
sme-review:
  personas:
    - role: "Principal Contractor (CDM 2015 duty-holder)"
      expertise: "CDM 2015 Regulation 12 construction-phase-plan duties, the F10 notification position, Schedule 3 significant-risk activities, site management & arrangements, and the proportionality of a CPP to the project's risk."
      lens: "would this CPP stand up on a real site and to a regulator — named project (not 'a building site'), every significant activity carrying a hierarchy-ranked control with a named owner, work at height led by collective protection (never a harness as the headline), the F10 / Reg 12 notification position stated for a notifiable project, and the sole-contractor's Reg 12(2) duty not excused"
    - role: "CDM Construction Manager"
      expertise: "The PCI → CPP → H&S File document chain (Reg 4 / 12 / 12(5)), site rules and welfare, emergency arrangements, and the review-and-update discipline through the construction phase."
      lens: "is the plan internally consistent and loosely coupled to the rest of the CDM chain — the one-line PCI / H&S File cross-reference present without assuming a sibling produced them, the Reg 4 gap honestly flagged [GAP] with stated assumptions where the PCI is absent, and a review trigger set for changes of method/sequence"
modes:
  construction-phase-plan:
    detected_by: "Q1 — Output type (the full Regulation 12 construction-phase-plan leg of the produced pack)"
    floor:
      - id: cpp-project-named-specific
        description: "The CPP names the specific project (scope + programme) and its significant-risk activities — it refuses a generic 'a building site' (KB-SNIP-CPP-STRUCTURE)"
        anchors: ['significant risks?', 'programme']
        min_matches: 1
      - id: cpp-at-height-collective-leads
        description: "Work at height leads with collective protection (edge protection / MEWP / nets / elimination); a harness-only headline is pushed up the hierarchy, never the lead control (KB-SNIP-HOC)"
        anchors: ['collective protection', 'edge protection']
        min_matches: 1
      - id: cpp-f10-reg12-notification
        description: "The F10 / Regulation 12 notification position is stated for a notifiable project and the sole contractor's Reg 12(2) ownership of the CPP is not excused (KB-REG-CDM2015)"
        anchors: ['F10', 'reg(ulation)?\s*12\(2\)', 'notifiable']
        min_matches: 1
      - id: cpp-cdm-chain-pci-gap
        description: "The PCI -> CPP -> H&S File chain (Reg 4 -> 12 -> 12(5)) is cross-referenced without assuming a sibling ran; an absent Reg 4 PCI is flagged [GAP] with stated assumptions (KB-SNIP-CONSTRUCTION-CLAUSE-MAP)"
        anchors: ['pre.construction information', 'reg(ulation)?\s*4\b', 'health (&|and) safety file']
        min_matches: 1
      - id: cpp-hoc-ranked-owned-actions
        description: "Every significant activity carries a hierarchy-ranked control and SMART actions carry a named owner + due date + hazard link (KB-SNIP-HOC / KB-STD-ISO45001)"
        anchors: ['hierarchy.ranked', 'hierarchy of controls']
        min_matches: 1
      - id: cpp-welfare-review-discipline
        description: "Welfare (CDM Schedule 2) is provided and the CPP is a live document with a review schedule (Reg 12(3)-(4)) triggered by any change of method/sequence (KB-REG-CDM2015)"
        anchors: ['welfare', 'review schedule']
        min_matches: 1
      - id: cpp-deid-role-labels
        description: "Input-derived persons (e.g. a prior fall-from-height near-miss) are de-identified to role labels; user-supplied duty-holders may stay named as a legitimate record"
        anchors: ['de.identif', 'role label']
        min_matches: 1
---

# SME Review & Sign-off — construction-phase-plan

Two construction-duty lenses review the CPP before any output: the **Principal Contractor**
(the Reg 12 duty-holder) and the **CDM Construction Manager** (the chain-and-arrangements
view). They apply the universal hard gates (no error or unsupported claim, every regulatory
trigger caught, no lower-order-only control without justification, zero de-identification
leak) plus the domain checklist below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The project is **named and specific** (scope + programme) — the CPP **refuses a generic "a building site"**; ≥1 significant activity and the contractor configuration are captured.
- [ ] **Significant risks & controls by activity** are present for every Schedule 3 activity from intake, each with a **hierarchy-ranked control and a named owner**; **work at height leads with collective protection** (edge protection / MEWP / nets / elimination) — a "operatives to wear harnesses" control with no collective protection is **flagged PPE-led and pushed up the hierarchy**, never the headline.
- [ ] The **F10 / Reg 12 notification position is stated** for a notifiable project (a notifiable project that omits the F10 / Reg 12 duty is a citation defect); the **sole contractor's Reg 12(2)** ownership of the CPP is not excused.
- [ ] The **CDM-chain cross-reference** (PCI → CPP → H&S File, Reg 4 → 12 → 12(5)) is present **without assuming a sibling skill ran**; where the **PCI is absent the Reg 4 gap is flagged `[GAP]`** with the assumptions the plan proceeds on.
- [ ] For **India**, the **state is resolved** (defers to `hse-india`) and a **literal `[GAP]`** is emitted where a BOCW state form/return is owed — **never a minted national form number**.
- [ ] Every action carries a **named owner + an ISO due date + a hazard link**; every citation traces to the KB (CDM 2015 Reg 12 / L153 for UK; 29 CFR 1926 Subpart C for US); de-identification holds (role labels for input-derived persons; the user-supplied duty-holders stay named as a legitimate record).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The CPP with no emergency leg (canary S1)** — controls are complete but there is no on-site
  emergency arrangement: fire plan / muster point, an at-height rescue plan, first-aid
  provision, nearest A&E, and the notification chain. A construction-phase plan for an occupied
  site with no rescue-and-emergency section is hollow.
- **The high residual with no interim bridge (canary S2)** — a High-residual activity (e.g.
  leading-edge work held pending edge-protection sign-off) carries a far due date with no
  interim measure, hold-point, or ALARP statement for the gap period.
- **The adjacent/occupied-building interaction never assessed (canary S7)** — SIMOPS between the
  works and the occupied building or the adjacent public footpath (drop zones, shared access,
  live services) assessed as one system, not two legs that never meet.
- **The welfare/exclusion quantitative basis asserted by silence (canary S5)** — welfare sized
  to a stated peak headcount, exclusion-zone distances and person-day counts recorded or
  `[GAP]`'d, never asserted with no inputs.

## Sign-off note
SME review: ran (personas: Principal Contractor + CDM Construction Manager); this is
decision-support that **precedes and never replaces** the human competent-person review, and
it **never** emits a competent-person approval claim on this statutory-adjacent CPP. A FLAG it
raises is recorded, never merge-blocking.
