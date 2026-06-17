# Methodology — DGMS statutory obligation resolution (legacy-first)

The skill extends the **B6 safety-audit** pattern (the statutory obligation is the runtime gate) and the **B5** reportability step (the accident-notice path).

## Steps
1. **Resolve the region/zone first** (`KB-REG-IN-STATEFORMS`) — mandatory; a wrong-zone DGMS office is a misfiled notice. Ask or infer-from-location-then-confirm.
2. **Resolve the obligation** to its `KB-REG-IN-MINES-ACT` duty row (appointment / plan duty / notification / returns).
3. **Resolve the form** from `KB-REG-IN-DGMS`. The five **verified anchors** (Form J, Form B, 24h accident notice, annual return ~20 Jan, statutory Manager appointment) are cited as values; **every other** DGMS form id is recorded `[GAP]` — never invented (the citation grader is row-blind; honesty rests on the `[GAP]` marker + the no-fabrication eval + the SME FLAG + the pre-launch DGMS-qualified verifier).
4. **Append the OSH-Code transition note** (legacy-first — most mines still file the legacy DGMS form).
5. **De-identify first** — accident-notice facts carry injured/deceased-miner PII; scrub to role labels and suppress <5 cells before drafting.
6. `smart_actions` assigns owner + due date to any follow-up action.

Every conclusion traces to a `KB-REG-IN-*` row; an unverified form is `[GAP]`, never a value.
