# Knowledge-base manifest for `pre-construction-information`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment; 8.1.2 hierarchy of controls) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every significant-hazard control the PCI surfaces for designers/contractors | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-FACTORIES | India Factories Act 1948 grounding; **defers to `hse-india` with mandatory state detection; emit `[GAP]`, never a national form number** (BOCW site information via `bocw-compliance`) | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India state-forms index — the resolved state's BOCW pre-work site information via `hse-india`; legacy-first, no minted national form id | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-CDM2015 | **UK duty grounding — CDM 2015 (SI 2015/51) Reg 4 + HSE L153**: the client's duty to provide the Pre-Construction Information *as soon as practicable* to everyone appointed/considered (Reg 4(4)), and Reg 4(5)/(6) (no construction start without arrangements/CPP). **Omitting the Reg 4 duty/timing is a regulatory_citation_accuracy hard-fail.** | ../../../knowledge-base/regulatory/cdm-2015.md |
| KB-SNIP-PCI-CHECKLIST | **The L153 Appendix-1 PCI content checklist** the pack is built from — project & client brief · existing structure · services · ground · surroundings · significant design/construction hazards · the information-gaps register (every unknown a `[GAP]`, never omitted) | ../../../knowledge-base/prompt-snippets/pci-checklist.md |
| KB-SNIP-CONSTRUCTION-CLAUSE-MAP | The bundle-shared **Reg 4 → 12 → 12(5)** CDM duty → artifact → skill cross-walk — the source for the **one-line cross-reference** to the CPP (Reg 12) this skill feeds and the H&S File (Reg 12(5)); **the CDM trilogy stays loosely coupled, no runtime sibling dependency** | ../../../knowledge-base/prompt-snippets/construction-clause-map.md |
