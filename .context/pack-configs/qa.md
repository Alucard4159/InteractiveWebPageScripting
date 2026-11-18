# QA pack config

## Scope
Static Curse of Strahd site. Prefer these paths unless the user narrows further:

- `Intro.html`, `barovia.html`, `Destiny.html`
- `home.html`, `gatesofBarovia.html`, `salichWoods.html`
- `strahdInfo.html`, `vistaniInfo.html`, `baroviansInfo.html`, `chapter3.html`, `Working.html`
- `includes/site.js`, `includes/style.css`, `includes/style2.css`
- Shared nav markup duplicated across the HTML pages above
- Vendored libs only when a finding depends on them: `includes/jquery.min.js`, `smartmenus/`

## Out of scope unless asked
- `.git/`, `LICENSE`, `README.md`
- Tarroka card image assets under `includes/tarroka deck/` (content only)
- Full-repo sweeps of minified vendor code

## Constraints
- Report-only until triage asks for a fix
- `Working.html` is an intentional stub for unfinished topics; do not file “page is unfinished” as a bug unless a nav label points at it while a real page already exists (e.g. Woods → `salichWoods.html`)
- Stack is plain HTML + jQuery 4.0.0 + SmartMenus 0.9.5 (vendored); no TypeScript/React/Express
