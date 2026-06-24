# Knowledge-base manifest for `electrical-permit-switching-program`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | OH&S management-system clause grounding (6.1.2 hazard ID & risk assessment) for every run | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | The hierarchy of controls applied to every switching-program control — de-energize + isolate first, PPE last; a program that authorises work un-proven / un-earthed is pushed up the hierarchy, never the program | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-ARCHETYPES | The runtime subagent archetypes (De-identifier-first + the HSE-SME-Reviewer hook) the orchestration block reuses | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-SNIP-SWITCHING-SEQUENCE | The ordered isolation → prove-dead → earthing → sanction-to-test → restore sequence; carries the full isolation / lock-off / prove-test-prove / protective-earthing / permit-to-work / sanction-to-test vocabulary, so this skill needs NO separate electrical-isolation fragment (the skill's core lever) | ../../../knowledge-base/prompt-snippets/switching-sequence.md |
| KB-SNIP-DEENERGIZE-FIRST | The de-energize-first / ESWC control spine — establish an electrically safe work condition (NFPA 70E Article 120) before any work; a PPE-led or convenience-led treatment is rejected | ../../../knowledge-base/prompt-snippets/deenergize-first.md |
| KB-STD-NFPA70E | The copyright-safe NFPA 70E Article 120 (establishing + verifying an electrically safe work condition) + Annex K + 120.5 clause→artifact structure map — the cited structural reference for the switching sequence (cite the clause/article numbers only, never the table cells) | ../../../knowledge-base/standards/nfpa-70e.md |
| KB-SNIP-UTILITIES-CLAUSE-MAP | The bundle-shared NFPA 70E Article 120 + 130.4 + 130.5 cross-walk that keeps the three hse-utilities-power skills consistent on de-energize-first | ../../../knowledge-base/prompt-snippets/utilities-clause-map.md |
| KB-REG-OSHA1910-269 | US duty — OSHA 29 CFR 1910.269 (T&D: 269(d) lockout/tagout, 269(n) protective grounding, 269(m) de-energizing) read with 1910.333 (work practices) + 1910.147 (the LOTO standard) | ../../../knowledge-base/regulatory/osha-1910-269.md |
| KB-REG-UK-EAWR | UK duty — EAWR 1989 regs 12–13 (means of cutting off supply + isolation / working dead) read with HSG85 (electricity at work — safe working practices) | ../../../knowledge-base/regulatory/uk-eawr.md |
| KB-REG-IN-ELECTRICAL | India CEA / state electricity rules + line-clearance / permit practice; defers to hse-india with mandatory state detection; emit `[GAP]`, never a national form number | ../../../knowledge-base/regulatory/in-electrical.md |
