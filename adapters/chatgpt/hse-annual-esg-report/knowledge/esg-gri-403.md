<!-- KB-STD-ESG-GRI403 -->
# GRI 403 / SASB / ESRS S1 — OH&S disclosure index (disclosure→artifact map)

**Fragment ID:** `KB-STD-ESG-GRI403`
**What this is:** a copyright-safe **disclosure-code → location map** for the
occupational-health-&-safety disclosures across the three main ESG reporting
frameworks — GRI 403 (Occupational Health & Safety 2018), SASB (industry standards),
and ESRS S1 (Own Workforce, under the EU CSRD) — i.e. which OH&S metric each
framework asks for and where the organisation reports it.
**What this is NOT:** a reproduction of the framework's disclosure text or guidance.
Cite the disclosure codes and topic structure only (user holds the licensed/public
framework documents).

> Source: GRI 403:2018 (Occupational Health & Safety) · SASB industry standards · ESRS S1 (Own Workforce, CSRD) — disclosure-code structure · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (ESRS/CSRD adoption is still settling; refresh on review).

These frameworks turn HSE performance into **disclosable, comparable** sustainability
reporting. This fragment grounds the ESG / sustainability disclosure-index artifact:
a table mapping each required OH&S disclosure to where it is reported and the
underlying metric.

## Disclosure topic → framework code → what it grounds

| OH&S disclosure topic | Framework code (cite, don't paste) | Disclosure-index entry it grounds |
|---|---|---|
| OH&S management system | GRI 403-1 | management-system description + scope |
| Hazard ID, risk assessment, incident investigation | GRI 403-2 | the HIRA / investigation process |
| Occupational health services | GRI 403-3 | health-service provision |
| Worker participation & consultation | GRI 403-4 | consultation arrangements |
| Worker training on OH&S | GRI 403-5 | training programme |
| Worker health promotion | GRI 403-6 | health-promotion programme |
| Prevention/mitigation of OH&S impacts in business relationships | GRI 403-7 | contractor/supply-chain controls |
| Coverage of the OH&S management system | GRI 403-8 | workforce-coverage figures |
| **Work-related injuries** (rates: recordable, lost-time, fatalities, hours) | GRI 403-9 / SASB / ESRS S1 | the injury-rate table (figures from `incident_rates`) |
| **Work-related ill health** | GRI 403-10 / ESRS S1 | the ill-health figures |

## How the skill uses this fragment
- Grounds the ESG / sustainability OH&S disclosure index; the rate figures (TRIR /
  LTIFR / fatality rate, hours worked) are computed by `incident_rates`, never invented.
- Each required disclosure with no data is recorded as `[GAP]`, never fabricated.
- Cross-walks GRI ↔ SASB ↔ ESRS codes so one metric reports once to the right index.
