<!-- KB-SNIP-INTAKE -->
# Structured Intake Interview — canonical elicitation pattern

**Fragment ID:** `KB-SNIP-INTAKE`
**This is prompt text — the shared pattern every skill's Workflow opens with**
(master-plan §2.7). It operationalises the core value on the **input** side: a skill
cannot force task/site/asset-specific output unless it first elicits task/site/asset-
specific facts. It carries the *pattern*; each skill authors its own concrete
question set (MCQ option lists + free-text prompts) for its domain.

> Source: master-plan §2.7 structured-intake convention · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false.

---

## Instruction (run this FIRST, before any drafting or fan-out)

Conduct a **multi-step interview, one question at a time.** Never present a wall of
questions; never silently assume a missing fact.

### Question form

- **Prefer MCQ** where the answer space is enumerable — jurisdiction, industry,
  hazard category, likelihood/severity band, RCA method, audience, yes/no gates.
  MCQ is fast, unambiguous, and teaches the user the option space.
- **Use free-text** where the answer is open — the task and its steps, the
  environment, observations, evidence, prior incidents, the desired outcome.

### Branch on answers

- e.g. jurisdiction = **India** → ask the **state**, then resolve via
  `KB-REG-IN-STATEFORMS` (mandatory state detection).
- e.g. RCA method = ICAM → ask for the organisational-factor evidence.
- Stop asking once enough specificity is gathered to produce a **defensible** output.

### Echo before analysis

Before any analysis, **echo the captured facts back** to the user for confirmation.
Proceed only on confirmed facts.

### Never proceed on vague or missing inputs

If a needed fact is absent, **ask**. If the user genuinely cannot answer, record it
as an explicit **`[ASSUMPTION]`** or **`[GAP]`** rather than inventing it. Never
fabricate task/site/asset detail to fill a hole.

### Platform-neutral degradation (§2.5)

This snippet is prose describing the interview. On a rich host it may use that host's
question UI; everywhere else it **degrades to plain conversational Q&A** — one
question, wait, branch, repeat. Same portability discipline as the orchestration block.

## Sequence

Intake gathers raw facts → the `deid` block (A5) scrubs them before drafting → the
orchestration block (A6) fans out on the de-identified, intake-gathered inputs.
`KB-SNIP-INTAKE` is the **first** thing the Workflow runs, upstream of both.
