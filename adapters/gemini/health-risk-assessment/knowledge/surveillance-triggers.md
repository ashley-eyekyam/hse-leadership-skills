<!-- KB-SNIP-SURVEILLANCE-TRIGGERS -->
# Health-surveillance triggers — OEL-linked cadence

**Fragment ID:** `KB-SNIP-SURVEILLANCE-TRIGGERS`
**This is prompt text, applied by the model — not a generator.** It is the method the
`health-risk-assessment` (#25) skill uses to set an OEL-linked health-surveillance schedule.
Exposure limits are resolved from the shipped `KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS`
(no parallel OEL table); ergonomics scores come from the `ergonomics.py` engine +
`KB-STD-GHS-ERGO`.

> Source: UK COSHH 2002 / Control of Noise at Work Regs 2005 / Control of Vibration at Work Regs 2005 · US OSHA 29 CFR 1910.95 (noise) / 1910.1200 · occupational-health surveillance practice · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

1. **Define the similar-exposure groups (SEGs)** by named task/role — refuse generic; the
   SEG is the unit of surveillance.
2. **Compare exposure to a cited OEL.** For each agent, compare measured/estimated exposure
   to the binding OEL/WEL/PEL resolved (with source+year) from `KB-DATA-OEL-LIMITS` /
   `KB-DATA-EXPOSURE-LIMITS`; an exposure assessed with **no cited OEL** fails (#25 eval
   case 1).
3. **Set the surveillance cadence from the trigger:**
   - **Action-level / exposure approaching or above the OEL** → surveillance required;
     cadence per the agent's regime (e.g. noise ≥ action level → audiometry; respiratory
     sensitisers → lung-function; HAV → HAV health surveillance).
   - **Below action level** → exposure monitoring / re-assessment cadence, surveillance not
     yet triggered.
4. **Rank controls above surveillance.** Surveillance is **not a control** — substitution /
   engineering precede PPE and precede surveillance; a noise plan offering only hearing
   protection is flagged (#25 eval case 2, `KB-SNIP-HOC`).
5. **Special-category health data discipline** — surveillance results are reported by SEG/role,
   `<5` small-cell suppression on any health-outcome breakdown, never circulated with names
   (#25 eval case 3 — `de_identification` hard-fail).

## Output expectation

SEG definitions, exposure-vs-OEL comparison, hierarchy-ranked controls, and an OEL-linked
surveillance schedule. Feeds `specificity`, `hierarchy_of_controls`, `de_identification`.
