---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A driver-fatigue assessment computes the hours-of-service compliance flags from the supplied duty log (Q3) afresh per shift; there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the duty log and the computed HOS flags are the assessment's starting facts."
    ELI-SCORING: "The HOS result is COMPUTED by the deterministic fatigue.py engine (per-rule PASS/FAIL compliance flags), not chosen on a qualitative scoring scale; the fatigue index is a clearly-flagged advisory metric the engine derives, and risk_matrix is used only for a qualitative residual framing — so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: India, activates_questions: [Q2a], activates_kb_row: KB-REG-IN-MTW, mandatory: true}
---

# Structured intake — driver-fatigue-management

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named fleet / operation (Q1 — the specificity anchor)**, then the **jurisdiction & rule-set
(Q2)** (which selects the HOS rules), the **driver duty log (Q3 — the computation input)**, the
**multi-day cycle & cross-shift rest (Q4 — the `[GAP]` discipline)**, the **proposed controls
(Q5 — the core-value gate)**, and the output/owner/review questions. **Refuse to "manage our
fatigue": you need the named fleet/operation (Q1), the jurisdiction (Q2), and the driver duty log
(Q3) before any analysis. Refuse a "just run a stay-alert toolbox talk" / "fit in-cab alertness
alarms" treatment as the headline control.** The HOS compliance flags are **never** narrated —
they are computed by the `fatigue.py` engine, and a missing duty-log segment / cycle figure /
cross-shift rest is a `[GAP]`, never an invented value.

One load-bearing branch: the **mandatory India→state branch** (Q2 = India → Q2a + `hse-india`;
confirm the state before citing any rule — never a national form number, emit `[GAP]` where a state
return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named fleet / operation** (the fleet / route / depot / operation + function) | free-text | "Name the exact fleet / route / depot / operation + function (e.g. 'night-trunk fleet, route R-204, Midlands depot'). **Refuse 'our drivers' / 'the fleet' — the assessment is operation-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Jurisdiction & rule-set** (selects the HOS rules) | mcq | USA (FMCSA 49 CFR 395) / EU (Reg 561/2006) / UK (GB drivers' hours — read with EU 561) / India / Other / Unknown | ELI-JURIS | always |
| Q2a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q2 == India |
| Q3 | **The driver duty log** (the IEEE-of-this-skill computation input) | free-text | "Give the shift as an ordered list of `{status, hours}` segments (`status` ∈ driving / on_duty / off_duty / sleeper; `hours` a float), or attach the ELD / tachograph download. **Refuse to compute on a missing or vague log → record a `[GAP]` and request the ELD/tachograph download; never invent driving hours, a rest segment, or a duty figure.**" | ELI-EXPOSURE | always |
| Q4 | **Multi-day cycle & cross-shift rest** (the `[GAP]` discipline) | free-text | "The 7-/8-day cumulative on-duty figure (for the FMCSA 60/70 h cycle + 34 h restart) and the cross-shift daily rest. **A single-shift log cannot evidence the multi-day cycle or the cross-shift rest — if not supplied, record a literal `[GAP]`; NEVER assert the cycle/restart compliant from one shift.**" | ELI-EVIDENCE | always |
| Q5 | **Proposed controls** (the core-value gate) | free-text | "What fatigue controls are proposed? **A 'stay alert' briefing / driver-alertness training / an in-cab fatigue-detection gadget as the HEADLINE control is a FLAG pushed up the hierarchy** — fatigue is led by roster / journey-plan / built-in-rest (FRMS) redesign; alertness measures are at most administrative / engineering backstops." | ELI-OBLIGATIONS | always |
| Q6 | Industry / setting | mcq+free-text | Road haulage / Last-mile & distribution / Passenger transport / Mixed-fleet (+ detail) | ELI-INDUSTRY | always |
| Q7 | Location / depot / operating area | free-text | "Which specific depot / operating area / route network is this?" | ELI-LOCATION | always |
| Q8 | Output artifact wanted + its reader | mcq | full fatigue-risk-management report (consultant) / HOS-compliance + FRMS summary (manager) / the roster fix-list (planner) | ELI-OUTPUT | always |
| Q9 | **Action owner(s) + verifier** | free-text | "Who owns the roster-redesign / FRMS / [GAP]-closure actions and who is the competent person reviewing the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q10 | **Review cycle / next review** | mcq+free-text | on-roster-change / on-ELD-exception / quarterly (or sooner) / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q2 = India → Q2a + `hse-india`; **mandatory** — confirm the state
before citing any rule; emit `[GAP]`, never a national form number).

## Echo-back

After the last applicable question (Q10, and Q2a if its branch ran), **echo a captured-facts
summary** and confirm before any analysis:
"Assessing driver fatigue for: night-trunk fleet, route R-204, Midlands depot, UK (EU 561 rule-set);
duty log = 4.5 h drive / 45-min break / 4.0 h drive / 1.0 h on-duty / 11 h off-duty; 7-day cumulative
on-duty figure NOT supplied → [GAP]; proposed controls led by roster redesign (relay split) with
in-cab detection as a backstop; full fatigue-risk-management report; review on roster change —
correct?" The HOS compliance flags are then computed by the `fatigue.py` engine, never narrated.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "our drivers" / "the fleet"; ask again or record
  `[GAP]`, never invent the operation or its routes.
- **Roster redesign first, alertness last** — a treatment whose headline is "stay alert" /
  driver-alertness training / an in-cab fatigue-detection gadget is **refused and pushed up the
  hierarchy**; fatigue is led by roster / journey-plan / built-in-rest (FRMS) redesign, and
  alertness measures are at most administrative / engineering backstops.
- **No invented hours or multi-day claims** — a missing duty-log segment (Q3) or an unsupplied
  multi-day cycle / cross-shift rest figure (Q4) is a `[GAP]` and a request for the ELD/tachograph
  download or the cumulative figure; the skill **never** invents a driving hour, a rest segment, or
  asserts the cycle/restart compliant from a single shift. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The driver duty log (Q3 — the ordered `{status, hours}` segments / ELD / tachograph download) · the
jurisdiction & rule-set (Q2 — FMCSA 49 CFR 395 / EU 561/2006 / India MTW via `hse-india`) · the
7-/8-day cumulative on-duty figure + cross-shift daily rest (Q4 — for the multi-day cycle / restart /
daily-rest rules, else a `[GAP]`) · the computed HOS compliance flags + the advisory fatigue index
from `fatigue.py` (not narrated) · the proposed controls (Q5 — roster/FRMS-led, alertness-led
flagged) · any driver medical-fitness / OSA / sleep-disorder note and fatigue-event / sickness-absence
count (de-identified to role label, `<5` small cells suppressed — highest-sensitivity
occupational-health data).
