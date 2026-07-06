---
sme-review:
  personas:
    - role: "Safety Review Board secretary / chair (Accountable Manager as chair)"
      expertise: "Annex 19 Pillar 3 management review, SRB/SAG governance, defensible decision-log discipline (decision + rationale + accountable person), action tracking with owner + due date"
      lens: "do these minutes constitute a DEFENSIBLE record — every decision reasoned and owned, every action tracked — that survives an audit of the safety-management process?"
modes:
  srb-minutes:
    detected_by: "Q1 — What do you want produced? == Minute a held meeting (the produced Safety Review Board minutes; ICAO Annex 19 Pillar 3 management review)"
    floor:
      - id: srb-decision-rationale-owned
        description: "Every decision in the decision log carries a rationale AND an accountable person — a decision with no 'why' or no owner is the failure mode"
        anchors: ['decision', 'rationale', 'accountable']
        min_matches: 2
      - id: srb-action-owner-due
        description: "Every action has an owner AND a due date — an open action with no due date is unmanaged"
        anchors: ['owner', 'due date', 'action']
        min_matches: 2
      - id: srb-spi-status-vs-threshold
        description: "The SPI/SPT review records each indicator against its alert/target level, the trend, and breach status — minutes that note SPIs were merely 'discussed' are thin"
        anchors: ['\bSPI', 'alert', 'target', 'breach', 'trend']
        min_matches: 2
      - id: srb-attendees-role-labels
        description: "Attendees appear as role labels and the chair is identified by role (typically the Accountable Manager); no reporter named in a hazard item is identified in the circulated minutes"
        anchors: ['role', 'chair', 'Accountable Manager']
        min_matches: 1
      - id: srb-meeting-metadata-quorum
        description: "Meeting metadata (date, body, quorum) is present and hazard/risk decisions cite the current 5×5 rating they acted on — record identity for a defensible minute"
        anchors: ['quorum', 'meeting', '\b5.?5\b', 'attendance']
        min_matches: 1
      - id: srb-prior-actions-carried
        description: "Prior-meeting actions are carried forward with status — continuity of the action log, not a fresh list each meeting"
        anchors: ['prior action', 'carried forward', 'action log', 'previous meeting']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **Record identity & basis** — the minutes are not tied to a dated meeting, a prior-minutes
  reference, or a stated review period, so they cannot be filed as the continuous
  management-review trail an SMS audit follows.
- **The breach minuted with no bridge** — a breached SPI or an elevated hazard is recorded as
  discussed and an action is logged with a far due date, but no interim measure or escalation
  is minuted for the period until the action closes.
- **Decisions without the evidence acted on** — a hazard decision is minuted without the 5×5
  rating, SPI status, or occurrence data it was taken against, so the record shows a verdict
  but not the basis a later auditor can test.

## Sign-off note
SME review: ran (persona: Safety Review Board secretary/chair — Annex 19 Pillar 3 management
review); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person (aviation-SME) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
