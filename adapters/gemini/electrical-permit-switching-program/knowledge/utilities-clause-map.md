<!-- KB-SNIP-UTILITIES-CLAUSE-MAP -->
# hse-utilities-power clause cross-walk — NFPA 70E Article 120 / 130.4 / 130.5 → owning skill

**Fragment ID:** `KB-SNIP-UTILITIES-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** (CONV-10) electrical control-hierarchy cross-walk for
`hse-utilities-power`: the de-energize-first **Article 120** ESWC axis plus the
shock (**130.4**) and arc-flash (**130.5**) risk-assessment axes mapped to the
three utilities skills. Every utilities skill's `kb-selection` references it so the
bundle routes consistently and applies one de-energize-first spine.

> Source: NFPA 70E Article 120 (establishing an ESWC) + 130.4 (shock risk assessment + approach boundaries) + 130.5 (arc-flash risk assessment + incident-energy analysis + labeling) + IEEE 1584-2018 — bundle cross-walk · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the utilities axis → owning skill

| Axis (cite, don't paste) | Electrical hazard | Owning hse-utilities-power skill |
|---|---|---|
| **Article 120** establish an ESWC (de-energize first) + 130.4/130.5 risk assessment | Arc flash (thermal incident energy) | `arc-flash-assessment` (UTIL-01) |
| **Article 120** ESWC sequencing + isolation / permit discipline | Switching / isolation / re-energization | `electrical-permit-switching-program` (UTIL-02) |
| **130.5** arc-flash + **130.4** shock risk assessment under the live-work gate | Energized (live) work exposure | `live-working-risk-assessment` (UTIL-03) |

## The de-energize-first spine (every skill applies it)
Each utilities skill leads with **Article 120** — establish an electrically safe
work condition (de-energize, isolate, prove dead, earth) — before any reliance on
arc-rated PPE or approach controls (`KB-SNIP-DEENERGIZE-FIRST`). The incident-energy
value and arc-flash boundary come from the `arcflash.py` engine and the NFPA 70E
PPE-category bands (`KB-STD-NFPA70E`), never invented. Live work is permitted only
through the reg-14 / 1910.333(a)(2) three-part gate (`KB-SNIP-LIVE-WORK-JUSTIFICATION`).

## Adjacent pointers (not axis rows)
- **US grounding:** `KB-REG-OSHA1910-269` (T&D + 1910.333 work practices).
- **UK grounding:** `KB-REG-UK-EAWR` (regs 12–14 + HSG85).
- **Arc-flash standard structure:** `KB-STD-NFPA70E` (130.7(C)(15) PPE bands,
  130.5(H) label, IEEE 1584 method) — reused, not duplicated.
- **India** electrical content defers to the `hse-india` engine (state detection
  mandatory; no national form numbers minted — `KB-REG-IN-ELECTRICAL`).

## How every utilities skill uses this fragment
Each skill references `KB-SNIP-UTILITIES-CLAUSE-MAP` in its `kb-selection` so the
bundle presents one consistent hazard → skill map and the shared de-energize-first
spine. No skill restates the cross-walk in its own body (anti-drift).
