---
sme-review:
  personas:
    - role: "Site HSE Manager"
      expertise: "Running site inductions for permanent staff, contractors and visitors on a live operational site; knowing this site's real hazards, emergency arrangements (muster points, evacuation routes), traffic management and permit systems; setting the competence-verification level a role must reach before site access; ISO 45001 7.2/7.3 (competence/awareness) and the legal-induction duty (UK MHSWR reg. 10/13 / US OSHA orientation / India Factories Act s.111A)."
      lens: "Would I let this person onto MY site on the strength of this induction? Is every topic tied to THIS site's real arrangement (the actual named muster point, the real traffic plan, the specific permits) rather than generic boilerplate, are the site's real hazards present with controls ranked up the hierarchy, is there a competence-verification record proving understanding (not just an attendance sheet), and is the refresher scheduled with a named owner and date?"
modes:
  induction:
    detected_by: "Q = the requested deliverable (a site induction pack for the named site and cohort) — single-output skill; this mode is always active"
    floor:
      - id: site-specific-not-generic
        description: "Every topic is tied to a named site arrangement (the actual muster point, traffic plan, permits) — generic-only boilerplate is a FLAG"
        anchors: ['this site|site-specific|named|specific', 'muster|hazard|arrangement']
        min_matches: 2
      - id: site-hazards-controls-ranked
        description: "The named site's real hazards are present with controls ranked up the hierarchy (not PPE-only)"
        anchors: ['hazard', 'hierarchy|control']
        min_matches: 2
      - id: competence-verification-understanding
        description: "A competence-verification record proves UNDERSTANDING per inductee (not just an attendance/signature sheet)"
        anchors: ['competence|verification', 'understanding|per inductee|record']
        min_matches: 2
      - id: verification-matches-role-risk
        description: "The verification level matches the role's task risk — a high-hazard role is not downgraded to a tick-box induction"
        anchors: ['role|task', 'verification|competence']
        min_matches: 2
      - id: contractor-site-rules-ptw
        description: "The contractor cohort gets site-rules + permit-to-work awareness — a contractor induction with no PTW/site-rules content is a FLAG"
        anchors: ['contractor', 'permit|site rule|ptw']
        min_matches: 2
      - id: refresher-scheduled-owned
        description: "A named-owner + dated refresher cadence by role-risk is scheduled — an induction with no refresher is flagged [GAP]"
        anchors: ['refresher', 'schedul|owner|due|date']
        min_matches: 2
---

# SME Review & Sign-off — induction-pack

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **Site HSE Manager** — the person who actually inducts people onto a
live site and owns the consequence of a generic induction. The universal hard gates (de-id leak,
citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **No generic-only content — every topic tied to a named site arrangement** — the emergency
      section names *this* site's muster point(s) and routes; the traffic section names *this*
      site's plan; the permit section names *this* site's PTW systems; the hazards are *this*
      site's real hazards. An induction that would read identically for any site is a FLAG (it is
      boilerplate, not a site induction).
- [ ] **The site's real hazards are present, controls ranked** — the named site's actual hazards
      are in the pack, each with its control ranked via `KB-SNIP-HOC`; a hazard treated PPE-only,
      or a known site hazard missing entirely, is a FLAG.
- [ ] **A competence-verification record is present and proves understanding** — per inductee,
      role-labelled in any shared copy, at the verification level the role needs on
      `KB-DATA-COMPETENCE-LEVELS` and the method from Q6. An "induction" that is only delivery
      content (an attendance sheet, no proof of understanding) is a FLAG.
- [ ] **Verification level matches the role's task risk, not downgraded** — a high-hazard role
      signed off at "aware" when the task needs "competent" is a FLAG.
- [ ] **The contractor cohort got site-rules + PTW awareness** — a contractor induction with no
      permit-to-work awareness, or not following prequalification, is a FLAG.
- [ ] **No inductee health/medical detail or names in a widely distributed copy** — inductee names
      live only on the legitimate signed verification record; a name or a medical note in a
      shared-distribution copy is a FLAG (and a `de_identification` hard block).
- [ ] **The refresher is scheduled** — a named-owner + dated refresher cadence by role-risk; an
      induction with no refresher schedule, or "refresh ASAP", is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The attendance sheet masquerading as verification** — a signed "I attended" list is not proof
  of understanding; without a per-inductee comprehension check (questions answered, a practical
  sign-off) the induction has verified nothing. Check the verification proves understanding.
- **The regime named, its element set unswept (S6)** — naming "site rules" or "the permit system"
  while omitting the concrete arrangements an inductee must actually know: the real muster point,
  the traffic/pedestrian segregation, the specific permits, first-aid and reporting routes.
- **Cohort mismatch** — a single generic pack issued to permanent operatives, contractors, and
  visitors alike; each cohort's risk exposure and the depth it needs (PTW awareness for
  contractors, escort rules for visitors) differ and must be addressed.
- **The un-owned refresher** — a refresher "recommended annually" with no named owner, no trigger
  (role change, incident, rule change) and no date is not scheduled; it is a hope.

## Sign-off note
SME review: ran (persona: Site HSE Manager); this is **decision-support only**. It **precedes —
and never replaces, never emits — the human competent-person sign-off**, and it never outputs the
affirmative claim "inducted" or "approved by a competent person". A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented/mis-cited regulation,
weighted score below threshold) are a separate enforcement class.
