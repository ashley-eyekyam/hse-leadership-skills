# Knowledge-base manifest for `contractor-prequalification`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The prequalification backbone — clause **8.1.4** (procurement / contractors / outsourcing); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-REG-UK-HSWA | UK jurisdiction — HSWA s.3/s.4 duties to non-employees, and **CDM 2015 reg. 8** (duty to appoint only those with the skills/knowledge/experience) where the work is construction. | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | US jurisdiction — the **OSHA multi-employer worksite policy (CPL 02-00-124)**: controlling-employer duty over contractor safety. | ../../../knowledge-base/regulatory/us-osha.md |
| KB-SNIP-HOC | Applied when evaluating the contractor's proposed controls / safe system of work; high-hazard (T3) work cannot pass on PPE/competence claims alone. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 scope&risk … Q5 decision type). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Evidence-Verifier + Scorer-&-Recommender + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-DATA-CONTRACTOR-TIERS | The **risk-tier → PQQ-depth → pass-threshold map** (T1 low / T2 medium / T3 high-hazard); tier set by the highest-risk activity; sets the PQQ depth and the pass threshold. | ../../../knowledge-base/data-points/contractor-tiers.md |
| KB-SNIP-PQQ-BANK | The **evidence-anchored PQQ question bank by tier** — each question tied to its required verifiable evidence; never score a self-asserted claim. | ../../../knowledge-base/prompt-snippets/pqq-bank.md |
| KB-SNIP-OPS-CLAUSE-MAP | The hse-operations clause cross-walk (ISO 45001 operations clause → owning skill) — locates this skill at clause **8.1.4**. | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-REG-IN-STATEFORMS | India state-form resolution — `jurisdiction: [All]` includes India, so mandatory state detection (Q4a) is wired; the resolved state form is cited, **never a national form number**. | ../../../knowledge-base/regulatory/in-state-forms.md |
