# Knowledge-base manifest for `rail-safety-management-system`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-REG-ROGS | The ROGS 2006 SMS duties + the safety-certificate / safety-authorisation / Part-3-verification route map — the backbone of every SMS element. | ../../../knowledge-base/regulatory/uk-rogs.md |
| KB-REG-CSM-RA | The change-management element — the significance test, the three risk-acceptance principles, and the independent AsBo (live change details `[GAP]` until supplied). | ../../../knowledge-base/regulatory/csm-ra.md |
| KB-REG-IN-RAIL | India framing (Railways Act 1989 / Commissioner of Railway Safety); state detection mandatory, state-specific non-railway-depot content deferred to `hse-india`, no national form invented (CONV-8). | ../../../knowledge-base/regulatory/in-rail.md |
| KB-SNIP-RAIL-CLAUSE-MAP | The bundle standard→artifact→skill cross-walk: routes the SMS element set + the route test + the RAIL-02-references-not-rebuilds / RAIL-03-owns-level-crossings boundaries. | ../../../knowledge-base/prompt-snippets/rail-clause-map.md |
| KB-SNIP-HOC | Rank every risk-control-arrangement mitigation through the hierarchy of controls (the SFAIRP adequacy test). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The rail-SMS Critic/QA persona + the roster archetypes. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
