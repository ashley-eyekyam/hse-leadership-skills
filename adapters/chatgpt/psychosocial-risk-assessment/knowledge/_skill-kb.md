# Knowledge-base manifest for `psychosocial-risk-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45003 | The psychosocial backbone — ISO 45003:2021 (managing psychosocial risk): work-design controls, confidentiality, multi-source evidence. Cited on every run. | ../../../knowledge-base/standards/iso-45003.md |
| KB-STD-ISO45001 | Clause **6.1.2** hazard identification — the psychosocial hazard is identified at source (work design) on the same hazard-id discipline as the physical RA. | ../../../knowledge-base/standards/iso-45001.md |
| KB-REG-UK-HSWA | The UK duty backbone — HSWA 1974 + the **Management of Health and Safety at Work Regulations 1999 reg. 3** general risk-assessment duty (psychosocial risk is in scope). | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-SNIP-HSE-MGMT-STANDARDS | The **six HSE Management Standards** (demands · control · support · relationships · role · change) with indicative work-design controls ranked above individual resilience — the per-domain hazard+control map this skill walks. | ../../../knowledge-base/prompt-snippets/hse-mgmt-standards.md |
| KB-DATA-PSYCHOSOCIAL-INDICATORS | Validated indicator-tool benchmark bands (each cited to source+year) used to rate each domain — special-category data; read the named bands, quote `source`+`year`. | ../../../knowledge-base/data-points/psychosocial-indicators.md |
| KB-SNIP-OPS-CLAUSE-MAP | The `hse-operations` ISO-45001 clause cross-walk (operations clauses → owning skill, D-10) — locates this skill's hazard-id clause within the bundle. | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-SNIP-HOC | Applied to **every** control recommendation (Workflow step 4): work-design organisational controls rank ABOVE individual resilience training; then verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 unit · Q2 domains · Q3 data sources · Q4 triggers · Q5 jurisdiction). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Domain-Analyst + Action-Planner + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
