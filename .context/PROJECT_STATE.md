# Project State

> **Context Safety:** Redact sensitive values. No secrets in this file.

Last updated: 2026-11-12

## What this project does

Static Curse of Strahd / Barovia course site: multi-page HTML with vendored jQuery 4.0.0 + SmartMenus 0.9.5. Gothic visual system (Cinzel / Source Serif 4 tokens), Tarroka fortune flow (`Intro` → `Destiny`), and underlapping Strahd side-portrait columns on desktop.

## Current status

- Phase: stabilization
- Overall: green — QA triage fixes landed; gothic rebuild + side-portrait bleed (`de87d20`) and Cursor context bootstrap (`9275278`) on `main` / GitHub Pages

## Active priorities

- P1: Keep Pages deploy at repo root working (`.nojekyll` present)
- P2: Fill stub pages (`Working.html` topics) when content is ready
- P3: Optional portrait crop/width tweaks only if visual feedback asks

## Environment notes (safe only)

- Runtime(s): Static files; local preview via `python -m http.server` as needed
- Deployment target(s): GitHub Pages from repository root (`/`)
- Key external dependencies (names only): Google Fonts (Cinzel, Source Serif 4); D&D course assets

## Deployment Environments

| Env | URL / path | Notes |
|---|---|---|
| Local | `http://127.0.0.1:<port>/home.html` | Ad-hoc Python http.server |
| GitHub Pages | repo Pages URL | Source = `/` (not `/docs`); `.nojekyll` required |

## Risks / blockers

- Sparse stub pages (Vistani/Barovians/Monsters) look empty beside side art — content debt, not layout debt
- SmartMenus 0.9.5 kept intentionally (no npm runtime upgrade path in this stack)
