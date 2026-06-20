---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-EXPOSURE: "captured inside the change risk assessment, not pre-elicited as a receptor list"
    ELI-LOCATION: "the change carries its own location; no separate site environment elicitation"
  branches:
    - {when: Q3, option: Replacement-in-kind (RIK — exits MOC), activates_output_section: RIK-exit-note}
    - {when: Q3, option: Significant change (full PHA or HAZOP), activates_output_section: pha-trigger, mandatory: true}
    - {when: Q4, option: Temporary, activates_questions: [Q4a], activates_output_section: temporary-change-expiry}
    - {when: Q9, activates_output_section: startup-blocked-banner, mandatory: true}
    - {when: Q10, option: USA, activates_kb_row: us-osha}
    - {when: Q10, option: India, activates_questions: [Q10a], mandatory: true, activates_kb_row: in-factories-act}
---

# Structured intake — management-of-change

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse a vague change** ("an upgrade") and **never authorise start-up while any PSSR item
is open**. Canonical runtime pattern: `KB-SNIP-INTAKE`.

The load-bearing structure is the **change-classification / triage branch** (Q3): a
like-for-like **replacement-in-kind exits MOC**; a **significant change triggers a full
PHA/HAZOP**; and the **PSSR is an inviolable pre-start-up gate** — start-up is withheld
until every PSSR item passes.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Describe the **exact, specific change**. | free-text | refuse "a change" / "an upgrade" — the specificity anchor | ELI-SUBJECT | always |
| Q2 | What **type** of change is it? | MCQ multi-select | Equipment/hardware / Process or operating-condition / Chemical or material / Procedure / Organisational or staffing / Software or control | ELI-SCOPE | always |
| Q3 | **Classification / triage:** like-for-like replacement, or a change requiring review? | MCQ | Replacement-in-kind (RIK — exits MOC) / Minor change / Significant change (full PHA or HAZOP) / Emergency change | ELI-SCOPE | always |
| Q4 | **Permanent or temporary?** | MCQ | Permanent / Temporary | ELI-TEMPORAL | always |
| Q4a | What is the **expiry condition/date**? | free-text | a temporary change without an expiry is flagged | ELI-TEMPORAL | Q4 == Temporary |
| Q5 | What is the **technical basis** (engineering/operational rationale)? | free-text | why the change is sound | ELI-SUBJECT | always |
| Q6 | What **hazards does the change introduce** (for the change RA)? | free-text | scored initial vs residual on the matrix | ELI-SCORING | Q3 != Replacement-in-kind |
| Q7 | Which **PSI / documents / procedures** are affected, and do you hold them? | MCQ multi-select | P&ID / PSI or datasheets / Operating procedures / Relief or SIS basis / Training material / None located | ELI-EVIDENCE | always |
| Q8 | Who is the **change owner** and who **authorises start-up (PSSR)**? | free-text | the gate signatories (de-identified to roles) | ELI-COMPETENCY | always |
| Q9 | Confirm the **PSSR items** — any open item **blocks** start-up. | MCQ multi-select | PSI updated / Procedures updated / Training done / RA controls in place / Equipment as-designed | ELI-OBLIGATIONS | Q3 != Replacement-in-kind |
| Q10 | **Jurisdiction** (statutory hook)? | MCQ | USA / UK / EU / India / ISO 45001 framework | ELI-JURIS | always |
| Q10a | *(India only)* Which **state** is the facility in? | MCQ + free-text | Tamil Nadu / Karnataka / Maharashtra / Delhi/Central / Gujarat / Other / Unknown — confirm the state before citing any state-specific obligation; never silently assume | ELI-JURIS | Q10 == India |
| Q11 | What **output**, for whom, and which **sector**? | MCQ + free-text | MOC package / PSSR checklist / Change RA — for M or C — sector (chemicals / O&G / refining / other) | ELI-OUTPUT | always |
| Q12 | Which **sector** frames the covered process? | MCQ | Chemicals / Oil & Gas / Refining / Petrochemicals / Other | ELI-INDUSTRY | always |

**Branch map:** Q3 = Replacement-in-kind → RIK-exit-note (record justification; skip Q6/Q9 depth, still log). Q3 = Significant change → pha-trigger (require full PHA/HAZOP linkage). Q3 = Emergency change → flag the retrospective-review obligation. Q4 = Temporary → require an expiry (Q4a); temporary-without-expiry is flagged; temporary-change-expiry section. Q9 any item open → startup-blocked-banner; start-up withheld (the hard gate; mandatory). Q10 = USA → `us-osha` (1910.119(l)); Q10 = India → **mandatory state branch** (Q10a) + `in-factories-act`.

## Echo-back

Echo the captured facts back and ask the user to confirm before the change RA:
"Change: **{change}** ({type}, classified **{class}**, **{perm/temp}**{ expiry: …}).
Technical basis: **{basis}**. Change owner **{owner}**, PSSR authoriser **{authoriser}**.
I will NOT authorise start-up until every PSSR item passes. Correct before the change RA?"

## Refuse-on-vague anchors

- Q1 is the specificity anchor: refuse "an MOC for an upgrade" with no specific change.
- A temporary change with no expiry is flagged (Q4a); never proceed without it.
- **Never** authorise start-up with an open PSSR item — start-up is blocked, no exceptions.
