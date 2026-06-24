# Pre-output Quality Checklist — iso45001-gap-analysis

Validate the draft gap analysis against this gate **before** producing any output. A failure
here is fixed, not shipped. The universal hard blocks (de-id leak, invented/mis-cited clause,
weighted score below threshold) are a separate, non-waivable enforcement class.

## Clause completeness (the core defensibility lever)
- [ ] **Every clause (4 → 10) is scored or explicitly marked N/A with a stated reason** — no
      clause silently omitted. The conformance matrix lists all of: 4 context · 5 leadership
      (incl. 5.2 policy) · 6 planning (incl. 6.1.2 hazard-id, 6.1.3 legal) · 7 support · 8
      operation · 9 performance evaluation (incl. 9.2 internal audit) · 10 improvement (incl.
      10.2 incident/nonconformity).
- [ ] Each conformance level is the `KB-DATA-ISO45001-MATURITY` scale's (0–4), and **satisfies
      that level's evidence test** — no level 3 "conformant" on a procedure with no records, no
      level asserted on self-assertion alone.
- [ ] A clause with no evidence is **scored as a gap (level 0/1)** with the missing evidence
      named as a `[GAP]` — never a guess, never an omission.

## Certification-blocker flagging
- [ ] **Every mandatory clause at level ≤ 2 is flagged as a certification-blocker** (5.2, 6.1.2,
      9.2, 10.2 and any other mandatory clause) — explicitly, in the gap register, **not
      downgraded** to a minor gap.
- [ ] The blocker vs minor-finding distinction follows ISO/IEC 17021-1 framing (a blocker is a
      major nonconformity that would stop certification).

## Gap traceability + roadmap
- [ ] **Every gap traces to its clause + its evidence basis + a named owner.**
- [ ] The remediation roadmap is **ordered blockers-first** (then high-severity non-blockers,
      then the rest) per `KB-SNIP-GAP-PRIORITISATION`.
- [ ] Every roadmap action is a SMART action — **named owner + ISO due date + a measure +
      a clause link + a cost estimate**; no anonymous actions, no "ASAP".
- [ ] Where clause 6.1 controls are assessed, the **hierarchy of controls is walked** — no
      PPE/admin-only remediation without a higher-order control or an explicit justification.

## Citation + de-identification
- [ ] Every clause number/title cited matches the **selected standard** (ISO 45001 / 14001 /
      45003) — no invented or mis-numbered clause (a `regulatory_citation_accuracy` hard block
      if wrong).
- [ ] **De-identification pass complete BEFORE drafting** — no leaked name, disclosed condition,
      exact date/location, or unsuppressed <5 personnel cell; no re-identification key embedded.
- [ ] No conformance conclusion rests on an unstated assumption (every `[ASSUMPTION]` is labelled).

## Standard selector
- [ ] If Q1 selected ISO 14001 / ISO 45003 / Combined, the matrix scores **that standard's clause
      set** (the matching `KB-STD-*` fragment was read), and the report names the standard assessed.
