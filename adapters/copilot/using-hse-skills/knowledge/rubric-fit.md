# Rubric fit for `using-hse-skills` — the `hierarchy_of_controls` carve-out (D-02)

**Status:** documentation-only. The shared eval rubric (`evals/rubric.yaml`) is
**byte-canonical and is NOT edited** for this skill. This note records why one
model-graded dimension is **N/A** for a *routing* skill, so a low score on it is
not read as a real quality failure.

## The issue

`using-hse-skills` is a **catalog router / intent-elicitation** skill. It:

1. elicits the user's task in structured, granular questions,
2. recommends one or more repo skills across all bundles, and
3. hands the chosen skill a de-identified context capsule.

It **does not itself treat a hazard** — it applies no controls, scores no risk
matrix, and produces no residual-risk re-score. The shared HSE rubric, written for
*hazard-treatment* deliverables (risk assessments, JSAs, RAMS…), weights
`hierarchy_of_controls` as a model-graded dimension. A routing skill produces zero
hierarchy-of-controls treatment **by design**, so that dimension drags its weighted
mean below the ≥4.0 gate for a reason that has nothing to do with its actual quality.

## The carve-out (D-02 — option (a), N/A; NOT a rubric variant)

For `using-hse-skills` ONLY:

- **`hierarchy_of_controls` is N/A** — a router applies no controls; it recommends
  and hands off de-identified context. The concept of a post-control **residual
  risk** re-score is likewise N/A for the same reason (the router treats nothing, so
  there is nothing to re-score). Do **not** count these against the router's score.
- The dimensions that DO apply and ARE assessed:
  - **`specificity`** — does it elicit task/site/role specifics and route on them
    (not generic "use a risk assessment")? ✔ applies.
  - **`defensibility`** — is the recommendation traceable to the elicited facts and
    the catalog, with honest hand-off? ✔ applies.
  - **`de_identification`** (deterministic hard-fail) — the context capsule it hands
    off must be de-identified. ✔ applies, and is proven by the de-id PAIR gate.
  - **`regulatory_citation_accuracy`** (deterministic hard-fail) — any standard it
    names must be real. ✔ applies.

So the router's binding gate is: the **deterministic floor** (de-id PAIR proven,
`run_evals` exit 0, no hard-fail) PLUS `specificity` + `defensibility` ≥ 4.0. A
weighted mean pulled under 4.0 *solely* by the N/A `hierarchy_of_controls` dimension
is **not** a gate failure for this skill (ROUTE-05).

## Why documentation, not a rubric edit

`evals/rubric.yaml` is the byte-canonical shared contract (anti-drift; the linter and
every other skill depend on its exact bytes). Authoring a per-skill rubric variant
was considered and **deferred** (it can be revisited if routing skills proliferate in
a future milestone). For v1.2.0 the carve-out is recorded here and cross-referenced
from `docs/AUTHORING_GUIDE.md` §7 — the rubric file is untouched.

*Decision: D-02 (`.planning/phases/17-…/17-CONTEXT.md`). Applies to `using-hse-skills` only.*
