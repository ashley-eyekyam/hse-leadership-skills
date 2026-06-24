# Knowledge-base manifest for `patient-handling-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every patient-handling control — eliminate the manual lift first, technique/PPE (back belt) last; a manual-lift recommendation where a mechanical aid is available, or a "good technique / back belt" headline, is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-STD-SPHM | Safe patient handling & mobility — ANA SPHM 8-standard move-toward-zero programme structure + ISO/TR 12296 method + NIOSH safe-lift; mechanical aids and environment design precede manual technique; residual risk on risk_matrix 5×5, NOT a NIOSH-equation engine | ../../../knowledge-base/standards/sphm.md |
| KB-REG-UK-MHOR | UK duty: Manual Handling Operations Regulations 1992 reg 4 (avoid → assess (suitable & sufficient) → reduce) + the Schedule 1 TILE factors (Task, Individual, Load, Environment) + reg 4(2) review — the regulation→duty→artifact citation map (cite the regulation numbers + TILE, never paste the wording) | ../../../knowledge-base/regulatory/uk-mhor.md |
| KB-SNIP-TILE-PEOPLE | The patient-handling assessment + control gate — avoid the manual lift → assess by TILE (Task/Individual/Load/Environment) → reduce, moving toward zero manual lift with mechanical aids as default; manual lifting last resort; handling-injury reporting small-cell-suppressed (the skill's core lever) | ../../../knowledge-base/prompt-snippets/tile-people.md |
| KB-SNIP-HEALTHCARE-CLAUSE-MAP | The bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent | ../../../knowledge-base/prompt-snippets/healthcare-clause-map.md |
