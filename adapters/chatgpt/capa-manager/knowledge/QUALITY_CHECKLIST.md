# Quality checklist — CAPA register (pre-output gate)

Run this self-check **before** assembling the report. Fix anything that fails first.
This is Workflow step 8; the Critic/QA pass re-checks it adversarially.

## De-identification (hard gate — a leak is non-waivable)

- [ ] The De-identifier ran **FIRST**, before any analysis or drafting.
- [ ] An ingested sibling output was **re-checked**, not assumed clean.
- [ ] Every identifier was detected and listed up front; the output uses **role labels
      only** ("Worker A", "Maintenance Lead").
- [ ] No residual name, address, phone, ID number, or health detail in the circulated
      output.
- [ ] No re-identification key / name↔label mapping embedded — it is returned
      **separately**.
- [ ] No injury/illness cell of fewer than 5 individuals is published.

## Specificity (forces a real finding)

- [ ] The output names the **actual finding/cause** — not "general non-compliance".
- [ ] The CAPA is anchored to the specific nonconformity/finding from intake (or the
      ingested one), against a named requirement/clause.
- [ ] No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` / `[GAP]`
      only; **no invented** cause or action.

## Cause traceability

- [ ] Every action carries a `links_to_cause: "RC-n"`; `smart_actions.validate_register`
      reports `all_traced_to_cause = true`.
- [ ] Where a cause was established standalone, `rca.validate` returned
      `reaches_systemic = true` (not stopped at individual error); an ingested `RC-n` was
      reused, **not** re-investigated.

## Hierarchy of controls (the core value)

- [ ] **Both** a corrective **and** ≥1 preventive action per cause (the corrective/
      preventive split is present).
- [ ] Every action is HoC-tagged (`hoc_tier`); `controls.rank_controls` was run over the
      **full** corrective + preventive set.
- [ ] **No PPE/admin-only corrective or preventive treatment without an explicit
      justification** — if `ppe_admin_only` is `True`, a higher-order control was added
      **or** the justification ("not reasonably practicable because…") is recorded.
- [ ] The preventive action favours a higher-order control where reasonably practicable.

## SMART register (deterministic — the engine, not prose)

- [ ] Every action has a **named owner** (no "TBD"/"unassigned").
- [ ] Every action has a valid **ISO-8601 due date** (no "ASAP").
- [ ] Every action has a measurable **effectiveness measure**.
- [ ] `smart_actions.validate_register` reports **0 invalid** actions.

## Effectiveness verification (the lifecycle B7 owns)

- [ ] Every CAPA carries a **`verification` `{method, due, status}`** (the floor).
- [ ] No CAPA is marked **`verified-effective`** without a recorded check.
- [ ] Any past-due verification is surfaced (`days_until_due` < 0 flagged in the
      register view).

## Regulatory citation

- [ ] **ISO 45001 clause 10.2** (and 8.1.2 for the HoC) is cited.
- [ ] The jurisdiction's documented-information / corrective-action duty is cited from
      the matched KB row; **India → the resolved state duty** via
      `KB-REG-IN-STATEFORMS` (never a national form number).
- [ ] Every citation quotes its fragment's `source`+`year`; **no invented** citation.

## Report

- [ ] A valid `report.json` (`hse-report-model/v1`) assembled per
      `assets/capa-report.template.json`.
- [ ] The canonical `report-output` call produces a branded docx + pdf (or warns-and-
      degrades).
- [ ] `meta.classification` = "Internal — competent-person review required".
