# Triage Session Summary
Date: 2026-11-12
Source: qa-bug-hunt on interactive HTML/JS (see `.context/pack-configs/qa.md`)
Total Findings: 3

## To Fix (3)
- [High] Chapters → Woods opens the stub instead of the woods page
  Fix: Point Woods nav to `salichWoods.html` on all shared nav pages. Applied.
- [High] Intro name labels do not focus their inputs
  Fix: Match `for` to `firstName` / `lastName`. Applied.
- [Medium] Rapid fortune clicks on Destiny stack and tear down card images mid-animation
  Fix: Stop fades, empty `#photo`, then fade in only the new card via `showFortune`. Applied.

## Deferred (0)

## Skipped (0)

## Re-investigated (0)
