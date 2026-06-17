# Knowledge-base manifest for `aviation-sms-builder`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ICAO-ANNEX19 | The four-pillar SMS framework — the backbone of every section of the manual. | ../../../knowledge-base/standards/icao-annex19.md |
| KB-REG-IN-DGCA | Align the SMS to the DGCA State Safety Programme where the jurisdiction is India (CAR number `[GAP]`, never invented). | ../../../knowledge-base/regulatory/in-dgca.md |
| KB-SNIP-HOC | Rank every Pillar-2 risk mitigation through the hierarchy of controls. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The Aviation-SMS Critic/QA persona + the roster archetypes. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
