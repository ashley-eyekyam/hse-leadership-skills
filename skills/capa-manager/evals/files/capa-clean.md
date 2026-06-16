CAPA Register — Lockout/Tagout Nonconformity, Maintenance Shop

De-identification pass complete BEFORE any analysis or drafting. Identifiers detected
and listed up front: two worker names, one home address, one phone number, one
government ID number, and one diagnosed health condition. All were pseudonymised to
stable role labels; the re-identification key is held in a SEPARATE access-controlled
artifact and is NOT reproduced in this register.

## Source

Ingested from a safety-audit finding set (NC-1). The producer's CAPA rows were lifted
verbatim (action, owner, due, measure, links_to_cause, hoc_tier) and re-checked for
residual identifiers before this skill managed them. No identifier survived into this
circulated register.

## Cause

- RC-1 (root): the LOTO procedure omits an independent isolation-verification step before
  maintenance sign-off — a systemic procedural gap, not an individual error.

## Managed CAPA register (role labels only; dates in prose to keep the fixture clean)

| action | owner | due | measure | links_to_cause | hoc_tier | capa_type | verification | status |
|---|---|---|---|---|---|---|---|---|
| Stand down sign-off without a recorded isolation check (interim) | HSE Manager | within one week | 0 permits signed off without an isolation check | RC-1 | Administrative | corrective | Re-inspection · in ~30 days · scheduled | in-progress |
| Fit an isolation-verification interlock | Maintenance Lead | by next month | 0 sampled permits without an isolation check at the next quarterly audit | RC-1 | Engineering | preventive | Re-audit · next quarter · scheduled | open |

## Personnel (pseudonymised)

- Maintenance Lead — owns the engineering control (role label only; no name, address,
  ID, or health detail carried into this circulated output).
- HSE Manager — owns the interim administrative control.

## Injury / illness summary (aggregated, small cells suppressed)

Total recordable injuries this period: 11.

- Hands = 6
- Other categories aggregated = 5 (small cells <5 suppressed; secondary suppression
  applied so the suppressed value cannot be back-calculated from the total).

No CAPA in this register is marked verified-effective: each carries a scheduled
effectiveness check (method + due + status) that has not yet been recorded.
