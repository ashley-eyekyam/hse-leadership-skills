# Methodology — toxic-release / dispersion SCENARIO framing (assistive, no modelling)

## Method (assistive — structures input, never models)
1. **De-identify first** — any PII → role labels.
2. **Source term + release mode** from the intake: substance, inventory, catastrophic/continuous/
   instantaneous. Capture the facts; **do not compute a release rate from first principles** unless
   the user supplies it.
3. **Receptors + scenario** — on-site / public / environment; the credible scenario.
4. **Consequence band** — a **qualitative** band via `risk_matrix` (consequence axis only). Any
   **quantitative** distance/concentration is `[GAP]` — handed to the competent-person modelling
   team. **NO PHAST/ALOHA; NO invented dispersion figures.**
5. **Hand to the study** — develop the consequence side with **`bowtie-builder`** (mitigative
   barriers, `KB-STD-CCPS-BOWTIE`) and **`lopa-worksheet`** (`KB-STD-IEC-61511`); name them as the
   downstream owners (SCOPE-OUT). This skill frames the input; it does not run the study.

## Output discipline
- Every un-modelled value is `[GAP]`-flagged. The output is **scenario framing**, explicitly not a
  modelled result — the assistive disclaimer + the no-fabrication eval enforce this.
