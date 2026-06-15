# Methodology — scaffold → validate → handoff (the forge's build-time method)

The forge's "domain method" is **authoring a new skill**, not analysing an HSE task.
It runs the author-interview, scaffolds a born-conformant skeleton, validates it
against the same linter CI runs, and hands the author the list of TODOs to fill.

## 1. Author-interview → answers.json

Run the ten-question interview (SKILL.md §Workflow Step 1) one question at a time,
branching and echoing facts back. Serialize to an `answers.json`:

- `metadata{}` — the nine required keys, vocab-validated against
  `template/metadata-vocab.yaml` (see `templates/metadata-stub.yaml`).
- `description` — the one-line domain framing (third-person, ≤1024 chars).
- `roster` — `single-thread` | `moderate` | `flagship-b5`
  (`references/orchestration-patterns.md`).
- `a7_components` — the deterministic engines the skill calls, or omit for none
  (no `scripts/` is created, the B3 shape).
- `kb_ids` — the `KB-…` fragments the skill grounds in (the `_skill-kb.md` manifest).

## 2. Scaffold (born-conformant by construction)

`scripts/scaffold.py --name <name> --answers <answers.json>`:

- copies the five inline blocks **byte-for-byte** from `template/blocks/*` (no second
  source of truth — A10 D1); seeds the runtime intake as a **TODO STEP only**;
- builds vocab-validated frontmatter; emits the folder skeleton (`references/`,
  `assets/`, `evals/` with the de-id fixture pair, `branding/` link); wires the A7
  symlink + verbatim `_shim.py` only when components are declared;
- **self-lints and refuses exit 0** unless its own output lints clean.
- `--from-skill-creator <draft.md>` wraps a skill-creator domain draft; `--standalone`
  uses the `templates/*` fallback skeletons.

## 3. Validate (identical to CI)

`scripts/validate_repo_skill.py <skill>` — the re-export of `lint_skills.py` (the SAME
module CI runs, so a skill can never pass the forge but fail CI). `--sync` re-pulls any
drifted canonical block from `template/blocks/*` and prints a unified diff (it never
silently overwrites; below-`:end` rosters/rows are left untouched — A10 D5/D7).

## 4. Handoff

Emit `assets/forge-handoff.template.json` listing the seeded TODOs the author must
fill: the domain body (`references/METHODOLOGY.md`), the intake question VALUES (the
seeded STEP), the eval `expectations`, and the de-id fixtures specific to the skill.
The skill is contract-clean from birth; the author fills the domain, then runs the
A8 eval gate (`evals/run_evals.py`) locally before pushing.
