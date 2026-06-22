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

Run these locally **before opening a PR** — the model-graded evals are run here, on
your machine, not in CI (see below):

```bash
python3 scripts/lint_skills.py --all                     # the 10-rule contract linter
python3 scripts/run_evals.py --changed                   # evals for skills changed vs origin/main
python3 scripts/run_evals.py skills/hse-core/risk-assessment   # …or a specific skill
python3 scripts/run_evals.py --all                       # …or every skill in the repo
```

Each run prints a `passed/total` line per skill and the grader id; a non-zero exit
under `--ci` means a hard-fail or a below-gate score.

### How the eval grader runs — and why you run evals locally

`run_evals.py` grades each case in **two layers**:

- **Deterministic hard blocks** (de-identification leak · invented/unverifiable
  regulatory citation · missing report) — pure Python, **no model**. A hit is a
  **non-waivable auto-fail** and short-circuits the case before the model grader.
- **Model-graded dimensions** (specificity · hierarchy-of-controls · defensibility,
  scored 1–5 against `evals/rubric.yaml`) — these call a model through the **local
  Claude CLI (`claude -p`), which runs on your Claude subscription — no API key
  needed.**

Because the model grader needs the Claude CLI, it runs **only locally**:

| Context | Model-graded score | Deterministic hard blocks |
|---|---|---|
| **Your machine** — `claude` CLI on PATH, signed into your subscription | ✅ runs on your subscription | ✅ |
| **GitHub Actions CI** — headless, no CLI / no key | ⏭️ skipped | ✅ enforced |

So **CI does not re-check the weighted ≥4.0 score** — it enforces only the
deterministic gate plus lint/tests. **Confirming the ≥4.0 model-graded bar is your
job, locally, before you push:** run `run_evals.py`, read each skill's `passed/total`
line, and fix anything below gate before opening the PR.

**Prerequisites**
- Python 3 + `pyyaml` (`pip install pyyaml`).
- For the model-graded pass: the **Claude CLI signed into your subscription**
  (`claude` on PATH). No API key, no repo secret.

**Grader model** — pinned to `claude-sonnet-4-6` (Sonnet-class). Override per run for
a heavier judge:

```bash
python3 scripts/run_evals.py --all --grader-model claude-opus-4-8
# or: GRADER_MODEL=claude-opus-4-8 python3 scripts/run_evals.py --all
```

A PR merges only when the linter is green, ≥3 evals pass weighted ≥4.0 with no
hard-fail (**confirmed locally**), the SME-persona pass ran, and a competent person
approved.

### Golden eval-output authoring (`evals/output/*.md`)

A golden output is a **CANDIDATE** the owner LOCKs before the milestone-wide
LOCAL ≥4.0 sweep — it is the exemplar the model grader scores against. It must
read like a **real consultant deliverable**, not a rubric-compliance
demonstration. This matters because the deterministic CI de-id gate scans the
**intake fixtures**, never the golden prose: a personal name or a piece of
rule-narration sitting in a golden is **invisible to CI** and surfaces only in
the owner eye-review or the LOCAL model sweep. That is precisely why this
convention is enforced by authoring discipline, not by the linter.

Three rules govern every golden:

1. **Owners by role label, never a realistic personal name.** Show
   accountability as a role — "Site Manager (role)", "Appointed Person", "the
   Principal Designer" — not a person. A personal name in a de-identified
   deliverable reads as a leak, and defensibility's "named owner" requirement is
   fully satisfied by the role. 33 of the 34 v1.0/v1.1 goldens already do this.
2. **No process meta-narration in the golden prose.** Cut the lines that exist
   only to show the grader the skill obeyed its rules — "De-identification ran
   first…", "…the engine's output, never narrated", "No parameter was invented",
   "(by design — the core value)". A real deliverable never contains them. KEEP
   the honest `[ASSUMPTION]` / `[GAP]` flags — those belong in a genuine
   deliverable and are not meta-narration.
3. **Representative deliverable depth.** A real CPP, lift plan, RAMS, or ERP runs
   many pages; goldens should reflect that document density without padding into
   noise.

DO / DON'T — owner accountability cell:

```markdown
DON'T:  | Principal Contractor — A. Mercer | Reg 12/13 — plan, manage & monitor | … |
DO:     | Principal Contractor (role)      | Reg 12/13 — plan, manage & monitor | … |
```

The DON'T form is the lone outlier in the repo today — the CON-01
`construction-phase-plan` golden names three personal owners
(`A. Mercer` / `R. Okafor` / `P. Nair`). It is cited here **only** as the
cautionary teaching example; do not edit it under this guidance (its fix lands
in the Phase-17 backfill, below).

DO / DON'T — process meta-narration:

```markdown
DON'T:  > De-identification ran first; the matrix is the engine's output, never
        > narrated. No parameter was invented (by design — the core value).
DO:     [ASSUMPTION] Daytime works assumed; confirm if any night shift is planned.
        [GAP] Asbestos survey ref not supplied — flagged for the duty-holder.
```

Keep the de-identification and traceability discipline **silent in the
deliverable body**; surface only the honest `[ASSUMPTION]` / `[GAP]` flags a real
report would carry.

The existing 34 goldens are being backfilled to this convention in the Phase-17
pre-LOCK QA (Track B); this guidance therefore governs all **new** goldens from
Phase 15 onward.

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
