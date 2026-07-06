---
sme-review:
  personas:
    - role: "Construction Logistics / Temporary Works (Traffic) Coordinator"
      expertise: "Construction site traffic management under CDM 2015 Reg 27 + Schedule 3 and HSE HSG144 — vehicle/pedestrian route design, the segregation-by-design hierarchy (eliminate/design-out reversing → one-way & turning → physical segregation → signage/speed/lighting → banksman last), loading & delivery management, one-way systems and turning circles, and the public / live-highway interface."
      lens: "would this traffic plan keep people and vehicles apart on the named site and stand up to a regulator — the site + access points + traffic types named (never a generic site), EVERY vehicle-pedestrian conflict point led by SEGREGATION-BY-DESIGN with a 'hi-vis + banksman only' pedestrian control flagged and pushed up the hierarchy, reversing led by ELIMINATION (one-way / turning / drive-through), routes SUITABLE / SUFFICIENT / SEPARATED with warning of approach (Schedule 3), and the public never controlled by a banksman alone"
modes:
  traffic-management-plan:
    detected_by: "Q1 — Output type (the CDM Reg 27 / Schedule 3 site traffic management plan)"
    floor:
      - id: tmp-named-site-routes-gate
        description: "The GATE holds — the named site + its access points + at least the vehicle and pedestrian traffic types, with named routes; the plan refuses a generic 'the site roads' (KB-SNIP-TRAFFIC-SEGREGATION)"
        anchors: ['(north|south) gate', 'suitable.{0,4}sufficient.{0,6}separated']
        min_matches: 1
      - id: tmp-segregation-by-design-leads
        description: "Segregation-by-design leads at EVERY conflict point; a 'hi-vis + banksman only' pedestrian control is flagged PPE/admin-led and pushed up the hierarchy — never the headline (KB-SNIP-HOC)"
        anchors: ['segregation.by.design', 'segregated (pedestrian )?walkway']
        min_matches: 1
      - id: tmp-reversing-eliminated
        description: "Reversing leads with elimination — a one-way system, turning circle, or drive-through loading bay; a banksman is the residual control AFTER the higher-order options are designed in"
        anchors: ['one.way', 'turning circle', 'reversing.{0,24}eliminat|eliminat.{0,24}reversing']
        min_matches: 1
      - id: tmp-routes-suitable-loading-mgmt
        description: "Routes are suitable/sufficient/separated (Schedule 3) with warning of approach; loading/delivery is managed (booked windows, bays, holding area) to remove ad-hoc reversing (KB-REG-CDM2015)"
        anchors: ['warning of approach', 'timed windows|booked.in', 'holding area']
        min_matches: 1
      - id: tmp-public-highway-interface
        description: "The public/live-highway interface is protected by hoarding/covered way/protected footway and the highway-signing duty — the public is never controlled by a banksman alone"
        anchors: ['hoarding', 'covered way', 'never.{0,20}banksman']
        min_matches: 1
      - id: tmp-speed-signage-lighting
        description: "Speed limits, signage and lighting are set at the conflict points (warning of approach, Schedule 3)"
        anchors: ['speed limit', 'signage', 'lighting']
        min_matches: 1
      - id: tmp-monitoring-review-deid
        description: "Enforcement/monitoring + a review schedule (owned, triggered by any change of phase/access/traffic) are set; the TMP is site/route-level and de-identified — no named individual"
        anchors: ['review schedule', 'de.identif', 'route.level']
        min_matches: 1
---

# SME Review & Sign-off — traffic-management-plan

A **Construction Logistics / Temporary Works (Traffic) Coordinator** reviews the traffic
management plan before any output. They apply the universal hard gates (no error or unsupported
claim, every regulatory trigger caught, no lower-order-only control without justification, zero
de-identification leak) plus the domain checklist below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The **GATE held**: the **named site + its access points** and **at least the vehicle and
  pedestrian types** are present — the plan **refused to proceed on a generic site, an unnamed
  access point, or "the site roads"**, and **named the routes** (no invented layout).
- [ ] **Segregation-by-design leads at EVERY conflict point** (`KB-SNIP-TRAFFIC-SEGREGATION`):
  **eliminate the conflict / design out reversing → one-way & turning → physical segregation →
  signage / speed / lighting → a banksman / traffic marshal LAST**. A pedestrian control whose
  only treatment is **"hi-vis and a banksman" with no physical or temporal segregation is flagged
  PPE/admin-led and pushed up the hierarchy** — never the headline control. This is the core value.
- [ ] **Reversing leads with elimination** — a one-way system, a turning circle, or a drive-through
  loading bay so vehicles do not reverse into the work area; a banksman is the residual control
  **after** the higher-order options are designed in, not the headline.
- [ ] **Routes are suitable, sufficient and separated** (Schedule 3) with **warning of approach**;
  loading / delivery is managed (booked-in windows, bays, holding area) to remove ad-hoc reversing;
  speed limits, signage, and lighting are set at conflict points.
- [ ] The **public / live-highway interface** is protected by hoarding / covered way / protected
  footway and the highway-signing duty — **the public is never controlled by a banksman alone**.
- [ ] For **India**, the **state is resolved** (defers to `hse-india`) and a **literal `[GAP]`** is
  emitted for the state site-traffic obligation — **never a minted national form number**. Every
  citation traces to the KB (**CDM 2015 Reg 27 + Schedule 3** + HSG144 for UK; **29 CFR 1926
  Subpart O** for US). De-id holds — the TMP is **site/route-level and carries no named
  individual**; any named driver / operative / banksman from the inputs is scrubbed.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The plan with no incident/emergency leg (canary S1)** — no route for emergency-vehicle
  access, no response to a vehicle-pedestrian strike, no breakdown/spill contingency on the
  circulation routes.
- **The public/adjacent interface assessed as a separate leg (canary S7)** — the live-highway,
  the public footway, and the site egress assessed as one system (wheel-wash, sight lines,
  emerging-vehicle warning), not a plan that stops at the hoarding line.
- **The quantitative basis asserted by silence (canary S5)** — speed limits, turning-circle
  radii, delivery volumes/peak vehicle movements and sight-line distances recorded or `[GAP]`'d,
  never a bare "keep speeds low".
- **The high-conflict point with no interim bridge (canary S2)** — a conflict point that cannot
  yet be segregated by design carries an interim measure and a dated action to close it, not an
  open banksman-only reliance with no bridge.

## Sign-off note
SME review: ran (persona: Construction Logistics / Temporary Works (Traffic) Coordinator); this is
decision-support that **precedes and never replaces** the human competent-person review, and it
**never** emits a competent-person approval claim on this traffic management plan. A FLAG it
raises is recorded, never merge-blocking.
