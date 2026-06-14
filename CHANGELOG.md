# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Versioning scheme

Two version surfaces, kept in step:

- **Per-skill** — each skill declares its own semantic version in its frontmatter
  `metadata.version` (e.g. `"1.0"`). Bump it whenever that skill's behaviour or
  contract changes; record the change under the relevant release below.
- **Repo releases** — the pack as a whole is released under date-annotated
  `vMAJOR.MINOR.PATCH` git tags. The first public release is **`v1.0.0`**
  (everything-at-once launch). Bump MAJOR for breaking contract changes, MINOR
  for new skills or capabilities, PATCH for fixes.

## [Unreleased]

### Added

- Repository scaffold: governance, licensing, and authoring-contract surface.

## [v1.0.0] — Unreleased

First public release — the full v1.0 cross-tool skill pack.
