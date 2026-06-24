# Knowledge-base manifest for `arc-flash-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every arc-flash control — de-energize first, arc-rated PPE last; a PPE-led treatment is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-DEENERGIZE-FIRST | The de-energize-first / ESWC / energized-work-justification control spine — establish an electrically safe work condition (NFPA 70E Article 120) before any reliance on arc-rated PPE; convenience-justified energized work is rejected (the skill's core lever) | ../../../knowledge-base/prompt-snippets/deenergize-first.md |
| KB-STD-NFPA70E | The copyright-safe NFPA 70E (130.4 / 130.5 / 130.5(G) / 130.5(H) / 130.7(C)(15) / Article 120) + IEEE 1584-2018 clause→artifact map + the PPE-category breakpoint structure (1.2/4/8/25/40 cal/cm²) — the cited structural reference for the engine-computed result (NOT a substitute for the computation) | ../../../knowledge-base/standards/nfpa-70e.md |
| KB-SNIP-UTILITIES-CLAUSE-MAP | The bundle-shared NFPA 70E Article 120 + 130.4 + 130.5 cross-walk that keeps the three hse-utilities-power skills consistent on de-energize-first | ../../../knowledge-base/prompt-snippets/utilities-clause-map.md |
| KB-REG-IN-ELECTRICAL | India CEA / state electricity rules; defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-electrical.md |
