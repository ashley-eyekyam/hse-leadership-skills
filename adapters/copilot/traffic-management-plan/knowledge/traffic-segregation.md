<!-- KB-SNIP-TRAFFIC-SEGREGATION -->
# Site traffic — segregation-by-design hierarchy (CDM 2015 Reg 27 + Schedule 3)

**Fragment ID:** `KB-SNIP-TRAFFIC-SEGREGATION`
**This is prompt text, applied by the model — not a generator.** It is the
segregation-**by-design** control hierarchy for construction site traffic, grounded in
CDM 2015 Regulation 27 (organise the site so pedestrians and vehicles can move safely)
and Schedule 3 (traffic routes — suitable, sufficient, separated; warning of approach).
It forces a plan that separates people from vehicles by design, with the banksman as
the **last** resort, not the headline control. Consumed by
`traffic-management-plan` (CON-05).

> Source: CDM 2015 (SI 2015/51) Reg 27 + Schedule 3 + HSE HSG144 *The safe use of vehicles on construction sites* · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the segregation-by-design hierarchy

Apply controls **in this order** for every vehicle-pedestrian conflict point — a plan
whose only control is "hi-vis and a banksman" is PPE/admin-led and must be pushed up:

1. **Eliminate the conflict** — design out reversing (drive-through / one-way systems),
   remove pedestrians from the vehicle area, reduce vehicle movements.
2. **One-way & turning arrangements** — turning circles, dedicated loading/unloading
   bays so vehicles do not reverse into the work area.
3. **Physical segregation** — barriers, segregated pedestrian routes, edge protection,
   gated crossing points; separate site access for vehicles and people.
4. **Signage, speed limits & lighting** — warning of approach (Schedule 3), speed
   limits, signage, adequate lighting at conflict points.
5. **Banksman / traffic marshal — LAST resort** — a trained banksman only where a
   higher-order control cannot eliminate the residual reversing/manoeuvring risk.

## Discipline
- Uncontrolled reversing with no Reg 27 / Schedule 3 grounding is a citation +
  specificity failure — name the routes, do not produce a generic plan.
- Routes must be **suitable, sufficient and separated** (Schedule 3); the public /
  live-highway interface pulls in the relevant traffic-signing duty.
- Every residual control is ranked via `KB-SNIP-HOC`.

## How the skill uses this fragment
`traffic-management-plan` references `KB-SNIP-TRAFFIC-SEGREGATION` for the
segregation-by-design hierarchy, grounds Reg 27 + Schedule 3 on `KB-REG-CDM2015` (which
carries the traffic-routes row), and emits the TMP for the named site.
