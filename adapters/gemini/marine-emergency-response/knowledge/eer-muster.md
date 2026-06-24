<!-- KB-SNIP-EER-MUSTER -->
# Offshore EER — muster→refuge→evacuation→escape→rescue control spine

**Fragment ID:** `KB-SNIP-EER-MUSTER`
**This is prompt text, applied by the model — not a generator.** It is the
emergency-response hierarchy spine for `marine-emergency-response` (MAR-03): the
EER chain is **muster → temporary refuge → evacuation → escape → rescue**, with
escalation-prevention and temporary-refuge (TR) integrity coming **before**
abandonment. An EER plan reduced to "muster and wait" or "abandon and hope for
rescue", with no escalation-prevention or TR-integrity basis, is the indefensible
paperwork this spine rejects.

> Source: PFEER 1995 (SI 1995/743) + HSE L65 + SOLAS Ch III / LSA Code — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the EER hierarchy

1. **Escalation prevention (primary).** Detect, control and prevent the emergency
   from escalating (fire/gas detection, ESD, firefighting) so abandonment is the
   last resort, not the plan.
2. **Muster + POB accounting.** Account for all persons against the station bill;
   muster to designated stations.
3. **Temporary refuge (TR) integrity.** Protect persons in the TR for the required
   endurance while the response decision is made.
4. **Evacuation → escape → rescue.** Controlled evacuation (TEMPSC/other),
   then escape and rescue (reg 17 recovery & rescue + ERRV) — in that order.

## The gate (reject these)
- An EER plan whose lead control is "abandon ship/installation" with no
  escalation-prevention or TR-integrity basis → **reject**.
- A muster plan with **named individuals** instead of role labels → **reject**;
  de-identify the station bill first.
- A missing TR endurance / EER basis / ERRV arrangement silently assumed →
  **reject**; emit `[GAP]`.

## How the skill uses this fragment
MAR-03 structures the emergency response on this hierarchy and rejects an
abandonment-led EER plan.
