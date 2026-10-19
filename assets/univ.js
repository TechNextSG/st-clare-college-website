/* St. Clare College - "Crimson University" interactions.
   Transparent masthead over the hero (solid + hide-on-scroll-down after it), hero slideshow, GSAP ScrollTrigger reveals,
   split-line headline entrances, counters, magnetic + ripple buttons, tabs, mobile menu, lite YouTube, lightbox, mailto form.
   Everything degrades to fully visible content without JS, without GSAP, and under prefers-reduced-motion. */
(function () {
  "use strict";
  var d = document, root = d.documentElement, w = window;
  var reduce = w.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = w.matchMedia("(hover: hover) and (pointer: fine)").matches;
  root.classList.add("js");
  /* ---------- intro: once per browser session; click to skip ---------- */
  var intro = d.querySelector(".intro"), introOn = !!intro && !reduce && !root.classList.contains("no-intro");
  if (introOn) {
    try { sessionStorage.setItem("sc-intro", "1"); } catch (e) {}
    intro.addEventListener("click", function () { intro.classList.add("skip"); });
    intro.addEventListener("animationend", function (e) { if (e.target === intro) intro.remove(); });
  }
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }

  /* ---------- masthead ---------- */
  var mh = d.querySelector(".masthead"), hero = d.querySelector(".hero, .ph"), lastY = 0;
  function onScroll() {
    if (!mh) return;
    var y = w.scrollY, edge = hero ? Math.max(80, hero.offsetHeight - 120) : 10;
    mh.classList.toggle("solid", !hero || y > 40);
    mh.classList.toggle("hide", y > edge && y > lastY + 4 && !d.body.classList.contains("menu-open"));
    if (y < lastY - 4 || y < edge) mh.classList.remove("hide");
    lastY = y;
  }
  w.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  d.addEventListener("focusin", function (e) { if (mh && mh.contains(e.target)) mh.classList.remove("hide"); });

  /* ---------- mobile menu: focus in, outside inert, Esc closes, Tab wraps ---------- */
  var mb = d.querySelector(".menu-btn"), nav = d.getElementById("nav");
  if (mb && nav) {
    var outside = $$("main, footer, .util, .brand, .skip");
    var setMenu = function (open) {
      d.body.classList.toggle("menu-open", open);
      mb.setAttribute("aria-expanded", open);
      mb.querySelector("span").textContent = open ? "Close" : "Menu";
      d.body.style.overflow = open ? "hidden" : "";
      outside.forEach(function (el) { open ? el.setAttribute("inert", "") : el.removeAttribute("inert"); });
      if (open) setTimeout(function () { var a = nav.querySelector("a"); if (a) a.focus(); }, 60);
    };
    mb.addEventListener("click", function () { setMenu(!d.body.classList.contains("menu-open")); });
    d.addEventListener("keydown", function (e) {
      if (!d.body.classList.contains("menu-open")) return;
      if (e.key === "Escape") { setMenu(false); mb.focus(); return; }
      if (e.key === "Tab") {
        var f = $$("a", nav).concat([mb]), i = f.indexOf(d.activeElement);
        if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
      }
    });
    w.addEventListener("resize", function () { if (w.innerWidth > 1100 && d.body.classList.contains("menu-open")) setMenu(false); });
  }

  /* ---------- home hero slideshow ---------- */
  var slides = $$(".slide"), dots = $$(".dots button"), cap = d.querySelector(".slide-cap"), cur = 0, timer, paused = reduce;
  function loadSlide(n) { var im = slides.length && slides[(n + slides.length) % slides.length].querySelector("img[data-src]"); if (!im) return; if (im.dataset.srcset) im.srcset = im.dataset.srcset; im.src = im.dataset.src; im.removeAttribute("data-src"); im.removeAttribute("data-srcset"); }
  function show(n) {
    if (!slides.length) return;
    cur = (n + slides.length) % slides.length;
    slides.forEach(function (s, i) { s.classList.toggle("on", i === cur); });
    dots.forEach(function (b, i) { b.classList.toggle("on", i === cur); b.setAttribute("aria-current", i === cur ? "true" : "false"); var bar = b.querySelector("i"); if (bar) { bar.style.animation = "none"; void bar.offsetWidth; bar.style.animation = ""; } });
    if (cap) cap.textContent = slides[cur].getAttribute("data-cap") || "";
    loadSlide(cur); loadSlide(cur + 1);
    clearTimeout(timer); if (!reduce && !paused) timer = setTimeout(function () { show(cur + 1); }, 7000);
  }
  if (slides.length) {
    dots.forEach(function (b, i) { b.addEventListener("click", function () { if (cap) cap.setAttribute("aria-live", "polite"); show(i); }); });
    var pb = d.querySelector(".slide-pause");
    if (pb) { if (paused) { pb.setAttribute("aria-pressed", "true"); pb.setAttribute("aria-label", "Play slideshow"); }
      pb.addEventListener("click", function () { paused = !paused; pb.setAttribute("aria-pressed", paused); pb.setAttribute("aria-label", paused ? "Play slideshow" : "Pause slideshow"); d.querySelector(".hero").classList.toggle("paused", paused); show(cur); }); }
    show(0);
    d.addEventListener("visibilitychange", function () { if (d.hidden) clearTimeout(timer); else show(cur); });
  }

  /* ---------- home hero: photo tilts toward the pointer; gentle sway on touch / idle ---------- */
  var hh = d.querySelector(".hero-home");
  if (hh && !reduce) {
    if (!fine) hh.classList.add("idle");
    else {
      hh.addEventListener("pointermove", function (e) {
        var r = hh.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        hh.style.setProperty("--ry", (x * 7).toFixed(2) + "deg");
        hh.style.setProperty("--rx", (-y * 5).toFixed(2) + "deg");
      });
      hh.addEventListener("pointerleave", function () {
        hh.style.setProperty("--ry", "0deg"); hh.style.setProperty("--rx", "0deg");
      });
    }
  }

  /* ---------- buttons: ripple + magnetic ---------- */
  $$(".btn").forEach(function (b) {
    b.addEventListener("pointerdown", function (e) {
      if (reduce) return;
      var r = b.getBoundingClientRect(), s = Math.max(r.width, r.height), sp = d.createElement("span");
      sp.className = "ripple"; sp.style.width = sp.style.height = s + "px";
      sp.style.left = (e.clientX - r.left - s / 2) + "px"; sp.style.top = (e.clientY - r.top - s / 2) + "px";
      b.appendChild(sp); setTimeout(function () { sp.remove(); }, 650);
    });
    if (!fine || reduce) return;
    b.addEventListener("pointermove", function (e) {
      var r = b.getBoundingClientRect(), x = (e.clientX - r.left - r.width / 2) / r.width, y = (e.clientY - r.top - r.height / 2) / r.height;
      b.style.transform = "translate(" + (x * 8).toFixed(1) + "px," + (y * 6).toFixed(1) + "px)";
    });
    b.addEventListener("pointerleave", function () { b.style.transform = ""; });
  });

  /* ---------- tabs ---------- */
  $$("[role=tablist]").forEach(function (list) {
    var tabs = $$("[role=tab]", list);
    function select(tab, focus) {
      tabs.forEach(function (t) { var on = t === tab; t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1; var p = d.getElementById(t.getAttribute("aria-controls")); if (p) p.hidden = !on; });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, n = k === "ArrowRight" ? i + 1 : k === "ArrowLeft" ? i - 1 : k === "Home" ? 0 : k === "End" ? tabs.length - 1 : null;
        if (n === null) return; e.preventDefault(); select(tabs[(n + tabs.length) % tabs.length], true);
      });
    });
    function fromHash() { var h = location.hash.slice(1), t = h && list.querySelector('[data-hash="' + h + '"]'); if (t) select(t); }
    select(tabs.filter(function (t) { return t.getAttribute("aria-selected") === "true"; })[0] || tabs[0]);
    fromHash(); w.addEventListener("hashchange", fromHash);
  });

  /* ---------- counters ---------- */
  function count(el) {
    var end = parseFloat(el.getAttribute("data-count")), suf = el.getAttribute("data-suffix") || "", t0 = null, dur = 1400;
    if (reduce || isNaN(end)) { el.textContent = end + suf; return; }
    function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 4); el.textContent = Math.round(end * e) + suf; if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }

  /* ---------- motion ---------- */
  var rv = $$(".rv"), imgs = $$(".rv-img"), counters = $$("[data-count]");
  function showAll() { $$(".sec-head h2").forEach(function (h2) { h2.classList.add("drawn"); }); rv.forEach(function (el) { el.style.opacity = 1; el.style.transform = "none"; }); imgs.forEach(function (el) { el.style.clipPath = "none"; }); counters.forEach(function (c) { c.textContent = c.getAttribute("data-count") + (c.getAttribute("data-suffix") || ""); }); }
  function motion() {
    var G = w.gsap, ST = w.ScrollTrigger;
    if (reduce || !G || !ST) { fallback(); return; }
    G.registerPlugin(ST);
    /* hero entrance: split lines rise, then lede/actions */
    var h = d.querySelector(".hero h1, .ph h1");
    var tl = G.timeline({ defaults: { ease: "expo.out" }, delay: introOn && d.querySelector(".intro") ? (intro.classList.contains("skip") ? .3 : 2.75) : 0 });
    if (h) {
      var lines = $$(".split-line > span", h);
      if (lines.length) tl.from(lines, { yPercent: 110, duration: 1.2, stagger: .09 }, .15);
      else tl.from(h, { y: 40, opacity: 0, duration: 1.1 }, .15);
    }
    tl.from($$(".hero .crumbs, .hero .lede, .hero .actions, .hero .since, .ph .crumbs, .ph .lede, .ph .actions, .ph .note-line"), { y: 24, opacity: 0, duration: 1, stagger: .08 }, .45);
    var heroArt = $$(".hero .h-art, .ph .ph-img");
    if (heroArt.length) tl.from(heroArt, { y: 50, opacity: 0, scale: .96, duration: 1.2, stagger: .07 }, .4);
    var bits = $$(".h-stats > div, .yearline li, .h-contact .qa, .np-tabs a");
    if (bits.length) tl.from(bits, { y: 20, opacity: 0, duration: .8, stagger: .05 }, .7);
    var stp = $$(".stp"); if (stp.length) tl.from(stp, { x: 60, opacity: 0, duration: 1.1, stagger: .12 }, .5);
    var bs = $$(".broadsheet > *"); if (bs.length) tl.from(bs, { y: 30, opacity: 0, duration: 1, stagger: .1 }, .55);
    var quick = $$(".quick li"); if (quick.length) tl.from(quick, { y: 30, opacity: 0, duration: .9, stagger: .07 }, .8);
    /* hero parallax */
    $$(".hero .bgimg img").forEach(function (el) {
      G.to(el, { yPercent: 12, ease: "none", scrollTrigger: { trigger: el.closest(".hero"), start: "top top", end: "bottom top", scrub: true } });
    });
    /* section reveals, batched */
    ST.batch(rv, { start: "top 88%", once: true, onEnter: function (b) { G.to(b, { opacity: 1, y: 0, duration: 1, ease: "expo.out", stagger: .08, overwrite: true }); } });
    imgs.forEach(function (el) { G.to(el, { clipPath: "inset(0 0 0% 0)", duration: 1.3, ease: "expo.inOut", scrollTrigger: { trigger: el, start: "top 85%", once: true } }); });
    counters.forEach(function (c) { ST.create({ trigger: c, start: "top 90%", once: true, onEnter: function () { count(c); } }); });
    /* section-heading accent line draws in */
    $$(".sec-head h2").forEach(function (h2) { ST.create({ trigger: h2, start: "top 90%", once: true, onEnter: function () { h2.classList.add("drawn"); } }); });
    setTimeout(function () { ST.refresh(); }, 600);
    w.addEventListener("load", function () { ST.refresh(); });
    setTimeout(function () { rv.forEach(function (el) { if (getComputedStyle(el).opacity === "0" && el.getBoundingClientRect().top < w.innerHeight) G.to(el, { opacity: 1, y: 0, duration: .6 }); }); }, 4000);
  }
  function fallback() {
    $$(".sec-head h2").forEach(function (h2) { h2.classList.add("drawn"); });
    if (reduce || !("IntersectionObserver" in w)) { showAll(); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; var el = e.target; io.unobserve(el);
        if (el.hasAttribute("data-count")) count(el);
        else { el.style.transition = "opacity .9s cubic-bezier(.16,1,.3,1), transform .9s cubic-bezier(.16,1,.3,1), clip-path 1.2s cubic-bezier(.16,1,.3,1)"; el.style.opacity = 1; el.style.transform = "none"; el.style.clipPath = "inset(0 0 0% 0)"; }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    rv.concat(imgs, counters).forEach(function (el) { io.observe(el); });
  }
  if (w.gsap && w.ScrollTrigger) motion();
  else w.addEventListener("load", function () { (w.gsap && w.ScrollTrigger) ? motion() : fallback(); });
  setTimeout(function () { if (!w.gsap) showAll(); }, 7000); /* failsafe if the CDN is blocked */

  /* ---------- ticker pause ---------- */
  $$(".tick-btn").forEach(function (b) { b.addEventListener("click", function () { var t = b.closest(".ticker, .reel"), on = !t.classList.contains("paused"); t.classList.toggle("paused", on); b.setAttribute("aria-pressed", on); b.setAttribute("aria-label", on ? "Play programme ticker" : "Pause programme ticker"); }); });

  /* ---------- About history: active milestone follows the scroll; side panel shows its year ---------- */
  $$(".history").forEach(function (h) {
    var items = $$(".tl-x li", h), tl = h.querySelector(".tl-x"), now = h.querySelector(".hist-now"), yEl = h.querySelector(".hist-year"), cEl = h.querySelector(".hist-cap"), cur = -1, ticking = false;
    if (!items.length) return;
    function update() {
      ticking = false;
      var mid = w.innerHeight * .5, idx = 0;
      items.forEach(function (li, i) { if (li.getBoundingClientRect().top < mid) idx = i; });
      var r = tl.getBoundingClientRect(), p = Math.min(1, Math.max(0, (mid - r.top) / r.height));
      tl.style.setProperty("--p", p.toFixed(3)); if (now) now.style.setProperty("--p", p.toFixed(3));
      if (idx === cur) return;
      cur = idx;
      items.forEach(function (li, i) { li.classList.toggle("on", i === idx); li.classList.toggle("past", i < idx); });
      if (now && yEl) {
        now.classList.add("swap");
        setTimeout(function () { yEl.textContent = items[idx].getAttribute("data-y"); cEl.textContent = items[idx].getAttribute("data-h"); now.classList.remove("swap"); }, reduce ? 0 : 180);
      }
    }
    w.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    w.addEventListener("resize", update); update();
  });

  /* ---------- contact icons draw in when the list comes into view ---------- */
  $$(".contact-list").forEach(function (l) {
    if (!("IntersectionObserver" in w)) { l.classList.add("live"); return; }
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { l.classList.add("live"); io.disconnect(); } }, { threshold: .2 });
    io.observe(l);
    setTimeout(function () { l.classList.add("live"); }, 4000); /* failsafe */
  });

  /* ---------- admission pass: 3D tilt toward the pointer ---------- */
  $$(".pass-wrap").forEach(function (wr) {
    var card = wr.querySelector(".pass"); if (!card || !fine || reduce) return;
    wr.addEventListener("pointermove", function (e) { var r = wr.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; card.style.transform = "rotate(-1deg) rotateY(" + (x * 14).toFixed(1) + "deg) rotateX(" + (-y * 10).toFixed(1) + "deg)"; });
    wr.addEventListener("pointerleave", function () { card.style.transform = ""; });
  });

  /* ---------- lite YouTube ---------- */
  $$(".yt img").forEach(function (im) { function bad() { if (im.naturalWidth && im.naturalWidth <= 120) im.closest(".yt").classList.add("noimg"); } im.addEventListener("error", function () { im.closest(".yt").classList.add("noimg"); }); im.complete ? bad() : im.addEventListener("load", bad); });
  function play(box, title) {
    var f = d.createElement("iframe"), st = box.getAttribute("data-start");
    f.src = "https://www.youtube-nocookie.com/embed/" + box.getAttribute("data-id") + "?autoplay=1&rel=0" + (st ? "&start=" + st : "");
    f.title = title || "Video";
    f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
    f.allowFullscreen = true;
    box.innerHTML = ""; box.appendChild(f);
  }
  $$(".yt[data-id]").forEach(function (box) {
    var b = box.querySelector("button"); if (!b) return;
    b.addEventListener("click", function () { play(box, b.getAttribute("aria-label")); });
  });

  /* ---------- theater playlist: a click loads that video on the stage and plays it ---------- */
  $$(".theater").forEach(function (th) {
    var box = th.querySelector(".stage .yt"), items = $$(".pl", th), n = items.length;
    items.forEach(function (it, i) {
      it.addEventListener("click", function () {
        items.forEach(function (x) { var on = x === it; x.classList.toggle("on", on); x.setAttribute("aria-pressed", on); });
        th.querySelector(".idx").textContent = (i + 1 < 10 ? "0" : "") + (i + 1);
        th.querySelector(".st-title").textContent = it.getAttribute("data-title");
        th.querySelector(".st-when").innerHTML = it.getAttribute("data-when");
        box.setAttribute("data-id", it.getAttribute("data-id")); box.classList.remove("noimg");
        play(box, "Video: " + it.getAttribute("data-title"));
        if (box.getBoundingClientRect().top < 60) box.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
      });
    });
  });

  /* ---------- lightbox ---------- */
  var full = $$("[data-full]");
  if (full.length) {
    var dlg = d.createElement("dialog"); dlg.className = "lb"; dlg.setAttribute("aria-label", "Image viewer");
    dlg.innerHTML = '<button class="x" type="button" aria-label="Close image">&times;</button><img alt=""><p></p>';
    d.body.appendChild(dlg);
    dlg.querySelector(".x").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    full.forEach(function (b) {
      b.addEventListener("click", function () {
        var im = dlg.querySelector("img"), c = b.getAttribute("data-cap") || "";
        im.src = b.getAttribute("data-full"); im.alt = c; dlg.querySelector("p").textContent = c;
        if (dlg.showModal) dlg.showModal(); else w.open(b.getAttribute("data-full"));
      });
    });
  }

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
})();
