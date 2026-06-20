---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT]
  omits:
    ELI-JURIS: "TODO: author — covered, or justify omission"
    ELI-INDUSTRY: "TODO: author — covered, or justify omission"
    ELI-LOCATION: "TODO: author — covered, or justify omission"
    ELI-EXPOSURE: "TODO: author — covered, or justify omission"
    ELI-BASELINE: "TODO: author — covered, or justify omission"
    ELI-EVIDENCE: "TODO: author — covered, or justify omission"
    ELI-OBLIGATIONS: "TODO: author — covered, or justify omission"
    ELI-SCORING: "TODO: author — covered, or justify omission"
    ELI-COMPETENCY: "TODO: author — covered, or justify omission"
    ELI-TEMPORAL: "TODO: author — covered, or justify omission"
  branches: []
---

# Structured intake — <skill>

<!-- TODO: author — this is a born-conformant intake stub. Replace the three universal
     question rows with this skill's real intake question set, cover or justify each
     conditional dimension above, and add any branches the domain method needs. -->

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | TODO: scope of this assessment / output | MCQ | TODO: author the enumerable scope options | ELI-SCOPE | always |
| Q1 | TODO: the named task / site / asset (the specificity anchor) | free-text | TODO: prompt for the specific task broken into steps + the site/area/asset | ELI-SUBJECT | always |
| Q2 | TODO: output artifact wanted + its reader | MCQ | TODO: author the deliverable + audience options (leadership / consultant / frontline) | ELI-OUTPUT | always |

## Echo-back
TODO: author the echo-back template — echo the captured facts back and ask the user to
confirm before any analysis begins (e.g. "Producing: {subject}, {scope}, {output} — correct?").

## Refuse-on-vague anchors
- Q1 is the specificity anchor: refuse a vague subject ("write me a risk assessment");
  never proceed on a vague or missing input — require the named task + steps.
