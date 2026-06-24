# Knowledge-base manifest for `health-safety-file`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID; 7.5 documented information) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every residual hazard's future-work (maintenance/cleaning/refurb/demolition) control | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-REG-IN-FACTORIES | India Factories Act 1948 grounding; **defers to `hse-india` with mandatory state detection; emit `[GAP]`, never a national form number** (BOCW completion records via `bocw-compliance`) | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India state-forms index — the resolved state's BOCW completion records via `hse-india`; legacy-first, no minted national form id | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-CDM2015 | **UK duty grounding — CDM 2015 (SI 2015/51) Reg 12(5)–(9) + HSE L153**: the **principal designer** prepares & maintains the H&S file (Reg 12(5)); review, update, **handover to the client at completion**, client retention (Reg 12(6)–(9)). **Attributing preparation to the wrong duty-holder, or omitting the handover duty, is a regulatory_citation_accuracy hard-fail.** | ../../../knowledge-base/regulatory/cdm-2015.md |
| KB-SNIP-HS-FILE-CONTENT | **The L153 Appendix-4 H&S-file content list** the file is built from — structure description & use · as-built & services info · residual & unusual hazards (located) · hazardous materials in situ · maintenance/demolition arrangements · information gaps — plus the **"could-not-reasonably-anticipate" residual-hazard test** (the residual-only-discipline lever) | ../../../knowledge-base/prompt-snippets/hs-file-content.md |
| KB-SNIP-CONSTRUCTION-CLAUSE-MAP | The bundle-shared **Reg 4 → 12 → 12(5)** CDM duty → artifact → skill cross-walk — the source for the **one-line cross-reference** to the PCI (Reg 4) and the CPP (Reg 12) this file completes; **the CDM trilogy stays loosely coupled, no runtime sibling dependency** | ../../../knowledge-base/prompt-snippets/construction-clause-map.md |
