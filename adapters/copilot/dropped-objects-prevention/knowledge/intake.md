---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-OBLIGATIONS: "The dropped-objects duty is the DROPS Recommended Practice / IADC §16 / API RP 2D & RP 54 (a recommended-practice + standard regime, not a substance-specific statutory obligation), resolved from the Q6 jurisdiction and grounded in the kb-selection rows (KB-REG-DROPS; India via KB-REG-IN-OFFSHORE / hse-india). A dedicated substance-obligation question is therefore not asked; the duty is carried by the practice/standard cite, not a separate obligations question."
  branches:
    - {when: Q5, activates_questions: [Q5a], activates_kb_row: KB-DATA-DROPS-IMPACT, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-OFFSHORE, mandatory: true}
---

# Structured intake — dropped-objects-prevention

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named installation / area (Q1 — the specificity anchor)**, captures the **survey scope &
at-height structures (Q2)** and the **object taxonomy (Q3)**, records the **existing securing &
condition (Q4)**, then the **consequence inputs (Q5)** and the **jurisdiction (Q6)**. **Refuse to
assess "the platform" or "looks secured": you need the named installation/area (Q1), the survey
scope & at-height items (Q2–Q3), and the existing-securing status (Q4) before any drafting.** An
at-height item with **no recorded securing standard** (Q4) is an immediate high-priority finding;
the control is **reliable securing + survey + exclusion zones first — never "hard hats below"**.

Two load-bearing branches: the **consequence-band branch** (Q5 = a user-held DROPS Calculator
band → Q5a; the public `m·g·h` energy uses the **user-supplied** mass + fall height, the licensed
threshold VALUES stay `[GAP]`; non-mandatory) and the **mandatory India→state branch** (Q6 = India
→ Q6a + `hse-india`; confirm the state before citing any rule — never a national form number, emit
`[GAP]` where a state return is owed, `KB-REG-IN-OFFSHORE`).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named installation / vessel / area** (the specificity anchor) | free-text | "Name the exact installation, vessel, or at-height work area + its operator/field + the area (e.g. 'Platform Bravo drilling derrick, monkeyboard to drill floor'). **Refuse 'the platform' / 'offshore' — the survey is installation- and area-specific.**" | ELI-SUBJECT | always |
| Q2 | **Survey scope & at-height structures** | mcqmulti-select | derrick or mast / crane boom & pedestal / monkeyboard & fingerboard / flare tip & boom / riser & wellhead deck / piping & small-bore fittings / lighting & instruments / other (+ detail) | ELI-SCOPE | always |
| Q3 | **Object taxonomy** (static vs dynamic, per KB-REG-DROPS) | mcqmulti-select | static dropped object (falls from a static position) / dynamic dropped object (knocked, swung, or dropped during an operation) | ELI-EXPOSURE | always |
| Q4 | **Existing securing & condition** | free-text | "What primary fixing + secondary retention (tethering/lanyards) is in place per at-height item, and its condition / last DROPS inspection? **An at-height item with no recorded securing standard is flagged immediately as a high-priority finding** — never assume an item is secured because it 'looks secured'." | ELI-BASELINE | always |
| Q5 | **Consequence inputs** (the public m·g·h method) | free-text→role | "For each banded object, the **mass (kg)** and the **fall height (m)** — both **user-supplied** (`E ≈ m·g·h`, KB-DATA-DROPS-IMPACT). A missing mass/height is a `[GAP]`, never invented." | ELI-EVIDENCE | always |
| Q5a | *(user holds a DROPS Calculator band)* Record the band | free-text→role | "If you have a DROPS Calculator consequence band for an object, give it — **the skill records your band and leaves the licensed threshold values `[GAP]`; it never recomputes the licensed table or hard-codes a band boundary** (A1 `[ASSUMED]`, surfaced for the SME)." | ELI-EVIDENCE | Q5 == has-band |
| Q6 | **Jurisdiction** | mcq | UK / UKCS / Norway / USA / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Gujarat / Maharashtra / Andhra Pradesh / Other — **mandatory state detection; defer to `hse-india` (KB-REG-IN-OFFSHORE), confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Offshore O&G / Marine-vessel / Offshore-wind / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / environment | free-text | "Which specific deck/level/area and what environment (height band, weather/sea state, SIMOPS overhead) is the at-height work in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full DROPS survey + dropped-object register report (consultant) / dropped-object register + securing plan (manager) / quick per-area securing & exclusion list (frontline) | ELI-OUTPUT | always |
| Q10 | **Securing owner(s) + verifier** | free-text | "Who owns the securing/inspection actions and who is the competent person verifying the DROPS survey (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | Residual risk scoring basis | mcq+free-text | 5×5 risk_matrix (default) / client matrix (+ detail) — the residual is re-scored after reliable securing + exclusion zones | ELI-SCORING | always |
| Q12 | **Review cycle / next survey** | mcq+free-text | per-campaign / on-modification / annual / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `consequence-band` (Q5 = a user-held DROPS band → Q5a + `KB-DATA-DROPS-IMPACT`; the
public `m·g·h` energy uses user-supplied mass + height, licensed thresholds `[GAP]`; non-mandatory);
`india-state` (Q6 = India → Q6a + `hse-india` / `KB-REG-IN-OFFSHORE`; **mandatory**).

## Echo-back

After the last applicable question (Q12, and Q5a / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Surveying dropped objects for: Platform Bravo drilling derrick (monkeyboard to drill floor),
UKCS; at-height structures derrick + monkeyboard + crane boom; objects static (fittings/lights) +
dynamic (swung tubulars); existing securing primary bolting + partial tethering (one fingerboard
item with no recorded securing standard — immediate finding); consequence inputs mass 4 kg / fall
height 28 m supplied, user DROPS band 'major' recorded (licensed thresholds `[GAP]`); full DROPS
survey + register report; review per-campaign — correct?" Each object runs the securing selection +
`m·g·h` banding individually at the analysis step.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "the platform" / "offshore" / "looks secured"; ask
  again or record `[GAP]`, never invent the installation, the at-height inventory, or a securing
  status.
- **Reliable-securing-led, never "hard hats below"** — a dropped-object control recorded as "hard
  hats for the people below" with no survey or reliable securing is a **FLAG pushed up the
  hierarchy** (`KB-SNIP-DROPS-SECURING`), never the headline control.
- **No invented mass/height, no licensed thresholds** — the consequence band traces to the public
  `m·g·h` method with **user-supplied** mass + fall height; a missing input is a `[GAP]`. The skill
  **never** invents a mass/height or reproduces the licensed DROPS Calculator threshold table. A
  missing input is a `[GAP]`. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The at-height inventory per area (Q2) · the static/dynamic taxonomy per object (Q3) · the existing
primary-fixing + secondary-retention status and last DROPS inspection per item (Q4 — a no-recorded-
securing item is an immediate finding) · the user-supplied mass + fall height per banded object and
any user-held DROPS Calculator band (Q5/Q5a — `KB-DATA-DROPS-IMPACT`, licensed thresholds `[GAP]`) ·
photos of the at-height structures / fixings (de-identified — no faces, no name; a prior struck-by /
fatality dropped-object incident de-identified to role label).
