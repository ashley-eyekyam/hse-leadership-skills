---
sme-review:
  personas:
    - role: "Procurement HSE Lead"
      expertise: "Contractor HSE prequalification and management to ISO 45001 clause 8.1.4 — risk-tiering a scope of work, evidence-based scoring (verified certificates/records, not claims), recognised accreditation schemes (SSIP, ISO 45001), UK CDM 2015 reg. 8 duty to appoint the competent, US OSHA multi-employer/controlling-employer duties, and approve/conditional/reject decisioning with conditions, owners, and review dates."
      lens: "Is the rigour proportionate to the work's risk (tier set by the highest-risk activity), is EVERY score tied to a VERIFIED evidence item rather than a self-asserted claim, is high-hazard work refused a pass on PPE/competence claims alone, and is the recommendation defensible with named conditions, owners, and a review date?"
modes:
  scoring:
    detected_by: "Q5 — Decision type + output (New approval / Re-approval / Project-specific → the evidence-based scorecard + approve/conditional/reject recommendation leg of the produced pack)"
    floor:
      - id: tier-highest-risk
        description: "The risk tier is set by the highest-risk activity in the scope, not the average (KB-DATA-CONTRACTOR-TIERS tiering rule)"
        anchors: ['highest.risk activity', 'risk tier']
        min_matches: 1
      - id: verified-evidence-register
        description: "An evidence register with per-criterion verification status — every score tied to a verified evidence item; a self-asserted claim is never scored as met"
        anchors: ['verified evidence', 'verification status', 'self.asserted']
        min_matches: 1
      - id: deid-before-scoring
        description: "The contractor's accident/enforcement records are de-identified before scoring — role labels only, no named injured person, small cells suppressed"
        anchors: ['de.identif', 'de.id pass', 'role label']
        min_matches: 1
      - id: accident-enforcement-history
        description: "Accident and enforcement history (rates, notices, prosecutions) over the last 3-5 years scored on verifiable records"
        anchors: ['accident.{0,8}enforcement', 'enforcement history', 'accident history']
        min_matches: 1
      - id: no-pass-on-claims-alone
        description: "High-hazard (T3) work is never passed on PPE/competence claims alone — higher-order controls must be evidenced (KB-DATA-CONTRACTOR-TIERS T3 threshold)"
        anchors: ['claims? alone', 'PPE/competence']
        min_matches: 1
      - id: gaps-block-unconditional
        description: "Open gap items block an unconditional approval — a recommendation issued over an open gap is conditional or reject, never approve"
        anchors: ['unconditional (pass|approval)', 'blocks? an unconditional']
        min_matches: 1
      - id: conditions-smart-owned
        description: "Every condition on a conditional decision is a SMART action — named owner, due date, measure, tied to the gap it closes"
        anchors: ['SMART', 'named owner', 'owner.{0,30}due date']
        min_matches: 1
      - id: review-date
        description: "A review date / review cadence is set for the approval decision (intake Q5c)"
        anchors: ['review date', 'review cadence']
        min_matches: 1
  questionnaire:
    detected_by: "Q5 — Decision type + output (the blank risk-tiered PQQ issued to the contractor — the questionnaire leg of the produced pack; the mode of the empirical Nagapattinam failure)"
    floor:
      - id: core-evidence-insurance
        description: "Employers'/public-liability (and Workmen's Compensation / CAR where the jurisdiction demands it) insurance demanded as a current certificate, never a claim (KB-SNIP-PQQ-BANK core row)"
        anchors: ['public.{0,3}liability', 'employers.{0,12}liability', 'workmen.{0,4}s compensation', 'insurance certificate']
        min_matches: 1
      - id: accident-enforcement-history
        description: "Accident and enforcement history (fatalities, reportable injuries, notices, prosecutions) demanded over the last 3-5 years with verifiable records (KB-SNIP-PQQ-BANK core row)"
        anchors: ['accident.{0,8}enforcement', 'enforcement history', 'accident history']
        min_matches: 1
      - id: high-hazard-module
        description: "The T3 high-hazard module is demanded for every high-hazard activity in scope, with activity-specific competence/certification evidence (KB-DATA-CONTRACTOR-TIERS T3 row)"
        anchors: ['high.hazard module', 'activity.specific (competence|certification)', 'high.hazard \(T3\)']
        min_matches: 1
      - id: scoring-scheme
        description: "A numerical scoring scheme is stated: per-question pass rule, weighted matrix or scorecard, and the minimum outcome threshold for approve/conditional/reject (intake Q5b)"
        anchors: ['scorecard', 'scoring (rubric|matrix|scheme)', 'weighted scor', 'pass/fail threshold']
        min_matches: 1
      - id: approval-authority
        description: "A named approval authority / decision owner and sign-off hierarchy for the final approve/conditional/reject decision (intake Q5c)"
        anchors: ['decision owner', 'approval authority', 'approving authority', '\|\s*owner\s*\|']
        min_matches: 1
      - id: statutory-regime-check
        description: "The jurisdiction's statutory regime is checked, not just generic HSE — UK CDM reg. 8 duty-holders; US OSHA multi-employer; India Contract Labour licence, ESIC/EPF and BOCW cess, Factories Act applicability (intake Q4 jurisdiction trigger)"
        anchors: ['CDM.{0,8}reg', 'OSHA multi.employer', 'Factories Act', 'Contract Labour', 'ESIC']
        min_matches: 1
      - id: conditions-smart-owned
        description: "Conditional approvals carry SMART conditions — each with a named owner, due date and measure tied to the gap it closes (KB-SNIP-PQQ-BANK output expectation)"
        anchors: ['SMART', 'named owner', 'owner.{0,30}due date']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A polished PQQ with no decision machinery** — professional-looking, evidence-anchored
  questions, but no numerical scoring scheme, no per-question pass rule, and no named
  approval authority or co-sign path for the final decision. Two evaluators could reach
  opposite decisions from the same pack. Check the decision machinery before the questions.
- **The jurisdiction's statutory layer beyond generic HSE** — India: Contract Labour (R&A)
  licence (both contractor licence and principal-employer registration), ESIC/EPF
  registration currency, BOCW cess payment evidence (not registration alone), Factories Act
  applicability and the state's factories rules; UK: CDM duty-holder checks; US: OSHA
  multi-employer/controlling-employer. A PQQ that asks only generic HSE questions silently
  strands the principal employer's statutory exposure.
- **Lifecycle edges** — submission/resubmission timeline, in-contract performance
  monitoring (KPIs, inspection frequency, suspension triggers), sub-contractor control and
  client-approval gates, document version control, and interface with the client site's
  emergency arrangements (SIMOPS with other trades, ERP integration, first-aid provision).
- **People controls beyond certificates** — minimum supervision ratio for the crew, health
  surveillance / medical fitness for confined-space and spray work, and the competence of
  the person who performs RPE face-fit testing.

## Sign-off note
SME review: ran (persona: Procurement HSE Lead); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
