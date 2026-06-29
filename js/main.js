/* =========================================================================
 * main.js — hand-authored vanilla JavaScript for the static portfolio.
 *
 * The original site was a Next.js / React app whose interactivity lived in
 * minified, bundled webpack chunks (framer-motion, Radix UI, etc.). That
 * compiled runtime was removed during the static rebuild. This file
 * re-implements the user-facing behaviour with zero dependencies as a
 * progressive enhancement: with JS disabled the page is fully readable;
 * with JS enabled the interactions below come to life.
 *
 * Sections:
 *   1. Scroll reveal      — fade content in as it enters the viewport
 *   2. Mobile navigation  — open/close the hamburger menu
 *   3. Copy-to-clipboard  — the "copy email" buttons
 *   4. Hero background     — cycle the Batman frames behind the hero
 *   5. Smooth anchor scroll — graceful in-page navigation
 * ===================================================================== */

(function () {
  "use strict";

  /* Reloads should always land at the top (hero), never a restored
   * scroll position or a stale "#section". Set this as early as possible. */
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  window.addEventListener("load", () => window.scrollTo(0, 0));

  /* Run after the DOM is parsed (script is also loaded with `defer`). */
  document.addEventListener("DOMContentLoaded", init);

  function init() {
    initScrollReveal();
    initMobileNav();
    initClipboard();
    initHeroBackground();
    initSmoothScroll();
    initSkillTabs();
    initProjectCarousel();
    initCustomCursor();
  }

  /* Small helpers shared by the data-driven widgets below. */
  function el(tag, cls, text) {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }
  function byText(scope, selector, text) {
    return Array.from(scope.querySelectorAll(selector)).find(
      (n) => n.textContent.trim() === text,
    );
  }

  /* ---------------------------------------------------------------------
   * 1. Scroll reveal
   * Tags the major page sections and animates them in on first view.
   * Respects the user's reduced-motion preference (handled in custom.css).
   * ------------------------------------------------------------------- */
  function initScrollReveal() {
    const els = Array.from(document.querySelectorAll("[data-reveal]"));
    if (!els.length) return;

    const reveal = (el) => el.classList.add("is-visible");

    // Reduced-motion: CSS already shows everything; nothing to animate.
    if (
      window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ) {
      els.forEach(reveal);
      return;
    }

    // Apply each element's original framer "from" transform as its start-state
    // (the CSS .js rule already set opacity:0). A light stagger between
    // siblings recreates the cascading entrance of the original site.
    const groupIndex = new Map();
    els.forEach((el) => {
      const from = el.getAttribute("data-reveal-from");
      if (from && from !== "none") el.style.transform = from;
      const parent = el.parentElement;
      const n = groupIndex.get(parent) || 0;
      groupIndex.set(parent, n + 1);
      el.style.transitionDelay = Math.min(n, 6) * 0.06 + "s";
    });

    const inViewport = (el) => {
      const r = el.getBoundingClientRect();
      return r.top < window.innerHeight && r.bottom > 0;
    };

    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(
        (entries, obs) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              reveal(entry.target);
              obs.unobserve(entry.target);
            }
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.08 },
      );
      // Animate above-the-fold elements in on load; observe the rest.
      requestAnimationFrame(() =>
        els.forEach((el) => {
          if (inViewport(el)) requestAnimationFrame(() => reveal(el));
          else observer.observe(el);
        }),
      );
    } else {
      els.forEach(reveal);
    }

    // Fail-open safety net.
    setTimeout(() => els.forEach(reveal), 4500);
  }

  /* ---------------------------------------------------------------------
   * 8. Custom cursor
   * Re-creates the original JS cursor: a solid dot tracking the pointer
   * exactly, and a ring that follows with easing and grows over interactive
   * elements. Only enabled on fine-pointer (mouse) devices.
   * ------------------------------------------------------------------- */
  function initCustomCursor() {
    if (!window.matchMedia || !window.matchMedia("(pointer: fine)").matches) {
      return; // touch / coarse pointer → keep the native cursor
    }

    const dot = el("div", "cursor-dot");
    const ring = el("div", "cursor-ring");
    document.body.appendChild(dot);
    document.body.appendChild(ring);
    document.documentElement.classList.add("custom-cursor-active");

    let mx = window.innerWidth / 2,
      my = window.innerHeight / 2;
    let rx = mx,
      ry = my;

    document.addEventListener(
      "mousemove",
      (e) => {
        mx = e.clientX;
        my = e.clientY;
        dot.style.left = mx + "px";
        dot.style.top = my + "px";
      },
      { passive: true },
    );

    // Ease the ring toward the pointer each frame.
    const loop = () => {
      rx += (mx - rx) * 0.18;
      ry += (my - ry) * 0.18;
      ring.style.left = rx + "px";
      ring.style.top = ry + "px";
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);

    // Grow the ring over clickable things.
    const interactive =
      'a, button, [role="button"], input, textarea, select, [data-case-card]';
    document.addEventListener("mouseover", (e) => {
      if (e.target.closest(interactive)) ring.classList.add("is-hovering");
    });
    document.addEventListener("mouseout", (e) => {
      if (e.target.closest(interactive)) ring.classList.remove("is-hovering");
    });

    // Hide when the pointer leaves the window; restore on return.
    document.addEventListener("mouseleave", () => {
      dot.style.opacity = ring.style.opacity = "0";
    });
    document.addEventListener("mouseenter", () => {
      dot.style.opacity = ring.style.opacity = "1";
    });
  }

  /* ---------------------------------------------------------------------
   * 2. Mobile navigation
   * Toggles the hamburger menu (button[aria-label="Open menu"]) and the
   * panel that contains nav[aria-label="Mobile navigation"].
   * ------------------------------------------------------------------- */
  function initMobileNav() {
    const toggle = document.querySelector('button[aria-label="Open menu"]');
    const nav = document.querySelector('nav[aria-label="Mobile navigation"]');
    if (!toggle || !nav) return;

    // The collapsible panel is the nav's nearest wrapping element.
    const panel = nav.closest("div") || nav;
    panel.setAttribute("data-mobile-panel", "");

    const setOpen = (open) => {
      panel.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    };
    setOpen(false);

    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    // Close when a link is tapped or when clicking outside the menu.
    panel.addEventListener("click", (e) => {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("click", (e) => {
      if (!panel.contains(e.target) && !toggle.contains(e.target)) {
        setOpen(false);
      }
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setOpen(false);
    });
  }

  /* ---------------------------------------------------------------------
   * 3. Copy-to-clipboard
   * The "Copy <email>" buttons carry the address in their aria-label.
   * ------------------------------------------------------------------- */
  function initClipboard() {
    const buttons = document.querySelectorAll('button[aria-label^="Copy "]');
    buttons.forEach((btn) => {
      btn.addEventListener("click", async () => {
        const value = btn.getAttribute("aria-label").replace(/^Copy\s+/, "");
        try {
          await navigator.clipboard.writeText(value);
          flash(btn, "Copied!");
        } catch (_) {
          flash(btn, "Press Ctrl+C");
        }
      });
    });
  }

  /* Brief, accessible confirmation bubble next to a button. */
  function flash(anchor, message) {
    const tip = document.createElement("span");
    tip.textContent = message;
    tip.setAttribute("role", "status");
    tip.style.cssText =
      "position:absolute;transform:translateY(-140%);background:#dc2626;" +
      "color:#fff;font-size:11px;padding:2px 6px;border-radius:4px;" +
      "white-space:nowrap;pointer-events:none;z-index:50;";
    anchor.style.position = anchor.style.position || "relative";
    anchor.appendChild(tip);
    setTimeout(() => tip.remove(), 1400);
  }

  /* ---------------------------------------------------------------------
   * 4. Scroll-scrubbed Batman canvas (the full-page background)
   * Re-creates the original GSAP ScrollTrigger effect with zero deps:
   * a fixed full-viewport <canvas> plays through 240 webp frames as the
   * page scrolls top→bottom (frame = scroll progress × 239). Frames are
   * lazy-loaded (first 30 eagerly, the rest on idle) and drawn cover-fit.
   * ------------------------------------------------------------------- */
  function initHeroBackground() {
    const canvas = document.querySelector("canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const FRAMES = 240;
    const src = (i) =>
      "assets/background/ezgif-frame-" +
      String(i + 1).padStart(3, "0") +
      ".webp";
    const imgs = new Array(FRAMES);
    const ready = new Array(FRAMES).fill(false);

    let dpr = 1;
    const resize = () => {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.floor(canvas.clientWidth * dpr);
      canvas.height = Math.floor(canvas.clientHeight * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      drawNow(Math.round(shown));
    };

    // Cover-fit draw of a single frame (falls back to nearest loaded frame).
    const drawNow = (i) => {
      let f = i;
      if (!ready[f]) {
        let lo = f,
          hi = f;
        while (lo >= 0 || hi < FRAMES) {
          if (lo >= 0 && ready[lo]) {
            f = lo;
            break;
          }
          if (hi < FRAMES && ready[hi]) {
            f = hi;
            break;
          }
          lo--;
          hi++;
        }
        if (!ready[f]) return;
      }
      const img = imgs[f];
      const cw = canvas.clientWidth,
        ch = canvas.clientHeight;
      const ir = img.naturalWidth / img.naturalHeight,
        cr = cw / ch;
      let dw, dh, dx, dy;
      if (ir > cr) {
        dh = ch;
        dw = ch * ir;
        dx = (cw - dw) / 2;
        dy = 0;
      } else {
        dw = cw;
        dh = cw / ir;
        dx = 0;
        dy = (ch - dh) / 2;
      }
      ctx.clearRect(0, 0, cw, ch);
      ctx.drawImage(img, dx, dy, dw, dh);
    };

    // Lazy frame loading: first 30 eagerly, the rest during idle time.
    const load = (i) => {
      const im = new Image();
      imgs[i] = im;
      im.onload = () => {
        ready[i] = true;
        if (Math.round(shown) === i) drawNow(i);
      };
      im.src = src(i);
    };
    for (let i = 0; i < 30 && i < FRAMES; i++) load(i);
    let h = 30;
    const idle = (deadline) => {
      const end = Math.min(h + 15, FRAMES);
      while (
        h < end &&
        !(deadline && !deadline.didTimeout && deadline.timeRemaining() < 4)
      )
        load(h++);
      if (h < FRAMES)
        "requestIdleCallback" in window
          ? requestIdleCallback(idle, { timeout: 4000 })
          : setTimeout(idle, 16);
    };
    "requestIdleCallback" in window
      ? requestIdleCallback(idle, { timeout: 4000 })
      : setTimeout(idle, 200);

    // Map scroll position → frame, with a touch of easing ("scrub").
    let target = 0,
      shown = 0,
      ticking = false;
    const reduce =
      window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const tick = () => {
      shown += (target - shown) * (reduce ? 1 : 0.2);
      const f = Math.round(shown);
      drawNow(f);
      if (!reduce && Math.abs(target - shown) > 0.25) {
        requestAnimationFrame(tick);
      } else {
        shown = target;
        drawNow(Math.round(shown));
        ticking = false;
      }
    };
    const onScroll = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const p = max > 0 ? window.scrollY / max : 0;
      target = Math.max(0, Math.min(FRAMES - 1, p * (FRAMES - 1)));
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(tick);
      }
    };

    window.addEventListener("resize", resize, { passive: true });
    window.addEventListener("scroll", onScroll, { passive: true });
    resize();
    onScroll();
  }

  /* ---------------------------------------------------------------------
   * 5. Smooth in-page scrolling
   * Anchor links are written as "index.html#section"; intercept same-page
   * ones so they scroll smoothly without a full reload.
   * ------------------------------------------------------------------- */
  function initSmoothScroll() {
    // Keep reloads at the top: don't let the browser restore a scrolled
    // position or a stale "#section" hash (that looked like a "redirect").
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";

    document.querySelectorAll('a[href*="#"]').forEach((link) => {
      link.addEventListener("click", (e) => {
        const hash = link.getAttribute("href").split("#")[1];
        if (!hash) return;
        const target = document.getElementById(hash);
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
        // NOTE: intentionally not writing location.hash — keeps the URL clean
        // so a page reload always starts at the hero instead of jumping.
      });
    });
  }

  /* ---------------------------------------------------------------------
   * 6. Skills tabs
   * Recovered category data lives in window.SKILLS (js/data.js). The tab
   * strip (role="tablist") switches the rendered skill grid. DOM anchors
   * are located by their initial content so the wiring survives class churn.
   * ------------------------------------------------------------------- */
  function initSkillTabs() {
    const data = window.SKILLS;
    const tablist = document.querySelector(
      '[role="tablist"][aria-label="AI Skills categories"]',
    );
    if (!data || !data.length || !tablist) return;

    const tabs = Array.from(tablist.querySelectorAll('button[role="tab"]'));
    const card = tablist.parentElement;
    const titleEl = byText(card, "h3", data[0].title);
    const modEl = Array.from(card.querySelectorAll("span")).find((s) =>
      s.textContent.trim().startsWith("MOD_"),
    );
    // The grid currently holding the first category's skill rows.
    const firstRow = byText(card, "span", data[0].skills[0]);
    const grid = firstRow && firstRow.closest("div").parentElement;
    if (!titleEl || !grid || tabs.length !== data.length) return;

    // Capture a pristine row template before we start mutating the grid.
    const rowTemplate = grid.firstElementChild.cloneNode(true);

    const select = (index) => {
      const cat = data[index];
      titleEl.textContent = cat.title;
      if (modEl)
        modEl.textContent = "MOD_" + String(index + 1).padStart(2, "0");

      grid.textContent = "";
      cat.skills.forEach((name) => {
        const row = rowTemplate.cloneNode(true);
        const spans = row.querySelectorAll("span");
        spans[spans.length - 1].textContent = name; // last span = skill name
        grid.appendChild(row);
      });

      tabs.forEach((tab, i) => {
        const active = i === index;
        tab.setAttribute("aria-selected", String(active));
        const bar = tab.querySelector("div");
        if (bar) bar.style.width = active ? "100%" : "0%";
      });
    };

    tabs.forEach((tab, i) => {
      tab.addEventListener("click", () => select(i));
    });
    select(0);
  }

  /* ---------------------------------------------------------------------
   * 7. Project carousel
   * window.PROJECTS (js/data.js) drives the featured viewer, the prev/next
   * navigation, the "x / total" counter, the category filter chips, and the
   * thumbnail strip. DOM anchors are again located by initial content.
   * ------------------------------------------------------------------- */
  function initProjectCarousel() {
    const projects = window.PROJECTS;
    const prev = document.querySelector(
      'button[aria-label="Previous project"]',
    );
    const next = document.querySelector('button[aria-label="Next project"]');
    if (!projects || !projects.length || !prev || !next) return;

    // The featured viewer is the nearest ancestor that also holds the title.
    let viewer = prev.parentElement;
    while (viewer && !byText(viewer, "h3", projects[0].title)) {
      viewer = viewer.parentElement;
    }
    if (!viewer) return;

    const imgEl = viewer.querySelector("img");
    const titleEl = byText(viewer, "h3", projects[0].title);
    const descEl = viewer.querySelector("p");
    const firstTag = byText(viewer, "button", projects[0].tags[0]);
    const tagsBox = firstTag && firstTag.parentElement;
    const tagTemplate = tagsBox && tagsBox.firstElementChild.cloneNode(true);
    // Counter: the element sitting between the prev and next buttons.
    const counterEl = prev.nextElementSibling;

    // Action row + button styling (the original "Open Case File" CTA). We reuse
    // its classes to render per-project "Source" / "Live Demo" links to the repos.
    const ctaBtn = byText(viewer, "button", "Open Case File");
    const actionRow = ctaBtn && ctaBtn.parentElement;
    const ctaClass = ctaBtn ? ctaBtn.className : "";

    // Thumbnails: map each "View case file: <title>" card to its project index.
    const thumbs = Array.from(
      document.querySelectorAll('[aria-label^="View case file:"]'),
    );
    const thumbByTitle = {};
    thumbs.forEach((t) => {
      const title = t
        .getAttribute("aria-label")
        .replace("View case file:", "")
        .trim();
      thumbByTitle[title] = t;
    });

    // Category filter chips (All + each category).
    const categories = ["All", ...new Set(projects.map((p) => p.category))];
    const filters = {};
    categories.forEach((c) => {
      const chip = byText(document.body, "button", c);
      if (chip) filters[c] = chip;
    });

    let view = projects.slice(); // current (possibly filtered) project list
    let pos = 0;

    const render = () => {
      const p = view[pos];
      if (!p) return;
      if (imgEl) {
        imgEl.src = p.image;
        imgEl.alt = p.title;
      }
      if (titleEl) titleEl.textContent = p.title;
      if (descEl) descEl.textContent = p.description;
      if (counterEl) {
        counterEl.textContent =
          String(pos + 1).padStart(2, "0") + " / " + view.length;
      }
      if (tagsBox && tagTemplate) {
        tagsBox.textContent = "";
        p.tags.forEach((tag) => {
          const node = tagTemplate.cloneNode(true);
          node.textContent = tag;
          tagsBox.appendChild(node);
        });
      }
      // Action row → real links to this project's GitHub repo (and live demo).
      if (actionRow) {
        actionRow.textContent = "";
        const mkLink = (label, href) => {
          const a = el("a", ctaClass, label);
          a.href = href;
          a.target = "_blank";
          a.rel = "noopener noreferrer";
          return a;
        };
        if (p.codeLink) actionRow.appendChild(mkLink("Source ↗", p.codeLink));
        if (p.demoLink)
          actionRow.appendChild(mkLink("Live Demo ↗", p.demoLink));
      }
      // Highlight the active thumbnail and bring it into view.
      thumbs.forEach((t) => {
        t.style.outline = "";
        t.style.opacity = "0.55";
      });
      const active = thumbByTitle[p.title];
      if (active) {
        active.style.outline = "2px solid #dc2626";
        active.style.opacity = "1";
        active.scrollIntoView({
          behavior: "smooth",
          inline: "center",
          block: "nearest",
        });
      }
    };

    const go = (delta) => {
      pos = (pos + delta + view.length) % view.length;
      render();
    };
    const jumpTo = (title) => {
      const i = view.findIndex((p) => p.title === title);
      if (i >= 0) {
        pos = i;
        render();
      }
    };
    const applyFilter = (cat) => {
      view =
        cat === "All"
          ? projects.slice()
          : projects.filter((p) => p.category === cat);
      pos = 0;
      // Show only thumbnails belonging to the active filter.
      thumbs.forEach((t) => {
        const title = t
          .getAttribute("aria-label")
          .replace("View case file:", "")
          .trim();
        const shown = view.some((p) => p.title === title);
        const card = t.closest("[data-case-card]") || t;
        card.style.display = shown ? "" : "none";
      });
      Object.entries(filters).forEach(([c, chip]) =>
        chip.setAttribute("aria-pressed", String(c === cat)),
      );
      render();
    };

    prev.addEventListener("click", () => go(-1));
    next.addEventListener("click", () => go(1));
    thumbs.forEach((t) => {
      const title = t
        .getAttribute("aria-label")
        .replace("View case file:", "")
        .trim();
      t.addEventListener("click", (e) => {
        e.preventDefault();
        jumpTo(title);
      });
    });
    Object.entries(filters).forEach(([cat, chip]) => {
      chip.addEventListener("click", () => applyFilter(cat));
    });

    render();
  }
})();
