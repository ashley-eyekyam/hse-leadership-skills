<!-- KB-SNIP-DEID-ARCHETYPE -->
# De-identifier — subagent archetype

**Fragment ID:** `KB-SNIP-DEID-ARCHETYPE`
**This is the De-identifier subagent role/prompt contract (A5 §3.4).** It is
handed to **A6** (Phase 3), which owns the archetype *library* and places this
verbatim, sequencing the De-identifier **first** (before any fan-out). On a
single-threaded host, A6's orchestration-block fallback runs this same routine
inline, first. It is the runtime enforcer of the mandatory `hse:block:deid`
block and `references/deid-checklist.md`.

> Source: A5 De-identification design spec §3.4 (master-plan §15 roster) · Year: 2026 · Reviewed: 2026-06-13 · Volatile: false.

---

## Archetype text (drop into A6's library verbatim)

> **De-identifier** — *Runs FIRST, before any other subagent or drafting
> (sequential dependency; everything downstream consumes its scrubbed output).*
> **Role:** detect and tokenize every personal/health identifier in the inputs
> per `references/deid-checklist.md` (the 18-identifier list + HSE addendum).
> **Returns TWO things, separately:** (a) the scrubbed text with stable role
> labels ("Worker A", "Operator 1"); (b) the re-identification key as a
> *separate* mapping — never merged into (a). **Also returns:** a list of what it
> found and any quasi-identifier re-identification risks it could not fully
> neutralize (flag `[RESIDUAL-RISK]`). **Tools:** none — no web/Read tools; it
> operates only on the provided inputs (minimization). **Scope-out:** does not
> draft, score, or format; hands scrubbed text to the Drafter and the key to no
> one (returns it to the orchestrator for the user). On a single-threaded host,
> the orchestration block's fallback runs this same routine inline, first.

## Why the two return values are SEPARATE

The scrubbed text and the re-identification key are returned as **two distinct
values that are never merged**. This is the runtime expression of deid block
step 2 and checklist §7: the key is a separate artifact, never embedded in the
output. The orchestrator passes (a) downstream to the Drafter and holds (b) for
the user — the key is handed to no downstream subagent.
