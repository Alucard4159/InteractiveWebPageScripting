"""One-shot site restructure: root index + chapters/history/monsters/flow/misc."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# old root filename -> new relative path from site root
MOVES: dict[str, str] = {
    "gatesofBarovia.html": "chapters/gates.html",
    "salichWoods.html": "chapters/woods.html",
    "chapter3.html": "chapters/chapter3.html",
    "vallaki.html": "chapters/vallaki.html",
    "strahdInfo.html": "history/strahd.html",
    "vistaniInfo.html": "history/vistani.html",
    "baroviansInfo.html": "history/barovians.html",
    "wolves.html": "monsters/wolves.html",
    "bats.html": "monsters/bats.html",
    "ghouls.html": "monsters/ghouls.html",
    "Intro.html": "flow/intro.html",
    "Destiny.html": "flow/destiny.html",
    "barovia.html": "flow/barovia.html",
    "Working.html": "misc/working.html",
}

# Canonical page keys used in link rewriting (old name -> new site-root path)
LINK_MAP: dict[str, str] = {
    "home.html": "index.html",
    "index.html": "index.html",
    **MOVES,
    # also accept already-new basenames for self-links after rename
    "gates.html": "chapters/gates.html",
    "woods.html": "chapters/woods.html",
    "strahd.html": "history/strahd.html",
    "vistani.html": "history/vistani.html",
    "barovians.html": "history/barovians.html",
    "intro.html": "flow/intro.html",
    "destiny.html": "flow/destiny.html",
    "working.html": "misc/working.html",
}

NAV_OLD = re.compile(
    r'<ul class="sm sm-blue">.*?</ul>\s*</nav>',
    re.DOTALL | re.IGNORECASE,
)


def depth_of(rel: str) -> int:
    return 0 if "/" not in rel else rel.count("/")


def prefix_for(rel: str) -> str:
    d = depth_of(rel)
    return "" if d == 0 else "../" * d


def href_to(target_root_rel: str, from_rel: str) -> str:
    return prefix_for(from_rel) + target_root_rel


def nav_html(from_rel: str) -> str:
    p = prefix_for(from_rel)
    return f"""<ul class="sm sm-blue">
			<li><a href="{p}index.html">Home</a></li>
			<li><a href="#">History</a>
				<ul>
					<li><a href="{p}history/strahd.html">Strahd</a></li>
					<li><a href="{p}history/vistani.html">Vistani</a></li>
					<li><a href="{p}history/barovians.html">Barovians</a></li>
				</ul>
			</li>
			<li><a href="#">Chapters</a>
				<ul>
					<li><a href="{p}chapters/gates.html">Gates</a></li>
					<li><a href="{p}chapters/woods.html">Woods</a></li>
					<li><a href="{p}chapters/chapter3.html">Chapter 3</a></li>
					<li><a href="{p}chapters/vallaki.html">Vallaki</a></li>
				</ul>
			</li>
			<li><a href="#">Monsters</a>
				<ul>
					<li><a href="{p}monsters/wolves.html">Wolves</a></li>
					<li><a href="{p}monsters/bats.html">Bats</a></li>
					<li><a href="{p}monsters/ghouls.html">Ghouls</a></li>
				</ul>
			</li>
		</ul>
	</nav>"""


def rewrite_assets(text: str, from_rel: str) -> str:
    p = prefix_for(from_rel)
    # stylesheet / script / img includes and smartmenus
    text = text.replace('href="includes/', f'href="{p}includes/')
    text = text.replace("href='includes/", f"href='{p}includes/")
    text = text.replace('src="includes/', f'src="{p}includes/')
    text = text.replace("src='includes/", f"src='{p}includes/")
    text = text.replace('href="smartmenus/', f'href="{p}smartmenus/')
    text = text.replace('src="smartmenus/', f'src="{p}smartmenus/')
    # JS string paths for tarroka deck
    text = text.replace('"includes/tarroka deck/', f'"{p}includes/tarroka deck/')
    return text


def rewrite_js_navigations(text: str, from_rel: str) -> str:
    p = prefix_for(from_rel)
    replacements = {
        'window.location.href = "Intro.html"': f'window.location.href = "{p}flow/intro.html"',
        'window.location.href = "barovia.html"': f'window.location.href = "{p}flow/barovia.html"',
        'window.location.href = "Destiny.html"': f'window.location.href = "{p}flow/destiny.html"',
        'window.location.href = "gatesofBarovia.html"': f'window.location.href = "{p}chapters/gates.html"',
        'window.location.href = "salichWoods.html"': f'window.location.href = "{p}chapters/woods.html"',
        'action="barovia.html"': f'action="{p}flow/barovia.html"',
        'action="Destiny.html"': f'action="{p}flow/destiny.html"',
    }
    # same-folder woods from gates after move: gates and woods both in chapters/
    if from_rel.startswith("chapters/"):
        replacements['window.location.href = "salichWoods.html"'] = 'window.location.href = "woods.html"'
        replacements[f'window.location.href = "{p}chapters/woods.html"'] = 'window.location.href = "woods.html"'
    for old, new in replacements.items():
        text = text.replace(old, new)
    # barovia.html + query concat in Intro
    text = text.replace(
        'window.location.href = "barovia.html" + newurl',
        f'window.location.href = "{p}flow/barovia.html" + newurl',
    )
    return text


def rewrite_misc_links(text: str, from_rel: str) -> str:
    p = prefix_for(from_rel)
    # Return home etc.
    text = text.replace('href="home.html"', f'href="{p}index.html"')
    # Any leftover bare old filenames in href=
    for old, new in sorted(LINK_MAP.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(f'href="{old}"', f'href="{href_to(new, from_rel)}"')
    return text


def transform(text: str, from_rel: str) -> str:
    if NAV_OLD.search(text):
        text = NAV_OLD.sub(nav_html(from_rel), text, count=1)
    text = rewrite_assets(text, from_rel)
    text = rewrite_js_navigations(text, from_rel)
    text = rewrite_misc_links(text, from_rel)
    return text


def redirect_html(target: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta http-equiv="refresh" content="0; url={target}" />
	<title>Moved</title>
	<link rel="canonical" href="{target}" />
	<script>location.replace({target!r});</script>
</head>
<body>
	<p>This page moved to <a href="{target}">{target}</a>.</p>
</body>
</html>
"""


def main() -> None:
    # Build index from home
    home = (ROOT / "home.html").read_text(encoding="utf-8")
    index_body = transform(home, "index.html")
    (ROOT / "index.html").write_text(index_body, encoding="utf-8", newline="\n")
    print("wrote index.html")

    # Move/transform each page
    for old_name, new_rel in MOVES.items():
        src = ROOT / old_name
        if not src.is_file():
            print(f"skip missing {old_name}")
            continue
        text = src.read_text(encoding="utf-8")
        text = transform(text, new_rel)
        dest = ROOT / new_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {new_rel}")
        # root redirect stub
        src.write_text(redirect_html(new_rel), encoding="utf-8", newline="\n")
        print(f"redirect {old_name} -> {new_rel}")

    # home.html redirects to index
    (ROOT / "home.html").write_text(redirect_html("index.html"), encoding="utf-8", newline="\n")
    print("redirect home.html -> index.html")

    # side-portraits: resolve includes relative to script URL
    portraits = ROOT / "includes" / "side-portraits.js"
    portraits.write_text(
        """(function () {
  if (document.querySelector(".side-portraits")) {
    return;
  }

  var base = "";
  var scripts = document.getElementsByTagName("script");
  for (var i = 0; i < scripts.length; i++) {
    var src = scripts[i].src || "";
    var marker = "/includes/side-portraits.js";
    var idx = src.lastIndexOf(marker);
    if (idx === -1) {
      idx = src.lastIndexOf("includes/side-portraits.js");
      if (idx !== -1) {
        base = src.slice(0, idx);
        break;
      }
    } else {
      base = src.slice(0, idx + 1);
      break;
    }
  }

  var wrap = document.createElement("div");
  wrap.className = "side-portraits";
  wrap.setAttribute("aria-hidden", "true");
  wrap.innerHTML =
    '<img class="portrait portrait-left" src="' + base + 'includes/Strahd-1.jpg" alt="">' +
    '<img class="portrait portrait-right" src="' + base + 'includes/Strahd-2.jpg" alt="">';
  document.body.prepend(wrap);
})();
""",
        encoding="utf-8",
        newline="\n",
    )
    print("updated includes/side-portraits.js")


if __name__ == "__main__":
    main()
