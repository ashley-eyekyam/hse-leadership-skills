<!-- KB-SNIP-RACKING-MHE -->
# Warehouse racking & MHE — design/inspection/segregation-first control spine

**Fragment ID:** `KB-SNIP-RACKING-MHE`
**This is prompt text, applied by the model — not a generator.** It is the
control-hierarchy spine for `warehouse-racking-mhe-safety` (LOG-02): **control
racking and MHE risk by SWL-design, the inspection regime and engineered
pedestrian-vehicle segregation first** — "inspect carefully" and hi-vis are
**never** the primary control. A warehouse artifact that treats collapse/impact
risk with a hi-vis vest and a "be careful" briefing, with no engineered
segregation or inspection regime, is the indefensible paperwork this spine rejects.

> Source: BS EN 15635:2008 + SEMA Code of Practice + OSHA 1910.178 / PUWER 1998 / HSE L117 / HSG136 — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the racking/MHE control order

1. **Eliminate / design (primary).** Correct SWL-rated configuration, column/upright
   protection, load-notice display; layout that designs out pedestrian-vehicle
   conflict (segregated/one-way routes, barriers, protected walkways/crossings).
2. **Substitute / engineer.** Engineered guards, rack-end protectors, speed
   controls, automated/segregated MHE flows.
3. **Administrative.** PRRS appointment + inspection regime (weekly visual +
   ≥12-monthly expert), operator competence/evaluation, damage-reporting route,
   the SEMA RAG remedial-priority.
4. **PPE (residual only).** Hi-vis, hard hats — supplement engineered segregation,
   never replace it.

## SEMA RAG remedial priority (action, not a risk recalc)
- **Green** = within tolerance → log + monitor.
- **Amber** = exceeds tolerance → repair/replace within 4 weeks, auto-escalate to
  Red if not actioned.
- **Red** = critical → **immediate off-load + isolate** the run.

## The gate (reject these)
- A treatment that leads with "inspect carefully" / hi-vis / "look out for
  forklifts" instead of SWL-design + engineered segregation + inspection → **reject**.
- A Red-band damage finding without an immediate off-load action → **reject**.
- An assumed SWL/tolerance/inspection interval → **reject**; emit `[GAP]`.

## How the skill uses this fragment
LOG-02 ranks every racking/MHE control through this order and applies the SEMA RAG
action to any damage finding.
