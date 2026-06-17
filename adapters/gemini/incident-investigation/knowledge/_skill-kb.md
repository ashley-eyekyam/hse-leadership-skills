# Knowledge-base manifest for `incident-investigation`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | Clause **10.2** (incident, nonconformity & corrective action) — the grounding standard for the RCA + CAPA structure. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to every CAPA control (the "always apply HOC" rubric line); paired with `controls.rank_controls`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured-intake pattern the §3.7 Q1–Q10 question set instantiates. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The 4-agent roster below `orchestration:end` draws its agent contracts from here. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India reporting — legacy-first state accident-notice forms (e.g. MH Form 24 within 24h) + the OSH-Code transition note; **mandatory state detection**. | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-IN-FACTORIES | India parent statute (Factories Act framing) behind the state forms. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-UK-HSWA | UK reporting — RIDDOR 2013 reportable events + timelines pointer. | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | US reporting — 29 CFR 1904 recordkeeping + 1904.39 reporting timelines (8h fatality / 24h hospitalization-amputation-eye-loss). | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-EU-OSH | EU framework reporting pointer. | ../../../knowledge-base/regulatory/eu-osh.md |
