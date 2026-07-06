---
sme-review:
  personas:
    - role: "Emergency Planning Officer"
      expertise: "ISO 45001 clause 8.2 emergency preparedness & response; scenario-based emergency planning, evacuation & muster design, call-out-tree and incident-command roles with deputies, drill programme design and cadence, and the fire/ambulance/mutual-aid responder interface (29 CFR 1910.38, RRFSO 2005 art.15, Factories Act s.41B)."
      lens: "Would this plan actually work on the day — is it keyed to THIS site's credible scenarios with prevention before response, does every emergency role have a named deputy, are muster points named and reachable, is the drill schedule dated and realistic, and is the on-site response capability proven rather than assumed?"
modes:
  erp:
    detected_by: "Q = the requested deliverable (an emergency response plan for the named site and its credible scenarios) — single-output skill; this mode is always active"
    floor:
      - id: prevention-before-response
        description: "For each scenario the prevention/elimination controls come FIRST — the plan does not rely solely on reacting to the emergency"
        anchors: ['prevention', 'response']
        min_matches: 2
      - id: scenario-keyed-not-generic
        description: "Each procedure is built from THIS site's credible scenarios with site-specific steps — a generic 'evacuate' procedure is a FLAG"
        anchors: ['scenario', 'credible|site-specific|this site']
        min_matches: 2
      - id: roles-have-named-deputies
        description: "The call-out tree and incident-command roles each have a named deputy/alternate — a single point of failure in the command chain is a FLAG"
        anchors: ['deput|alternate', 'role|command|call.out']
        min_matches: 2
      - id: muster-points-named-reachable
        description: "Assembly/muster points are named for the site (not 'assemble outside') with evacuation routes and a head-count/roll-call arrangement"
        anchors: ['muster|assembly', 'evacuat|route']
        min_matches: 2
      - id: drill-schedule-dated
        description: "Drills are scheduled by scenario/site-class with dates and owners (cadence from KB-DATA-DRILL-FREQ, source+year) — an undated 'do drills' line is a FLAG"
        anchors: ['drill', 'schedul|date']
        min_matches: 2
      - id: external-responder-interface
        description: "Fire/ambulance access, isolation points and any mutual-aid arrangement are specified, not implied"
        anchors: ['access|isolation', 'fire|ambulance|mutual|responder']
        min_matches: 2
      - id: erp-bcp-boundary
        description: "The plan stays within emergency response and carries the one-line pointer to business-continuity-plan for continuity of critical activities — the two are not merged"
        anchors: ['business-continuity-plan|business continuity', 'continuity']
        min_matches: 2
---

# SME Review & Sign-off — emergency-response-plan

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`) into an **Emergency Planning Officer**. The universal
hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are
the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Prevention precedes response** — the plan does not rely solely on reacting to the emergency; for each scenario the **prevention/elimination controls come first** (apply `KB-SNIP-HOC`). A response-only plan for a preventable scenario (e.g. flammable storage with no source/ignition control) is a FLAG.
- [ ] **Scenario-keyed, not generic** — each procedure is built from THIS site's credible scenarios (Q2) with site-specific steps; a generic "evacuate" procedure with no scenario-keyed actions is a FLAG.
- [ ] **Every role has a named deputy** — the call-out tree and incident-command roles each have a deputy/alternate; a single point of failure in the command chain (no deputy) is a FLAG.
- [ ] **Muster points are named & reachable** — assembly/muster points are named for the site (not "assemble outside"), with evacuation routes and a head-count/roll-call method; an unnamed or unreachable muster point is a FLAG.
- [ ] **Drill schedule is dated & realistic** — drills are scheduled by scenario/site-class with dates and owners (cadence from `KB-DATA-DRILL-FREQ`, source+year quoted); an undated "do drills periodically" is a FLAG.
- [ ] **Response capability is proven, not assumed** — where the plan relies on an on-site ERT/fire team, that capability (training, numbers, availability across shifts) is evidenced; a plan that assumes a capability that may not exist on the day is a FLAG.
- [ ] **External-responder interface is real** — fire/ambulance access, isolation points and any mutual-aid arrangement are specified, not implied.
- [ ] **ERP↔BCP boundary honoured** — the plan stays within emergency response and carries the one-line pointer to `business-continuity-plan` for continuity of critical activities; it does not drift into RTO/RPO/MTPD recovery planning.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The response capability assumed, not proven** — where the plan relies on an on-site
  emergency/fire/first-aid team, that capability (numbers trained, availability across all shifts,
  equipment maintained) must be evidenced; a plan that assumes a team that may not be present on
  the night shift is hollow.
- **The regime/scenario named, its control set unswept (S6)** — a credible scenario named (fire,
  chemical release, medical) while the concrete site-specific steps, isolation points and PPE for
  that scenario are silently generic. Build each procedure from the scenario's real controls.
- **The unreachable muster point** — a muster point named but on the wrong side of the hazard
  (downwind of a release, past the fire), or with no alternate for a blocked primary route. Name
  a primary AND an alternate assembly point and the head-count owner.
- **Vulnerable-persons and out-of-hours gaps** — evacuation of mobility-impaired/lone/night-shift
  workers and visitors is a routine ERP omission; the plan states the arrangement or flags [GAP].

## Sign-off note
SME review: ran (persona: Emergency Planning Officer); this is **decision-support only**.
It **precedes — and never replaces, never emits — the human competent-person sign-off**,
and it never outputs the affirmative claim "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
