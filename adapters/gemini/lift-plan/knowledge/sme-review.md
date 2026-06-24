---
sme-review:
  personas:
    - role: "Appointed Person (BS 7121 / LOLER Reg 8)"
      expertise: "Lift planning and supervision under LOLER 1998 Reg 8 + BS 7121, lift categorisation (basic/standard/complex), confirmation of load weight and SWL-at-radius from the manufacturer's rated-capacity chart, exclusion-zone and segregation method, and the contingency / abort criteria a complex lift requires."
      lens: "would this lift plan stand up before the lift and to a regulator — the lift correctly categorised (the highest triggered BS 7121 criterion), the load weight (incl. rigging), the SWL-at-radius, and a named appointed person CONFIRMED (never assumed), the SWL / utilisation TRANSCRIBED-AND-CITED from the chart (never computed), and an appointed-person WRITTEN plan with contingency / abort for a complex lift"
    - role: "Lifting Operations Specialist (rigging & proximity)"
      expertise: "Rigging configuration and lifting-accessory selection, utilisation margins, ground / outrigger bearing, overhead-line clearance (GS6) and proximity exclusion zones, in-service wind limits, and the sequenced safe lift method (rig → trial-lift / weigh → travel → slew → place → de-rig)."
      lens: "is the lift physically safe and the proximity controlled — utilisation within the planned safe margin (re-select the crane if over), the overhead-line / proximity hazard led by ELIMINATION or an ENGINEERED EXCLUSION (a PPE-only 'operatives to take care' overhead-line control is the prevented downgrade), the ground / outrigger loads assessed, and the method sequenced with weather limits and named stop conditions"
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

## Sign-off note
SME review: ran (personas: Appointed Person + Lifting Operations Specialist); this is
decision-support that **precedes and never replaces** the human competent-person review, and it
**never** emits a competent-person approval claim on this safety-critical lift plan. A FLAG it
raises is recorded, never merge-blocking.
