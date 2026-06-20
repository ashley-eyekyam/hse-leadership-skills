---
sme-review:
  personas:
    - role: "Multi-state India HSE-compliance research specialist (statutory form resolution)"
      expertise: "the (law, state, obligation) lookup across Factories Act + BOCW; legacy-first / no-national-form discipline (KB-02); the citing-rule + due-date + portal triad"
      lens: "given the law + the CONFIRMED state + the obligation, is the resolved legacy form the one the establishment actually files, with the right rule/due/portal, and is an unseeded state honestly [GAP]?"
---

# SME Review & Sign-off — india-state-form-finder

This is the **state-resolution engine itself** — its intake *is* the (law, state, obligation)
detection, so the India→state branch is the family's reference branch and the load-bearing
nuance here. `ELI-JURIS` is the spine: the state must be resolved and **confirmed** BEFORE any
form is cited, because a wrong state is a wrong statutory form. One lens suffices — this is a
deterministic resolution task owned by a single research specialist. The persona **narrows** the
`India-Regulatory` SME-persona archetype (`KB-SNIP-ARCHETYPES`) to the (law, state, obligation)
→ form resolution surface. The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

**Single-threaded skill.** This is the tier-1, single-threaded entry point ("Single-threaded by
design — no subagents"); the SME pass still runs **inline via the orchestration single-thread
fallback**, not as a spawned subagent — same persona, same checklist, same gate, performed
in-context before any output.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **State is a BLOCKING gate; anything outside the seeded set → `[GAP]` + refusal** — a form cited on an unconfirmed state, or an inferred-from-address state used without echo-back confirmation, is the load-bearing FLAG; an unseeded state (outside TN/KA/MH/DL/GJ) must yield a literal `[GAP]` and a refusal to emit a national form, never an invented row.
- [ ] **`(law, state, obligation)` triad fully resolved before any citation** — law (factories-act / bocw) AND obligation both pinned; a form returned on an under-specified key is FLAGged.
- [ ] **Resolved form = the legacy state form, traced to the row by fragment ID** — `form`/`rule`/`due`/`portal` come from the matched `KB-REG-IN-STATEFORMS` row, not recall. **[GAP — verify each claimed form id (TN 22 / KA 20 / MH 27 / DL 21 / GJ `[GAP]`, BOCW Form XXV) against the live state rule; do not assert.]**
- [ ] **The GJ `[GAP]` is surfaced explicitly, never substituted** — when the matched row's `form` is `[GAP]` (the GJ row), the output says so; a guessed GJ value is FLAGged (row-blind-grader trap).
- [ ] **Other-law obligations are deferred, not re-authored** — PESO→`hse-process`, MSIHC→`hse-chemicals`, Mines/DGMS→`hse-mining`; this skill resolves Factories-Act/BOCW only and points elsewhere rather than fabricating their forms.
- [ ] **Portal pointer is state-correct or honestly "verify locally"** — the `KB-REG-IN-PORTALS` pointer matches the resolved state/obligation, never a hard-coded national portal as the filing target.
- [ ] **OSH-Code note appended, legacy primary; scope held** — points to `india-osh-code-pack`; the skill *finds* the form, does not assemble (defers to `factories-act-returns`) or run an RCA.

## Sign-off note
SME review: ran (persona: multi-state India HSE-compliance research specialist (statutory form
resolution)); this is **decision-support only** and does not replace competent-person sign-off.
Single-threaded skill: the SME pass runs inline via the orchestration fallback, not as a spawned
subagent. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs "approved by a competent person". A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted
score below threshold) are a separate enforcement class.
