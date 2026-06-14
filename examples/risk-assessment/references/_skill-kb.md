# Knowledge-base manifest for `risk-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The
A8 linter cross-checks every ID against the named folder's `_registry.yaml` and
every path against the on-disk tree; `hse-skill-forge --sync` (A10, Phase 4) keeps
this list in step with the `kb-selection` rows.

## Standards (jurisdiction-independent — always grounded)

| ID | Clause / use | Path |
|---|---|---|
| KB-STD-ISO45001 | 6.1.2 hazard ID & risk assessment (the HIRA core) | ../../../knowledge-base/standards/iso-45001.md |

## Prompt snippets (always applied)

| ID | Use | Path |
|---|---|---|
| KB-SNIP-HOC | hierarchy-of-controls ranking on every control recommendation | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | structured intake interview pattern (Workflow) | ../../../knowledge-base/prompt-snippets/intake-interview.md |

## Jurisdiction fragments (resolved at runtime from the kb-selection rows)

| ID | When | Path |
|---|---|---|
| KB-REG-IN-FACTORIES | India site — statutory OH&S framing | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-REG-IN-STATEFORMS | India site — state form lookup after mandatory state detection | ../../../knowledge-base/regulatory/in-state-forms.md |

> The fixture demonstrates an India-grounded HIRA: it reads `KB-STD-ISO45001`
> (always), applies `KB-SNIP-HOC` (always), and resolves `KB-REG-IN-STATEFORMS`
> after detecting the state. The AC8 dry-run (`tests/test_kb_resolution.py`)
> asserts every path here resolves on disk and every `KB-…` ID exists in its
> folder's `_registry.yaml`.
