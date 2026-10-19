/* St. Clare College - Paper Campus motion.
   Grammar: pop-up (layers rise like a pop-up book), parallax depth, slap-down sheets,
   envelope opening, re-deal, crowd bob. No per-frame layout reads. */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var G = window.gsap, ST = window.ScrollTrigger;
  var motion = !!(G && ST) && !reduce;
  if (motion) { root.classList.add("js"); G.registerPlugin(ST); }
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }

  /* ---------- menu: focus moves in, outside is inert, Esc closes ---------- */
  var mb = d.querySelector(".menu-btn"), menu = d.getElementById("menu");
  if (mb && menu) {
    var outside = $$("main, footer, .brand, .portal-quick, .skip");
    function setMenu(open) {
      d.body.classList.toggle("menu-open", open);
      mb.setAttribute("aria-expanded", open);
      mb.querySelector("span").textContent = open ? "Close" : "Menu";
      d.body.style.overflow = open ? "hidden" : "";
      outside.forEach(function (el) { if (open) el.setAttribute("inert", ""); else el.removeAttribute("inert"); });
      if (open) { var first = menu.querySelector("a"); if (first) setTimeout(function () { first.focus(); }, 60); }
    }
    mb.addEventListener("click", function () { setMenu(!d.body.classList.contains("menu-open")); });
    d.addEventListener("keydown", function (e) {
      if (!d.body.classList.contains("menu-open")) return;
      if (e.key === "Escape") { setMenu(false); mb.focus(); return; }
      if (e.key === "Tab") {
        var f = $$("a", menu).concat([mb]), i = f.indexOf(d.activeElement);
        if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
      }
    });
    window.addEventListener("resize", function () { if (window.innerWidth > 1120 && d.body.classList.contains("menu-open")) setMenu(false); });
  }

  /* ---------- tabs (level picker + requirement sheets) ---------- */
  $$("[role=tablist]").forEach(function (list) {
    var tabs = $$("[role=tab]", list);
    function select(tab, focus) {
      if (tab.getAttribute("aria-selected") === "true") { if (focus) tab.focus(); return; }
      tabs.forEach(function (t) {
        var on = t === tab; t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1;
        var p = d.getElementById(t.getAttribute("aria-controls")); if (p) p.hidden = !on;
      });
      if (focus) tab.focus();
      var panel = d.getElementById(tab.getAttribute("aria-controls"));
      if (panel && motion) deal(panel);
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, n = k === "ArrowRight" || k === "ArrowDown" ? i + 1 : k === "ArrowLeft" || k === "ArrowUp" ? i - 1 : k === "Home" ? 0 : k === "End" ? tabs.length - 1 : null;
        if (n === null) return; e.preventDefault(); select(tabs[(n + tabs.length) % tabs.length], true);
      });
    });
    function fromHash() { var h = location.hash.slice(1), t = h && list.querySelector('[data-hash="' + h + '"]'); if (t) select(t); }
    fromHash(); window.addEventListener("hashchange", fromHash);
  });
  function deal(panel) {
    G.fromTo($$(".rows li, .checklist li", panel), { x: 60, rotation: 3, opacity: 0 }, { x: 0, rotation: 0, opacity: 1, duration: .6, ease: "expo.out", stagger: .04 });
    G.fromTo($$(".deal-figs > *", panel), { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .8, ease: "back.out(1.7)", stagger: .07, delay: .08 });
  }

  /* ---------- ribbon pause ---------- */
  $$(".ribbon").forEach(function (r) {
    var b = r.querySelector(".pause"); if (!b) return;
    b.addEventListener("click", function () {
      var p = r.classList.toggle("paused");
      b.setAttribute("aria-label", p ? "Play the programme ribbon" : "Pause the programme ribbon");
      b.innerHTML = p ? '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3 1l11 7-11 7z"/></svg>' : '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3 1h4v14H3zM9 1h4v14H9z"/></svg>';
    });
  });

  /* ---------- contact form -> email draft ---------- */
  var form = d.querySelector("[data-mailto]");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form), lines = [];
    f.forEach(function (v, k) { if (k !== "subject") lines.push(k + ": " + v); });
    location.href = "mailto:" + form.getAttribute("data-mailto") + "?subject=" + encodeURIComponent(f.get("subject") || "Website inquiry") + "&body=" + encodeURIComponent(lines.join("\n"));
    var st = form.querySelector(".form-status");
    if (st) st.textContent = "Your email app should open with this message. If it doesn't, email " + form.getAttribute("data-mailto") + " or call (02) 8232-4483.";
  });
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  if (!motion) return;

  /* ---------- smooth scroll ---------- */
  if (window.Lenis && window.matchMedia("(pointer: fine)").matches) {
    var lenis = new window.Lenis({ lerp: .11 });
    lenis.on("scroll", ST.update);
    G.ticker.add(function (t) { lenis.raf(t * 1000); });
    G.ticker.lagSmoothing(0);
    $$('a[href^="#"]').forEach(function (a) { a.addEventListener("click", function (e) { var t = d.querySelector(a.getAttribute("href")); if (t) { e.preventDefault(); lenis.scrollTo(t, { offset: -90 }); } }); });
  }
  function has(sel, c) { return (c || d).querySelector(sel); }

  /* ---------- hero: pop-up book intro + depth parallax ---------- */
  var hero = has(".hero") || has(".phero");
  if (hero) {
    var layers = $$("[data-depth]", hero);
    var tl = G.timeline({ defaults: { ease: "back.out(1.4)" } });
    if (layers.length) tl.from(layers, { yPercent: 18, opacity: 0, duration: 1.1, stagger: .09, transformOrigin: "50% 100%" });
    var copy = $$(".crumbs, h1 .l, .lede, .actions > *", hero);
    if (copy.length) tl.from(copy, { y: 40, opacity: 0, rotation: -2, duration: .9, ease: "expo.out", stagger: .08 }, layers.length ? "-=.9" : 0);
    var peeps = $$(".crowd .peep", hero);
    if (peeps.length) tl.from(peeps, { yPercent: 70, opacity: 0, duration: .8, ease: "back.out(2)", stagger: { each: .06, from: "random" } }, "-=.7");
    var seal = has(".hero-seal", hero);
    if (seal) tl.from(seal, { scale: 2, rotation: -60, opacity: 0, duration: .6, ease: "power4.in" }, "-=.5");
    setTimeout(function () { if (tl.progress() < 1) tl.progress(1); }, 4500); /* failsafe for throttled tabs */
    /* scroll + pointer parallax move whole composited elements (the svg, the crowd), never the filtered layers */
    var scene = has(".scene", hero), crowdEl = has(".crowd", hero);
    if (scene) G.to(scene, { yPercent: 8, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
    if (crowdEl) G.to(crowdEl, { yPercent: -6, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
    if (window.matchMedia("(pointer: fine)").matches && scene) {
      var sx = G.quickTo(scene, "x", { duration: 1, ease: "power3" }), cx = crowdEl ? G.quickTo(crowdEl, "x", { duration: .8, ease: "power3" }) : null;
      hero.addEventListener("pointermove", function (e) { var nx = e.clientX / window.innerWidth - .5; sx(-nx * 14); if (cx) cx(-nx * 30); });
    }
    /* crowd idles: gentle bobs, paused off-screen by ScrollTrigger toggle */
    if (peeps.length) {
      var bob = G.to(peeps, { y: -8, rotation: function (i) { return i % 2 ? 2 : -2; }, duration: function () { return G.utils.random(1.2, 2); }, ease: "sine.inOut", yoyo: true, repeat: -1, stagger: { each: .2, from: "random" }, paused: true, delay: 2 });
      ST.create({ trigger: hero, start: "top bottom", end: "bottom top", onToggle: function (s) { s.isActive ? bob.play() : bob.pause(); } });
    }
  }

  /* ---------- reveals ---------- */
  ST.batch("[data-pop]", { start: "top 88%", onEnter: function (els) {
    G.to(els, { opacity: 1, y: 0, scale: 1, rotation: function (i, el) { return parseFloat(getComputedStyle(el).getPropertyValue("--rest")) || 0; }, duration: .9, ease: "back.out(1.5)", stagger: .08, onStart: function () { els.forEach(function (e) { e.style.willChange = "transform"; }); }, onComplete: function () { els.forEach(function (e) { e.style.willChange = ""; }); } });
  } });
  ST.batch("[data-rise]", { start: "top 90%", onEnter: function (els) {
    G.to(els, { opacity: 1, y: 0, duration: 1, ease: "expo.out", stagger: .06 });
  } });
  $$(".band h2, .closer h2").forEach(function (h) {
    G.from(h, { y: 50, opacity: 0, rotation: -1.5, duration: 1, ease: "expo.out", scrollTrigger: { trigger: h, start: "top 88%" } });
  });

  /* ---------- envelope opens, documents slide out, checklist ticks ---------- */
  var env = has(".env");
  if (env) {
    var etl = G.timeline({ scrollTrigger: { trigger: env, start: "top 85%", end: "bottom 45%", scrub: .8 } });
    etl.fromTo(env.querySelector(".env-flap"), { rotationX: 0, transformPerspective: 800 }, { rotationX: 180, transformPerspective: 800, ease: "none", duration: .3 })
       .set(env.querySelector(".env-flap"), { zIndex: 1 })
       .fromTo($$(".env-doc", env), { yPercent: 8 }, { yPercent: function (i) { return -22 - i * 10; }, rotation: function (i) { return [-4, 3, -1][i]; }, ease: "power2.out", stagger: .08, duration: .5 });
    $$(".checklist li").forEach(function (li) {
      G.fromTo(li, { "--tick": 0 }, { "--tick": 1, duration: .35, ease: "back.out(3)", scrollTrigger: { trigger: li, start: "top 82%" } });
    });
  }
  $$(".ticket").forEach(function (t, i) {
    G.from(t, { y: 80, rotation: i % 2 ? 5 : -5, opacity: 0, duration: 1, ease: "back.out(1.4)", scrollTrigger: { trigger: t, start: "top 86%" } });
  });

  /* ---------- equation tiles slap down ---------- */
  var eq = has(".eq");
  if (eq) G.from(eq.children, { y: -80, rotation: function (i) { return i % 2 ? 0 : G.utils.random(-14, 14); }, opacity: 0, duration: .7, ease: "bounce.out", stagger: .1, scrollTrigger: { trigger: eq, start: "top 82%" } });
  $$(".print, .label").forEach(function (p, i) {
    G.from(p, { y: 90, rotation: i % 2 ? 10 : -10, opacity: 0, duration: 1, ease: "back.out(1.3)", scrollTrigger: { trigger: p, start: "top 88%" } });
  });

  /* ---------- bunting drops on its line ---------- */
  $$(".flags").forEach(function (fl) {
    G.from(fl.children, { yPercent: -110, opacity: 0, duration: 1, ease: "elastic.out(1, .45)", stagger: .06, scrollTrigger: { trigger: fl, start: "top 82%" }, clearProps: "transform,opacity" });
  });
  $$(".keys").forEach(function (k) {
    G.from(k.children, { y: -60, opacity: 0, duration: 1.1, ease: "elastic.out(1, .5)", stagger: .07, scrollTrigger: { trigger: k, start: "top 86%" }, clearProps: "transform,opacity" });
  });

  /* ---------- flame flicker ---------- */
  $$(".flame").forEach(function (fl) {
    var tws = $$("path", fl).map(function (p, i) { return G.to(p, { scaleY: G.utils.random(1.05, 1.12), scaleX: G.utils.random(.92, .97), duration: G.utils.random(.4, .65), ease: "sine.inOut", yoyo: true, repeat: -1, delay: i * .12, paused: true }); });
    ST.create({ trigger: fl, start: "top bottom", end: "bottom top", onToggle: function (s) { tws.forEach(function (t) { s.isActive ? t.play() : t.pause(); }); } });
  });

  /* ---------- closer crowd pops up ---------- */
  var cc = $$(".closer .peep");
  if (cc.length) G.from(cc, { yPercent: 90, duration: .9, ease: "back.out(2)", stagger: { each: .05, from: "center" }, scrollTrigger: { trigger: ".closer .crowd", start: "top 95%" } });

  window.addEventListener("load", function () { ST.refresh(); });
})();
