# Knowledge-base manifest for `icmm-critical-control-management`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | 6.1.2 HIRA backbone for the unwanted event | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-ICMM-CCM | CCM method structure + mining principal-hazard taxonomy (mining-owned) | ../../../knowledge-base/standards/icmm-ccm.md |
| KB-STD-CCPS-BOWTIE | bowtie technique — developed via the bowtie-builder facilitator | ../../../knowledge-base/standards/ccps-bowtie.md |
| KB-SNIP-HOC | hierarchy-rank the critical controls (flag critical) | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | structured intake pattern | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | subagent roster + Mine-Manager SME persona | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-DATA-MINING-HAZARDS | material-unwanted-event / principal-hazard selection | ../../../knowledge-base/data-points/mining-hazards.md |
