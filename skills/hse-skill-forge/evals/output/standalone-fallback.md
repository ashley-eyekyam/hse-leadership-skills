# Forge output — scaffolded skill: `permit-to-work` (standalone fallback)

This is the artifact the forge EMITS for the request when `skill-creator` is NOT
installed: a born-conformant `skills/permit-to-work/` directory, scaffolded from the
standalone `templates/*` fallback skeletons (`workflow-skeleton.md`,
`intake-todo.md`, `metadata-stub.yaml`). The absence of `skill-creator` never blocks
scaffolding and never yields a non-conformant skill — the inline blocks come from
`template/blocks/*`, not from `skill-creator`, so the skill is contract-clean by
construction. The forge produces NO HSE artifact — it produces the *next skill's*
fillable skeleton.

## Environment detection

```
> Probing for skill-creator … NOT FOUND in this environment.
> Falling back to the standalone templates/* skeletons (A10 §3.3):
>   templates/workflow-skeleton.md   → SKILL.md Workflow spine
>   templates/intake-todo.md         → seeded §2.7 runtime-intake STEP
>   templates/metadata-stub.yaml     → frontmatter starter (vocab-validated)
> The five inline blocks are copied from template/blocks/* regardless of path,
> so the output is born-conformant whether or not skill-creator drafted a body.
```

## Author-interview echo (captured BEFORE scaffolding)

The forge's own build-time Q&A (one question at a time) captured and echoed back:

| Question | Captured answer |
|---|---|
| Skill name | `permit-to-work` |
| One-line domain | a task/site-specific permit-to-work certificate for a named high-risk activity |
| Category | `compliance` |
| Audience | M (manager), F (frontline) |
| Industry | All |
| Jurisdictions | All |
| Single-thread vs roster | moderate fan-out (2–3 jobs) |
| A7 components | none (no `scripts/`) |
| Trigger keywords | permit to work, hot work permit, confined-space permit |
| Tier + status | tier 1, stable |

## Scaffolded folder skeleton (standalone path — every reference resolves)

```
skills/permit-to-work/
  SKILL.md                         # from workflow-skeleton.md + 5 blocks byte-matching template/blocks/*
  references/
    METHODOLOGY.md                 # TODO scaffold — author the permit method
    QUALITY_CHECKLIST.md           # TODO scaffold — the pre-output gate
    deid-checklist.md              # A5 checklist (resolved)
    _skill-kb.md                   # KB fragments this skill resolves
  assets/
  evals/
    evals.json                     # A8-shaped skeleton (≥3 cases, de-id fixture pair)
    rubric.yaml                    # canonical template/evals/rubric.yaml
    files/deid-clean.md
    files/deid-leak.md
  branding/company-card.yaml       # A9 editable card
```

## Scaffolded `skills/permit-to-work/SKILL.md` (frontmatter + structure)

```yaml
---
name: permit-to-work
description: >
  Produces a task- and site-specific permit-to-work certificate for a named
  high-risk activity — forcing the specific isolation, controls, and the
  hierarchy of controls, with named owners and validity windows.
license: Apache-2.0
metadata:
  author: eyekyam
  version: "1.0"
  category: compliance      # vocab-validated against template/metadata-vocab.yaml
  tier: 1
  audience: [M, F]
  industry: [All]
  jurisdiction: [All]
  status: stable
  plugin: hse-core
  hse_reviewed_by: ""
  hse_reviewed_date: ""
---
```

All ten sections present. The five inline blocks — `deid`, `kb-selection`,
`orchestration`, `report-output`, `attribution` — are copied **byte-for-byte** from
`template/blocks/*` (NOT from `skill-creator`, which is absent). The Workflow spine
is seeded from `templates/workflow-skeleton.md` as a labelled TODO body for the
author to replace with the real permit method.

The roster subsection (presence-only, below the orchestration `:end` marker) reads:

> - Moderate fan-out (2–3 jobs): e.g. an isolation/lock-out analyst and a controls
>   reviewer, with the De-identifier running FIRST and a mandatory Critic/QA pass.
>   (Author refines the named jobs here.)

The seeded §2.7 runtime intake is a **TODO STEP only** (`templates/intake-todo.md`),
with no invented permit-to-work domain VALUES — the two intakes are never conflated
(A10 D4). The METHODOLOGY and QUALITY_CHECKLIST are likewise seeded as labelled
domain-TODO scaffolds for the author to fill.

## Authoring-conformance summary

- **Standalone fallback worked.** `skill-creator` was detected absent; the forge used
  the `templates/*` fallback skeletons and still emitted a contract-clean skill —
  the absence never blocked scaffolding or produced a non-conformant result.
- **Born-conformant / lint-clean.** `lint_skills.py` passes with zero hand-edits:
  10 sections, 5 inline blocks present and marked, metadata vocab-validated.
- **Blocks byte-identical.** All five `hse:block:*` regions match `template/blocks/*`
  exactly — copied from the canonical source, independent of the skill-creator path.
- **Every reference resolves (rule-8 passes).** Each `references/*` pointer, KB
  fragment, and seeded TODO scaffold resolves on disk — no dead links. The TODOs
  (METHODOLOGY, QUALITY_CHECKLIST, the intake STEP) are labelled author hand-offs,
  not broken references. **Defensibility** = a clean, fillable skeleton with no dead
  links.
- **Intakes not conflated.** The author-interview captured WHAT to build; the new
  skill's §2.7 runtime intake is a seeded TODO STEP with no invented domain VALUES.
- **Hierarchy of controls: N/A.** The forge is a build-time scaffolder, not an
  HSE-advice skill — it emits no controls and ranks no hazards. HoC is a structural
  non-fit; the grade rests on AUTHORING conformance (born-conformant, blocks
  byte-identical, fallback path clean, no dead links), not on control ranking.
