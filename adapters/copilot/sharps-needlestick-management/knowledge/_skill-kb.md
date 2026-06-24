# Knowledge-base manifest for `sharps-needlestick-management`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every sharps control — eliminate the sharp first, PPE/PEP last; a behaviour-led / PPE-led treatment is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-SHARPS-HIERARCHY | The sharps engineering-first control spine — eliminate unnecessary sharps → safety-engineered devices + point-of-use disposal → safe work practices → PPE/PEP residual; a "be careful / wear gloves" treatment of an eliminable/engineerable sharp is rejected (the skill's core lever); exposure reporting is small-cell-suppressed | ../../../knowledge-base/prompt-snippets/sharps-hierarchy.md |
| KB-SNIP-HEALTHCARE-CLAUSE-MAP | The bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent | ../../../knowledge-base/prompt-snippets/healthcare-clause-map.md |
| KB-REG-OSHA-BBP | US duty: OSHA 29 CFR 1910.1030 ((c) ECP / (c)(1)(iv) annual safer-device evaluation with frontline input / (d)(2) engineering & work-practice controls / (f) confidential post-exposure follow-up / (h)(5) Sharps Injury Log) + the Needlestick Safety and Prevention Act — the paragraph→duty→artifact citation map (cite the topics, never paste the rule) | ../../../knowledge-base/regulatory/osha-bbp.md |
| KB-REG-EU-SHARPS-2010-32 | EU/UK duty: EU Directive 2010/32/EU (eliminate unnecessary sharps, safer engineered devices, recapping ban, safe disposal, training, reporting + PEP) + the UK Sharps Regulations 2013 with COSHH — clause→duty→artifact map; cite the member-state transposition for the binding obligation | ../../../knowledge-base/regulatory/eu-sharps-2010-32.md |
| KB-REG-IN-BMW2016 | India Bio-Medical Waste Management Rules 2016 sharps segregation (yellow/blue/white-translucent stream); defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-bmw2016.md |
