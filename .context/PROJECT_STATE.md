# Project State

> **Context Safety:** Redact sensitive values. No secrets in this file.

Last updated: 2026-11-19

## What this project does

Static Curse of Strahd / Barovia course site: multi-page HTML with vendored jQuery 4.0.0 + SmartMenus 0.9.5. Gothic visual system (Cinzel / Source Serif 4 tokens), Tarroka fortune flow (`flow/intro` → `flow/destiny`), and underlapping Strahd side-portrait columns on desktop.

## Current status

- Phase: stabilization
- Overall: green on content; **local uncommitted** folder restructure (`index.html` + `chapters/` / `history/` / `monsters/` / `flow/`) pending push
- Prior content commits on `main`: `87119de`, `31a7791`

## Active priorities

- P1: Commit/push restructure so Pages `/` serves `index.html`
- P2: Optional portrait polish if visual feedback asks
- P3: Optional Krezk/Abbey overviews (spoiler-scrubbed)

## Environment notes (safe only)

- Runtime(s): Static files; local preview via `python -m http.server` as needed
- Deployment target(s): GitHub Pages from repository root (`/`)
- Key external dependencies (names only): Google Fonts (Cinzel, Source Serif 4); D&D course assets

## Deployment Environments

| Env | URL / path | Notes |
|---|---|---|
| Local | `http://127.0.0.1:<port>/` or `/index.html` | Ad-hoc Python http.server |
| GitHub Pages | repo Pages URL | Source = `/`; entry = `index.html`; `.nojekyll` required |

## Risks / blockers

- SmartMenus 0.9.5 kept intentionally (no npm runtime upgrade path in this stack)
- `home.html` is LinkedIn redirect-only — edit `index.html` for home content
