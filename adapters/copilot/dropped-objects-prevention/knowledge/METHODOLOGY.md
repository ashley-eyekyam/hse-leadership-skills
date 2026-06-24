# Methodology — dropped-objects-prevention (MAR-02)

The domain method this skill applies: a **DROPS survey → dropped-object register → reliable-securing
controls → exclusion zones** workflow grounded in `KB-REG-DROPS` (DROPS Recommended Practice 2017 /
DROPS Reliable Securing / IADC HSE Guidelines Section 16 / API RP 2D & RP 54), ranked through
`KB-SNIP-DROPS-SECURING`, with consequence banding by the public `m·g·h` method
(`KB-DATA-DROPS-IMPACT`). Decision-support only; a competent person must review the output.

## 1. Survey the at-height inventory (per named area)

For the named installation/vessel and area (intake Q1–Q2), systematically survey the **fixed and
potential dropped objects** at height — derrick/mast, crane boom & pedestal, monkeyboard &
fingerboard, flare tip & boom, riser/wellhead deck, piping & small-bore fittings, lighting &
instruments. The survey is **installation- and area-specific**, never a generic checklist.

## 2. Classify each object — static vs dynamic (the taxonomy)

Every register entry is classified per `KB-REG-DROPS`:
- **Static dropped object** — falls from a static position (a loose fitting, light, bolt, or tool
  left at height).
- **Dynamic dropped object** — knocked, swung, or dropped during an operation (a lifted load, a
  swung tubular, a tool in use).

The taxonomy drives the control: static objects need **reliable securing**; dynamic objects need
**operational control + exclusion zones** in addition.

## 3. Record the existing securing & condition (the baseline)

For each at-height item, record the **primary fixing + secondary retention (tethering/lanyards)**
and its condition / last DROPS inspection (intake Q4). An at-height item with **no recorded
securing standard** is flagged immediately as a **high-priority finding** — never assume an item is
secured because it "looks secured".

## 4. Rank the control — reliable securing first (the core lever)

Run every control through `KB-SNIP-DROPS-SECURING` via the `controls` engine
(`controls.rank_controls` / `validate_treatment` — a deterministic call, never a narrated
judgment):
1. **Eliminate** — remove items from height; design out the source; do the task at ground level.
2. **Reliable securing (engineer)** — primary fixing + secondary retention to a reliable-securing
   standard; barriers/nets.
3. **Administrative** — DROPS survey + register, inspection regime, exclusion/red zones below
   at-height work, permit control.
4. **PPE (residual only)** — hard hats for persons who must be in the area; **supplement** the
   survey/securing/exclusion controls, **never replace** them.

A treatment that **leads with "hard hats below"** (`ppe_admin_only=True`) is **FLAGGED and pushed
up the hierarchy** — never the headline control. This is the failure mode the skill exists to
prevent.

## 5. Band the consequence — the public m·g·h method (licensed values cite-only)

For each banded object, compute the **public** impact energy `E ≈ m · g · h`
(`KB-DATA-DROPS-IMPACT`) with the **user-supplied** mass (kg) and fall height (m); `g = 9.81 m/s²`
is the public constant. Map the energy to a consequence band using **generic labels only**.

**Discipline (D-03 — licensed, cite-not-reproduce):**
- `mass` and `fall height` are **always user-supplied** — never invented → `[GAP]` where unsupplied.
- The **licensed DROPS Calculator consequence-band threshold VALUES are NOT reproduced**. The skill
  **records the user's band** (from their licensed Calculator), or reports the `m·g·h` energy with
  the band left **`[GAP]` / user-confirmed** (A1 `[ASSUMED]`, surfaced for the SME).
- A consequence band asserted with **hard-coded licensed thresholds is a D-03 violation — reject
  it.**

## 6. Re-score the residual + assign SMART actions

Re-score the residual risk on the `risk_matrix` 5×5 **after** reliable securing + exclusion zones.
Assign `smart_actions` — each with a **named role owner + ISO due date + measure**, including each
`[GAP]`-closure action (a missing securing standard, a missing mass/height, an unconfirmed band).

## 7. Validate + emit

Validate the draft against `references/QUALITY_CHECKLIST.md`, run the mandatory Critic/QA + SME
pass, then emit the branded report (DOCX + PDF) via the Output format section. The DROPS survey +
register feeds the offshore safety case (`offshore-safety-case`, MAR-01) — cross-referenced, never
rebuilt here.

## Evidence & assumptions

Every finding traces to its survey evidence (the at-height item, its securing status, the
user-supplied mass/height). Flag `[ASSUMPTION]` / `[GAP]` honestly — a missing mass/height is a
`[GAP]`, never an invented number; an unconfirmed licensed band stays `[GAP]` for the SME.
