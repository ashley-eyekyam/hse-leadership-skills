# Methodology — BBS Program Designer (ABC + non-punitive cards + system-fix routing)

The domain method the `bbs-program-designer` skill applies. It designs a **non-punitive
behaviour-based-safety program** grounded in **ABC (antecedent–behaviour–consequence)
analysis** (`KB-SNIP-BBS-METHOD`), with **defined metrics** (`KB-DATA-BBS-METRICS`) and
at-risk behaviours trended to **systemic** causes and routed to the deterministic A7
`controls` engine. It maps to **ISO 45001 clause 5.4** (worker participation) via
`KB-SNIP-LEADERSHIP-CLAUSE-MAP`. Control selection is deterministic (the A7 `controls`
engine), never prose judgement.

## Principle 1 — Non-punitive by design (the core constraint)

A BBS observation card is **role-labelled or anonymous**, **voluntary**, and its data is
used for **trending and learning, never individual sanction**. **No card ever records a
nameable individual for discipline** — that is a `de_identification` hard-fail. The
program observes the **work and the behaviour**, not the worker as a culprit. If a card
design names individuals or feeds a disciplinary process, it is a defect the Critic/QA
and SME passes must reject.

## Principle 2 — Observable, site-specific behaviours (never "work safely")

Every card item must be **observable and countable**, tied to a named task/area
("three points of contact on the rack ladder", "hands clear of the pinch point"). A
**non-observable slogan** ("work safely", "be careful") cannot be observed, counted, or
trended — it is **refused** at the card-design step; record `[GAP]` and elicit the
observable behaviour. This is the specificity lever for this skill.

## Principle 3 — ABC analysis (design the consequence)

For each target behaviour, map (`KB-SNIP-BBS-METHOD`):

| Element | What it is | Discipline |
|---|---|---|
| **Antecedent** | the real trigger/cue/condition | identify the real trigger, not a slogan |
| **Behaviour** | the observable, site-specific act | must be observable — never "work safely" |
| **Consequence** | what follows and reinforces it | the strongest driver; soon/certain/positive dominate |

**Design principle:** engineer the system so the **safe** behaviour carries the
**soon / certain / positive** consequence. An at-risk behaviour is a signal of a
**system gap**, not a bad worker.

## Principle 4 — At-risk behaviours route to SYSTEM fixes (the hierarchy lever)

Apply `KB-SNIP-HOC` to every trended at-risk category and call `controls.rank_controls`
+ `controls.validate_treatment`: route it to a **hierarchy-ranked system fix**
(eliminate / substitute / engineer / administrate before PPE). **Never "retrain the
worker", "be more careful", or discipline** as the response to a trended at-risk
category — a treatment whose only response is retraining or sanction is a defect the
Critic/QA and SME passes must flag and push up to a system fix. This is the hard
enforcement of the core value.

## Principle 5 — Defined metrics + small-cell confidentiality

From `KB-DATA-BBS-METRICS`:
- **percent-safe** = (safe ÷ total observations) × 100
- **participation** = (active observers ÷ trained pool) × 100
- **trend by behaviour category** — **never by person**

Apply the **`<5` small-cell suppression** to any team breakdown: a percent-safe for a
**4-person crew is suppressed**; apply **secondary suppression** so a suppressed cell
cannot be back-calculated from totals. Metrics measure the **system**, not individuals.

## The method loop

1. **De-identify first** — scrub any input cards/logs to role/group labels; no
   individual recorded for discipline; suppress `<5` cells (Principle 1/5). Everything
   downstream consumes scrubbed text.
2. **ABC-map each target behaviour** (Principle 3) — antecedent, observable behaviour,
   consequence; design the consequence for the safe behaviour.
3. **Design the observation card** (Principles 1–2) — observable, site-specific items;
   role-labelled/anonymous; voluntary; trending-and-learning use.
4. **Define the metrics** (Principle 5) — percent-safe / participation /
   trend-by-category from `KB-DATA-BBS-METRICS`, with `<5` suppression.
5. **Route at-risk categories to system fixes** — `KB-SNIP-HOC` +
   `controls.rank_controls` + `controls.validate_treatment` (Principle 4); never
   retrain-the-worker.
6. **Trend to systemic causes** — aggregate by behaviour category, identify the
   recurring systemic driver, and produce owned/dated SMART actions
   (`smart_actions.validate_register`: named role-label owner + ISO due date + measure).
7. **Close the observer-feedback loop** — two-way, immediate feedback; learning fed back
   to observers and the workforce.
8. **Validate** against `QUALITY_CHECKLIST.md`.
9. **Assemble** the branded report (`assets/report.json`).

## Citations

ABC / behaviour-based safety method (DuPont STOP, Krause/BST peer-observation as
exemplars) · `KB-SNIP-BBS-METHOD` · `KB-DATA-BBS-METRICS` · ISO 45001:2018 clause 5.4
(worker participation) via `KB-SNIP-LEADERSHIP-CLAUSE-MAP` · the jurisdiction's
worker-consultation duty (UK Safety Representatives / Consultation Regs; US OSH Act /
VPP employee involvement; EU OSH Framework Directive 89/391/EEC; India safety-committee
participation via `hse-india`). Cite the method as method, not law; never invent a
standard reference.
