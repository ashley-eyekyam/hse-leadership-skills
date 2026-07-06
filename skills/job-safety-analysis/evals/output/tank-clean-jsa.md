<!-- LOCKED fixture — owner-LOCKED at the SW4 19-05 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Job Safety Analysis (JSA / JHA)
## Cleaning & Internal Inspection — Tank T‑402

| Field | Detail |
|---|---|
| **Task** | Confined‑space cleaning and internal inspection of storage tank **T‑402** |
| **Asset / Location** | Tank T‑402, **Plant 3**, Maharashtra, India |
| **JSA Ref / Rev** | JSA‑T402‑CSE / Rev 0 |
| **Date prepared** | 6 July 2026 |
| **Prepared by (role)** | Site HSE Manager |
| **Jurisdiction** | India — **Maharashtra** (Factories Act 1948 + Maharashtra Factories Rules 1963; OSH Code 2020 transition flagged) |
| **Personnel** | Own workers **+** confined‑space‑permitted contractor crew, under **one** entry permit and **one** Confined Space Supervisor |
| **Key equipment / materials** | Cherry‑picker (MEWP) for top‑manway access · multi‑gas detector (O₂/LEL/CO/H₂S + PID‑VOC) · cleaning **solvent** |
| **Review trigger** | Before each entry; on any change of substance, method, crew, plant condition, or atmosphere; after any incident/near‑miss; on permit expiry |

> **Classification: HIGH‑HAZARD CONFINED SPACE ENTRY.** This is a permit‑controlled entry into a space that has contained flammable/toxic solvent. **No entry may occur until Steps 1–3 are complete, the atmosphere is proven acceptable, and a rescue capability is on station.**

---

### Risk matrix (org 5×5)

**Score = Likelihood (L) × Severity (S).**

| L | Likelihood | | S | Severity |
|---|---|---|---|---|
| 1 | Rare | | 1 | Negligible (first aid) |
| 2 | Unlikely | | 2 | Minor (medical treatment) |
| 3 | Possible | | 3 | Moderate (lost‑time, reversible) |
| 4 | Likely | | 4 | Major (permanent disabling injury) |
| 5 | Almost certain | | 5 | Catastrophic (fatality / multiple) |

| Band | Score | Action |
|---|---|---|
| **Low** | 1–4 | Acceptable — manage by routine controls |
| **Medium** | 5–9 | Tolerable — defined controls required |
| **High** | 10–15 | Unacceptable without additional controls; management sign‑off |
| **Extreme** | 16–25 | **STOP** — do not proceed until reduced |

*HoC tier tags:* **(E)** Elimination · **(S)** Substitution · **(EC)** Engineering · **(A)** Administrative · **(P)** PPE. Controls are ranked highest‑order first; **no step is treated by PPE alone.**

---

### Interfaces that gate this job (establish before Step 1)

**Permits (all live simultaneously, cross‑checked for conflict):**
- **Confined Space Entry (CSE) permit** — primary; carries the gas‑test certificate and entrant/attendant register. *Issuer: Permit Authority (Occupier’s authorised person).*
- **LOTO / isolation certificate** — verified against current P&ID. *Owner: Isolation Authority.*
- **Line‑breaking permit** — for draining/blinding residual solvent lines. *Owner: Permit Authority.*
- **Work‑at‑height permit** — MEWP access to top manway. *Owner: Contractor Site Supervisor.*
- **Hot‑work permit — PROHIBITED concurrently.** No ignition source, no hot work while a flammable atmosphere is credible. *Enforced by: Permit Authority.*

**Gas‑test acceptance criteria** (test **O₂ → flammable → toxic**, at top/mid/bottom depths via aspirated probe *before* breaking the plane; log each level on the CSE permit):
- **Oxygen** 19.5 %–23.5 % · **Flammable** ≤10 % LEL (target <5 %) · **Toxic** solvent‑vapour < OEL (SDS TWA / Factories Act Second Schedule permissible limit); **H₂S** <10 ppm; **CO** <25 ppm. *Owner: Authorised Gas Tester.*

**Rescue & emergency arrangements (must be on station before entry):**
- Trained confined‑space **rescue team on standby** with **non‑entry retrieval** rigged (tripod/davit + winch), **airline BA / SCBA + escape sets**, IS emergency comms, O₂ resuscitation and first‑aider. Rescue plan **rehearsed**; local emergency services notified. **No unplanned rescuer entry** — the attendant never enters. *Owner: Rescue Team Lead.*

**Contractor management:** confined‑space competency + confined‑space medical‑fitness certificates verified; contractor crew inducted to the site permit system and placed **under the site Confined Space Supervisor**. *Owner: Contractor Site Supervisor / Site HSE Manager.*

---

## Per‑step analysis

### Step 1 — Isolate & lockout

| Hazard (energy source) | Exposed | Initial L×S (band) | Controls — HoC tier & role owner | Residual L×S (band) |
|---|---|---|---|---|
| Inadvertent energisation of agitator / feed & discharge pumps / actuated valves (mechanical–electrical–kinetic) | Isolation crew; later entrants | **4×5 = 20 (Extreme)** | (EC) Positive electrical isolation at MCC, fuses out, drive physically disconnected; **insert blinds/spades** on all process lines (not valve‑closed only) — *Isolation Authority*<br>(A) Personal locks + group lock box; isolation cert cross‑checked to P&ID; **try‑test** to prove dead — *Confined Space Supervisor* | **1×5 = 5 (Medium)** |
| Stored‑energy / residual‑pressure & chemical release at line break (N₂ blanket, product, solvent) (pressure–chemical) | Isolation crew | **4×4 = 16 (Extreme)** | (EC) Drain & depressurise to safe route, vent N₂ to scrubber, **double‑block‑and‑bleed**, confirm zero pressure at gauge — *Process/Isolation Authority*<br>(A) Line‑break permit; crack furthest flange first, controlled release — *Permit Authority*<br>(P) Chemical splash suit, face shield, gauntlets — *Contractor Site Supervisor* | **1×4 = 4 (Low)** |
| Backflow of solvent / steam / N₂ from connected lines during later work (chemical–thermal) | Entrants | **3×5 = 15 (High)** | (EC) Physical blinds on every connected line; single point of proven isolation — *Isolation Authority*<br>(A) Isolation register signed and left in place until permit close — *Confined Space Supervisor* | **1×5 = 5 (Medium)** |
| Manual handling / slips inserting spades on spilled product | Fitters | **3×2 = 6 (Medium)** | (EC) Mechanical aids for heavy spades; bund/absorb spill — *Contractor Site Supervisor*<br>(A) Housekeeping, task briefing — *Contractor Site Supervisor*<br>(P) Anti‑slip footwear, gloves — *Entrant* | **1×2 = 2 (Low)** |

---

### Step 2 — Purge / ventilate

| Hazard (energy source) | Exposed | Initial L×S (band) | Controls — HoC tier & role owner | Residual L×S (band) |
|---|---|---|---|---|
| Flammable solvent‑vapour atmosphere ignites (chemical–thermal → flash fire/explosion) | All personnel nearby | **4×5 = 20 (Extreme)** | (S) Water/steam‑flush residues first, then inert‑purge below LEL, then air‑purge — *Process Engineer*<br>(EC) ATEX/IS forced‑air eductor; **bond & earth** tank and equipment; classify zone, clear ignition sources — *Electrical Authority / HSE Manager*<br>(A) Hot work prohibited; **continuous LEL monitoring** during purge — *Authorised Gas Tester* | **1×5 = 5 (Medium)** |
| Oxygen deficiency from nitrogen purge / displacement (asphyxiation) | Anyone at manway; entrants | **4×5 = 20 (Extreme)** | (EC) **Air‑purge after inert phase** to restore O₂ 19.5–23.5 %; ventilation runs continuously through entry — *Confined Space Supervisor*<br>(A) **No entry during N₂ phase**; continuous O₂ monitoring; “never enter on nitrogen” rule — *Authorised Gas Tester* | **1×5 = 5 (Medium)** |
| Ineffective purge leaving vapour pockets / dead zones (chemical) | Later entrants | **3×5 = 15 (High)** | (EC) Ventilation positioned to sweep low points; forced through/across, not spot — *Confined Space Supervisor*<br>(A) Verify clearance by multi‑depth test (Step 3) before acceptance — *Authorised Gas Tester* | **1×5 = 5 (Medium)** |
| Toxic exhaust vapour to surroundings / MEWP operator at top (chemical) | Bystanders; MEWP operator | **3×3 = 9 (Medium)** | (EC) Exhaust routed away from work areas / to scrubber; exclusion zone — *HSE Manager*<br>(A) Bystander control, wind‑direction check — *Contractor Site Supervisor* | **1×3 = 3 (Low)** |

---

### Step 3 — Gas‑test

| Hazard (energy source) | Exposed | Initial L×S (band) | Controls — HoC tier & role owner | Residual L×S (band) |
|---|---|---|---|---|
| False “safe” reading from un‑calibrated / un‑bump‑tested detector (instrument failure) | Entrants | **3×5 = 15 (High)** | (EC) Calibrated multi‑gas detector (O₂/LEL/CO/H₂S + PID‑VOC); **bump‑test & zero before each use**; alarm set‑points configured — *Authorised Gas Tester*<br>(A) Current calibration certificate; backup second instrument; defined acceptance criteria — *Occupational Hygienist* | **1×5 = 5 (Medium)** |
| Unrepresentative sample — surface‑only test misses stratified/heavy solvent vapour at depth (chemical) | Entrants | **4×5 = 20 (Extreme)** | (EC) **Aspirated remote probe sampled at top, mid, bottom and corners before breaking the plane** — *Authorised Gas Tester*<br>(A) Each level’s readings logged on CSE permit; competent gas tester only — *Confined Space Supervisor* | **1×5 = 5 (Medium)** |
| Atmosphere changes during occupancy — desorption from sludge, disturbed residue re‑releases vapour (chemical) | Entrants during work | **4×5 = 20 (Extreme)** | (EC) **Continuous personal + area monitoring** with audible alarm; ventilation maintained throughout — *Authorised Gas Tester*<br>(A) Re‑test at set intervals and after every break; **auto‑evacuate on alarm** — *Confined Space Supervisor* | **1×5 = 5 (Medium)** |

---

### Step 4 — Enter

| Hazard (energy source) | Exposed | Initial L×S (band) | Controls — HoC tier & role owner | Residual L×S (band) |
|---|---|---|---|---|
| Fall from / overturn of cherry‑picker accessing top manway (gravity–kinetic) | Entrants; MEWP operator | **3×4 = 12 (High)** | (E) Use fixed platform/stair to manway where one exists, in preference to the MEWP — *Confined Space Supervisor*<br>(EC) MEWP on firm level ground, outriggers deployed, exclusion zone, wind‑speed limit, guardrails — *MEWP Operator*<br>(A) MEWP pre‑use inspection + rescue‑from‑height plan; licensed operator — *Contractor Site Supervisor*<br>(P) Full‑body harness + short restraint lanyard to MEWP anchor; helmet w/ chinstrap — *Entrant* | **1×4 = 4 (Low)** |
| Fall into tank through open manway on entry (gravity) | Entrant | **3×5 = 15 (High)** | (EC) **Tripod/davit + winch fall‑arrest/retrieval rigged at manway**; controlled descent — *Rescue Team Lead*<br>(A) Entry only after atmosphere accepted and permit authorises — *Permit Authority*<br>(P) Full‑body harness on retrieval line — *Entrant* | **1×5 = 5 (Medium)** |
| Engulfment/entrapment in residual sludge; entrant overcome with delayed rescue (chemical–kinetic) | Entrant | **3×5 = 15 (High)** | (E) **Remove bulk sludge externally (vacuum truck) before entry** — *Confined Space Supervisor*<br>(EC) Non‑entry retrieval system; airline BA/SCBA where atmosphere not guaranteed — *Rescue Team Lead*<br>(A) Dedicated trained **attendant at all times**; rescue team on standby; rehearsed plan; entrant tally board — *Rescue Team Lead* | **1×5 = 5 (Medium)** |
| Loss of communication entrant↔attendant | Entrant | **3×4 = 12 (High)** | (EC) IS two‑way radio / hard‑wired comms; rope‑tug signals as backup — *Standby Person*<br>(A) Continuous attendant; comms check at set intervals — *Confined Space Supervisor* | **1×4 = 4 (Low)** |
| Manual handling / entrapment on internals through restricted opening | Entrant | **3×3 = 9 (Medium)** | (EC) Clear opening, padded edges, controlled sequence — *Confined Space Supervisor*<br>(A) Body‑size/fitness check, task briefing — *Contractor Site Supervisor* | **1×3 = 3 (Low)** |

---

### Step 5 — Clean

| Hazard (energy source) | Exposed | Initial L×S (band) | Controls — HoC tier & role owner | Residual L×S (band) |
|---|---|---|---|---|
| Solvent exposure — inhalation of vapour, dermal/eye contact in enclosed space (chemical) | Entrant | **4×4 = 16 (Extreme)** | (S) **Substitute a higher‑flashpoint / water‑based cleaner** where efficacy allows — *Occupational Hygienist / Process Engineer*<br>(EC) Continuous forced ventilation / local exhaust; long‑handled tools; minimise quantity — *Confined Space Supervisor*<br>(A) SDS exposure controls; limit exposure time / rotate; VOC monitoring vs OEL — *Occupational Hygienist*<br>(P) **Supplied‑air / airline BA** (not cartridge) + chemical suit & gloves — *Entrant* | **1×4 = 4 (Low)** |
| Flammable atmosphere from solvent evaporation during cleaning (chemical–thermal → flash fire) | Entrant | **4×5 = 20 (Extreme)** | (S) Higher‑flashpoint/water‑based cleaner removes the flammable source — *Process Engineer*<br>(EC) Ventilation holds LEL <10 %; bonding/earthing; ATEX/IS equipment only — *HSE Manager*<br>(A) Continuous LEL monitoring, **auto‑evacuate at 10 % LEL**; no hot work; controlled solvent volume — *Authorised Gas Tester*<br>(P) Anti‑static, natural‑fibre clothing — *Entrant* | **1×5 = 5 (Medium)** |
| Static discharge from jetting/cleaning ignites vapour (electrical–thermal) | Entrant | **3×5 = 15 (High)** | (EC) **Bond & earth** tank, MEWP, jetting gear and drums; conductive hoses — *Electrical Authority*<br>(A) Earthing verified before start — *HSE Manager* | **1×5 = 5 (Medium)** |
| Non‑IS lighting/tools inside tank (electrical → ignition/shock) | Entrant | **3×5 = 15 (High)** | (EC) **24 V ATEX/IS low‑voltage lighting** and IS tools; ELV via RCD; no mains inside (Factories Act §36A) — *Electrical Authority* | **1×4 = 4 (Low)** |
| Heat / ergonomic stress & fatigue in hot, restricted, PPE‑laden space | Entrant | **3×3 = 9 (Medium)** | (EC) Ventilation/cooling; scheduled work‑rest cycles — *Confined Space Supervisor*<br>(A) Hydration, stay‑time limits, physiological watch by attendant — *First Aider* | **1×2 = 2 (Low)** |
| Slips on wet surfaces / high‑pressure‑jet injury | Entrant | **3×3 = 9 (Medium)** | (EC) Drainage, anti‑slip footing, jet trigger guards — *Confined Space Supervisor*<br>(A) Jetting technique briefing — *Contractor Site Supervisor*<br>(P) Cut/impact gloves, eye protection — *Entrant* | **1×3 = 3 (Low)** |

---

### Step 6 — Exit & restore

| Hazard (energy source) | Exposed | Initial L×S (band) | Controls — HoC tier & role owner | Residual L×S (band) |
|---|---|---|---|---|
| **Premature re‑energisation / de‑isolation while personnel or tools still inside** (mechanical–electrical–chemical) | Entrant; fitters | **4×5 = 20 (Extreme)** | (EC) De‑isolate **only** by reverse‑isolation procedure via group lock box; each personal lock removed by its owner — *Isolation Authority*<br>(A) **Permit close‑out signed confirming all personnel out + tools removed BEFORE de‑isolation**; headcount reconciled — *Confined Space Supervisor / Permit Authority* | **1×5 = 5 (Medium)** |
| Entrant left inside — miscount / incomplete personnel accounting | Entrant | **3×5 = 15 (High)** | (EC) Entry/exit **tally board**; permit cannot close until count = 0 — *Standby Person*<br>(A) Attendant confirms all entrants out and signs — *Confined Space Supervisor* | **1×5 = 5 (Medium)** |
| Fall from height on MEWP exit; fatigue‑induced misstep (gravity) | Entrant | **3×4 = 12 (High)** | (EC) Retrieval system for controlled exit; MEWP guardrails — *MEWP Operator*<br>(P) Harness + restraint lanyard — *Entrant* | **1×4 = 4 (Low)** |
| Waste solvent / contaminated rags handling & environmental release (chemical) | Workers; environment | **3×3 = 9 (Medium)** | (EC) Collect waste solvent in labelled closed containers to **MPCB‑authorised** hazardous‑waste handler (Hazardous & Other Wastes Rules 2016) — *HSE Manager*<br>(A) Spill kit ready; segregate contaminated rags — *Contractor Site Supervisor* | **1×2 = 2 (Low)** |
| Reinstatement error — blind left in / lines mis‑reconnected → later process upset (mechanical–chemical) | Downstream operators | **2×4 = 8 (Medium)** | (EC) Reinstatement to **P&ID checklist**; blind/spade removal tallied — *Isolation Authority*<br>(A) Independent verification before restart — *Process Engineer* | **1×3 = 3 (Low)** |

---

## Consolidated SMART action register

*Action‑type controls to be completed before/for this entry. Every action has a named role owner, a due date, a measure, and the step/hazard it closes. Today: 6 July 2026.*

| # | SMART action (measure) | Owner (role) | Due | Step → hazard |
|---|---|---|---|---|
| A1 | Calibrate & bump‑test the multi‑gas detector, confirm calibration certificate current, configure alarm set‑points; ready a backup unit | Authorised Gas Tester | **8 July 2026** | 3 → false reading |
| A2 | Verify contractor confined‑space competency **and** confined‑space medical‑fitness certificates for every entrant; induct crew to site permit system | Contractor Site Supervisor / Site HSE Manager | **10 July 2026** | 4 → all CSE |
| A3 | Confirm & rehearse the confined‑space rescue plan; rig tripod/davit + winch; check availability of airline BA/SCBA + escape sets | Rescue Team Lead | **12 July 2026** | 4 → engulfment/rescue |
| A4 | Substitution study — evaluate higher‑flashpoint / water‑based cleaner vs current solvent; record decision & residual‑risk basis | Occupational Hygienist / Process Engineer | **13 July 2026** | 5 → solvent exposure & flammable |
| A5 | Confirm MEWP current inspection certificate + operator licence; complete ground/stability assessment for cherry‑picker set‑up | MEWP Operator / Contractor Site Supervisor | **13 July 2026** | 4 → fall from height |
| A6 | Arrange MPCB‑authorised hazardous‑waste disposal route + labelled closed containers for waste solvent | Site HSE Manager | **11 July 2026** | 6 → waste release |
| A7 | Prepare isolation certificate cross‑checked to current P&ID; install blinds/spades and verify positive isolation (try‑test) | Isolation Authority | **14 July 2026** | 1 → energisation/backflow |
| A8 | Vacuum‑truck removal of bulk sludge from T‑402 before any entry | Confined Space Supervisor | **14 July 2026** (pre‑entry) | 4 → engulfment |
| A9 | Confirm bonding/earthing of tank, MEWP, jetting gear & drums; issue 24 V ATEX/IS lighting and IS tools | Electrical Authority | **14 July 2026** | 5 → static & electrical |
| A10 | **[VERIFY]** Confirm the applicable Maharashtra Factories Rules 1963 permit‑to‑work / PPE rule references and OSH Code 2020 applicability with a competent person | Factory Manager (competent person) | **10 July 2026** | Regulatory basis |

---

## Confined‑space entry controls — summary (must all hold at the moment of entry)

- Positive isolation + LOTO proven (try‑test) — **A7** ✔ before entry
- Atmosphere purged, ventilated, and proven at multiple depths within acceptance criteria — Steps 2–3 ✔
- Continuous atmospheric monitoring with auto‑evacuate on alarm — Step 3 ✔
- Live CSE permit + line‑break + work‑at‑height permits; **hot work excluded** — Interfaces ✔
- Dedicated attendant + reconciled tally board; entrant count controlled — Steps 4 & 6 ✔
- Non‑entry retrieval rigged; rescue team on standby; airline BA available — **A3** ✔
- Supplied‑air respiratory protection for cleaning; IS/ATEX equipment only — Step 5 ✔
- Contractor competency & medical fitness verified; single supervisor of record — **A2** ✔

---

## Regulatory basis (India — Maharashtra)

- **Factories Act 1948 — §36** (precautions against dangerous fumes/gases; no entry to confined space until tested safe or BA worn) and **§36A** (no portable light >24 V and no naked flame in confined spaces unless flameproof); **§21/§22** (guarding / work on machinery in motion — supports isolation); **§87** (dangerous operations) and **Second Schedule** (permissible exposure limits) inform the gas‑test toxic criteria.
- **Maharashtra Factories Rules 1963** — the applicable **state** rules for permit‑to‑work, confined‑space precautions and PPE. Exact rule numbers to be confirmed by the competent person (**A10**) — recorded **[VERIFY]**, not assumed. Statutory notifications, where triggered, use the **Maharashtra state form**, not a national form number.
- **OSH Code 2020** (Occupational Safety, Health and Working Conditions Code) — transition flagged; confirm current commencement/applicability before relying on it (**A10**).
- **Hazardous & Other Wastes (Management & Transboundary Movement) Rules 2016** — waste solvent to an MPCB‑authorised handler (**A6**).

---

## Sign‑off & acceptance (role‑based — to be signed on the day of work)

| Role | Responsibility affirmed | Name/Sign | Date |
|---|---|---|---|
| Permit Authority (Occupier’s authorised person) | Permit issued; isolations & atmosphere verified | ________ | ____ |
| Confined Space Supervisor | Method, controls, attendant & tally in place | ________ | ____ |
| Authorised Gas Tester | Detector calibrated; atmosphere within criteria | ________ | ____ |
| Isolation Authority | Positive isolation + LOTO proven | ________ | ____ |
| Rescue Team Lead | Rescue capability on station & rehearsed | ________ | ____ |
| Contractor Site Supervisor | Crew competent, medically fit, inducted | ________ | ____ |
| Entrant(s) | Briefed; understand hazards, controls, evacuation | ________ | ____ |
| Site HSE Manager | JSA reviewed; SMART actions tracked to closure | ________ | ____ |

---

> **Decision‑support notice.** This JSA is decision‑support only. It is **not** a permit, not legal advice, and **not** a substitute for review and sign‑off by a **competent person** familiar with tank T‑402, Plant 3 and Maharashtra statutory requirements. It must be verified against the current P&ID, the solvent’s Safety Data Sheet, plant condition on the day, and the applicable Maharashtra Factories Rules before any work proceeds. Items marked **[VERIFY]** require confirmation before reliance. Risk scores use the org 5×5 (L×S) and reflect the stated assumptions; re‑score if conditions differ.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
