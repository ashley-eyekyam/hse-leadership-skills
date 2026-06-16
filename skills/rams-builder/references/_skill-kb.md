# Knowledge-base manifest for `rams-builder`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The RA-half backbone — clause **6.1.2** (hazard identification & risk assessment) + **8.1.2** (hierarchy of controls); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** control recommendation (Workflow step 4), then verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1…Q6 incl. the Q-S sequence anchor). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Researcher + Regulatory-Checker + Drafter + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-UK-HSWA | **UK construction law** — CDM 2015 **Reg 13** (principal-contractor duties), **Reg 15** (contractor duties), and the **Construction Phase Plan** linkage (Reg 12/15(4)); the RAMS frame for the role at Q6. | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-IN-STATEFORMS | **India construction law** — **BOCW** Form XXV annual return + the user's resolved **state**; **mandatory state detection** (Q1a) before citing any form; legacy-first, **never a national form number**; unseeded state → `[GAP]`. | ../../../knowledge-base/regulatory/in-state-forms.md |
| KB-REG-US-OSHA | **USA construction law** — 29 CFR 1926 (the site-specific safety plan) when the jurisdiction is USA. | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-EU-OSH | **EU** OSH framework when the jurisdiction is EU. | ../../../knowledge-base/regulatory/eu-osh.md |
