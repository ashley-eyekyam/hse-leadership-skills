---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-JURIS: "ISO 22301 is a jurisdiction-independent management-system standard with no national forms; recovery objectives derive from the org's own BIA, not from any state law. Jurisdiction is captured as optional context in Q5b (statutory continuity duties, e.g. India Factories Act s.41B) — never as a form-routing branch — so no mandatory jurisdiction question is required."
  branches:
    - {when: Q3, option: Loss of key supplier, activates_questions: [Q5], activates_kb_row: KB-DATA-RTO-RPO-GUIDANCE, mandatory: false}
---

# Structured intake — business-continuity-plan

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the answers;
**echo the captured facts back for confirmation before any analysis**. The intake opens with
the **scope gate + BCP-vs-ERP disambiguation (Q1)**, then runs the BIA-driving questions.
**Refuse to proceed on a vague scope (Q1) or before the critical activities + dependencies
are captured (Q2/Q5)** — ask again, or record `[ASSUMPTION]` / `[GAP]`; never invent a
recovery time.

**Load-bearing disambiguation (D-07, mandatory):** at Q1, if the user actually wants the
**immediate incident response** — muster, evacuation, scenario response procedures, the
call-out tree, emergency drills — that is **`emergency-response-plan`** (ERP), not this
skill; **route there and stop**. This skill owns the *continuity* leg: critical activities,
RTO/RPO/MTPD, dependencies, recovery strategies, recovery roles. The two are adjacent and
cross-referenced, never merged (`KB-SNIP-OPS-CLAUSE-MAP`).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Scope + BCP-vs-ERP gate** (the specificity anchor) | free-text | "Which **named organisation / site / function** does this BCP cover? — **first**: if you actually want the immediate incident response (muster / evacuation / scenario procedures / call-out tree / drills), that is `emergency-response-plan`, not this skill. This skill covers **continuity of critical activities** (critical activities / RTO / RPO / MTPD / recovery). **Refuse a generic scope** ('the whole company')." | ELI-SCOPE | always |
| Q1b | Industry / sector | MCQ + free-text | Finance / Manufacturing / Healthcare / Utilities / Logistics / Public-sector / General-Other (+ detail) — sets the impact-over-time lens | ELI-INDUSTRY | always |
| Q1c | Site / location of the function | free-text | "Which specific site/premises/data-centre does this function run from? (a premises dependency)" | ELI-LOCATION | always |
| Q2 | **Critical activities + their outputs** (drives the BIA) | free-text | "List the **time-critical activities** and what each must keep producing (e.g. 'claims processing -> settled claims'). **Refuse to set any recovery objective until these are captured.**" | ELI-SUBJECT | always |
| Q3 | Disruption scenarios | MCQ multi-select | Loss of site / Loss of IT / Loss of key supplier / Loss of key staff / Utility failure — branch per scenario | ELI-EXPOSURE | always |
| Q4 | Current recovery capability | MCQ | None / Informal / Documented-DR / Tested-BCP — seeds the maturity baseline | ELI-BASELINE | always |
| Q4b | **Evidence held** | free-text | "Prior BIA / DR runbooks, dependency maps, supplier contracts/SLAs, backup logs (for RPO), or past exercise reports? (or 'none' -> I'll flag `[GAP]`)" | ELI-EVIDENCE | always |
| Q5 | **Objectives basis + dependencies** | free-text | "Any known MTPD/RTO/RPO per activity, **and the dependencies** (people / IT-systems / suppliers / premises / equipment) for each. **RTO must be derived under a stated MTPD — never asserted alone.**" | ELI-SCORING | always |
| Q5b | Statutory continuity obligations *(optional context)* | free-text | "Any statutory continuity/emergency-plan duty for your jurisdiction (e.g. India Factories Act s.41B on-site emergency plan for MAH installations, sector regulator resilience rules)? (or 'none')" | ELI-OBLIGATIONS | always |
| Q6 | **Recovery-role owners + deputies** | free-text | "Who owns each recovery role, and who is the **deputy** for each? (named role/person — no 'TBD'; every recovery role needs a deputy)" | ELI-COMPETENCY | always |
| Q6b | Output artifact + reader | MCQ | Full BCP (board/exec) / BIA + objectives only (consultant) / Activation card (operational) | ELI-OUTPUT | always |
| Q6c | **Exercise cadence + next review** | MCQ + free-text | Annual / On change / Other (+date) — feeds the exercise/test schedule + review block | ELI-TEMPORAL | always |

**Branch map:** `bcp-vs-erp` (Q1 = an incident-response request -> route to
`emergency-response-plan` and stop; the **mandatory disambiguation** described above,
`KB-SNIP-OPS-CLAUSE-MAP`); `supplier-dependency` (Q3 = Loss of key supplier -> Q5 must
capture the supplier dependency so the strategy covers it; non-mandatory,
`KB-DATA-RTO-RPO-GUIDANCE`).

## Echo-back

After the last applicable question (Q6c), **echo a captured-facts summary** and confirm
before any analysis: "Building a BCP for: {function} at {site}, critical activities {...},
scenarios {...}, MTPD/RTO/RPO basis {...}, recovery roles {...} with deputies — correct?"
Then run the BIA method.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse a generic scope ("write me a continuity plan",
  "the whole company"); never proceed on a vague subject.
- **No recovery objective is set until Q2's named critical activities + Q5's dependencies are
  captured**; an RTO with no stated MTPD basis, or RTO >= MTPD, is **invalid** — refuse it,
  record `[GAP]`, never invent a recovery time.

## Domain evidence types (ELI-EVIDENCE)

Prior BIA / DR/continuity runbooks / dependency maps / supplier contracts-SLAs (for
single-supplier dependencies) / backup logs (for the RPO) / past exercise-test reports.
