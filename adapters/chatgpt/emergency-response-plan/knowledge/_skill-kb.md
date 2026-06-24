# Knowledge-base manifest for `emergency-response-plan`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | Clause 8.2 — emergency preparedness & response (the ERP grounding clause); 8.1.2 → hierarchy of controls | ../../../knowledge-base/standards/iso-45001.md |
| KB-REG-US-OSHA | 29 CFR 1910.38 Emergency Action Plans; 1910.157/1910.165 alarms & extinguishers | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-UK-HSWA | Regulatory Reform (Fire Safety) Order 2005 art. 15 emergency procedures; DSEAR 2002 where flammable atmospheres | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-IN-FACTORIES | Factories Act 1948 s.41B on-site emergency plan for MAH installations (India → state via hse-india) | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-SNIP-HOC | Apply prevention-first hierarchy to every scenario — prevention/elimination before the plan relies on response | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The runtime structured-intake pattern (one question at a time, refuse-on-vague) | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ERP-SCENARIOS | The credible-scenario catalogue + per-scenario response-procedure skeletons (prevention-first, alarm, actions, roles+deputies, muster, responder interface, recovery+BCP link) | ../../../knowledge-base/prompt-snippets/erp-scenarios.md |
| KB-DATA-DRILL-FREQ | Drill frequencies by scenario / site-class, each with a cited source+year (the dated drill schedule); [GAP] where unresolved | ../../../knowledge-base/data-points/drill-freq.md |
| KB-SNIP-OPS-CLAUSE-MAP | The hse-operations bundle ISO 45001 clause cross-walk (8.2 → this skill) | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
