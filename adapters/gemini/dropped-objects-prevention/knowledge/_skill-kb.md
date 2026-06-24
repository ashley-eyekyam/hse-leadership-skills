# Knowledge-base manifest for `dropped-objects-prevention`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-REG-DROPS | The dropped-objects duty: survey → static/dynamic taxonomy → reliable-securing hierarchy → exclusion-zone map (DROPS Recommended Practice 2017 / DROPS Reliable Securing / IADC HSE Guidelines Section 16 / API RP 2D & RP 54). Citation map only; the DROPS Calculator consequence-band table is licensed → cite-only | ../../../knowledge-base/regulatory/drops.md |
| KB-DATA-DROPS-IMPACT | The PUBLIC impact-energy method `E ≈ m·g·h` (mass + fall height user-supplied) + generic band LABELS only; the licensed DROPS Calculator threshold VALUES stay `[GAP]` / user-confirmed (A1 `[ASSUMED]`). The skill records the user's band, never recomputes the licensed table or hard-codes boundaries | ../../../knowledge-base/data-points/drops-impact.md |
| KB-SNIP-DROPS-SECURING | The control-hierarchy spine — survey + reliable securing + exclusion zones FIRST; a "hard hats for those below" treatment is rejected (PPE-led), an at-height item with no recorded securing standard is rejected, a band asserted with hard-coded licensed thresholds is rejected. The skill's core lever | ../../../knowledge-base/prompt-snippets/drops-securing.md |
| KB-SNIP-MARINE-CLAUSE-MAP | The bundle-shared standard → artifact → owning-skill cross-walk (DROPS RP → dropped-objects-prevention MAR-02; PFEER/SOLAS → marine-emergency-response MAR-03; SI 2015/398 → offshore-safety-case MAR-01); single source, never duplicated | ../../../knowledge-base/prompt-snippets/marine-clause-map.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every dropped-object control recommendation — a "hard hats below" / PPE-led treatment of an unsecured at-height item is rejected, not the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-REG-IN-OFFSHORE | India offshore duty — defers to `hse-india` with mandatory state detection; emit `[GAP]`, never a national form number (CONV-8) | ../../../knowledge-base/regulatory/in-offshore.md |
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
