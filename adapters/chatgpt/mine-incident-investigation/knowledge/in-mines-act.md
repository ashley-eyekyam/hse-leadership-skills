<!-- KB-REG-IN-MINES-ACT -->
# India — Mines Act 1952 + Mines Rules (statutory-artifact map, legacy-first)

**Fragment ID:** `KB-REG-IN-MINES-ACT`
**What this is:** a copyright-safe **provision → artifact map** for the Mines Act
1952 and the Mines Rules — the *duties* each provision creates and which HSE
artifact grounds in it (statutory-Manager / officials appointment, the
ventilation / strata-control / blasting plan duties, the accident-notification
duty, the returns/registers duty). It cites the **duty + topic**, never the
reproduced statutory wording.
**What this is NOT:** a reproduction of the Act / Rules text, and NOT a source of
numbered forms — the *form* layer lives in `KB-REG-IN-DGMS` (forms resolved from
that row, never assumed here). Cross-references `KB-REG-IN-DGMS` for the form ids
and `KB-REG-IN-STATEFORMS` for the legacy-first region resolution.

> Source: Mines Act 1952 + Mines Rules / DGMS (https://www.dgms.gov.in/) — provision→duty map (user holds the statutory text) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (Mines Act among the 13 laws subsumed by the OSH Code 2020 — status in flux).

The Mines Act is the parent OH&S statute for mines (opencast + underground); the
**DGMS** (Directorate General of Mines Safety) administers it through regional /
zonal offices. India is **legacy-first** here: most mines still file the legacy
DGMS forms today, so a mining skill **resolves the mine's region/zone first**
(`KB-REG-IN-STATEFORMS`, mandatory state/region detection), defaults to the
legacy DGMS/Mines Act artifact the mine files, and appends the OSH-Code
transition note. A wrong/invented form is the exact failure this discipline
prevents.

## Provision (duty) → artifact → grounds

| Provision / duty | Artifact it grounds | Skill it grounds | Form layer |
|---|---|---|---|
| Appointment of a statutory **Manager** + statutory officials (qualified, DGMS-recognised) | appointment letters; duty register | dgms-statutory-pack | `KB-REG-IN-DGMS` (appointment letters) |
| **Ventilation** adequacy duty (air quantity/quality underground) | ventilation plan | mine-ventilation-strata-blasting-plan | — (plan, not a prescribed form) |
| **Strata / ground-control** duty (support, roof/side stability) | strata-control / ground-control plan | mine-ventilation-strata-blasting-plan | — |
| **Blasting / shotfiring** duty (explosives use, exclusion, misfire) | blasting plan | mine-ventilation-strata-blasting-plan | — |
| **Emergency preparedness / mine-rescue** duty | mine-rescue emergency response plan | mine-rescue-erp | — |
| **Accident / dangerous-occurrence notification** duty | 24h accident notice; Form J register | dgms-statutory-pack; mine-incident-investigation | `KB-REG-IN-DGMS` (notice + Form J) |
| **Returns / registers** duty | annual return (~20 Jan); Form B employee register | dgms-statutory-pack | `KB-REG-IN-DGMS` (annual return; Form B) |

## How the skills use this fragment
- `dgms-statutory-pack` resolves the obligation → the matched duty row → the
  prescribed artifact + the **form** from `KB-REG-IN-DGMS` (never an invented
  number; unverified forms carry `[GAP]`).
- `mine-ventilation-strata-blasting-plan` grounds the three plan duties (the
  plans are not numbered forms — they are site-specific documents the competent
  person owns).
- Region/zone detection is **mandatory** before citing any form — ask, or
  infer-from-location-then-confirm, never silently assume (`KB-REG-IN-STATEFORMS`).
- The OSH Code 2020 subsumes the Mines Act (state-by-state, transition pending);
  every artifact appends the legacy-first transition note.
