<!-- KB-SNIP-LIVE-WORK-JUSTIFICATION -->
# Live-work justification — the three-part gate (convenience is not a justification)

**Fragment ID:** `KB-SNIP-LIVE-WORK-JUSTIFICATION`
**This is prompt text, applied by the model — not a generator.** It is the gate
that decides whether any energized (live) electrical work is permitted in
`hse-utilities-power`. The default is **dead working**; live work is the rare,
fully-justified exception. **Convenience, cost, or schedule pressure is never a
justification.**

> Source: EAWR reg 14 (three-part test) + OSHA 1910.333(a)(2) (energized-work conditions) + NFPA 70E 130.2 (energized-work permit conditions) — gate prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the three-part live-work test (all three must hold)

Live / energized work is permitted **only** where ALL of the following are true,
each recorded:

1. **It is unreasonable in the circumstances to work dead** — de-energizing
   introduces a *greater* hazard (e.g. life-support, ventilation, an
   infeasible-to-interrupt continuous process) or is genuinely infeasible. A
   *desire* to keep equipment running is **not** "unreasonable to work dead".
2. **It is reasonable in the circumstances to work live** — the task can be done
   safely live given the system, the work, and the competence available.
3. **Suitable precautions are taken** — competent persons, approach-boundary
   control, insulated tools/PPE selected against the **calculated** incident energy
   (`arcflash.py` → NFPA 70E band, `KB-STD-NFPA70E`) and shock approach limits,
   and an **energized-electrical-work permit** authorizing the task.

## The gate (reject these)
- A live-work treatment justified by convenience / cost / "it's quicker" → **reject**.
- Live work with no energized-electrical-work permit → **reject**.
- PPE selected against a narrated/estimated incident energy rather than the engine
  output → **reject**.
- Any of the three tests not recorded → treat as **not justified**; default to dead
  working or emit `[GAP]`.

## How the skill uses this fragment
`live-working-risk-assessment` (UTIL-03) and any energized-task path in the
switching program apply this three-part gate before authorizing live work; the
arc-flash figure is the engine's, never invented. No skill restates the gate in its
own body (anti-drift).
