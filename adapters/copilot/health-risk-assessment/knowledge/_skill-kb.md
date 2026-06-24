# Knowledge-base manifest for `health-risk-assessment`

The KB fragments this skill grounds in (the rule-9 reference manifest, §3.11). The A8 linter cross-checks every ID against the named folder's `_registry.yaml` and every path against the on-disk tree; `hse-skill-forge --sync` keeps this list in step with the `kb-selection` rows.

| ID | Use | Path |
|---|---|---|
| KB-STD-ISO45001 | The OH&S backbone — clause **6.1.2** (hazard identification & assessment of health risks); cited on every run. | ../../../knowledge-base/standards/iso-45001.md |
| KB-STD-GHS-ERGO | The ergonomics method facts (RULA / REBA / NIOSH lifting equation action bands) that the `ergonomics` engine computes against; cited when an ergonomic score is produced. | ../../../knowledge-base/standards/ghs-ergo.md |
| KB-DATA-OEL-LIMITS | The substance → OEL/WEL/PEL reference anchors (authority+year per row). **The single OEL source** — every exposure is compared to a value resolved here; no parallel OEL table. | ../../../knowledge-base/data-points/oel-limits.md |
| KB-DATA-EXPOSURE-LIMITS | The jurisdiction → exposure-limit resolution map (which authority to cite per jurisdiction); paired with KB-DATA-OEL-LIMITS for the binding value at use time. | ../../../knowledge-base/data-points/exposure-limits.md |
| KB-REG-UK-HSWA | UK regulatory basis — HSWA + COSHH / Control of Noise / Control of Vibration surveillance triggers (cited for a UK site). | ../../../knowledge-base/regulatory/uk-hswa.md |
| KB-REG-US-OSHA | US regulatory basis — OSHA 1910.95 (noise) / 1910.1200 (HazCom) (cited for a US site). | ../../../knowledge-base/regulatory/us-osha.md |
| KB-REG-IN-FACTORIES | India regulatory basis — Factories Act health provisions; **India defers to `hse-india`**, mandatory state detection via KB-REG-IN-STATEFORMS. | ../../../knowledge-base/regulatory/in-factories-act.md |
| KB-SNIP-HOC | Applied to **every** control recommendation (Workflow step 5): substitution/engineering before PPE **and before surveillance**; verified by `controls.py`. | ../../../knowledge-base/prompt-snippets/hierarchy-of-controls.md |
| KB-SNIP-INTAKE | The one-at-a-time, branch, echo-back intake pattern the Workflow opens with (Q1 hazard → Q2 SEG → Q3 exposure → Q4 OEL → Q5 ergonomics tool → Q6 jurisdiction). | ../../../knowledge-base/prompt-snippets/intake-interview.md |
| KB-SNIP-SURVEILLANCE-TRIGGERS | The #25 method snippet — SEG → OEL comparison → OEL-linked surveillance cadence → controls above PPE/surveillance → `<5` health-outcome suppression. | ../../../knowledge-base/prompt-snippets/surveillance-triggers.md |
| KB-SNIP-OPS-CLAUSE-MAP | The hse-operations ISO-45001 clause cross-walk (6.1.2 / 8.1.2 health-risk + surveillance); referenced for the regulatory-basis section. | ../../../knowledge-base/prompt-snippets/ops-clause-map.md |
