<!-- KB-SNIP-CHECKIN-ESCALATION -->
# Lone working — check-in / escalation control spine

**Fragment ID:** `KB-SNIP-CHECKIN-ESCALATION`
**This is prompt text, applied by the model — not a generator.** It is the
control-hierarchy spine for `lone-working-assessment` (REN-02): a lone worker is
protected by **scheduled check-ins + a missed-check-in escalation path +
coverage-checked communication** — a lone-worker device is a *supplement*, never the
control. A lone-working artifact that "controls" the risk with a panic-button app
and no scheduled check-in or escalation procedure, where **"no mobile signal" is
treated as an accepted risk**, is the indefensible paperwork this spine rejects.

> Source: HSE INDG73 (rev 4) + BS 8484:2022 — control-spine prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the lone-working control order

1. **Eliminate (primary).** Avoid lone working for the task where reasonably
   practicable (some tasks require more than one person).
2. **Engineer / substitute.** Reliable, **coverage-checked** communication;
   buddy/pairing; change the task or location so comms work.
3. **Administrative.** **Scheduled check-ins** at a defined interval + a **defined
   missed-check-in escalation path** (who responds, how, in what time).
4. **Device (residual only).** A BS 8484 lone-worker device supplements the
   check-in/escalation procedure — never replaces it.

## The gate (reject these)
- A treatment that leads with a device/app and has no scheduled check-in or
  escalation procedure → **reject** (device-led).
- **"No mobile signal in that area"** accepted as a residual risk → **reject**; it
  is a control failure (fix the comms or change the task).
- A missed-check-in with no defined responder/response-time → **reject**; emit
  `[GAP]`.

## How the skill uses this fragment
REN-02 ranks every lone-working control through this order, requires a scheduled
check-in + escalation procedure, and treats a coverage gap as a control failure.
