---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-SCORING: "Not applicable — noise exposure is a transcribed measured value compared to a cited threshold; there is NO scoring tool (no dosimetry computed, D-08a)."
  branches:
    - {when: Q1, option: none-yet, activates_questions: [Q1a], mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — noise-exposure-health-surveillance

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo the
captured facts back for confirmation before any analysis**. The intake opens with the
**exposure-data basis (Q1)** — the gate that decides whether a surveillance plan can be set at
all — then captures the **named area + SEG (Q2, the specificity anchor)**, the **exposure levels
(Q3)**, the noise sources, the existing controls, and the jurisdiction.

**Refuse to set an audiometry / surveillance schedule until an exposure basis (Q1), a named
area/SEG (Q2), and ≥ an estimated TWA (Q3) are captured** — ask again, or record `[ASSUMPTION]`
/ `[GAP]`; **never invent a dB figure**. On Q1 = *none yet*, recommend a **measurement strategy
first** and set **no surveillance plan** until an exposure basis exists.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Exposure-data basis** (measured = dosimetry / ISO 9612 area survey; estimated = from equipment or similar tasks; none-yet → measure-first) | mcq | measured / estimated / none-yet | ELI-EVIDENCE | always |
| Q1a | *(none-yet only)* Why no data, and is measurement planned? | free-text | "No exposure data → I recommend a **measurement strategy first** (ISO 9612) and will NOT set a surveillance plan or fabricate a comparison." | ELI-EVIDENCE | Q1 == none-yet |
| Q2 | **Named area + similar-exposure group (SEG) / roles** | free-text | "Name the exact area/process and the SEG/roles (e.g. 'press shop line 2 — power-press operators: load → stroke → eject'). **Refuse a generic area ('the factory') or SEG ('all staff') — this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q3 | **Exposure levels** | free-text | "The **8-hr TWA / L_EX,8h dB(A) per SEG** (and peak / C-weighted dB(C) if impulsive). **≥ 85 dBA triggers a hearing-conservation program; at/above the limit mandates noise reduction.** Transcribe the value — never compute or invent one." | ELI-EXPOSURE | always |
| Q4 | **Noise sources** | mcq multi-select | presses / impact · grinding / cutting · pneumatics / air · fans / motors · material handling · other (the equipment/processes driving the exposure) | ELI-SCOPE | always |
| Q5 | **Existing controls & current state** | mcq multi-select | source/engineering control · enclosure/acoustic damping · admin (rotation / time limits / signage) · **hearing protection only** (flagged — does not satisfy the hierarchy) · none | ELI-BASELINE | always |
| Q6 | **Jurisdiction** | mcq | USA / UK / EU / India / Other / Unknown — sets the cited action level / limit | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`; emit a literal `[GAP]`, never a national form-id** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq + free-text | Manufacturing / Construction / Oil-and-Gas / Chemicals / Mining / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site/area/process is each SEG exposed in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full noise + hearing-conservation report (consultant) / SEG audiometry schedule (manager) / single-area noise check (frontline) | ELI-OUTPUT | always |
| Q10 | **Assessor + action owners** | free-text | "Who is the competent person (occupational hygienist / audiometric technician / OH physician role) performing this, and who owns the noise-reduction & surveillance actions? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq + free-text | annual / on-exposure-change / on-STS-trigger / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `no-data` (Q1 = none-yet → Q1a → measurement-strategy-first, no fabricated
comparison; non-mandatory); `india-state` (Q6 = India → Q6a + `KB-REG-IN-FACTORIES`;
**mandatory** state detection, defer to `hse-india`, literal `[GAP]` never a national form-id).

## Echo-back

After the last applicable question (Q11, and Q1a / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing: press-shop noise exposure for the line-2 operator SEG, Plant 3, measured
92 dB(A) L_EX,8h, US OSHA 1910.95 basis, full noise + hearing-conservation report, review on
STS trigger — correct?" Each SEG/area is compared to its cited action level / limit individually
at the comparison step.

## Refuse-on-vague anchors

- **Q2 is the specificity anchor** — refuse a generic area ("the factory") or SEG ("all staff");
  ask again or record `[ASSUMPTION]` / `[GAP]`, never invent a SEG.
- **No surveillance schedule without an exposure basis** — if Q1 (basis), Q2 (named area/SEG)
  and Q3 (≥ an estimated TWA) are not all captured, **do not set an audiometry / surveillance
  schedule**; on Q1 = none-yet, recommend a measurement strategy first. **Never invent a dB
  figure or proceed on "it seems loud".**

## Domain evidence types (ELI-EVIDENCE)

Personal / area noise monitoring (dosimetry, octave-band area survey per ISO 9612) · equipment
sound-power data for an estimated exposure · prior audiometry / standard-threshold-shift outcomes
(**special-category, de-identified by SEG, `<5` suppressed**) · the existing hearing-conservation
program / PPE issue records.
