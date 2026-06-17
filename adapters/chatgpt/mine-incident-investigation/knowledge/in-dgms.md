<!-- KB-REG-IN-DGMS -->
# India — DGMS forms, notices, returns & appointments (legacy-first)

**Fragment ID:** `KB-REG-IN-DGMS`
**What this is:** the mine-specific **form layer** for the Mines Act 1952 / Mines
Rules — the prescribed forms, notices, returns and statutory-appointment
instruments the Directorate General of Mines Safety (DGMS) administers. Each row
carries the *duty + timing + register/form name* the source verifies; **any form
id the source does NOT verify is a marked `[GAP]` — never invented.**
**What this is NOT:** a reproduction of the Mines Rules text, and NOT a complete
numbered-form catalogue. A fabricated form value is worse than a `[GAP]` (Decision
6): the citation grader is *row-blind* (it checks that the KB *fragment ID*
resolves, not that a form *value* is real), so honesty is enforced here by the
`[GAP]` marker + the per-skill no-fabrication eval + the SME FLAG + the pre-launch
DGMS-qualified verifier (out of scope this phase).

> Source: Mines Act 1952 + Mines Rules / DGMS (https://www.dgms.gov.in/) — verified anchors per row; `[GAP]` where the source does not supply a numbered form · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (Mines Act among the 13 laws subsumed by the OSH Code 2020 — status in flux).

DGMS administers the Mines Act through **regional / zonal offices**; the
filing/portal context is regional, so an India mining skill **resolves the mine's
region/zone first** (`KB-REG-IN-STATEFORMS`, mandatory) before citing any form,
defaults to the legacy DGMS form the mine files today, and appends the OSH-Code
transition note. The Mines/DGMS data lives **once** here and is cross-referenced
(not duplicated) by `hse-india`'s Mines module.

## Verified anchors (concrete) vs. unverified forms (`[GAP]`)

These are the five anchors the source verifies as concrete — cite them as values:

| Obligation | Form / register (VERIFIED anchor) | Timing | Grounds |
|---|---|---|---|
| Accident / dangerous-occurrence register | **Form J** — accident & dangerous-occurrence register | maintained current | dgms-statutory-pack; mine-incident-investigation |
| Employee register | **Form B** — employee register | maintained current | dgms-statutory-pack |
| Accident notification | **24-hour accident notice** (serious/fatal/dangerous occurrence) | within 24h of the event | dgms-statutory-pack; mine-incident-investigation |
| Periodic return | **Annual return** | by **~20 January** | dgms-statutory-pack |
| Statutory appointment | **Manager (+ statutory officials) appointment** letter | on appointment | dgms-statutory-pack |

Every **other** DGMS form id is an unverified extension slot and is marked `[GAP]`:

| Obligation | Form (UNVERIFIED) | Note |
|---|---|---|
| The numbered accident-notice form id | `(DGMS-prescribed — verify per mine)` `[GAP]` | the 24h duty + timing are verified; the exact *numbered form* is `[GAP]` |
| Quarterly / periodic returns beyond the annual | `(DGMS-prescribed — verify per mine)` `[GAP]` | only the annual return ~20 Jan is a verified anchor |
| Other prescribed registers / notices | `(DGMS-prescribed — verify per mine)` `[GAP]` | resolve the numbered form per mine/region; record `[GAP]`, never invent |

## How the skills use this fragment
- `dgms-statutory-pack` + `mine-incident-investigation` cite **only** the five
  verified anchors as values; ANY DGMS form beyond them emits a literal `[GAP]`
  (e.g. `(DGMS-prescribed — verify per mine) [GAP]`), never a fabricated number.
- Region/zone detection is **mandatory** before citing a form (a wrong-zone DGMS
  office = a misfiled statutory notice).
- The OSH-Code transition note is appended legacy-first (most mines still file the
  legacy DGMS forms; the Code's commencement is state-by-state and pending).
- A no-fabrication eval (per skill) asserts the skill emits `[GAP]` rather than a
  value for any un-verified DGMS form.
