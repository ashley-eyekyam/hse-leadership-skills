<!-- KB-DATA-ALCRM-BANDS -->
# Level-crossing risk bands — ALCRM (record the user's band, values [GAP])

**Fragment ID:** `KB-DATA-ALCRM-BANDS`
**What this is:** the framing for the **All Level Crossing Risk Model (ALCRM)** —
the RSSB / Network Rail model that bands every GB level crossing by **individual and
collective risk** so the highest-risk crossings are targeted — grounding
`level-crossing-track-worker-safety` (RAIL-03). It carries the *concept* and
*generic band labels* only.
**What this is NOT:** the ALCRM band **threshold values**. Those are the **licensed
RSSB/NR model output** → they are **`[GAP]` / user-supplied**. The skill **records
the user's ALCRM band, it never recomputes it.** `[ASSUMED A2]`: the exact
embeddable band labels are proprietary — the SME/owner confirms any embeddable
label set before golden-output LOCK; until then, values stay `[GAP]`.

> Source: All Level Crossing Risk Model (ALCRM), RSSB / Network Rail risk model (in use since 2007); band threshold VALUES are the licensed model output (not embedded) · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true (licensed model; resolve embeddable labels with owner/SME at use time).

---

## The concept (labels only)

ALCRM exists to **prioritise** level crossings by risk:
- **Individual risk** — risk to a typical individual user of the crossing.
- **Collective risk** — total risk across all users of the crossing.

The model assigns each crossing a **risk band** (a letter/number grade in the
licensed model) so the highest-risk crossings are targeted for remediation. **The
band boundary VALUES are the licensed RSSB/NR model output → `[GAP]` /
user-supplied.**

## Discipline (D-03 — licensed, cite-not-reproduce)
- Embed the **concept and generic band labels only** — never the proprietary
  threshold numbers or the full grade scale.
- The skill **records the user's ALCRM band** (from their licensed model output) —
  it never recomputes a band.
- A `KB-DATA-ALCRM-BANDS` use that hard-codes numeric band boundaries is a D-03
  violation — reject it.
- If the user has no ALCRM band, the band is `[GAP]`; the remediation hierarchy
  (`KB-REG-LX-TRACKWORKER`) still applies.

## How the skill uses this fragment
RAIL-03 records the user's ALCRM individual/collective band, uses it to prioritise
the crossing for the remedial hierarchy, and leaves the licensed band values
`[GAP]` for SME/owner confirmation (A2) — it never recomputes the licensed model.
