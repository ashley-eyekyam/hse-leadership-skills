# CONTRACT-PROOF — `risk-assessment` fixture vs. the A2 §5 linter rules

This document proves **CONTRACT-05** (the six-block A2 skill contract is
*satisfiable*) and **CONTRACT-04** (the per-skill folder-layout contract is
demonstrable) by hand-walking all ten A2 §5 linter rules against the fixture in
this directory, `examples/risk-assessment/`.

## Why a hand-walk

**There is no executable linter in Phase 1.** A8 builds `lint_skills.py` /
`validate_repo_skill.py` (the shared module that enforces these ten rules) in
**Phase 3**. Per **D-09**, this proof is therefore a *documented hand-walk*: each
rule below is checked manually against the fixture and recorded **PASS** with
concrete, reproducible evidence.

**The one exception is Rule 1** (block byte-identity), which is proven
**executably** — not by a manual diff claim — by running the parameterized
Plan-03 helper `_blockcheck.py` against this fixture. That tool extracts the
fixture's five marked regions and diffs each byte-for-byte against the canonical
`template/blocks/*.md`, exiting nonzero on any drift. The A8 linter will subsume
exactly this check as Rule 1.

Run every command below from the **public-repo root** (`hse-leadership-skills/`)
unless noted. The fixture itself is the proof artifact.

## Hard gates vs. warnings (A2 §5)

Per A2 §5, rules **1–6, 8, 9 are HARD CI gates** (exit nonzero → blocks merge);
rules **7 and 10 are WARNINGS** (advisory, do not block). This fixture passes all
ten, hard gates and warnings alike.

## The 10-rule hand-walk

| Rule | Check | Proof method | Evidence | Verdict |
|------|-------|--------------|----------|---------|
| **1 — Block markers + canonical match** *(HARD)* | All five inline `hse:block:*` markers present; each invariant core byte-identical to `template/blocks/*.md`. | **Executable** — `python3 .planning/phases/01-repo-scaffold-skill-contract/_blockcheck.py hse-leadership-skills/examples/risk-assessment/SKILL.md` (run from the private build-repo root, where `_blockcheck.py` lives). | Prints `OK: all 5 blocks byte-identical (…/examples/risk-assessment/SKILL.md)` and **exits 0**. `grep -c "hse:block:.*:start" SKILL.md` → **5**. | **PASS** |
| **2 — Orchestration roster** *(HARD)* | A non-empty "Subagent roster for THIS skill" subsection exists **below** the `hse:block:orchestration:end` marker (presence-only; never diffed). | Inspect SKILL.md after the `orchestration:end` line. | The "### Subagent roster for THIS skill" subsection names **Risk Scorer / Control Adviser / Regulatory Checker / Critic-QA** and a single-threaded fallback — non-empty, below `:end`. | **PASS** |
| **3 — Folder layout** *(HARD)* | `references/`, `assets/`, `evals/{evals.json,rubric.yaml,run_evals.py,files/}`, `branding/company-card.yaml` all present. | `find examples/risk-assessment -type f` + dir listing. | Present on disk: `references/{METHODOLOGY.md,deid-checklist.md,QUALITY_CHECKLIST.md}`, `assets/.gitkeep`, `scripts/.gitkeep`, `evals/{evals.json,rubric.yaml,run_evals.py,files/.gitkeep}`, `branding/company-card.yaml`. | **PASS** |
| **4 — `name`** *(HARD)* | `name` equals the folder name, lowercase + hyphens, ≤64 chars. | Compare frontmatter `name` to the folder; regex `^[a-z0-9-]+$`; length. | `name: risk-assessment` == folder `risk-assessment`; matches `^[a-z0-9-]+$`; 15 chars ≤ 64. | **PASS** |
| **5 — `description`** *(HARD)* | ≤1024 chars; third-person (no first-person pronouns `I/we/my/our`). | `len()` of the parsed `description` value; `\b(I\|we\|my\|our)\b` grep. | Description is **324 chars** ≤ 1024; pronoun grep returns **[]** (none). | **PASS** |
| **6 — `metadata`** *(HARD)* | All required keys present; values in the controlled vocabularies; `plugin` resolves to a registered bundle. | Validate the `metadata` map against `template/metadata.schema.json` with `jsonschema.Draft202012Validator`. | Validator returns **NONE** (no errors). All required keys present; `category: risk-assessment`, `tier: 1`, `audience: [M,C,F]`, `industry: [All]`, `jurisdiction: [All]`, `status: stable`, `plugin: hse-core` — all in vocab. *(plugin-registry cross-check is wired by A8/CI in Phase 3; `hse-core` is the canonical bundle.)* | **PASS** |
| **7 — Body length** *(WARNING)* | Warn approaching ~400 lines; fail >500. | `wc -l SKILL.md`. | **191 lines** — well under the 400-line warn threshold. | **PASS** |
| **8 — Dead reference links** *(HARD)* | Every `references/…` path cited in the body resolves on disk. | Extract every `` `references/…` `` token from the body; `test -f` each. | Cited: `references/METHODOLOGY.md`, `references/deid-checklist.md`, `references/QUALITY_CHECKLIST.md` — **all three exist**. The body cites **no** unresolved path (the template's `_skill-kb.md` pointer, an A3/Phase-2 artifact, is intentionally NOT cited here so this rule passes). | **PASS** |
| **9 — KB resolution** *(HARD)* | Every `../../knowledge-base/…` path and `_registry.yaml` ID the skill **names** must resolve. | Inspect the body for real KB paths/IDs. | The skill **names no resolvable KB path or registry ID** — KB content is Phase 2 (A3). The single literal `../../knowledge-base/<facet>/<fragment>.md` present is the **schematic placeholder inside the byte-identical `kb-selection` block** (literal `<facet>`/`<fragment>` angle-bracket tokens, not a named path). The rule resolves only paths the skill actually names; there are none, so it **passes trivially**. See note below. | **PASS** |
| **10 — No time-sensitive phrasing** *(WARNING)* | No absolute dates / "as of" / "currently" in the body. | `grep -ni "as of\|currently\|20[0-9][0-9]" SKILL.md`. | Returns **no matches**. | **PASS** |

## Note on Rule 1 ↔ Rule 9 reconciliation

A literal `grep -c "../../knowledge-base" SKILL.md` returns **1**, not 0 — because
the mandatory `hse:block:kb-selection` block is copied **byte-identically** from
`template/blocks/kb-selection.md` (Rule 1, a HARD gate) and that canonical block
contains the schematic example row `` `../../knowledge-base/<facet>/<fragment>.md` ``.

Byte-identity (Rule 1) is non-negotiable, so the placeholder row cannot be edited
out of the fixture. Rule 9, correctly read, resolves only `../../knowledge-base/…`
paths the skill **names** as real fragments. The `<facet>/<fragment>.md` token has
literal angle-bracket placeholders — it is a schematic, not a named path, and A3
fills the real `(law, state) → fragment` rows in Phase 2. **No real KB path is
named**, so Rule 9 passes. The A8 linter (Phase 3) must treat the angle-bracketed
schematic inside the canonical block as a non-path; this fixture is the reference
case confirming the two hard gates (1 and 9) are jointly satisfiable.

## Result

All ten A2 §5 rules — eight hard gates (1–6, 8, 9) and two warnings (7, 10) —
**PASS** against `examples/risk-assessment/`. The six-block contract is
**satisfiable** (CONTRACT-05) and the per-skill folder-layout contract is
**demonstrable** (CONTRACT-04). When A8 lands `lint_skills.py` in Phase 3, this
fixture is the ready-made dry-run target for A2 §8 AC5.
