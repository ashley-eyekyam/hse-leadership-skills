---
sme-review:
  personas:
    - role: "PHA facilitator (What-If / What-If-checklist method)"
      expertise: "Systematic What-If question-set design; hazard/consequence elicitation; safeguard adequacy; risk-ranked recommendations; the What-If/Checklist hybrid for procedures and simpler systems."
      lens: "Is the question set systematic enough that no credible failure mode was missed, and is every team answer recorded with a safeguard and an action rather than left hanging?"
modes:
  question-register:
    detected_by: "Q10 — What output, audience, distribution? (Worksheet / Full report — both emit the What-If question register, the skill's single artifact class)"
    floor:
      - id: bounded-scope-and-kind
        description: "One named procedure/operation/system as the bounded scope with its kind stated — never 'the site' (intake Q1 specificity anchor)"
        anchors: ['procedure|operation|system', 'scope']
        min_matches: 2
      - id: disciplined-seed-set
        description: "The question set spans the disciplined seeds — loss of utility · wrong sequence · wrong material/quantity · human error/omission · equipment failure · external event · start-up/shutdown/abnormal — structured, not a freeform brainstorm (intake Q3)"
        anchors: ['loss of utilit', 'wrong (sequence|material|product)', 'human error']
        min_matches: 2
      - id: what-if-question-rows
        description: "Each register row is a recorded 'What if …?' question with the team's answer — an unaddressed seed reads a literal [GAP], never a silent blank"
        anchors: ['what if']
        min_matches: 1
      - id: safeguards-matched-to-severity
        description: "Existing safeguards are recorded per row and matched against consequence severity; a high-consequence answer carried by administrative safeguards alone gets a higher-order recommendation (KB-SNIP-HOC)"
        anchors: ['safeguard', 'higher.order|hierarchy of controls']
        min_matches: 2
      - id: rows-risk-ranked
        description: "Each row's consequence is risk-ranked on the named matrix (intake Q8, risk_matrix output)"
        anchors: ['risk rank|risk band', 'matrix|5.?[x×].?5']
        min_matches: 1
      - id: actions-owned-to-closure
        description: "Each recommendation carries a named role owner + due date + measure, tracked to closure — never 'consider' / 'review further' (smart_actions discipline)"
        anchors: ['named owner|action owner', 'due date', 'closure']
        min_matches: 2
      - id: team-facilitator-recorded
        description: "The team (operations + process) and facilitator/scribe are recorded as roles; an incomplete team carries the 'study not yet performed' banner (intake Q6/Q7, the assistive evidence)"
        anchors: ['facilitator|scribe', 'team']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A brainstorm formatted as a study** — plausible questions and answers, but no seed-set
  spine; the reader cannot tell whether 'what if cooling is lost' was answered or never
  asked — the systematic-coverage claim is the first thing to silently vanish.
- **Answers without dispositions** — hazards recorded, safeguards listed, and then
  nothing: no rank, no action, no owner; the register documents worry rather than
  managing it.
- **The abnormal-modes hole** — steady-state questions answered thoroughly while
  start-up/shutdown/abnormal-operation seeds (where the incidents actually live) are
  missing entirely.
- **Severity-blind safeguard credit** — a catastrophic-consequence row 'covered' by the
  same operator-check safeguard as a trivial one, with no escalation; the matrix rank and
  the safeguard order never talk to each other.

## Sign-off note
SME review: ran (persona: PHA (What-If) facilitator); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and
it never outputs "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted
score below threshold) are a separate enforcement class owned by the automated harness.
