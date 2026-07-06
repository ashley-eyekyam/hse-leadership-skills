---
sme-review:
  personas:
    - role: "Indian OSH-Code-2020 transition advisor / labour-law consolidation specialist"
      expertise: "the four labour codes' consolidation (single registration, single consolidated annual return, raised factory thresholds 10/20->20/40, shifted Safety-Officer trigger 1000->500/250); the savings clause; per-state Rule-notification status"
      lens: "is the legacy state form still the PRIMARY answer, and is every consolidated equivalent correctly caveated as not-yet-live unless the state has notified its OSH Rules?"
modes:
  transition-briefing:
    detected_by: "Q1 = India + Q3 = the legacy obligation being mapped → the OSH-Code transition briefing (legacy-primary, consolidated as forward-look) for the confirmed state"
    floor:
      - id: legacy-form-primary
        description: "The legacy state form is the PRIMARY, defensible answer (here DL Form 21); an output that leads with or substitutes the OSH-Code form is a FLAG"
        anchors: ['form 21', 'legacy']
        min_matches: 2
      - id: state-resolved-before-commencement
        description: "The state is resolved and confirmed before any commencement claim — commencement is state-specific; asserting a consolidated form is live for an unconfirmed state is a FLAG"
        anchors: ['delhi|\bdl\b', 'notif']
        min_matches: 2
      - id: never-file-unnotified-form
        description: "The load-bearing safety check: never instruct filing an OSH form the state has not notified — an unnotified consolidated form is [GAP], never presented as filable"
        anchors: ['not notified|has not notified|unnotified', 'do not file|no legal effect']
        min_matches: 2
      - id: consolidated-form-gap-never-invented
        description: "The un-notified consolidated form is rendered a literal [GAP], never a fabricated OSH-Code form number (row-blind grader trap)"
        anchors: ['\[gap', 'not notif|no consolidated|not been prescribed']
        min_matches: 2
      - id: per-state-notification-sourced
        description: "Per-state OSH-Rule notification status (GJ/AR notified; DL not) is read from KB-REG-IN-OSH-CODE, not model recall"
        anchors: ['notified', 'gujarat|arunachal']
        min_matches: 2
      - id: threshold-shifts-sourced
        description: "The threshold shifts (factory 10/20 → 20/40; Safety-Officer 1,000 → 500/250) are stated correctly and sourced, not recalled"
        anchors: ['20 workers|10.{0,6}20|20.{0,6}40', '500|250|1,000']
        min_matches: 2
      - id: savings-clause-legacy-valid
        description: "The savings clause is stated so the reader is not told their legacy filing is void — legacy filings remain in force until commencement"
        anchors: ['savings clause|section 143', 'full force|remain|no gap']
        min_matches: 1
      - id: staleness-caveat
        description: "Given status:beta + the 90-day window, an explicit verify-currency / review-horizon caveat is carried rather than presenting the map as settled"
        anchors: ['90.day|staleness|review horizon', 'verify']
        min_matches: 2
---

# SME Review & Sign-off — india-osh-code-pack

This is an **always-India**, **`status: beta`** skill — the most volatile in the family; the KB
fragment carries a 90-day staleness window. `ELI-JURIS` is the spine: the state must be resolved
and confirmed BEFORE any commencement claim, because OSH-Rule notification status is
state-specific (only a couple of states have notified). One lens suffices — the primary advisor
owns both the transition mapping and the commencement-status caveat; this is one coherent
specialism. The persona **narrows** the `India-Regulatory` SME-persona archetype
(`KB-SNIP-ARCHETYPES`) to the OSH Code 2020 legacy→consolidated transition surface. The universal
hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Legacy state form stays the PRIMARY, defensible answer** — the consolidated mapping is opt-in and additive; an output that *leads* with (or substitutes) the OSH-Code form over the legacy state form is FLAGged.
- [ ] **State resolved before any commencement claim** — commencement is state-specific; asserting a consolidated form is live for an unconfirmed/unseeded state is FLAGged — give direction-of-travel only. The state is the mandatory, blocking, infer-then-confirm gate (`KB-REG-IN-STATEFORMS`, topic `state-detection`); an unseeded/unknown state → direction-of-travel only, never a fabricated state-specific consolidated form.
- [ ] **Never instruct filing an OSH form the state has not notified** — the load-bearing safety check: any consolidated form for a non-notifying state is rendered `[GAP]`, never presented as filable. An instruction to file an unnotified form is the highest-consequence FLAG.
- [ ] **Per-state notification status read from the KB, not the skill body / model recall** — the volatile commencement fact lives only in `KB-REG-IN-OSH-CODE` (90-day staleness); a hard-coded or recalled "X state has notified" claim is FLAGged. **[GAP — verify the current per-state OSH-Rule notification list against `KB-REG-IN-OSH-CODE`'s `last_reviewed`; the "only GJ + AR notified" snapshot must be re-checked against the live fragment, not asserted.]**
- [ ] **Threshold shifts stated correctly + sourced** — the raised factory threshold (10/20→20/40) and shifted Safety-Officer trigger (1000→500/250) trace to `KB-REG-IN-OSH-CODE`, not recall; a wrong number is FLAGged. **[GAP — verify the exact threshold numbers against the live fragment.]**
- [ ] **Savings clause stated — legacy filings remain valid** — the transition note carries the savings clause so the reader is not told their legacy filing is void.
- [ ] **Staleness honesty** — given `status: beta` + the 90-day window, the artifact carries an explicit "verify currency with a competent person / the live notification" caveat rather than presenting the transition map as settled.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The four-code frame named, the element set unswept (S6)** — naming "the OSH Code / four
  labour codes" while omitting the concrete shifts it drives for this establishment: single
  registration, the consolidated return, the raised factory threshold, and the tightened
  Safety-Officer trigger. Map each legacy obligation to its consolidated equivalent, or [GAP].
- **The high-consequence instruction with no bridge (S2)** — telling a reader to "move to the
  consolidated regime" without the interim rule (file the legacy form now; the consolidated form
  is [GAP] until the state notifies) leaves a compliance gap during the transition. Always state
  what to file TODAY and the trigger that changes it.
- **The transition asserted as settled (S5)** — commencement dates, notification lists and
  thresholds are volatile facts that must carry their source and an "as at <date>" / review-window
  stamp, or a numeric value is a recalled guess. Source each figure or [GAP] it.
- **Legacy-void misread** — the reader must never infer their current legacy filing is void; the
  savings clause and legacy-primary framing are load-bearing, not decorative.

## Sign-off note
SME review: ran (persona: Indian OSH-Code-2020 transition advisor / labour-law consolidation
specialist); this is **decision-support only** and does not replace competent-person sign-off —
status beta, the law is actively transitioning and currency must be re-verified. It **precedes —
and never replaces, never emits — the human competent-person sign-off**, and it never outputs
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
