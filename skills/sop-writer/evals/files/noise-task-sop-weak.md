# Weak SOP request — abrasive cutting (the specificity + HoC-PPE-only catch fixture)

> This fixture is deliberately WEAK on both core-value levers: generic non-steps and a
> PPE-only control set with no higher-order control and no justification. The skill must
> NOT ship it as-is — it must refuse the vague steps and flag the PPE-only treatment.

**Task (as supplied, vague):** "Write an SOP for the grinding/cutting job. Operate the
machine safely and follow all procedures."

**Steps (as supplied):**
- "Work safely at all times."
- "Follow all the rules."
- "Wear your ear plugs."

**Controls (as supplied):** Hearing protection (ear plugs) — and nothing else. No
isolation, no enclosure, no on-tool extraction, no quieter process, no justification for
the absence of higher-order controls.

**Hazards (implied):** High noise exposure from abrasive cutting; airborne dust;
rotating abrasive wheel.

## What a correct response must do

- REFUSE the generic "work safely" / "follow all rules" steps — elicit/derive real,
  ordered, task-specific steps (or record [GAP] where the user cannot supply them).
- On the control side, `controls.rank_controls` returns `ppe_admin_only: True`; the SOP
  must either ADD a higher-order control (engineering: enclosure / on-tool extraction /
  acoustic damping; substitution: a quieter process) OR record an explicit justification
  that higher-order controls are not reasonably practicable.
- An output that emits boilerplate "work safely" steps with ear plugs as the sole control
  and no higher-order option and no justification scores <=2 on BOTH specificity and
  hierarchy_of_controls and is flagged by the Critic/QA pass.
