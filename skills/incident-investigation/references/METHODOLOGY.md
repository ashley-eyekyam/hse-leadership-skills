# Incident-investigation methodology — the five RCA methods + the defensibility spine

This is the domain method `incident-investigation` applies. It is grounded in **ISO
45001 clause 10.2** (incident, nonconformity & corrective action). Two rules are
load-bearing and run through everything below:

- **Evidence before cause, cause before control.** No cause is asserted without a
  numbered evidence reference (`E-n`); no control (CAPA) exists without a cause
  reference (`RC-n`). A cause with no evidence cannot be a *root* cause.
- **De-identify first.** The De-identifier scrubs all PII/health detail to role labels
  **before** any analysis. Everything here operates on scrubbed, role-labelled text;
  the re-identification key is held separately and never enters the report or a
  subagent prompt.

## The evidence discipline

Reconstruct the factual timeline first (numbered, time-ordered), then build the
**evidence log** — each item `E-1, E-2, …`, typed (statement / photo-ref / log /
reading / document), each summary scrubbed. Where a needed fact is missing, record
`[GAP]` rather than inferring it; where something is inferred, tag `[ASSUMPTION]`.
Facts only at this stage — no causes.

## The five RCA methods (user-chosen at intake Q8; all A7-validated)

Every method is run through the A7 `rca` engine: `rca.scaffold(method, problem)` →
fill the slots **from the evidence log** (each causal claim cites an `E-n`) →
`rca.validate(method, analysis)`. **`reaches_systemic` is enforced on all five** — a
method may not stop at individual blame.

| Method | When to pick | `reaches_systemic` rule (enforced by `rca.validate`) |
|---|---|---|
| **5-Whys** | Quick, single causal chain; minor events. | ≥5 whys, and the **terminal why must not still blame an individual act** (careless / forgot / failed-to-follow → fails). |
| **ICAM** | Systems-based, organisational focus; serious / high-potential events. | ≥1 **Organisational Factor** populated (the four categories: absent/failed defences, individual/team actions, task/environmental conditions, organisational factors). |
| **SCAT** | Loss-Causation model linking to management-system control failures. | **Basic Causes AND Lack-of-Control** both present (immediate causes alone are not enough). |
| **Fishbone (Ishikawa)** | Categorise causes across Man/Machine/Method/Material/Measurement/Environment when factors span domains. | **≥1 non-"Man" branch populated** (a Fishbone with only the "Man" branch is all-individual-blame → fails); every populated cause must be evidence-referenced. |
| **Swiss-Cheese (Reason)** | Trace failed/absent defence layers to latent organisational influences; barrier / defence-in-depth events. | The **organisational-influences (latent) layer populated** with a named failed/absent barrier (active-failures-only → fails); each populated layer names its barrier. |

`references/METHODOLOGY.md` notes the fit, but the **user chooses** — `rca.validate`
still enforces `reaches_systemic` whatever the method, so a mismatched-but-valid method
cannot smuggle in a non-systemic conclusion. (TapRooT / Apollo / Tripod-Beta are out of
v1.0 scope — deferred to the sector packs.)

## Cause → evidence and CAPA → cause traceability

- **Causes** are emitted as `{id: "RC-n", statement, tier: root|contributing|immediate,
  evidence_ref: "E-n"}`. The `evidence_ref` points into the numbered evidence log.
- **CAPAs** are emitted as `{action, owner, due (ISO-8601), measure, links_to_cause:
  "RC-n", hoc_tier}` and ranked by the hierarchy of controls (`KB-SNIP-HOC`). Run
  `controls.rank_controls` (it flags PPE/admin-only-without-justification — prefer
  Elimination/Substitution/Engineering, justify any lower-order-only treatment) and
  `smart_actions.validate_register` (`all_traced_to_cause` true; every action owner +
  ISO date + measure + `links_to_cause`). No anonymous actions, no "ASAP".

## Jurisdiction reporting/notification (a first-class step)

Resolve the jurisdiction; **India → resolve the STATE first (mandatory)** and read the
accident-notice row in `KB-REG-IN-STATEFORMS` (legacy-first — e.g. Maharashtra Form 24
within 24h — plus the OSH-Code transition note; **never a national form number**; an
un-seeded state → `[GAP]` + "verify with a competent person"). UK → RIDDOR 2013
reportable events + timelines; US → OSHA 29 CFR 1904 recordkeeping + 1904.39 (8h
fatality / 24h in-patient-hospitalization, amputation, eye-loss); EU → `KB-REG-EU-OSH`.
**Surface the verdict even when not reportable** — a documented negative is itself
defensible. Unknown jurisdiction → ask before citing. Quote each fragment's
`source`+`year`; never invent a citation.

## Contextual incident rate (optional, off by default)

Only if the intake captured period hours **and** recordable counts, call
`incident_rates.compute_all` for a single *contextual* TRIR/LTIFR figure — never the
conclusion, never fabricated (`incident_rates` raises on zero/negative hours, so it is
guarded and omitted when inputs are absent). Rate dashboards belong to B10.
