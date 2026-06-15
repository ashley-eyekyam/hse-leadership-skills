# Incident-investigation intake — Conveyor entanglement (de-identified; RCA systemic-trace case)

De-identified intake. Role labels only; no names, IDs, addresses, or small injury cells.
This case tempts an individual-error conclusion but the evidence points to systemic
factors — the RCA must drive past "the operator didn't follow the procedure" to an
organisational cause.

## What happened (Q1)
A maintenance technician (Operator B) reached into a running conveyor to free a snagged
product and their sleeve was caught. The obvious explanation offered by the line manager
is "the operator didn't follow the lockout procedure."

## When and where (Q2)
[GAP — exact date withheld]; Plant 2, packing hall, Conveyor C-7.

## Incident type / severity (Q3 / Q4)
Injury · medical-treatment (one person).

## People involved (Q5 — role labels only)
Operator B (maintenance technician / injured party). Witness W-2 (line lead).

## Immediate / obvious causes (Q6)
Operator reached into a running conveyor without locking it out.

## Evidence available (Q7) — points to SYSTEMIC factors, not individual blame
- E-1 statement: the lockout procedure for C-7 is ambiguous about whether minor snag
  clearance counts as "maintenance" requiring lockout.
- E-2 training records: the technician's lockout refresher had lapsed beyond its cycle.
- E-3 production log: a standing informal practice of clearing snags live to avoid a
  line stop under throughput pressure (the guard interlock had been bypassed previously).
- E-4 photo: no quick-release isolation point within reach of the snag location.

## RCA method preference (Q8)
ICAM (to reach the organisational layer). The investigator should ALSO note that a
Man-only Fishbone or an active-failures-only Swiss-Cheese would be caught by rca.validate
as non-systemic — the systemic floor holds whatever method is chosen.

## Jurisdiction (Q9)
UK.

## Notes for the investigator
The tempting individual-error story ("didn't follow the procedure") is the immediate
cause, not the root. Drive the RCA to the organisational factors (ambiguous procedure
E-1, lapsed training E-2, informal live-clearance practice under pressure E-3); every
cause must cite an E-n, and rca.validate must report reaches_systemic = true.
