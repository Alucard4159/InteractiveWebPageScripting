# Plugin versions (synced)

> **Context Safety:** Never store secrets/tokens/passwords/private keys in this file.

Records the version this project last reconciled against, per plugin it uses — read from that plugin's own `README.md` `Version:` and `Last updated:` fields. The Synced date column is a copy of `Last updated:` itself, not the calendar date of the bootstrap or sync session. Backs `context-closure`'s **Plugin version drift gate**: without a recorded version to compare against, that gate has nothing to check and always reports `n/a`, which is why it existed as dead code before this file did (see this repo's `context/SUGGESTIONS.md` and `CHANGELOG.md`, entry adding this file, for the full account).

**One row per plugin this project has a `.context/pack-configs/<plugin>.md` for** — the same set `context-bootstrap` step 5 seeds configs for. A plugin the project doesn't use isn't tracked here; an unused plugin changing version is not this project's concern.

| Plugin | Synced version | Synced date |
|---|---|---|
| qa | 1.0.3 | 2026-11-15 |

## Maintenance

- **Written by:** `context-bootstrap` (seeds one row per plugin registered via `pack-configs/`, copying each plugin's current `README.md` `Version:` and `Last updated:` — Synced date is that `Last updated:` value, not the day the row was written) and `context-update-project` (refreshes a plugin's row after its offered changes are accepted — never bumps unless the user actually reconciled).
- **Read by:** `context-closure`'s `Plugin version drift gate`, via `scripts/plugin_registry_io.py::parse_registered` (in the `context-closure` skill) — compared against each plugin's actual current `README.md` version.
- **Never hand-edit the version/date columns** unless deliberately marking a plugin as "reconciled" without running `context-update-project` (e.g. after manually confirming no drift matters for a project's purposes). Prefer letting the two skills above own this file.
- **A plugin added to `pack-configs/` after this file's last write** needs a row added here too — `context-bootstrap`'s top-up behavior handles this automatically on a re-run; don't add rows by hand unless bootstrap can't be re-run for some reason.
