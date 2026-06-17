# Knowledge-base manifest for `comah-safety-report-assistant`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree.

| ID | Use | Path |
|---|---|---|
| KB-REG-UK-COMAH | The COMAH 2015 / Seveso III duty map — lower/upper-tier duties, MAPP, Safety Report elements, emergency plans; cited on every run. | ../../../knowledge-base/regulatory/uk-comah.md |
| KB-STD-ISO45001 | OH&S/management-system backbone framing the SMS description. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to the risk-reduction measures in the ALARP demonstration — admin/PPE-only measures flagged. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time establishment/tier/element intake the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The moderate roster + the Process-Safety-Engineer persona reviewing the report argument. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
