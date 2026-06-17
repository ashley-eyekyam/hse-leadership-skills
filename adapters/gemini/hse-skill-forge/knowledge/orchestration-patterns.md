# Roster-authoring menu (what the forge seeds below `orchestration:end`)

> The orchestration BLOCK is invariant (copied byte-for-byte from
> `template/blocks/orchestration.md`). The **roster subsection** that follows it —
> "Subagent roster for THIS skill", below the `:end` marker — is per-skill and
> presence-only (rule 2, never byte-diffed). This file is the menu the forge picks
> from when `answers.json` declares a `roster`.
>
> Archetype prompts the roster draws from live in
> `../../../knowledge-base/prompt-snippets/subagent-archetypes.md` (`KB-SNIP-ARCHETYPES`)
> — the seven core archetypes (Researcher, Regulatory-Checker, Risk-Scorer,
> Drafter, De-identifier, Critic/QA, SME-reviewer). The forge does not re-state
> them here; it points at the canonical menu.

## Two invariants every roster honours

- **The De-identifier runs FIRST** — a sequential gate; everything downstream
  consumes only its scrubbed output (A5 / the deid block).
- **The Critic/QA pass is MANDATORY** — all output in this pack is regulatory/safety
  output; the roster always ends with an adversarial read-only review.

## The triage-count mapping (orchestration Step 0/1)

| Complexity | Fan-out | Roster shape |
|---|---|---|
| simple / single-subject / ~2-min artifact | 0 — do it yourself | `single-thread` one-liner |
| moderate | 2–3 | `moderate` (Researcher + Drafter + Critic/QA) |
| complex | 4–6 (never exceed MAX=6) | `flagship-b5` (the four-agent investigation roster) |

## The three seeded rosters (the `roster` flag)

- **`single-thread`** — "Single-threaded by design — no subagents." The De-identifier
  scrub and the Critic/QA pass still run inline via the block's fallback. (B3
  toolbox-talk; the forge itself.)
- **`moderate`** — Researcher (gathers the scrubbed task/jurisdiction facts) →
  Drafter (assembles the deliverable, hierarchy-of-controls applied) → Critic/QA.
  No "Risk-Scorer" subagent when scoring is deterministic via A7. (B1 risk-assessment.)
- **`flagship-b5`** — the examined four-agent fan-out: De-identifier (first) →
  Evidence & Timeline Reconstructor + Root-Cause Analyst + Regulatory Reportability
  Checker + Corrective-Action Drafter → MANDATORY Critic/QA. Pre-seeded verbatim so
  B5 incident-investigation scaffolds with its gate-approved roster (SC-1 ↔ SC-5).

## Build-time vs runtime fan-out (never conflate)

The rosters above describe **runtime** fan-out (a user running one finished skill).
The forge's own §3.7 **build-time** fan-out — one subagent authoring each skill in
parallel during a build campaign — is a different mechanism entirely (master-plan
§2.4). The forge seeds runtime rosters into other skills; it is not itself a runtime
fan-out.
