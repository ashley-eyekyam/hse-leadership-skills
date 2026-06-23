---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A racking + MHE safety assessment classifies the CURRENT installation against the EN 15635 inspection regime and the SEMA RAG bands afresh from the supplied damage findings and SWL load notices (Q2/Q4); there is no prior quantitative baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the displayed SWL, the inspection cadence, and the current damage findings are the assessment's starting facts."
    ELI-SCORING: "The SEMA RAG band is a damage/severity CLASSIFICATION applied by the inspector (Green/Amber/Red), not a qualitative scoring scale the user picks; the residual is re-scored on the deterministic risk_matrix 5x5 engine after controls — so a user-facing scoring-scale question is not asked. The SEMA band drives the remedial action (Red=immediate off-load), not a numeric score."
  branches:
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-MTW, mandatory: true}
---

# Structured intake — warehouse-racking-mhe-safety

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where the
answer space is enumerable and free-text where it is open; branch on the answers; **echo the captured
facts back for confirmation before any analysis**. The intake opens with the **named warehouse /
installation (Q1 — the specificity anchor)**, then the **racking configuration & SWL (Q2 — the
integrity-of-advice gate)**, the **inspection regime & PRRS (Q3)**, the **damage findings & SEMA RAG
band (Q4 — the remedial-action gate)**, the **MHE & pedestrian traffic layout (Q5 — the core-value
control gate)**, the **jurisdiction (Q6)**, and the output/owner/review questions. **Refuse to "make
our warehouse safe": you need the named site/installation (Q1), the racking configuration + SWL (Q2),
and the traffic layout (Q5) before any analysis. Refuse a "just brief everyone to be careful / wear
hi-vis" treatment as the headline control.** A site-specific SWL, tolerance, inspection interval, or
bay configuration is **never** assumed — a missing value is a `[GAP]`, never an invented rating, and a
SEMA **Red** finding is **never** down-rated to "monitor".

One load-bearing branch: the **mandatory India→state branch** (Q6 = India → Q6a + `hse-india`; confirm
the state before citing any rule — never a national form number, emit `[GAP]` where a state return is
owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named warehouse / installation** (the site + the racking installation + what it stores) | free-text | "Name the exact site + racking installation + what it stores (e.g. 'Coventry DC, 8 m APR pallet racking, chilled ambient, bays A1–A48'). **Refuse 'a warehouse' / 'the DC' — the assessment is site- and installation-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Racking configuration & SWL** (the integrity-of-advice gate) | free-text | "The rack type (APR / drive-in / cantilever / mobile), the bay/beam configuration, and the **displayed SWL load notices**. **A site-specific SWL, tolerance, or bay configuration is NEVER assumed — if not supplied, record a literal `[GAP]` and request the SWL load notice / rack-design drawing; never invent an SWL rating.**" | ELI-EXPOSURE | always |
| Q3 | **Inspection regime & PRRS** (the EN 15635 regime) | mcq+free-text | "Is a **PRRS** (Person Responsible for Racking Safety) named? Inspection cadence — weekly visual / ≥12-monthly expert / 6-monthly (high-traffic) / unknown. **An unappointed PRRS or an absent ≥12-monthly expert inspection is a high-priority finding.**" | ELI-OBLIGATIONS | always |
| Q4 | **Damage findings & SEMA RAG band** (the remedial-action gate) | free-text | "What rack damage is present, and its SEMA RAG classification (Green / Amber / Red)? **A Red-band finding triggers an IMMEDIATE off-load + isolate action — it is NEVER down-rated to 'monitor'; Amber repairs within 4 weeks and auto-escalates to Red. Damage at an unstated tolerance is a `[GAP]`.**" | ELI-EVIDENCE | always |
| Q5 | **MHE & pedestrian traffic layout** (the core-value control gate) | mcq+free-text | "The MHE inventory (forklift / reach / VNA / PPT) and the **traffic layout**: are vehicles and pedestrians **engineered apart** (barriers, one-way systems, marked/protected walkways/crossings)? **A treatment that treats MHE/pedestrian conflict with hi-vis / signage / 'look out for forklifts' alone — no engineered segregation — is a FLAG pushed up the hierarchy, never the headline control.**" | ELI-OBLIGATIONS | always |
| Q6 | **Jurisdiction** (selects the duty map) | mcq | UK / USA / EU / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / setting | mcq+free-text | Distribution / 3PL warehouse / Cold store / Manufacturing store / Retail back-of-house / Mixed (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / area / bays in scope | free-text | "Which specific area / aisles / bays / marshalling zone is in scope?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full racking + traffic safety report (consultant) / racking inspection regime + PRRS pack (manager) / the SEMA RAG remedial fix-list (warehouse lead) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the SWL-correction / inspection-regime / segregation / [GAP]-closure actions, and who is the competent person reviewing the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-damage-report / on-reconfiguration / quarterly (or sooner for high-traffic / 24-7 sites) / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q6 = India → Q6a + `hse-india`; **mandatory** — confirm the state before
citing any rule; emit `[GAP]`, never a national form number).

## Echo-back

After the last applicable question (Q11, and Q6a if its branch ran), **echo a captured-facts summary**
and confirm before any analysis:
"Assessing warehouse racking + MHE safety for: Coventry DC, 8 m APR pallet racking, bays A1–A48, UK
(EN 15635 / SEMA + PUWER/L117); SWL load notices supplied for bays A1–A24, NOT supplied for A25–A48 →
[GAP]; PRRS named, weekly visual in place, no ≥12-monthly expert inspection (high-priority finding);
two Red-band frame buckles on bays A12 and A18 → immediate off-load + isolate; MHE/pedestrian
controlled by hi-vis only with no engineered segregation in goods-in → FLAG, pushed up to barriers +
one-way routing; full racking + traffic safety report; review on damage report — correct?" The SEMA RAG
band drives the remedial action; the residual is then re-scored on the risk_matrix engine.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a warehouse" / "the DC"; ask again or record `[GAP]`,
  never invent the site or its racking installation.
- **SWL/design + inspection + engineered segregation first, hi-vis last** — a treatment whose headline
  is "inspect carefully" / hi-vis / "look out for forklifts" is **refused and pushed up the
  hierarchy**; racking is led by SWL-rated configuration + column protection + the EN 15635 inspection
  regime, and MHE/pedestrian conflict by engineered segregation (barriers, one-way systems, marked
  walkways); hi-vis/signage are residual only.
- **No invented SWL / tolerance / interval** — a missing SWL (Q2), inspection interval (Q3), or a
  damage tolerance (Q4) is a `[GAP]` and a request for the SWL load notice / rack-design drawing; the
  skill **never** invents an SWL rating or a tolerance.
- **A SEMA Red finding is never down-rated** — a Red-band damage finding ALWAYS carries an immediate
  off-load + isolate action; it is never recorded as "monitor". **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The displayed SWL load notices + the rack-design drawing (Q2 — the integrity-of-advice anchor; else a
`[GAP]`) · the bay/beam configuration and rack type (Q2) · the PRRS appointment + the EN 15635
inspection cadence (Q3 — weekly visual / ≥12-monthly expert) · the damage findings + their SEMA RAG
band (Q4 — Green/Amber/Red with the matching action) · the MHE inventory + the traffic layout (Q5 —
engineered segregation vs hi-vis-led) · the jurisdiction duty map (Q6 — OSHA 1910.178 / PUWER+L117 /
India MTW via `hse-india`) · any prior struck-by / rack-collapse incident note (de-identified to role
label, `<5` small cells suppressed — special-category occupational-health data, lower-tier but never
circulated with a name).
