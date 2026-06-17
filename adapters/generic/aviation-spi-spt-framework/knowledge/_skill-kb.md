# Knowledge-base manifest for `aviation-spi-spt-framework`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ICAO-ANNEX19 | Pillar 3 (Safety Assurance) — the SPI/SPT + safety-performance-monitoring grounding. | ../../../knowledge-base/standards/icao-annex19.md |
| KB-REG-IN-DGCA | Align SPIs to the DGCA SSP's acceptable level of safety performance (India). | ../../../knowledge-base/regulatory/in-dgca.md |
| KB-DATA-TRIR-BENCHMARKS | Rate/trend context (via incident_rates) — quote source+year, never a bare number. | ../../../knowledge-base/data-points/incident-rates-benchmarks.md |
| KB-SNIP-HOC | Hierarchy of controls where the framework recommends a control response to a breach. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The Aviation-SMS Critic/QA persona + the roster archetypes. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
