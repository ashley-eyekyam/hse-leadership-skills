# Pre-output Quality Checklist — induction-pack

Validate the draft induction pack against this gate **before** producing any output. A failure
here is fixed, not shipped. The universal hard blocks (de-id leak, invented/mis-cited regulation,
weighted score below threshold) are a separate, non-waivable enforcement class.

## Site-specificity (the core defensibility lever)
- [ ] **No generic-only content** — the pack is grounded in a **named site**; a generic induction
      with no named site or site-specific hazards is **refused**, not shipped.
- [ ] **Every baseline topic is tied to a named site arrangement** — the actual named muster
      point, the real traffic-management plan, the specific permit systems, the real site hazards
      of *this* location. A topic with no named site arrangement is a `[GAP]`, never boilerplate.
- [ ] **A different site produces a different induction** — the named hazards and arrangements of
      a warehouse and an oil terminal differ; a pack that would read identically for any site
      fails the specificity test.
- [ ] The **mandatory baseline** (`KB-SNIP-INDUCTION-BASELINE`) is fully covered — emergency ·
      welfare & first aid · site rules · site-specific hazards · incident/concern reporting — and
      the baseline is the floor, not the whole pack.

## Hierarchy of controls
- [ ] Every **site-specific hazard** carries its control ranked via `KB-SNIP-HOC` (Elimination →
      Substitution → Engineering → Administrative → PPE) — **no PPE/admin-only line** without a
      higher-order control or an explicit justification.

## Competence-verification record (always present)
- [ ] **A competence-verification record is present** — per inductee, role-labelled in any shared
      copy. An induction with **no verification record fails the quality gate** (it is not just an
      attendance sheet — it proves the content was understood).
- [ ] The **verification level** for each role is set on `KB-DATA-COMPETENCE-LEVELS` (aware /
      trained / competent / expert), by the role's task risk — **never downgraded** to pass an
      inductee — and the verification method (Q6) is named.

## Refresher schedule
- [ ] The **refresher schedule** is present, with each refresher a SMART action — **named owner +
      ISO due date** — and higher-risk roles refreshing more often. No anonymous actions, no "ASAP".

## Citation + de-identification
- [ ] Every legal-induction citation matches the resolved jurisdiction (UK MHSWR reg. 10/13 / US
      OSHA orientation duties / India Factories Act s.111A → `hse-india`) — **no invented or
      mis-cited regulation, no national form number minted** (a `regulatory_citation_accuracy`
      hard block if wrong).
- [ ] **De-identification pass complete BEFORE drafting** — inductee names appear **only** on the
      legitimate signed verification record; **role labels** in any widely distributed copy; **no
      inductee health/medical detail** in the pack; **no re-identification key** embedded.
- [ ] No induction conclusion rests on an unstated assumption (every `[ASSUMPTION]` is labelled).
