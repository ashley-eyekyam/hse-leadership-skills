<!-- KB-DATA-LIFT-CATEGORIES -->
# Lift categorisation — BS 7121 basic / standard / complex criteria (with source+year)

**Fragment ID:** `KB-DATA-LIFT-CATEGORIES`
**Discipline:** the lift **category** sets the planning depth and whether an
appointed-person written plan is mandatory. Each criterion below is a **cited
classification test**, not a number to assert blindly; the SWL/utilisation values are
read from the manufacturer's rated-capacity chart (an input, transcribed and checked),
never computed by the skill. Pairs with `KB-REG-LOLER-BS7121` (the LOLER Reg 8/9 +
appointed-person method).

> Volatile: false · last_reviewed: 2026-06-22 (review window 180 days, D-05).

---

## Classification rule

1. Assess the lift against the BS 7121 category criteria below — the **highest**
   triggered band sets the category.
2. The category sets the planning depth: a **complex** lift mandates a written lift
   plan, a named appointed person, and contingency/abort criteria.
3. Confirm the load weight (incl. rigging) and the SWL at the working radius before
   planning — an unconfirmed weight is a `[GAP]`, never assumed.

## BS 7121 lift categories (cite the code + the triggering criterion)

| Category | Typical criteria | Planning depth it sets |
|---|---|---|
| **Basic** | single crane, light/known load well within SWL, good ground, no proximity hazard, routine repetitive lift | competent operator + slinger; documented safe method |
| **Standard** | single crane, load a significant fraction of SWL-at-radius, some proximity/ground considerations | named appointed person; documented lift plan |
| **Complex** | tandem/multi-crane lift, blind lift, lift over the public/occupied area, load near the SWL, poor/unknown ground, or overhead-line/structure proximity | appointed-person **written** lift plan + contingency/abort + supervision |

## Utilisation / proximity thresholds (transcribed inputs, each cited)

| Parameter | Test (resolve the value from the source) | Source line to quote |
|---|---|---|
| SWL-at-radius utilisation | load (incl. rigging) ÷ rated capacity at the working radius; above the planned safe-utilisation margin → re-select equipment | "manufacturer's rated-capacity chart, [model], [year]" |
| Overhead-line proximity | minimum safe clearance / exclusion distance from live overhead lines | "GS6 *Avoiding danger from overhead power lines*, [year]" |
| Ground bearing | ground assessed to support outrigger/track loads; unknown ground → confirm before lifting | "manufacturer outrigger loads + site ground report, [year]" |

**Present every value as:** `<parameter> = <value> (<source>, <year>)`. Resolve the
current edition of BS 7121 / GS6 and the specific rated-capacity chart at use time.

> Source: BS 7121 *Safe Use of Cranes* (lift-categorisation framework) + HSE GS6 (overhead-line clearance) + the manufacturer's rated-capacity chart (per-lift) · Year: 2026 (framework); confirm the current edition + the specific chart at use time.
