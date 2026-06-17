# Knowledge-base manifest for `mine-rescue-erp`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | 8.2 emergency preparedness & response backbone | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | rank any prevention/mitigation control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | structured intake pattern | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | subagent roster + Mine-Manager SME persona | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-MINES-ACT | Mines Act emergency-preparedness / mine-rescue duty | ../../../knowledge-base/regulatory/in-mines-act.md |
| KB-DATA-MINING-HAZARDS | principal-hazard library -> emergency scenarios | ../../../knowledge-base/data-points/mining-hazards.md |
