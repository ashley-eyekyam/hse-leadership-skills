<!-- KB-SNIP-FATIGUE-FRMS -->
# Fatigue risk management — schedule-redesign-first control spine

**Fragment ID:** `KB-SNIP-FATIGUE-FRMS`
**This is prompt text, applied by the model — not a generator.** It is the
control-hierarchy spine for `driver-fatigue-management` (LOG-01): **manage fatigue
by redesigning the schedule/roster and the operating system first** — a
driver-alertness rule or an in-cab alertness gadget is **never** the primary
control. A fatigue artifact that "controls" long hours with a dashcam warning and
a "stay alert" toolbox talk, with no roster/schedule change, is the indefensible
paperwork this spine rejects.

> Source: FMCSA Hours-of-Service 49 CFR Part 395 + EU Reg 561/2006 + NAFMP FRMS framework — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the fatigue control order

1. **Eliminate / redesign (primary).** Redesign the schedule, roster, route and
   journey plan to keep duty/driving within the hours-of-service limits and avoid
   night/WOCL exposure where reasonably practicable. Compliance is computed by the
   `fatigue.py` engine (FMCSA + EU 561), never narrated.
2. **Substitute / engineer.** Relief drivers, journey-management changes, depot
   placement, vehicle ergonomics that reduce fatigue load.
3. **Administrative.** FRMS policy, fitness-for-duty + OSA screening pathway,
   fatigue-reporting culture, training, scheduled rest discipline.
4. **PPE / device (residual only).** In-cab alertness monitoring supplements,
   never replaces, the schedule/roster controls — it is the headline of nothing.

## The gate (reject these)
- A treatment that leads with "driver alertness rule" / in-cab gadget / "stay
  alert" briefing instead of a schedule/roster change → **reject** (admin/PPE-led).
- An hours-of-service compliance claim narrated rather than computed by
  `fatigue.py` → **reject**.
- A multi-day cycle (60/70h, 34h restart) or cross-shift rest claim made without
  the cumulative duty log → **reject**; emit `[GAP]` (single-shift logs default
  the cycle/restart flags to compliant — never assert multi-day compliance).
- Fatigue-event detail that identifies a driver → **reject**; de-identify first.

## How the skill uses this fragment
LOG-01 ranks every fatigue control through this order, computes compliance with
the engine, and rejects an alertness-device-led or briefing-led treatment.
