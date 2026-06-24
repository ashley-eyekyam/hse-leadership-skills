# Knowledge-base manifest for `infection-control-plan`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment / 8.1.2 hierarchy of controls) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every IPC control — engineering (ventilation, AIIR / negative pressure, single rooms) and administrative controls first, PPE last; a PPE-only / respirator-alone treatment is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-STD-IPC-CDC-WHO | The IPC framework spine — CDC isolation precautions (Standard + Transmission-Based: contact/droplet/airborne) + WHO IPC core components + Spaulding reprocessing classification (critical/semi-critical/non-critical); the topic→artifact structure map (cite the topics, never paste the guideline) | ../../../knowledge-base/standards/ipc-cdc-who.md |
| KB-SNIP-IPC-PRECAUTIONS | The per-route precaution-selection logic — Standard Precautions always, then layer Transmission-Based precautions by route; engineering (ventilation, single rooms, negative pressure) and administrative controls before PPE; a PPE-led plan with no room/ventilation control, or an airborne agent with no AIIR/respirator, is rejected; cluster reporting is small-cell-suppressed | ../../../knowledge-base/prompt-snippets/ipc-precautions.md |
| KB-SNIP-HEALTHCARE-CLAUSE-MAP | The bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent | ../../../knowledge-base/prompt-snippets/healthcare-clause-map.md |
| KB-REG-OSHA-BBP | US confidentiality discipline reused for IPC PHI handling: OSHA 29 CFR 1910.1030 ((f) confidential post-exposure / health-data follow-up) — the paragraph→duty→artifact citation map (cite the topics, never paste the rule) | ../../../knowledge-base/regulatory/osha-bbp.md |
| KB-REG-IN-BMW2016 | India Bio-Medical Waste Management Rules 2016 segregation (yellow/red/blue/white-translucent stream); defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-bmw2016.md |
