# Knowledge-base manifest for `mine-incident-investigation`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | 10.2 incident, nonconformity & corrective action backbone | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | HoC-tag the CAPA (no PPE/admin-only without justification) | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | structured intake pattern | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | B5 4-agent roster + Mine-Manager SME persona | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-MINES-ACT | Mines Act notification duty | ../../../knowledge-base/regulatory/in-mines-act.md |
| KB-REG-IN-DGMS | DGMS reportability — 24h notice + Form J (verified anchors; [GAP] elsewhere) | ../../../knowledge-base/regulatory/in-dgms.md |
| KB-REG-IN-STATEFORMS | mandatory region/zone resolution before any form | ../../../knowledge-base/regulatory/in-state-forms.md |
