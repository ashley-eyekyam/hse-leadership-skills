<!-- KB-HAZ-HEALTHCARE -->
# Healthcare hazard library — sharps / IPC / WPV / biosafety (hazard→artifact map)

**Fragment ID:** `KB-HAZ-HEALTHCARE`
**What this is:** a copyright-safe **hazard library** for the healthcare sector — a
structured menu of the recurring physical, biological, and chemical hazards of care
settings, each routed to the assessment/control artifact it grounds. A seeding list
for HIRA / JSA / toolbox-talk intake, not a substitute for the site-specific assessment.
**What this is NOT:** a reproduction of any licensed guideline (WHO/CDC/HSE) text.
Cite the hazard category and the standard's number/topic only — never paste the
guidance wording.

> Source: healthcare-sector hazard taxonomy (sharps/IPC/WPV/biosafety) — hazard-category structure · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false.

This library seeds the hazard-identification step for healthcare tasks. The
psychosocial hazards (workplace violence as a stressor, emotional labour) route to
`KB-STD-HEALTHCARE-PSYCHOSOCIAL` / `KB-STD-ISO45003`; the physical/biological
hazards below ground the risk assessment and the hierarchy-of-controls selection.

## Hazard → typical controls (hierarchy-of-controls framing) → artifact

| Hazard category | Examples | Higher-order controls it grounds | Artifact |
|---|---|---|---|
| **Sharps / needlestick** | needles, scalpels, lancets | engineered safety-sharps (elimination/substitution), sharps bins, safe-disposal procedure | sharps-injury control plan |
| **Infection prevention & control (IPC)** | bioaerosols, contact/droplet/airborne transmission | ventilation/isolation (engineering), PPE (last), hand-hygiene procedure | IPC risk assessment |
| **Workplace violence (WPV)** | patient/visitor aggression | layout/security design, staffing, de-escalation training; reporting | WPV risk assessment (see also psychosocial cross-list) |
| **Biosafety / pathogens** | clinical specimens, lab cultures, containment levels | containment-level design, biosafety cabinets, exposure procedure | biosafety assessment |
| **Hazardous drugs / chemicals** | cytotoxics, anaesthetic gases, disinfectants | closed-system transfer, LEV, scavenging; SDS-driven controls | chemical-exposure assessment |
| **Manual handling / patient handling** | repositioning, transfers | hoists/aids (engineering), task design | ergonomics assessment (routes to `KB-STD-GHS-ERGO`) |
| **Radiation** | imaging, radiotherapy sources | shielding, distance, time; dosimetry | radiation safety record |

## How the skill uses this fragment
- Seeds healthcare HIRA / JSA / toolbox-talk hazard identification; every listed
  hazard is confirmed against the actual task/site — listed ≠ present.
- Controls are ranked via `KB-SNIP-HOC` (no PPE-only treatment without justification).
- A hazard with no site-specific control captured is recorded as `[GAP]`, never invented.
