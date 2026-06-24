<!-- KB-DATA-OBLIGATION-FAMILIES -->
# Obligation families — activity → obligation-family lookup per jurisdiction

**Fragment ID:** `KB-DATA-OBLIGATION-FAMILIES`
**What this is:** the **applicability lookup** the `legal-compliance-register` (#20) skill
uses to map a named activity/hazard profile to the family of legal & other requirements
that typically applies, per jurisdiction. It is the seeding menu for the register's
"obligation → applicability" rows.
**What this is NOT:** a definitive list of applicable law, a substitute for a competent
legal-applicability determination, or a source of statutory form numbers. Applicability is
always confirmed against the named activity and the binding regulation at use time. **India
rows POINT INTO `hse-india`** (`factories-act-returns` / `india-state-form-finder` /
`india-accident-notice`) after mandatory state detection — **no national India form number
is ever minted here**; an unverified form id is left literal `[GAP]`.

> Source: ISO 45001:2018 cl. 6.1.3 (legal & other requirements) / 9.1.2 (evaluation of compliance) · UK HSWA 1974 + MHSWR 1999 · US OSH Act 1970 + 29 CFR 1910/1926 · EU OSH Framework Directive 89/391/EEC · India → hse-india (Factories Act 1948 / OSH Code 2020) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (legislation amended; resolve binding obligation at use time).

---

## Activity → obligation-family map (confirm applicability per named activity)

| Activity / hazard profile | UK family | US family | EU family | India → `hse-india` |
|---|---|---|---|---|
| General workplace | HSWA 1974 s.2/s.3; MHSWR 1999 | OSH Act §5 General Duty; 29 CFR 1910 | Framework Dir. 89/391 Art.5/6 | → `hse-india` (Factories Act general duties) |
| Construction | CDM 2015; Work at Height Regs 2005 | 29 CFR 1926 (Focus Four) | Construction Sites Dir. 92/57 | → `hse-india` (state factory + BOCW rules) |
| Chemicals / process | COSHH 2002; DSEAR 2002 | 29 CFR 1910.1200 HazCom; PSM 1910.119 | CLP + REACH; Seveso III | → `hse-india` (Factories Act 2nd Sch.; MSIHC) |
| Noise / vibration | Control of Noise 2005; Vibration 2005 | 29 CFR 1910.95 | Noise Dir. 2003/10; Vibration Dir. 2002/44 | → `hse-india` (state rules) |
| Manual handling / DSE | MHOR 1992; DSE Regs 1992 | General Duty / ergonomics guidance | Manual Handling Dir. 90/269; DSE Dir. 90/270 | → `hse-india` (state rules) |
| Incident reporting / returns | RIDDOR 2013 | 29 CFR 1904 (300/300A/301) | Member-state transposition | → `hse-india` (state forms — `[GAP]` until detected) |

**Discipline:** every row is an **applicability prompt**, not a confirmed obligation —
the register confirms applicability against the named activity and cites the binding
regulation with its source. For India, the row is a **routing pointer**: run `hse-india`
state detection first, then resolve the state obligation/form there; never assert a national
form number — leave it `[GAP]` until `hse-india` resolves it.

## How the skill uses this fragment

- **#20 legal-compliance-register** reads the activity/hazard profile → selects the
  obligation families → builds the register's obligation/applicability/evidence/gap/owner
  rows per jurisdiction (`KB-SNIP-LEGAL-REGISTER-METHOD` drives the method). A register that
  lists an inapplicable regulation is flagged (#20 eval case 1); an India scenario that
  hard-codes a national form number instead of deferring to `hse-india` is a
  `regulatory_citation_accuracy` hard-fail (#20 eval case 2).
