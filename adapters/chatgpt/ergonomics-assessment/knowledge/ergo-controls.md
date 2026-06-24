<!-- KB-SNIP-ERGO-CONTROLS -->
# MSD control hierarchy — eliminate → engineer → admin → training last

**Fragment ID:** `KB-SNIP-ERGO-CONTROLS`
**This is prompt text, applied by the model — not a generator.** It is the
musculoskeletal-disorder (MSD) control hierarchy for an ergonomics assessment, with the
discipline that **"training is not a control for biomechanical overload."** The
RULA/REBA/NIOSH **scores** come from the `ergonomics.py` engine (D-02), not from here —
this fragment ranks the **controls** once a risk is scored. Consumed by
`ergonomics-assessment` (MFG-02).

> Source: ISO 11228 series + the hierarchy of controls (work-design-first) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the MSD control hierarchy

Once the task's MSD risk is scored by the engine, rank controls **in this order** — a
treatment that stops at "manual-handling training" for a biomechanical overload is
flagged and pushed up:

1. **Eliminate the handling** — design out the manual handling (delivery to point of
   use, gravity feed, no double-handling).
2. **Engineer the workstation / provide an aid / mechanise** — adjust working heights
   and reaches, provide a lifting aid / hoist / conveyor / manipulator, reduce load
   mass and frequency.
3. **Administrative controls** — job rotation, rest breaks, load limits, two-person
   handling **as a reduction, not a fix**.
4. **Training — LAST** — safe-handling technique training supports the above; it is
   **not** a control for biomechanical overload on its own.

## Discipline
- Work-design controls sit **above** behaviour change; "train the worker to lift
  correctly" is never the headline control for an over-threshold task.
- The action bands that decide *whether* a control is required come from the engine via
  `KB-STD-ISO11228`; this fragment decides *which* control.
- Every control is owned/dated (`smart_actions`); a missing input is a `[GAP]`.

## How the skill uses this fragment
`ergonomics-assessment` scores the task with `ergonomics.py`, then references
`KB-SNIP-ERGO-CONTROLS` to rank the residual controls work-design-first, recording the
named owner and date for each redesign/aid.
