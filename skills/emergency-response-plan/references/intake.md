---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE,
           ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "Captured implicitly via Q2 credible-scenario selection (the scenario set is the operative sector cut for an ERP); a generic ERP serves All industries, so a separate industry question is not load-bearing."
    ELI-SCORING: "No risk-matrix scoring in this skill — the ERP is scenario-keyed (credible-scenario catalogue), not a likelihood×severity-scored assessment; the scoring dimension does not apply."
  branches:
    - {when: Q1, route_to: business-continuity-plan, note: "Continuity request (RTO/RPO/MTPD) routes to business-continuity-plan; ERP stays emergency-response-only", mandatory: true}
    - {when: Q2, activates_questions: [Q2a], activates_kb_row: KB-SNIP-ERP-SCENARIOS, note: "each selected credible scenario activates its procedure stub", mandatory: false}
    - {when: Q5, option: India, activates_questions: [Q5a], activates_kb_row: KB-REG-IN-FACTORIES, route_to: hse-india, mandatory: true}
---

# Structured intake — emergency-response-plan

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
intake opens with the **site & ERP/BCP disambiguation gate (Q1)**, then enumerates the
credible scenarios (Q2, the per-scenario branch), the response capability (Q3), the
external-responder interface (Q4), the jurisdiction (Q5, the mandatory India→state
branch), and the drill history (Q6). **Refuse to proceed on a vague request** — no plan
until the named site + ≥1 credible scenario + muster/evacuation arrangements are
captured.

**ERP↔BCP boundary (D-07):** this skill plans the **immediate emergency response**
(scenarios / muster / evacuation / call-out tree). If the user wants **continuity of
critical activities after the emergency is controlled** (RTO / RPO / MTPD, recovery
strategies), Q1 routes them to **`business-continuity-plan`** — the two are complementary,
never merged. This generic ERP does not subsume `mine-rescue-erp` (mining) or the
marine/offshore-emergency skill.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Site & occupancy** + ERP/BCP disambiguation | free-text + MCQ | "Which specific site/facility, and its headcount / shift pattern?" — **the specificity anchor; refuse a generic site.** Confirm scope: **Emergency response** (scenarios/muster/evacuation — this skill) **or** Continuity of critical activities (RTO/RPO/MTPD → route to `business-continuity-plan`) | ELI-SUBJECT | always |
| Q1b | Output artifact + reader | MCQ | Full ERP document (default) / evacuation-plan extract / drill schedule only — and reader (site management / consultant / frontline crew) | ELI-OUTPUT | always |
| Q2 | **Credible scenarios for THIS site** | MCQ multi-select | Fire/explosion · Chemical/gas release · Medical · Structural/collapse · Severe weather/flood · Security/violence · Loss of utilities — **branch to a scenario-specific procedure stub per selection** (`KB-SNIP-ERP-SCENARIOS`) | ELI-SCOPE | always |
| Q2a | *(per scenario)* Scenario specifics | free-text | "For each selected scenario, what is the site-specific trigger / source / worst-credible case?" — keeps each procedure scenario-keyed, not generic | ELI-LOCATION | Q2 has a selection |
| Q3 | **On-site response capability** | MCQ | First-aiders only / Trained ERT / Fire team / None — capability must be **proven before the plan relies on it** (seeds the prevention-vs-response baseline) | ELI-BASELINE | always |
| Q4 | **External responders & site interface** | free-text | "Fire/ambulance access routes, isolation points, assembly/muster points, and any mutual-aid arrangement?" — drives the responder-integration sheet + named muster points | ELI-OBLIGATIONS | always |
| Q4b | **Roles, deputies & owners** | free-text | "Who are the emergency roles (Incident Controller, wardens, first-aiders) and their **deputies**, and who owns the plan + drills? (named role — no 'TBD'; no deputy = a FLAG)" | ELI-COMPETENCY | always |
| Q5 | **Jurisdiction** | MCQ | India / UK / USA / EU / Other / Unknown (India → Q5a) — sets the legal ERP baseline (8.2 / 1910.38 / RRFSO art.15 / s.41B) | ELI-JURIS | always |
| Q5a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; never a national form number** | ELI-JURIS | Q5 == India |
| Q6 | **Drill history** | free-text | "What drills have been run, and when? (optional; 'none' → `[GAP]`)" — seeds the **dated drill schedule** against `KB-DATA-DRILL-FREQ` | ELI-EVIDENCE | always |
| Q6b | Drill / review cadence | MCQ + free-text | Per `KB-DATA-DRILL-FREQ` by scenario/site-class / Annual / On change / Other (+date) — the temporal validity + drill cadence | ELI-TEMPORAL | always |

**Exposed population (ELI-EXPOSURE):** captured within Q1 (occupancy / headcount / shift
pattern) and Q4 (visitors, neighbours, contractors at the muster/assembly points) — the
ERP must account for **everyone who could be on site** during each scenario.

**Branch map:** `erp-bcp` (Q1 = Continuity request → route to `business-continuity-plan`;
**mandatory** disambiguation); `scenario` (Q2 selection → Q2a + `KB-SNIP-ERP-SCENARIOS`
per-scenario stub); `india-state` (Q5 = India → Q5a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q6b, and Q5a if the India branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Producing an ERP for: Plant 4 solvent-storage warehouse (45 staff, 2 shifts); scenarios
fire/explosion + chemical release; trained ERT; muster point = north car park; UK
(RRFSO art.15); drills quarterly — correct?"

## Refuse-on-vague anchors

- Q1 is the specificity anchor — refuse a vague/generic site ("write me an emergency
  plan"); require the **named site + occupancy**. A request for continuity of critical
  activities is **routed to `business-continuity-plan`**, not answered here.
- **No plan is produced** until the named site **+ ≥1 credible scenario (Q2) + muster /
  evacuation arrangements (Q4)** are all captured. A generic "evacuate" procedure with no
  scenario-keyed steps is explicitly refused.
- Q3 capability that the plan relies on must be **stated and proven**, not assumed.

## Domain evidence types (ELI-EVIDENCE)

Prior ERP / evacuation plan · drill records & debriefs · site layout / muster-point map ·
SDS / inventory for flammable or toxic stock named in Q2 · mutual-aid agreements ·
incident/near-miss history for the site · the local fire/ambulance service interface notes.
