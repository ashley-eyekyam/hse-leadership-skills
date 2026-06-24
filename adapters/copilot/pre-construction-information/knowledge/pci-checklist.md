<!-- KB-SNIP-PCI-CHECKLIST -->
# Pre-Construction Information — L153 Appendix-1 content checklist (CDM 2015 Reg 4)

**Fragment ID:** `KB-SNIP-PCI-CHECKLIST`
**This is prompt text, applied by the model — not a generator.** It is the
Pre-Construction Information (PCI) content checklist from HSE L153 Appendix 1, grounded
in CDM 2015 Regulation 4 (the client provides the PCI as soon as practicable to
everyone appointed or being considered — Reg 4(4); no construction start without
arrangements/CPP — Reg 4(5)/(6)). Consumed by `pre-construction-information` (CON-02).

> Source: CDM 2015 (SI 2015/51) Reg 4 + HSE L153 ACOP Appendix 1 · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the L153 Appendix-1 PCI checklist

Assemble the pre-tender hazard and information set the client must provide. Walk these
heads, stating what is **known** versus a documented information **gap**:

1. **Project description & client brief** — the named project, programme, key dates,
   and the client's significant requirements.
2. **Existing structure information** — drawings/as-builts, structural form/stability,
   pre-construction surveys, the existing **health & safety file** content.
3. **Existing services** — buried and overhead services (electricity, gas, water,
   telecoms), their location and isolation arrangements.
4. **Ground conditions** — ground/geotechnical/contamination information, water table,
   previous use.
5. **Surroundings** — adjacent occupancies, boundaries, access/egress, public
   interface, neighbouring activities.
6. **Significant design & construction hazards** — known hazards a designer/contractor
   must be told of (asbestos and other hazardous materials, confined spaces,
   demolition hazards, fragile surfaces).
7. **Information gaps register** — every unknown recorded as a `[GAP]` (e.g. a missing
   asbestos survey), never silently omitted.

## Discipline
- A PCI that silently omits a missing survey instead of recording a `[GAP]` is a
  defensibility failure — state the gap and proceed with assumptions surfaced.
- State the client's Reg 4 duty and timing (as soon as practicable; before
  appointments/start).
- The PCI feeds the Construction Phase Plan — it is information, not the plan itself.

## How the skill uses this fragment
`pre-construction-information` references `KB-SNIP-PCI-CHECKLIST` for the content heads,
grounds the Reg 4 duty on `KB-REG-CDM2015`, and emits the PCI pack. The PCI → CPP →
H&S File chain is cross-walked in `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`.
