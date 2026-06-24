# Knowledge-base manifest for `induction-pack`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The binding clauses the induction satisfies — **7.2 (competence)** and **7.3 (awareness)**: workers competent and aware of the hazards and arrangements that affect them. Cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-REG-UK-HSWA | The UK legal-induction baseline — MHSWR 1999 reg. 10 (information for employees) + reg. 13 (capabilities & training); read when Q5 = UK. | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | The US legal-induction baseline — OSH Act s.5(a)(1) General Duty Clause + standard-specific orientation/training duties; read when Q5 = USA. | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-IN-FACTORIES | The India legal-induction baseline — Factories Act 1948 s.111A (worker right to information); read when Q5 = India, deferring to `hse-india` for the state detail (no national form number minted). | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-SNIP-INDUCTION-BASELINE | The **mandatory induction-topic baseline** (emergency · welfare · site rules · site-specific hazards · incident/concern reporting) the named site's specifics are layered onto; a generic induction is refused; every induction produces a competence-verification record. The core domain snippet — read every run. | ../../../knowledge-base/prompt-snippets/induction-baseline.md |
| KB-DATA-COMPETENCE-LEVELS | The shared **4-level competence scale** (aware / trained / competent / expert) with the evidence test per level; sets the **verification level** each inductee/role must reach on the verification record. Quote its `source`+`year`. | ../../../knowledge-base/data-points/competence-levels.md |
| KB-SNIP-OPS-CLAUSE-MAP | The bundle-shared ISO 45001 operations clause cross-walk (induction = 7.3 awareness); routes a user who asks for the wrong artifact for a clause to the owning sibling (e.g. competence-matrix → `training-needs-analysis`). | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-SNIP-HOC | Applied to **every** site-specific hazard's control in the induction (never a PPE-only line) and to the refresher remediation; the no-PPE/admin-only-without-justification gate is enforced by the Critic/QA pass. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 audience + Q2 named site + the refuse-on-vague site/hazard anchor). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the single-thread-by-default roster (De-identifier-first + Content-Assembler on the fan-out-to-2 variant + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
