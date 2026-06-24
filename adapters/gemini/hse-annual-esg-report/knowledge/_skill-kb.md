# Knowledge-base manifest for `hse-annual-esg-report`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ESG-GRI403 | **REUSED, not minted (D-02)** — the shipped GRI 403 / SASB / ESRS S1 OH&S disclosure→artifact crosswalk. The skill selects each required disclosure from this index; no duplicate disclosure-index fragment is minted or referenced. Read on every run. | ../../../knowledge-base/standards/esg-gri-403.md |
| KB-SNIP-ESG-ASSURANCE | The assurance method applied to make every figure assurable — assurance level (limited/reasonable), reporting boundary (operational/financial/equity + own-workforce/non-employee split), data-quality (definition + denominator + source + period + completeness), double materiality, and the strictest-tier de-id (`<5` + secondary suppression). Read on every run. | ../../../knowledge-base/prompt-snippets/esg-assurance.md |
| KB-SNIP-LEADERSHIP-CLAUSE-MAP | ISO 45001:2018 leadership-cluster clause → owning skill; locates this skill at **clause 9.1** (monitoring, measurement, analysis, performance evaluation — the disclosed performance figures). | ../../../knowledge-base/prompt-snippets/leadership-clause-map.md |
| KB-DATA-TRIR-BENCHMARKS | The lagging-rate definitions/benchmarks (TRIR / DART / LTIFR) — every disclosed injury rate is computed by the `incident_rates` engine to these standard definitions/denominators (anchors TRIR 2.07 / LTIFR 6.00); quote `source`+`year`, never a bare number. | ../../../knowledge-base/data-points/incident-rates-benchmarks.md |
| KB-SNIP-HOC | Applied to any control/improvement-action narration (a published programme commitment must rank higher-order controls above PPE/admin). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (period · boundary · workforce split · assurance level · materiality basis · disclosures). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Disclosure-Mapper + Figure-Validator + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
