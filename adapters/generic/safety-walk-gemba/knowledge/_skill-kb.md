# Knowledge-base manifest for `safety-walk-gemba`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-SNIP-GEMBA-PROMPTS | The **open-question conversation-prompt bank** by purpose/area (felt-leadership · hazard-spotting · control-verification · post-incident) — engagement, never a tick-box; concerns role-labelled. Read on every run to select the prompt family. | ../../../knowledge-base/prompt-snippets/gemba-prompts.md |
| KB-SNIP-LEADERSHIP-CLAUSE-MAP | The ISO 45001 leadership clause cross-walk — this skill owns clauses **5.1** (leadership and commitment, felt leadership) and **5.4** (consultation and participation of workers). Cited on every run. | ../../../knowledge-base/prompt-snippets/leadership-clause-map.md |
| KB-DATA-LEADING-INDICATORS | The single-sourced leading/lagging indicator catalogue — read the **gemba-commitment closure-rate** entry; report walk-commitment closure as a leading indicator, quote `source`+`year`. | ../../../knowledge-base/data-points/leading-indicators.md |
| KB-STD-ISO45001 | The management-system backbone for clauses **5.1 / 5.4** — leadership, commitment, and worker consultation/participation. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to any control a walk commitment implies (Workflow step 4): higher-order controls before PPE/admin; then verified by `controls.py`. Never a PPE-only or "retrain the worker" default. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 purpose/disambiguation · Q2 named area · Q3 prompt family · Q5 jurisdiction). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Walk-Designer + Commitment-Tracker + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
