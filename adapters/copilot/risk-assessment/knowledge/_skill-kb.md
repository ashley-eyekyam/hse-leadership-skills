# Knowledge-base manifest for `risk-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The HIRA backbone — clause **6.1.2** (hazard identification & assessment of risks) + **8.1.2** (hierarchy of controls); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-ISO14001 | The environmental branch only (Q0 = Environmental/Both) — clause **6.1.2** (environmental aspects & impacts); cited when the branch ran. | ../../../knowledge-base/standards/iso-14001.md |
| KB-SNIP-HOC | Applied to **every** control recommendation, safety and environmental alike (Workflow step 4), then verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q0 + Q1…Q10 + Q-E1…Q-E5). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Researcher + Regulatory-Checker + Drafter + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India state-form resolution — `jurisdiction: [All]` includes India, so mandatory state detection (Q1a) is wired; the resolved state form is cited, **never a national form number**. | ../../../knowledge-base/regulatory/in-state-forms.md |
