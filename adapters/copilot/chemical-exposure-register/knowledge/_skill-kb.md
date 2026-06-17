# Knowledge-base manifest for `chemical-exposure-register`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree.

| ID | Use | Path |
|---|---|---|
| KB-DATA-OEL-LIMITS | OEL/WEL/PEL anchors with source+year per agent | ../../../knowledge-base/data-points/oel-limits.md |
| KB-STD-ISO45001 | 6.1.2 HIRA grounding for the exposure register | ../../../knowledge-base/standards/iso-45001.md |
| KB-REG-EU-REACH | REACH exposure scenario + RMM link (EU) | ../../../knowledge-base/regulatory/eu-clp-reach.md |
| KB-REG-UK-HSWA | COSHH (UK) | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | PEL basis (US) | ../../../knowledge-base/regulatory/us-osha.md |
| KB-SNIP-HOC | rank exposure control tier (engineering before RPE) | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | structured intake pattern | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | subagent roster + Chemical-Process-Safety SME persona | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
