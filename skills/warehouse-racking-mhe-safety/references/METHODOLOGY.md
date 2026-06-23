# Methodology — warehouse-racking-mhe-safety

The domain method LOG-02 applies. It produces a defensible racking + MHE/pedestrian-segregation
artifact whose **primary controls are design- and engineering-led** and whose remedial actions follow
the **correct SEMA escalation**. Run it AFTER the de-identification scrub and the structured intake
(`references/intake.md`).

## 1. Resolve the installation + the SWL (the integrity-of-advice anchor)

Capture the named site, the racking installation, the rack type, and the bay/beam configuration
(intake Q1–Q2). Resolve the **displayed SWL load notices** against the rack-design drawing. A
site-specific SWL, tolerance, or bay configuration that is **not supplied is a literal `[GAP]`** with a
request for the SWL load notice / rack-design drawing — **never an invented rating** (threat
T-16-09-02: an assumed SWL is integrity-of-advice tampering). Configuration is not changed without
recalculation.

## 2. Resolve the EN 15635 inspection regime (`KB-STD-EN15635-SEMA`)

Establish the **PRRS** (Person Responsible for Racking Safety) appointment and the inspection cadence —
the **weekly visual** inspection and the **≥12-monthly expert** inspection (6-monthly for high-traffic
/ 24-7 sites). An unappointed PRRS or an absent expert inspection is a **high-priority finding**.

## 3. Classify damage on the SEMA RAG band and ground the matching action

For every damage finding, classify on the **SEMA Red/Amber/Green** band and ground the matching
remedial action — the band is a *damage/severity classification*, not a replacement for the 5×5
residual score:

| Band | Meaning | Action |
|---|---|---|
| **Green** | Within tolerance | Log and continue to monitor at the routine interval |
| **Amber** | Exceeds tolerance | Repair/replace within 4 weeks; **auto-escalate to Red** if not actioned (the off-load nuance — whether Amber also needs immediate off-load — is confirmed by the SEMA-approved inspector for the site, A5/Open-Q1) |
| **Red** | Critical | **Immediately off-load and isolate** the affected run; repair before reuse |

**A Red-band finding is never down-rated to "monitor".** Damage at an unstated tolerance is a `[GAP]`.

## 4. Rank every control through the SWL-design + segregation-first spine (`KB-SNIP-RACKING-MHE`)

Run the `controls` engine over each racking/MHE hazard in this order:

1. **Eliminate / design (primary)** — correct SWL-rated configuration, column/upright protection, load-
   notice display; layout that designs out pedestrian-vehicle conflict (segregated/one-way routes,
   barriers, protected walkways/crossings).
2. **Substitute / engineer** — engineered guards, rack-end protectors, speed controls, automated/
   segregated MHE flows.
3. **Administrative** — the PRRS appointment + inspection regime, operator competence/evaluation
   (`KB-REG-MHE-PIT`, OSHA 1910.178(l) / PUWER / L117), the damage-reporting route, the SEMA RAG
   remedial priority.
4. **PPE (residual only)** — hi-vis, hard hats — supplement engineered segregation, never replace it.

A racking/MHE control left as **hi-vis / "inspect carefully" / "look out for forklifts" only** is a
**FLAG pushed up the hierarchy — never the headline control** (threat T-16-09-03).

## 5. MHE / pedestrian segregation by engineered design (`KB-REG-MHE-PIT`)

Pedestrian-vehicle separation is achieved **by design first** — physical barriers, segregated/one-way
routes, marked and protected walkways and crossing points — **before** any reliance on hi-vis,
signage, or "look out for forklifts." Evidence operator competence/evaluation and the pre-use
inspection regime. Resolve jurisdiction (US 1910.178 / UK PUWER+L117 / India MTW via `hse-india`).

## 6. Re-score the residual, assign owned/dated actions

Re-score the residual on the deterministic `risk_matrix` 5×5 engine after controls. Assign every
remedial action and every `[GAP]`-closure via `smart_actions` with a **named role owner + ISO due
date + measure** — no "TBD".

## 7. India deferral (CONV-8) + de-identification

For an India site, resolve the state via `hse-india` (**mandatory state detection**, `KB-REG-IN-MTW`)
and emit a literal `[GAP]` where a state form/return is owed — never a minted national form number.
Any **prior struck-by / rack-collapse incident** is de-identified to role labels with `<5` cells
suppressed (lower de-id tier — asset/site data dominates — but a named injured worker is never
circulated). Validate against `references/QUALITY_CHECKLIST.md` before producing the output.
