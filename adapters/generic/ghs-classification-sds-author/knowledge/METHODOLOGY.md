# Methodology — GHS/CLP classification + 16-section SDS

## Method
1. **De-identify first** (the deid block) — any author/contact PII → role labels.
2. **Resolve identity + data** from the intake: substance/CAS, mixture composition, available
   hazard data, jurisdiction. **No data → no class** (`[GAP]` + route to a competent person /
   testing). Never assign a GHS class the stated data does not support.
3. **Classify** against the GHS hazard-class structure (`KB-STD-GHS`): physical / health /
   environmental classes + categories. For the EU, apply CLP (`KB-REG-EU-CLP`) including Annex VI
   harmonised entries; resolve the binding criteria from the user's licensed GHS/CLP text.
4. **Assemble the SDS** in the 16-section GHS order (`KB-STD-GHS`). Render **§8 exposure controls
   as an `hoc_table`** — engineering/ventilation before PPE; cite any OEL/WEL/PEL with source+year
   (the exposure register, `chemical-exposure-register`, is the deeper SEG analysis). Cross-walk
   **§14 transport** through `chemical-transport-safety` (ADR/DOT/IMDG).
5. **REACH duties** (`KB-REG-EU-REACH`): registration, (e)SDS + exposure scenarios,
   authorisation/restriction — surface in §15.
6. **HoC ranking** (`controls`): every handling/exposure control ranked elimination → substitution
   → engineering → administrative → PPE; a PPE-only treatment is flagged.

## Output discipline
- The SDS is a **decision-support draft for a competent person**, never an authoritative
  regulatory SDS — the engine stamps the limitations + de-identification notice.
- No invented hazard class / category / H-statement; `[GAP]` is honest, fabrication fails the
  citation grader and the SME-persona review.
