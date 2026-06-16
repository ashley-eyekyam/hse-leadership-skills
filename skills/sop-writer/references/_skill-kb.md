# Knowledge-base manifest for `sop-writer`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The operational-control backbone — clause **8.1** (operational control) + **8.1.2** (hierarchy of controls); cited on every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** control embedded in a step; the Workflow ranks Elimination→…→PPE before `controls.rank_controls` verifies | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-question-at-a-time structured-intake pattern the Workflow opens with | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The roster source (De-identifier-first → Researcher + Drafter → Critic/QA) | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-AUDIENCE | The **literacy lever** — pitch the procedure's reading level + register to the stated reader (Q10) | ../../../knowledge-base/prompt-snippets/audience-calibration.md |
| KB-REG-IN-STATEFORMS | India **mandatory state detection** — resolve the state before citing any documented-procedure duty; **no SOP form number** (an SOP is an internal MS document) | ../../../knowledge-base/regulatory/in-state-forms.md |
