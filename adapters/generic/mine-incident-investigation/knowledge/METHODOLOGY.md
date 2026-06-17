# Methodology — mine-incident-investigation (B5 pattern + DGMS overlay)

Extends the **B5 incident-investigation** flagship verbatim: the de-id-first 4-subagent fan-out + mandatory Critic/QA (the roster is pre-seeded below the orchestration block). ICAM is the mining-default RCA method.

## Steps
1. **De-identify first** (sequential dependency) — injured/deceased-miner identity, witness detail, exact pit/shaft locations, small (<5) fatality/injury cells scrubbed before analysis.
2. **Reconstruct** the numbered timeline + evidence log (E-n) from the scrubbed inputs.
3. **RCA** (`rca`) — ICAM default; every causal claim cites an evidence item; reaches a **systemic/organisational** factor (`reaches_systemic` true).
4. **DGMS reportability** — resolve the region/zone first (`KB-REG-IN-STATEFORMS`), then the **24-hour accident notice + Form J** register entry for a DGMS-reportable accident/dangerous occurrence (`KB-REG-IN-DGMS`). Cite **only** the verified anchors as values; any other DGMS form id is `[GAP]`, **never invented** (the citation grader is row-blind — honesty rests on the `[GAP]` marker + the no-fabrication eval + the SME FLAG + the human verifier).
5. **CAPA** — HoC-tagged (`controls` / `smart_actions`), each tracing to a named cause with owner + due date; prefer higher-order controls.
6. `incident_rates` is **context only** (no headline rate unless hours+counts are given).

Every cause is evidence-backed; every CAPA traces to a cause; reportability cites the matched KB row or `[GAP]`.
