# Knowledge-base manifest for `lopa-worksheet`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree.

| ID | Use | Path |
|---|---|---|
| KB-STD-IEC-61511 | The LOPA/SIL method map — initiating event, IPL independence, residual gap, SIL; cited on every run. PFD/SIL engineer-supplied. | ../../../knowledge-base/standards/iec-61511.md |
| KB-STD-ISO45001 | OH&S backbone — 8.1.2 hierarchy of controls frames the IPL ranking. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to the IPL set — an IPL set that is administrative/PPE-only without an engineered IPL is flagged. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time scenario/IPL intake the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | Single-threaded by design; the Process-Safety-Engineer persona reviews IPL independence. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
