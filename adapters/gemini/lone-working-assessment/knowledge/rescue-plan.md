<!-- KB-SNIP-RESCUE-PLAN -->
# Work-at-height rescue — rescue-plan-mandatory control spine

**Fragment ID:** `KB-SNIP-RESCUE-PLAN`
**This is prompt text, applied by the model — not a generator.** It is the
rescue-discipline spine shared by `wind-turbine-work-at-height-rescue` (REN-01) and
`lone-working-assessment` (REN-02): **a tested rescue plan is mandatory before work
at height begins** — a suspended worker is recovered in minutes by the team's own
capability, and **"call the emergency services" is NOT a rescue plan.** A WAH
artifact whose rescue arrangement is "phone 999/112 and wait" is the indefensible
paperwork this spine rejects.

> Source: Work at Height Regulations 2005 reg 4 (rescue planning) + GWO ART rescue competence — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the rescue discipline

1. **Plan rescue before work (reg 4).** Rescue is planned and resourced as part of
   the work-at-height plan — not improvised after a fall.
2. **Team-owned, timed capability.** The team has the competence (GWO ART /
   equivalent), equipment and method to recover a suspended worker **within minutes**
   (suspension trauma) — not after an external response arrives.
3. **Emergency services supplement, never substitute.** Calling 999/112 is an
   addition to the team's own tested rescue, never the rescue plan itself.
4. **Two-person-minimum + ground support.** A climb is a two-person-minimum team
   with ground support able to initiate the rescue.

## The gate (reject these)
- A rescue plan whose lead arrangement is "call the emergency services" → **reject**.
- A WAH plan with **no** rescue plan → **reject** (reg 4 makes it mandatory).
- A rescue that depends on an untested capability or unstated recovery time →
  **reject**; emit `[GAP]`.

## How the skill uses this fragment
REN-01 and REN-02 require a tested, team-owned, timed rescue plan before WAH /
foreseeable-rescue lone work, and reject an emergency-services-alone arrangement.
