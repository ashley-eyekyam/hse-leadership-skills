# Knowledge-base manifest for `ergonomics-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The OH&S backbone — clause **6.1.2** (hazard identification & assessment of MSD/ergonomic risks); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** control recommendation: task/workstation redesign and engineering before PPE **and before training**; verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-REG-IN-FACTORIES | India regulatory basis — Factories Act 1948 health provisions; **India defers to `hse-india`**, mandatory state detection; a state form/return owed is a literal `[GAP]`, never a minted national form number. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-STD-ISO11228 | The ergonomics method scope — ISO 11228-1 (lifting & carrying) / -2 (pushing & pulling) / -3 (low loads at high frequency) + the manual-handling decision flow; the method facts the RULA/REBA/NIOSH scores (the `ergonomics` engine's output) are interpreted against. | ../../../knowledge-base/standards/iso11228.md |
| KB-SNIP-ERGO-CONTROLS | The MSD control hierarchy applied to every control: eliminate the handling → engineer the workstation / mechanise / add an aid → administrative rotation/limits → training LAST, with the "training is not a control for a biomechanical overload" rule. | ../../../knowledge-base/prompt-snippets/ergo-controls.md |
| KB-SNIP-MANUFACTURING-CLAUSE-MAP | The hse-manufacturing ISO-45001 clause cross-walk (§6.1.2 hazard/risk assessment · §8.1.2 operational control) referenced for the regulatory-basis section. | ../../../knowledge-base/prompt-snippets/manufacturing-clause-map.md |
