---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-OBLIGATIONS: "The machine-guarding duty is resolved from the Q6 jurisdiction (OSHA 29 CFR 1910 Subpart O 1910.212/.219 · UK PUWER 1998 Regs 11–12 · India Factories Act §21 via hse-india), so a dedicated substance-obligation question is not asked; the per-zone duty is grounded in the kb-selection rows, not a separate obligations question."
  branches:
    - {when: Q5, option: maintenance, activates_questions: [Q5a], activates_kb_row: KB-REG-LOTO, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — machine-guarding-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named machine (Q1 — the specificity anchor)**, captures the **machine type & motion (Q2)**
and the **danger zones (Q3)**, records the **existing safeguarding & condition (Q4)**, then the
**interaction modes (Q5)** and the **jurisdiction (Q6)**. **Refuse to assess "a machine" or
"looks guarded": you need the named machine (Q1), the motion/hazard type (Q2), and the
existing-safeguarding status (Q4) before any drafting.** A danger zone is assessed and a guard
selected in order (it is **never** left as a PPE/admin-only headline control); a
defeated/missing/overridden guard (Q4) is an immediate high-priority finding.

Two load-bearing branches: the **maintenance→LOTO branch** (Q5 = maintenance → Q5a, cross-reference
`KB-REG-LOTO` for energy isolation; non-mandatory) and the **mandatory India→state branch**
(Q6 = India → Q6a + `hse-india`; confirm the state before citing any rule — never a national
form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named machine** (the machine / line / cell + manufacturer/model + function) | free-text | "Name the exact machine, line, or cell + manufacturer/model + what it does (e.g. 'PL-3 250-ton power press, blanking line'). **Refuse 'a machine' / 'the factory' — the assessment is machine-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Machine type & hazardous motion** | mcqmulti-select | power press / rotating shaft or spindle / conveyor or in-running rolls / robot or automated cell / mixer or auger / saw or blade / other (+ detail) | ELI-SCOPE | always |
| Q3 | **Danger zones** (per 1910.212(a) / ISO 12100) | mcqmulti-select | point of operation / in-running nip point / rotating parts / power-transmission (shaft/belt/gear) / flying chips or sparks / crush or trap point | ELI-EXPOSURE | always |
| Q4 | **Existing safeguarding & condition** | free-text | "What guards/devices are fitted today and in what condition? **A defeated, missing, or overridden guard is flagged immediately as a high-priority finding** — never assume a zone is guarded because it 'looks guarded'." | ELI-BASELINE | always |
| Q5 | **Interaction modes** (maintenance triggers the LOTO cross-reference to `KB-REG-LOTO`) | mcqmulti-select | normal operation / setting / cleaning / maintenance | ELI-EVIDENCE | always |
| Q5a | *(maintenance only)* Energy sources for isolation | free-text→role | "For the maintenance interaction, what energy sources must be isolated (electrical / stored mechanical / hydraulic / pneumatic / thermal / gravity)? Cross-reference `KB-REG-LOTO`: identify sources → isolate → verify zero energy before access." | ELI-EVIDENCE | Q5 == maintenance |
| Q6 | **Jurisdiction** | mcq | USA / UK / EU / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Manufacturing / Warehousing-Logistics / Process / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site/area/line is the machine in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full guarding-register report (consultant) / hazard-zone register + guard-by-zone (manager) / quick per-zone guard list (frontline) | ELI-OUTPUT | always |
| Q10 | **Guard owner(s) + verifier** | free-text | "Who owns the guard install/repair actions and who is the competent person verifying the guarding (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-machine-change / on-guard-modification / annual / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `maintenance-loto` (Q5 = maintenance → Q5a + `KB-REG-LOTO`; energy isolation,
verify zero energy; non-mandatory); `india-state` (Q6 = India → Q6a + `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q5a / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing guarding for: PL-3 250-ton power press, blanking line, Plant 3, Maharashtra; danger
zones point-of-operation + power-transmission shaft; existing safeguarding light-curtain (defeated
— immediate finding) + fixed shaft guard; interaction modes normal + maintenance (→ LOTO energy
isolation); full guarding-register report; review on guard-modification — correct?" Each danger
zone runs the guard/device selection individually at the selection step.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a machine" / "the factory" / "looks guarded"; ask
  again or record `[GAP]`, never invent the machine, the motion, or a guard status.
- **No "guard all moving parts"** — every danger zone (Q3) gets a specific guard/device selected
  in order (`KB-SNIP-GUARD-SELECTION`); a generic blanket statement is refused.
- **Engineering-led, never PPE/admin-only** — a mechanical-zone control recorded as "operators to
  keep hands clear / wear gloves" with no fixed/interlocked guard is a **FLAG pushed up the
  hierarchy**, never the headline control. A missing input is a `[GAP]`. **Never proceed on a
  vague input.**

## Domain evidence types (ELI-EVIDENCE)

The danger zones per machine (Q3) · the existing guards/devices and their condition (Q4 — a
defeated/missing guard is an immediate finding) · the interaction modes and the energy sources
to isolate for maintenance (Q5/Q5a — `KB-REG-LOTO`) · the access frequency per zone (drives the
guard-selection order) · photos of the machine / guards (de-identified — no faces, no name; a
prior amputation / crush incident de-identified to role label).
