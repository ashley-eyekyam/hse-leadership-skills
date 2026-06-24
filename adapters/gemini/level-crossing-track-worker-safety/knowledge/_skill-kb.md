# Knowledge-base manifest for `level-crossing-track-worker-safety`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows. This skill **mints no new KB** — it reuses the rail bundle's existing fragments.

| ID | Use | Path |
|---|---|---|
| KB-REG-LX-TRACKWORKER | The two engineered hierarchies: level-crossing remedial (closure → grade separation → engineering → signage/admin LAST) and track-worker protection (separation → SSOW → warning → lookout-only LAST), plus the COSS role and Sentinel competence framing. Cite NR/L2/OHS/019 + ORR LX guidance + LXRMTK by reference only (issue/date is `[ASSUMED A3]` → `[GAP]`/SME-confirmed); never reproduce the text. | ../../../knowledge-base/regulatory/lx-trackworker.md |
| KB-DATA-ALCRM-BANDS | RECORD the user's ALCRM individual/collective risk band to prioritise the crossing for remediation. Band threshold VALUES are the licensed RSSB/NR model output → never embedded, never recomputed; a missing band is `[GAP]`. A use that hard-codes numeric ALCRM thresholds is a D-03 violation. | ../../../knowledge-base/data-points/alcrm-bands.md |
| KB-SNIP-LX-HIERARCHY | The control-spine prompt that REJECTS a signage-led crossing treatment or a lookout-only-led track-work system where a higher order is reasonably practicable. The core-value lever for this skill. | ../../../knowledge-base/prompt-snippets/lx-hierarchy.md |
| KB-REG-CSM-RA | Where altering a crossing/asset is a significant change: the significance test, the three risk-acceptance principles, and the independent AsBo (change specifics `[GAP]` until supplied). | ../../../knowledge-base/regulatory/csm-ra.md |
| KB-REG-IN-RAIL | India framing (Railways Act 1989 / Commissioner of Railway Safety); state detection mandatory, state-specific content deferred to `hse-india`, no national form invented (CONV-8). | ../../../knowledge-base/regulatory/in-rail.md |
| KB-SNIP-RAIL-CLAUSE-MAP | The bundle standard→artifact→skill cross-walk: routes the sibling boundary that **RAIL-03 owns level crossings + track-worker safety** while RAIL-01 owns the SMS and RAIL-02 the ROGS application (CONV-12). | ../../../knowledge-base/prompt-snippets/rail-clause-map.md |
| KB-SNIP-HOC | Rank every crossing and track-work control through the hierarchy of controls (the SFAIRP adequacy test). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The level-crossing / track-safety Critic/QA persona + the roster archetypes. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
