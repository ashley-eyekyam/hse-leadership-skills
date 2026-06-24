# Quality checklist — business-continuity-plan (the pre-output validation gate)

Run this self-check before producing any output. A failure is a defect to fix, not a caveat
to ship. The **RTO < MTPD rule is enforced here** (it is a checklist constraint, not an
engine).

## BIA completeness (ISO 22301 8.2.2)
- [ ] **Scope is specific** — a named organisation / site / function, not "the whole
      company". A generic scope is **refused** (the specificity anchor).
- [ ] Every **critical activity** is named with its **output** (what it must keep producing).
- [ ] Each activity has an **impact-over-time** rationale that yields its **MTPD** — the MTPD
      is derived from the curve, never asserted bare.
- [ ] Every activity's **dependencies** (people · IT · suppliers · premises · equipment) are
      captured; single-point dependencies are flagged. Unknowns are `[GAP]`, never invented.

## Recovery objectives (the core constraint)
- [ ] **Every critical activity has an RTO under a stated MTPD** — *RTO < MTPD*, with a stated
      margin. **An RTO asserted with no MTPD basis, or RTO ≥ MTPD, is INVALID** (a
      `regulatory_citation_accuracy` hard-fail on ISO 22301 8.2.2). No exceptions.
- [ ] Every critical activity has an **RPO** set from its data/transaction-loss tolerance.

## Continuity strategies (8.3) — dependency coverage
- [ ] Each strategy **meets its activity's RTO/RPO**.
- [ ] **Every stated dependency is covered by a strategy** — a strategy that ignores a stated
      dependency (e.g. a single supplier, a single key person) is a **defect** (flagged by
      the dependency-coverage check).
- [ ] Any **preventive** control is ranked via `KB-SNIP-HOC` — eliminate the single point of
      failure before merely mitigating it; no token treatment dressed as adequate.

## Plan, roles & exercise (8.4 / 8.5)
- [ ] **Every recovery role has a named deputy** — no single point of failure in the response.
- [ ] An **exercise/test schedule** exists, with owners and ISO due dates (`smart_actions`).
      An untested plan is `[GAP]`, never assumed adequate.
- [ ] A **review cycle / next-review date** is set.
- [ ] A **one-line cross-reference to `emergency-response-plan`** is present for the immediate
      incident-response leg (BCP complements, never duplicates, the ERP — D-07).

## De-identification & citation
- [ ] De-id ran first. Recovery roles may name individuals, but **no recovery-role holder's
      home address or medical note** appears in a shared/role-labelled copy.
- [ ] Every clause citation traces to `KB-STD-ISO22301`; no invented clause or recovery time.
- [ ] No conclusion rests on an unstated assumption — `[ASSUMPTION]` / `[GAP]` are recorded.
