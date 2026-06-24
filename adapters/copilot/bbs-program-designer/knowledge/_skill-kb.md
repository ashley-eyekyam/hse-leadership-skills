# Knowledge-base manifest for `bbs-program-designer`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-SNIP-BBS-METHOD | The method backbone — ABC (antecedent-behaviour-consequence) analysis, non-punitive observation-card design, the observer-feedback loop; at-risk behaviours route to hierarchy-ranked system fixes, never retrain-the-worker. Cited on every run. | ../../../knowledge-base/prompt-snippets/bbs-method.md |
| KB-DATA-BBS-METRICS | The defined BBS metrics — percent-safe / participation / trend-by-category — and the mandatory `<5` small-cell suppression guardrail on any team breakdown. Read the named figures; trend by category, never by person. | ../../../knowledge-base/data-points/bbs-metrics.md |
| KB-SNIP-LEADERSHIP-CLAUSE-MAP | The bundle-shared ISO 45001 leadership clause cross-walk — maps clause **5.4** (worker participation) to this skill; single source, never duplicated into the body. | ../../../knowledge-base/prompt-snippets/leadership-clause-map.md |
| KB-SNIP-HOC | Applied to **every** at-risk-behaviour treatment (Workflow step 5): system fixes (eliminate/substitute/engineer/administrate) rank ABOVE "retrain the worker"; then verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 scope+sibling check · Q2 behaviours · Q3 observability gate · Q5 metrics · Q6 jurisdiction). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Program-Designer + Action-Planner + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
