---
sme-review:
  personas:
    - role: "Appointed Person (BS 7121 / LOLER Reg 8)"
      expertise: "Lift planning and supervision under LOLER 1998 Reg 8 + BS 7121, lift categorisation (basic/standard/complex), confirmation of load weight and SWL-at-radius from the manufacturer's rated-capacity chart, exclusion-zone and segregation method, and the contingency / abort criteria a complex lift requires."
      lens: "would this lift plan stand up before the lift and to a regulator — the lift correctly categorised (the highest triggered BS 7121 criterion), the load weight (incl. rigging), the SWL-at-radius, and a named appointed person CONFIRMED (never assumed), the SWL / utilisation TRANSCRIBED-AND-CITED from the chart (never computed), and an appointed-person WRITTEN plan with contingency / abort for a complex lift"
    - role: "Lifting Operations Specialist (rigging & proximity)"
      expertise: "Rigging configuration and lifting-accessory selection, utilisation margins, ground / outrigger bearing, overhead-line clearance (GS6) and proximity exclusion zones, in-service wind limits, and the sequenced safe lift method (rig → trial-lift / weigh → travel → slew → place → de-rig)."
      lens: "is the lift physically safe and the proximity controlled — utilisation within the planned safe margin (re-select the crane if over), the overhead-line / proximity hazard led by ELIMINATION or an ENGINEERED EXCLUSION (a PPE-only 'operatives to take care' overhead-line control is the prevented downgrade), the ground / outrigger loads assessed, and the method sequenced with weather limits and named stop conditions"
modes:
  lift-plan:
    detected_by: "Q1 — Output type (the appointed-person lift plan for the named lifting operation)"
    floor:
      - id: lift-classified-bs7121
        description: "The lift is classified basic/standard/complex against the highest triggered BS 7121 criterion; a complex/tandem/blind lift carries an appointed-person WRITTEN plan + contingency/abort (KB-DATA-LIFT-CATEGORIES)"
        anchors: ['BS ?7121', 'lift classif', 'basic . standard . complex']
        min_matches: 1
      - id: lift-gate-confirmed-weight-ap
        description: "The GATE holds — a CONFIRMED load weight (incl. rigging), the equipment SWL at working radius, and a named appointed person; the plan refuses to proceed on an unconfirmed weight or unknown SWL"
        anchors: ['confirmed.{0,24}weight|weight.{0,24}confirmed', 'appointed person']
        min_matches: 1
      - id: lift-swl-transcribed-not-computed
        description: "SWL-at-radius and utilisation are TRANSCRIBED-AND-CITED from the manufacturer's rated-capacity chart and checked against the utilisation test — never computed; over-margin flags crane re-selection"
        anchors: ['rated.capacity chart', 'utilisation', 'not computed']
        min_matches: 1
      - id: lift-proximity-hoc-overhead-line
        description: "Every proximity hazard is hierarchy-ranked; an overhead-line hazard leads with elimination/re-routing/an engineered exclusion zone (goal-posts, banksman) — a 'take care/PPE' overhead-line control is pushed up the hierarchy (KB-SNIP-HOC)"
        anchors: ['overhead.line', 'exclusion zone', 'GS6']
        min_matches: 1
      - id: lift-sequenced-method-roles
        description: "The method is sequenced (rig -> trial-lift/weigh -> travel/slew -> place -> de-rig) with named roles (appointed person, operator, slinger/signaller) and their competence basis"
        anchors: ['trial.lift', 'slinger', 'sequenced']
        min_matches: 1
      - id: lift-contingency-abort-weather
        description: "Contingency/abort criteria (loss of communication, wind exceedance, unplanned obstruction) and the chart's in-service wind limit are stated (KB-REG-LOLER-BS7121)"
        anchors: ['abort', 'contingency', 'in.service wind']
        min_matches: 1
      - id: lift-residual-rescored-owned
        description: "Residual risk is re-scored via risk_matrix after controls; a residual High/Critical flags a hold-point (do-not-lift); actions carry named owners + dates"
        anchors: ['residual risk', 'risk.matrix', 'hold.point']
        min_matches: 1
---

# SME Review & Sign-off — lift-plan

Two lifting-duty lenses review the lift plan before any output: the **Appointed Person** (the
LOLER Reg 8 / BS 7121 plan-and-supervise view) and the **Lifting Operations Specialist** (the
rigging-and-proximity view). They apply the universal hard gates (no error or unsupported
claim, every regulatory trigger caught, no lower-order-only control without justification,
zero de-identification leak) plus the domain checklist below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The lift is **classified** basic / standard / complex against the **highest triggered BS
  7121 criterion** (`KB-DATA-LIFT-CATEGORIES`); a **complex / tandem / blind** lift carries an
  **appointed-person WRITTEN plan + contingency / abort criteria + supervision**.
- [ ] The **GATE held**: a **confirmed load weight (incl. rigging)**, the **equipment SWL at the
  working radius**, and a **named appointed person** (standard / complex) are present — the plan
  **refused to proceed on an unconfirmed weight, an unknown SWL, or a "should-be-fine" ground**.
- [ ] **SWL-at-radius and utilisation are TRANSCRIBED-AND-CITED from the manufacturer's
  rated-capacity chart** (`<value> (<chart, year>)`) and checked against the
  `KB-DATA-LIFT-CATEGORIES` utilisation test — **never computed** (no lifting calculator);
  utilisation over the safe margin **flags re-selection of the equipment**.
- [ ] Every proximity hazard is **hierarchy-ranked**; an **overhead-line hazard leads with
  ELIMINATION / re-routing / an ENGINEERED EXCLUSION zone (goal-posts, banksman)** — a
  **"operatives to take care / wear PPE" overhead-line control is flagged PPE-only and pushed
  up the hierarchy**, never the headline. Exclusion zones / segregation are set from the
  proximity tests; residual risk is re-scored on `risk_matrix`.
- [ ] The method is **sequenced** with **named roles** (appointed person, operator, slinger /
  signaller — each with the competence basis), **weather / wind limits** (the chart's in-service
  wind speed), and **contingency / abort criteria** (loss of communication, wind exceedance, an
  unplanned obstruction).
- [ ] For **India**, the **state is resolved** (defers to `hse-india`) and a **literal `[GAP]`**
  is emitted for the state crane-rules form — **never a minted national form number**. Every
  citation traces to the KB (LOLER Reg 8 / BS 7121 for UK; 29 CFR 1926 Subpart CC for US); de-id
  holds — the **appointed person / operator / slinger stay named** as a legitimate competence
  record while **no medical-fitness / health detail** is circulated.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The lift plan with no abort/emergency leg (canary S1)** — a sequenced method with no
  contingency/abort criteria, no dropped-load or entrapment response, and no rescue for a person
  in the exclusion zone. A lift plan that cannot say when to STOP is hollow.
- **The high residual with no hold-point bridge (canary S2)** — a residual High/Critical lift
  with a far action date and no do-not-lift hold-point or interim measure for the gap period.
- **The quantitative basis asserted by silence (canary S5)** — the SWL-at-radius, utilisation %,
  in-service wind limit and outrigger/ground bearing recorded and CITED to the chart/report, or
  `[GAP]`'d — never a bare number with no source.
- **The two legs that never meet (canary S7)** — SIMOPS between the lift and adjacent work /
  occupied areas / other cranes assessed as one system (shared drop zones, slew-radius overlap),
  not a lift plan that ignores what else is live on site.

## Sign-off note
SME review: ran (personas: Appointed Person + Lifting Operations Specialist); this is
decision-support that **precedes and never replaces** the human competent-person review, and it
**never** emits a competent-person approval claim on this safety-critical lift plan. A FLAG it
raises is recorded, never merge-blocking.
