---
sme-review:
  personas:
    - role: "Procurement HSE Lead"
      expertise: "Contractor HSE prequalification and management to ISO 45001 clause 8.1.4 — risk-tiering a scope of work, evidence-based scoring (verified certificates/records, not claims), recognised accreditation schemes (SSIP, ISO 45001), UK CDM 2015 reg. 8 duty to appoint the competent, US OSHA multi-employer/controlling-employer duties, and approve/conditional/reject decisioning with conditions, owners, and review dates."
      lens: "Is the rigour proportionate to the work's risk (tier set by the highest-risk activity), is EVERY score tied to a VERIFIED evidence item rather than a self-asserted claim, is high-hazard work refused a pass on PPE/competence claims alone, and is the recommendation defensible with named conditions, owners, and a review date?"
---

# SME Review & Sign-off — contractor-prequalification

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a **Procurement HSE Lead**. The universal hard gates (de-id
leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and
are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Tier set by the highest-risk activity, not the average** — a package containing a
      single hot-work / confined-space / work-at-height / lifting / energised-electrical /
      demolition task that is scored as T1/T2 (so the deep PQQ and high bar are skipped) is a FLAG.
- [ ] **Every score is tied to a verified evidence item** — a criterion scored "met / pass" on
      a **self-asserted accreditation or competence with no supplied certificate/record** is a
      FLAG (it must be a `[GAP]`, never "met"). This is the core integrity gate.
- [ ] **High-hazard work is not passed on PPE/competence claims alone** — a T3 recommendation
      that clears the threshold without evidenced higher-order controls / activity-specific
      certification is a FLAG.
- [ ] **`[GAP]`s block an unconditional pass** — an `approve` recommendation issued over an open
      `[GAP]` (missing insurance, unverified accreditation, no high-hazard competence) is a FLAG;
      it should be `conditional` with a closing action or `reject`.
- [ ] **Conditions are real SMART actions** — each condition on a `conditional` decision has a
      named owner, an ISO due date, a measure, and ties to the gap it closes; "improve safety
      record" with no owner/date is a FLAG.
- [ ] **The contractor's accident/enforcement history is de-identified before scoring** — a
      named injured person (from a prosecution/RIDDOR/OSHA record) or an un-suppressed injury
      cell < 5 reaching the scorecard is a FLAG (and a de-id hard-fail).
- [ ] **The right statutory regime is cited** — construction work without CDM reg. 8, or a US
      controlling-employer scenario without the OSHA multi-employer policy, is a FLAG.

## Sign-off note
SME review: ran (persona: Procurement HSE Lead); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
