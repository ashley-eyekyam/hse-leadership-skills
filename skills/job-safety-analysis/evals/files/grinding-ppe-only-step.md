# JSA intake — Fabrication job with a PPE-only grinding step + an empty-steps probe

De-identified intake. All personnel are role labels. This case has TWO purposes:
(1) one step (grinding) is deliberately controlled PPE-only so the skill must escalate
the hierarchy of controls **for that step**; (2) it also probes refuse-on-empty-steps —
the "vague job" variant below must be refused, not silently decomposed by the skill.

## Jurisdiction (Q1)
UK.

## Industry (Q2)
Manufacturing — metal fabrication.

## The job/task (Q3)
Cut, grind, and deburr a steel bracket at the fabrication bench, line 2.

## The job's steps, in order (Q4 — the spine)
1. Mark out the bracket.
2. Cut to length (abrasive chop saw).
3. **Grind the cut edge (angle grinder).**
4. Deburr and inspect.

## Tools / equipment / materials (Q5)
Angle grinder, abrasive chop saw, bench vice, marking tools.

## Who performs the job (Q6)
Own workers (fabricators).

## Environment / conditions (Q7)
Workshop; live plant nearby.

## Likelihood / severity / matrix (Q9 / Q10 / Q11)
Org 5x5 matrix.

## The PPE-only step (the core-value probe)
For **Step 3 (grind)** the ONLY proposed control is a face shield + gloves (PPE-only).
No engineering or substitution control is proposed for grinding; no justification is
recorded for why higher-order controls are not used. Steps 1, 2, and 4 are adequately
controlled (engineering guarding on the chop saw, etc.).

The skill must NOT accept the PPE-only grinding step silently: controls.rank_controls
should return ppe_admin_only = True FOR THAT STEP, and the output must EITHER add a
higher-order control for the grinding step (engineering: local exhaust ventilation /
guarding / a fixed grinding station; substitution: a pre-cut / no-grind method) OR record
an explicit per-step "higher-order controls not reasonably practicable because…"
justification. A JSA that ships the grinding step with PPE as the sole control, no
higher-order option, and no justification scores <=2 on hierarchy_of_controls and is
flagged by the Critic/QA pass.

## The refuse-on-empty-steps probe
If instead the user supplies only a one-line vague job ("do some general fabrication
maintenance") with NO step sequence, the skill must REFUSE to proceed and ask the user to
break the job into its actual ordered steps — it must NOT invent the steps. A JSA with no
steps is not a JSA.
