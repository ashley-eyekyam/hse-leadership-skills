<!-- KB-SNIP-CPP-STRUCTURE -->
# Construction Phase Plan — proportionate content skeleton (CDM 2015 Reg 12)

**Fragment ID:** `KB-SNIP-CPP-STRUCTURE`
**This is prompt text, applied by the model — not a generator.** It is the
**proportionate** Construction Phase Plan content skeleton under CDM 2015 Regulation
12(1)–(2): management & arrangements / site rules / significant-risk controls by
activity. It forces a CPP built from the *named* project's real high-risk activities,
not a boilerplate template. Consumed by `construction-phase-plan` (CON-01).

> Source: CDM 2015 (SI 2015/51) Reg 12(1)–(4) + HSE L153 ACOP · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the proportionate CPP skeleton

A Construction Phase Plan is proportionate to the project's risk — a small
refurbishment's plan is short; a multi-contractor new-build's is fuller. Build these
sections, scaled to the named project:

1. **Project description & programme** — the named project, scope, duration, key dates.
2. **Management & arrangements** — duty-holders and responsibilities (Reg 13 PC
   duties), induction, consultation, supervision, emergency arrangements, welfare.
3. **Site rules** — the site-specific rules everyone on site must follow.
4. **Significant risks & controls by activity** — for each significant/high-risk
   activity present (the Schedule 3 set: work at height · excavation/ground works ·
   demolition · lifting operations · confined spaces · work near water/services · hot
   works), the **hierarchy-of-controls-ranked** control with a named owner — work at
   height leads with **collective protection**, never PPE as the headline control.
5. **Notification status** — state the F10/notifiable position (a notifiable project's
   plan must state the duty); a sole contractor still owns the CPP under Reg 12(2).
6. **Review schedule** — the CPP is reviewed and updated through the project
   (Reg 12(3)–(4)).

## Discipline
- Refuse a generic "a building site" — force the named project + ≥1 significant
  activity + the contractor configuration before producing a plan.
- A missing input (no PCI, unknown ground) is a `[GAP]`, never invented.
- Every significant activity has a named control + owner via `KB-SNIP-HOC`; a
  boilerplate-only plan is not a CPP.

## How the skill uses this fragment
`construction-phase-plan` references `KB-SNIP-CPP-STRUCTURE` for the content skeleton,
grounds the duties on `KB-REG-CDM2015`, ranks every control via `KB-SNIP-HOC`, and
emits the CPP report. The PCI it consumes and the H&S File it feeds are cross-walked in
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP`.
