# Knowledge-base manifest for `iso45001-gap-analysis`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The default clause set (4–10) the gap analysis scores against — context · leadership · planning · support · operation · performance evaluation · improvement; the binding clause requirements (the user holds the licensed standard). Cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-ISO14001 | The ISO 14001:2015 environmental clause set — substituted via the Q1 standard selector for an environmental management-system gap analysis (same clause-walk method). | ../../../knowledge-base/standards/iso-14001.md |
| KB-STD-ISO45003 | The ISO 45003:2021 psychosocial clause set — substituted via the Q1 standard selector; the psychosocial extension of ISO 45001 6.1.2 hazard-id. | ../../../knowledge-base/standards/iso-45003.md |
| KB-DATA-ISO45001-MATURITY | The **5-level conformance/maturity scale** (0 Absent → 4 Measured & improving) every clause is scored on, each level carrying an evidence test; the certification-readiness rule (mandatory clause at level ≤ 2 = certification-blocker). Quote its `source`+`year`. | ../../../knowledge-base/data-points/iso45001-maturity.md |
| KB-SNIP-GAP-PRIORITISATION | The gap-ordering method — classify each gap by severity × certification-blocking, prioritise blockers first, then high-severity, then the rest; cost + date as SMART actions traced to clause + owner. | ../../../knowledge-base/prompt-snippets/gap-prioritisation.md |
| KB-SNIP-OPS-CLAUSE-MAP | The bundle-shared ISO 45001 operations clause cross-walk (clause → owning hse-operations skill); routes a user who asks for the wrong artifact for a clause to the owning sibling. | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-SNIP-HOC | Applied to **every** control recommendation in the planning clauses (6.1) and the remediation roadmap (Workflow steps 6/7), then the no-PPE/admin-only-without-justification gate is enforced by the Critic/QA pass. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 standard selector + Q2…Q5 + the refuse-on-vague evidence anchor). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate-to-complex roster (De-identifier-first + 3 Clause-Group-Assessors + Roadmap-Synthesizer + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
