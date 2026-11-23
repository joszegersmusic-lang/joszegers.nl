"""Bouwt index.html, en/index.html en de/index.html uit één sjabloon.

Gebruik:  python3 build/build.py
Teksten staan per taal in build/content.py.
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import LANGS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.joszegers.nl"
LETTERS = "ABCDEFGH"


def img(name, widths, w, h, alt, sizes, eager=False):
    srcset = ", ".join(f"/img/{name}-{x}.webp {x}w" for x in widths)
    src = f"/img/{name}-{widths[0]}.webp"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{src}" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" {load} alt="{html.escape(alt)}">')


PHOTOS = {
    "fbw": ("fbw-dirigeren", [700, 1170], 1170, 1462, "(max-width: 860px) 100vw, 36vw"),
    "kso": ("kso-applaus", [800, 1400], 1400, 1230, "(max-width: 860px) 100vw, 36vw"),
    "repetitie": ("repetitie", [800, 1280], 1280, 854, "(max-width: 860px) 100vw, 70vw"),
    "portret": ("portret", [800, 1280], 1280, 859, "(max-width: 860px) 26rem, 30vw"),
    "pixie": ("pixie-dust-studio", [700, 1280], 1280, 960, "(max-width: 860px) 100vw, 36vw"),
    "zw": ("portret-zw", [700, 1279], 1279, 1279, "(max-width: 860px) 16rem, 20vw"),
}


def photo(key, alt, caption=None, cls=""):
    name, widths, w, h, sizes = PHOTOS[key]
    cap = f"\n              <figcaption>{caption}</figcaption>" if caption else ""
    c = f' class="{cls}"' if cls else ""
    return f"<figure{c}>\n              {img(name, widths, w, h, alt, sizes)}{cap}\n            </figure>"


def section(i, sid, title, body, extra_class=""):
    return f'''
    <section class="part" id="{sid}" aria-labelledby="h-{sid}">
      <header class="part__head">
        <span class="mark" aria-hidden="true">{LETTERS[i]}</span>
        <h2 id="h-{sid}">{title}</h2>
      </header>
      <div class="part__body{(' ' + extra_class) if extra_class else ''}">{body}
      </div>
    </section>'''


def paras(items, indent="          "):
    return "".join(f"\n{indent}<p>{p}</p>" for p in items)


def build(code):
    t = LANGS[code]
    path = t["path"]
    sec = t["sections"]  # list of (id, title)

    # A: functies
    rows = []
    for e in t["positions"]:
        fig = ""
        if e.get("photo"):
            fig = "\n            " + photo(e["photo"], e["alt"], e.get("caption"))
        more = f'\n              <p class="more"><a href="{e["link"][0]}">{e["link"][1]}</a></p>' if e.get("link") else ""
        cls = f' class="{e["cls"]}"' if e.get("cls") else ""
        rows.append(f'''
          <li{cls}>
            <div class="prose">
              <h3>{e["name"]}</h3>
              <p class="meta">{e["role"]}</p>
              <p>{e["text"]}</p>{more}
            </div>{fig}
          </li>''')
    s_a = f'\n        <ul class="ensembles">{"".join(rows)}\n        </ul>'

    # B: biografie
    b = t["bio"]
    facts = "".join(f"\n            <dt>{y}</dt><dd>{d}</dd>" for y, d in b["facts"])
    s_b = f'''
        <div class="prose">
          <p class="lead">{b["lead"]}</p>{paras(b["early"])}
          <div class="sub">
            <h3>{b["munich_title"]}</h3>{paras(b["munich"], "            ")}
          </div>
          <div class="sub">
            <h3>{b["back_title"]}</h3>{paras(b["back"], "            ")}
          </div>
          <dl class="facts">{facts}
          </dl>
        </div>
        {photo("portret", b["alt"])}'''

    # C: onderwijs
    o = t["teaching"]
    s_c = f'''
        <div class="prose">
          <p class="lead">{o["lead"]}</p>{paras(o["text"])}
        </div>
        {photo("repetitie", o["alt"], cls="wide-photo")}
        <div class="prose sub">
          <h3>{o["coach_title"]}</h3>
          <p>{o["coach"]}</p>
          <p><a href="#{sec[6][0]}">{o["coach_link"]}</a></p>
        </div>'''

    # D: Maestro
    m = t["maestro"]
    links = "".join(
        f'\n            <li><a href="{u}" rel="noopener"><span class="listen__name">{n}</span><span class="listen__do">{d}</span></a></li>'
        for n, d, u in m["links"])
    s_d = f'''
        <div class="prose">
          <p class="lead">{m["lead"]}</p>{paras(m["text"])}
        </div>
        <div class="listen">
          <p class="listen__intro">{m["invite"]}</p>
          <ul>{links}
          </ul>
        </div>'''

    # E: projecten
    p = t["projects"]
    works = []
    for w in p:
        fig = ("\n            " + photo(w["photo"], w["alt"])) if w.get("photo") else ""
        more = f'\n              <p class="more"><a href="{w["link"][0]}" rel="noopener">{w["link"][1]}</a></p>' if w.get("link") else ""
        works.append(f'''
          <li>
            <div class="prose">
              <h3>{w["name"]}</h3>
              <p class="meta">{w["meta"]}</p>
              <p>{w["text"]}</p>{more}
            </div>{fig}
          </li>''')
    s_e = f'\n        <ul class="works">{"".join(works)}\n        </ul>'

    # F: samenspel
    g = t["together"]
    artists = "".join(f"\n            <li>{n}</li>" for n in sorted(g["artists"], key=lambda x: x.lower().replace("é", "e")))
    bands = "".join(f"\n            <li>{n}</li>" for n in g["bands"])
    s_f = f'''
        <div>
          <h3>{g["artists_title"]}</h3>
          <p class="meta">{g["artists_note"]}</p>
          <ul class="names">{artists}
          </ul>
        </div>
        <div>
          <h3>{g["bands_title"]}</h3>
          <ul class="names">{bands}
          </ul>
        </div>'''

    # G: contact
    c = t["contact"]
    s_g = f'''
        <div>
          <p class="lead">{c["lead"]}</p>
          <a class="contact__mail" href="mailto:joszegersmusic@gmail.com">joszegersmusic<wbr>@gmail.com</a>
          <p><a href="https://www.linkedin.com/in/joszegers" rel="noopener">LinkedIn</a></p>
        </div>
        {photo("zw", c["alt"])}'''

    bodies = [s_a, s_b, s_c, s_d, s_e, s_f, s_g]
    classes = ["", "bio", "", "", "", "groups", "contact"]
    sections = "".join(section(i, sid, title, bodies[i], classes[i]) for i, (sid, title) in enumerate(sec))

    menu = "".join(f'\n        <li><a href="#{sid}"><span>{LETTERS[i]}</span>{title}</a></li>' for i, (sid, title) in enumerate(sec))

    langs = []
    for lc, label, href in [("nl", "Nederlands", "/"), ("en", "English", "/en/"), ("de", "Deutsch", "/de/")]:
        cur = ' aria-current="page"' if lc == code else f' hreflang="{lc}"'
        langs.append(f'\n        <li><a href="{href}" lang="{lc}"{cur} title="{label}">{lc.upper()}</a></li>')
    foot = "".join(f'\n      <li><a href="{href}" lang="{lc}" hreflang="{lc}">{label}</a></li>'
                   for lc, label, href in [("nl", "Nederlands", "/"), ("en", "English", "/en/"), ("de", "Deutsch", "/de/")] if lc != code)

    ld = {
        "@context": "https://schema.org", "@type": "Person", "name": "Jos Zegers",
        "jobTitle": t["job"], "url": SITE + path, "email": "mailto:joszegersmusic@gmail.com",
        "sameAs": ["https://www.linkedin.com/in/joszegers"],
        "worksFor": [
            {"@type": "MusicGroup", "name": "Fanfare Bereden Wapens"},
            {"@type": "CollegeOrUniversity", "name": "Conservatorium Maastricht"},
            {"@type": "MusicGroup", "name": "Kerkraads Symfonie Orkest"},
            {"@type": "MusicGroup", "name": "Philharmonie Sittard"},
        ],
    }

    page = f'''<!DOCTYPE html>
<html lang="{code}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t["title"]}</title>
  <meta name="description" content="{t["description"]}">
  <link rel="canonical" href="{SITE}{path}">
  <link rel="alternate" hreflang="nl" href="{SITE}/">
  <link rel="alternate" hreflang="en" href="{SITE}/en/">
  <link rel="alternate" hreflang="de" href="{SITE}/de/">
  <link rel="alternate" hreflang="x-default" href="{SITE}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{t["title"]}">
  <meta property="og:description" content="{t["description"]}">
  <meta property="og:url" content="{SITE}{path}">
  <meta property="og:image" content="{SITE}/img/og.jpg">
  <meta property="og:locale" content="{t["locale"]}">
  <meta name="theme-color" content="#fafaf7" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0e1828" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/fonts/bodoni-moda.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/css/site.css">
  <script>try{{var t=localStorage.getItem("theme");if(t==="dark"||t==="light")document.documentElement.dataset.theme=t}}catch(e){{}}</script>
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <a class="skip" href="#inhoud">{t["ui"]["skip"]}</a>

  <header class="bar">
    <a class="bar__name" href="{path}">Jos Zegers</a>
    <button class="menu-button" type="button" aria-expanded="false" aria-controls="menu">{t["ui"]["menu"]}</button>
    <nav class="nav" aria-label="{t["ui"]["nav"]}">
      <ol class="menu" id="menu">{menu}
      </ol>
    </nav>
    <div class="tools">
      <ul class="langs">{"".join(langs)}
      </ul>
      <button class="theme" type="button" aria-pressed="false" aria-label="{t["ui"]["dark"]}">
        <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M8 1.5a6.5 6.5 0 0 1 0 13z" fill="currentColor"/></svg>
      </button>
    </div>
  </header>

  <main id="inhoud">
    <section class="opening" aria-label="{t["ui"]["intro"]}">
      <h1 class="opening__name"><span>Jos</span> <span>Zegers</span></h1>
      <p class="opening__lead">{t["lead"]}</p>
      <figure class="opening__photo">
        {img("dirigeren-kso", [800, 1600, 2400], 2400, 1600, t["hero_alt"], "100vw", eager=True)}
      </figure>
    </section>
{sections}
  </main>

  <footer class="foot">
    <p>© <span data-year>2026</span> Jos Zegers</p>
    <ul>{foot}
    </ul>
  </footer>

  <script src="/js/site.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print("geschreven:", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    for code in LANGS:
        build(code)
