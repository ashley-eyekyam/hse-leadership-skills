---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-EXPOSURE, ELI-BASELINE,
           ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "BBS is a participation method (ISO 45001 clause 5.4) applied identically across sectors; the target behaviours change with the task but the method (ABC, non-punitive cards, system-fix routing, percent-safe/participation metrics) does not branch on industry. Sector is captured as free-text context in Q1, never a branch. The skill is industry: [All]."
    ELI-LOCATION: "The unit of design is a site/crew/operation (a participation population), captured as free-text context within Q1; there is no location-specific hazard set the way a confined-space RA has, and the observable behaviours are tied to the named task/area in Q2/Q3 rather than to a distinct location dimension. No separate location branch is needed."
    ELI-SCORING: "A BBS program has no likelihood×severity risk matrix; its quantitative outputs are the defined behavioural metrics (percent-safe, participation, trend-by-category from KB-DATA-BBS-METRICS), captured in Q5, not a scoring scale. At-risk-behaviour fixes are ranked deterministically by the controls engine (hierarchy of controls), not a numeric score chosen at intake."
  branches:
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — bbs-program-designer

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. This
skill **designs a non-punitive BBS program** (ABC analysis, an observable observation
card, defined metrics, at-risk behaviours trended to systemic causes) — it does **not**
record nameable individuals, and it never frames the worker as the problem.

**Two hard refuse-on-vague anchors:** **Q1** (a named site / crew / operation — and the
sibling-disambiguation gate) and **Q3** (the card behaviours must be **observable and
site-specific** — refuse "work safely"). The **mandatory India→state branch** (Q6 =
India → Q6a) resolves the state before citing any obligation and never mints a national
form number.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Program scope** (named site / crew / operation) + sibling check | free-text + MCQ | "Which specific site, crew, or operation is the BBS program for? (e.g. 'order-picking crew, Leeds DC')." **Then confirm you want a BBS observation program** — if you actually want a culture-maturity assessment (`safety-culture-assessment`), a leadership gemba walk (`safety-walk-gemba`), or a leading/lagging KPI framework (`leading-lagging-kpi-framework`), route there instead. **Refuse a vague "improve our safety culture" with no named unit.** | ELI-SUBJECT | always |
| Q2 | **Target behaviours / focus areas** | MCQ multi-select + free-text | The tasks/areas the program will observe (e.g. manual handling, line-of-fire, working at height, PPE-in-use, housekeeping, mobile-plant interaction) — branch a card section per selected area | ELI-SCOPE | always |
| Q3 | **Card item phrasing** (the observability gate) | free-text | "State each card item as an **observable, site-specific** behaviour tied to a named task/area (e.g. 'three points of contact climbing the rack ladder'). **Refuse 'work safely' / 'be careful'** — these cannot be observed or counted." — **the specificity anchor; refuse a non-observable item** | ELI-EVIDENCE | always |
| Q4 | **Existing data / baseline** | free-text | "Any existing observation cards, participation logs, or incident/near-miss data to design from? (de-identified — role/group labels only, never named individuals)" (seeds the baseline) | ELI-BASELINE | always |
| Q4b | **Observer pool & participation** | MCQ + free-text | Who observes (peers / supervisors / mixed), the **trained pool size**, and that participation is **voluntary** — role/group labels only | ELI-EXPOSURE | always |
| Q5 | **Metrics to track** | MCQ multi-select | Percent-safe / Participation rate / Trend-by-behaviour-category (default: all three; `KB-DATA-BBS-METRICS`) — **`<5` small-cell suppression applies to any team breakdown** | ELI-OBLIGATIONS | always |
| Q6 | **Jurisdiction** (worker-consultation duty) | MCQ | UK / USA / EU / India / Other / Unknown (India → Q6a) | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`; never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | **Output artifact + reader** | MCQ | Full BBS program design (consultant) / Management roll-out summary (leadership) / Card + metrics pack only — and its audience (M / C / E) | ELI-OUTPUT | always |
| Q8 | **Program owner + action owners** | free-text | "Who owns the BBS program (role), and who will own the system-fix actions for trended at-risk categories? (named **role**, no 'TBD')" | ELI-COMPETENCY | always |
| Q9 | **Review cycle / next review** | MCQ + free-text | Monthly metric review / Quarterly card review / On change (MoC) / Other (+date) | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q6 = India → Q6a; **mandatory**). Behaviour branches (Q2)
activate a card section per selected task/area.

## Echo-back

After the last applicable question (Q9, and Q6a if the India branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Designing: a non-punitive BBS observation program for the order-picking crew (Leeds DC),
target behaviours = manual handling + line-of-fire + housekeeping, cards observable and
role-labelled, metrics = percent-safe + participation + trend-by-category (with `<5`
suppression), voluntary peer observers, UK, review monthly — correct?" Confirm the card
items are **observable** before any drafting.

## Refuse-on-vague anchors

- **Q1 is the specificity + routing anchor** — refuse "improve our safety culture" with
  no named unit; require a named site/crew/operation, and route to the correct sibling
  (`safety-culture-assessment` / `safety-walk-gemba` /
  `leading-lagging-kpi-framework`) if the user does not actually want a BBS program.
  Record `[ASSUMPTION]` / `[GAP]`, never invent a unit.
- **Q3 is the observability gate** — **refuse a non-observable card item ("work safely",
  "be careful").** Require an observable, site-specific behaviour tied to a named
  task/area; if the user offers a slogan, flag `[GAP]` and elicit the observable
  behaviour before building the card.
- **Never record a nameable individual on a card** — observation data is role-labelled
  or anonymous, voluntary, and used for trending and learning, **never** individual
  discipline.

## Evidence types (ELI-EVIDENCE)

Existing observation cards (de-identified) · participation logs (role/group counts) ·
near-miss / incident patterns by task (aggregated) · the trained-observer pool. All are
handled under `references/deid-checklist.md` (role/group labels, `<5` suppression, no
individual named) before any analysis.
