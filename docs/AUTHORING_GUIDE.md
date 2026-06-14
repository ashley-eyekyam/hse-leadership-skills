# Authoring Guide

The human contract for authoring an HSE Leadership skill. This is the
machine-readable contract's prose companion: it documents what every skill must
satisfy so a contribution clears the linter, the evals, and competent-person
review. Some sections are filled by the units that own their detail; those carry
a `<!-- filled by AX -->` anchor.

---

## 1. The six-block contract

Every `SKILL.md` is a fixed 10-section body (see section 2 below for the folder,
and the body order: Title → When to use → Data Protection → Knowledge base →
Workflow → Agentic Execution → Output format → Attribution → Reference material).
Six of those obligations are **contract blocks** — five inline, two folder/file:

| # | Block | Form | What the linter checks |
|---|-------|------|------------------------|
| 1 | Orchestration | inline marked | `hse:block:orchestration` present; invariant core matches `template/blocks/orchestration.md`; a non-empty "Subagent roster for THIS skill" subsection sits **below** the `:end` marker (presence-only, never diffed) |
| 2 | De-identification | inline marked | `hse:block:deid` present + exact canonical match — runs **before** any drafting |
| 3 | KB selection | inline marked | `hse:block:kb-selection` present + exact canonical match (table shape canonical; jurisdiction rows supplied per the knowledge base) |
| 4 | Branded report output | inline marked | `hse:block:report-output` present + exact canonical match |
| 5 | Eval scaffold | **folder** | `evals/` exists with `evals.json`, `rubric.yaml`, `run_evals.py`, `files/` |
| 6 | Company card | inline + **file** | `hse:block:attribution` present + canonical match **and** `branding/company-card.yaml` exists |

So: **five inline marked regions + two folder/file presence checks.**

### Marker convention

Inline blocks are delimited by HTML comments, which render invisibly and survive
chat-platform adapters:

```markdown
<!-- hse:block:deid:start -->
## Data Protection & De-identification (MANDATORY — apply before drafting)
…canonical invariant text…
<!-- hse:block:deid:end -->
```

The linter extracts the text between `:start`/`:end` and diffs it against
`template/blocks/<block>.md`. Block text must be **byte-identical** to the
template — do not edit it by hand; run `hse-skill-forge --sync` to refresh.
`MAX=6` is hard-coded in the canonical orchestration text (no variable
substitution). The structured-intake Q&A (see section 3) is a **Workflow
convention, not a seventh block** — the six-block contract is unchanged.

---

## 2. Per-skill folder layout

```
skills/<name>/
├── SKILL.md            # the 10 sections, in fixed order
├── references/         # METHODOLOGY.md, deid-checklist.md, QUALITY_CHECKLIST.md, _skill-kb.md
├── assets/             # output template(s) the Output block renders into
├── scripts/            # deterministic helpers, or a symlink to shared scripts/ (see section 5)
├── evals/              # evals.json, rubric.yaml, run_evals.py, files/   ← block 5
└── branding/           # company-card.yaml                              ← block 6
```

`name` must equal the folder name (lowercase + hyphens, ≤64 chars).

---

## 3. The structured-intake Workflow convention

Every skill's **Workflow** opens with a structured multi-step Q&A intake — MCQ
where the answer space is enumerable, free-text where open; **one question at a
time**; never proceed on vague or missing inputs. This is the operational core
of *forcing specificity*, and the evals **reward elicited specificity and
penalize unstated assumptions**. It is a Workflow convention, not a mandatory
block.

<!-- filled by A3 --> (points at the shared `KB-SNIP-INTAKE` snippet)

---

## 4. Knowledge-base reference syntax

How a skill cites the shared knowledge base and `_registry.yaml` IDs (every cited
`../../knowledge-base/…` path and registry ID must resolve, per linter rule 9).

<!-- filled by A3 -->

---

## 5. Shared-scripts reference mechanism

How a skill reuses `scripts/hse_components/` — the reference mechanism plus the
symlink / `sys.path` shim fallback for hosts that do not follow symlinks.

<!-- filled by A7 -->

---

## 6. Company-card symlink / override mechanism

How `branding/company-card.yaml` is symlinked to the repo default and overridden
per skill or per deployment.

<!-- filled by A9 -->

---

## 7. Local eval / lint commands + the quality gate

Run the same checks CI runs, locally, before opening a PR:

```bash
python scripts/lint_skills.py --all
python scripts/run_evals.py --changed
```

A PR merges only when the linter is green, ≥3 evals pass weighted ≥4.0 with no
hard-fail, the SME-persona pass ran, and a competent person approved.

### The ten linter rules (the machine contract)

`lint_skills.py` (CI) and `validate_repo_skill.py` (forge) are the same shared
module. Exit nonzero on any hard rule (1–6, 8, 9) → blocks merge; rules 7 and 10
are warnings.

1. **Block markers** — all five inline `hse:block:*` markers present; invariant
   cores match `template/blocks/*.md`. Mismatch → fail with a `run
   hse-skill-forge --sync` hint.
2. **Orchestration roster** — the subsection below `orchestration:end` is present
   and non-empty.
3. **Folder layout** — `references/`, `assets/`,
   `evals/{evals.json,rubric.yaml,run_evals.py,files/}`, and
   `branding/company-card.yaml` all present.
4. **`name`** — equals the folder name, lowercase + hyphens, ≤64 chars.
5. **`description`** — ≤1024 chars; third-person (no first-person pronouns).
6. **`metadata`** — all required keys present; values in the controlled
   vocabularies; `plugin` resolves to a registered bundle.
7. **Body length** — warn approaching ~400 lines, fail >500. *(warning)*
8. **Dead reference links** — every `references/…` path cited in the body
   resolves on disk.
9. **KB resolution** — every `../../knowledge-base/…` path and every
   `_registry.yaml` ID the skill names exists.
10. **No time-sensitive phrasing** — regex for absolute dates / "as of" /
    "currently" in the body → warn, with a pointer to push volatile facts into
    the KB. *(warning)*
