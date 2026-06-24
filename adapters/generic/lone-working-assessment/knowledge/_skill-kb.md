# Knowledge-base manifest for `lone-working-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows. This skill **mints no new KB** — it reuses the renewables fragments authored in 16-01 and Phase 11.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every lone-working run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every lone-working control — eliminate the solitary exposure first, device last; a device-led treatment is pushed up the hierarchy, never the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The structured one-question-at-a-time intake pattern the Workflow opens with (forcing specificity — the named role/site + the specific solitary activity) | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-LONE-WORKING | The lone-working risk-assessment duty map (HSE INDG73 rev 4): explicit risk-assessment duty, reliable coverage-checked communication, scheduled check-ins + a missed-check-in escalation procedure, violence + stress/wellbeing — the cited structural reference for the lone-working RA | ../../../knowledge-base/regulatory/lone-working.md |
| KB-STD-BS8484 | The lone-worker device-service conformance map (BS 8484:2022): the conformant device, the monitored alarm-receiving/response chain, and the discipline that a device supplements — never replaces — the check-in / escalation procedure | ../../../knowledge-base/standards/bs8484.md |
| KB-SNIP-CHECKIN-ESCALATION | The lone-working control spine (the skill's core lever): eliminate the solitary exposure first → coverage-checked comms → scheduled check-ins + a missed-check-in escalation path → device residual-only; a coverage gap is a control failure, a device-led treatment is rejected | ../../../knowledge-base/prompt-snippets/checkin-escalation.md |
| KB-SNIP-RESCUE-PLAN | The shared (REN-01 + REN-02) rescue-plan-mandatory spine — a tested, team-owned, timed rescue before work at height / foreseeable-rescue lone work; "call the emergency services" is not the rescue plan; routes lone WAH to REN-01's two-person baseline | ../../../knowledge-base/prompt-snippets/rescue-plan.md |
| KB-SNIP-RENEWABLES-CLAUSE-MAP | The bundle-shared renewables standard → artifact → owning skill cross-walk (CONV-10) that keeps the renewables skills consistent (REN-01 owns WAH+rescue; REN-02 owns lone working; REN-03 owns weather thresholds) | ../../../knowledge-base/prompt-snippets/renewables-clause-map.md |
| KB-REG-IN-RENEWABLES | India renewables/lone-working deferral pointer — defers to the `hse-india` engine with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-renewables.md |

**Cross-referenced by path (not minted, not re-stated here):** the renewables hazard library `../../../knowledge-base/hazard-library/renewables.md` (the single home of the renewables lone-working / WAH / electrical hazard categories, built Phase 11; all three renewables skills cross-reference it).
