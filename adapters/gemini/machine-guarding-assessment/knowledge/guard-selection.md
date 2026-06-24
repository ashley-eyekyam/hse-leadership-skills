<!-- KB-SNIP-GUARD-SELECTION -->
# Machine guard/device selection logic (ISO 12100/14120 + OSHA 1910 Subpart O)

**Fragment ID:** `KB-SNIP-GUARD-SELECTION`
**This is prompt text, applied by the model — not a generator.** It is the guard /
protective-device **selection logic** for a machine-guarding assessment: fixed →
interlocked → presence-sensing → two-hand/hold-to-run → trip, governed by the
**access-frequency** rule. It is a **cited decision rule, not a calculation**. Consumed
by `machine-guarding-assessment` (MFG-01).

> Source: ISO 12100:2010 + ISO 14120:2015 (guard taxonomy) + OSHA 29 CFR 1910 Subpart O · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the guard/device selection order

For each machine danger zone, after Step 1 (design out the hazard — ISO 12100), select
the **highest-order** safeguarding measure the task allows:

1. **Fixed guard** — where access to the danger zone is **not** needed in normal
   operation (the preferred guard; no moving parts to defeat).
2. **Interlocked movable guard** — where regular access is needed; opening the guard
   removes the hazard (stops/isolates the machine).
3. **Presence-sensing device** (light curtains, mats) — where frequent access is needed
   and a physical guard would impede the task; sensing stops the dangerous motion.
4. **Two-hand / hold-to-run control** — where the operator's hands must be kept out of
   the danger zone during the hazardous motion.
5. **Trip device** — as a complementary measure for the residual hazard.

## The access-frequency rule
The **more frequent** the access needed in normal operation, the further down the list
the practical guard sits — but a higher-order **design-out** (ISO 12100 Step 1) is
always preferred over selecting a lower-order guard.

## Discipline
- Guarding is **engineering-control-led**; "operators to be careful / wear gloves" as a
  headline control is rejected (`KB-SNIP-HOC`).
- Ground the duty on `KB-REG-OSHA1910-O` (US) and the method on
  `KB-STD-ISO12100-14120`; a missing input (no access frequency) is a `[GAP]`.

## How the skill uses this fragment
`machine-guarding-assessment` references `KB-SNIP-GUARD-SELECTION` to choose the guard
type per danger zone against the access-frequency rule, then records the residual risk
and the named owner/date for any guard install.
