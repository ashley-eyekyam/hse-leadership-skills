# Pre-report quality checklist (Workflow step 8 — run before drafting the report)

The self-check the orchestrator (and the mandatory Critic/QA pass) runs **before** the
report is assembled. Every item must pass; fix anything that fails first.

## De-identification (the non-waivable floor — a leak is an auto-fail)

- [ ] The de-id scrub ran **FIRST**, before any analysis or drafting.
- [ ] No residual identifier in the circulated output — no real name, employee/Aadhaar/SSN/NI number, contact, exact date, precise location, job-title/crew/shift, or medical detail.
- [ ] No injury/illness cell `<5` survives (aggregated/suppressed, secondary suppression applied).
- [ ] No re-identification key and no name↔label mapping anywhere in the output (the key is held separately).

## Evidence & causation (defensibility)

- [ ] A numbered, time-ordered timeline and a numbered evidence log (`E-1…`) exist; `[GAP]` flagged where facts are missing.
- [ ] **Every root/contributing cause carries an `evidence_ref` (`E-n`)** into the evidence log; no un-evidenced root cause.
- [ ] `rca.validate(method, analysis)` passed — `reaches_systemic` is **true** for the chosen method (the RCA reached a systemic/organisational factor, not individual blame).
- [ ] The chosen method's structure is complete (no `issues` from `rca.validate`).

## CAPA (hierarchy of controls + traceability)

- [ ] Every control walked through the hierarchy of controls; **≥1 Engineering-or-higher control, or an explicit justified absence** (no PPE/admin-only-without-justification — `controls.rank_controls` clears or is justified).
- [ ] **Every CAPA carries a `links_to_cause` (`RC-n`)**, a named (role-label) owner, a valid ISO-8601 `due` date, and a `measure` — `smart_actions.validate_register` reports `all_traced_to_cause` true. No anonymous actions, no "ASAP".

## Reporting & grounding

- [ ] A jurisdiction reportability **verdict** is stated (even when "not reportable"), cited to the matched KB row — India state form via `KB-REG-IN-STATEFORMS` with the **state resolved** (never a national form number; un-seeded state → `[GAP]` + competent-person); UK RIDDOR / US OSHA 29 CFR 1904.39 timelines; Unknown → "ask before citing".
- [ ] Every citation traces to the KB and quotes its `source`+`year`; **no invented citation**.
- [ ] Any contextual incident rate is present **only** if hours+counts were captured (never a fabricated denominator).
- [ ] No conclusion rests on an unstated `[ASSUMPTION]`.
