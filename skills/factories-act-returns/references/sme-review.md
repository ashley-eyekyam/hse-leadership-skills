---
sme-review:
  personas:
    - role: "Indian factory / occupational-safety compliance specialist (Factories Act 1948 + state Factories Rules)"
      expertise: "the state-Rule annual/half-yearly return + statutory registers; the occupier's statutory duty; the row-blind-citation trap"
      lens: "is this the correct STATE form for the occupier, with the citing rule + due date + portal, and is every unverified field honestly [GAP]?"
modes:
  return-assembly:
    detected_by: "Q1 = the statutory obligation (annual / half-yearly return / register) + Q0 = India → assemble the filled state Factories-Act return for the confirmed state"
    floor:
      - id: correct-state-form-or-gap
        description: "The correct STATE Factories-Rules form is resolved for the confirmed state (never a national form); an unseeded state → literal [GAP] + refusal to assemble a national form"
        anchors: ['gujarat factories rules', 'annual (statutory )?return']
        min_matches: 1
      - id: gj-gap-preserved-never-backfilled
        description: "An unverified/unseeded form id (the GJ row) is preserved as a literal [GAP] and never back-filled — a fabricated form number passes the row-blind grader but fails a regulator (the load-bearing FLAG)"
        anchors: ['\[gap', 'do not assume|not verified|not confirmed|not in doubt']
        min_matches: 2
      - id: obligation-cadence-and-period
        description: "The obligation cadence (annual vs half-yearly) and the exact return period/year are pinned before assembly"
        anchors: ['annual (statutory )?return', 'calendar year 2025|cy2025|cy 2025']
        min_matches: 2
      - id: row-sourced-rule-authority
        description: "The citing rule + filing authority/portal trace to the matched KB-REG-IN-STATEFORMS row (DISH for GJ), not model recall"
        anchors: ['kb-reg-in-stateforms', 'directorate of industrial safety|dish']
        min_matches: 1
      - id: absent-fields-are-literal-gap
        description: "Every return field absent from the source stays a literal [GAP]/to-be-entered placeholder — an invented count in a FILED return is the highest-consequence FLAG"
        anchors: ['\[enter', '\[gap']
        min_matches: 2
      - id: occupier-duty-small-cell-suppressed
        description: "The duty-holder is the OCCUPIER (not generically 'management'); accident cells below 5 are aggregated/suppressed before they enter the return"
        anchors: ['occupier', 'suppress|aggregat|below five|<\s*5|fewer than five']
        min_matches: 2
      - id: osh-code-note-legacy-primary
        description: "The legacy state return is the PRIMARY deliverable; an OSH-Code transition note is appended as direction-of-travel only, pointing to india-osh-code-pack"
        anchors: ['osh code', 'india-osh-code-pack', 'legacy']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The return with no filed, dated basis (S8)** — establishment particulars, the return period,
  the signatory/occupier declaration and the date must tie the return to a filed instrument; a
  return that reads well but carries no licence/registration particulars, no return period, and
  no dated declaration cannot be filed. Surface each as a field or a literal [GAP], never omit it.
- **The register that pairs with the return, unswept (S6)** — the Factories-Act return sits on a
  regime that also demands muster-roll, leave-with-wages, overtime and accident registers; naming
  the return while silently omitting the register set (or its prescribed form ids) strands the
  occupier's exposure. Cite the register set or [GAP] the prescribed form.
- **Accident-history silence (S3)** — the accident/dangerous-occurrence summary either carries the
  aggregated CY figures cross-referenced to the notices filed, or explicitly confirms nil; a return
  that omits the accident column entirely (rather than stating 0 or aggregating) is hollow.
- **The invented figure that a filed return makes dangerous** — the highest-consequence failure is
  a fabricated count/form-id in a document that will actually be filed. Absent data stays a literal
  [GAP]/placeholder routed to the occupier's registers, never a plausible-looking invented number.

## Sign-off note
SME review: ran (persona: Indian factory / occupational-safety compliance specialist
(Factories Act 1948 + state Factories Rules)); this is **decision-support only** and does not
replace competent-person sign-off before filing. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a competent
person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks
(de-id leak, invented citation, weighted score below threshold) are a separate enforcement class.
