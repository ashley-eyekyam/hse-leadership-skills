# Knowledge-base manifest for `safety-authorisation`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows. **This skill mints NO unique new KB** — it reuses the rail bundle's existing fragments (RAIL-02 authors no KB; the application-pack structure lives in this skill's `references/`).

| ID | Use | Path |
|---|---|---|
| KB-REG-ROGS | The ROGS 2006 route map (infrastructure manager → safety authorisation; transport operator → safety certificate; non-mainline → Part-3 verification) + the SMS duties the application pack packages and submits. | ../../../knowledge-base/regulatory/uk-rogs.md |
| KB-REG-CSM-RA | The change-evidence limb of the pack — the significance test, the three risk-acceptance principles, and the independent AsBo (live change details `[GAP]` until supplied). RAIL-02 references this method for change-related authorisation evidence; it does not rebuild the SMS. | ../../../knowledge-base/regulatory/csm-ra.md |
| KB-REG-IN-RAIL | India framing (Railways Act 1989 / Commissioner of Railway Safety); state detection mandatory, state-specific non-railway-depot content deferred to `hse-india`, no national form invented (CONV-8). | ../../../knowledge-base/regulatory/in-rail.md |
| KB-SNIP-RAIL-CLAUSE-MAP | The bundle standard→artifact→skill cross-walk: routes the application route test and the boundary that **RAIL-02 references RAIL-01's SMS rather than rebuilding it** (RAIL-03 owns level crossings). | ../../../knowledge-base/prompt-snippets/rail-clause-map.md |
| KB-SNIP-HOC | Rank every risk-control-summary mitigation through the hierarchy of controls (the SFAIRP adequacy test). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured intake pattern that opens the Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The rail-ORR-submission Critic/QA persona + the roster archetypes. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
