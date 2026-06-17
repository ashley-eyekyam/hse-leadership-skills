# Knowledge-base manifest for `aviation-confidential-reporting`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ICAO-ANNEX19 | Pillar 4 (Safety Promotion) — the confidential/voluntary reporting grounding. | ../../../knowledge-base/standards/icao-annex19.md |
| KB-SNIP-HOC | Hierarchy of controls where the reporting outcome drives a control response. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The Aviation-SMS Critic/QA persona + the roster archetypes (De-identifier load-bearing). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
