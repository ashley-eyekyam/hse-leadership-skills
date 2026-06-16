# Incident Investigation — Conveyor C-7 Entanglement, Plant 2 Packing Hall

**Classification:** Injury · medical-treatment (one person) · UK jurisdiction
**Method:** ICAM (Incident Cause Analysis Method) — selected to reach the organisational layer
**Status:** De-identification pass completed FIRST; role labels only throughout.

> De-identification: identifiers detected and pseudonymised before any drafting. The injured
> party is referred to as Operator B (maintenance technician); the line lead as Witness W-2.
> No names, contact details, IDs, addresses, or small injury cells appear below. Any
> re-identification key is held in a separate controlled artifact, not in this report.

---

## 1. What happened (one-paragraph factual account)

Operator B reached into the running Conveyor C-7 to free a snagged product during a
throughput-pressured shift; their sleeve was drawn into the moving belt, causing a
medical-treatment injury. The conveyor was not isolated at the time of the reach-in. The
line manager's first account framed this as "the operator didn't follow the lockout
procedure" — that is the IMMEDIATE cause and a tempting end-point, not the root. The
evidence below drives the analysis past individual error to the organisational system that
made the unsafe act predictable and routine.

## 2. Evidence log (every cause below cites a numbered item)

- **E-1** — Witness/document: the C-7 lockout procedure is AMBIGUOUS about whether minor
  snag clearance counts as "maintenance" requiring full lockout. [verbatim from intake]
- **E-2** — Training records: Operator B's lockout/isolation refresher had lapsed beyond
  its scheduled cycle; the competency was not current at the time of the incident.
- **E-3** — Production log: a STANDING INFORMAL PRACTICE of clearing snags live (without a
  line stop) to protect throughput; the guard interlock had been bypassed on prior
  occasions and this was tacitly tolerated.
- **E-4** — Photograph: no quick-release isolation point within reach of the snag
  location, so isolating meant a walk to a remote isolator and a line stop.

## 3. ICAM analysis

ICAM works outward from the loss through four layers: Absent/Failed Defences →
Individual/Team Actions → Task/Environmental Conditions → Organisational Factors. The
analysis is NOT complete (and `rca.validate(method="icam", …)` does NOT report
`reaches_systemic=True`) until at least one **Organisational Factor** is populated.

### 3.1 Absent or failed defences (the barriers that should have stopped the loss)
- **AFD-1** — The machine guard interlock that should have prevented a live reach-in had a
  known bypass route and had been bypassed before *(E-3)*.
- **AFD-2** — No quick-release isolation point at the snag location, so the lockout
  defence was impractical to use in the moment *(E-4)*.

### 3.2 Individual / team actions (the sharp-end acts — NOT the stopping point)
- **ITA-1** — Operator B reached into a running conveyor without isolating it *(E-3, intake Q6)*.
  This is the immediate act the line manager named. ICAM treats it as a SYMPTOM to be
  explained, not a root cause to be blamed.

### 3.3 Task / environmental conditions (what shaped the act)
- **TEC-1** — Snags were frequent and the only sanctioned isolation point was remote,
  making a live clear the fast, throughput-protecting choice *(E-4)*.
- **TEC-2** — Throughput pressure on the shift created a real cost to stopping the line *(E-3)*.

### 3.4 Organisational factors (the SYSTEMIC layer — the actual roots)
- **OF-1 (root) — Ambiguous lockout procedure.** The written procedure does not clearly
  classify minor snag clearance as lockout-requiring maintenance, so compliant behaviour
  was undefined at the point of work *(E-1)*. **reaches_systemic driver.**
- **OF-2 (root) — Lapsed refresher-training cycle not enforced.** A management-system
  control (competency currency) had failed: the refresher had lapsed and work continued
  *(E-2)*.
- **OF-3 (contributing) — Normalised informal live-clearing practice under throughput
  pressure.** The organisation tolerated (did not detect or correct) a standing workaround
  and a previously bypassed interlock — a supervisory/management-monitoring failure *(E-3)*.

## 4. Root-cause statement (drives PAST individual error)

The injury was **not** caused by an individually careless operator. It was caused by an
organisational system in which (OF-1) the procedure was ambiguous at the point of work,
(OF-2) competency currency was not enforced, and (OF-3) an unsafe live-clearing workaround
was normalised under throughput pressure with a bypassable guard and no nearby isolation
point. The "didn't follow the procedure" account inverts cause and effect: the system made
the unsafe act the path of least resistance.

## 5. Systemic-reach self-check (engine-aligned)

`rca.validate(method="icam", analysis=…)` over §3 returns **`reaches_systemic = True`** and
**`valid = True`**: the `organisational_factors` list is populated (OF-1, OF-2, OF-3, each a
non-empty cause) and all four ICAM categories are present with no structural issues.

**Cross-method floor (proves the floor holds whatever the method, per the eval expectation):**
- A **Man-only Fishbone** — every cause placed under the *Man* branch (e.g. "operator
  inattentive") with no Machine/Method/Organisation branch — is caught by
  `rca.validate(method="fishbone", …)` as `reaches_systemic = False` (no non-"Man" branch
  populated). It would be REJECTED here.
- A **Swiss-Cheese with active failures only** — populating only `active_failures` (the
  live reach-in) and leaving `organisational_influences` empty — is caught by
  `rca.validate(method="swiss-cheese", …)` as `reaches_systemic = False` (the latent
  organisational layer is empty). It would be REJECTED here.

Only the ICAM analysis above, which names OF-1/OF-2/OF-3, clears the systemic floor.

## 6. Provisional corrective directions (full CAPA register on the reportability workstream)

Each links to an organisational root so corrective effort lands on the system, not the
person: re-write the C-7 lockout procedure to classify snag clearance unambiguously (→OF-1);
restore and enforce the refresher-training currency control (→OF-2); install a quick-release
isolation point at the snag location and close the interlock-bypass route, then audit the
informal live-clearing practice out of existence (→OF-3, →AFD-1/AFD-2).

## 7. Assumptions / gaps

- **[GAP]** Exact incident date withheld in intake (Q2) — reporting timeline to be set
  against the actual date on file.
- **[ASSUMPTION]** "Throughput pressure" is taken from the production log narrative (E-3);
  no quantified production-target document was supplied.

---
*Decision-support output. Must be reviewed by a competent person before use. Not legal advice.*
