# Forge output — scaffolded skill: `toolbox-talk`

This is the artifact the forge EMITS for the request: a born-conformant
`skills/toolbox-talk/` directory, scaffolded single-threaded (no fan-out), no A7
components, category `training`, audience F. The forge produces NO HSE artifact —
no talk, no risk assessment — it produces the *next skill's* contract-clean
skeleton for the author to fill.

## Author-interview echo (captured BEFORE scaffolding)

The forge ran its own build-time Q&A (one question at a time) and echoed these
captured facts back before writing anything. These are the FORGE's questions about
WHAT to build — never the new skill's runtime domain questions.

| Question | Captured answer |
|---|---|
| Skill name | `toolbox-talk` |
| One-line domain | a short, site/task-specific frontline safety talk + sign-off sheet |
| Category | `training` |
| Audience | F (frontline) |
| Industry | All |
| Jurisdictions | All |
| Single-thread vs roster | single-thread (no subagents) |
| A7 components | none (no `scripts/`) |
| Trigger keywords | toolbox talk, safety briefing, pre-task talk |
| Tier + status | tier 2, beta |

## Scaffolded folder skeleton (every reference resolves on disk)

```
skills/toolbox-talk/
  SKILL.md                         # 10 sections, 5 inline blocks byte-matching template/blocks/*
  references/
    METHODOLOGY.md                 # TODO scaffold — author the talk method
    QUALITY_CHECKLIST.md           # TODO scaffold — the pre-output gate
    deid-checklist.md              # A5 checklist (resolved)
    _skill-kb.md                   # KB fragments this skill resolves
  assets/                          # (no report-engine override; uses shared engine)
  evals/
    evals.json                     # A8-shaped skeleton (≥3 cases, de-id fixture pair)
    rubric.yaml                    # canonical template/evals/rubric.yaml
    files/deid-clean.md            # de-id fixture pair (clean)
    files/deid-leak.md             # de-id fixture pair (seeded leak)
  branding/company-card.yaml       # A9 editable card
```
No `scripts/` directory is scaffolded — the author selected no A7 components, so
the orchestration roster stays single-threaded and the report-output block uses
the shared engine unchanged.

## Scaffolded `skills/toolbox-talk/SKILL.md` (frontmatter + structure)

```yaml
---
name: toolbox-talk
description: >
  Produces a short, site- and task-specific frontline toolbox talk plus a
  sign-off sheet for a named activity — forcing the specifics and the hierarchy
  of controls, never a generic copy-paste briefing.
license: Apache-2.0
metadata:
  author: eyekyam
  version: "1.0"
  category: training        # vocab-validated against template/metadata-vocab.yaml
  tier: 2
  audience: [F]
  industry: [All]
  jurisdiction: [All]
  status: beta
  plugin: hse-core
  hse_reviewed_by: ""
  hse_reviewed_date: ""
---
```

The ten sections are all present. The five inline blocks — `deid`, `kb-selection`,
`orchestration`, `report-output`, `attribution` — are copied **byte-for-byte** from
`template/blocks/*` (the forge never re-types block text; it copies the canonical
source, so `lint_skills.py` rule-2 byte-diff passes born-clean).

The roster subsection (authored BELOW the orchestration `:end` marker, presence-only)
reads:

> - Single-threaded by design — no subagents. (Frontline ~2-min artifact: the
>   triage gate stays single-threaded; the Critic/QA pass still runs in this context.)

The seeded §2.7 runtime intake is a **TODO STEP only** (`templates/intake-todo.md`):

```
1. **TODO** — first intake question (the specific task / activity / subject).
2. **TODO** — second intake question (the named site / asset / scope).
3. **TODO** — remaining domain questions; never proceed on vague or missing inputs.
```

The forge does NOT invent the toolbox-talk's domain question VALUES — the two
intakes are categorically distinct and are never conflated (A10 D4). The author
fills these VALUES later.

## Authoring-conformance summary

- **Born-conformant / lint-clean.** The scaffolded `skills/toolbox-talk/` passes
  `lint_skills.py` with zero hand-edits: 10 sections present, 5 inline blocks
  present and correctly marked, metadata vocab-validated, folder skeleton complete.
- **Blocks byte-identical.** All five `hse:block:*` regions match `template/blocks/*`
  exactly — copied from the canonical source, not re-typed (anti-drift rule holds).
- **Intakes not conflated.** The forge's author-interview captured WHAT to build;
  the new skill's §2.7 runtime intake is seeded as a TODO STEP with no invented
  domain VALUES (A10 D4 — the single most important error avoided).
- **References resolve (no dead links).** Every `references/*` and KB pointer
  resolves on disk; rule-8 dead-reference check passes.
- **Specificity** rests on the captured answers being reflected in the skeleton
  (name, category `training`, audience F, single-thread, no `scripts/`), not a
  generic shell. **Defensibility** rests on a clean, fillable skeleton with no
  dead links — every TODO is a labelled author hand-off, not a broken reference.
- **Hierarchy of controls: N/A.** The forge is a build-time scaffolder, not an
  HSE-advice skill — it emits no controls and ranks no hazards. HoC is a structural
  non-fit; the grade rests on AUTHORING conformance above, not on control ranking.
  (The scaffolded skill will apply `KB-SNIP-HOC` at *its* runtime; the forge only
  seeds that pointer, it does not exercise it.)
