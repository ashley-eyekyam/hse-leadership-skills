<!-- KB-SNIP-DEENERGIZE-FIRST -->
# De-energize first — the electrically-safe-work-condition (ESWC) control spine

**Fragment ID:** `KB-SNIP-DEENERGIZE-FIRST`
**This is prompt text, applied by the model — not a generator.** It is the
electrical control-hierarchy spine for `hse-utilities-power`: **establish an
electrically safe work condition (ESWC) — de-energize and verify — before any
reliance on arc-rated PPE or approach controls.** A utilities artifact that
"controls" an energized task with a flash suit and a glove rating alone, with no
recorded de-energization decision, is exactly the indefensible paperwork this
spine rejects.

> Source: NFPA 70E Article 120 (ESWC) + OSHA 1910.269(m)/1910.333 + EAWR regs 13–14 — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the de-energize-first decision order

1. **Eliminate / de-energize (primary).** Plan the task to be done **dead**.
   Establish an ESWC: identify all sources, isolate, lock/tag, test for absence of
   voltage, apply protective grounding/earthing where required. Record the
   de-energization decision.
2. **Substitute / engineer.** Where some energized condition is unavoidable, reduce
   exposure by remote operation, barriers, insulated tooling, and reducing the
   available incident energy (faster protection, current limiting).
3. **Administrative.** Permit-to-work, approach-boundary control, job briefing,
   competent-person authorization.
4. **PPE (residual only).** Arc-rated PPE selected against the **calculated**
   incident energy (`arcflash.py` engine → NFPA 70E band, `KB-STD-NFPA70E`), and
   shock PPE against the approach boundaries — never as the headline control.

## The gate (reject these)
- A treatment that jumps straight to PPE without an ESWC decision or a documented
  live-work justification → **reject** (PPE-led / convenience-led).
- An incident-energy figure that is narrated or estimated rather than computed by
  the engine → **reject**.
- A missing input (clearing time, electrode config, working distance) silently
  assumed → **reject**; emit `[GAP]`.

## How the skill uses this fragment
Every `hse-utilities-power` skill applies this spine so the artifact leads with the
de-energization decision; PPE and approach controls are the documented residual
last line, against the cited engine output. No skill restates the spine in its own
body (anti-drift).
