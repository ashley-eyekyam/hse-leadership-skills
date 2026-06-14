<!-- KB-REG-IN-STATEFORMS -->
# India — (law, state, obligation) → {form, rule, due, portal} lookup engine

**Fragment ID:** `KB-REG-IN-STATEFORMS`
**Jurisdiction:** India (IN). **This is data, not code** — lookup tables a skill (or
its Regulatory-Checker subagent) reads *after* resolving the user's state.

> Source: state Factory Rules (TN 1950, KA 1969, MH 1963, Delhi/central) and the BOCW Rules — per-row citation in the `rule` column · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (OSH-Code transition in flux).

**Legacy-first.** Resolution returns the **legacy state form** as the primary answer
(what regulators accept today), then appends the row's short OSH-Code transition note.
**No India form is ever cited as a single nationwide number — every form below is a
state-prescribed string.** (The OSH Code consolidates returns in principle, but most
states have not notified their OSH Rules; legacy filings remain valid.)

## Data model — one row per `(law, state, obligation)`

| field | meaning |
|---|---|
| `law` | parent statute/rules — `factories-act`, `bocw`, `mines-act`, `peso`, `msihc` |
| `state` | state code — `TN`, `KA`, `MH`, `DL` (Delhi/central), `All` (rules apply across states), … (row-extensible) |
| `obligation` | `annual-return`, `half-yearly-return`, `accident-notice`, `register`, `license`, … |
| `form` | the prescribed **state** form id (string) |
| `rule` | citing rule / section reference |
| `due` | filing timing |
| `portal` | filing portal pointer, or "verify locally" |
| `osh_transition` | the short OSH-Code transition note for this obligation |

## Seeded rows (verified — the factual anchor)

| law | state | obligation | form | rule | due | portal | osh_transition |
|---|---|---|---|---|---|---|---|
| factories-act | TN | annual-return | Form 22 | TN Factory Rules 1950 | by ~1 Feb (preceding CY) | state portal — verify | OSH Code → single consolidated annual return; TN OSH Rules not yet notified. |
| factories-act | KA | annual-return | Form 20 | KA Factory Rules 1969 | by 1 Feb | state portal — verify | OSH Code → consolidated return; KA not yet notified. |
| factories-act | MH | accident-notice | Form 24 (+ Form 24A dangerous occurrence) | MH Factory Rules 1963 | within 24h | state portal — verify | OSH Code retains accident-notice duty; MH not yet notified. |
| factories-act | DL | annual-return | Form 21 | Delhi/central pattern | by ~1 Feb | state portal — verify | OSH Code → consolidated return. |
| bocw | All | annual-return | Form XXV | BOCW Rules | by 15 Feb | state welfare board | OSH Code subsumes BOCW; rules pending in most states. |

> The four seeded states are **TN / KA / MH / DL** — the only states with verified
> forms supplied by the source masterplan. Every other state is an explicit
> **extension slot** (add a row with verified data only — never invent a state's form).

## Cross-sector module slots (rows seeded; some bodies authored in Phase 6)

These `(law)` rows register the cross-sector modules so India skills can reference
`KB-REG-IN-STATEFORMS` now. The **PESO** and **MSIHC** *fragment bodies* are authored
in Phase 6 sector packs (`hse-process` → PESO, `hse-chemicals` → MSIHC); A3 seeds the
slot + obligation row here.

| law | state | obligation | form | rule | due | portal | osh_transition |
|---|---|---|---|---|---|---|---|
| mines-act | All | accident-notice | (DGMS-prescribed — verify per mine) | Mines Act 1952 / Mines Rules; DGMS | per DGMS timing | DGMS | OSH Code consolidates mines safety; transition pending. |
| peso | All | license | (PESO-prescribed — body in Phase 6 hse-process) | Explosives/Petroleum Rules; PESO | per licence cycle | PESO portal | (extension slot — see Phase 6) |
| msihc | All | register | (MSIHC-prescribed — body in Phase 6 hse-chemicals) | MSIHC Rules 1989 | per rule | state authority | (extension slot — see Phase 6) |

## Mandatory state detection (topic: `state-detection`)

Any India-facing skill MUST resolve the state **before** citing any form:

1. **Ask explicitly** for the state first.
2. **May infer** from a supplied site address — but **confirm before citing** (a
   wrong state = a wrong statutory form).
3. If still unknown → fall back to "Unknown": ask before citing any specific law;
   do not guess.

`state-detection` is a registered `topic` on this fragment so the linter/forge can
confirm India skills reference it.

## Resolution behaviour (legacy-first + transition flag)

- Return the matched legacy row's `form` / `rule` / `due` / `portal` as the primary answer.
- Append the row's `osh_transition` note (direction of change; most states have not
  switched; savings clause keeps legacy filings valid).
- **Optional transition mode** (offered, not default): map the legacy obligation to
  its consolidated OSH equivalent and warn the form/portal may not be live.
