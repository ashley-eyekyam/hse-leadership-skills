# Knowledge-base manifest for `business-continuity-plan`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows. This skill **reuses the Phase-11-shipped `KB-STD-ISO22301`** (D-02) — it never re-authors the standard fragment, and it adds no new engine (the RTO<MTPD rule is a checklist constraint).

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO22301 | The BCMS backbone — the ISO 22301:2019 clause -> artifact map (8.2.2 BIA / 8.2.3 risk assessment / 8.3 strategies / 8.4 plans / 8.5 exercise); cited on every run. **Reused, not re-authored.** | ../../../knowledge-base/standards/iso-22301.md |
| KB-SNIP-BIA-METHOD | The domain method this skill follows — BIA -> impact-over-time -> MTPD -> RTO/RPO derivation -> dependency-covering strategies -> plan + deputies + exercise + ERP cross-ref. | ../../../knowledge-base/prompt-snippets/bia-method.md |
| KB-DATA-RTO-RPO-GUIDANCE | The recovery-objective banding + the **RTO < MTPD** margin discipline; an RTO with no MTPD basis or RTO >= MTPD is invalid (checklist constraint, not an engine). | ../../../knowledge-base/data-points/rto-rpo-guidance.md |
| KB-SNIP-OPS-CLAUSE-MAP | The bundle-shared ISO 45001 operations clause cross-walk — routes a user to the right sibling and anchors the **BCP <-> ERP boundary** (`emergency-response-plan` owns the 8.2 incident response). | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
| KB-SNIP-HOC | Applied to every **preventive** continuity control (eliminate the single point of failure before merely mitigating it), then verified. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 scope + BCP-vs-ERP gate -> Q6c). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-ARCHETYPES | The subagent-roster archetype source for the moderate roster (De-identifier-first + BIA-Analyst + Strategy-&-Objectives + Plan-Assembler + SME + Critic/QA). | ../../../knowledge-base/prompt-snippets/subagent-archetypes.md |
