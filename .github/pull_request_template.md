<!-- Pull request template — captures the competent-person sign-off (A8 §2 / §7),
     the quality-gate checklist (§2.3), and the disclaimer acknowledgement.
     The hse_reviewed_by / hse_reviewed_date fields below map to metadata.hse_reviewed_by
     and metadata.hse_reviewed_date (A2 §4). This template *nudges* the values; the
     actual block/gate enforcement is A8's. -->

## What & why

<!-- Summary of the change and why it is needed. Link the issue it closes. -->

Closes #

## Skill(s) touched

<!-- List every skill this PR adds or changes, and confirm the bumped metadata.version
     for each (Decision 6 — per-skill semantic version). -->

- Skill:
- Bumped `metadata.version`:

## Competent-person review (HSE accuracy)

> This skill's HSE accuracy has been reviewed by a competent person (a suitably
> qualified and experienced HSE professional) before merge.

- [ ] This skill's HSE accuracy has been reviewed by a competent person.
- **`hse_reviewed_by`** (reviewer name / credential): ____________________
- **`hse_reviewed_date`** (YYYY-MM-DD): ____________________

## Quality-gate checklist

> Author self-attests; CI verifies. A PR merges to `main` only when these hold.

- [ ] Linter is green (`lint`).
- [ ] ≥3 evals present and weighted score ≥4.0, with **no hard-fail**.
- [ ] **De-identification applied** — no PII / special-category (health) data leak.
- [ ] **Regulatory citations verified against the knowledge base** — none invented.
- [ ] **Structured intake present in the Workflow** (§2.7 — MCQ + free-text, one
      question at a time, echoes facts before analysis).
- [ ] Branded report renders (docx + pdf) from the sample `report.json`.

## Disclaimer acknowledgement

- [ ] I understand outputs are **decision-support**, require **competent-person
      review**, and are **not legal advice** — see [`DISCLAIMER.md`](../DISCLAIMER.md).
