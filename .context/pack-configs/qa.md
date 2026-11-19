# QA pack config

## Scope
Static Curse of Strahd site. Prefer these paths unless the user narrows further:

- `index.html` (entry; `home.html` is redirect-only)
- `flow/intro.html`, `flow/barovia.html`, `flow/destiny.html`
- `chapters/gates.html`, `chapters/woods.html`, `chapters/chapter3.html`, `chapters/vallaki.html`
- `history/strahd.html`, `history/vistani.html`, `history/barovians.html`
- `monsters/wolves.html`, `monsters/bats.html`, `monsters/ghouls.html`
- `misc/working.html` (retired stub)
- `includes/site.js`, `includes/style.css`, `includes/style2.css`, `includes/side-portraits.js`
- Shared nav markup duplicated across the HTML pages above
- Vendored libs only when a finding depends on them: `includes/jquery.min.js`, `smartmenus/`

## Out of scope unless asked
- `.git/`, `LICENSE`, `README.md`
- Tarroka card image assets under `includes/tarroka deck/` (content only)
- Full-repo sweeps of minified vendor code
- Legacy root names (removed); only `home.html` redirect → `index.html` remains

## Constraints
- Report-only until triage asks for a fix
- `misc/working.html` is an intentional retired stub; do not file “page is unfinished” as a bug
- Stack is plain HTML + jQuery 4.0.0 + SmartMenus 0.9.5 (vendored); no TypeScript/React/Express
- Nested pages must keep correct `../includes/` and `../smartmenus/` prefixes
