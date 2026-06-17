# Methodology — the CAPA lifecycle (ISO 45001 clause 10.2)

`capa-manager` (B7) manages the full **Corrective & Preventive Action** lifecycle for a
finding, nonconformity, or incident cause — grounded in **ISO 45001 clause 10.2**
(incident, nonconformity & corrective action). It is the **management** layer, not the
upstream artifact: the audit is `safety-audit`'s job, the investigation is
`incident-investigation`'s. The three skills **share one CAPA schema and one engine**
(`smart_actions.py`) — the siblings *produce* the register, this skill *manages* it.

**Stateless-per-run (v1.0).** The whole lifecycle runs **within one invocation** —
ingest/capture → structure → validate → schedule → emit. There is **no persistent,
cross-session CAPA store** (no overdue-dashboard polling across sessions); the `status`
and `verification` fields are designed so a future persistent store (v2) can read them
without a schema change, but v1.0 does not maintain one.

## The ISO 45001 10.2 loop, run as a lifecycle

1. **React to the nonconformity/finding** — capture (or ingest) the specific finding.
2. **Evaluate the need to eliminate the cause** so it does not recur — confirm or
   establish the root cause (the "eliminate the cause" step is what makes a CAPA more
   than a to-do list).
3. **Determine and implement corrective + preventive action** — both first-class, both
   HoC-ranked.
4. **Review the effectiveness** of the action taken — the scheduled effectiveness
   verification (the lifecycle half B7 owns over a produce-once register).
5. **Retain documented evidence** — the branded CAPA register report.

## Corrective vs preventive — both first-class, both HoC-ranked

For **each cause** the output carries **both**:

- a **corrective** action (`capa_type: corrective`) — fix *this* occurrence; and
- **≥1 preventive** action (`capa_type: preventive`) — stop *recurrence*.

Both run through `KB-SNIP-HOC` + `controls.rank_controls`/`validate_treatment`. The
**preventive** action especially favours **Elimination / Substitution / Engineering**
over a one-off administrative fix — the hierarchy lever is what stops "re-train the
operator" being booked as a preventive control. A CAPA with only a corrective patch and
no preventive control is the exact failure clause 10.2 ("eliminate the cause so it does
not recur") exists to catch.

**PPE/admin-only enforcement (the core value, made mechanical).** If
`controls.rank_controls` returns `ppe_admin_only: True`, the Workflow **must** either add
a higher-order control or record an explicit justification ("higher-order controls not
reasonably practicable because…"). A PPE/admin-only corrective **or** preventive
treatment with no higher-order option and no justification is a **defect the Critic/QA
pass must catch** (and scores ≤2 on the `hierarchy_of_controls` rubric dimension).

## The CAPA action schema — reused verbatim, extended additively (NEVER forked)

Each action is the **exact** shape an `incident-investigation`/`safety-audit` register
emits, extended with the lifecycle metadata B7 owns:

```python
{
  "action": "...",                 # producer shape — the action text
  "owner": "Maintenance Lead",     # producer — named owner (smart_actions: no "TBD")
  "due": "2026-07-31",             # producer — ISO-8601 (smart_actions: due_iso_ok)
  "measure": "...",                # producer — the measurable element
  "links_to_cause": "RC-1",        # producer — traceability to a cause id (all_traced_to_cause)
  "hoc_tier": "engineering",       # producer — the controls.py hierarchy tier
  # --- B7 lifecycle additions (additive metadata; NOT in smart_actions.REQUIRED_FIELDS) ---
  "capa_type": "preventive",       # corrective | preventive
  "verification": {                # the effectiveness check B7 schedules
    "method": "re-inspection", "due": "2026-08-31",
    "status": "scheduled", "verified_by": "", "verified_date": ""
  },
  "status": "open"                 # open | in-progress | verified-effective | verified-ineffective | closed
}
```

The **first six fields are validated by `smart_actions.validate_register`**
(`REQUIRED_FIELDS = [action, owner, due, measure, links_to_cause]` + the `hoc_tier` from
`controls`). The **`capa_type` / `verification` / `status` fields are B7's lifecycle
metadata the engine ignores** — so the register round-trips between the producers
(produce) and B7 (manage) with **zero A7 change**.

> **The anti-fork rule (load-bearing).** Never move `verification`/`status`/`capa_type`
> into `smart_actions.REQUIRED_FIELDS`. That would force a `smart_actions` change (an A7
> fork) and break the round-trip — a CAPA could no longer flow from a producer into B7
> without translation. The lifecycle fields are **B7-side** metadata only.

## Effectiveness verification — mandatory, scheduled, first-class

Every CAPA carries a **verification method + a verification due date + a status**. The
**floor** is `method + due + status`. The Workflow **refuses to close a CAPA
`verified-effective` without a recorded check**, and surfaces a CAPA whose verification
is past-due via `smart_actions.days_until_due(verification.due, today)` (negative =
overdue). A CAPA with no effectiveness check is a defect the Critic/QA pass must catch.

**Encouraged (not hard-required): a re-occurrence window.** A stronger verification
records "no recurrence in N days/cycles" as the effectiveness test (e.g. "0 sampled
permits signed off without a recorded isolation check at the next quarterly audit"). The
floor remains method + due + status; the recurrence window is encouraged but not
mandatory in v1.0.

## A7 component wiring (exact functions)

| Step | A7 call | Returns / use |
|---|---|---|
| 4 Confirm/establish cause *(standalone only)* | `rca.scaffold("5-whys", finding)` → `rca.validate("5-whys", analysis)` | minimal cause + `reaches_systemic` — used **only** when no upstream cause is supplied; when an `RC-n` is ingested, reuse it and skip this. |
| 5 Control ranking | `controls.rank_controls(controls)` + `controls.validate_treatment(controls)` over the corrective + preventive set | `{ranked, highest_order, ppe_admin_only, flag}` — the PPE/admin-only flag that forces step-5 justification. |
| 6 Register validation **(the core engine)** | `smart_actions.validate_register(actions)` | `{total, valid, invalid[], all_traced_to_cause}` — owner + ISO date + measure + `links_to_cause` on every action; `all_traced_to_cause` must be true. |
| 7 Lifecycle / overdue view | `smart_actions.days_until_due(verification.due, today)` per action | int — drives the verification-due / overdue surface. |

`risk_matrix` and `incident_rates` are **not** wired (those are B1's and B10's). `rca`
is an **optional** cause-establishment path only — B7 runs a **light** structural check
to establish a minimal cause for a standalone finding, never a full investigation
narrative (that is `incident-investigation`).

## The INGEST field-mapping (the B6→B7 / B5→B7 round-trip)

When a sibling output is supplied (Q0a), B7 **ingests** it rather than re-eliciting:

| From the producer | Lifted into B7 |
|---|---|
| the finding / nonconformity (a `safety-audit` finding id, a `incident-investigation` event) | the step-3 finding anchor |
| the cause id(s) `RC-n` + statement + evidence ref | the step-4 cause (reused, **not** re-investigated) |
| the first CAPA rows `{action, owner, due, measure, links_to_cause, hoc_tier}` | the step-5/6 action set (validated by the **same** `smart_actions.validate_register`) |
| the de-identified facts | re-checked by the De-identifier (not assumed clean) |

B7 then **completes** the CAPA: adds the **preventive** action if the producer supplied
only a corrective one, runs `controls`/`smart_actions` over the full set, and
**schedules an effectiveness check** for each — the lifecycle layer B7 adds. It **does
not** re-run the audit or the investigation (compose, don't overlap). If a supplied
output is malformed or pre-dates the shared schema, the INGEST branch **falls back to
manual capture** (flag `[GAP]`, re-elicit) — never silently fabricating a cause or
action.

## Jurisdiction grounding

ISO 45001 **10.2** + **8.1.2** always. The jurisdiction's documented-information /
corrective-action / record-retention duty is cited from the matched KB row; **India →
resolve the STATE first** (`KB-REG-IN-STATEFORMS`, mandatory state detection) for the
documented corrective-action / return duty — never an invented national form number; an
un-seeded state → `[GAP]` + "verify with a competent person". Unknown jurisdiction →
ask before citing.

## Intake guidance (relocated from SKILL.md Step 0 for char-fit — substance unchanged)

- **Q2 worked example** (the finding/nonconformity anchor): "Audit NC-07: emergency
  lighting in Bay 3 not tested — ISO 45001 8.2 / local fire rule." Refuse to proceed
  on "general non-compliance".
