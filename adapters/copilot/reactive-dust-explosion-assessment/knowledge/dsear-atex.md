<!-- KB-STD-DSEAR -->
<!-- KB-STD-ATEX -->
# DSEAR 2002 + ATEX — basis-of-safety + explosive-atmosphere zoning (clause→artifact)

**Fragment IDs:** `KB-STD-DSEAR`, `KB-STD-ATEX`
**What this is:** a copyright-safe **duty → basis-of-safety / zone → artifact map**
for the Dangerous Substances and Explosive Atmospheres Regulations 2002 (DSEAR) and
the ATEX regime (Directive 2014/34/EU equipment + Directive 1999/92/EC workplace).
**What this is NOT:** a reproduction of the regulations' normative text. Cite the
regulation / zone references only — never paste the statutory wording; the user holds
the licensed text. Area classification is a **competent-person engineering judgement** —
this map structures it, it does not decide the zone.

> Source: DSEAR 2002 + ATEX 2014/34/EU (equipment) & 1999/92/EC (workplace) — clause/zone structure (user holds the text) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false (multi-year revision cycle).

DSEAR and ATEX are read **together** for combustible-dust / flammable-vapour work:
DSEAR sets the duty (assess, prevent/mitigate, classify, control), ATEX sets the
**zone scheme + equipment category** for the hazardous area. Apply the
hierarchy-of-controls **basis of safety** — eliminate/substitute the dangerous
substance and inherently-safer design *before* engineering (ventilation, inerting,
explosion venting/suppression), engineering *before* administrative/PPE.

## `KB-STD-DSEAR` — duty → basis of safety → artifact

| DSEAR duty | Requirement topic | Grounds (skill / artifact) |
|---|---|---|
| Risk assessment | identify dangerous substances + explosive-atmosphere risk | reactive-dust-explosion-assessment |
| Prevention / mitigation hierarchy | eliminate/substitute → control ignition + atmosphere → mitigate | reactive-dust-explosion-assessment; `controls` (HoC) |
| Basis of safety | avoid the explosive atmosphere OR avoid ignition sources OR mitigate the explosion | reactive-dust-explosion-assessment (the load-bearing conclusion) |
| Area classification | classify into zones (ATEX) | → `KB-STD-ATEX` below |
| Equipment / control of ignition | equipment selection by zone; control all ignition sources | reactive-dust-explosion-assessment; tank-farm-bunding-controls |
| Information / emergency | warning, drills, emergency arrangements | reactive-dust-explosion-assessment |

## `KB-STD-ATEX` — zone scheme (structure only)

| Atmosphere | Zone (frequency of explosive atmosphere) | Equipment category |
|---|---|---|
| Gas / vapour / mist | Zone 0 (continuous/long periods) · Zone 1 (likely in normal operation) · Zone 2 (unlikely; short period) | Cat 1G / 2G / 3G |
| Combustible dust | Zone 20 (continuous/long periods) · Zone 21 (likely in normal operation) · Zone 22 (unlikely; short period) | Cat 1D / 2D / 3D |

The zone drives the **Equipment Protection Level (EPL)** and the permitted equipment
category. The classification is justified from the released-substance properties,
release grade, and ventilation — **never defaulted**; an unjustified zone is a
SME-persona FLAG.

## How the skills use these fragments
- `reactive-dust-explosion-assessment` resolves the hazard scope → the DSEAR basis of
  safety + the ATEX zone + EPL, HoC-ranked via `controls`; reactive-chemistry /
  dust-hazard nodes are handed to `hazop-facilitator` for the HAZOP/DHA study.
- `tank-farm-bunding-controls` reads DSEAR for flammable-vapour area control around
  bulk storage.
- Dust explosion parameters (Kst/Pmax/MIE/MIT) are referenced from `nfpa-652-660.md`
  with source+year, or `[GAP]`-flagged — never invented per-dust figures.
