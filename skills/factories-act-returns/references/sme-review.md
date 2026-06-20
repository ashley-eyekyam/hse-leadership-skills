---
sme-review:
  personas:
    - role: "Indian factory / occupational-safety compliance specialist (Factories Act 1948 + state Factories Rules)"
      expertise: "the state-Rule annual/half-yearly return + statutory registers; the occupier's statutory duty; the row-blind-citation trap"
      lens: "is this the correct STATE form for the occupier, with the citing rule + due date + portal, and is every unverified field honestly [GAP]?"
---

# SME Review & Sign-off — factories-act-returns

This is an **always-India** skill and the **highest-stakes filer in the family** — it
*assembles a return for filing*, so the SME lens is correspondingly sharp. `ELI-JURIS` is the
spine: the state must be resolved and confirmed BEFORE any state form is cited, because a wrong
state is a wrong statutory form. One lens suffices — the legal interpretation here is
form-selection-by-state, which the primary owns. The persona **narrows** the `India-Regulatory`
SME-persona archetype (`KB-SNIP-ARCHETYPES`) to the Factories Act 1948 + state Factories Rules
return-assembly surface. The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-
only, owned-and-dated actions) are the enforced class and are not restated below.

**Row-blind-grader catch (load-bearing).** The citation grader checks only that the fragment ID
resolves, not that a form *value* is real — so a plausible-but-wrong form number passes the
automated gate but fails a regulator. This SME pass is the catch: every claimed state form id is
carried forward `[GAP]` to verify against `KB-REG-IN-STATEFORMS` and the live state rule, never
asserted as ground truth.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Correct STATE form for the detected state — never a national form** — the form id resolves from the matched `KB-REG-IN-STATEFORMS` row; an unseeded state yields `[GAP]` + a refusal to assemble a national form. A national number, or a form for the *wrong* state, is the load-bearing FLAG. **[GAP — verify each claimed state form id (TN 22 / KA 20 / MH 27 / DL 21) against the live state Factories Rules; do not assert. NOTE: the KB seeds NO MH annual-return row — the claimed "MH Form 27" annual return must stay a literal `[GAP]`, never emitted as a real value, until the owner verifies and seeds the row.]**
- [ ] **The GJ row's `[GAP]` form id is preserved, never back-filled** — because the citation grader is row-blind, a fabricated GJ form number passes the automated gate but fails a regulator; FLAG any guessed GJ value. The family's clearest "automated gate can't catch this" check.
- [ ] **Obligation matched to the right cadence** — annual vs half-yearly vs register resolved before assembly; a half-yearly assembled under the annual rule (or vice-versa) is FLAGged.
- [ ] **Citing rule + due date + portal are the resolved row's, not recalled** — every form/rule/due/portal traces to the matched row by fragment ID; a plausible-but-uncited rule/due is FLAGged.
- [ ] **Every absent return field is a literal `[GAP]`, not fabricated** — employment/accident/leave figures absent from the source stay `[GAP]`; an invented count in a *filed* return is the highest-consequence FLAG.
- [ ] **Occupier duty + small-cell suppression** — the return's duty-holder is the **occupier** (not generically "management"); accident cells <5 are aggregated before they enter the return.
- [ ] **OSH-Code transition appended, legacy stays primary** — the legacy state return is the primary deliverable; the OSH-Code note is direction-of-travel only.

## Sign-off note
SME review: ran (persona: Indian factory / occupational-safety compliance specialist
(Factories Act 1948 + state Factories Rules)); this is **decision-support only** and does not
replace competent-person sign-off before filing. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a competent
person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks
(de-id leak, invented citation, weighted score below threshold) are a separate enforcement class.
