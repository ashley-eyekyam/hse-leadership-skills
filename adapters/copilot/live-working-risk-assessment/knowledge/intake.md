---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A live-working assessment is built afresh for a defined energized task from the named task, the live conductors, and the operating voltage (Q1); there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the de-energization evaluation and the statutory justification are the assessment's starting facts."
    ELI-SCORING: "The live-working decision is governed by the statutory three-part test (unreasonable-to-be-dead + reasonable-to-work-live + suitable-precautions) and the de-energize-first hierarchy, not chosen on a qualitative scoring scale; risk_matrix is used only for a qualitative residual framing, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: "no or partly", activates_questions: [Q3], activates_kb_row: KB-SNIP-LIVE-WORK-JUSTIFICATION, mandatory: true}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-ELECTRICAL, mandatory: true}
---

# Structured intake — live-working-risk-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named task & live conductors (Q1 — the specificity anchor)**, then the **can-it-be-done-dead
gate (Q2 — the gate the whole skill turns on)**, the **live-working justification (Q3 — only if
Q2 ≠ yes; the spine of the artifact)**, the **approach distances & precautions (Q4)**, the
**energized-work permit (Q5)**, and the **jurisdiction (Q6)**. **Refuse to assess "work near the
live parts": you need the named task (Q1), the live conductors, and the operating voltage before any
drafting. The assessment does not proceed past Q2 unless de-energization has been genuinely
evaluated; if live work is proposed, a statutory justification (Q3) is mandatory — and a
justification of mere convenience is REFUSED.** A missing required input is a `[GAP]`, never an
invented approach boundary, justification, or arc-flash figure.

Two load-bearing branches: the **mandatory live-working-justification branch** (Q2 = no/partly → Q3
+ `KB-SNIP-LIVE-WORK-JUSTIFICATION`; the three-part EAWR reg 14 / OSHA 1910.333(a)(2) test —
convenience is refused) and the **mandatory India→state branch** (Q6 = India → Q6a + `hse-india`;
confirm the state before citing any rule — never a national form number, emit `[GAP]` where a state
return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named task & live conductors** (the task + the live conductors/apparatus + the operating voltage) | free-text | "Name the exact task + the live conductors/apparatus + the operating voltage (e.g. 'thermographic survey on the energized LV switchboard SB-2, 400 V'). **Refuse 'work near the live parts' / 'a panel' — the assessment is task- and conductor-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Can the task be done dead?** (the gate the whole skill turns on — asked first among the controls because de-energization is the primary control; "yes" → recommend de-energization + an ESWC and do NOT assess live work further (the default); "no or partly" → branch to Q3) | mcq | yes / no or partly | ELI-SCOPE | always |
| Q3 | *(only if Q2 ≠ yes)* **Live-working justification** (the spine of the artifact) | free-text | "Justify against the statutory three-part test: **EAWR reg 14** — (a) it is *unreasonable to be dead* + (b) it is *reasonable to work live* + (c) *suitable precautions* are taken — **or** OSHA **1910.333(a)(2)** ('additional/increased hazard or infeasible'). **A bare 'production cannot stop / it's quicker' is REFUSED** — economic convenience alone does not justify live work. Record verbatim; route to an energized-work permit." | ELI-OBLIGATIONS | Q2 != yes |
| Q4 | **Approach distances & precautions** (the arc-flash incident energy is cross-referenced from #1, never recomputed) | free-text | "The working distance vs the **limited and restricted approach boundaries** (NFPA 70E 130.4 / 1910.269); insulation / barriers / insulated tools; the qualified-person & accompaniment requirement; and the **arc-flash incident energy + PPE category at the working position — cross-referenced from `arc-flash-assessment` (#1)**, never recomputed here. Arc-rated PPE is recorded as the **last** precaution." | ELI-EXPOSURE | always |
| Q5 | **Energized-work permit** (the NFPA 70E Annex J permit content) | mcq | live work authorised → generate the energized-work permit (Annex J content) with the justification, precautions, approach boundaries, PPE, and authorising signature / not authorised → recommend dead working (ESWC) | ELI-EVIDENCE | always |
| Q6 | **Jurisdiction** | mcq | USA / UK / EU / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Generation / Transmission-Distribution / Industrial-Commercial / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / substation / switchroom is the live work in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full live-working risk assessment + energized-work permit (consultant) / live-work justification + approach-boundary register (manager) / quick energized-work permit (frontline) | ELI-OUTPUT | always |
| Q10 | **Live-work authority + verifier** | free-text | "Who is the competent person authorising the live work and who is the competent person verifying the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | per-live-work-operation / on-equipment-change / on-procedure-change / annual / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `live-work-justification` (Q2 = no/partly → Q3 + `KB-SNIP-LIVE-WORK-JUSTIFICATION`;
EAWR reg 14 / OSHA 1910.333(a)(2); convenience refused; **mandatory** for any live-work path);
`india-state` (Q6 = India → Q6a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q3 / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing live work for: thermographic survey on the energized LV switchboard SB-2, 400 V,
Substation 2, Maharashtra; CAN it be done dead? — no (continuous-monitoring survey, de-energizing
defeats the purpose → EAWR reg 14 justification recorded); limited/restricted approach boundaries
defined; arc-flash incident energy + PPE category cross-referenced from arc-flash-assessment;
energized-work permit (Annex J) generated; full live-working risk assessment; review per live-work
operation — correct?" The de-energization evaluation is recorded FIRST; if live work is proposed the
three-part statutory gate is applied before any approach/permit work.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "work near the live parts" / "a panel"; ask again or
  record `[GAP]`, never invent the task, the conductors, or the voltage.
- **No live-working assessment past Q2 without a genuine de-energization evaluation** — and if live
  work is proposed, the statutory three-part test (Q3) is **mandatory**; a justification of mere
  convenience ("production cannot stop / it's quicker") is **REFUSED** — EAWR reg 14 and OSHA
  1910.333 do not permit live work for production speed alone.
- **Never "wear the flash suit" as the assessment** — a plan whose only control is arc-rated PPE with
  no de-energization evaluation is a **FLAG pushed up the hierarchy**; PPE is the residual-hazard last
  line. The arc-flash incident energy is **cross-referenced from #1, never invented**. A missing input
  is a `[GAP]`. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The de-energization evaluation (Q2) and any live-working justification (Q3 — EAWR reg 14 / OSHA
1910.333(a)(2)) · the limited/restricted approach boundaries per task (Q4 — NFPA 70E 130.4 /
1910.269) · the arc-flash incident energy + PPE category at the working position
(cross-referenced from `arc-flash-assessment` #1, never recomputed) · the energized-work-permit
content — Annex J (Q5) · the operating voltage and the authorisation level (Q1/Q10) · a prior
contact / electrocution / arc-flash burn incident referenced for context (de-identified to role
label — injury/health detail is highest-sensitivity).
