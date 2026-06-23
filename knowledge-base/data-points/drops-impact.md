<!-- KB-DATA-DROPS-IMPACT -->
# Dropped-object impact energy — the public m·g·h method (band values [GAP])

**Fragment ID:** `KB-DATA-DROPS-IMPACT`
**What this is:** the **public impact-energy method** for classifying a dropped
object's consequence — impact energy ≈ **mass × g × fall height** (`m·g·h`,
public physics) → a consequence band — grounding `dropped-objects-prevention`
(MAR-02). It carries the *method* and *generic band labels* only.
**What this is NOT:** the **DROPS Calculator consequence-band threshold table.**
Those threshold **values are proprietary/licensed** → they are **`[GAP]` /
user-confirmed**. The skill **records the user's band, it never recomputes the
licensed thresholds**. `[ASSUMED A1]`: the exact embeddable band thresholds are
the licensed DROPS Calculator output — the SME/owner confirms any embeddable band
labels before golden-output LOCK; until then, values stay `[GAP]`.

> Source: DROPS Calculator impact-energy method (public formula m·g·h); consequence-band threshold VALUES are the licensed DROPS Calculator table (not embedded) · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true (licensed table; resolve embeddable values with owner/SME at use time).

---

## The public method (formula only)

Impact energy of a falling object (ignoring drag):

```
E ≈ m · g · h
  m = mass of the object (kg)            — user-supplied
  g = 9.81 m/s² (gravitational accel.)   — public constant
  h = fall height (m)                     — user-supplied
E in joules (J)
```

The energy figure is then mapped to a **consequence band** (generic labels such as
*minor → major → fatal-potential*). **The band boundary VALUES are the licensed
DROPS Calculator table → `[GAP]` / user-confirmed.**

## Discipline (D-03 — licensed, cite-not-reproduce)
- Embed the **formula and generic band labels only** — never the proprietary
  threshold numbers.
- The skill **records the user's DROPS band** (from their licensed Calculator) or
  reports the `m·g·h` energy with the band left `[GAP]` if the user has no band.
- A `KB-DATA-DROPS-IMPACT` use that hard-codes numeric band boundaries is a D-03
  violation — reject it.
- `mass` and `fall height` are always user-supplied; never invented → `[GAP]`.

## How the skill uses this fragment
MAR-02 computes the public `m·g·h` energy where mass+height are supplied, records
the user's licensed DROPS consequence band, and leaves the licensed threshold
values `[GAP]` for SME/owner confirmation (A1) — it never recomputes the licensed
table.
