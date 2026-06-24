# Knowledge-base manifest for `lab-biosafety-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every biosafety control — engineering containment (biosafety cabinet, ventilation) first, PPE last; a PPE-led treatment is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-STD-BIOSAFETY-BMBL-WHO | The biosafety determination spine — CDC/NIH BMBL 6th ed BSL-1–4 + biosafety-cabinet classes + WHO LBM 4th ed risk groups RG1–RG4 + risk-assessment structure + NIH Guidelines pointer; the risk-group → containment-level decision (cite, never paste the manual) | ../../../knowledge-base/standards/biosafety-bmbl-who.md |
| KB-SNIP-BIOSAFETY-RA | The biosafety risk-assessment gate — classify the risk group (RG1–RG4; unknown → `[GAP]`, never invent) → assess the procedure → select the BSL → engineering/BSC containment before PPE; small-cell-suppressed exposure reporting (the skill's core lever) | ../../../knowledge-base/prompt-snippets/biosafety-ra.md |
| KB-SNIP-HEALTHCARE-CLAUSE-MAP | The bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent | ../../../knowledge-base/prompt-snippets/healthcare-clause-map.md |
| KB-REG-OSHA-BBP | US duty (where a lab procedure handles human blood / OPIM): OSHA 29 CFR 1910.1030 ((c) ECP / (d)(2) engineering & work-practice controls / (f) confidential post-exposure follow-up + HBV vaccination) — the paragraph→duty→artifact citation map (cite the topics, never paste the rule); reused from HC-01 | ../../../knowledge-base/regulatory/osha-bbp.md |
| KB-REG-IN-BMW2016 | India Bio-Medical Waste Management Rules 2016 lab-waste segregation; defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-bmw2016.md |
