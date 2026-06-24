<!-- KB-DATA-ROAD-SAFETY-INDICATORS -->
# Road-safety leading/lagging indicators — ISO 39001 RTS factors (the single home)

**Fragment ID:** `KB-DATA-ROAD-SAFETY-INDICATORS`
**What this is:** the **single home** of road-safety leading/lagging KPIs (D-01), consumed by the
`leading-lagging-kpi-framework` road-safety EXTEND branch (LEAD-06). The five spec indicators map to
**ISO 39001:2012** Road Traffic Safety (RTS) performance factors + telematics practice. **LEAD-06 owns
the indicator; LOG-01 owns the engine** — Phase-16 logistics skills cross-reference this fragment, they
do not re-build it.
**What this is NOT:** a fatigue/hours-of-service calculator. Driver-hours compliance **cross-references**
SUB-03 fatigue-index and FMCSA HOS / EU drivers' hours but **does NOT compute** them here. Cited to the
standard.

> Source: ISO 39001:2012 (Road Traffic Safety Management Systems) RTS performance factors · telematics practice (over-speed / harsh-event rates) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (telematics benchmarks revised; resolve current target at use time).

---

## The five road-safety indicators (each → ISO 39001 RTS factor)

| Indicator | Tag | Formula | Source | Target basis |
|---|---|---|---|---|
| **Speeding** | leading | (journeys/segments within speed limit ÷ total) × 100; or over-speed events ÷ distance | ISO 39001:2012 (vehicle speed = key RTS factor) + telematics | improve stretch-but-credible |
| **Harsh-braking / harsh events** | leading | (harsh braking + acceleration + cornering events) ÷ distance (telematics) | telematics intermediate behaviour indicator | reduce period-over-period |
| **Journey management** | leading | (% journeys risk-assessed / planned) × 100 | ISO 39001:2012 (exposure-oriented control) | toward 100% for high-risk journeys |
| **Vehicle-defect rate** | leading | (pre-use checks with a defect ÷ checks done) × 100; or % vehicles passing condition assessment | ISO 39001:2012 (vehicle-condition factor) | trend down; defects closed owned/dated |
| **Driver-hours compliance** | lagging | (% within HOS / drivers'-hours window) × 100 | ISO 39001:2012 fatigue-management factor; **cross-refs** SUB-03 fatigue-index + FMCSA HOS / EU drivers' hours (NOT computed here) | 100% compliance |

## Additional named ISO 39001 RTS factors (cite where relevant)

- **Seatbelt use** — % occupants belted (restraint-use RTS factor).
- **Helmet use** — % riders helmeted (protective-equipment RTS factor).
- Both are recognised ISO 39001:2012 RTS performance factors; add them where the road scope includes
  occupants / two-wheelers.

## Discipline

- Each indicator carries `leading|lagging` tag · formula · source · target — a bare road-safety figure
  with no formula/source fails specificity.
- Driver-hours compliance is reported here as an **indicator** only; the fatigue/HOS **computation**
  defers to SUB-03 / the LOG-01 engine. No fabricated form or rule number is minted.

## How the skill uses this fragment

`leading-lagging-kpi-framework` adds these five indicators (+ seatbelt/helmet where relevant) when the
intake selects a road-transport scope, defines each (formula·source·target), and reports them in the
balanced set — staying one skill (an in-skill branch), the single home of road-safety KPIs.
