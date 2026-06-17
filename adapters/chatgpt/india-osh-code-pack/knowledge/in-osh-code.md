<!-- KB-REG-IN-OSH-CODE -->
# India — OSH Code 2020 (transitional consolidation of 13 labour laws, legacy-first)

**Fragment ID:** `KB-REG-IN-OSH-CODE`
**What this is:** the transition **citation map** for the Occupational Safety,
Health & Working Conditions Code, 2020 (Act 37 of 2020) — what it consolidates, the
single-registration / single-return direction of travel, the savings clause, and the
**state-by-state commencement** status. **This is data, not the Code text** — a skill
reads it *alongside* the legacy fragment to append the transition note.
**What this is NOT:** a live commencement tracker, and NOT a numbered-form catalogue.
The Code's Central/State OSH Rules are **draft / partially notified**; this fragment
carries the *direction* of change, not live form numbers.

> Source: Occupational Safety, Health and Working Conditions Code, 2020 (Act 37 of 2020) + draft Central/State OSH Rules — status in flux · Year: 2026 · Reviewed: 2026-06-17 · Volatile: true · **Staleness window: 90 days** (D-05c — the law is ACTIVELY TRANSITIONING; surfaces a freshness WARN earlier than the 180d default).

**Status: `beta` (transitional).** This fragment is consumed legacy-first: the
**legacy state form is always the primary answer** (`KB-REG-IN-STATEFORMS`), and the
OSH-Code mapping is offered only as an explicit, opt-in transition mode with a warning
that the consolidated form/portal may not be live in the user's state.

## What the Code consolidates (the 13 laws)
The OSH Code 2020 repeals + consolidates 13 central labour laws, including:
- The **Factories Act 1948** (→ `KB-REG-IN-FACTORIES` / `KB-REG-IN-STATEFORMS`)
- The **BOCW Act 1996** (→ `KB-REG-IN-BOCW`)
- The **Mines Act 1952** (→ `KB-REG-IN-MINES-ACT` / `KB-REG-IN-DGMS`)
- The Contract Labour (R&A) Act, the Inter-State Migrant Workmen Act, the Dock
  Workers Act, the Plantations Labour Act, the Working Journalists Acts, the Motor
  Transport Workers Act, the Beedi & Cigar Workers Act, the Sales Promotion Employees
  Act, and the Cine-Workers Act.

## Direction of travel (in principle)
| Legacy pattern | OSH-Code consolidation | Live? |
|---|---|---|
| Per-law registration (Factories/BOCW/Mines licence) | **Single registration** (one registration covering the establishment) | Direction only — state Rules largely pending `[GAP]` |
| Multiple per-law periodic returns | **Single consolidated annual return** | Direction only — form not live in most states `[GAP]` |
| Per-law accident notice | Accident-notice duty **retained** | Duty retained; legacy notice still filed |
| Per-state portals | Move toward unified filing (Shram Suvidha) | Partial — verify per state (`KB-REG-IN-PORTALS`) |

## Savings clause (why legacy-first holds)
The Code carries a savings clause: until a provision is **commenced** and the relevant
state notifies its OSH Rules, **legacy filings under the repealed Acts remain valid**.
Commencement is **state-by-state** and as of review is largely **pending** — only a
handful of states (e.g. Gujarat) have notified their OSH Rules. Therefore:
- Cite the **legacy state form** as the primary, defensible answer (no national OSH
  form number is hard-coded — that would be a fabrication the row-blind citation
  grader cannot catch; emit `[GAP]` for any unnotified consolidated form).
- Append the transition note: *"OSH Code 2020 consolidates this into a single
  return/registration in principle; your state's OSH Rules are [notified / pending] —
  verify before relying on the consolidated form."*

## How the skills use this fragment
- `india-osh-code-pack` reads this fragment (status: beta) to produce a transition
  briefing: legacy-first form + the consolidated direction + a per-state commencement
  caveat, every unnotified consolidated form marked `[GAP]`, never invented.
- The other India skills (`factories-act-returns`, `bocw-compliance`,
  `india-accident-notice`) append this fragment's transition note to their
  legacy-first answer; they do not re-author it.
- The **90-day staleness window** (D-05c, the 06-01 rule-9 per-fragment override) trips
  a freshness WARN sooner than the 180d default — appropriate for a law whose
  commencement status changes state-by-state.
