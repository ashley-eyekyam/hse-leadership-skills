---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY,
           ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-LOCATION: "A legal register is org/site-level, not a single physical work environment; the site is captured as scope (Q2/ELI-SUBJECT), not as a per-hazard location."
    ELI-EXPOSURE: "Exposed-population scoring is a risk-assessment concern; the register lists obligations by activity, not by exposed party."
    ELI-BASELINE: "No initial-vs-residual baseline — the register tracks compliance status (compliant/gap), captured via the existing-register question (Q5) + the evidence question (Q6), not a control baseline."
    ELI-SCORING: "No risk-matrix scoring — obligations are mapped by applicability + compliance status, not scored on a likelihood/severity matrix."
  branches:
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — legal-compliance-register

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
intake opens with the **jurisdiction(s) gate (Q1, multi-select)**; when **India** is
selected the **mandatory India → state branch (Q1a + `KB-REG-IN-STATEFORMS`)** runs and
state detection must complete **before any India obligation is cited**. **Refuse to list
any obligation** until the jurisdiction(s) **and** the activity profile are captured
(Q2/Q3 are the specificity anchors) — record `[ASSUMPTION]` / `[GAP]`, never invent a
citation or a state form number.

The mandatory branch: **India → state** (Q1 includes India → Q1a + `KB-REG-IN-STATEFORMS`;
confirm the state before citing any form — **never a national form number**; the India
leg defers to the `hse-india` engine, `india-state-form-finder` / `factories-act-returns`).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Jurisdiction(s) for this register | MCQ multi-select | UK / USA / EU / India / Other (India → Q1a; **multi-select — one register may span several**) | ELI-JURIS | always |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any form; defers to hse-india** | ELI-JURIS | Q1 == India |
| Q2 | **Named organisation / site + the activities it performs** | free-text | "Which specific org/site, and what activities does it perform? (activities drive applicability)" — **the specificity anchor; refuse a generic 'a company'** | ELI-SUBJECT | always |
| Q3 | Activity / hazard profile | mcq multi-select | General workplace / Construction / Process or major-hazard / Chemicals / Transport / Noise-vibration / DSE (each pulls its obligation family) | ELI-INDUSTRY | always |
| Q4 | Register purpose | MCQ | ISO 45001 6.1.3 evidence / Due diligence / M&A / New-site setup | ELI-OUTPUT | always |
| Q5 | Existing register state | MCQ | None / Outdated / Partial | ELI-SCOPE | always |
| Q6 | **Compliance evidence held** | free-text | "What evidence of compliance do you hold per activity (permits, certificates, test records, procedures), or 'none' → I'll flag `[GAP]`?" | ELI-EVIDENCE | always |
| Q7 | **Obligation owners** | free-text | "Who owns each obligation area (named role/person — no 'TBD'; de-identified to role labels in the shared register)?" | ELI-COMPETENCY | always |
| Q8 | **Review cycle / next review** | mcq+free-text | Annual / On legal change / Other (+date) — feeds each obligation's review-date cell | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q1 includes India → Q1a + `KB-REG-IN-STATEFORMS`;
**mandatory**; defers to `hse-india`).

## Echo-back

After the last applicable question (Q8, and Q1a if India was selected), **echo a
captured-facts summary** and confirm before any analysis: "Building a legal register for:
{org/site}, jurisdictions {UK + India (Maharashtra)}, activities {general workplace +
chemicals}, purpose {ISO 45001 6.1.3 evidence}, existing register {partial}, review
{annual} — correct? (India obligations will defer to hse-india after state confirmation.)"

## Refuse-on-vague anchors

- Q2/Q3 are the specificity anchors — **refuse to list any obligation** until the
  jurisdiction(s) **and** the activity profile are captured; never list an obligation for
  a jurisdiction or activity not in scope (applicability rigour).
- For **India**, state detection (Q1a) **must complete before any India obligation is
  cited** — never cite an India form before the state is confirmed, and never mint a
  national form number (unverified → `[GAP]`; defer to `hse-india`).

## Domain evidence types (ELI-EVIDENCE)

Permits + licences in force · statutory examination/test certificates · monitoring
records · procedures/SOPs demonstrating an obligation is met · the prior legal register
(if any) · enforcement/audit history (de-identified).
