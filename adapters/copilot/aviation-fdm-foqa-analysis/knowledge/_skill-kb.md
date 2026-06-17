# Knowledge-base manifest for `aviation-fdm-foqa-analysis`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ICAO-ANNEX19 | Pillar 3 (Safety Assurance) — operational-data monitoring inputs (FDM/FOQA) grounding. | ../../../knowledge-base/standards/icao-annex19.md |
| KB-SNIP-HOC | Rank the SMS actions arising from the analysis through the hierarchy of controls. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The Aviation-SMS Critic/QA persona (the load-bearing assistive no-fabrication check). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
