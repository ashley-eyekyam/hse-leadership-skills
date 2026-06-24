<!-- KB-STD-BIOSAFETY-BMBL-WHO -->
# Laboratory biosafety — BMBL biosafety levels + BSC classes + WHO LBM risk groups

**Fragment ID:** `KB-STD-BIOSAFETY-BMBL-WHO`
**What this is:** a copyright-safe **topic → artifact** structure map for
laboratory biosafety — the CDC/NIH Biosafety in Microbiological and Biomedical
Laboratories (BMBL, 6th ed.) biosafety levels BSL-1 to BSL-4 and biosafety-cabinet
(BSC) classes, the WHO Laboratory Biosafety Manual risk-group classification
(RG1–RG4) and risk-assessment approach, and a pointer to the NIH Guidelines for
recombinant/synthetic nucleic acids. It grounds a lab-biosafety-assessment skill in
the risk-group → containment-level decision.
**What this is NOT:** a reproduction of the manual text or the agent summary
statements. Cite the levels, the cabinet classes, the risk groups, and the
risk-assessment structure only — never paste the wording (user holds the
licensed/public source).

> Source: CDC/NIH BMBL 6th ed. (BSL-1–4 + BSC classes) + WHO Laboratory Biosafety Manual (risk groups RG1–RG4 + risk assessment) + NIH Guidelines (recombinant/synthetic NA, pointer) — structure map · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false. Jurisdiction: All.

## Topic → what it grounds

| Topic (cite, don't paste) | Focus | Artifact it grounds |
|---|---|---|
| WHO risk groups RG1–RG4 | Agent hazard classification by infectivity/severity/treatability | the agent risk-group determination |
| BMBL biosafety levels BSL-1–BSL-4 | Containment practices, facilities, safety equipment per level | the containment-level decision |
| Biosafety cabinet classes (I / II A–B / III) | Primary containment by aerosol-protection class | the BSC selection |
| WHO risk-assessment approach | Agent + procedure + competence → containment | the biosafety risk assessment method |
| NIH Guidelines (pointer) | Recombinant / synthetic nucleic-acid work oversight (IBC) | the rDNA oversight pointer |

## How the skill uses this fragment
- Grounds lab-biosafety-assessment in the risk-group → BSL containment decision
  (`KB-SNIP-BIOSAFETY-RA`); engineering controls (BSC, ventilation, containment)
  and procedures precede PPE (hierarchy of controls).
- Where the agent's risk group is unknown, the skill **does not invent** a risk
  group or BSL — it emits `[GAP]` and routes to a competent biosafety officer.
- Any incident/exposure detail is **de-identified** per the mandatory de-id block +
  the PHI extension.
- A missing element is recorded as `[GAP]`, never invented.
