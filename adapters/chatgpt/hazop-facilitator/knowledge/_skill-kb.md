# Knowledge-base manifest for `hazop-facilitator`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree.

| ID | Use | Path |
|---|---|---|
| KB-STD-IEC-61882 | The HAZOP method map — node/guideword/parameter structure and the worksheet columns; cited on every run. | ../../../knowledge-base/standards/iec-61882.md |
| KB-STD-ISO45001 | OH&S backbone — 6.1.2 hazard identification frames the study; 8.1.2 points to the hierarchy of controls for safeguards. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to every safeguard/recommendation — a procedure/PPE-only safeguard set without a higher-order barrier is flagged. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time node/intent/team intake the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The moderate roster (De-identifier-first + Researcher + Drafter + Critic/QA) + the Process-Safety-Engineer persona. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
