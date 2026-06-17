# Methodology — chemical exposure register (SEG-based)

## Method
1. **De-identify first** — exposure-monitoring results and health-surveillance outcomes are tied
   to **SEG/role labels, never names**; per-worker cells <5 suppressed (deid block + checklist §5).
2. **Resolve SEGs + agents** from the intake. For each (SEG × agent): resolve the applicable
   **OEL/WEL/PEL with source+year** (`KB-DATA-OEL-LIMITS`); where the jurisdiction has no statutory
   limit (e.g. India), cite the **most-protective referenced** value and flag it non-statutory.
3. **Band the exposure** with `risk_matrix.score` — chemicals consequence descriptors against the
   same axes (the B1-environmental precedent). Confidence reflects measured vs modelled vs `[GAP]`.
4. **Control tier** — HoC-rank each control with `controls` (LEV/containment/substitution before
   RPE); flag any PPE/RPE-only treatment.
5. **Monitoring / surveillance schedule** — `smart_actions.validate_register`: each action has a
   named (role-label) owner + ISO date + the agent/SEG it addresses.

## Output discipline
- The register rows are `{agent, CAS, SEG/task, OEL (source+year), measured/estimated exposure,
  risk band, control tier, monitoring-due}` — rendered via the report engine.
- No invented OEL value; `[GAP]` + most-protective referenced anchor is honest.
