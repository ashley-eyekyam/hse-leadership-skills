# Knowledge-base manifest for `traffic-management-plan`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment; 8.1.2 hierarchy of controls) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every residual traffic control — a **"hi-vis + banksman only" pedestrian control is flagged PPE/admin-led and pushed up the hierarchy** | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-TRAFFIC-SEGREGATION | **The segregation-by-design control hierarchy** (CDM 2015 Reg 27 + Schedule 3 + HSE HSG144): eliminate the conflict / design out reversing → one-way & turning → physical segregation → signage / speed / lighting → banksman LAST. Read **every run**; the core-value lever for this skill | ../../../knowledge-base/prompt-snippets/traffic-segregation.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-CDM2015 | UK construction grounding — **CDM 2015 Reg 27** (organise the site so pedestrians and vehicles move safely) + **Schedule 3** (traffic routes — suitable / sufficient / separated, warning of approach): the **traffic-routes row** added to this fragment in 14-01 | ../../../knowledge-base/regulatory/cdm-2015.md |
| KB-REG-OSHA1926 | US duty grounding — **OSHA 29 CFR 1926 Subpart O** (motor vehicles, mechanised equipment & marine operations) + 1926.601 / .602 (site traffic / equipment access) | ../../../knowledge-base/regulatory/osha-1926.md |
| KB-SNIP-CONSTRUCTION-CLAUSE-MAP | The bundle-shared CDM duty → artifact → skill cross-walk — the **Reg 27 + Schedule 3 → Traffic Management Plan** row that places this skill in the hse-construction document chain (loosely coupled, no runtime sibling dependency) | ../../../knowledge-base/prompt-snippets/construction-clause-map.md |
| KB-REG-IN-FACTORIES | India Factories Act 1948 grounding; **defers to `hse-india` with mandatory state detection; emit `[GAP]`, never a national form number** | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India state-forms index — the resolved state's site-traffic obligation via `hse-india`; legacy-first, no minted national form id | ../../../knowledge-base/regulatory/in-state-forms.md |
