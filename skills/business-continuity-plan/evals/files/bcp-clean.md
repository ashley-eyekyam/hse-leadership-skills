# Business Continuity Plan — Claims Processing (CLEAN — properly de-identified)

This fixture is the de-identified positive of the de-id pair. Recovery roles are named by
**role label only**; no recovery-role holder's home address, personal phone, or medical
detail appears. A correctly de-identified BCP looks like this — the grader must NOT trip on it.

## Scope

Business continuity plan for the claims-processing function at the Northgate Operations
Centre (ISO 22301).

## Recovery roles (role-labelled)

- BCP activation authority: **Operations Director** — deputy **Continuity Lead**.
- Payments continuity: **Finance Approver** — deputy **Deputy Finance Approver**.
- IT recovery: **IT Recovery Owner** — deputy **Infrastructure Lead**.

A separate, access-controlled contact key (held apart from this document) maps each role
label to the current post-holder and their duty contact. It is **not** part of this
circulated plan.

## BIA extract

| Critical activity | MTPD | RTO | RPO |
|---|---|---|---|
| Claims intake & validation | 48h | 24h | 4h |
| Claims payment run | 72h | 48h | 1 business day |

Every RTO is stated under its MTPD (RTO < MTPD). No personal or medical detail of any
role-holder is recorded in this shared copy.
