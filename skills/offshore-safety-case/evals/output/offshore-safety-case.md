# Offshore Safety Case — Argument Map (assistive structure) — Thistle Bravo platform

**Installation:** Thistle Bravo (fixed production platform)
**Regime:** SI 2015/398 — Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 (current; SCR 2005 is the superseded legacy reference)
**Scope:** SI 2015/398 Schedule 6/7 elements — MAH identification · SEMS · CMAPP · ALARP demonstration · SCE register + performance standards · independent verification scheme · emergency response (EER)
**Classification:** Confidential — competent-person review required; PRECEDES competent-authority (HSE + OPRED) acceptance
**De-identification:** Every accountability is by role label (OIM, Technical Authority, Independent Verifier, Duty Holder). Names, contacts and competence-card numbers were pseudonymised before drafting; persons-on-board is carried as a count; the re-identification key is held separately.

---

## 1. Assistive posture (what this is — and is not)

This is an **assistive structuring** of the duty-holder's safety case. It assembles the goal-structured **claim → argument → evidence** map and **records** the duty-holder's content. It does **not**:

- produce the safety case autonomously;
- compute or invent any QRA, consequence distance, or major-accident frequency (external figures are recorded **with provenance**);
- assert any barrier / SCE effective without a cited performance standard or verifier finding;
- emit "accepted / approved / authorised" status — **acceptance is the competent authority's act**, and this output precedes it.

Unsupplied elements, figures, and barrier-effectiveness claims are recorded **`[GAP]`**.

## 2. Safety-case argument map (SI 2015/398 Schedule 6/7)

| Claim | Sub-claim / element | Argument strategy | Evidence reference (duty-holder-supplied) | Status |
|---|---|---|---|---|
| Risks are ALARP | MAH identification | Identify MAH & scenarios from the duty-holder's HAZID/bowtie | HAZID-TB-2025; bowtie BT-01..BT-04 | Supported |
| Risks are ALARP | Hydrocarbon release controlled | Prevention + detection + mitigation barriers, each to a performance standard | Bowtie BT-01; F&G SCE PS-07 (verifier-confirmed) | Supported |
| Risks are ALARP | Fire & explosion controlled | Passive + active fire protection adequacy to a performance standard | FEA-TB-02; deluge SCE PS-09 | Supported |
| Risks are ALARP | ALARP demonstration | Record the **external** QRA with provenance — never computed here | **`[GAP]`** — external QRA not yet supplied | Pending external input |
| Risks are ALARP | SCE register + performance standards | List the SCEs and the performance standard each must meet | SCE register TB-SCE-v3 (2 performance standards **`[GAP]`**) | Partially supported |
| Risks are ALARP | Independent verification | Record the verifier findings against the SCE performance standards | Verifier report VR-2025-11 | Supported |
| Risks are ALARP | Structural integrity assured | Fatigue + inspection regime adequacy | SIM plan TB-SIM-2025; last inspection report | Supported |
| Risks are ALARP | Emergency response (EER) adequate | **Cross-reference** the marine-emergency-response (MAR-03) EER plan — not rebuilt | marine-emergency-response (MAR-03) plan — Thistle Bravo | Cross-referenced |

A row with no supplied evidence is recorded **`[GAP]` / Pending**, never asserted "Supported".

## 3. SEMS & CMAPP

- **CMAPP** — the corporate major-accident-prevention policy is recorded as supplied; each policy commitment is traced to a delivering SEMS element. A policy commitment with no corresponding SEMS element is flagged **`[GAP]`**.
- **SEMS** — the safety & environmental management system description is recorded; ISO 45001 clause 5/8 framing applied. The SEMS delivers the CMAPP commitments.

## 4. SCE register & verification (no un-evidenced effectiveness)

| SCE | Performance standard | Verifier finding | Status |
|---|---|---|---|
| Fire & gas detection | PS-07 | VR-2025-11: met | Effective — evidenced |
| Emergency shutdown (ESD) | PS-08 | VR-2025-11: met | Effective — evidenced |
| Deluge / active fire protection | PS-09 | VR-2025-11: met | Effective — evidenced |
| Temporary refuge integrity | **`[GAP]`** — no performance standard supplied | — | **`[GAP]`** — not asserted effective |
| Blowdown system | **`[GAP]`** — no performance standard supplied | — | **`[GAP]`** — not asserted effective |

No SCE is asserted effective without a cited performance standard **and** a verifier finding. The two outstanding SCEs are recorded **`[GAP]`**, not assumed adequate.

## 5. Key findings (structuring gaps, not analysis)

| # | Finding | Risk | Evidence |
|---|---|---|---|
| F1 | External QRA / ALARP demonstration not supplied — cannot be assembled; **`[GAP]`**, no figure invented or computed | High | Argument map, ALARP row |
| F2 | Two SCE performance standards (TR integrity, blowdown) outstanding — neither asserted effective | Medium | SCE register TB-SCE-v3 |
| F3 | CMAPP commitment on management-of-change not yet traced to a SEMS element | Medium | SEMS/CMAPP cross-check |

## 6. Hierarchy of controls (HoC-ranked risk-reduction measures)

| Order | Control | Tier | Owner (role) |
|---|---|---|---|
| 1 | Inherently safer design — topsides hydrocarbon inventory minimisation | Elimination | Process Authority |
| 2 | Fire & gas detection with automatic deluge (SCE PS-07/PS-09, verified) | Engineering | Technical Authority |
| 3 | Emergency shutdown & blowdown (blowdown PS **`[GAP]`**) | Engineering | Technical Authority |
| 4 | Permit-to-work and safe-isolation regime | Administrative | OIM |

## 7. Recommendations (SMART, [GAP]-closure)

| Priority | Action | Owner (role) | Due |
|---|---|---|---|
| P1 | Supply the external QRA / consequence analysis so the ALARP demonstration can be recorded with provenance (the skill records, it does not compute) | Technical Authority | 2026-09-30 |
| P1 | Supply the two outstanding SCE performance standards (TR integrity, blowdown) and the verifier findings against them | Duty Holder | 2026-08-31 |
| P2 | Trace the management-of-change CMAPP commitment to a delivering SEMS element | OIM | 2026-09-15 |

## 8. Cross-reference

The **emergency-response (EER) element** of this safety case is produced and maintained by the `marine-emergency-response` (MAR-03) plan for Thistle Bravo. This safety case **cross-references** that plan — the two are kept distinct and never merged.

## Regulatory basis

- **SI 2015/398** — Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 (the current regime; SCR 2005 is the superseded legacy reference).
- **Offshore Safety Directive 2013/30/EU**.
- **ALARP demonstration principles** — the external QRA is recorded with provenance, never computed here.
- **ISO 45001 cl 8.1.2** — hierarchy of controls.

*Decision-support only. This structured argument must be reviewed by a competent person and PRECEDES competent-authority acceptance; it does not assert "accepted", "approved", or "authorised" status.*
