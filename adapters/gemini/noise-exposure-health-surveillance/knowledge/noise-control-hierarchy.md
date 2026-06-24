<!-- KB-SNIP-NOISE-CONTROL-HIERARCHY -->
# Noise-control hierarchy — source → enclosure/damping → distance/time → HPD last

**Fragment ID:** `KB-SNIP-NOISE-CONTROL-HIERARCHY`
**This is prompt text, applied by the model — not a generator.** It is the
noise-control hierarchy for a noise-exposure / health-surveillance assessment, with the
discipline that **hearing protection is the last line, never the first or only
control.** Consumed by `noise-exposure-health-surveillance` (MFG-03).

> Source: OSHA 29 CFR 1910.95 + UK Control of Noise at Work Regulations 2005 + the hierarchy of controls · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the noise-control hierarchy

Once the exposure is compared against the cited action/limit thresholds
(`KB-REG-OSHA1910-95`), rank controls **in this order** — a treatment whose first or
only control is "issue ear plugs" is flagged and pushed up:

1. **Eliminate / substitute the source** — quieter process or equipment, buy-quiet
   procurement, remove the noisy task.
2. **Engineering controls** — enclosure, acoustic damping/lagging, silencers,
   vibration isolation, anti-vibration mounts.
3. **Distance & time (administrative)** — increase separation, limit exposure time,
   relocate people, schedule noisy work away from others.
4. **Hearing protection (HPD) — LAST** — selected against the residual exposure (with
   attenuation accounted for), zoned, and supported by health surveillance — never the
   primary control.

## Discipline
- HPD as the first/only control is rejected (`KB-SNIP-HOC`); engineering control sits
  above PPE.
- The thresholds that trigger action come from `KB-REG-OSHA1910-95`; the measurement
  method is `KB-STD-ISO1999-9612`. A missing measured TWA is a `[GAP]`.
- Audiometric/health data is small-cell suppressed and de-identified.

## How the skill uses this fragment
`noise-exposure-health-surveillance` compares the transcribed exposure against the cited
thresholds, then references `KB-SNIP-NOISE-CONTROL-HIERARCHY` to rank residual controls
source-first, recording owners/dates for each noise-reduction item.
