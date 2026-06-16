# Knowledge-base manifest for `board-safety-report`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The grounding standard — clause **9.1** (monitoring & performance evaluation — the indicators) + **9.3** (management review — the board structure the narrative serves); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-ISO14001 | The **optional** environmental-performance line ONLY (intake Q9 = Yes) — clause **9.1.2** (evaluation of compliance); a single line, NOT a full ESG branch (D-02). | ../../../knowledge-base/standards/iso-14001.md |
| KB-DATA-TRIR-BENCHMARKS | The benchmark figures performance is compared against — surfaced **with its publishing body + year + sector** every time, never a bare number (the defensibility lever). | ../../../knowledge-base/data-points/incident-rates-benchmarks.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1…Q10). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first → Data-Synthesizer + Narrative-Drafter → Critic/QA; the Synthesizer composes the Benchmarker + Synthesizer archetypes). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India context — `jurisdiction: [All]` includes India, so mandatory state detection is wired and the resolved state form cited **only if** a statutory figure is referenced (B9 is a narrative skill, not a statutory-notice skill). | ../../../knowledge-base/regulatory/in-state-forms.md |
