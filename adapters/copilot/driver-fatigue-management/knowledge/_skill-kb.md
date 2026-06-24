# Knowledge-base manifest for `driver-fatigue-management`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every fatigue control — roster/journey-plan/built-in-rest (FRMS) redesign first, "stay alert" / in-cab alertness gadget last; an alertness-led treatment is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-INTAKE | The structured one-question-at-a-time intake pattern the Workflow opens with (forcing specificity) | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-FATIGUE-FRMS | The schedule-redesign-first fatigue-control spine (the skill's core lever): redesign roster/route/journey-plan and build in rest before any "stay alert" briefing or in-cab alertness gadget; HOS computed by fatigue.py, never narrated; a multi-day cycle / cross-shift claim without the cumulative log is a [GAP] | ../../../knowledge-base/prompt-snippets/fatigue-frms.md |
| KB-SNIP-LOGISTICS-CLAUSE-MAP | The bundle-shared FMCSA HOS / EU 561 + FRMS → driver-fatigue-management cross-walk that keeps the logistics-transport skills consistent (HOS computed by fatigue.py; India via KB-REG-IN-MTW) | ../../../knowledge-base/prompt-snippets/logistics-clause-map.md |
| KB-REG-FMCSA-HOS | The combined US FMCSA Hours-of-Service (49 CFR Part 395) + EU Regulation (EC) 561/2006 drivers'-hours duty→limit-category→artifact citation map (a single fragment, never split) — the cited structural reference for the engine-computed HOS flags (NOT a substitute for the computation; numeric limits are LOCKED constants in fatigue.py) | ../../../knowledge-base/regulatory/fmcsa-hos.md |
| KB-REG-IN-MTW | India Motor Transport Workers Act 1961 + Factories-Act-as-warehouse + flagged OSH Code 2020 transition; defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-mtw.md |
