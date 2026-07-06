---
sme-review:
  personas:
    - role: "HSE practice lead / catalog steward"
      expertise: "The full HSE skill catalog and its bundles, the elicitation taxonomy and the shared-fact carry-over contract, the hierarchy-of-controls dependency between artifacts (RA → JSA → permit → toolbox talk), de-identification of handoff context, and where a request belongs (which single skill vs. an ordered chain)."
      lens: "Does this routing send the user to the RIGHT skill(s) in the RIGHT order for the stated intent — a complete, correctly-sequenced chain, no clear single-skill request hijacked into a full elicitation, and a run sheet whose context is de-identified and whose every dependent step attaches the prior skill's output?"
modes:
  run-sheet:
    detected_by: "The router's recommendation output — after intent + the six shared facts are echoed back and confirmed, it recommends the ordered chain and composes the run sheet. This single run-sheet mode is the router's only produced artifact (Open Question 2: no separate roadmap-doc mode is emitted)."
    floor:
      - id: ordered-chain-with-why
        description: "The recommended chain is complete, correctly ordered by dependency (risk-assessment -> job-safety-analysis -> permit-to-work -> toolbox-talk), and each step carries a one-line WHY tying it to the elicited intent (ROUTE-03)"
        anchors: ['recommended chain|ordered chain|\bordered\b', '\bwhy\b']
        min_matches: 2
      - id: context-capsule-once
        description: "ONE de-identified Context Capsule (the Step-0 facts + the SEQUENCE MAP) is emitted once at the top of the run sheet — not a per-step full-context repeat"
        anchors: ['context capsule', 'sequence map']
        min_matches: 2
      - id: carry-in-facts
        description: "The shared carry-over facts (jurisdiction -> state, industry, exposed population) ride the handoff so the user enters them once and each downstream skill reuses them"
        anchors: ['jurisdiction|\bstate\b', 'industry', 'exposure|exposed']
        min_matches: 2
      - id: per-step-attach-prior-output
        description: "Each Step 2+ is a lean continuation prompt that ATTACHES the named prior skill OUTPUT and states the dependency/feeds link — not just the original elicited context (D-03/D-04)"
        anchors: ['attach', 'dependency|feeds']
        min_matches: 2
      - id: deid-persist-durable
        description: "The captured facts are de-identified FIRST, and the run sheet is PERSISTED as a durable artifact (a file path on a file-capable host, or a delimited save-block on a chat-only host)"
        anchors: ['de.identif', 'saved run sheet|persist|run.sheet']
        min_matches: 2
      - id: clearance-gate-before-step1
        description: "The persisted run sheet is PRESENTED before Step 1 (file-first ordering), and the Step-1 skill runs ONLY on the user's explicit clearance ('go' / 'proceed' / 'run step 1'); an edit routes back and re-persists (R2/R3; the 16.1 GAP-3 fix)"
        anchors: ['clearance|proceed|run step 1', 'before step 1|review this before']
        min_matches: 1
---

# SME Review & Sign-off — using-hse-skills (catalog router)

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into an HSE practice lead / catalog steward. The router produces
no traditional HSE artifact — it routes — so the reviewer checks the *routing quality* (the
right chain, no hijack, a clean handoff) rather than the controls of a single deliverable.
The universal hard gates (de-id leak, citation accuracy, owned-and-dated handoff) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The recommended chain is **complete and correctly ordered** — the right skills for the stated intent, in a defensible dependency sequence (e.g. risk-assessment before job-safety-analysis before permit-to-work before toolbox-talk); a missing prerequisite step, or a step out of dependency order, is a FLAG.
- [ ] **No clear single-skill request was hijacked** — an unambiguous single-artifact request ("write a toolbox talk for tonight's shift") is pointed straight at that skill, not dragged through a full router elicitation; over-triggering on a request that names its own artifact is a FLAG (D-06).
- [ ] The run sheet's **de-identification and prior-output handover are present** — the shared context is pseudonymized to role labels (`[SITE-1]`, `[ROLE: site manager]`, `[CONTRACTOR]`) BEFORE it is written into any step, and every step 2+ `CARRY-IN` explicitly instructs the user to ATTACH the prior skill's OUTPUT (not just the original elicited context); a verbatim identifier in a step block, or a dependent step that omits the attach-prior-output instruction, is a FLAG (D-03/D-04).
- [ ] Each recommended skill carries a **one-line WHY** tying it to the elicited intent / success-criteria — a recommendation with no rationale, or a rationale that does not match the captured facts, is a FLAG (ROUTE-03).
- [ ] The **mandatory India→state** branch was honoured — an India request routed to a form-bearing skill without the state confirmed first is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints. This skill is the catalog ROUTER, not a hazard
artifact — the floor tests routing quality, not the controls of a single deliverable.

Skill-specific blind spots (where this routing artifact has actually gone hollow):
- **The hijacked single-skill request** — a request that names its own artifact ("write a
  toolbox talk for tonight") dragged through a full router elicitation instead of pointed
  straight at that skill (D-06 over-triggering).
- **The incomplete or mis-ordered chain** — a missing prerequisite (a permit recommended with
  no risk-assessment first) or a step out of dependency order.
- **The hollow run sheet** (the 16.1 GAP-3 failure) — a polished run sheet whose continuation
  prompts repeat the original context but do NOT attach the prior skill's OUTPUT, and/or omit
  the carry-in facts, so each dependent step starts cold.
- **The identifier in the handoff** — a verbatim name/site/phone surviving into the Context
  Capsule, a continuation prompt, or the persisted run-sheet file (the filename must be a
  role-label slug, never a verbatim name/site).
- **The auto-fired Step 1** — Step 1 invoked before the user cleared it, or the run sheet not
  persisted and presented before Step 1 runs (the file-first, clearance-gated ordering).
- **The India state skipped** — an India request routed to a form-bearing skill without the
  state confirmed first.

## Sign-off note
SME review: ran (persona: HSE practice lead / catalog steward); this is **decision-support
only**. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs the affirmative claim "approved by a competent person".
A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id
leak, invented citation, weighted score below threshold) are a separate enforcement class.
