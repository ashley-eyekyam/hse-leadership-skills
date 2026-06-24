# Knowledge-base manifest for `machine-guarding-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every guard recommendation — a PPE/admin-only mechanical-zone control is rejected, not the headline control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-FACTORIES | India Factories Act 1948 §21 (fencing of machinery) duty; defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-OSHA1910-O | US duty — OSHA 29 CFR 1910 Subpart O: 1910.212 (general machine guarding) + 1910.219 (mechanical power-transmission apparatus) | ../../../knowledge-base/regulatory/osha-1910-o.md |
| KB-STD-ISO12100-14120 | The ISO 12100 three-step method (inherent safe design → safeguarding → information) + the ISO 14120 guard taxonomy the assessment sits inside | ../../../knowledge-base/standards/iso12100-14120.md |
| KB-SNIP-GUARD-SELECTION | The engineering-control-led guard/device selection order (fixed → interlocked → presence-sensing → two-hand/hold-to-run → trip) governed by the access-frequency rule — the skill's core lever | ../../../knowledge-base/prompt-snippets/guard-selection.md |
| KB-REG-LOTO | REUSE (existing fragment) — the energy-source → isolation-step → verify-zero-energy map cross-referenced by the maintenance interaction mode (Q5) for lockout/tagout | ../../../knowledge-base/regulatory/loto.md |
| KB-SNIP-MANUFACTURING-CLAUSE-MAP | The ISO-45001 §6.1.2 / §8.1.2 + ISO 12100 three-step manufacturing clause cross-walk shared across the hse-manufacturing bundle | ../../../knowledge-base/prompt-snippets/manufacturing-clause-map.md |
