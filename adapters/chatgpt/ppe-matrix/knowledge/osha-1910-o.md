<!-- KB-REG-OSHA1910-O -->
# United States — OSHA 29 CFR 1910 Subpart O (Machinery & Machine Guarding map)

**Fragment ID:** `KB-REG-OSHA1910-O`
**What this is:** a copyright-safe **hazard → standard → control map** for OSHA's
machine-guarding standards (29 CFR 1910 Subpart O) — 1910.212 general requirements for
all machines (guarding the point of operation, in-running nip points, rotating parts,
flying chips/sparks; guards affixed and secure; fixed machines anchored) and 1910.219
mechanical power-transmission apparatus, plus the machine-specific sections.
**What this is NOT:** a reproduction of 29 CFR 1910 text. Cite the CFR section numbers
and the duty topics only — never paste the regulation wording.

> Source: OSHA 29 CFR 1910 Subpart O (Machinery and Machine Guarding) — citation map · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false (stable CFR structure; refresh on review).

29 CFR 1910 Subpart O is the US general-industry machine-guarding grounding. It is
shared by the machine-guarding skill (MFG-01) and the machine leg of the PPE skill
(MFG-04), applied through the hierarchy of controls.

## Hazard / topic → section → control expectation it grounds

| Hazard / topic | Section | Control expectation it grounds |
|---|---|---|
| Point of operation, nip points, rotating parts, flying chips/sparks | 1910.212(a) | guard the hazard at the point of operation; guards affixed and secure |
| Anchoring fixed machinery | 1910.212(b) | machines designed for a fixed location are securely anchored |
| Point-of-operation guarding | 1910.212(a)(3) | the point of operation is guarded so no body part enters the danger zone during operation |
| Mechanical power-transmission apparatus | 1910.219 | belts, gears, pulleys, chains, shafts, projecting set-screws/keys guarded |
| Machine-specific sections | 1910.213–.219 (woodworking, abrasive wheels, mechanical/hydraulic presses, etc.) | the machine-specific guarding requirement for the named machine |

## How the skill uses this fragment
- `machine-guarding-assessment` (MFG-01) resolves the machine hazard, cites the
  governing 1910 section, and grounds an **engineering-control-led** guard via
  `KB-STD-ISO12100-14120` + `KB-SNIP-GUARD-SELECTION`.
- `ppe-matrix` (MFG-04) cites this for the machine-hazard leg where PPE is the
  residual-only control after guarding.
- A missing input (no machine type, no access frequency) is a `[GAP]`; "operators to be
  careful" is never the headline control (`KB-SNIP-HOC`).
