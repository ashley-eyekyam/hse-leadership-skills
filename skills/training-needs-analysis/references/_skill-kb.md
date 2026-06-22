# Knowledge-base manifest for `training-needs-analysis`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The TNA backbone — clause **7.2** (competence = education + training + experience, demonstrated) + **7.3** (awareness); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-DATA-COMPETENCE-LEVELS | The shared **4-level competence scale** (aware/trained/competent/expert) + evidence tests; every role×competence cell is banded current-vs-required against it. | ../../../knowledge-base/data-points/competence-levels.md |
| KB-SNIP-TNA-METHOD | The gap-scoring + prioritisation method (role-profiling → required competencies → current-state evidence → gap = required − current → SPOF flags → prioritise by gap × risk × legal-mandate → SMART plan). | ../../../knowledge-base/prompt-snippets/tna-method.md |
| KB-SNIP-OPS-CLAUSE-MAP | The bundle-shared ISO 45001 operations clause cross-walk — TNA owns clause **7.2** (competence); routes a user to the sibling that owns an adjacent clause (induction #14 = 7.3). | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-SNIP-HOC | Applied to frame training as an **administrative** control (Workflow step 6) — never the sole treatment of a hazard that admits a higher-order control; verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 scope … Q6 budget). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Competence-Requirement-Mapper + Gap-Scorer-&-Planner + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-UK-HSWA | The UK legal-competence row — Management of Health and Safety at Work Regulations 1999 reg. 13 (capabilities and training); the legal-required-competency source for a UK scope. | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | The US legal-competence row — standard-specific training mandates (e.g. 29 CFR 1910.132(f) PPE, 1910.147(c)(7) LOTO); the legal-required-competency source for a US scope. | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-IN-FACTORIES | The India legal-competence row — Factories Act 1948 s.7A(2)(c) (training); India **defers to `hse-india`** and resolves the state, never a national form number. | ../../../knowledge-base/regulatory/in-factories-act.md |
