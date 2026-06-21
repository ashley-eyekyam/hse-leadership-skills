# Knowledge Base — master index (navigation only)

**Purpose:** the single always-cheap-to-scan entry point. Per facet folder, this lists
every fragment's `id · path · title · facets · summary` — drawn from each folder's
`_registry.yaml`. **It carries no domain content itself.**

**How to use:** a skill (or its Researcher subagent) scans this index to *choose* the
ONE fragment matching its `(jurisdiction × industry × audience)` facets, then reads
**only that one file** — never the whole base.

**ID scheme:** `KB-<FOLDER>-<FACET>-<SLUG>` (folder codes `STD`/`REG`/`DATA`/`SNIP`/`RES`/`HAZ`/`ASSET`).
The ID is the durable handle; filenames are incidental.

**Always-on rubric (applies regardless of which fragment is chosen):**
- Resolve jurisdiction first; if unknown, **ask before citing any specific law**.
- For India, **state detection is mandatory** before citing a form (`KB-REG-IN-STATEFORMS`, topic `state-detection`).
- Ground management-system structure in `standards/` (`KB-STD-ISO45001` · `KB-STD-ISO14001` · `KB-STD-ISO45003`).
- Always rank controls via `KB-SNIP-HOC`; never a PPE-only treatment.
- Every benchmark/figure is quoted with its `source`+`year` — never bare.

> This index is generated/validated from the `_registry.yaml` files so it never drifts
> (A8 can regenerate and diff it).

---

## standards/ — international management-system standards (jurisdiction-independent)

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-STD-ISO45001 | standards/iso-45001.md | ISO 45001:2018 — OH&S MS (clause→artifact map) | juris:All; ind:All; aud:M/C; topics:ohsms/hira/hierarchy-of-controls/audit | OH&S clause map; 6.1.2 HIRA core; 8.1.2→KB-SNIP-HOC; 9.2 audit; 10.2 incident/CAPA. Structural reference, not the standard text. |
| KB-STD-ISO14001 | standards/iso-14001.md | ISO 14001:2015 — Environmental MS (clause→artifact map) | juris:All; ind:All; aud:M/C; topics:ems/environmental-aspects/compliance-obligations/lifecycle | Annex-SL-aligned clause map; 6.1.2 environmental aspects/impacts register; 8.1 lifecycle; compliance evaluation. Structural reference, not the standard text. |
| KB-STD-ISO45003 | standards/iso-45003.md | ISO 45003:2021 — Psychosocial risk (clause→artifact map) | juris:All; ind:All; aud:M/C; topics:psychosocial/work-design-controls/mental-health/monitoring | Psychosocial guidance extending 45001; work-design controls (not resilience-only); psychosocial hazard ID/RA/monitoring. Structural reference, not the standard text. |
| KB-STD-NFPA70E | standards/nfpa-70e.md | NFPA 70E / IEEE 1584 — arc-flash boundary & PPE category (clause→artifact map) | juris:All; ind:utilities/renewables/Mfg; aud:M/C; topics:arc-flash/incident-energy/ppe-category/electrical-safety/ieee-1584/boundary | Arc-flash study structure: IEEE 1584-2018 incident-energy method → boundary + NFPA 70E PPE-category bands (1.2/4/8/25/40 cal/cm² breakpoints, structure only). Pairs with the SUB-02 arcflash engine. Structural reference, not the standard tables. |
| KB-STD-ISO22301 | standards/iso-22301.md | ISO 22301:2019 — Business Continuity Management (clause→artifact map) | juris:All; ind:All; aud:M/C; topics:bcms/business-impact-analysis/rto/rpo/continuity-plan/emergency-response | BCMS clause map: BIA → RTO/RPO → continuity strategy → BCP → exercise. Annex-SL-aligned; pairs with KB-STD-ISO45001 + the ERP skills. Structural reference, not the standard text. |
| KB-STD-GHS-ERGO | standards/ghs-ergo.md | Ergonomics methods — NIOSH / RULA / REBA (method→artifact map) | juris:All; ind:All/Mfg; aud:M/C; topics:ergonomics/niosh-lifting-equation/rula/reba/manual-handling/posture | NIOSH RWL/LI + RULA (1–7) + REBA (1–15) method structure → action levels → control selection (work-design-first). Pairs with the SUB-01 ergonomics engine. Method structure only; copyrighted score tables embedded in the engine under citation. |
| KB-STD-ESG-GRI403 | standards/esg-gri-403.md | GRI 403 / SASB / ESRS S1 — OH&S disclosure index (disclosure→artifact map) | juris:All; ind:All; aud:M/C; topics:esg/gri-403/sasb/esrs-s1/disclosure-index/injury-rates/sustainability-reporting | OH&S disclosure-code map across GRI 403 / SASB / ESRS S1 → the disclosure-index artifact; injury-rate figures from incident_rates, never invented. Disclosure-code structure only, not the framework text. |
| KB-STD-HEALTHCARE-PSYCHOSOCIAL | standards/healthcare-psychosocial.md | Healthcare psychosocial risk — cross-list into ISO 45003 (topic→artifact map) | juris:All; ind:healthcare; aud:M/C; topics:psychosocial/workplace-violence/emotional-labour/shift-fatigue/moral-distress/work-design-controls | Healthcare psychosocial hazards (WPV, emotional labour, shift fatigue, moral distress) cross-listed onto the existing KB-STD-ISO45003 work-design-control structure — references it, does not duplicate it. Wiring deferred to Ph17. |

## regulatory/ — statutory jurisdiction fragments

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-REG-IN-FACTORIES | regulatory/in-factories-act.md | India — Factories Act, 1948 (statutory framing, legacy-first) | juris:IN; ind:All; aud:M/C; topics:factories-act/general-duties/returns/accident-notice | Federal Factories-Act framing; state forms/due/portal resolved via KB-REG-IN-STATEFORMS after state detection. Legacy-first; OSH-Code transition flagged. |
| KB-REG-IN-STATEFORMS | regulatory/in-state-forms.md | India — Factories Act state-form lookup (legacy-first) | juris:IN; ind:All; aud:M/C; topics:annual-return/half-yearly-return/accident-notice/registers/state-detection | (law, state, obligation) → {form, rule, due, portal, osh_transition}; TN/KA/MH/DL + BOCW seeded; Mines/PESO/MSIHC module slots; OSH-Code transition note. No nationwide form number. |
| KB-REG-UK-HSWA | regulatory/uk-hswa.md | United Kingdom — HSWA 1974 + MHSWR 1999 | juris:UK; ind:All; aud:M/C; topics:general-duties/risk-assessment/principles-of-prevention/riddor | HSWA s.2/s.3 duties; MHSWR reg.3 suitable & sufficient risk assessment; principles of prevention (HOC); RIDDOR; reasonably-practicable test. |
| KB-REG-US-OSHA | regulatory/us-osha.md | United States — OSHA (OSH Act / 29 CFR 1910/1926/1904) | juris:US; ind:All; aud:M/C; topics:general-duty-clause/general-industry/construction/recordkeeping | General Duty Clause; 29 CFR 1910/1926 standards; 1904 injury/illness recordkeeping (drives TRIR/DART); 1904.29 privacy-case (de-id). |
| KB-REG-EU-OSH | regulatory/eu-osh.md | European Union — OSH Framework Directive 89/391/EEC | juris:EU; ind:All; aud:M/C; topics:general-obligation/principles-of-prevention/information-consultation/daughter-directives | Framework Directive Art.5/6 (employer duty; general principles of prevention = HOC); Arts.10-12 information/consultation; cite member-state transposition for binding forms. |
| KB-REG-CDM2015 | regulatory/cdm-2015.md | United Kingdom — CDM 2015 (Construction Design & Management duty map) | juris:UK; ind:Con; aud:M/C; topics:cdm/principal-designer/principal-contractor/construction-phase-plan/health-safety-file/f10 | CDM 2015 dutyholder→artifact map: Client/PD/Designer/PC/Contractor duties, PCI / Construction Phase Plan / Health & Safety File, F10 notification trigger → grounds UK construction permit/plan + risk-assessment skills. Citation map, not the regulation/ACOP text. |
| KB-REG-OSHA1926 | regulatory/osha-1926.md | United States — OSHA 29 CFR 1926 (construction standards / Focus Four map) | juris:US; ind:Con; aud:M/C; topics:osha-1926/focus-four/falls/struck-by/caught-in/electrocution/construction | OSHA 29 CFR 1926 hazard→standard→control map anchored on the construction Focus Four (falls/struck-by/caught-in/electrocution) + scaffolds/cranes/HazCom/recordkeeping → grounds US construction permit/JSA + risk-assessment skills. Citation map, not the regulation text. |
| KB-REG-ROGS | regulatory/uk-rogs.md | United Kingdom — ROGS 2006 (rail/guided-transport SMS + authorisation map) | juris:UK; ind:Rail; aud:M/C; topics:rogs/safety-management-system/safety-authorisation/safety-certificate/safety-critical-work/sfairp | ROGS 2006 duty→artifact map: SMS duties, safety-authorisation/safety-certificate framework, risk co-operation, safety-critical competence/fitness, safety verification → grounds GB rail SMS/safety-case skills. Citation map, not the regulation/ORR-guidance text. |
| KB-REG-OFFSHORE-SCR | regulatory/offshore-scr.md | United Kingdom — Offshore Installations (Safety Case) Regs 2015 + SEMS map | juris:UK; ind:O&G/Marine; aud:M/C; topics:safety-case/offshore-safety-directive/major-accident-hazard/sece/verification/alarp/sems | SCR 2015 duty→safety-case-element map: safety-case acceptance regime, MAH identification, ALARP demonstration, SECE register + performance standards, independent verification, emergency response, SEMS → grounds offshore safety-case/SIMOPS skills. Citation map, not the regulation/OSD text. |
| KB-REG-FMCSA-HOS | regulatory/fmcsa-hos.md | United States / European Union — FMCSA Hours-of-Service + EU drivers' hours map | juris:US/EU; ind:Transport; aud:M/C; topics:fmcsa-hos/eu-561/drivers-hours/driving-window/break/rest/eld/tachograph/fatigue | FMCSA HOS (49 CFR 395) + EU Reg 561/2006 duty→limit-category→artifact map naming the driving/duty/break/rest categories + ELD/tachograph records; numeric limits live in the fatigue engine (LOCKED constants), not this fragment → grounds logistics/transport skills. Citation map, not the regulation text. |
| KB-REG-WPV-OSHA3148 | regulatory/wpv-osha-3148.md | United States — OSHA 3148 workplace-violence prevention program map (healthcare) | juris:US; ind:Healthcare; aud:M/C; topics:workplace-violence/osha-3148/general-duty-clause/hazard-assessment/prevention-controls/training/recordkeeping | OSHA 3148 five-element WPV-program map (management commitment + worker participation / worksite analysis / hazard prevention + control / training / recordkeeping + evaluation), enforced via OSH Act §5(a)(1) General Duty Clause → grounds healthcare WPV-program skill. Citation map, not the guideline text. |
| KB-REG-CONSTRUCTION-PERMIT | regulatory/construction-permit.md | Cross-list — Construction high-risk-activity permit-to-work map | juris:UK/US/All; ind:Con; aud:M/C; topics:permit-to-work/excavation/working-at-height/hot-work/confined-space/lifting/electrical-permit | Construction PTW activity→permit→control map (excavation/WAH/hot-work/confined-space/lifting/electrical) cross-walking KB-REG-CDM2015 (UK) / KB-REG-OSHA1926 (US); per-facet cross-list content for the construction pack. Practice map, not statute text. Seam wiring deferred to Ph17 (SEAM-01). |
| KB-REG-LOTO | regulatory/loto.md | Cross-list — Lockout/Tagout (control of hazardous energy) map | juris:US/UK/All; ind:All; aud:M/C; topics:lockout-tagout/hazardous-energy/isolation/verify-zero-energy/electrical/mechanical/hydraulic/pneumatic | Control-of-hazardous-energy energy-source→isolation-step→artifact map (electrical/mechanical/hydraulic/pneumatic/thermal/gravity/process) + the verify-zero-energy gate; cross-walks OSHA 29 CFR 1910.147/1926.417 + UK EAWR safe-isolation. Practice map, not standard text. Seam wiring deferred to Ph17 (SEAM-01). |
| KB-REG-MFG-HAZCOM | regulatory/manufacturing-hazcom.md | Cross-list — Manufacturing hazard-communication (HazCom / GHS) map | juris:US/EU/All; ind:Mfg; aud:M/C; topics:hazcom/ghs/sds/labelling/chemical-inventory/exposure-control/training | Manufacturing HazCom duty→artifact map (inventory / SDS access / GHS labelling / written program / training / task-exposure controls) cross-walking OSHA HCS 1910.1200 + EU CLP + KB-STD-GHS; per-facet cross-list content for the manufacturing pack. Practice map, not standard text. Seam wiring deferred to Ph17 (SEAM-01). |
| KB-REG-UTILITIES-ERP | regulatory/utilities-erp.md | Cross-list — Utilities / power emergency-response-plan (ERP) map | juris:All; ind:Utilities; aud:M/C; topics:emergency-response/arc-flash/restoration/downed-conductor/storm-response/confined-space-rescue | Utilities/power ERP scenario→response-element→artifact map (arc-flash incident / loss-of-supply / substation fire / downed conductor / vault rescue / storm) cross-walking KB-STD-NFPA70E arc-flash boundaries; per-facet cross-list content for the utilities pack. Practice map, not standard text. Seam wiring deferred to Ph17 (SEAM-01). |
| KB-REG-OFFSHORE-SIMOPS | regulatory/offshore-simops.md | Cross-list — Offshore simultaneous-operations (SIMOPS) map | juris:UK/All; ind:O&G/Marine; aud:M/C; topics:simops/simultaneous-operations/interaction-hazard/simops-matrix/bridging-document/exclusion-zone | Offshore SIMOPS concurrent-activity→interaction-hazard→control map (drilling+production / lifting+transfer / diving+DP / hot-work+hydrocarbon / heli+crane / bridging) cross-walking KB-REG-OFFSHORE-SCR; per-facet cross-list content for the marine/offshore pack. Practice map, not standard text. Seam wiring deferred to Ph17 (SEAM-01). |
| KB-REG-RAIL-SIGNALLING | regulatory/rail-signalling.md | Cross-list — Rail signalling / track-safety (possession & protection) map | juris:UK/All; ind:Rail; aud:M/C; topics:track-safety/possession/safe-system-of-work/lookout/electrical-isolation/signalling-commissioning/adjacent-line-open | Rail on-track task→protection-arrangement→artifact map (possession / lookout SSOW / OLE-3rd-rail isolation / signalling commissioning / level-crossing / adjacent-line-open) cross-walking KB-REG-ROGS; per-facet cross-list content for the rail pack. Practice map, not rule-book text. Seam wiring deferred to Ph17 (SEAM-01). |
| KB-REG-RENEWABLES-ELECTRICAL | regulatory/renewables-electrical.md | Cross-list — Renewables electrical-safety (wind / solar / BESS) map | juris:All; ind:Renewables; aud:M/C; topics:renewables/wind-turbine/solar-pv/bess/arc-flash/dc-isolation/working-at-height/thermal-runaway | Renewables asset→electrical-hazard→control map (wind nacelle HV / solar PV always-live DC / BESS thermal-runaway / inverter arc-flash / grid switching / cable strike) cross-walking KB-STD-NFPA70E + KB-REG-LOTO; per-facet cross-list content for the renewables pack. Practice map, not standard text. Seam wiring deferred to Ph17 (SEAM-01). |

## data-points/ — benchmark fragments (every figure carries source+year)

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-DATA-TRIR-BENCHMARKS | data-points/incident-rates-benchmarks.md | Incident-rate benchmarks (TRIR / DART / LTIFR) | juris:All; ind:All; aud:M/C; topics:trir/dart/ltifr/benchmarks | Rate formulae (stable) + the publishing bodies (BLS SOII / UK HSE / ILO) to resolve current-year sector figures; quote body+year+sector, never a bare number. |
| KB-DATA-EXPOSURE-LIMITS | data-points/exposure-limits.md | Occupational exposure limits (OELs) — resolution map | juris:All; ind:All; aud:C; topics:oel/twa/stel/ceiling | TWA/STEL/ceiling concepts + the jurisdiction authority to resolve binding limits (OSHA PEL / NIOSH REL / ACGIH TLV / UK EH40 WEL / EU OEL); present value+unit+authority+year. |
| KB-DATA-PPE-STANDARDS | data-points/ppe-standards.md | PPE conformity standards reference | juris:All; ind:All; aud:C/F; topics:ppe/conformity-standards/selection | PPE-last selection rule + EN/ANSI-ISEA/NIOSH/ASTM conformity standards by category; cite standard+year, never assert protection without the standard. |

## prompt-snippets/ — reusable prompt instructions

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-SNIP-HOC | prompt-snippets/hierarchy-of-controls.md | Hierarchy of controls — canonical control-ranking instruction | juris:All; ind:All; aud:M/C/F; topics:hierarchy-of-controls/control-selection/ppe-flag | Forces E→S→Eng→Admin→PPE ranking; names the specific hazard; flags PPE/admin-only as lower-order (justify-or-escalate). Prompt text, not a generator. |
| KB-SNIP-INTAKE | prompt-snippets/intake-interview.md | Structured intake interview — canonical elicitation pattern | juris:All; ind:All; aud:M/C/F; topics:intake/elicitation/mcq/state-detection | Multi-step one-at-a-time interview; MCQ where enumerable, free-text where open; branch (India→state→KB-REG-IN-STATEFORMS), echo before analysis, never proceed on vague; platform-neutral. |
| KB-SNIP-AUDIENCE | prompt-snippets/audience-calibration.md | Audience calibration — pitch the artifact to its reader | juris:All; ind:All; aud:M/C/F; topics:audience/calibration/tone | Calibrates depth/language/emphasis to M (leadership), C (consultant), F (frontline); keeps controls ranked and figures sourced across all. |
| KB-SNIP-DEFENSIBILITY | prompt-snippets/defensibility-framing.md | Defensibility framing — survive a regulator's challenge | juris:All; ind:All; aud:M/C; topics:defensibility/specificity/evidence-trail/accountability | Six-point check: specificity, ranked controls, evidence trail (source+year), proportionality, named owners+dates, surfaced assumptions. |

## research/ — background reference fragments

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-RES-PSYCHOSOCIAL | research/psychosocial-hazards.md | Psychosocial hazards — background reference | juris:All; ind:All; aud:M/C; topics:psychosocial/work-design/mental-health | Psychosocial hazard categories (work-organisation lens); work-design control discipline; pairs with KB-STD-ISO45003. |
| KB-RES-SAFETY-CULTURE | research/safety-culture-models.md | Safety culture & maturity models — background reference | juris:All; ind:All; aud:M/C; topics:safety-culture/maturity-model/just-culture/systemic-models | Named safety-culture/maturity models (maturity ladder, Just Culture, accident-pyramid + critique, Swiss-cheese) for audit/board/incident framing; frame, don't substitute for evidence. |

## hazard-library/ — sector hazard libraries (HIRA/JSA/permit intake seeding menus)

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-HAZ-HEALTHCARE | hazard-library/healthcare.md | Healthcare hazard library — sharps/IPC/WPV/biosafety (hazard→artifact map) | juris:All; ind:healthcare; aud:M/C; topics:sharps/infection-prevention/workplace-violence/biosafety/hazardous-drugs/manual-handling | Healthcare hazard menu (sharps/IPC/WPV/biosafety/hazardous-drugs) → hierarchy-of-controls artifacts; physical/biological hazards (psychosocial route to KB-STD-HEALTHCARE-PSYCHOSOCIAL). Seeding list, not the site assessment. |
| KB-HAZ-RENEWABLES | hazard-library/renewables.md | Renewables hazard library — turbine WAH/rescue/weather (hazard→artifact map) | juris:All; ind:renewables; aud:M/C; topics:work-at-height/confined-space-rescue/weather-thresholds/electrical/loto/lifting/lone-working | Wind/solar hazard menu (WAH, tower rescue, weather-threshold stop conditions, electrical/arc-flash, LOTO, lifting) → hierarchy-of-controls artifacts. Seeding list, not the site assessment. |

## assets/ — reusable non-text (no registry)

Pointed-to by ID-bearing fragments (e.g. control-matrix templates, icons). Not facet-resolved.
