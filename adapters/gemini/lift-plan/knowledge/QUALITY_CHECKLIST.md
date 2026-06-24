# Pre-output Quality Checklist — lift-plan

Before producing any output, validate the draft against this gate. A failure is a defect to fix,
not a note to ship.

## The confirmed-input GATE (refuse-on-vague)
- [ ] The **load weight including rigging** is **confirmed** (Q2) — not assumed; an unconfirmed
  weight is a `[GAP]` and a **stop**.
- [ ] The **equipment SWL at the working radius** is **confirmed** (Q3) from the chart.
- [ ] A **named appointed person** is present for a **standard / complex** lift; no plan ships on
  an unconfirmed weight, an unknown SWL, or a "should-be-fine" ground.

## SWL read-not-computed
- [ ] **SWL-at-radius and utilisation are TRANSCRIBED from the manufacturer's rated-capacity
  chart** and presented as `<value> (<chart, year>)` — **no value is computed by the skill**
  (no lifting calculator).
- [ ] Utilisation is **checked against the `KB-DATA-LIFT-CATEGORIES` test**; over the safe margin
  → **equipment re-selection is flagged** (not proceeded past).

## Categorisation & method
- [ ] The lift is **classified** basic / standard / complex by the **highest triggered BS 7121
  criterion**; a complex / tandem / blind lift carries an **appointed-person WRITTEN plan +
  contingency / abort criteria**.
- [ ] The method is **sequenced** (rig → trial-lift / weigh → travel → slew → place → de-rig)
  with **named roles** (appointed person, operator, slinger / signaller + competence basis),
  **weather / wind limits**, and **abort criteria**.

## Hierarchy of controls (the core value)
- [ ] Every proximity / ground hazard is **HoC-ranked**; an **overhead-line hazard leads with
  elimination / engineered exclusion** — **no un-justified PPE-only ("operatives to take care")
  overhead-line control** ships.
- [ ] **Exclusion zones / segregation** are set from the proximity tests (GS6 clearance, swing
  radius, drop zone); the ground / outrigger bearing is assessed.
- [ ] Residual risk is **re-scored via the A7 `risk_matrix` engine** after controls; a residual
  High / Critical flags additional controls or a hold-point.

## Defensibility & citation
- [ ] Every action carries a **named owner + an ISO due date + a hazard link** (no anonymous
  actions, no "ASAP").
- [ ] Every citation traces to the KB — **LOLER Reg 8 / BS 7121** (UK), **29 CFR 1926 Subpart
  CC** (US); for **India** the **state is resolved** (defers to `hse-india`) and a **literal
  `[GAP]`** is emitted, **never a national form number**.

## De-identification
- [ ] De-id pass complete **BEFORE drafting**; the **appointed person / operator / slinger stay
  named** (legitimate competence record) while **no medical-fitness / health detail and no
  incident-derived name** is circulated; no embedded re-id key; no unsuppressed `<5` injury cell.

## SME boundary
- [ ] The output **never** claims "approved by a competent person" — it is decision-support that
  precedes the human competent-person review.
