# Knowledge-base manifest for `board-safety-report`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | (author the use) | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-ISO14001 | (author the use) | ../../../knowledge-base/standards/iso-14001.md |
| KB-DATA-TRIR-BENCHMARKS | (author the use) |  |
| KB-SNIP-INTAKE | (author the use) | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | (author the use) | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | (author the use) | ../../../knowledge-base/regulatory/in-state-forms.md |
