<!-- KB-REG-IN-DGCA -->
# India — DGCA State Safety Programme + operator SMS acceptance (Annex 19 adoption)

**Fragment ID:** `KB-REG-IN-DGCA`
**What this is:** the **alignment map** for India's **DGCA State Safety Programme
(SSP)** and the operator/airport/AMO **SMS-acceptance** expectations — the statutory
aviation-safety layer through which India adopts ICAO Annex 19. It is the
**cross-cutting KB capability** the `hse-aviation` skills carry as a jurisdiction row
(the same way the B-skills carry an India row): `aviation-sms-builder` aligns the SMS
manual to the SSP, `aviation-spi-spt-framework` aligns SPIs/SPTs to the SSP's
acceptable-level-of-safety-performance expectations, and so on.
**What this is NOT:** a reproduction of DGCA CAR text, and **NOT a ninth skill** —
DGCA SSP alignment is delivered here as a fragment + jurisdiction row (CT-10; the
aviation design spec §3.1 line 65). It is a **flag-and-defer pointer** to the live
DGCA SSP/CAR, never dated rule text.

> Source: DGCA Civil Aviation Requirements (CAR Section 1 — General, the SMS / SSP series) + ICAO Annex 19 adoption — alignment map; the DGCA CAR numbering evolves, so cite the topic and verify the live CAR · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (DGCA CARs / the SSP evolve — staleness window applies).

**Legacy-first / transition-aware only insofar as DGCA CARs evolve.** The DGCA
maintains the **State Safety Programme** (the State's safety-management framework under
Annex 19) and *accepts* each operator's/airport's/AMO's SMS. The numbering and detail
of the SMS-related CARs change over time, so an aviation skill **cites the SSP/CAR
topic and defers to the live DGCA document** rather than a hard-coded CAR clause —
exactly the flag-and-defer discipline the India regulatory fragments use.

## SSP layer → Annex 19 pillar → what the operator must show

| SSP / DGCA expectation | Annex 19 pillar it adopts | What the operator's SMS must show |
|---|---|---|
| State safety policy, objectives & resources | Pillar 1 (Policy) | the operator's SMS policy is consistent with the SSP; the Accountable Manager is named |
| State safety risk management | Pillar 2 (Risk Management) | a hazard register + risk classification (the ICAO 5×5) + management of change |
| State safety assurance & SPI/SPT acceptance | Pillar 3 (Assurance) | SPIs/SPTs aligned to the SSP's acceptable level of safety performance (ALoSP) |
| State safety promotion | Pillar 4 (Promotion) | training, just culture, and a confidential reporting system |
| **SMS acceptance / approval submission** | all four | a complete four-pillar SMS manual the DGCA can accept |

## Verified anchors vs `[GAP]`

- **Verified anchor (cite as a value):** the DGCA operates a **State Safety Programme**
  and **accepts operator SMS** under its CAR framework adopting ICAO Annex 19; the
  **Accountable Manager** and **Safety Manager** are named SMS roles.
- **`[GAP]` (resolve from the live DGCA document, never invent):** the **exact CAR
  Section/number and revision** for the SMS/SSP requirement — DGCA CAR numbering
  evolves; cite the topic and mark the precise clause `[GAP]` for the user to confirm
  against the current DGCA CAR. **Never fabricate a CAR number** (the citation grader
  is row-blind, so an invented clause would pass the automated gate — honesty rests on
  the `[GAP]` marker + the SME FLAG).

## Cross-reference to `hse-india`

An Indian aviation organisation that **also** runs ground operations under the
Factories Act discovers both layers: aviation safety management lives here
(`KB-REG-IN-DGCA`), while factory/contract-labour statutory filings resolve through
the `hse-india` state-form engine (`KB-REG-IN-STATEFORMS`, mandatory state detection).
This is a **navigation cross-reference, not a shared skill** — no skill is co-owned
across packs.

## Usage note

`aviation-sms-builder` reads this fragment to align the SMS manual to the DGCA SSP
when the jurisdiction is India; the other aviation skills carry the DGCA row in their
`kb-selection` table. The four-pillar SMS framework itself is jurisdiction-independent
and lives in `../standards/icao-annex19.md` (`KB-STD-ICAO-ANNEX19`).
