# Knowledge-base manifest for `hse-skill-forge`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The
A8 linter cross-checks every ID against the named folder's `_registry.yaml` and
every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in
step with the `kb-selection` rows.

The forge is a build-time authoring tool — it grounds in the **authoring** snippets
(the subagent archetype menu it seeds rosters from, and the runtime-intake pattern
it seeds the intake STEP from), not in jurisdiction advice fragments.

| ID | Use | Path |
|---|---|---|
| KB-SNIP-ARCHETYPES | The roster-authoring menu the forge seeds below `orchestration:end` (see references/orchestration-patterns.md). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-INTAKE | The §2.7 runtime-intake pattern the forge seeds as a TODO STEP into every scaffolded skill's Workflow. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
