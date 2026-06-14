# Knowledge Base — master index (navigation only)

**Purpose:** the single always-cheap-to-scan entry point. Per facet folder, this lists
every fragment's `id · path · title · facets · summary` — drawn from each folder's
`_registry.yaml`. **It carries no domain content itself.**

**How to use:** a skill (or its Researcher subagent) scans this index to *choose* the
ONE fragment matching its `(jurisdiction × industry × audience)` facets, then reads
**only that one file** — never the whole base.

**ID scheme:** `KB-<FOLDER>-<FACET>-<SLUG>` (folder codes `STD`/`REG`/`DATA`/`SNIP`/`RES`/`ASSET`).
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

## regulatory/ — statutory jurisdiction fragments

| ID | Path | Title | Facets | Summary |
|---|---|---|---|---|
| KB-REG-IN-FACTORIES | regulatory/in-factories-act.md | India — Factories Act, 1948 (statutory framing, legacy-first) | juris:IN; ind:All; aud:M/C; topics:factories-act/general-duties/returns/accident-notice | Federal Factories-Act framing; state forms/due/portal resolved via KB-REG-IN-STATEFORMS after state detection. Legacy-first; OSH-Code transition flagged. |
| KB-REG-IN-STATEFORMS | regulatory/in-state-forms.md | India — Factories Act state-form lookup (legacy-first) | juris:IN; ind:All; aud:M/C; topics:annual-return/half-yearly-return/accident-notice/registers/state-detection | (law, state, obligation) → {form, rule, due, portal, osh_transition}; TN/KA/MH/DL + BOCW seeded; Mines/PESO/MSIHC module slots; OSH-Code transition note. No nationwide form number. |
| KB-REG-UK-HSWA | regulatory/uk-hswa.md | United Kingdom — HSWA 1974 + MHSWR 1999 | juris:UK; ind:All; aud:M/C; topics:general-duties/risk-assessment/principles-of-prevention/riddor | HSWA s.2/s.3 duties; MHSWR reg.3 suitable & sufficient risk assessment; principles of prevention (HOC); RIDDOR; reasonably-practicable test. |
| KB-REG-US-OSHA | regulatory/us-osha.md | United States — OSHA (OSH Act / 29 CFR 1910/1926/1904) | juris:US; ind:All; aud:M/C; topics:general-duty-clause/general-industry/construction/recordkeeping | General Duty Clause; 29 CFR 1910/1926 standards; 1904 injury/illness recordkeeping (drives TRIR/DART); 1904.29 privacy-case (de-id). |
| KB-REG-EU-OSH | regulatory/eu-osh.md | European Union — OSH Framework Directive 89/391/EEC | juris:EU; ind:All; aud:M/C; topics:general-obligation/principles-of-prevention/information-consultation/daughter-directives | Framework Directive Art.5/6 (employer duty; general principles of prevention = HOC); Arts.10-12 information/consultation; cite member-state transposition for binding forms. |

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

## assets/ — reusable non-text (no registry)

Pointed-to by ID-bearing fragments (e.g. control-matrix templates, icons). Not facet-resolved.
