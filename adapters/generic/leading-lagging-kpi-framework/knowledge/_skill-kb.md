# Knowledge-base manifest for `leading-lagging-kpi-framework`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-SNIP-KPI-DESIGN | The balanced-architecture method: leading + lagging, per-indicator definition (formula·source·frequency·owner·target), anti-gaming guardrails, target-setting by maturity. The skill's core method. | ../../../knowledge-base/prompt-snippets/kpi-design.md |
| KB-DATA-LEADING-INDICATORS | The single-source leading/lagging indicator catalogue (each cited); the balanced set is built from this — never a private per-skill list. | ../../../knowledge-base/data-points/leading-indicators.md |
| KB-DATA-ROAD-SAFETY-INDICATORS | The road-safety EXTEND branch (D-01) — the ISO 39001:2012 road-safety indicator set; consumed only when the intake selects a road / transport / fleet scope. This skill is its single home. | ../../../knowledge-base/data-points/road-safety-indicators.md |
| KB-SNIP-LEADERSHIP-CLAUSE-MAP | The bundle-shared ISO 45001 leadership clause cross-walk (CONV-10); this skill is the primary owner of clause 9.1 (monitoring, measurement, analysis & performance evaluation). | ../../../knowledge-base/prompt-snippets/leadership-clause-map.md |
| KB-STD-ISO45001 | The OH&S management-system backbone; clause 9.1 is the regulatory anchor for the balanced indicator set. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied wherever a leading indicator implies a control action (a measure must rank above admin/PPE; never a PPE-only treatment). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-question-at-a-time scope / subject / indicator / target intake the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The moderate roster + the HSE-Performance / Assurance-Manager SME persona hook. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |

> Lagging rates are **computed** by the `scripts/hse_components/incident_rates` engine to standard definitions (anchors TRIR 2.07 / LTIFR 6.00), never invented in-prompt. This skill *designs / normalises* the indicator set — it is distinct from `incident-rate-calculator` (computes given rates) and `process-safety-kpi` (API RP 754 tiers) / `aviation-spi-spt-framework` (ICAO Annex 19), which it references as domain exemplars, not replacements.
