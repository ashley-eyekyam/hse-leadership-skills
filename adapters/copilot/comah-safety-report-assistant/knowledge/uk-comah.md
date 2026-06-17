<!-- KB-REG-UK-COMAH -->
# United Kingdom — COMAH 2015 / Seveso III (statutory map)

**Fragment ID:** `KB-REG-UK-COMAH`
**What this is:** a copyright-safe **duty → safety-report-element map** for the
Control of Major Accident Hazards Regulations 2015 (COMAH, transposing Seveso III
Directive 2012/18/EU) — lower/upper-tier duties, the MAPP, the Safety Report
contents, and the emergency-plan duties.
**What this is NOT:** a reproduction of the regulation's text. Cite the regulation
/ Schedule numbers and the duty topics only — never paste the statutory wording.

> Source: COMAH 2015 / Seveso III Directive 2012/18/EU — citation map · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (statutory status + guidance drift; refresh on review).

COMAH governs UK/EU establishments holding dangerous substances above threshold
quantities, where the failure mode is a **major accident** (fire/explosion/toxic
release). It grounds `comah-safety-report-assistant` (assistive — it structures
the Safety Report argument; QRA/consequence modelling is done externally).

## Tier → duty → artifact it grounds

| Tier / topic | Duty | Safety-Report element it grounds |
|---|---|---|
| Lower-tier | Notify; MAPP; take all measures necessary | MAPP (Major Accident Prevention Policy) |
| Upper-tier | All lower-tier duties + a Safety Report | the full Safety Report (below) |
| MAPP | Major-accident-prevention policy + SMS | MAPP + Safety Management System description |
| Establishment description | Site, substances, surroundings | establishment & environs description |
| Hazard identification | Major-accident scenarios | scenario identification (PHA inputs from the facilitators) |
| Risk / ALARP | Demonstrate risks reduced ALARP | ALARP demonstration (consequence/likelihood) |
| Emergency planning | Internal (on-site) + external (off-site) plans | internal emergency plan |
| Notification thresholds | Named-substance / category thresholds | the lower/upper-tier determination |

## How the skill uses this fragment
- `comah-safety-report-assistant` structures each Safety Report element above and
  records the duty-holder's content — it **never** produces the Safety Report
  autonomously; QRA/consequence modelling and the ALARP numbers are external.
- A missing element is recorded as `[GAP]`, never invented.
