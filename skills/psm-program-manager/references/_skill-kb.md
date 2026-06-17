# Knowledge-base manifest for `psm-program-manager`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree.

| ID | Use | Path |
|---|---|---|
| KB-STD-PSM | The 14-element framework map — each element → its artifact + status; cited on every run. | ../../../knowledge-base/standards/psm.md |
| KB-REG-US-OSHA | The US statutory hook (29 CFR 1910.119) cited alongside the framework for US users; kept aligned with KB-STD-PSM. | ../../../knowledge-base/regulatory/us-osha.md |
| KB-STD-ISO45001 | OH&S backbone — 8.1.2 hierarchy of controls for gap remediation; 8.1.3 MoC element. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to every gap-remediation control — admin/PPE-only remediation flagged. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time facility/element/evidence intake the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The moderate roster + the Process-Safety-Engineer persona. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
