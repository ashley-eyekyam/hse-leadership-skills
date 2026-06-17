# Knowledge-base manifest for `dgms-statutory-pack`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | management-system backbone (compliance register, 6.1.3) | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | rank any follow-up control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | structured intake pattern | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | subagent roster + Mine-Manager SME persona | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-MINES-ACT | Mines Act provision -> artifact map | ../../../knowledge-base/regulatory/in-mines-act.md |
| KB-REG-IN-DGMS | DGMS form layer (5 verified anchors; [GAP] elsewhere) | ../../../knowledge-base/regulatory/in-dgms.md |
| KB-REG-IN-STATEFORMS | mandatory region/zone resolution | ../../../knowledge-base/regulatory/in-state-forms.md |
