# Methodology — what makes a good toolbox talk

A toolbox talk is a short, pre-task safety briefing delivered to a crew before they
start a specific job. It is the frontline operational realisation of **ISO 45001
clause 7.4 (communication)** and **5.4 (consultation & participation of workers)** —
the moment the management system actually reaches the people doing the work. Its
value is **speed + specificity together**: it must be deliverable in ~2 minutes, yet
be entirely about *this* task, *this* crew, *this* site. A generic talk has failed.

## The five marks of a good talk

1. **Specific, not generic.** Name the actual task, site/area, and crew, and the
   concrete observable hazards of *that* job (the leading edge, the unavailable MEWP,
   the live conductor) — not a hazard *category* ("work safely at height"). This is
   the single lever the skill exists to force; the load-bearing intake Q3 (site +
   specific task) is where it is captured, and a vague answer is refused, never
   papered over.
2. **Hierarchy-of-controls-aware.** State higher-order controls first (eliminate →
   substitute → engineer → administrate → PPE). If only PPE/admin controls are
   available, **say why** higher-order controls are not reasonably practicable —
   never default to "wear your PPE". Each control names the hazard it addresses.
   (Prompt-side `KB-SNIP-HOC` discipline; B3 wires no `controls.py`.)
3. **Two-way, not a lecture.** Build in 2–3 open discussion prompts that get the crew
   talking about what could go wrong on *their* task today. Participation (5.4) is the
   point — a talk read *at* a crew teaches less than one that asks them.
4. **One clear takeaway set.** 3–5 short, actionable points the crew can act on this
   shift. Keep within the duration target (intake Q4, default <5 min) and at the
   crew's reading level (Q6). Short paragraphs, plain language, frontline-readable.
5. **Signed off.** Every talk ends with an attendance / sign-off sheet (Name/Role ·
   Signature · Date). The sign-off is what makes the briefing **auditable** — a
   toolbox talk with no attendance record is not defensible.

## Incident references — de-identify, and never fabricate

A recent relevant incident or near-miss makes a talk vivid and credible — but only if
it is true and protected:

- Any **real** incident the user references is run through the de-identification scrub
  (the `deid` block, before drafting): role labels only, no names, no <5 injury cells,
  no re-identification key in the talk.
- If the user supplies **no** incident, use a **clearly-labelled typical / illustrative
  example** ("a near-miss of this type reported elsewhere") — **never** fabricate a
  "last week on this site" local event. A fabricated local incident is both a
  defensibility failure and a trust-destroyer: a crew that knows it did not happen
  loses faith in the whole talk.

## The single-thread assembly

B3 assembles the talk in one short pass (no subagent fan-out): de-identify → hook →
specific hazards → HoC-aware controls → de-identified-or-typical incident → discussion
prompts → takeaways + sign-off. The mandatory Critic/QA self-check then validates the
draft against `QUALITY_CHECKLIST.md` before the report is produced.
