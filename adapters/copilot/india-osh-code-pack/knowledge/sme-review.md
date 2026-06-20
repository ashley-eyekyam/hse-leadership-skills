---
sme-review:
  personas:
    - role: "Indian OSH-Code-2020 transition advisor / labour-law consolidation specialist"
      expertise: "the four labour codes' consolidation (single registration, single consolidated annual return, raised factory thresholds 10/20->20/40, shifted Safety-Officer trigger 1000->500/250); the savings clause; per-state Rule-notification status"
      lens: "is the legacy state form still the PRIMARY answer, and is every consolidated equivalent correctly caveated as not-yet-live unless the state has notified its OSH Rules?"
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

## Sign-off note
SME review: ran (persona: Indian OSH-Code-2020 transition advisor / labour-law consolidation
specialist); this is **decision-support only** and does not replace competent-person sign-off —
status beta, the law is actively transitioning and currency must be re-verified. It **precedes —
and never replaces, never emits — the human competent-person sign-off**, and it never outputs
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
