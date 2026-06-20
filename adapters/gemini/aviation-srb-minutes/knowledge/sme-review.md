---
sme-review:
  personas:
    - role: "Safety Review Board secretary / chair (Accountable Manager as chair)"
      expertise: "Annex 19 Pillar 3 management review, SRB/SAG governance, defensible decision-log discipline (decision + rationale + accountable person), action tracking with owner + due date"
      lens: "do these minutes constitute a DEFENSIBLE record — every decision reasoned and owned, every action tracked — that survives an audit of the safety-management process?"
---

# SME Review & Sign-off — aviation-srb-minutes

This skill carries **one** SME lens, narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the "decisions have rationale" clause + reporter-identity protection)
to the Safety Review Board minutes; single-threaded by design. The universal hard gates
(de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced
class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every decision in the decision log carries a rationale AND an accountable person — a decision with no "why" or no owner is the failure mode; flag it.
- [ ] Every action has an owner AND a due date — an open action with no due date is unmanaged.
- [ ] The SPI/SPT review records each indicator against its alert/target level, the trend, and breach status — minutes that note SPIs were "discussed" without status are thin.
- [ ] Attendees appear as role labels and the chair is identified by role (typically the Accountable Manager); **no reporter named in a hazard item is identified** in the circulated minutes (the recurring confidentiality check; a leak is a de-id hard-fail).
- [ ] Quorum / meeting metadata present, and hazard/risk decisions cite the current 5×5 rating they acted on.
- [ ] Empty-row tables are clearly *templates to fill*, not asserted-as-held meetings — flag any output that presents an un-held meeting as minuted fact.

## Sign-off note
SME review: ran (persona: Safety Review Board secretary/chair — Annex 19 Pillar 3 management
review); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person (aviation-SME) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
