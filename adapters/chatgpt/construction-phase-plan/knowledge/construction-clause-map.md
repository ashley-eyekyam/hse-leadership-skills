<!-- KB-SNIP-CONSTRUCTION-CLAUSE-MAP -->
# hse-construction clause cross-walk — CDM 2015 duty → artifact → owning skill

**Fragment ID:** `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** CDM 2015 duty → artifact → skill cross-walk (D-04): which
`hse-construction` skill / artifact owns each CDM duty, and the PCI → CPP → H&S File
document chain (D-06). Every construction skill's `kb-selection` references it so a user
asking "which skill covers duty X?" is routed consistently, and each skill knows which
sibling owns an adjacent duty. Referenced by every hse-construction skill's
kb-selection; single source, never duplicated.

> Source: CDM 2015 (SI 2015/51) Reg 4 / 12 / 27 + Schedule 3 + LOLER 1998 Reg 8 + BS 7121 · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — the CDM duty → artifact → skill cross-walk

| CDM / LOLER clause | Artifact | Owning hse-construction skill |
|---|---|---|
| **Reg 4** Pre-construction information | PCI pack | `pre-construction-information` (CON-02) |
| **Reg 12(1)–(2)** Construction phase plan | Construction Phase Plan (CPP) | `construction-phase-plan` (CON-01) |
| **Reg 12(5)** Health & safety file | Health & Safety File | `health-and-safety-file` (CON-03) |
| **Reg 27 + Schedule 3** Traffic routes | Traffic Management Plan | `traffic-management-plan` (CON-05) |
| **LOLER Reg 8 / BS 7121** Lifting operations | Lifting Plan | `lifting-plan` (CON-04) |

## The CDM document chain (D-06) — PCI → CPP → H&S File

The three CDM-document skills share one timing-and-ownership chain so they stay
consistent on who produces what and when:

1. **PCI** (Reg 4, client) — the pre-tender information set, provided as soon as
   practicable → **feeds** the CPP.
2. **CPP** (Reg 12(1)–(2), principal contractor / sole contractor) — produced **before
   construction starts**, built from the PCI and the project's significant activities.
3. **H&S File** (Reg 12(5), principal designer) — the as-built residual-risk record,
   prepared and maintained through the project and **handed over** to the client at
   completion (Reg 12(6)–(9)).

## Adjacent pointers (not duty rows)
- **OSHA 29 CFR 1926** is the US-jurisdiction equivalent grounding (`KB-REG-OSHA1926`);
  a skill selects it when the US jurisdiction is chosen.
- **India BOCW** defers to the `hse-india` engine (state detection mandatory; no
  national form numbers minted).

## How every construction skill uses this fragment
Each skill references `KB-SNIP-CONSTRUCTION-CLAUSE-MAP` in its `kb-selection` so the
bundle presents a single, consistent duty → artifact → skill map and the PCI → CPP →
H&S File chain. No skill restates the cross-walk in its own body (anti-drift).
