# The six-block skill contract (what the forge guarantees)

> Human-readable companion to the A2 contract. This file **documents** the contract
> — it restates **no** canonical block text. The single source of truth for each
> inline block's prose is `template/blocks/<block>.md`; the forge copies it
> byte-for-byte at scaffold time, the A8 linter diffs against it (rule 1), and
> `hse-skill-forge --sync` heals any in-marker drift back to it.

Every skill in the pack — the forge included — carries the **same six mandatory
blocks**. Five are **inline** in `SKILL.md` (each fenced by a paired
`hse:block:<name>` start/end HTML comment marker); the sixth is **folder-level** (`evals/` +
`branding/company-card.yaml`). The block text is **invariant by contract** (A10
D7): legitimate per-skill variation lives *outside* the markers (the kb-selection
jurisdiction rows; the orchestration roster), never inside them.

## The five inline blocks

| Block marker | Purpose | Canonical source | Owning unit |
|---|---|---|---|
| `hse:block:deid` | Pseudonymize-by-default data protection; runs FIRST, before any drafting; a leak is a non-waivable hard auto-fail. | `template/blocks/deid.md` | A5 |
| `hse:block:kb-selection` | Read ONE matching jurisdiction fragment; apply the hierarchy of controls; quote `source`+`year`. Per-skill jurisdiction ROWS sit BELOW `:end` (presence-only). | `template/blocks/kb-selection.md` | A3 |
| `hse:block:orchestration` | Triage → plan → fan-out (MAX 6) → synthesis → MANDATORY Critic/QA; degrades to single-thread. Per-skill ROSTER sits BELOW `:end` (presence-only). | `template/blocks/orchestration.md` | A6 |
| `hse:block:report-output` | Assemble one `report.json` → render branded DOCX + PDF via the shared engine. The start marker is glued to `## Output format` on one line. | `template/blocks/report-output.md` | A4 |
| `hse:block:attribution` | Non-intrusive company-card line, after the deliverable, per `branding/company-card.yaml` `placement`. | `template/blocks/attribution.md` | A9 |

## The folder-level block

- `evals/` — `evals.json` (≥3 cases in the skill-creator schema) + `rubric.yaml`
  (the canonical `template/evals/rubric.yaml`) + `run_evals.py` (the thin A8 shim) +
  `files/` (the de-id fixture PAIR `deid-clean.md` + `deid-leak.md`). A8 quality gate.
- `branding/company-card.yaml` — the shared Eyekyam card (relative symlink →
  `../../../branding/company-card.yaml`, real-copy fallback on symlink-stripping hosts). A9.

## The structured intake is a Workflow convention, NOT a block

The §2.7 **structured runtime intake** is the multi-step Q&A that opens a skill's
Workflow at *runtime* (a user running the skill). It is a Workflow convention, not
a sixth block. The forge seeds it as a **TODO STEP only** (`templates/intake-todo.md`)
— it never invents the new skill's domain question VALUES.

## The two intakes are categorically distinct (A10 D4)

This is the single most important authoring error to avoid:

| | Forge author-interview | Seeded runtime intake STEP |
|---|---|---|
| **Whose Workflow** | the FORGE's own (`SKILL.md` §Workflow). | the NEW skill's Workflow (a seeded `<!-- TODO -->`). |
| **When it runs** | BUILD time (authoring a skill). | RUN time (a user running that skill). |
| **What it asks** | WHAT skill to build (name/category/roster/…). | the new skill's DOMAIN facts (task/site/asset). |
| **Who fills the values** | the author, answering the forge. | the author later, replacing the TODO. |
| **Source** | this skill's Workflow Step 1. | `templates/intake-todo.md` (a scaffold). |

The forge drives **build-time** subagent fan-out (one author per skill, §3.7); the
orchestration block it *seeds* drives **runtime** fan-out (a user running one skill).
Master-plan §2.4: these two subagent uses are never conflated.
