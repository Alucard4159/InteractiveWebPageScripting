# Recent Changes

> **Context Safety:** Redact sensitive values. No secrets in this file.

## 2026-11-19

- Committed folder restructure + index.html entry to main.
- Added root `index.html` (Pages entry) and moved pages into `chapters/`, `history/`, `monsters/`, `flow/`, `misc/`; `side-portraits.js` resolves assets from its script URL. Restructure script: `scripts/restructure_site.py`.
- Deleted legacy root redirect stubs except `home.html` → `index.html` (LinkedIn).

## 2026-11-18

- Added `vallaki.html` (spoiler-scrubbed town overview); Chapters → Vallaki nav link on all menu pages.
- Added `wolves.html`, `bats.html`, `ghouls.html`; Monsters nav retargeted off `Working.html`; stub page marked retired.
- Committed the monsters + Vallaki bundle as `31a7791` on `main`.

## 2026-11-17

- Added `chapter3.html` (Village of Barovia, spoiler-scrubbed); Chapters → Chapter 3 nav retargeted off `Working.html`.
- Filled `vistaniInfo.html` with Vistani lore; added `baroviansInfo.html` and retargeted History → Barovians nav off `Working.html`.
- Noted live-table campaign chat [Curse of Strahd campaign help](5b6e581a-21df-4cfe-8652-47b0179e4437) as optional setting source — keep table spoilers off the public site.
- Committed the above as `87119de` on `main`.

## 2026-11-12

- Bootstrapped Cursor `.context/` + `.cursor/rules` + hooks (kept existing `triage-summary.md` and `pack-configs/qa.md`); committed `9275278`.
- Added underlapping Strahd side portraits (`includes/side-portraits.js`, token bleed, mask fades) across pages; committed `de87d20`.
- Gothic visual rebuild (tokens, home hero, SmartMenus theme, Intro/Destiny) earlier same day.
- Pages fix: `.nojekyll` + root source.
- QA triage fixes: Woods → `salichWoods.html`, Intro label `for` attrs, Destiny `showFortune` fade race; prior intro XSS/parser fixes.
