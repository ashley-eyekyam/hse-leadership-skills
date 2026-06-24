# Knowledge-base manifest for `offshore-safety-case`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-REG-OFFSHORE-SCR | The SI 2015/398 (SCR 2015) duty → safety-case-element + SEMS map — MAH identification, ALARP demonstration, SCE register + performance standards, independent verification, emergency response; cited on every run. SI 2015/398 is current; SCR 2005 is named only as the superseded legacy reference. | ../../../knowledge-base/regulatory/offshore-scr.md |
| KB-SNIP-MARINE-CLAUSE-MAP | The marine/offshore clause-citation idiom applied when framing the safety-case argument's regulatory basis. | ../../../knowledge-base/prompt-snippets/marine-clause-map.md |
| KB-SNIP-HOC | Applied to the risk-reduction measures in the ALARP demonstration — admin/PPE-only measures flagged; higher-order inherent-safety / engineered measures first. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-REG-IN-OFFSHORE | India offshore deferral pointer (CONV-8) — OISD + PNG offshore rules; state detection mandatory for shore-base, defers to hse-india; no national form minted, unverified content stays `[GAP]`. | ../../../knowledge-base/regulatory/in-offshore.md |
| KB-STD-ISO45001 | OH&S / management-system backbone framing the SEMS description. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-INTAKE | The one-at-a-time installation / element / provenance intake the Workflow opens with. | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The moderate roster + the Process-Safety-Engineer persona reviewing the safety-case argument. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
