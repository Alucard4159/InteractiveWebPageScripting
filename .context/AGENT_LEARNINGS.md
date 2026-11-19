# Agent Learnings

> **Context Safety:** Redact sensitive values. No secrets in this file.

## Visual / layout

- Body-background Strahd art (option A) reads too dark/cropped; fixed `<img>` columns (B) are clearer.
- “Transparent gutters” only works if portraits **underlap** past `--side-art` into the content band; opacity alone on empty regions does nothing when no art is behind them.
- Keep aside + `#cxt` / section panels opaque so map/text stay readable over bleed.

## Tooling

- GitHub Pages `/docs` silently fails if that folder is not the real site tree — prefer root + `.nojekyll` for this repo.
- Local preview: `python -m http.server <port>` from repo root; kill when done.
- PowerShell: use `;` not `&&` on older hosts; commit identity may need `GIT_AUTHOR_*` env if config unset (do not write git config).

## QA scope

- Prefer `.context/pack-configs/qa.md` paths; `misc/working.html` is a retired unlinked stub — don’t file “unfinished page” unless nav still points at it.
