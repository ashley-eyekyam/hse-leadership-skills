---
sme-review:
  personas:
    - role: "Multi-state India HSE-compliance research specialist (statutory form resolution)"
      expertise: "the (law, state, obligation) lookup across Factories Act + BOCW; legacy-first / no-national-form discipline (KB-02); the citing-rule + due-date + portal triad"
      lens: "given the law + the CONFIRMED state + the obligation, is the resolved legacy form the one the establishment actually files, with the right rule/due/portal, and is an unseeded state honestly [GAP]?"
modes:
  resolution:
    detected_by: "Q1 = Identify the form (stay in the finder) + Q1a = India → the (law, state, obligation) → form resolution memo (this skill's single output; assembling/filing routes to a sibling skill)"
    floor:
      - id: state-confirmed-before-citing
        description: "The Indian state is resolved and CONFIRMED (infer-from-address echoed back) before any form is cited — an unconfirmed/inferred state is never used to cite a form (KB-REG-IN-STATEFORMS, topic state-detection)"
        anchors: ['(state|GJ).{0,25}confirm', 'client.confirmed', 'confirmed value']
        min_matches: 1
      - id: law-state-obligation-triad
        description: "The full (law, state, obligation) triad is pinned before resolution — a form returned on an under-specified key is a FLAG"
        anchors: ['law:.{0,25}(state|GJ)', 'lookup key', 'obligation']
        min_matches: 1
      - id: form-traced-to-kb-row
        description: "The resolved form/rule/due/portal trace to the matched KB-REG-IN-STATEFORMS row by fragment id, not model recall"
        anchors: ['KB-REG-IN-STATEFORMS', 'source fragment']
        min_matches: 1
      - id: gj-gap-surfaced-never-fabricated
        description: "An unseeded/unverified form value (the GJ row) is surfaced as a literal [GAP] and never back-filled — an invented state/national form number is the load-bearing FLAG (row-blind-grader trap)"
        anchors: ['\[GAP\]', 'not (confirmed|verified)', 'never.{0,20}(invent|assum|fabricat)|do not (assume|invent)']
        min_matches: 2
      - id: portal-state-correct
        description: "The filing-portal pointer is state-correct or honestly 'verify locally' — never a hard-coded national portal presented as the filing target"
        anchors: ['DISH|Directorate of Industrial Safety', 'verify.{0,20}local|confirm.{0,20}local']
        min_matches: 1
      - id: osh-code-note-legacy-primary
        description: "An OSH-Code transition note is appended with the LEGACY state form as the primary answer, pointing to india-osh-code-pack for the mapping"
        anchors: ['OSH Code', 'india-osh-code-pack', 'legacy.{0,30}(primary|remains)']
        min_matches: 2
      - id: competent-person-decision-support
        description: "The memo is framed decision-support only and routes the unresolved value to a competent person for verification"
        anchors: ['competent person', 'decision-support']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The form asserted without its dated, sourced basis (S8)** — a resolved form id with no
  citing rule, no fragment id, and no "as at <date>" currency stamp cannot be tied to a filed
  basis; a reader cannot tell whether the value is current or a recalled guess. Every resolved
  value carries its row/rule and a dated currency caveat, or it is `[GAP]`.
- **The regime named, its element set unswept (S6)** — naming "Factories Act / BOCW" or "the
  OSH Code" while omitting what that regime actually demands for the obligation (the citing
  rule, the due-date basis, the portal, the register that pairs with the return). Cite the hook
  AND resolve its element set, or `[GAP]` the missing element.
- **The inferred-from-address state used without echo-back** — a state silently inferred from a
  supplied address and used to cite a form, with no confirm-back to the user. A wrong state is a
  wrong statutory form; the inference must be echoed and confirmed, never assumed.
- **Sibling-obligation scope creep** — resolving (or worse, assembling) a Mines/DGMS, PESO or
  MSIHC obligation this finder does not own instead of routing it onward; the finder locates the
  Factories-Act/BOCW form and hands off, never fabricates a sibling regime's form.

## Sign-off note
SME review: ran (persona: multi-state India HSE-compliance research specialist (statutory form
resolution)); this is **decision-support only** and does not replace competent-person sign-off.
Single-threaded skill: the SME pass runs inline via the orchestration fallback, not as a spawned
subagent. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs "approved by a competent person". A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted
score below threshold) are a separate enforcement class.
