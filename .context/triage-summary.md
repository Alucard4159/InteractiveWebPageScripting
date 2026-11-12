# Triage Session Summary
Date: 2026-11-12
Source: commit a595f63 (jQuery 4.0.0 swap) — Intro.html, barovia.html, related pages
Total Findings: 4

## To Fix (4)
- [High] Intro submit goes to the wrong place
  Fix: `event.preventDefault()`, then `window.location.href = "barovia.html" + newurl`. Applied.
- [High] Barovia query parser fails open and fails closed
  Fix: Use `URLSearchParams`, skip greeting when `fname` is missing, coalesce missing fields. Applied.
- [Medium] Intro fade-in can miss `load`
  Fix: If `document.readyState === "complete"`, start fade-in; otherwise bind `load`. Applied.
- [Medium — Security] Reflected HTML injection on `barovia.html`
  Fix: Build greeting paragraphs with `.text()` so query values are not parsed as HTML. Applied.

## Deferred (0)

## Skipped (0)

## Re-investigated (0)
