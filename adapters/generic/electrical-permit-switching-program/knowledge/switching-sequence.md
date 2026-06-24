<!-- KB-SNIP-SWITCHING-SEQUENCE -->
# Switching sequence — isolation, prove dead, earthing, sanction-to-test discipline

**Fragment ID:** `KB-SNIP-SWITCHING-SEQUENCE`
**This is prompt text, applied by the model — not a generator.** It is the
electrical **switching and isolation** discipline for `hse-utilities-power`: the
ordered safety-document sequence that takes equipment from energized to a proven
safe working condition and back, with the safety-document control that prevents
inadvertent re-energization. It carries the full isolation / prove-dead / earthing
/ sanction-to-test vocabulary so a switching-program skill needs no separate
electrical-isolation fragment.

> Source: HSG85 safe-working-practice steps + EAWR regs 12–13 + OSHA 1910.269(d)/(m)/(n) + utility switching/safety-document practice — method prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the switching / isolation sequence

1. **Plan & authorize.** Identify the apparatus, all points of supply, and the
   competent authorized person; issue the switching schedule under control.
2. **Isolate.** Open the isolating device(s) at every point of supply; render the
   isolation secure (lock-off / caps-and-locks) so it cannot be inadvertently
   re-energized.
3. **Prove dead.** Test for absence of voltage at the point of work with a proving
   unit verified before and after (the prove-test-prove discipline).
4. **Earth / ground.** Apply protective earthing/grounding where the system or
   procedure requires it, to discharge and hold the conductor at earth potential.
5. **Issue the safety document.** Issue a **permit-to-work** (work on dead
   equipment) or a **sanction-to-test** (where testing requires controlled
   re-energization), defining the safe zone, the precautions, and the limits.
6. **Carry out, then restore.** Work within the document's limits; on completion,
   cancel the document, remove earths, remove locks/tags, and restore supply under
   the switching schedule.

## Vocabulary this fragment carries (so UTIL-02 needs no separate fragment)
isolation · point of isolation · lock-off / caps-and-locks · prove dead /
prove-test-prove · protective earthing / grounding · permit-to-work ·
sanction-to-test · safety document · switching schedule · authorized / competent
person · safe working condition.

## The gate (reject these)
- Work authorized on equipment that was isolated but **not proven dead** → reject.
- A switching program that omits earthing where the procedure requires it → reject.
- Re-energization without cancelling the safety document and removing earths/locks
  → reject.

## How the skill uses this fragment
`electrical-permit-switching-program` (UTIL-02) and the live-working assessment
ground their switching/isolation method here — including the isolation vocabulary —
so no skill restates the sequence in its own body (anti-drift).
