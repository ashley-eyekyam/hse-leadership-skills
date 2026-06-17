# Knowledge-base manifest for `incident-rate-calculator`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The grounding standard — clause **9.1** (monitoring, measurement, analysis & performance evaluation) is the basis for measuring a defensible lagging rate; cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-DATA-TRIR-BENCHMARKS | The industry benchmark figures a computed rate is compared against — surfaced **with its publishing body + year + sector** every time, never a bare number (the defensibility lever). Feeds `benchmark_delta`. | ../../../knowledge-base/data-points/incident-rates-benchmarks.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the lean Workflow opens with (counts → mandatory hours → period → base → optional benchmark). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source. B10 is single-threaded by design, so the block self-deactivates at runtime; the archetype reference is retained for the inline de-identifier + Critic/QA discipline. | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
| KB-REG-IN-STATEFORMS | India context — `jurisdiction: [All]` includes India, so mandatory state detection is wired and the resolved state form is consulted **only** to settle a recordability/notifiable-injury definition feeding a count (B10 computes a rate, it does not file a statutory notice). | ../../../knowledge-base/regulatory/in-state-forms.md |
