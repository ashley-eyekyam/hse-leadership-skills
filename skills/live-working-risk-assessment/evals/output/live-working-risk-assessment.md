<!-- CANDIDATE golden output for live-working-risk-assessment (UTIL-03). Generated from eval case 1's
     scenario (thermographic survey on the energized LV switchboard SB-2, 400 V, Substation 2). It
     demonstrates the core lever: de-energize-first + live-working justification discipline. The
     crew's proposal — "just do it live, it's quicker, production can't stop, and we'll wear the
     arc-flash suit" — is a convenience justification led by arc-rated PPE; it is REJECTED on the
     convenience grounds and FLAGGED as PPE-led, then PUSHED UP the hierarchy (de-energize -> engineer
     -> approach control + permit -> arc-rated PPE LAST). The EAWR reg 14 three-part statutory test is
     applied and a VALID justification recorded (an in-service survey is unreasonable to perform dead).
     The arc-flash incident energy is CROSS-REFERENCED from arc-flash-assessment (UTIL-01), never
     re-derived. An energized-work permit (Annex J) is issued. The prior contact incident is
     de-identified to role level. NOT owner-LOCKED — the owner reviews + locks in P17. -->

# Live-Working Risk Assessment — Thermographic Survey, Energized LV Switchboard SB-2 (Substation 2)

*Decision-support only. A competent person must review this assessment and a competent authority must
sanction the live work before it proceeds. A prior contact incident is cited at role level as
context; the re-identification key is held separately.*

## 1. Task & live-conductor description

De-identification ran first: the injured worker's name, the incident date, and the medical detail
were scrubbed to role level; no named worker and no `<5` injury cell appears below.

- **Task:** thermographic (infrared) survey of the energized LV switchboard SB-2, worked **live**.
- **Live conductors / apparatus:** SB-2 main switchboard busbars and outgoing ways, **400 V** (LV),
  Substation 2 (task- and conductor-specific — not "work near the live parts").
- **Proposed approach (as received):** "just do it live, it's quicker — production can't stop to
  de-energize, and we'll wear the arc-flash suit". This is assessed against the de-energization
  evaluation and the statutory justification gate below.

## 2. De-energization evaluation (recorded FIRST — the primary control)

The default is to establish an **electrically safe work condition** (NFPA 70E **Article 120** / EAWR
dead-working). For an **in-service thermographic survey**, de-energizing the board removes the
thermal load the survey exists to measure — so dead working defeats the purpose of the task. The
de-energization evaluation is therefore recorded **before** any justification, and live work is
treated as the **exception**, not the default. (A task that could be done dead would be recommended
for an ESWC and would **not** be assessed live.)

## 3. Statutory live-working justification (EAWR reg 14 / OSHA 1910.333(a)(2))

The crew's reason — **"it's quicker / production can't stop"** — is **convenience and is REJECTED**:
economic convenience alone never satisfies EAWR reg 14 or OSHA 1910.333(a)(2). The three-part
statutory test is applied, and a **valid** justification recorded only because all three genuinely
hold:

| Statutory test (all three must hold) | Recorded finding |
|---|---|
| (a) It is **unreasonable to work dead** | An in-service infrared survey cannot be performed dead — de-energizing removes the thermal load being measured (a genuine task constraint, not a desire to keep running). |
| (b) It is **reasonable to work live** | A **non-contact** survey, performed by a qualified person within a controlled approach boundary, can be done safely live. |
| (c) **Suitable precautions** are taken | Approach-boundary control, non-contact technique, insulated barriers, qualified persons, arc-rated PPE against the cross-referenced incident energy, and an energized-work permit (below). |

## 4. Approach boundaries (shock — NFPA 70E 130.4 / OSHA 1910.269)

| Boundary / parameter | Value | Basis |
|---|---|---|
| Nominal system voltage | 400 V (LV) | Named apparatus SB-2 |
| Limited approach boundary | Per NFPA 70E 130.4 Table (confirm for 400 V) | NFPA 70E 130.4 (shock) |
| Restricted approach boundary | Per NFPA 70E 130.4 Table (confirm for 400 V) | NFPA 70E 130.4 (shock) |
| Working distance / technique | Non-contact survey, outside the restricted boundary | Task method |
| Arc-flash incident energy at working position | **Cross-referenced from arc-flash-assessment (#1)** — not recomputed here | arc-flash-assessment / `arcflash.py` |
| NFPA 70E PPE category at working position | **Cross-referenced from arc-flash-assessment (#1)** | arc-flash-assessment / NFPA 70E 130.7 |

> The arc-flash incident energy + PPE category are **computed once** by `arc-flash-assessment` and
> **cross-referenced** here — this assessment never re-derives the cal/cm² value. A missing arc-flash
> study is a `[GAP]`; where the cross-referenced incident energy exceeds **40 cal/cm²**, the work is
> flagged **prohibited**.

## 5. De-energize-first / convenience-rejection gate (the lever)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "do it live
because it's quicker and wear the arc-flash suit" is **PPE-led with a convenience justification** —
it is a **CONTROLS FLAG** **pushed up the hierarchy**.

| Proposed / existing control | Gate outcome |
|---|---|
| "Do it live — it's quicker, production can't stop; we'll wear the arc-flash suit" | **FLAG — convenience justification + PPE-led.** Rejected on convenience grounds; the de-energization evaluation + the three-part statutory test are applied first, the control is pushed up the hierarchy (de-energize → non-contact technique/barriers → approach control + permit → arc-rated PPE LAST), and arc-rated PPE is recorded as the residual last line, not the headline. |

## 6. Hierarchy-ranked precautions (de-energize first → arc-rated PPE last)

| Control | Tier | Owner (role) |
|---|---|---|
| De-energize + establish an ESWC (Article 120) — the default wherever the task can be done dead | Elimination | Authorised Person |
| Non-contact survey technique + insulated barriers between the worker and the live conductors | Engineering | Electrical Engineer |
| Approach-boundary control + qualified-person & accompaniment + energized-work permit | Administrative | Authorised Person |
| Arc-rated PPE selected against the cross-referenced incident energy — the documented LAST line | PPE | Qualified Electrical Worker |

## 7. Energized electrical work permit (NFPA 70E Annex J content)

| Permit element (Annex J) | Content |
|---|---|
| Description of energized work + apparatus | Thermographic survey, energized LV switchboard SB-2 (400 V), Substation 2 |
| Justification for energized work | EAWR reg 14 three-part test met (recorded §3); convenience reason rejected |
| Shock approach boundaries + protection | Limited/restricted approach boundaries (130.4); non-contact technique; insulated barriers |
| Arc-flash boundary + incident energy + PPE | Cross-referenced from arc-flash-assessment (#1); arc-rated PPE per the computed category |
| Qualified persons + accompaniment | Qualified Electrical Worker + Authorised Person accompaniment |
| Authorising signature | Competent authority sign-off (role) — REQUIRED before live work proceeds |

## 8. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Cross-reference the arc-flash incident energy + PPE category from arc-flash-assessment (no re-derivation) | P1 | Electrical Engineer | 2026-07-05 |
| Confirm the limited/restricted approach boundaries for 400 V (NFPA 70E 130.4) + brief the work party | P1 | Authorised Person | 2026-07-05 |
| Issue + authorise the energized-work permit (Annex J content) with the recorded justification | P1 | Authorised Person | 2026-07-08 |

## 9. Assumptions, gaps & sign-off

- The arc-flash incident energy at the working position is cross-referenced from
  `arc-flash-assessment` — a missing arc-flash study is a `[GAP]`, never an invented cal/cm² value.
- Where the cross-referenced incident energy exceeds **40 cal/cm²**, the live work is flagged
  **prohibited**.
- India site (if applicable): state electricity-rule line-clearance return owed — `[GAP]` (resolve
  the state via `hse-india`; no national form number minted).
- **Regulatory basis:** NFPA 70E (2024) 110.5/130.2 (justification + permit), 130.4 (approach
  boundaries), Annex J (the permit), Article 120 (the ESWC default); OSHA 29 CFR 1910.333(a)(2) +
  1910.269; UK EAWR 1989 reg 14 + HSG85 + HSR25; ISO 45001 §6.1.2.
- Review trigger: per live-work operation / on equipment change / on procedure change — whichever is
  first.
- Decision-support only — a competent person must review and a competent authority must sanction any
  live work before use.
