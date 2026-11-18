# Decisions

> **Context Safety:** Redact sensitive values. No secrets in this file.

## 2026-11-18 — Vallaki as Chapters entry (not “Chapter 4”)

- **Decision:** Add `vallaki.html` labeled **Vallaki** in Chapters, not “Chapter 4”.
- **Why:** Course nav already mixes named locations (Gates/Woods) with “Chapter 3”; Vallaki is a place name students recognize. Avoid implying a strict module chapter index that would pull in Abbey spoilers next.
- **Alternatives rejected:** Naming it Chapter 4; stuffing Vallaki into `chapter3.html`.

## 2026-11-18 — Monsters get dedicated pages; retire `Working.html` from nav

- **Decision:** Add `wolves.html`, `bats.html`, `ghouls.html` with course-safe lore; point Monsters menu there; keep `Working.html` as an unlinked “coming soon” for old bookmarks.
- **Why:** Same pattern as Barovians/Chapter 3 — finished topics should not share one stub URL. Empty menus beside side art were the remaining content debt.
- **Alternatives rejected:** Leaving monsters on `Working.html`; deleting `Working.html` (breaks any saved links).

## 2026-11-17 — Chapter 3 = Village of Barovia page

- **Decision:** Add `chapter3.html` as a spoiler-scrubbed Village of Barovia overview; point Chapters → Chapter 3 there. Do not paste live-table campaign spoilers from DM notes.
- **Why:** Next beat after Gates/Woods in the course site; campaign chat is useful for setting texture, not for public WBG310 copy.
- **Alternatives rejected:** Leaving Chapter 3 on `Working.html`; writing Vallaki/Abbey spoilers into the course page.

## 2026-11-17 — Barovians get their own page; keep `Working.html` as multi-stub

- **Decision:** Add `baroviansInfo.html` and retarget History → Barovians there (same dedicated-page pattern later used for Chapter 3 and Monsters).
- **Why:** Barovians is a finished History topic; overwriting `Working.html` would still leave other stubs pointing at Barovians content. A dedicated page matches Strahd/Vistani and keeps the stub honest.
- **Alternatives rejected:** Replacing `Working.html` body with Barovians copy; leaving Barovians on the stub until all topics are ready.

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
