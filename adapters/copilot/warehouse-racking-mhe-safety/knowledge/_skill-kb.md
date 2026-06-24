# Knowledge-base manifest for `warehouse-racking-mhe-safety`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-EN15635-SEMA | The BS EN 15635:2008 + SEMA inspection-regime + RAG-action map: the PRRS appointment, the weekly-visual + ≥12-monthly-expert inspection cadence, the SWL load-notice duty, and the SEMA Red/Amber/Green damage-classification with the matching action (Red = immediate off-load + isolate) | ../../../knowledge-base/standards/en15635-sema.md |
| KB-REG-MHE-PIT | The powered-industrial-truck duty→control map (OSHA 1910.178 / PUWER / L117 / HSG136): operator competence + pre-use inspection + ENGINEERED pedestrian-vehicle segregation by design before "look out for forklifts" | ../../../knowledge-base/regulatory/mhe-pit.md |
| KB-SNIP-RACKING-MHE | The skill's core lever — the SWL-design + inspection-regime + engineered-segregation-first control spine; a hi-vis/"inspect carefully" headline control is rejected and pushed up the hierarchy; a Red finding without an immediate off-load is rejected; an assumed SWL/tolerance/interval is rejected → `[GAP]` | ../../../knowledge-base/prompt-snippets/racking-mhe.md |
| KB-SNIP-LOGISTICS-CLAUSE-MAP | The bundle-shared standard→artifact→skill cross-walk (EN 15635/SEMA + OSHA 1910.178/PUWER → LOG-02) that locates this skill within the hse-logistics-transport bundle; single source, never duplicated | ../../../knowledge-base/prompt-snippets/logistics-clause-map.md |
| KB-REG-IN-MTW | India logistics deferral pointer (Motor Transport Workers Act 1961 + Factories-Act-as-warehouse + flagged OSH Code 2020 transition); mandatory state detection; defers all form/return content to `hse-india`; emit `[GAP]`, never a national form number (CONV-8) | ../../../knowledge-base/regulatory/in-mtw.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every racking/MHE recommendation — a hi-vis/admin-only treatment of a collapse/struck-by risk is rejected, not the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
