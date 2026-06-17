<!-- KB-REG-EU-CLP -->
<!-- KB-REG-EU-REACH -->
# EU — CLP + REACH (chemicals classification & registration map, legacy-safe)

**Fragment IDs:** `KB-REG-EU-CLP`, `KB-REG-EU-REACH`
**What this is:** a copyright-safe **duty → artifact map** for the two EU chemicals
Regulations the chemicals pack reads: CLP — Regulation (EC) No 1272/2008
(Classification, Labelling and Packaging) — and REACH — Regulation (EC) No 1907/2006
(Registration, Evaluation, Authorisation and Restriction of Chemicals).
**What this is NOT:** a reproduction of the Regulations' Annexes or harmonised
classification tables. Cite the Article / Annex references only; the user resolves
the binding harmonised classification (Annex VI) and the registration dossier from
the official ECHA sources.

> Source: CLP (EC) 1272/2008 + REACH (EC) 1907/2006 — Article/Annex structure (user holds the official text) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (ATPs + REACH restriction/authorisation list updates).

CLP is the EU implementation of GHS (`../standards/ghs.md`) — read GHS for the class
*structure*, CLP for the EU *legal* classification/labelling/packaging duty and the
Annex VI harmonised entries. REACH governs the registration, the (extended) Safety
Data Sheet, authorisation/restriction, and exposure scenarios. US HazCom
(29 CFR 1910.1200, GHS-aligned) is reached via `us-osha.md`; UK COSHH via
`uk-hswa.md` — no duplicate fragment.

## `KB-REG-EU-CLP` — classification / labelling / packaging

| CLP duty | Topic | Grounds (skill / artifact) |
|---|---|---|
| Classify | self-classify or apply Annex VI harmonised classification | ghs-classification-sds-author |
| Label | pictogram + signal word + H/P statements per class | ghs-classification-sds-author |
| Package | child-resistant fastening / tactile warning where required | ghs-classification-sds-author |
| Notify | C&L inventory notification to ECHA | ghs-classification-sds-author |

## `KB-REG-EU-REACH` — registration / SDS / authorisation / restriction

| REACH duty | Topic | Grounds (skill / artifact) |
|---|---|---|
| Registration | dossier for substances ≥1 t/y; no data, no market | ghs-classification-sds-author |
| (e)SDS | the 16-section SDS + exposure scenarios for hazardous substances | ghs-classification-sds-author; chemical-exposure-register |
| Authorisation | Annex XIV SVHC sunset/authorisation | ghs-classification-sds-author |
| Restriction | Annex XVII conditions of use | ghs-classification-sds-author |
| Exposure scenario | use-condition + risk-management measures (link to exposure register) | chemical-exposure-register |

## How the skills use these fragments
- `ghs-classification-sds-author` reads CLP for the EU legal classification/labelling
  and REACH for the (e)SDS + registration/authorisation duties; the SDS §15 regulatory
  section cites these.
- `chemical-exposure-register` reads the REACH exposure-scenario use-condition + RMM
  link when building the SEG-based exposure rows for EU sites.
