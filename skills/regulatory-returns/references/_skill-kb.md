# Knowledge-base manifest for `regulatory-returns`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-REG-US-OSHA | The US branch — OSHA 29 CFR **1904** recordkeeping leg (300 log / 300A summary / 301 incident report + 1904.41 electronic submission). | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-UK-HSWA | The UK branch — **RIDDOR 2013** reportability (specified injury reg. 4/Sch. 1, over-7-day reg. 4, disease reg. 8/9, dangerous occurrence reg. 7/Sch. 2, the 15-day rule). | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-EU-OSH | The EU branch — member-state equivalent return (cite the national instrument). | ../../../knowledge-base/regulatory/eu-osh.md |
| KB-REG-IN-FACTORIES | India deferral — Factories Act statutory-return basis (read inline at tier-2 of the `hse-india` degrade; the leg routes to `factories-act-returns`). | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India deferral — state-form resolution after **mandatory state detection** (Q1a); the resolved state form is cited via `hse-india`, **never a national form number**. | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-IN-PORTALS | India deferral — statutory filing-portal pointers (Shram Suvidha + state factory/labour portals) for the routed India return. | ../../../knowledge-base/regulatory/in-portals.md |
| KB-DATA-RECORDABILITY-TESTS | The cited recordability/reportability **decision logic + deadlines** per jurisdiction (OSHA 1904 + RIDDOR); each verdict cites its test. The India row points into `hse-india` — no national form numbers. | ../../../knowledge-base/data-points/recordability-tests.md |
| KB-SNIP-RETURNS-METHOD | The **determine → form → deadline → prepare** method the Workflow applies. | ../../../knowledge-base/prompt-snippets/returns-method.md |
| KB-SNIP-OPS-CLAUSE-MAP | The bundle-shared operations ISO-45001 clause cross-walk (6.1.3 / 9.1 monitoring & compliance-obligations). | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-SNIP-HOC | Applied to any follow-up corrective control raised by the return (Workflow). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1…Q5b + the India→state branch). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source (De-identifier-first + Determination-&-Form-Preparer + Critic/QA + SME). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
