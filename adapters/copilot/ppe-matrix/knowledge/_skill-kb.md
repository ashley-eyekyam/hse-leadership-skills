# Knowledge-base manifest for `ppe-matrix`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The OH&S backbone — clause **6.1.2** (hazard identification & risk assessment) framing the body-region hazard assessment; cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** hazard before any PPE row — eliminate / substitute / engineer / administrative **before** PPE; the controls-first gate is built on it and verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-PPE-MATRIX-LOGIC | **The literal spine** — the residual-hazard-only PPE-selection logic + the controls-first gate (higher-order controls applied/justified before PPE; a hazard with none flagged, not given a PPE row). | ../../../knowledge-base/prompt-snippets/ppe-matrix-logic.md |
| KB-DATA-PPE-STANDARDS | The EN/ANSI conformity standard per PPE category — **REUSED, never re-authored**; every PPE row cites its standard + year, never asserts protection without it. | ../../../knowledge-base/data-points/ppe-standards.md |
| KB-REG-OSHA1910-I | The US PPE duty map — 1910.132(d)(1) PPE hazard assessment + the **mandatory 1910.132(d)(2) written certification** + body-region sections (.133/.135/.136/.138). | ../../../knowledge-base/regulatory/osha-1910-i.md |
| KB-REG-OSHA1910-O | The machinery/operational-control cross-reference where PPE sits as the residual control after machine guarding (Subpart O). | ../../../knowledge-base/regulatory/osha-1910-o.md |
| KB-REG-IN-FACTORIES | India regulatory basis — Factories Act 1948 PPE provisions; **India defers to `hse-india`**, mandatory state detection; a state form/return owed is a literal `[GAP]`, never a minted national form number. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-SNIP-MANUFACTURING-CLAUSE-MAP | The hse-manufacturing ISO-45001 clause cross-walk (§6.1.2 hazard/risk assessment · §8.1.2 operational control) referenced for the regulatory-basis section. | ../../../knowledge-base/prompt-snippets/manufacturing-clause-map.md |
