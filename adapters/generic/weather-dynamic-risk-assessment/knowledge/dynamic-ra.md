<!-- KB-SNIP-DYNAMIC-RA -->
# Weather dynamic RA — threshold→action→re-assessment control spine

**Fragment ID:** `KB-SNIP-DYNAMIC-RA`
**This is prompt text, applied by the model — not a generator.** It is the
control-hierarchy spine for `weather-dynamic-risk-assessment` (REN-03): a weather
RA defines a **numeric threshold → an action (hold / stop / evacuate) → a mandatory
re-assessment trigger**, measured at **hub height (not base of tower)** for turbine
work. A weather artifact that says "monitor the wind and stop if it gets too windy",
with no numeric threshold and no defined action, is the indefensible paperwork this
spine rejects.

> Source: ISO 45001:2018 cl 6.1.2 (dynamic/point-of-work RA) + BS 7121-1 (man-riding ceiling) + NFPA 780 (lightning) — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the dynamic-RA structure (per weather parameter)

1. **Threshold.** A specific numeric trigger for each parameter (wind, lightning,
   ice, visibility, temperature). The BS 7121-1 **7 m/s** man-riding figure is the
   verified anchor; the ≈15 m/s tower-top baseline is **proposed-and-user-confirmed**
   (`[ASSUMED A4]`); manufacturer/site values are `[GAP]`.
2. **Action.** What happens when the threshold is reached — **hold / stop /
   evacuate** — defined in advance, not decided on the day.
3. **Mandatory re-assessment trigger.** A defined event/interval that forces a fresh
   point-of-work assessment (e.g. forecast change, threshold approached).
4. **Measurement discipline.** Wind is measured at **hub height, not base of
   tower** — a base-of-tower reading understates the exposure.

## The gate (reject these)
- A weather control with **no numeric threshold** ("stop if too windy") → **reject**.
- A threshold with **no defined action** (hold/stop/evacuate) → **reject**.
- A threshold with **no re-assessment trigger** → **reject**.
- A wind figure read at the base of the tower for tower-top work → **reject**.
- A threshold invented rather than cited/proposed-and-confirmed → **reject**; emit
  `[GAP]`.

## How the skill uses this fragment
REN-03 builds each weather control as threshold→action→re-assessment-trigger at hub
height, cites the BS 7121-1 anchor, and proposes-and-confirms or `[GAP]`s every
other numeric threshold.
