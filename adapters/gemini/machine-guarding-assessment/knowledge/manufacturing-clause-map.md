<!-- KB-SNIP-MANUFACTURING-CLAUSE-MAP -->
# hse-manufacturing clause cross-walk — ISO 45001 6.1.2 + ISO 12100 three-step → owning skill

**Fragment ID:** `KB-SNIP-MANUFACTURING-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** manufacturing cross-walk (D-04): ISO 45001:2018 clause 6.1.2
(hazard identification & risk assessment) + the ISO 12100 three-step method (inherent
safe design → safeguarding → information) mapped to the four `hse-manufacturing` skills
(guarding / ergonomics / noise / PPE). Every manufacturing skill's `kb-selection`
references it so the bundle routes consistently. Referenced by every hse-manufacturing
skill's kb-selection; single source, never duplicated.

> Source: ISO 45001:2018 (clause 6.1.2) + ISO 12100:2010 (three-step method) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the manufacturing axis → owning skill

| Axis | Manufacturing hazard | Owning hse-manufacturing skill |
|---|---|---|
| ISO 45001 **6.1.2** hazard-id loop + ISO 12100 **three-step method** | Machine / mechanical hazards | `machine-guarding-assessment` (MFG-01) |
| ISO 45001 **6.1.2** + ISO 11228 handling method | Musculoskeletal / manual-handling (MSD) | `ergonomics-assessment` (MFG-02) |
| ISO 45001 **6.1.2** + the noise hierarchy | Noise exposure / hearing loss | `noise-exposure-health-surveillance` (MFG-03) |
| ISO 45001 **6.1.2** + the controls-first gate | Residual body-region hazards (PPE) | `ppe-matrix` (MFG-04) |

## The three-step spine (every skill applies it)
Each manufacturing skill applies ISO 12100's order — **design out** the hazard first,
**safeguard** the residual (guard / aid / enclosure), **inform** last. PPE / hearing
protection / training is always the residual-only, documented last line
(`KB-SNIP-HOC`), never the headline control.

## Adjacent pointers (not axis rows)
- **US grounding:** `KB-REG-OSHA1910-O` (guarding), `KB-REG-OSHA1910-95` (noise),
  `KB-REG-OSHA1910-I` (PPE).
- **LOTO / energy isolation** reuses the built `KB-REG-LOTO` (no separate fragment).
- **India** factory content defers to the `hse-india` engine (state detection
  mandatory; no national form numbers minted).

## How every manufacturing skill uses this fragment
Each skill references `KB-SNIP-MANUFACTURING-CLAUSE-MAP` in its `kb-selection` so the
bundle presents one consistent hazard → skill map and the shared three-step spine. No
skill restates the cross-walk in its own body (anti-drift).
