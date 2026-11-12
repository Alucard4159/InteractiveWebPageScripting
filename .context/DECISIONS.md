# Decisions

> **Context Safety:** Redact sensitive values. No secrets in this file.

## 2026-11-12 — Side portraits option B + underlap bleed

- **Decision:** Real fixed `<img>` columns (`side-portraits.js`) instead of body background art; portraits underlap content gutters with CSS masks; content panels remain opaque.
- **Why:** Background-only (A) cropped/darkened poorly; user preferred B, then transparent gutters via underlap.
- **Alternatives rejected:** Soft vignette-only (C), drop side art (D), opaque body gutters that hid bleed.

## 2026-11-12 — GitHub Pages from repo root

- **Decision:** Serve from `/` with `.nojekyll`, not `/docs`.
- **Why:** `/docs` path was empty / not updating; root matches the actual static tree.

## 2026-11-12 — Keep SmartMenus 0.9.5; single jQuery 4.0.0

- **Decision:** One vendored jQuery; leave SmartMenus at 0.9.5.
- **Why:** Course static site — no npm app runtime; stacked jQuery copies were the bug.

## 2026-11-12 — Context bootstrap plugins = qa only

- **Decision:** Register `qa` pack-config only (keep existing customized `qa.md`).
- **Why:** Stack is static HTML/jQuery — typescript/secrev/devops packs add noise without matching runtime.
