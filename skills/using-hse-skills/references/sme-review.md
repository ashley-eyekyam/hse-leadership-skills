---
sme-review:
  personas:
    - role: "HSE practice lead / catalog steward"
      expertise: "The full HSE skill catalog and its bundles, the elicitation taxonomy and the shared-fact carry-over contract, the hierarchy-of-controls dependency between artifacts (RA → JSA → permit → toolbox talk), de-identification of handoff context, and where a request belongs (which single skill vs. an ordered chain)."
      lens: "Does this routing send the user to the RIGHT skill(s) in the RIGHT order for the stated intent — a complete, correctly-sequenced chain, no clear single-skill request hijacked into a full elicitation, and a run sheet whose context is de-identified and whose every dependent step attaches the prior skill's output?"
---

# SME Review & Sign-off — using-hse-skills (catalog router)

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into an HSE practice lead / catalog steward. The router produces
no traditional HSE artifact — it routes — so the reviewer checks the *routing quality* (the
right chain, no hijack, a clean handoff) rather than the controls of a single deliverable.
The universal hard gates (de-id leak, citation accuracy, owned-and-dated handoff) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The recommended chain is **complete and correctly ordered** — the right skills for the stated intent, in a defensible dependency sequence (e.g. risk-assessment before job-safety-analysis before permit-to-work before toolbox-talk); a missing prerequisite step, or a step out of dependency order, is a FLAG.
- [ ] **No clear single-skill request was hijacked** — an unambiguous single-artifact request ("write a toolbox talk for tonight's shift") is pointed straight at that skill, not dragged through a full router elicitation; over-triggering on a request that names its own artifact is a FLAG (D-06).
- [ ] The run sheet's **de-identification and prior-output handover are present** — the shared context is pseudonymized to role labels (`[SITE-1]`, `[ROLE: site manager]`, `[CONTRACTOR]`) BEFORE it is written into any step, and every step 2+ `CARRY-IN` explicitly instructs the user to ATTACH the prior skill's OUTPUT (not just the original elicited context); a verbatim identifier in a step block, or a dependent step that omits the attach-prior-output instruction, is a FLAG (D-03/D-04).
- [ ] Each recommended skill carries a **one-line WHY** tying it to the elicited intent / success-criteria — a recommendation with no rationale, or a rationale that does not match the captured facts, is a FLAG (ROUTE-03).
- [ ] The **mandatory India→state** branch was honoured — an India request routed to a form-bearing skill without the state confirmed first is a FLAG.

## Sign-off note
SME review: ran (persona: HSE practice lead / catalog steward); this is **decision-support
only**. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs the affirmative claim "approved by a competent person".
A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id
leak, invented citation, weighted score below threshold) are a separate enforcement class.
