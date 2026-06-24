# Electrical Permit & Switching Program — 11 kV Feeder F2 to RMU-3 (Substation 2)

*Decision-support only. A competent person (authorised / senior authorised person) must review and
sign off this switching program. A prior switching incident is cited at role level as context; the
re-identification key is held separately.*

## 1. Apparatus & work activity

De-identification ran first: the injured operator's name, the incident date, and the medical detail
were scrubbed to role level; no named operator and no `<5` injury cell appears below.

- **Apparatus:** 11 kV feeder F2 to RMU-3, ring main, Substation 2 (apparatus-specific — not "the
  substation").
- **Work activity:** cable work on the F2 feeder, worked **dead**.
- **Proposed control (as received):** "just isolate the feeder breaker and crack on — we don't need
  to prove dead or earth it". This is assessed against the isolation-integrity gate below.

## 2. De-energization / isolation decision (recorded FIRST — the primary control)

The cable work **CAN be done dead**. An **electrically safe work condition** (NFPA 70E **Article
120**) is established **before** any work: isolate at every point of supply → prove dead → apply
protective earthing. The proposed "don't prove dead or earth it" shortcut is **REJECTED** — an
isolated-but-unproven, un-earthed apparatus is not a safe working condition.

## 3. Point-of-isolation & earthing register

| Point of isolation / earthing | Device | Action | Authorisation |
|---|---|---|---|
| Feeder F2 circuit breaker (source) | 11 kV CB | Open + rack out; lock-off | Senior Authorised Person |
| RMU-3 incomer (downstream point of supply) | Ring main unit switch | Open + lock-off (caps-and-locks) | Authorised Person |
| Point of work — F2 cable | Proving unit | Prove dead (prove-test-prove) | Authorised Person |
| Point of work — F2 cable | Portable earths | Apply protective earthing | Senior Authorised Person |
| LV auxiliary / VT supply | Auxiliary isolator | Isolate + lock-off | Authorised Person |

## 4. Ordered switching sequence (isolate → prove dead → earth → sanction → restore)

| Step | Switching action | Authorisation |
|---|---|---|
| 1 — Plan & authorise | Issue the switching schedule under control; brief the work party | Senior Authorised Person |
| 2 — Isolate | Open feeder F2 CB + RMU-3 incomer at every point of supply; lock-off / caps-and-locks | Senior Authorised Person |
| 3 — Prove dead | Test for absence of voltage at the point of work; prove the unit before AND after (prove-test-prove) | Authorised Person |
| 4 — Earth | Apply protective earthing at the point of work to hold the conductor at earth potential | Senior Authorised Person |
| 5 — Sanction the work | Issue the **permit-to-work** (work on dead equipment) defining the safe zone, precautions, and limits | Senior Authorised Person |
| 6 — Carry out + restore | Work within the permit limits; on completion cancel the permit, remove earths, remove locks/tags, restore supply | Senior Authorised Person |

> **Sanction-to-test is kept DISTINCT.** This activity is work on dead equipment — a
> **permit-to-work**, not a sanction-to-test. A sanction-to-test (controlled re-energization for
> testing) is a separate safety document and is never combined with a work-on-dead permit.

## 5. Isolation-integrity gate (the de-energize-first lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "isolate and
crack on — don't prove dead or earth it" is the **isolation-integrity failure** — it authorises work
on apparatus isolated but **not proven dead** and **omits protective earthing** where the HV
procedure requires it. It is a **CONTROLS FLAG** **pushed up the hierarchy**.

| Proposed / existing control | Gate outcome |
|---|---|
| "Isolate the feeder breaker and crack on — don't prove dead or earth it" | **FLAG — work authorised un-proven and un-earthed.** Pushed up the hierarchy: isolate → **prove dead (prove-test-prove)** → **apply protective earthing** → issue the permit-to-work. Work is never authorised on apparatus isolated but not proven dead. |

## 6. Hierarchy-ranked controls (de-energize + isolate first → PPE last)

| Control | Tier | Owner (role) |
|---|---|---|
| De-energize + isolate at every point of supply; establish an ESWC (Article 120) — the primary control | Elimination | Senior Authorised Person |
| Prove dead (prove-test-prove) + apply protective earthing before any work | Engineering | Senior Authorised Person |
| Issue the permit-to-work (safety-document control) defining the safe zone and limits | Administrative | Senior Authorised Person |
| Electrical / arc-rated PPE as the residual last line during the switching steps | PPE | Authorised Person |

## 7. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Confirm portable-earth ratings and earthing points for the F2 cable work | P1 | Senior Authorised Person | 2026-07-05 |
| Verify the proving unit is in calibration before the switching operation | P1 | Authorised Person | 2026-07-05 |
| Brief the switching schedule + permit limits to the work party | P2 | Senior Authorised Person | 2026-07-08 |

## 8. Assumptions, gaps & sign-off

- Points of isolation taken from the supplied single-line diagram — a missing point of supply would
  be a `[GAP]`, never an assumed isolation.
- India site (if applicable): state electricity-rule line-clearance return owed — `[GAP]` (resolve
  the state via `hse-india`; no national form number minted).
- **Regulatory basis:** NFPA 70E (2024) Article 120 / Annex K / 120.5; OSHA 29 CFR 1910.269
  (269(d) / 269(n) / 269(m)) + 1910.333 + 1910.147; UK EAWR 1989 regs 12–13 + HSG85; ISO 45001
  §6.1.2.
- Review trigger: per switching operation / on network change / on procedure change — whichever is
  first.
- Decision-support only — a competent person (authorised / senior authorised person) must review
  before use.
