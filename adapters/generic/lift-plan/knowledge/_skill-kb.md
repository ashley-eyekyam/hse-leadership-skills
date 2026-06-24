# Knowledge-base manifest for `lift-plan`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment; 8.1.2 hierarchy of controls) for every run — the risk half reuses the `risk-assessment` HIRA loop | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every proximity / ground control — **an overhead-line hazard leads with elimination / engineered exclusion; a PPE-only "operatives to take care" overhead-line control is flagged and pushed up the hierarchy** | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-DATA-LIFT-CATEGORIES | **BS 7121 basic / standard / complex classification thresholds + the SWL-at-radius utilisation test + the overhead-line / ground proximity tests** — each value is **transcribed from the manufacturer's rated-capacity chart (or GS6) and checked against these thresholds, never computed** (D-08a) | ../../../knowledge-base/data-points/lift-categories.md |
| KB-REG-CDM2015 | UK construction grounding where the lift is part of construction works — CDM 2015 (the lifting operation sits under the Construction Phase Plan) | ../../../knowledge-base/regulatory/cdm-2015.md |
| KB-REG-OSHA1926 | US duty grounding — **OSHA 29 CFR 1926 Subpart CC** (cranes & derricks in construction) + Subpart H (rigging) | ../../../knowledge-base/regulatory/osha-1926.md |
| KB-SNIP-CONSTRUCTION-CLAUSE-MAP | The bundle-shared CDM duty → artifact → skill cross-walk — the **LOLER Reg 8 / BS 7121 → Lifting Plan** row that places this skill in the hse-construction document chain (loosely coupled, no runtime sibling dependency) | ../../../knowledge-base/prompt-snippets/construction-clause-map.md |
| KB-REG-IN-FACTORIES | India Factories Act 1948 grounding; **defers to `hse-india` with mandatory state detection; emit `[GAP]`, never a national form number** | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India state-forms index — the resolved state's crane / lifting rules via `hse-india`; legacy-first, no minted national form id | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-LOLER-BS7121 | **LOLER 1998 Reg 8** (plan / organise / supervise) + **Reg 9** (thorough examination) + **BS 7121** lift categorisation, appointed-person role, SWL-at-radius / exclusion-zone method — the lifting-specific citation map (the skill's primary legal authority) | ../../../knowledge-base/regulatory/loler-bs7121.md |
