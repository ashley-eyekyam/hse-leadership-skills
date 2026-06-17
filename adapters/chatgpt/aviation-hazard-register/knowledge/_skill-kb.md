# Knowledge-base manifest for `aviation-hazard-register`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ICAO-ANNEX19 | Pillar 2 (Safety Risk Management) — the hazard-ID + risk-assessment grounding. | ../../../knowledge-base/standards/icao-annex19.md |
| KB-DATA-AVI-RISK-MATRIX | The ICAO 5×5 MatrixConfig passed to risk_matrix.score() for initial + residual ratings. | ../../../knowledge-base/data-points/aviation-risk-matrix.md |
| KB-SNIP-HOC | Rank every mitigation through the hierarchy of controls (flag PPE/admin-only). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The Aviation-SMS Critic/QA persona + the roster archetypes. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
