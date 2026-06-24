<!-- KB-SNIP-INDUCTION-BASELINE -->
# Induction baseline — mandatory induction-topic set

**Fragment ID:** `KB-SNIP-INDUCTION-BASELINE`
**This is prompt text, applied by the model — not a generator.** It is the mandatory
baseline of induction topics the `induction-pack` (#14) skill layers the **named site's**
specifics onto. A generic induction with no named site/hazards is refused; the verification
level uses `KB-DATA-COMPETENCE-LEVELS`.

> Source: ISO 45001:2018 cl. 7.2/7.3 (competence/awareness) · UK MHSWR 1999 reg. 10/13 (information for employees) · US OSHA orientation duties (General Duty Clause + standard-specific) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the baseline every induction MUST cover, then layer the site's specifics

1. **Emergency arrangements** — alarm, evacuation routes, named muster point(s), what to do
   on discovering an incident (ties to `emergency-response-plan` #15).
2. **Welfare & first aid** — first-aiders, first-aid location, welfare facilities, reporting
   feeling unwell.
3. **Site rules** — access/egress, PPE rules, traffic management, permit/PTW awareness
   (contractor cohorts get the PTW-awareness branch).
4. **Site-specific hazards & controls** — the real hazards of *this* site, each with its
   control ranked via `KB-SNIP-HOC` — never generic.
5. **Incident & concern reporting** — how to report a hazard, near-miss, or concern, and the
   no-blame expectation.

**Refuse-on-vague:** do not issue a pack until the named site + at least the emergency
arrangements + at least one site-specific hazard are captured. Every topic ties to a **named
site arrangement**, not boilerplate.

**Verification:** every induction produces a **competence-verification record** (per
inductee, role-labelled in any shared copy) proving the content was understood, at the
verification level set on `KB-DATA-COMPETENCE-LEVELS`; an induction with no verification
record fails the quality gate (#14 eval case 3).

## Output expectation

A site-specific delivery pack (baseline + layered site specifics), an inductee verification
record, and a refresher schedule. Feeds `specificity` and `defensibility`.
