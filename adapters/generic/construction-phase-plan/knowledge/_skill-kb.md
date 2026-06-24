# Knowledge-base manifest for `construction-phase-plan`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment; 8.1.2 hierarchy of controls) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every activity control — **work at height leads with collective protection; a PPE-led WAH control (harnesses, no collective protection) is flagged and pushed up the hierarchy** | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-FACTORIES | India Factories Act 1948 grounding; **defers to `hse-india` with mandatory state detection; emit `[GAP]`, never a national form number** (BOCW state form via `bocw-compliance`) | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India state-forms index — the resolved state's BOCW return via `hse-india`; legacy-first, no minted national form id | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-CDM2015 | **UK duty grounding — CDM 2015 (SI 2015/51) Reg 12(1)–(4) + Schedule 3 + HSE L153 ACOP**: the principal/sole contractor's duty to draw up the CPP before the construction phase, the review duty, and the F10 / Reg 12 notification position | ../../../knowledge-base/regulatory/cdm-2015.md |
| KB-REG-OSHA1926 | US duty grounding — **OSHA 29 CFR 1926 Subpart C** (accident-prevention responsibilities / site-specific safety programme) as the US-jurisdiction CPP-equivalent | ../../../knowledge-base/regulatory/osha-1926.md |
| KB-SNIP-CPP-STRUCTURE | **The proportionate CPP content skeleton (Reg 12(1)–(2))** the plan is built from — project description & programme · management & arrangements · site rules · significant risks & controls by activity (hierarchy-ranked) · notification status · review schedule | ../../../knowledge-base/prompt-snippets/cpp-structure.md |
| KB-SNIP-CONSTRUCTION-CLAUSE-MAP | The bundle-shared **Reg 4 → 12 → 12(5)** CDM duty → artifact → skill cross-walk — the source for the **one-line cross-reference** to the PCI (Reg 4) this skill consumes and the H&S File (Reg 12(5)) it feeds; **the CDM trilogy stays loosely coupled, no runtime sibling dependency** | ../../../knowledge-base/prompt-snippets/construction-clause-map.md |
