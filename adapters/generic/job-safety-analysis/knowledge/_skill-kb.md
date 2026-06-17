# Knowledge-base manifest for `job-safety-analysis`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The JSA backbone — clause **6.1.2** (hazard identification & assessment of risks, applied **per step**) + **8.1.2** (hierarchy of controls); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied to **every** per-step control recommendation (Workflow step 5), then verified per step by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1…Q11; the job + step-sequence free-text anchors are the spine). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + Researcher + Regulatory-Checker + Drafter + Critic/QA; no Risk-Scorer). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India state-form resolution — `jurisdiction: [All]` includes India, so mandatory state detection (Q1a) is wired; the resolved state form is cited, **never a national form number**. | ../../../knowledge-base/regulatory/in-state-forms.md |

This skill is **safety-only** — it has **no `KB-STD-ISO14001` dependency** (no environmental-aspects branch; Decision 8). For UK construction work the JSA cites the CDM 2015 rows in `KB-REG-UK-HSWA` (reg. 13 / reg. 15 / Construction Phase Plan) via the `kb-selection` UK row; India-facing runs must resolve the state (Q1a) before citing any form.
