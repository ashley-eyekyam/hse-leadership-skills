# Knowledge-base manifest for `toolbox-talk`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

B3's KB surface is intentionally **lean** (Decision 5): a toolbox talk briefs a crew, it does not file a statutory form, so it needs the ISO 45001 management-system backbone (7.4/5.4) + the hierarchy-of-controls discipline + the intake pattern + the topic hazard facts — not a heavy per-jurisdiction citation table.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The management-system basis for a toolbox talk — clause **7.4 (communication: information, instruction & briefing)** + **5.4 (consultation & participation of workers)**; cited on every run. The talk *is* the operational realisation of 7.4/5.4. Also **8.1.2 (hierarchy of controls)** when controls are stated → `KB-SNIP-HOC`. | ../../../knowledge-base/standards/iso-45001.md |
| KB-SNIP-HOC | Applied **prompt-side** whenever controls are stated (Workflow step 4): rank elimination → substitution → engineering → administrative → PPE, and justify any PPE/admin-only treatment. B3 wires **no** `controls.py` — for the ~2 controls a talk names, the prompt-side discipline is sufficient (the A7↔A3 boundary: B3 uses the *words*, not the *code*). | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch-on-answers, echo-back intake pattern the lean ~6–7-question intake (Q1…Q7) instantiates; also the never-invent / refuse-on-vague discipline. | ../../../knowledge-base/prompt-snippets/intake-interview.md |

**Topic hazard facts** — the relevant `data-points/` fragment(s) selected by intake Q1 (e.g. working-at-height, confined-space hazard facts) supply the concrete hazards in talk element 3; each figure quoted with its `source`+`year`. The "Other (free-text)" topic path degrades to general hazard framing when no matching fragment exists (recorded `[GAP]`, never invented).
