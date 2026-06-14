## Data Protection & De-identification (MANDATORY — apply before drafting)

<!-- PLACEHOLDER → A5 Phase 2: this body is a byte-identical Phase-1 placeholder.
     The detect → pseudonymize → aggregate → warn → minimize skeleton below is
     finalized by A5 via `hse-skill-forge --sync`; the marker positions are FINAL. -->

Before drafting ANY output, de-identify the inputs. This block fires first and
is non-waivable (a de-id leak is an eval hard-fail).

1. **Detect** personal and sensitive data (names, contact details, IDs, exact
   dates of birth, health data, and any GDPR Art. 9 / India DPDP / OSHA
   privacy-case category) in the user's inputs.
2. **Pseudonymize by default** — replace identifiers with stable role/seq tokens
   (e.g. `Worker-A`, `Supervisor-1`, `Site-X`) and keep a private mapping out of
   the artifact.
3. **Aggregate** small-number cells that could re-identify an individual.
4. **Warn** the user when input still carries identifiers and ask before
   proceeding.
5. **Minimize** — carry only the data the artifact actually needs.
