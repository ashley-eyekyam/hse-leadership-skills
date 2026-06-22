<!-- CANDIDATE golden output (D-09 / CONV-5). Generated in Phase 12 from eval case 1's
     scenario. Status: candidate, pending owner review + competent-person sign-off. -->

# Emergency Response Plan — Plant 4 Solvent-Storage Warehouse

*Scenario-keyed ERP grounded in ISO 45001 clause 8.2 (emergency preparedness & response).
UK baseline: Regulatory Reform (Fire Safety) Order 2005 art. 15; DSEAR 2002 (flammable
atmospheres). Classification: Internal — competent-person review required. Decision-support
only.*

De-identification pass: identifiers detected and pseudonymised before drafting; the
call-out tree below uses role + duty-phone labels; the internal master contact list (the
re-identification key) is held separately and is NOT part of this distributed document.

## 1. Site & occupancy

Plant 4 solvent-storage warehouse: drummed flammable-solvent store + decant bay. Peak
occupancy 45 staff across 2 shifts (day 30 / night 15), plus up to 4 visiting drivers.
The plan accounts for staff, contractors and visitors who may be on site during each
scenario.

| Metric | Value |
|---|---|
| Site occupancy (peak) | 45 + 4 visitors |
| Credible scenarios planned | 2 |
| Named muster points | 2 (with roll-call) |

## 2. Credible emergency scenarios

- **Fire/explosion** — ignition of drummed flammable solvent; worst-credible case is a
  fork-truck ignition source in the decant bay during a spill.
- **Chemical/gas release** — solvent vapour build-up from a leaking drum or decant spill
  (vapour heavier than air, pools at low level).

## 3. Prevention controls (hierarchy — prevention BEFORE response)

| Tier | Control | Owner |
|---|---|---|
| Elimination/Reduction | Cap the maximum drummed quantity in the decant bay to a one-shift working stock; bulk store held in the segregated outer compound | Site Manager |
| Substitution | Replace the diesel fork-truck in the store with an ATEX-rated electric unit (removes the in-store ignition source) | Engineering Lead |
| Engineering | Flammable-vapour detection interlocked to forced extraction + drench/foam suppression; bunded decant bay | Engineering Lead |
| Administrative | Hot-work permit + housekeeping + no-ignition-source rule in the store; spill kit at the decant bay | HSE Lead |

Prevention precedes the response procedures below — the plan does not rely on reacting to
a fire that engineering and substitution controls should prevent. (HoC applied via
`controls`; `KB-SNIP-HOC`.)

## 4. Scenario response procedures (scenario-keyed)

**Fire/explosion**
1. Detection/alarm — vapour detector or break-glass raises the continuous evacuation
   alarm; auto-extraction + suppression initiate.
2. Immediate actions — Incident Controller role confirms; isolate electrical + solvent
   supply at isolation point ISO-1; no re-entry.
3. Escalation/call-out — activate the call-out tree (§5); call 999, state "flammable
   solvent fire, drummed store".
4. Evacuation — route E-1 (main) / E-2 (rear) to muster; account for the decant-bay crew
   first.
5. Muster + roll-call (§6); all-clear only by the fire service + a competent person.

**Chemical/gas release**
1. Detection — vapour alarm or visual/odour; treat as flammable + harmful.
2. Immediate actions — upwind evacuation; isolate the leaking drum if safe via ISO-2;
   start forced extraction.
3. External notification — fire service (HazMat), with SDS handed at the gatehouse.
4. Muster + roll-call; no re-entry until atmosphere cleared and a competent person signs
   off.

## 5. Call-out tree & roles (with named deputies)

| Role | Holder (role label) | Deputy (role label) | Duty phone |
|---|---|---|---|
| Incident Controller | Duty Manager | Shift Supervisor | Duty-phone 1 |
| Fire Warden — Decant Bay | Warden A | Warden A-deputy | Duty-phone 2 |
| Fire Warden — Store | Warden B | Warden B-deputy | Duty-phone 3 |
| First-aid Lead | First-aider 1 | First-aider 2 | Duty-phone 4 |
| Responder Liaison / Comms | Comms Officer | Comms deputy | Duty-phone 5 |

Every role has a named deputy across both shifts. Role + duty-phone labels in this
circulated copy; the real personal contacts are in the separate internal master list.

## 6. Muster & evacuation

Primary muster point: **the north car park** (clear of the prevailing-wind vapour path);
secondary: **the east gate assembly area**. Evacuation routes E-1 (main door) and E-2
(rear fire exit). Roll-call against the gate access register; visiting drivers escorted by
the Responder Liaison; one PRM (mobility) provision via the refuge at stair core S-1.

## 7. External-responder integration

| Responder | Access route | Isolation / hazard point | Interface / mutual aid |
|---|---|---|---|
| Fire service (HazMat) | West gate, hardstanding for appliances | ISO-1 electrical, ISO-2 solvent supply | Site plan + SDS + keys at gatehouse |
| Ambulance | West gate to first-aid point FA-1 | — | Meet at the north car park |

## 8. Drill schedule (dated)

| Drill | Scenario | Frequency (source + year) | Owner | Next date |
|---|---|---|---|---|
| Full evacuation drill | Fire/explosion | Quarterly for a higher-hazard flammable-store site *(per KB-DATA-DRILL-FREQ — confirm source+year at use time; [GAP] if unresolved)* | HSE Lead | 15 Sep 2026 |
| Chemical-release table-top + isolation exercise | Chemical/gas release | Semi-annual *(per KB-DATA-DRILL-FREQ)* | Engineering Lead | 01 Aug 2026 |
| Call-out-tree contactability test | All | Monthly | Duty Manager | 05 Jul 2026 |

Each drill is debriefed; corrective actions are logged with a named owner + date
(`smart_actions`). Quote the `KB-DATA-DRILL-FREQ` source+year at use time — never a bare
number.

## 9. Review & sign-off

ERP grounded in ISO 45001 clause 8.2 (and RRFSO 2005 art. 15 / DSEAR 2002, UK). SME review
by the **Emergency Planning Officer** persona completed (prevention-before-response, every
role deputised, muster named, drills dated, capability proven). This is decision-support
only and **must be reviewed and signed off by a competent person before reliance**.

---

**For continuity of critical activities AFTER the emergency is controlled** (recovery of
operations, RTO / RPO / MTPD), see the **`business-continuity-plan`** skill — the ERP plans
the immediate response, the BCP plans the recovery. The two are complementary and not
merged.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
