---
sme-review:
  personas:
    - role: "PHA facilitator (What-If / What-If-checklist method)"
      expertise: "Systematic What-If question-set design; hazard/consequence elicitation; safeguard adequacy; risk-ranked recommendations; the What-If/Checklist hybrid for procedures and simpler systems."
      lens: "Is the question set systematic enough that no credible failure mode was missed, and is every team answer recorded with a safeguard and an action rather than left hanging?"
---

# SME Review & Sign-off — whatif-facilitator

This skill carries **one** specialized SME lens: a What-If PHA facilitator. It narrows the
family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) to the
disciplined What-If question-set PHA; the generic **HSE-SME-Reviewer** hook is the
inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**What-If is an assistive, team-recorded study.** The bounded scope and the team
(operations + process + facilitator) are the assistive evidence: no full team present →
the worksheet is structured and marked **"study not yet performed"**, never presented as a
completed study. The failure mode this lens guards is an *unsystematic* sweep — a freeform
brainstorm rather than a disciplined seed set. A consequence or rank the team did not raise
is recorded `[GAP]`, never invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The "What if…?" prompts span the disciplined seed set (loss of utility · wrong sequence · wrong material/quantity · human error/omission · external event · equipment failure) — structured, not a freeform brainstorm.
- [ ] No seeded question is left with a blank response; an unaddressed seed reads `[GAP]`, not blank.
- [ ] Each recorded hazard/consequence is plausible for the named process — no invented consequence the team did not raise.
- [ ] Existing safeguards are matched to consequence severity; a high-consequence answer carried only by weak/administrative safeguards is surfaced.
- [ ] Each recommendation carries a named owner + due date + a measure, tracked to closure — not "consider" / "review further".
- [ ] Scope is bounded (one named process / operation / procedure) and the team + competencies are named; an incomplete team carries the "study not yet performed" banner (FLAG).

## Sign-off note
SME review: ran (persona: PHA (What-If) facilitator); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and
it never outputs "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted
score below threshold) are a separate enforcement class owned by the automated harness.
