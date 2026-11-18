# Architecture

> **Context Safety:** Redact sensitive values. No secrets in this file.

Last updated: 2026-11-12

## Stack

- Plain HTML pages at repo root (no bundler, no npm runtime)
- `includes/jquery.min.js` (4.0.0, single copy)
- `smartmenus/` (0.9.5) + `sm-red.css` theme overrides
- CSS: `includes/tokens.css` → `style.css` / `style2.css` (Intro/Destiny)
- Side art: `includes/side-portraits.js` injects fixed `<img>` columns; CSS underlap via `--side-art` / `--side-art-bleed`

## Page map

| Page | Role |
|---|---|
| `home.html` | Brand hero + map CTA → Intro |
| `Intro.html` | Name entry → Destiny |
| `Destiny.html` | Tarroka fortune UI |
| `gatesofBarovia.html`, `salichWoods.html`, `chapter3.html`, `barovia.html` | Chapter / setting pages |
| `strahdInfo.html`, `vistaniInfo.html`, `baroviansInfo.html` | History topics |
| `Working.html` | Intentional stub for unfinished nav targets (Monsters only) |

## Layout

- Desktop (≥1101px): body padding = `--side-art`; portraits wider (`--side-art-bleed`) with edge masks so gutters show art; aside + section panels stay opaque
- Shared nav duplicated across HTML pages (no shared include server-side)

## Deploy

- GitHub Pages from repository **root**
- `.nojekyll` so Jekyll does not strip assets
