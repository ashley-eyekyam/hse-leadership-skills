# Methodology — synthesis-to-narrative for a board safety report

This skill's domain method is **synthesis into insight**, grounded in ISO 45001
clause **9.1** (monitoring, measurement, analysis & performance evaluation — where the
indicators come from) and clause **9.3** (management review — the leadership/board
structure the narrative serves). The board report is the artifact a management review
consumes. The load-bearing discipline is **exec narrative, not data dump**: a figure
with no narrative reading is incomplete; a report that is only tables is a defect.

## The leading & lagging indicator taxonomy

- **Lagging** (outcome — what already happened): recordable injuries, lost-time
  injuries, DART cases, fatalities, environmental events. The rates (TRIR / DART /
  LTIFR) are computed **deterministically** by `incident_rates.compute_all` — never in
  prose — and **only when hours + counts were captured** (else a pre-computed rate is
  taken as input, or the figure is `[GAP]`; a denominator is never fabricated).
- **Leading** (predictive — what shapes the next outcome): training completion %,
  audit / inspection closure rate, near-miss reporting rate, corrective-action on-time
  closure, leadership safety tours. These are **user-supplied** structured figures —
  there is no A7 engine for them; they are *synthesized* (judgement), not computed.

A recommended leading-indicator set (a soft guide, not a fixed enum — leading
indicators vary by org maturity): training-completion %, audit/inspection closure %,
near-miss reporting rate (per 100 workers or per period), CAPA on-time closure %, and
leadership safety-tour count. Accept any user-supplied leading metric as free-text.

## Trends & benchmarks (every figure carries a reading; every benchmark a source + year)

For each indicator, compute the **movement vs the prior period** and the **position vs
the benchmark** (`incident_rates.benchmark_delta`), reading the benchmark from
`KB-DATA-TRIR-BENCHMARKS` (or a user-supplied figure) **with its publishing body +
year + sector** — never a bare number, never an unsourced "industry average". The
output of this step is *readings* ("LTIFR fell 18% vs FY24 and now sits below the
[BLS SOII, 2023] sector average"), which become the narrative.

## The HiPo / SIF lens (D-01 — the one override this skill adds)

A board narrative must surface, **explicitly and interpreted**, two predictive lenses
that a lagging-rate table hides:

- **HiPo (High-Potential incident)** — an event (often a near-miss) whose *realistic
  worst credible outcome* was serious or fatal, regardless of the actual (often
  trivial) outcome. HiPo counts reveal where the organisation is *exposed* before the
  outcome arrives.
- **SIF precursor (Serious-Injury-or-Fatality precursor)** — the conditions and
  activities empirically correlated with fatal/life-altering outcomes (e.g. work at
  height without edge protection, energised work, line-of-fire, confined space). SIF
  precursor frequency is a leading signal that the *next* serious event is being set up.

**Interpret, do not list.** The board does not need an enumerated incident log; it
needs the *reading*: what the HiPo/SIF pattern reveals about exposure, which activity
or site is most likely to produce the next serious event, and what that implies for the
decisions the board must make. A bare list of HiPo events with no interpretation fails
this lens. The HiPo/SIF inputs are de-identified **and aggregated** (step 1) exactly
like the key-events field — the board-report leak vector is re-identification via a
vivid single-incident anecdote, so a single dramatic SIF event is rolled up, never
narrated with a date + location + injury detail.

This lens is prompt-side only — it adds **no new engine** and computes no new rate; it
reframes the existing aggregated event data and the `incident_rates` output into an
exposure-and-decision reading for the board.

## The narrative (insight → decision)

Turn the readings into: **what changed** (the trend story) → **why it matters** (the
risk/exposure/cultural implication, including the HiPo/SIF reading) → **what leadership
must decide** (the explicit governance-level asks — resource, policy, accountability —
tied to ISO 45001 9.3 management-review outputs). The indicator tables are supporting
evidence *behind* the narrative, never the deliverable.

## Optional environmental-performance line (D-02 — NOT a full ESG branch)

When the user supplies environmental metrics (intake Q9 = Yes), add a **single**
environmental-performance line grounded in ISO 14001 clause **9.1.2** (evaluation of
compliance). This is one optional line in a safety-led board paper — it is **not** a
full E/ESG board-report branch (that is out of v1.0 scope).

## De-identification + aggregation (the discipline, not a separate engine)

The `deid` block runs first and is inherited verbatim (A5). B9's twist is
**aggregation**: because a board report rolls up a whole period, the bar is that **no
individual incident, injured party, or <5 cell is identifiable** — pseudonymization
alone is insufficient when a single fatality at a named small site in a stated month
re-identifies through quasi-identifiers. The re-identification key never enters the
report. The aggregation discipline + the Critic/QA pass + the competent-person review
are the backstop above the auto-fail regex floor.
