# De-identification Checklist (placeholder)

> **Phase-1 placeholder.** The canonical de-identification checklist is authored by
> **A5** in Phase 2 (via `hse-skill-forge --sync`). It is referenced from the
> mandatory `hse:block:deid` block in SKILL.md and exists here so rule 8 (dead
> reference links) resolves from Phase 1. A de-id leak is an eval **hard-fail** and
> cannot be waived.

## Checklist (to be expanded by A5)

- [ ] **Detect** — scan inputs for names, contact details, IDs, exact dates of
      birth, health data, and any GDPR Art. 9 / India DPDP / OSHA privacy-case
      category.
- [ ] **Pseudonymize** — replace identifiers with stable role/seq tokens
      (`Worker-A`, `Supervisor-1`, `Site-X`); keep the mapping OUT of the artifact.
- [ ] **Aggregate** — collapse small-number cells that could re-identify an
      individual.
- [ ] **Warn** — if identifiers remain, warn the user and ask before proceeding.
- [ ] **Minimize** — carry only the data the artifact actually needs.
