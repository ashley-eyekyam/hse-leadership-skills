<!-- LOCKED fixture — owner-LOCKED at the SW4 19-05 review (CONV-5, 5 July 2026); generated 5 July 2026 via local claude -p subscription capture; do NOT edit without a new owner LOCK. -->

# Incident-Rate Calculation Report — Plant 2, Q1 2026

**Scope:** Plant 2 · **Period:** Q1 2026 (January–March 2026), period-actual
**Recordability standard:** OSHA (29 CFR 1904) · **Base convention:** OSHA standard (200,000 for TRIR/DART; 1,000,000 for LTIFR)
**Prepared:** 6 July 2026 · **Status:** Decision-support — requires competent-person review before use

---

## 1. Inputs (as supplied — aggregate counts only)

De-identification check: inputs are aggregate counts with **no personal or health identifiers** (no names, dates, job titles, or per-case detail). Nothing to scrub; no small-cell (<5) sub-group is published.

| Input | Value | Notes |
|---|---|---|
| OSHA-recordable cases | 3 | Period total |
| DART cases (days away / restricted / transfer) | 2 | Subset of recordables |
| Lost-time injuries (LTI) | 1 | Subset of DART |
| Total hours worked | 290,000 | **Actual hours for the quarter — NOT annualized** |
| Period | Q1 2026 (Jan–Mar) | Period label recorded; never used as a scaling factor |

**Denominator integrity:** hours worked = 290,000 (> 0), supplied and period-actual → **no [GAP] on any denominator**; all three rates share this real exposure base.
**Internal consistency:** recordables (3) ≥ DART (2) ≥ LTI (1) — counts nest correctly.

---

## 2. TRIR — Total Recordable Incident Rate

- **Formula:** TRIR = recordable cases × 200,000 ÷ hours worked
- **Inputs:** 3 × 200,000 ÷ 290,000 = 600,000 ÷ 290,000 = 2.0690…
- **Computed value: 2.07** (2 dp)
- **Base:** 200,000 hours (= 100 full-time-equivalent workers × 2,000 h/yr)
- **Plain-language reading:** At this rate, about **2.07 recordable injuries or illnesses per 100 full-time-equivalent workers per year**. Across the quarter, Plant 2 logged 3 recordables over 290,000 hours.

## 3. DART Rate — Days Away, Restricted, or Transferred

- **Formula:** DART = DART cases × 200,000 ÷ hours worked
- **Inputs:** 2 × 200,000 ÷ 290,000 = 400,000 ÷ 290,000 = 1.3793…
- **Computed value: 1.38** (2 dp)
- **Base:** 200,000 hours
- **Plain-language reading:** About **1.38 cases per 100 FTE-workers per year involved days away, restricted duty, or job transfer**. Two of the three recordables (≈67%) carried a work-limiting consequence — the majority of recordables at Plant 2 this quarter were not minor.

## 4. LTIFR — Lost-Time Injury Frequency Rate

- **Formula:** LTIFR = lost-time injuries × 1,000,000 ÷ hours worked
- **Inputs:** 1 × 1,000,000 ÷ 290,000 = 1,000,000 ÷ 290,000 = 3.4483…
- **Computed value: 3.45** (2 dp)
- **Base:** 1,000,000 hours
- **Plain-language reading:** About **3.45 lost-time injuries per 1,000,000 hours worked**. One LTI occurred this quarter; because the million-hour base is ~3.4× the actual hours worked, a single case produces a rate above 3 — read as "one lost-time event in this exposure," not as a stable trend.

---

## 5. Severity rate

**[GAP] — not computed.** Severity rate is out of scope: there is no validated severity-rate engine in v1.0, and no lost-day count was supplied. Do not infer it from the figures above. Route to a competent person if a severity measure is required.

## 6. Benchmark comparison

**[GAP] — none performed.** No industry benchmark (with source + year) was supplied. A bare comparator is never used. To benchmark TRIR/DART/LTIFR against a sector figure, provide the comparator **with its publishing body and year** (e.g. a BLS/OSHA NAICS-matched rate).

---

## 7. Data-quality caveats (read before acting on these figures)

1. **Small numbers, single quarter, single site.** With only 3 recordables over one quarter, these rates are volatile. Sensitivity: one *additional* recordable would move TRIR from 2.07 to **2.76** (4 × 200,000 ÷ 290,000); one fewer would drop it to **1.38**. Treat quarter-on-quarter movement as signal only when it persists.
2. **Partial-period, not annualized.** All three rates are computed on the actual 290,000 hours for Q1 2026. They are **not** an annual rate and must not be compared to a full-year figure without either (a) accumulating all four quarters or (b) explicitly stated annualization — which was deliberately not applied here.
3. **Classification is assumed correct.** Rates are only as sound as the underlying OSHA 29 CFR 1904 recordability determinations. This calculator did not re-adjudicate whether each case is recordable, DART-qualifying, or lost-time — those classifications are taken as supplied and should be confirmed against the OSHA 300 log by the competent person.
4. **Denominator basis.** 290,000 hours is taken as actual hours worked (productive/exposure hours). If this figure includes non-exposure hours (e.g. certain paid leave) or excludes contractor hours that should be in scope, the rates shift proportionally.
5. **De-identification.** Only aggregate counts were processed; if a case log is later attached, it must be scrubbed to aggregate counts (no per-case line, no <5 sub-group) before any wider circulation.

---

## 8. Ownership, review & disposition

| Item | Owner (role) | Date |
|---|---|---|
| Rate calculation prepared | HSE Data / Metrics Analyst | 6 July 2026 |
| OSHA 300-log classification confirmation | Site Safety Lead, Plant 2 | Confirm by 13 July 2026 |
| Competent-person review & sign-off | Plant 2 HSE Manager | Before any distribution |

**This is decision-support, not a certified statistic.** The figures above are lagging indicators intended to inform review; they do **not** by themselves confirm recordability, establish a trend, or constitute regulatory reporting. A competent person must review the classifications, the denominator basis, and the readings before these rates are published, benchmarked, or acted upon.

---

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
