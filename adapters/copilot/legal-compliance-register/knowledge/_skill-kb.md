# Knowledge-base manifest for `legal-compliance-register`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The register backbone — clause **6.1.3** (legal & other requirements) + **9.1.2** (evaluation of compliance); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-REG-UK-HSWA | UK obligation set — HSWA 1974 + MHSWR 1999; the UK Obligation-Mapper confirms applicability per activity. | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | US obligation set — OSH Act + the applicable 29 CFR 1910/1926 standards for the named activities. | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-EU-OSH | EU obligation set — Framework Directive 89/391/EEC; cite member-state transposition for binding forms. | ../../../knowledge-base/regulatory/eu-osh.md |
| KB-REG-IN-FACTORIES | India statutory framing (Tier-2 inline read) — Factories Act 1948; the state forms resolve via KB-REG-IN-STATEFORMS. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India **mandatory state detection** — the resolved state form/return/portal; the India leg defers to hse-india; **never a national form number** ([GAP] until resolved). | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-IN-OSH-CODE | India OSH Code 2020 transition note — flagged alongside the legacy state form (the legacy form is the primary answer). | ../../../knowledge-base/regulatory/in-osh-code.md |
| KB-SNIP-HOC | Applied to any control raised against a compliance gap (Workflow step 5), then verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 jurisdiction multi-select + the India→state branch). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate, by-jurisdiction roster (De-identifier-first + per-jurisdiction Obligation-Mappers + Register-Synthesizer + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-LEGAL-REGISTER-METHOD | The #20 method — applicability determination (confirm, not just list) → evidence mapping → gap/owner/review-date → 9.1.2 evaluation; India defers to hse-india. | ../../../knowledge-base/prompt-snippets/legal-register-method.md |
| KB-DATA-OBLIGATION-FAMILIES | The activity → obligation-family lookup per jurisdiction (UK/US/EU rows + India→hse-india pointer); every row an applicability prompt confirmed at use time. | ../../../knowledge-base/data-points/obligation-families.md |
| KB-SNIP-OPS-CLAUSE-MAP | The bundle-shared ISO 45001 operations clause cross-walk (6.1.3/9.1.2 → this skill); single source, referenced not duplicated. | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
