# Knowledge-base manifest for `noise-exposure-health-surveillance`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The OH&S backbone — clause **6.1.2** (hazard identification & assessment of noise/health risks); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** control recommendation: source/substitution and engineering before **hearing protection**; verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-REG-IN-FACTORIES | India regulatory basis — Factories Act noise provisions; **India defers to `hse-india`**, mandatory state detection; emit a literal `[GAP]`, never a national form-id. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-OSHA1910-95 | US regulatory basis — OSHA 29 CFR 1910.95: the **85 dBA** action level (hearing-conservation program + audiometry) and the **90 dBA** PEL, 8-hr TWA; cited (authority+year) for a US site. | ../../../knowledge-base/regulatory/osha-1910-95.md |
| KB-STD-ISO1999-9612 | The measurement / estimation **method** — ISO 9612:2009 (occupational-noise measurement) + ISO 1999:2013 (NIHL estimation). The skill **transcribes** the measured value against the cited threshold; it does **not** compute dosimetry (D-08a). | ../../../knowledge-base/standards/iso1999-9612.md |
| KB-SNIP-NOISE-CONTROL-HIERARCHY | The noise-specific control hierarchy — eliminate/substitute the source → engineering enclosure/damping → distance/time admin → **hearing protection LAST**; **HPD as the first/only control ≥ 85 dBA is flagged**. | ../../../knowledge-base/prompt-snippets/noise-control-hierarchy.md |
| KB-SNIP-MANUFACTURING-CLAUSE-MAP | The hse-manufacturing ISO-45001 clause cross-walk (§6.1.2 / §8.1.2 noise-risk + operational control); referenced for the regulatory-basis section. | ../../../knowledge-base/prompt-snippets/manufacturing-clause-map.md |
