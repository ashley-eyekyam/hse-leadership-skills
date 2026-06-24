---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A switching program is built afresh for a defined work activity from the named apparatus, the operating voltage, and the points of isolation/earthing (Q1/Q2/Q3); there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the de-energization/isolation decision and the enumerated points of isolation are the program's starting facts."
    ELI-SCORING: "The switching program is governed by the ordered isolate → prove-dead → earth → sanction → restore sequence and the safety-document control, not chosen on a qualitative scoring scale; risk_matrix is used only for a qualitative residual framing, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q5, option: "live work", activates_questions: [Q5a], activates_kb_row: KB-SNIP-DEENERGIZE-FIRST, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-ELECTRICAL, mandatory: true}
---

# Structured intake — electrical-permit-switching-program

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named apparatus (Q1 — the specificity anchor)**, then the **operating voltage & system (Q2)**,
the **points of isolation & earthing (Q3 — the program backbone)**, the **work activity & document
type (Q4)**, the **de-energization decision (Q5)**, and the **jurisdiction (Q6)**. **Refuse to
author a program for "the substation": you need the named apparatus (Q1), the operating voltage
(Q2), and the points of isolation/earthing (Q3) before any drafting. Refuse a program that would
authorise work without prove-dead and (where required) protective earthing.** The ordered switching
sequence is **never** narrated loosely — it is built per `KB-SNIP-SWITCHING-SEQUENCE`, and a missing
required input is a `[GAP]`, never an invented isolation point.

Two load-bearing branches: the **live-work-justification branch** (Q5 = live work proposed → Q5a,
against OSHA 1910.333 / EAWR — a bare convenience reason is refused; non-mandatory) and the
**mandatory India→state branch** (Q6 = India → Q6a + `hse-india`; confirm the state before citing
any rule — never a national form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named apparatus** (the feeder / busbar section / transformer / RMU / switchboard + operating voltage + function) | free-text | "Name the exact apparatus + type + operating voltage + function (e.g. '11 kV feeder F2 to RMU-3, ring main'). **Refuse 'the substation' / 'the switchroom' — the program is apparatus-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Operating voltage & system** (drives approach distances, the earthing requirement, and the authorisation level) | mcq | LV (≤1 kV) / HV 11 kV / HV 33 kV / HV other / mixed | ELI-SCOPE | always |
| Q3 | **Points of isolation & earthing** (the program backbone) | free-text | "List every point of supply / isolation for this apparatus and where protective earthing will be applied. **A program that cannot enumerate its points of isolation is refused; working un-earthed where the procedure requires earthing is a flagged failure.**" | ELI-EXPOSURE | always |
| Q4 | **Work activity & safety-document type** (the sanction-to-test is kept DISTINCT from a permit-to-work) | mcq | work on dead equipment (permit-to-work) / controlled re-energization for testing (sanction-to-test) / both | ELI-OBLIGATIONS | always |
| Q5 | **De-energization decision** (asked among the controls — de-energization + isolation is the primary control; work dead is the default; live work branches to Q5a) | mcq | work dead / live work | ELI-EVIDENCE | always |
| Q5a | *(live work only)* **Live-work justification** | free-text | "Justify against OSHA 1910.333(a)(2) ('additional/increased hazard or infeasible') **or** EAWR ('unreasonable to be dead'). **A bare 'it's quicker / production needs it' is REFUSED** — economic convenience alone does not justify live work. Record verbatim; route to the appropriate live-work control." | ELI-OBLIGATIONS | Q5 == live work |
| Q6 | **Jurisdiction** | mcq | USA / UK / EU / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Generation / Transmission-Distribution / Industrial-Commercial / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / substation / switchroom is the apparatus in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full switching program + safety-document plan (consultant) / switching schedule + isolation/earthing register (manager) / quick ordered switching steps (frontline) | ELI-OUTPUT | always |
| Q10 | **Switching authority + verifier** | free-text | "Who is the authorised / senior authorised person carrying out the switching and who is the competent person verifying the program (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | per-switching-operation / on-network-change / on-procedure-change / annual / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `live-work-justification` (Q5 = live work → Q5a + `KB-SNIP-DEENERGIZE-FIRST`;
OSHA 1910.333 / EAWR; convenience refused; non-mandatory); `india-state` (Q6 = India → Q6a +
`hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q5a / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Building a switching program for: 11 kV feeder F2 to RMU-3, ring main, Substation 2, Maharashtra;
HV 11 kV; points of isolation at the feeder CB and the RMU incomer, protective earthing at the work
point; work on dead equipment → permit-to-work; worked DEAD → ESWC scoped (Article 120); full
switching program; review per switching operation — correct?" The ordered switching sequence
(isolate → prove dead → earth → sanction → restore) is then built per `KB-SNIP-SWITCHING-SEQUENCE`,
with per-step authorisation.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "the substation" / "the switchroom"; ask again or record
  `[GAP]`, never invent the apparatus or its rating.
- **No program without prove-dead and earthing** — a sequence that would authorise work on apparatus
  isolated but not proven dead, or that omits protective earthing where the procedure requires it, is
  **refused and pushed up the hierarchy**; the safety document is issued only after the apparatus is
  in a proven safe working condition.
- **Sanction-to-test ≠ permit-to-work** — controlled re-energization for testing is never issued as a
  work-on-dead permit. A missing input is a `[GAP]`. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The de-energization / isolation decision (Q5) and any live-work justification (Q5a — OSHA 1910.333 /
EAWR) · the points of isolation and the protective-earthing requirement per apparatus (Q3) · the
safety-document type — permit-to-work vs sanction-to-test (Q4) · the operating voltage and the
authorisation level (Q2/Q10) · the ordered switching sequence per `KB-SNIP-SWITCHING-SEQUENCE` · a
prior switching / electrocution incident referenced for context (de-identified to role label —
injury/health detail is highest-sensitivity).
