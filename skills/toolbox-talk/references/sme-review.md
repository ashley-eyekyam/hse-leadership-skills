---
sme-review:
  personas:
    - role: "Frontline safety supervisor / crew lead (toolbox-talk delivery)"
      expertise: "Pre-task briefings, tailgate/pre-start talks, communicating one specific hazard to a working crew, near-miss storytelling without fabrication, and getting crew engagement in a short window."
      lens: "Is this talk about THIS task/crew/site today, deliverable in the target time, with real controls and a real (or clearly-labelled typical) incident — never a fabricated local event and never generic safety patter?"
modes:
  short-briefing:
    detected_by: "Q4 — Duration target (<5 min default / 5–10 min / 10–15 min): every intake path emits the ONE short pre-task briefing artifact; Q4 caps its script length, and Q3 (site/area & the specific task today) anchors what it briefs"
    floor:
      - id: named-task-hazards
        description: "The hazards of THIS task/site/crew today are named concretely (intake Q3, the load-bearing specificity anchor) — never a generic hazard category that could be briefed anywhere"
        anchors: ['hazards? on this (job|task|shift|bay)', 'on this job \(not', 'the exact task today']
        min_matches: 1
      - id: duration-target
        description: "The talk declares its delivery time budget and is deliverable within it (intake Q4 — <5 min is the frontline norm; a script over budget is a FLAG)"
        anchors: ['duration.{0,30}minute', 'under \d+ minutes', '<\s*\d+\s*min']
        min_matches: 1
      - id: hierarchy-of-controls
        description: "Controls are hierarchy-aware even in a short talk — higher-order controls named first; PPE is the last line, never the only line; if only PPE/admin, say why (KB-SNIP-HOC discipline)"
        anchors: ['highest.protection controls first', 'ppe is the last line', 'hierarchy of controls']
        min_matches: 1
      - id: incident-reference
        description: "A recent relevant incident/near-miss appears de-identified (role labels) OR as a clearly-labelled typical/illustrative example — NEVER a fabricated local event (intake Q5, Decision 6)"
        anchors: ['illustrative example', 'typical (case|example)', 'not a local event', 'de.identified']
        min_matches: 1
      - id: discussion-prompts
        description: "2–3 open crew questions that engage, not lecture — the crew talks it through, they are not talked at"
        anchors: ['talk it through', 'discussion (prompt|question)', 'open (crew )?question']
        min_matches: 1
      - id: key-takeaways
        description: "Actionable takeaways the crew can act on today — short, concrete, task-specific"
        anchors: ['take.?away', 'things to take']
        min_matches: 1
      - id: sign-off-attendance
        description: "A fillable attendance / sign-off sheet (Name/Role, Signature, Date) is present — the auditable record that the briefing happened"
        anchors: ['attendance', 'sign.?off', 'signature']
        min_matches: 1
---

# SME Review & Sign-off — toolbox-talk

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a frontline supervisor / crew-briefing SME. This is the
leanest skill in the pack, so the checklist stays short and frontline. The universal hard
gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Specific to this task/crew/site today — generic patter that could be delivered anywhere is a FLAG.
- [ ] The incident is real-and-de-identified OR a clearly-labelled typical example — a fabricated local event is the signature toolbox-talk FLAG and a defensibility trap; never invent one.
- [ ] Controls are hierarchy-aware even in a short talk — name higher-order controls first; if only PPE/admin, say *why*.
- [ ] Deliverable in the target duration — a script over its time budget is a FLAG.
- [ ] Discussion prompts engage, not lecture — 2–3 open crew questions.
- [ ] A sign-off / attendance sheet is present with actionable takeaways — a talk with no signable record is a FLAG.
- [ ] Right tool — a request needing a full hazard assessment / investigation is steered to risk-assessment / job-safety-analysis / incident-investigation.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the
short-briefing must-include floor (the tripwire the pass reconciles against — never its
search space). Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class goes hollow):
- **The anywhere-talk** — fluent, well-formed safety patter (statistics, "stay alert", broad
  hazard-category talk) that could be delivered on any site to any crew; the Q3 task/site
  anchor never lands, so nothing in the talk is checkable against today's actual job.
- **The invented local story** — the signature toolbox-talk trap: an engaging "last week on
  this site" event that never happened, added because a story lands better than a statistic.
  Only a de-identified real event or a clearly-labelled *typical* example is defensible;
  an unlabelled, unverifiable local anecdote is a fabrication finding, not colour.
- **PPE-first in two minutes** — the short format used as a licence for a flat "wear your
  harness / gloves / hard hat" list with no higher-order control named and no *why* when
  only PPE/admin remains; brevity never suspends the hierarchy.
- **The lecture** — no open crew questions and no actionable takeaways: the crew is talked
  at for two minutes and walks away with nothing they can do differently today.
- **The unsignable talk** — no attendance / sign-off record, so there is no auditable
  evidence the briefing ever happened or who received it.

Boundedness (the short-artifact guard): on a ~2-minute briefing the lens surfaces a SHORT
deficiency note — `[GAP]` lines naming the item with a one-line reason — and NEVER pads the
talk toward a full assessment to satisfy the floor; a request that genuinely needs that
depth is steered to risk-assessment / job-safety-analysis instead (the right-tool check in
the domain checklist above).

## Sign-off note
SME review: ran (persona: Frontline safety supervisor / crew lead); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
