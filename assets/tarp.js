/* St. Clare College - Campus Tarpaulin motion.
   Grammar: unfurl (clip drop), sway (spring), flap (per character), pin-drop, stamp. */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var G = window.gsap, ST = window.ScrollTrigger;
  var motion = !!(G && ST) && !reduce;
  if (motion) { root.classList.add("js"); G.registerPlugin(ST); }

  /* ---------- menu ---------- */
  var mb = d.querySelector(".menu-btn");
  if (mb) {
    function setMenu(open) { d.body.classList.toggle("menu-open", open); mb.setAttribute("aria-expanded", open); mb.querySelector("span").textContent = open ? "Close" : "Menu"; d.body.style.overflow = open ? "hidden" : ""; }
    mb.addEventListener("click", function () { setMenu(!d.body.classList.contains("menu-open")); });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape" && d.body.classList.contains("menu-open")) { setMenu(false); mb.focus(); } });
  }

  /* ---------- tabs (level picker + requirement envelopes) ---------- */
  d.querySelectorAll("[role=tablist]").forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll("[role=tab]"));
    function select(tab, focus) {
      var prev = tabs.filter(function (t) { return t.getAttribute("aria-selected") === "true"; })[0];
      if (prev === tab) return;
      var oldP = prev && d.getElementById(prev.getAttribute("aria-controls"));
      var newP = d.getElementById(tab.getAttribute("aria-controls"));
      tabs.forEach(function (t) { var on = t === tab; t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1; });
      if (focus) tab.focus();
      if (oldP) oldP.hidden = true;
      if (newP) { newP.hidden = false; if (motion) deal(newP); }
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, n = k === "ArrowRight" || k === "ArrowDown" ? i + 1 : k === "ArrowLeft" || k === "ArrowUp" ? i - 1 : k === "Home" ? 0 : k === "End" ? tabs.length - 1 : null;
        if (n === null) return; e.preventDefault(); select(tabs[(n + tabs.length) % tabs.length], true);
      });
    });
    function fromHash() { var h = location.hash.slice(1); var t = h && list.querySelector('[data-hash="' + h + '"]'); if (t) select(t); }
    fromHash(); window.addEventListener("hashchange", fromHash);
  });
  /* re-deal: rows fly in like dealt cards, figures pop up */
  function deal(panel) {
    var rows = panel.querySelectorAll(".rows li, .checklist li");
    var figs = panel.querySelectorAll(".deal-figs img, .rubber, .note-card");
    G.fromTo(rows, { x: 80, rotation: 4, opacity: 0 }, { x: 0, rotation: 0, opacity: 1, duration: .7, ease: "expo.out", stagger: .045 });
    G.fromTo(figs, { y: 90, opacity: 0 }, { y: 0, opacity: 1, duration: .9, ease: "back.out(1.6)", stagger: .08, delay: .1 });
  }

  /* ---------- split-flap ticker ---------- */
  var CH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-&. ";
  d.querySelectorAll("[data-flaps]").forEach(function (box) {
    var words = JSON.parse(box.getAttribute("data-flaps")), len = parseInt(box.getAttribute("data-len"), 10) || 18;
    var cells = [];
    for (var i = 0; i < len; i++) { var s = d.createElement("span"); s.setAttribute("aria-hidden", "true"); s.textContent = " "; box.appendChild(s); cells.push(s); }
    var live = d.createElement("span"); live.className = "sr-only"; box.parentNode.appendChild(live);
    var w = 0, paused = false, timer;
    function show(word) {
      word = word.toUpperCase().slice(0, len); while (word.length < len) word += " ";
      live.textContent = word.trim();
      cells.forEach(function (c, i) {
        var target = word[i];
        if (reduce) { c.textContent = target; return; }
        var steps = 2 + Math.floor(Math.random() * 6), n = 0;
        setTimeout(function tick() {
          c.classList.remove("flip"); void c.offsetWidth; c.classList.add("flip");
          c.textContent = n < steps ? CH[Math.floor(Math.random() * CH.length)] : target;
          if (n++ < steps) setTimeout(tick, 70);
        }, i * 28);
      });
    }
    function loop() { if (!paused) show(words[w++ % words.length]); timer = setTimeout(loop, 3200); }
    loop();
    var pb = box.parentNode.querySelector(".mq-btn");
    if (pb) pb.addEventListener("click", function () { paused = !paused; pb.setAttribute("aria-label", paused ? "Resume programme ticker" : "Pause programme ticker"); pb.innerHTML = paused ? '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3 1l11 7-11 7z"/></svg>' : '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3 1h4v14H3zM9 1h4v14H9z"/></svg>'; });
    if (reduce) { paused = true; }
  });

  /* ---------- contact form -> email draft ---------- */
  var form = d.querySelector("[data-mailto]");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form), lines = [];
    f.forEach(function (v, k) { if (k !== "subject") lines.push(k + ": " + v); });
    location.href = "mailto:" + form.getAttribute("data-mailto") + "?subject=" + encodeURIComponent(f.get("subject") || "Website inquiry") + "&body=" + encodeURIComponent(lines.join("\n"));
    var st = form.querySelector(".form-status"); if (st) st.textContent = "Your email app should open with this message. If it doesn't, email " + form.getAttribute("data-mailto") + " or call (02) 8232-4483.";
  });
  d.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  if (!motion) return;

  /* ---------- smooth scroll (Lenis) ---------- */
  var lenis = null;
  if (window.Lenis) {
    lenis = new window.Lenis({ lerp: .11, wheelMultiplier: 1 });
    lenis.on("scroll", ST.update);
    G.ticker.add(function (t) { lenis.raf(t * 1000); });
    G.ticker.lagSmoothing(0);
    d.querySelectorAll('a[href^="#"]').forEach(function (a) { a.addEventListener("click", function (e) { var t = d.querySelector(a.getAttribute("href")); if (t) { e.preventDefault(); lenis.scrollTo(t, { offset: -90 }); } }); });
  }

  /* ---------- spring sway: hung vinyl reacts to scroll velocity + pointer ---------- */
  var hung = Array.prototype.slice.call(d.querySelectorAll(".tarp, .flag, .key, .hang")).map(function (el, i) {
    var big = el.classList.contains("tarp"), tag = el.classList.contains("hang");
    return { el: el, a: 0, v: tag ? 1.2 : 0, k: big ? 0.018 : 0.03, c: big ? 0.07 : tag ? 0.035 : 0.05, m: big ? 0.35 : 1, ph: i * 0.7, vis: false };
  });
  if ("IntersectionObserver" in window) {
    var hio = new IntersectionObserver(function (es) { es.forEach(function (e) { hung.forEach(function (h) { if (h.el === e.target) h.vis = e.isIntersecting; }); }); });
    hung.forEach(function (h) { hio.observe(h.el); });
  }
  var lastY = window.scrollY, scrollV = 0, px = -1, pvx = 0, lastPx = -1, py = -1;
  window.addEventListener("pointermove", function (e) { px = e.clientX; py = e.clientY; }, { passive: true });
  var t0 = 0;
  G.ticker.add(function () {
    t0 += 1;
    var y = window.scrollY; scrollV = scrollV * 0.8 + (y - lastY) * 0.2; lastY = y;
    pvx = lastPx < 0 ? 0 : px - lastPx; lastPx = px;
    hung.forEach(function (h) {
      if (!h.vis) return;
      var f = -h.k * h.a - h.c * h.v;                      /* spring + damping */
      f += Math.max(-6, Math.min(6, scrollV)) * 0.012 * h.m; /* scroll gust */
      f += Math.sin(t0 * 0.012 + h.ph) * 0.004 * h.m;       /* breeze */
      if (px >= 0) { var r = h.el.getBoundingClientRect(); if (py > r.top && py < r.bottom && px > r.left && px < r.right) f += pvx * 0.02 * h.m; }
      h.v += f; h.a += h.v;
      h.a = Math.max(-7, Math.min(7, h.a));
      h.el.style.setProperty("--sway", h.a.toFixed(3) + "deg");
    });
  });

  /* ---------- hero intro ---------- */
  var hero = d.querySelector(".hero, .phero");
  if (hero) {
    var tl = G.timeline({ defaults: { ease: "expo.out" } });
    var tarp = hero.querySelector(".tarp");
    tl.from(hero.querySelector(".pipe"), { scaleX: 0, transformOrigin: "left", duration: .9 })
      .fromTo(tarp, { clipPath: "inset(0 0 100% 0)" }, { clipPath: "inset(0 0 0% 0)", duration: 1.3, clearProps: "clipPath" }, "-=.45")
      .from(hero.querySelectorAll(".tie"), { scaleY: 0, transformOrigin: "top", duration: .5, stagger: .06 }, "<")
      .from(hero.querySelectorAll("h1 .l > span"), { yPercent: 110, duration: 1.1, stagger: .09 }, "-=.9")
      .from(hero.querySelectorAll(".lede, .crumbs"), { y: 24, opacity: 0, duration: .9 }, "-=.7")
      .from(hero.querySelectorAll(".hero-actions > *, .hang"), { rotation: -28, y: -30, opacity: 0, transformOrigin: "16px 50%", duration: 1.2, ease: "elastic.out(1, .45)", stagger: .1, clearProps: "transform" }, "-=.6")
      .from(hero.querySelectorAll(".stamp"), { scale: 2.2, opacity: 0, rotation: -40, duration: .5, ease: "power4.in" }, "-=1")
      .to(hero.querySelectorAll(".stamp"), { scale: 1.06, duration: .08, yoyo: true, repeat: 1 })
      .from(hero.querySelectorAll(".hero-vr, .cut"), { yPercent: 40, opacity: 0, duration: 1.4 }, "-=1.1");
    hung.forEach(function (h) { if (h.el === tarp) h.v = 0.6; });
    setTimeout(function () { if (tl.progress() < 1) tl.progress(1); }, 4500); /* failsafe for throttled tabs */
    /* scroll: photo drifts, tarp lifts slightly */
    var ph = hero.querySelector(".hero-photo img, .phero-photo img");
    if (ph) G.to(ph, { yPercent: 12, scale: 1.08, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
    var vr = hero.querySelector(".hero-vr");
    if (vr) G.to(vr, { yPercent: -14, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
  }

  /* ---------- reveals ---------- */
  G.utils.toArray("[data-unfurl]").forEach(function (el) {
    G.to(el, { clipPath: "inset(0 0 0% 0)", duration: 1.3, ease: "expo.out", clearProps: "clipPath", scrollTrigger: { trigger: el, start: "top 85%" },
      onComplete: function () { hung.forEach(function (h) { if (h.el === el) h.v = 0.5; }); } });
  });
  G.utils.toArray("[data-rise]").forEach(function (el) {
    G.to(el, { opacity: 1, y: 0, duration: 1.1, ease: "expo.out", scrollTrigger: { trigger: el, start: "top 88%" } });
  });
  ST.batch("[data-pin]", { start: "top 90%", onEnter: function (els) {
    G.to(els, { opacity: 1, y: 0, rotation: function (i, el) { return parseFloat(getComputedStyle(el).getPropertyValue("--r")) || 0; }, duration: .9, ease: "bounce.out", stagger: .09 });
  } });
  ST.batch("[data-stamp]", { start: "top 85%", onEnter: function (els) {
    G.to(els, { opacity: 1, scale: 1, rotation: -6, duration: .45, ease: "power4.in", stagger: .12 });
  } });
  /* big headings: letters rise as the section enters */
  G.utils.toArray("[data-letters]").forEach(function (h) {
    var txt = h.textContent; h.setAttribute("aria-label", txt); h.textContent = "";
    txt.split(" ").forEach(function (word, wi) {
      var w = d.createElement("span"); w.style.display = "inline-block"; w.style.whiteSpace = "nowrap"; w.setAttribute("aria-hidden", "true");
      word.split("").forEach(function (ch) { var s = d.createElement("span"); s.textContent = ch; s.style.display = "inline-block"; w.appendChild(s); });
      h.appendChild(w); if (wi < txt.split(" ").length - 1) h.appendChild(d.createTextNode(" "));
    });
    G.from(h.querySelectorAll("span span"), { yPercent: 100, rotation: function () { return G.utils.random(-12, 12); }, opacity: 0, duration: .9, ease: "back.out(2)", stagger: .025, scrollTrigger: { trigger: h, start: "top 85%" } });
  });

  /* ---------- facts banner: scrubbed sideways ---------- */
  G.utils.toArray(".facttrack").forEach(function (tr) {
    G.fromTo(tr, { x: function () { return window.innerWidth * 0.15; } }, { x: function () { return -(tr.scrollWidth - window.innerWidth * 0.85); }, ease: "none",
      scrollTrigger: { trigger: tr.parentNode, start: "top bottom", end: "bottom top", scrub: .6, invalidateOnRefresh: true } });
  });

  /* ---------- envelope opens, documents slide out, checklist ticks ---------- */
  var env = d.querySelector(".env");
  if (env) {
    var etl = G.timeline({ scrollTrigger: { trigger: ".route", start: "top 70%", end: "center 45%", scrub: .8 } });
    etl.fromTo(env.querySelector(".env-flap"), { rotationX: 0, transformPerspective: 800 }, { rotationX: 180, transformPerspective: 800, ease: "none", duration: .3 })
       .set(env.querySelector(".env-flap"), { zIndex: 1 })
       .fromTo(env.querySelectorAll(".env-doc"), { yPercent: 40 }, { yPercent: function (i) { return -22 - i * 10; }, rotation: function (i) { return [-4, 3, -1][i]; }, ease: "power2.out", stagger: .08, duration: .5 });
    G.utils.toArray(".route .checklist li").forEach(function (li, i) {
      G.fromTo(li, { "--tick": 0 }, { "--tick": 1, duration: .35, ease: "back.out(3)", scrollTrigger: { trigger: li, start: "top 80%" }, delay: i * .03 });
    });
  }

  /* ---------- tickets: tear in with a stamp ---------- */
  G.utils.toArray(".ticket").forEach(function (t, i) {
    G.from(t, { x: i % 2 ? 120 : -120, rotation: i % 2 ? 6 : -6, opacity: 0, duration: 1.1, ease: "expo.out", scrollTrigger: { trigger: t, start: "top 85%" } });
    var w = t.querySelector(".where"); if (w) G.from(w, { scale: 2, opacity: 0, duration: .4, ease: "power4.in", scrollTrigger: { trigger: t, start: "top 70%" } });
  });

  /* ---------- equation slams ---------- */
  var eq = d.querySelector(".eq");
  if (eq) G.from(eq.children, { y: 120, rotation: function (i) { return i % 2 ? 0 : -10; }, opacity: 0, duration: 1, ease: "back.out(1.4)", stagger: .12, scrollTrigger: { trigger: eq, start: "top 80%" } });

  /* ---------- bunting drops on its line ---------- */
  G.utils.toArray(".flags").forEach(function (fl) {
    G.from(fl.children, { yPercent: -120, rotation: function () { return G.utils.random(-25, 25); }, duration: 1.2, ease: "elastic.out(1, .4)", stagger: .07, clearProps: "transform", scrollTrigger: { trigger: fl, start: "top 80%" } });
  });
  G.utils.toArray(".keys").forEach(function (k) {
    G.from(k.children, { yPercent: -60, opacity: 0, rotation: function () { return G.utils.random(-14, 14); }, duration: 1.3, ease: "elastic.out(1, .45)", stagger: .08, clearProps: "transform,opacity", scrollTrigger: { trigger: k, start: "top 85%" } });
  });

  /* ---------- flame flicker (flat paper layers) ---------- */
  d.querySelectorAll(".flame path").forEach(function (p, i) {
    G.to(p, { scaleY: G.utils.random(1.06, 1.14), scaleX: G.utils.random(.9, .96), skewX: G.utils.random(-4, 4), duration: G.utils.random(.35, .6), ease: "sine.inOut", yoyo: true, repeat: -1, delay: i * .12 });
  });

  /* ---------- closer: giant word scales in on scrub ---------- */
  var cl = d.querySelector(".closer h2");
  if (cl) G.fromTo(cl, { scale: .7, opacity: .2 }, { scale: 1, opacity: 1, ease: "none", scrollTrigger: { trigger: cl, start: "top 95%", end: "top 40%", scrub: true } });
  var fw = d.querySelector(".foot-word");
  if (fw) G.from(fw, { yPercent: 70, ease: "none", scrollTrigger: { trigger: ".foot", start: "top bottom", end: "bottom bottom", scrub: true } });

  /* ---------- years stamp in ---------- */
  G.utils.toArray(".yr b").forEach(function (b) {
    G.from(b, { scale: 1.8, opacity: 0, rotation: -10, duration: .45, ease: "power4.in", scrollTrigger: { trigger: b, start: "top 82%" } });
  });

  /* ---------- board rows slide in ---------- */
  ST.batch(".board details, .files li, .ev, .faq details, .rows li", { start: "top 92%", onEnter: function (els) {
    G.from(els, { x: -40, opacity: 0, duration: .8, ease: "expo.out", stagger: .05 });
  } });

  window.addEventListener("load", function () { ST.refresh(); });
})();
