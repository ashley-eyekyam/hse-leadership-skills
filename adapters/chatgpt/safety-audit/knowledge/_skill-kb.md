# Knowledge-base manifest for `safety-audit`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The audit **method** backbone — clause 9.2 (internal audit), always cited; plus 8.1.2 (hierarchy of controls) for corrective actions and 10.2 (nonconformity & corrective action) for the finding→CAPA loop. When Q-Crit = ISO 45001, the audited clauses become the **criteria** set. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to every corrective action before `controls.rank_controls` (step 6). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern the Workflow opens with (Q-Scope / Q-Crit gates). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The source for the De-identifier / Evidence-Assessor / Regulatory-Checker / Drafter / Critic roster. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India compliance audits — resolve the **state** form (mandatory state detection) before citing; never a national form number. | ../../../knowledge-base/regulatory/in-state-forms.md |
