---
sme-review:
  personas:
    - role: "mine-rescue superintendent / emergency-preparedness officer (rescue-station / mutual-aid scheme experience)"
      expertise: "mine-rescue team mobilisation, rescue-station coverage, mutual-aid agreements, NDMA/DGMS emergency-preparedness duties, irrespirable-atmosphere / entrapment / inrush / fire scenarios, drill regimes"
      lens: "If this scenario happened tonight, is the mobilisation REAL and TIMEABLE — named team, named station, named mutual-aid, credible travel/donning/deployment timing — or an aspirational placeholder that fails on the night?"
modes:
  erp:
    detected_by: "Q1 — Draft new ERP or review-gap-check existing; Q4 selects the emergency scenarios. The floor applies to every ERP output."
    floor:
      - id: mobilisation-concrete-timeable
        description: "Mobilisation is concrete and timeable end-to-end — named team -> named station -> named mutual-aid, each with credible timing; 'as required' / 'to be arranged' / unnamed links are a miss (realism is the point) (intake Q5/Q6/Q7)"
        anchors: ['mobilis', 'timeline|response time|timing']
        min_matches: 2
      - id: route-matches-scenario
        description: "The mobilisation route matches the mine type and worst-credible scenario — an underground irrespirable-atmosphere event needs breathing-apparatus coverage and re-fresh-base logic, not a surface-only response (intake Q2/Q4)"
        anchors: ['breathing apparatus|self.rescuer|refuge', 'scenario']
        min_matches: 2
      - id: scenarios-ranked
        description: "Scenarios are risk-ranked on the org matrix and the highest-ranked drive the plan detail (intake Q9)"
        anchors: ['scenario', 'rank']
        min_matches: 2
      - id: drills-schedule-owned
        description: "A drills/exercise schedule exists with owner + due date / cadence for each critical scenario (intake Q8)"
        anchors: ['drill', 'owner|cadence']
        min_matches: 2
      - id: mutual-aid-agreed
        description: "Mutual-aid and rescue-station links are reciprocated/agreed and named, not assumed — an un-agreed dependency is [ASSUMPTION], never silent (intake Q6)"
        anchors: ['mutual.aid', 'station']
        min_matches: 2
      - id: refuge-selfrescuer-comms
        description: "Self-rescuer / refuge-chamber / escapeway / communication provisions appear where the scenario demands (underground gassy/fire)"
        anchors: ['refuge', 'self.rescuer|scsr|escapeway']
        min_matches: 2
      - id: command-structure
        description: "An incident command structure and activation/notification chain define who runs the response and how it is triggered"
        anchors: ['command', 'activation|notif']
        min_matches: 2
---

# SME Review & Sign-off — mine-rescue-erp

Single specialized persona, narrowing the **Mine Manager** archetype slot
(`KB-SNIP-ARCHETYPES`, archetypes:291-326 — its "mine-rescue mobilisation realistic
… names the rescue team / station / mutual-aid and a credible mobilisation timing,
not an aspirational placeholder" bullet, archetypes:310-311) to a mine-rescue
superintendent. The persona's hardest, most distinctive value is the
**timing-realism** check — exactly the dimension the generic HSE-SME-Reviewer cannot
judge (SME audit:221-223); make it the headline test.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Mobilisation is concrete and timeable end-to-end — named team → named station → named mutual-aid → NDMA/DGMS alignment, each with credible timing; FLAG any "as required" / "to be arranged" / unnamed link (realism is the whole point).
- [ ] The mobilisation route matches the mine type and worst-credible scenario — e.g. an underground irrespirable-atmosphere event → breathing-apparatus team coverage and re-fresh-base logic, not a surface-only response; FLAG a route that cannot reach the credible scenario.
- [ ] Scenarios are ranked on the org matrix and the highest-ranked drive the plan detail; FLAG a plan whose detail does not concentrate on the top-ranked scenarios.
- [ ] A drills schedule exists with owner + due date for each critical scenario; FLAG missing/undated drills.
- [ ] Mutual-aid and station links are reciprocated/agreed, not assumed; FLAG a dependency stated without evidence the partner agreed coverage (an un-agreed link is `[ASSUMPTION]`).
- [ ] Self-rescuer / refuge-chamber / communication provisions appear where the scenario demands (underground gassy/fire); FLAG their absence from an underground plan ranking fire/explosion or irrespirable atmosphere as credible.

> **[GAP]** Indian statutory mine-rescue drill cadence / rescue-station rules are cited
> generically via `KB-REG-IN-MINES-ACT`; the intake authors the drill-cadence question
> as confirm-against-duty rather than a hard-coded interval (intake audit:211) — confirm
> the live cadence with a competent person, never a fabricated interval.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The aspirational placeholder** — "rescue team will respond quickly", "mutual aid as
  required", an unnamed station; a plan that reads complete but has no named, timeable
  mobilisation and fails on the night.
- **The route that cannot reach the scenario** — a surface-oriented response for an
  underground irrespirable-atmosphere or fire event, with no breathing-apparatus coverage,
  re-fresh base, or refuge/self-rescuer logic for the credible worst case.
- **The un-agreed dependency** — mutual-aid or station coverage assumed rather than shown as
  reciprocated/agreed; a link recorded as fact that is really an `[ASSUMPTION]`.
- **Undated drills** — a plan with no drill schedule, or drills with no owner and no cadence,
  so preparedness cannot be assured.
- **Detail in the wrong place** — plan depth spread evenly instead of concentrated on the
  top-ranked scenarios, so the highest-consequence event is under-planned.

## Sign-off note
Reviewed-as: mine-rescue superintendent — model QA (decision-support); recorded,
FLAGs non-blocking. This review precedes — and never replaces, never emits — the
competent person who must validate mobilisation realism and sign off; it never
outputs "approved by a competent person".
