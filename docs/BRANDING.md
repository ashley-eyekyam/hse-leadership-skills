# Branding

Make every output your own. This pack ships with the **Eyekyam default** brand so it
looks finished out of the box, and re-brands the *whole* pack from **two files** — no
per-skill editing.

This document is the branding **narrative**: the default, the override mechanism, the
attribution behaviour, logo usage, and how to regenerate the visual assets. The field
**schemas** live with the engines that own them — this file points at them, it does not
restate them:

- visual theme → [`assets/report-engine/brand.schema.json`](../assets/report-engine/) (the A4 report engine)
- identity & attribution → [`branding/company-card.schema.json`](../branding/) (the A9 company card)

---

## The Eyekyam default

Out of the box, every branded report uses the Eyekyam visual identity:

| Element | Value |
|---|---|
| Primary teal | `#2AADA8` — headings, borders, table headers |
| Light teal (accent) | `#47C4BE` — highlights, callout borders |
| Deep teal (secondary) | `#1A7070` — footers, top-dot accent |
| Logo | the Eyekyam mark (`docs/assets/logo.svg`), shared with the report cover |
| Company card | name **Eyekyam** · tagline *"HSE Leadership, operationalised with AI."* · `eyekyam.com` · `ashley@eyekyam.com` |

The default `company-card.yaml` ships at the repo root (`branding/company-card.yaml`).
The owner has approved including the contact in the public default.

---

## Re-brand the whole pack — the two-file override

You re-brand **everything** by editing two repo-root files. Every skill surfaces the
same brand, so one edit propagates across the pack (the "edit once" promise — each
skill's `branding/company-card.yaml` is a symlink to the repo-root file).

| File | Owns | What you put in it |
|---|---|---|
| `brand.yaml` (A4 — the report engine) | the **visual theme** | logo asset, colour palette, fonts, layout |
| `company-card.yaml` (A9 — the company card) | **identity & attribution** | name, tagline, website, contact, CTA, `show`, `placement`, `report_branding_default` |

- **Re-brand globally:** edit `assets/report-engine/brand.yaml` (visuals) and/or the
  repo-root `branding/company-card.yaml` (identity) — the change applies to every skill
  at once.
- **Override per-skill:** replace that skill's `branding/company-card.yaml` *symlink*
  with a real file to give one skill its own card without affecting the rest.

For the exact field reference, see the two schemas linked above — this guide does not
duplicate them (they are the canonical source; restating them here would only drift).

### Attribution behaviour

Attribution is **non-intrusive**: a single line surfaced at a non-blocking moment
(`placement: footer | after-output | on-request`), never a blocking prompt. Set
`show: false` in `company-card.yaml` to omit it entirely.

### The report-branding default

When `company-card.yaml` has `report_branding_default: true`, the report engine applies
the Eyekyam brand automatically whenever a user supplies no `brand.yaml`. Supply your own
`brand.yaml` and it takes precedence.

---

## Logo usage

The hero logo and the branded report cover share the **same mark** (`docs/assets/logo.svg`)
so the GitHub page and the generated PDF/DOCX read as one identity. When you swap in your
own logo, point `brand.yaml` at your asset and replace `docs/assets/logo.svg` (or update
the path) so the README hero and the report cover stay consistent.

---

## Regenerating the visual assets (`docs/assets/`)

All launch visuals are in-repo under `docs/assets/` — no external CDN, so nothing rots:

| Asset | What it is | How to regenerate |
|---|---|---|
| `logo.svg` / wordmark | the brand mark (hero + report cover) | owner-supplied SVG; drop it in and update `brand.yaml` |
| `architecture.svg` | the layering diagram (contract → KB → engines → skills → adapters) | hand-authored SVG; edit in place |
| `screenshot-risk-assessment-*.svg` | de-identified flagship report samples | re-render from a de-identified `report.json` (see the demo script below) |
| `demo.gif` | the highest-converting hero element (owner fast-follow) | record the scripted scenario below; **must be fully de-identified** |

---

## The demo-GIF scenario (scripted, repeatable, owner fast-follow)

The demo GIF is an **owner fast-follow** — it does not block the v1.0.0 tag. Keeping the
scenario scripted here makes re-recording (after a host UI change) a documented, repeatable
step rather than a from-scratch effort. The on-screen data **must be fully de-identified**
(role labels, no real names or sites) — the demo itself honours the de-identification
guarantee.

**Canonical scenario — `risk-assessment`, the T-402 confined-space entry (fully synthetic):**

1. **Prompt (one line):** `Help me risk-assess confined-space entry to clean tank T-402 in Plant 3.`
2. **Intake:** answer the structured §2.7 Q&A with the synthetic facts — prior contents
   (a non-hazardous residue), entry by a two-person crew with role labels (no names),
   atmosphere tested before entry, no prior incidents. The skill echoes the captured facts.
3. **Output:** a T-402-specific finding set, controls ranked elimination-first (PPE-only
   flagged), de-identified throughout, every action with a role-owner + due date.
4. **Render:** run the report engine to produce the branded DOCX + PDF and show the
   Eyekyam-branded cover + the findings / hierarchy-of-controls table.

To render the branded report from a de-identified model:

```bash
pip3 install reportlab python-docx pyyaml
python3 assets/report-engine/generate_report.py \
  --model report.json \
  --brand assets/report-engine/brand.yaml \
  --out ./out \
  --formats docx,pdf
```

**Fallback scenario:** `toolbox-talk` for a shorter, snappier capture if dogfooding shows
it converts better — same de-identification rule applies.

---

See [`README.md`](../README.md#customize--brand) for the one-paragraph "Customize & brand"
pitch that links back here.
