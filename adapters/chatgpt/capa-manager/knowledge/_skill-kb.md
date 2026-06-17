# Knowledge-base manifest for `capa-manager`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The CAPA-lifecycle backbone every run cites — **clause 10.2** (incident, nonconformity & corrective action: react → eliminate the cause so it does not recur → corrective + preventive action → review effectiveness → retain documented evidence) + **clause 8.1.2** (hierarchy of controls). | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** corrective and preventive action at Workflow step 5 (then verified by `controls.rank_controls`/`validate_treatment` — the `ppe_admin_only` flag). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured one-question-at-a-time intake the Workflow opens with (the source gate + the INGEST branch + the specificity anchor). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The source of the moderate roster below `orchestration:end` (De-identifier-first → Researcher/Cause-Analyst + Drafter → Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India documented-information / corrective-action / return duty by state — **mandatory state detection** (resolve the state before citing; un-seeded state → `[GAP]`, never an invented national form number). | ../../../knowledge-base/regulatory/in-state-forms.md |
