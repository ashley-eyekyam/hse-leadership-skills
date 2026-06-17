# Knowledge-base manifest for `peso-licensing-assistant`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree.

| ID | Use | Path |
|---|---|---|
| KB-REG-IN-PESO | The PESO rule → licence → form → authority cluster; cited on every run. Forms come from this row, never hard-coded. | ../../../knowledge-base/regulatory/in-peso.md |
| KB-REG-IN-STATEFORMS | Resolved AFTER mandatory state detection for any state-specific obligation (siting, state consents). | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-IN-FACTORIES | The Factories-Act framing for the MAH installation's state factory interactions. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-STD-ISO45001 | OH&S backbone for the on-site emergency plan structure. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to the emergency-plan and licensing controls. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time installation/licence/state intake with the India state branch. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The moderate roster + the Process-Safety-Engineer persona. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
