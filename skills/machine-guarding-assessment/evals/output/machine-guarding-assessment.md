<!-- CANDIDATE golden output for machine-guarding-assessment (MFG-01). Generated from eval case 1's
     scenario (PL-3 250-ton power press, blanking line, Plant 3). It demonstrates the core lever:
     the engineering-control-led guard gate. The point-of-operation control proposed by the line —
     "operators trained to keep hands clear / wear gloves" — is a PPE/admin-only treatment of a
     mechanical hazard zone; it is FLAGGED and PUSHED UP the hierarchy (restored presence-sensing
     interlock + fixed perimeter), never accepted as the headline control. Each danger zone gets a
     specific guard selected in order against the access-frequency rule, cited to its ISO 14120 /
     OSHA Subpart O basis. The defeated interlock is an immediate high-priority finding. The
     maintenance interaction cross-references KB-REG-LOTO. The prior amputation incident is
     de-identified to role level. NOT owner-LOCKED — the owner reviews + locks in P17. -->

# Machine-Guarding Assessment — PL-3 Power Press (blanking line, Plant 3)

*Decision-support only. A competent person must review and sign off this machine-guarding
assessment. A prior amputation incident is cited at role level as evidence; the re-identification
key is held separately.*

## 1. Machine description & function

De-identification ran first: the injured operator's name, the incident date, and the medical detail
were scrubbed to role level; no named operator and no `<5` injury cell appears below.

- **Machine:** PL-3 250-ton mechanical power press, blanking line, Plant 3 (machine-specific — not a
  "guard all moving parts" statement).
- **Hazardous motions:** descending platen (point of operation / crush), exposed rotating
  power-transmission shaft + coupling at the rear drive, in-running nip at the feed rolls.

## 2. Hazard-zone register

| Danger zone | Risk | Basis / evidence |
|---|---|---|
| Point of operation — descending platen | **High** | OSHA 1910.212; a prior **amputation injury** at this zone (role-level evidence; light-curtain interlock was bridged) |
| Power-transmission shaft + coupling (rear drive) | Medium | OSHA 1910.219; fixed guard removed for maintenance, not refitted (WO-228) |
| In-running nip — feed rolls | Medium | OSHA 1910.212; nip accessible during setting, no fixed/interlocked guard |

> **Immediate high-priority finding:** the platen light-curtain interlock is **defeated (bridged)** —
> the press must remain quarantined and locked out until the interlock is restored and proven.

## 3. Engineering-led guard gate (the controls-first lever)

`controls.validate_treatment` was run for **each** danger zone before any control was accepted. The
guard/device is selected in order (fixed → interlocked → presence-sensing → two-hand/hold-to-run →
trip) against the **access-frequency rule**. A mechanical-zone control left **PPE-only / admin-only**
is a **FLAG pushed up the hierarchy — never the headline control**.

| Danger zone | Proposed / existing control | Gate outcome |
|---|---|---|
| Point of operation | Line proposed **"operators to keep hands clear / wear cut-resistant gloves"** | **CONTROLS FLAG — PPE/admin-only on a mechanical hazard zone (`ppe_admin_only=True`).** Pushed up the hierarchy: **restore + tamper-seal the presence-sensing light-curtain interlock** (frequent access) + a **fixed perimeter** where access is not needed. Operator care/gloves is NOT the headline control. |
| Power-transmission shaft | Fixed guard removed, not refitted | **Refit the fixed guard** (rare/maintenance-only access — preferred guard; ISO 14120 / 1910.219). |
| In-running nip — feed rolls | None | **Interlocked movable guard** (opening isolates the rolls; occasional setting access; ISO 14120 / 1910.212). |

> **Why the point-of-operation flag matters:** "operators trained to keep hands clear and wear
> gloves" is exactly the PPE/admin-only treatment of a mechanical hazard zone this assessment exists
> to reject. A prior amputation already occurred here. The control is the **engineering-led guard**
> (presence-sensing interlock + fixed perimeter); gloves are at most residual PPE, never the
> safeguarding measure.

## 4. Guard/device selection by zone (ISO 14120 basis)

| Danger zone | Access frequency | Selected guard/device | Cited basis |
|---|---|---|---|
| Point of operation — platen | Frequent (each cycle) | Restored presence-sensing light-curtain interlock + fixed perimeter | OSHA 1910.212; ISO 12100 step 2; ISO 14120 (presence-sensing per access-frequency rule) |
| Power-transmission shaft + coupling | Rare (maintenance only) | Fixed guard refitted + secured | OSHA 1910.219; ISO 14120 fixed guard |
| In-running nip — feed rolls | Occasional (setting) | Interlocked movable guard | OSHA 1910.212; ISO 14120 interlocked guard |

No guard recommendation is asserted without its cited duty/standard basis.

## 5. Safeguarding plan — hierarchy of controls (residual-ranked)

| Control | Tier | Owner (role) |
|---|---|---|
| Restore + tamper-seal the platen presence-sensing light-curtain interlock | Engineering | Maintenance Lead |
| Refit + secure the power-transmission shaft fixed guard before restart | Engineering | Maintenance Lead |
| Fit an interlocked movable guard to the feed-roll nip | Engineering | Process Engineer |
| Guard-integrity check added to start-of-shift checklist (supports, never replaces, the guards) | Administrative | Production Lead |

## 6. Interaction-mode controls (incl. maintenance LOTO)

| Interaction mode | Control |
|---|---|
| Normal operation | Presence-sensing + fixed/interlocked guards in place; guard-integrity check at start of shift |
| Setting | Interlocked feed-roll guard; hold-to-run at reduced speed where access is unavoidable |
| Cleaning | Stop + isolate before reaching into any danger zone; no cleaning of moving parts |
| **Maintenance** | **LOTO energy isolation (`KB-REG-LOTO`):** identify sources (electrical, stored mechanical/flywheel, pneumatic) → isolate + lock → **verify zero energy** (flywheel at rest, pressure bled) before guard removal or die-area access |

## 7. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Restore + verify the platen interlock by a competent person (clears the high finding + the controls flag) | P1 | Maintenance Lead | 2026-06-28 |
| Refit the power-transmission shaft fixed guard before restart | P1 | Maintenance Lead | 2026-06-28 |
| Install + commission the interlocked feed-roll nip guard | P2 | Process Engineer | 2026-07-18 |

## 8. Assumptions, gaps & sign-off

- Access frequency for the feed-roll nip assumed "occasional (setting)" — confirm with the line
  supervisor.
- India site (if applicable): state return owed — `[GAP]` (resolve the state via `hse-india`; no
  national form number minted).
- Presence-sensing safety-function performance level (ISO 13849 PL) to be confirmed against the
  residual risk — `[GAP]`.
- **Regulatory basis:** OSHA 29 CFR 1910 Subpart O (1910.212 + 1910.219); ISO 12100 + ISO 14120;
  UK PUWER 1998 Regs 11–12; ISO 45001 §6.1.2 / §8.1.2.
- Review trigger: on machine change / on guard modification / annual — whichever is first.
- Decision-support only — a competent person must review before use.
