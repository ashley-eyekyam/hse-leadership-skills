# FY2025 board safety inputs — benchmark / defensibility fixture

A period's rates with a request to position them against the industry/sector
benchmark. The skill must surface every benchmark WITH its source + year (read from
KB-DATA-TRIR-BENCHMARKS or a user-stated source), compute the rate-vs-benchmark delta
via incident_rates.benchmark_delta (no figure invented or "rounded" by prose), and flag
[GAP] for any comparator with no available source. All inputs de-identified/aggregated.

## Period
- FY2025 (annual), for the Executive Committee.

## Lagging indicators (counts + hours)
- Recordable cases: 14; lost-time: 6; DART: 9. Hours worked: 1,350,000.

## Prior period (FY2024)
- LTIFR 6.00; TRIR 2.31.

## Benchmark request
- "Compare our TRIR and LTIFR against the sector average." The KB benchmark figures
  (KB-DATA-TRIR-BENCHMARKS) are available: sector LTIFR 5.4 and TRIR 2.7, BLS SOII
  manufacturing, 2023.
- A second benchmark — "the global ILO average" — is requested, but no sourced figure
  is available to the skill; this comparator must be flagged [GAP], not invented.

## Expectation
- Every benchmark the narrative makes carries its body + year (BLS SOII, 2023); no
  unsourced "industry average" line; the unavailable ILO comparator is [GAP]; the
  rate-vs-benchmark delta matches the deterministic incident_rates output; a branded
  report.json / docx / pdf is produced.
