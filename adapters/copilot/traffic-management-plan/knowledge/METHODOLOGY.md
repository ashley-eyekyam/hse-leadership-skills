# Methodology — Construction traffic management (CDM 2015 Reg 27 + Schedule 3, segregation-by-design)

The traffic-management method this skill applies. The skill **reads** the segregation-by-design
hierarchy (`KB-SNIP-TRAFFIC-SEGREGATION`) and **ranks** controls via `KB-SNIP-HOC` (the optional
`controls` engine ranks / validates a residual conflict's treatment). The defining constraint:
**segregation by design** — separate people from vehicles by design, with the banksman as the
**LAST** resort, not the headline control. There is **no traffic-flow or risk-scoring calculator**.

## 0. De-identify the inputs (before any drafting)
Run the `deid` block + `references/deid-checklist.md`. This is the **lowest-PII** skill (site /
route-level), but any **named driver / operative / banksman** and **every fitness-for-duty / health
detail** in the inputs (e.g. a named driver in a prior reversing near-miss) is scrubbed to a
**role / location label** before any analysis. **The TMP carries no named individual** in the
circulated plan — there is no duty-holder exception here.

## 1. Map the site & routes (the specificity anchor)
From Q1 / Q3 lay out the **named** vehicle routes, the **named** pedestrian routes, the access
points, the loading / delivery bays, the welfare route, and the conflict points (gates, crossings,
blind corners, shared routes). **An unnamed route or "the site roads" is a `[GAP]` and a stop —
never invented.** Refuse a generic site (the GATE).

## 2. Identify every vehicle-pedestrian conflict point
For each Q2 / Q3 interface name **what** conflicts (reversing HGV vs operative crossing, forklift
vs pedestrian on a shared route, the public footway vs the site access) and **where**. Routes must
be **suitable, sufficient and separated** (Schedule 3).

## 3. Apply the segregation-by-design hierarchy (the core-value lever)
For **every** conflict point apply `KB-SNIP-TRAFFIC-SEGREGATION` **in order**:
1. **Eliminate the conflict / design out reversing** — drive-through / one-way systems, remove
   pedestrians from the vehicle area, reduce vehicle movements.
2. **One-way & turning arrangements** — turning circles, dedicated loading / unloading bays so
   vehicles do not reverse into the work area.
3. **Physical segregation** — barriers, segregated pedestrian routes, edge protection, gated
   crossing points; separate site access for vehicles and people.
4. **Signage, speed limits & lighting** — warning of approach (Schedule 3), speed limits, signage,
   adequate lighting at conflict points.
5. **Banksman / traffic marshal — the LAST resort** — a trained banksman only where a higher-order
   control cannot eliminate the residual reversing / manoeuvring risk.

A pedestrian control whose only treatment is **"hi-vis and a banksman" with no physical or temporal
segregation is flagged PPE/admin-led and pushed up the hierarchy** (`controls.validate_treatment`
→ `ppe_admin_only=True` with no higher-order control and no justification is a **defect** the
Critic/QA pass must catch). Rank every residual control via `KB-SNIP-HOC`.

## 4. Reversing elimination (Q4)
Where reversing is present, the plan **leads with eliminating it**: a one-way system, a turning
circle, or a drive-through loading bay so vehicles do not reverse into the work area. A banksman is
the residual control **after** the higher-order options are designed in — never the headline. A
continuous reversing profile makes this section **mandatory**.

## 5. Loading / delivery management
Schedule deliveries (banked / booked-in delivery windows to reduce queueing and ad-hoc reversing),
set the loading / unloading bays, the holding area, and the routing to and from them.

## 6. Speed limits & signage (Schedule 3 — warning of approach)
Set the site speed limit, the signage at conflict points, the lighting at crossings, and the
wheel-wash / road-cleanliness provision where the highway interface needs it.

## 7. Public / highway interface (Q5)
For a footway-adjacent or live-highway interface, set the pedestrian protection (hoarding, covered
way, protected footway), the highway-signing duty (where applicable), and the public segregation.
**The public is never controlled by a banksman alone.** A live-highway interface makes this
section **mandatory**.

## 8. Enforcement, monitoring & review (SMART actions)
Set who enforces the plan on site, the monitoring (route inspections, near-miss capture), and the
**review schedule** (a re-plan trigger on any change of phase, access, traffic type, or delivery
profile) — each as a **SMART action with a named owner (role) + a review date**.

## 9. Validate + assemble
Run `references/QUALITY_CHECKLIST.md`, then build `report.json`
(`assets/traffic-management-plan.report.json`) and render via the `report-output` block.

## Regulatory grounding
- **UK** — **CDM 2015 Reg 27** (organise the site so pedestrians and vehicles move safely) +
  **Schedule 3** (traffic routes — suitable / sufficient / separated, warning of approach) via
  `KB-REG-CDM2015` (the traffic-routes row added in 14-01) + **HSE HSG144** *The safe use of
  vehicles on construction sites*; the bundle clause cross-walk `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`
  carries the **Reg 27 + Schedule 3 → Traffic Management Plan** row.
- **US** — **29 CFR 1926 Subpart O** (motor vehicles, mechanised equipment & marine operations) +
  **1926.601 / .602** via `KB-REG-OSHA1926`.
- **India** — defers to `hse-india`; **mandatory state detection** via `KB-REG-IN-STATEFORMS`; the
  state site-traffic obligation is a **literal `[GAP]`, never a minted national form number**.
- **Always** — ISO 45001 6.1.2 / 8.1.2 (`KB-STD-ISO45001`) + `KB-SNIP-HOC` on every control, and
  `KB-SNIP-TRAFFIC-SEGREGATION` (the segregation-by-design hierarchy) read every run.
