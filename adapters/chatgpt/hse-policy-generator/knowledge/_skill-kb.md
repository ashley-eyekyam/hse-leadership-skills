# Knowledge-base manifest for `hse-policy-generator`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-SNIP-POLICY-COMMITMENTS | The five mandatory ISO 45001 clause-5.2 commitments + clause-5.2 characteristics + variant selector + the anti-boilerplate context-fit test; the policy is assembled FROM this fragment. | ../../../knowledge-base/prompt-snippets/policy-commitments.md |
| KB-SNIP-LEADERSHIP-CLAUSE-MAP | The bundle ISO 45001 leadership clause cross-walk (5.1/5.2/5.4/9.1 → owning skill); routes a wrong-artifact request to the owning sibling. | ../../../knowledge-base/prompt-snippets/leadership-clause-map.md |
| KB-STD-ISO45001 | Grounds the policy in ISO 45001:2018 clause 5.2 (OH&S policy) — the default standard selector. | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-ISO14001 | ISO 14001:2015 clause 5.2 environmental-policy variant (Q1 selector). | ../../../knowledge-base/standards/iso-14001.md |
| KB-STD-ISO45003 | ISO 45003:2021 psychosocial policy-commitment variant (Q1 selector). | ../../../knowledge-base/standards/iso-45003.md |
| KB-SNIP-HOC | The hazard-elimination/risk-reduction commitment (commitment 3) is phrased up the full hierarchy of controls — never PPE-/admin-only. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured refuse-on-vague intake pattern the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
