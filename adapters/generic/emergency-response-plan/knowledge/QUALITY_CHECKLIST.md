# Pre-output Quality Checklist — emergency-response-plan

Validate the draft ERP against this gate **before** producing any output. A failure here
is fixed and re-checked, not shipped.

## Specificity & scenario-keying
- [ ] The plan is for a **named site/facility** with its occupancy — not a generic template.
- [ ] At least **one credible scenario** is captured and each response procedure is
      **scenario-keyed** (site-specific steps) — **no generic "evacuate" with no
      scenario-keyed actions**.
- [ ] Each scenario's site-specific trigger / source / worst-credible case is recorded
      (or `[GAP]` flagged — never invented).

## Prevention before response (the core-value lever)
- [ ] For every scenario, **prevention/elimination controls precede the response** (the
      hierarchy of controls is applied via `controls` + `KB-SNIP-HOC`) — **no
      response-only plan** for a preventable scenario.
- [ ] Any PPE/admin-only treatment carries a higher-order control **or** an explicit
      "not reasonably practicable because…" justification.

## Roles, muster & responders
- [ ] **Every emergency role has a named deputy/alternate** across the shift pattern — no
      command-chain single point of failure.
- [ ] **Muster/assembly points are named** (not "outside"), with evacuation routes, a
      roll-call/head-count method, and provision for visitors/contractors/PRM.
- [ ] The **external-responder interface** (fire/ambulance access, isolation points,
      mutual aid) is specified; any on-site ERT/fire-team capability the plan relies on is
      **proven, not assumed**.

## Drills, dates & owners
- [ ] The **drill schedule is dated** by scenario/site-class (cadence from
      `KB-DATA-DRILL-FREQ`, `source`+`year` quoted; `[GAP]` where unresolved).
- [ ] Every drill and every corrective action has a **named (role-label) owner + a date +
      a measure** (`smart_actions.validate_register` clears — no anonymous, no "ASAP").

## Citations, de-id & boundary
- [ ] The legal ERP baseline is cited correctly (ISO 45001 **8.2**; US 29 CFR 1910.38;
      UK RRFSO 2005 art.15; India Factories Act s.41B → `hse-india`, **never a national
      form number**) — no invented citation.
- [ ] **De-identification pass complete BEFORE drafting**; any circulated copy uses **role
      + duty-phone labels** in the call-out tree (no personal mobile numbers in a widely
      distributed copy); no responder health/medical detail.
- [ ] The **ERP→BCP cross-reference** is present (continuity of critical activities →
      `business-continuity-plan`); the plan has not drifted into RTO/RPO/MTPD recovery.
