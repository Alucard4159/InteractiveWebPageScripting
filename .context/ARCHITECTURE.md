# Architecture

> **Context Safety:** Redact sensitive values. No secrets in this file.

Last updated: 2026-11-19

## Stack

- Plain HTML (no bundler, no npm runtime)
- `includes/jquery.min.js` (4.0.0, single copy)
- `smartmenus/` (0.9.5) + `sm-red.css` theme overrides
- CSS: `includes/tokens.css` → `style.css` / `style2.css` (Intro/Destiny)
- Side art: `includes/side-portraits.js` resolves image base from its own script URL (works from nested folders)

## Directory layout

| Path | Role |
|---|---|
| `index.html` | Site entry (GitHub Pages `/`) |
| `home.html` | Redirect → `index.html` |
| `chapters/` | Gates, Woods, Chapter 3, Vallaki |
| `history/` | Strahd, Vistani, Barovians |
| `monsters/` | Wolves, Bats, Ghouls |
| `flow/` | Intro → Barovia greeting → Destiny |
| `misc/working.html` | Retired stub (unlinked) |
| `includes/`, `smartmenus/` | Shared assets (stay at repo root) |

Only `home.html` remains at root as a **redirect to `index.html`** (LinkedIn). Other legacy root page names were removed after the move.

## Layout

- Desktop (≥1101px): body padding = `--side-art`; portraits wider (`--side-art-bleed`) with edge masks; aside + section panels stay opaque
- Shared nav duplicated across HTML pages (no shared include server-side); nested pages use `../` asset + nav prefixes

## Deploy

- GitHub Pages from repository **root**
- `.nojekyll` so Jekyll does not strip assets
- Entry URL: site root (`index.html`), not `home.html`
