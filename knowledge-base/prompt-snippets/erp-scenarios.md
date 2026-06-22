<!-- KB-SNIP-ERP-SCENARIOS -->
# Emergency-response scenarios — credible-scenario catalogue + procedure skeletons

**Fragment ID:** `KB-SNIP-ERP-SCENARIOS`
**This is prompt text, applied by the model — not a generator.** It is the credible-scenario
catalogue and the response-procedure skeleton the `emergency-response-plan` (#15) skill keys
its plan to. Drill cadence per scenario is resolved from `KB-DATA-DRILL-FREQ`.

> Source: ISO 45001:2018 cl. 8.2 (emergency preparedness & response) · US OSHA 29 CFR 1910.38 (EAP) · UK RRFSO 2005 art. 15 · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

### Credible-scenario menu (select those credible for the named site — refuse generic)
- Fire / explosion · chemical or gas release · medical emergency · structural collapse ·
  severe weather / flood · security / violence · loss of critical utilities.
- Add site-specific scenarios from the hazard profile (e.g. confined-space rescue, LOTO
  failure, vehicle/plant incident).

### Per-scenario response-procedure skeleton
For each selected scenario produce:
1. **Prevention first** — the higher-order controls that reduce the scenario's likelihood,
   ranked via `KB-SNIP-HOC`; **never** a plan that relies on response alone (#15 eval case 1).
2. **Detection & alarm** — how it is detected, how the alarm is raised.
3. **Immediate actions** — make-safe, isolate, evacuate or shelter, scenario-specific steps
   (not a generic "evacuate" — #15 eval case 2).
4. **Roles & call-out** — named roles **each with a deputy**; the call-out tree.
5. **Muster & headcount** — named muster point(s), roll-call, all-clear.
6. **External-responder interface** — access, isolation points, information handover.
7. **Recovery / stand-down** and the link to `business-continuity-plan` (#26) for continuity
   of critical activities.

**Capability before reliance:** prove the rescue/response capability the procedure assumes
exists (trained ERT, equipment) before the plan relies on it; schedule the drill from
`KB-DATA-DRILL-FREQ`.

## Output expectation

Scenario-keyed procedures, a call-out tree with deputies, muster arrangements, responder
integration, and a dated drill schedule. Feeds `specificity`, `hierarchy_of_controls`,
`defensibility`.
