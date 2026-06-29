Portfolio (Clean Static Build)

A framework-free, production-ready static rebuild of the portfolio site,
recovered and sanitised from a deployed Next.js scrape. No build step, no
runtime dependencies — open `index.html` or drop the folder on any static
host (Netlify, GitHub Pages, S3, Nginx, …).

## Run locally

```bash
# any static server works; e.g.
python3 -m http.server 8000
# then open http://localhost:8000
```

> Open via a server (not `file://`) so relative paths and clipboard behave.

## Project structure

```
client-build/
├── index.html              # server-rendered markup, cleaned + prettified
├── css/
│   ├── styles.css          # compiled utility/Tailwind styles (prettified)
│   ├── fonts.css           # @font-face declarations (Geist / Geist Mono)
│   └── custom.css          # hand-authored: scroll-reveal, mobile nav, hero bg
├── js/
│   ├── data.js             # SKILLS + PROJECTS content recovered from the bundle
│   └── main.js             # hand-authored vanilla JS (zero dependencies)
├── assets/
│   ├── images/             # 20 project/profile images (highest-quality variant)
│   ├── fonts/              # 6 WOFF2 font files
│   ├── icons/              # Letterboxd + Trakt SVG icons
│   └── background/         # 5 Batman hero animation frames (.webp)
├── favicon.ico
├── apple-touch-icon.png
├── site.webmanifest
└── robots.txt
```

## What was changed during sanitisation

- **Removed the Next.js runtime** — 16 minified webpack/React chunks and all
  13 `self.__next_f` hydration data blocks were stripped. (The original
  TSX/React source is destroyed at build time and is not recoverable from a
  scrape; it was replaced with the hand-authored `js/main.js` below.)
- **Localised every asset** — all `/_next/image?url=…` optimizer URLs (both
  single- and double-encoded variants) and the responsive `srcSet`/`sizes`
  attributes were collapsed to clean relative paths like
  `assets/images/frameiq.jpg`. Fonts moved from `_next/static/media` to
  `assets/fonts`. See **ASSET-MAP.md**.
- **Neutralised framer-motion hidden states** — 118 elements shipped with an
  inline `opacity:0` (revealed by the now-removed JS). These were set visible
  so nothing renders blank, then re-animated via the reveal layer below.
- **Recovered the real widget data** — the skills and projects datasets were
  extracted verbatim from the original JS bundle into `js/data.js` (no content
  was fabricated).
- **Kept** the JSON-LD structured data and SEO metadata (`og:`, `twitter:`,
  `canonical`) pointing at the canonical domain — social scrapers require
  absolute URLs.
- **Prettified** all HTML, CSS, and JS with Prettier 3.

## Re-implemented interactivity (`js/main.js`)

Progressive enhancement — with JS off, the page is fully readable.

| Feature | Hook |
|---|---|
| Scroll reveal (IntersectionObserver) | `section`, `[data-case-card]`, `article` |
| Mobile navigation toggle | `button[aria-label="Open menu"]` ↔ `nav[aria-label="Mobile navigation"]` |
| Copy-to-clipboard | `button[aria-label^="Copy "]` |
| Hero Batman background cross-fade | `[aria-label="Hero section"]` |
| Smooth in-page scrolling | `a[href*="#"]` |
| **Skills category tabs** | `[role="tablist"][aria-label="AI Skills categories"]` → re-renders the skill grid from `window.SKILLS` |
| **Project carousel** | `Prev/Next project` + counter + thumbnail strip, driven by `window.PROJECTS` |
| **Project category filters** | `All / Professional Work / AI Agents / Machine Learning / Data Analysis` chips subset the carousel |

The skills tabs and project carousel/filters are wired against the recovered
data and verified with an automated DOM test (all interactions pass).

## Optional enhancement not wired

- **Case-file detail modal** — each thumbnail (`[data-case-card]`) could open a
  modal showing the project's `longDescription` (already present in
  `js/data.js`). Currently a thumbnail click selects that project in the
  featured viewer instead. Wiring the modal is a small addition to `main.js`.

## Reproducing this build

The deliverable is regenerated from the original scrape by `build_clean.py`
(hand-authored sources live in `static-src/`). It localises assets, recovers
`data.js` from the bundle, transforms the HTML, and writes `README.md` /
`ASSET-MAP.md`. Re-run with `python3 build_clean.py`.
