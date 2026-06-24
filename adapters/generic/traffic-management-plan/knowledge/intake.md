---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-EVIDENCE: "A traffic management plan is built from the site layout / access drawing and the delivery profile (Q1/Q3/Q4), not from an evidence register of prior records — so a dedicated evidence-held question is not asked at intake; any site drawing or prior TMP the user offers is ingested as the Q1 layout source."
    ELI-SCORING: "The plan ranks each conflict point on the segregation-by-design hierarchy (KB-SNIP-TRAFFIC-SEGREGATION) and, where a residual conflict needs validating, the controls engine flags a 'hi-vis + banksman only' treatment — there is NO traffic-flow / risk-scoring calculator and no org risk matrix to size at intake, so a matrix-size question is not asked."
    ELI-COMPETENCY: "The TMP is a site/route-level document and carries NO named individual (the De-identifier scrubs any named driver / operative / banksman) — so an individual competence-card question is not asked at intake; the banksman / traffic-marshal requirement is set at role level as a LAST-resort residual control, not a named-person record."
  branches:
    - {when: Q4, option: continuous, activates_output_section: reversing-elimination-one-way-turning, mandatory: true}
    - {when: Q5, option: live highway, activates_output_section: public-highway-interface, mandatory: true}
    - {when: Q6, option: UK, activates_kb_row: KB-REG-CDM2015, activates_output_section: reg27-schedule3-basis, mandatory: false}
    - {when: Q6, option: USA, activates_kb_row: KB-REG-OSHA1926, activates_output_section: osha-1926-basis, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: india-state-gap, mandatory: true}
---

# Structured intake — traffic-management-plan

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where the
answer space is enumerable and free-text where it is open; branch on the answers; **echo the
captured facts back for confirmation before any analysis**.

**The GATE (refuse-on-vague):** **no traffic management plan is produced** until both **a named
site with its access points (Q1)** and **at least the vehicle and pedestrian types that
interface (Q2)** are captured. The skill **refuses to plan on a generic site, an unnamed access
point, or "the site roads"** — ask again, or record `[ASSUMPTION]` / `[GAP]`; **never invent a
layout, a route, an access point, or a conflict point.** **Uncontrolled reversing with no Reg 27 /
Schedule 3 grounding is a citation + specificity failure** — name the routes, do not produce a
generic plan.

**Jurisdiction paths:** the **UK → CDM 2015 Reg 27 / Schedule 3 branch** (Q6 = UK →
`cdm-2015.md` + HSE HSG144; non-mandatory) and the **mandatory India → state branch** (Q6 = India
→ Q6a + `KB-REG-IN-STATEFORMS`, **defers to `hse-india`, mandatory state detection, literal
`[GAP]`, never a minted national form number**). The **reversing branch** (Q4 = continuous /
ad-hoc reversing → the reversing-elimination / one-way & turning section is mandatory for a
continuous profile) and the **highway branch** (Q5 = live highway → the public / highway interface
section is mandatory) tune the plan.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Site & layout (the specificity anchor)** | free-text | "Name the **site** and describe the **layout & access points**: the site name / address, the vehicle access(es) and pedestrian access(es), the work areas, the welfare / cabin locations, and any fixed constraints (gradient, blind corner, narrow gate). e.g. 'Meadowbank Road site: north gate (HGV) + south gate (operatives), loading bay at the north-east corner, welfare cabins south, single 3.5 m gate at the north.'" — **refuse a generic site; an unnamed access point or 'the site roads' is a `[GAP]`, never invented** | ELI-SUBJECT / ELI-LOCATION | always |
| Q2 | **Traffic types (who & what interfaces)** | MCQ multi-select | HGV deliveries / Plant or MEWP / Forklift or telehandler / Light vehicles / Pedestrians or operatives / Public or highway — **at least one vehicle type AND pedestrians / operatives must be present for a plan to be produced** (the interface is the whole point) | ELI-EXPOSURE / ELI-INDUSTRY | always |
| Q3 | **Known conflict points** | free-text | "Where do vehicles and people conflict? — gates, loading / unloading bays, crossings, blind corners, shared routes, the welfare route. **Name them** (e.g. 'reversing HGVs at the north loading bay cross the operative route to the welfare cabins')." — names drive the segregation-by-design layout; a generic answer is a `[GAP]` | ELI-EXPOSURE / ELI-LOCATION | always |
| Q4 | **Delivery & reversing profile** | MCQ | Scheduled-banked (booked-in windows) / Ad-hoc / Continuous; reversing present → the plan PUSHES toward eliminating it via a one-way system, a turning circle, or a drive-through loading bay, with a banksman as the LAST resort, never the headline control (a continuous reversing profile makes the reversing-elimination / one-way & turning section mandatory) | ELI-BASELINE | always |
| Q5 | **Public & highway interface** | MCQ | None-enclosed / Footway adjacent / Live highway; this drives the public-protection & highway-signing section, and the public is never controlled by a banksman alone (a live-highway interface makes the public / highway interface section mandatory) | ELI-EXPOSURE / ELI-OBLIGATIONS | always |
| Q6 | **Jurisdiction** | MCQ | UK / USA / India / EU / Unknown — UK → CDM 2015 Reg 27 + Schedule 3 + HSG144; USA → 29 CFR 1926 Subpart O (+ 1926.601 / .602); India → Q6a + state site-traffic obligation via `hse-india`; Unknown → ask before citing | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; confirm the state before citing any obligation; emit a literal `[GAP]`, never a minted national form number** | ELI-JURIS | Q6 == India |
| Q7 | **Existing controls / arrangements** | free-text | "What is already in place — a one-way system, segregated pedestrian routes, barriers / edge protection, gated crossings, a site speed limit, signage, a delivery booking system, a banksman?" (seeds the baseline the plan improves) | ELI-BASELINE | always |
| Q8 | **Plan window & review trigger** | free-text | "Which construction phase / window does this TMP cover, and what triggers a re-plan / re-brief (a change of phase, access, traffic type, or delivery profile)?" | ELI-TEMPORAL | always |

*ELI-OUTPUT is fixed (the artifact is a Traffic Management Plan); ELI-OBLIGATIONS is set by Q5 / Q6 (the highway-signing duty + the jurisdiction's traffic-routes duty).*

**Branch map:** `continuous-reversing` (Q4 = continuous → the **mandatory** reversing-elimination /
one-way & turning section); `live-highway` (Q5 = live highway → the **mandatory** public / highway
interface section); `uk-cdm` (Q6 = UK → `cdm-2015.md` + the Reg 27 / Schedule 3 basis + HSG144;
non-mandatory); `us-osha` (Q6 = USA → `KB-REG-OSHA1926`; non-mandatory); `india-state` (Q6 = India
→ Q6a + `KB-REG-IN-STATEFORMS`, **mandatory** state detection, defers to `hse-india`).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before any
analysis: "Traffic management plan for the **Meadowbank Road** site: north gate (HGV deliveries,
**continuous reversing into the loading bay**) + south gate (operatives), conflict at the north
loading bay where reversing HGVs cross the welfare route, **footway adjacent** to the north
hoarding, UK / CDM 2015 Reg 27 + Schedule 3, re-plan on a change of phase or access — correct?"
Every conflict point is then ranked on the segregation-by-design hierarchy (reversing leads with
elimination; a 'hi-vis + banksman only' control is pushed up).

## Refuse-on-vague anchors

- **The GATE:** Q1 (a named site with its access points) and Q2 (at least one vehicle type AND
  pedestrians / operatives) are load-bearing — **refuse a generic site, an unnamed access point,
  or "the site roads"**; never invent a layout, a route, an access point, or a conflict point
  (record `[GAP]`).
- **Uncontrolled reversing is a citation + specificity failure** — name the routes and ground the
  reversing control in **CDM 2015 Reg 27 + Schedule 3** (routes suitable / sufficient / separated,
  warning of approach); a plan whose only pedestrian control is **"hi-vis and a banksman"** is
  PPE/admin-led and is pushed up the segregation-by-design hierarchy.
