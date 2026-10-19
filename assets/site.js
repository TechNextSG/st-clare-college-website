/* St. Clare College - site interactions */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  root.classList.remove("no-js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* header state, progress bar, back-to-top */
  var header = d.querySelector(".site-header"), bar = d.querySelector(".progress"), top = d.querySelector(".to-top");
  function onScroll() {
    var y = window.scrollY, h = d.body.scrollHeight - window.innerHeight;
    if (header) header.classList.toggle("scrolled", y > 8);
    if (bar) bar.style.transform = "scaleX(" + (h > 0 ? y / h : 0) + ")";
    if (top) top.classList.toggle("show", y > 900);
  }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  if (top) top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* mobile menu */
  var mb = d.querySelector(".menu-btn");
  if (mb) {
    mb.addEventListener("click", function () {
      var open = d.body.classList.toggle("menu-open");
      mb.setAttribute("aria-expanded", open);
    });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape" && d.body.classList.contains("menu-open")) { d.body.classList.remove("menu-open"); mb.setAttribute("aria-expanded", "false"); mb.focus(); } });
  }

  /* split headline words */
  d.querySelectorAll("[data-split]").forEach(function (el) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          var frag = d.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(d.createTextNode(t)); return; }
            var w = d.createElement("span"); w.className = "w";
            var s = d.createElement("span"); s.textContent = t; s.style.setProperty("--i", i++);
            w.appendChild(s); frag.appendChild(w);
          });
          c.parentNode.replaceChild(frag, c);
        } else if (c.nodeType === 1 && c.tagName !== "BR") walk(c);
      });
    })(el);
    el.classList.add("split-words");
  });

  /* reveal on scroll */
  var rvEls = d.querySelectorAll(".rv, .rv-l, .rv-s, .split-words, .mode");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    rvEls.forEach(function (el) { io.observe(el); });
  } else rvEls.forEach(function (el) { el.classList.add("in"); });

  /* counters */
  var counters = d.querySelectorAll("[data-count]");
  function runCount(el) {
    var to = parseFloat(el.getAttribute("data-count")), dur = 1600, t0 = null, fmt = el.hasAttribute("data-comma");
    if (reduce) { el.textContent = fmt ? to.toLocaleString("en-US") : to; return; }
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min(1, (t - t0) / dur), v = Math.round(to * (1 - Math.pow(1 - p, 4)));
      el.textContent = fmt ? v.toLocaleString("en-US") : v;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var co = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { runCount(e.target); co.unobserve(e.target); } }); }, { threshold: .5 });
    counters.forEach(function (c) { co.observe(c); });
  } else counters.forEach(runCount);

  /* tabs */
  d.querySelectorAll("[role=tablist]").forEach(function (list) {
    var tabs = list.querySelectorAll("[role=tab]");
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab; t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1;
        var p = d.getElementById(t.getAttribute("aria-controls")); if (p) p.hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var n = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : e.key === "Home" ? 0 : e.key === "End" ? tabs.length - 1 : null;
        if (n === null) return; e.preventDefault(); select(tabs[(n + tabs.length) % tabs.length], true);
      });
    });
    function fromHash() { if (location.hash) { var h = list.querySelector('[data-hash="' + location.hash.slice(1) + '"]'); if (h) select(h); } }
    fromHash(); window.addEventListener("hashchange", fromHash);
  });

  /* rails */
  d.querySelectorAll("[data-rail]").forEach(function (wrap) {
    var rail = wrap.querySelector(".rail");
    wrap.querySelectorAll("[data-dir]").forEach(function (b) {
      b.addEventListener("click", function () {
        var card = rail.firstElementChild; var w = card ? card.getBoundingClientRect().width + 20 : 320;
        rail.scrollBy({ left: w * parseInt(b.getAttribute("data-dir"), 10), behavior: reduce ? "auto" : "smooth" });
      });
    });
  });

  /* cursor glow on dark sections */
  if (!reduce && window.matchMedia("(pointer: fine)").matches) {
    d.querySelectorAll(".dark, .dusk").forEach(function (sec) {
      if (sec.classList.contains("hero") || sec.classList.contains("phero")) return;
      var g = d.createElement("div"); g.className = "glow-follow"; sec.prepend(g);
      sec.addEventListener("pointermove", function (e) { var r = sec.getBoundingClientRect(); g.style.left = (e.clientX - r.left) + "px"; g.style.top = (e.clientY - r.top) + "px"; });
    });
    /* tilt */
    d.querySelectorAll("[data-tilt]").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        el.style.transform = "perspective(900px) rotateY(" + x * 8 + "deg) rotateX(" + (-y * 8) + "deg) translateY(-6px)";
      });
      el.addEventListener("pointerleave", function () { el.style.transform = ""; });
    });
  }

  /* dotted wave canvas (brand motif from the enrollment slides) */
  d.querySelectorAll("canvas.fx-canvas").forEach(function (cv) {
    var ctx = cv.getContext("2d"), W, H, dpr = Math.min(window.devicePixelRatio || 1, 2), t = 0, visible = true, raf;
    var hue = cv.getAttribute("data-tone") || "mix";
    function size() { var r = cv.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    size(); window.addEventListener("resize", size);
    function frame() {
      ctx.clearRect(0, 0, W, H);
      var cols = Math.round(W / 16), rows = 26, gap = W / cols;
      for (var j = 0; j < rows; j++) {
        var pj = j / rows;
        for (var i = 0; i <= cols; i++) {
          var x = i * gap, px = i / cols;
          var y = H * (.35 + pj * .55) + Math.sin(px * 6 + t + pj * 3) * 38 * (1 - pj * .4) + Math.cos(px * 3.2 - t * .7 + pj * 5) * 24;
          var a = (.08 + .5 * Math.pow(Math.sin(px * 3.14), 2)) * (1 - pj * .55);
          var c = hue === "gold" ? "247,216,58" : (px > .5 ? "212,23,126" : "120,140,255");
          ctx.fillStyle = "rgba(" + c + "," + a.toFixed(3) + ")";
          ctx.beginPath(); ctx.arc(x, y, 1.15 + (1 - pj) * .6, 0, 6.283); ctx.fill();
        }
      }
      t += .008;
      if (visible && !reduce) raf = requestAnimationFrame(frame);
    }
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; if (visible && !reduce) { cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); } }).observe(cv);
    }
    frame();
  });

  /* contact form -> email draft (no data leaves the browser until the user sends it) */
  var form = d.querySelector("[data-mailto]");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form), lines = [];
    f.forEach(function (v, k) { if (k !== "subject") lines.push(k + ": " + v); });
    location.href = "mailto:" + form.getAttribute("data-mailto") + "?subject=" + encodeURIComponent(f.get("subject") || "Website inquiry") + "&body=" + encodeURIComponent(lines.join("\n"));
    var st = form.querySelector(".form-status"); if (st) st.textContent = "Your email app should open with your message. If it doesn't, write to " + form.getAttribute("data-mailto") + " or call (02) 8232-4483.";
  });

  /* marquee pause */
  d.querySelectorAll(".marquee").forEach(function (m) {
    var b = d.createElement("button"); b.className = "mq-btn"; b.type = "button"; b.setAttribute("aria-label", "Pause scrolling text"); b.textContent = "II";
    b.addEventListener("click", function () { var p = m.classList.toggle("paused"); b.setAttribute("aria-label", p ? "Play scrolling text" : "Pause scrolling text"); b.textContent = p ? "\u25B6" : "II"; });
    m.appendChild(b);
  });

  /* three.js only where the globe shows */
  var gh = d.getElementById("globe");
  if (gh && window.matchMedia("(min-width: 921px) and (prefers-reduced-motion: no-preference)").matches) {
    var sc = d.createElement("script"); sc.src = "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js";
    sc.onload = function () { window.initGlobe && window.initGlobe(); }; d.head.appendChild(sc);
  }

  /* year */
  d.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

/* 3D dotted globe (SCO Online - "the leading edge in online education") */
window.initGlobe = function () {
  var host = document.getElementById("globe");
  if (!host || !window.THREE) return;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var THREE = window.THREE, W = host.clientWidth, H = host.clientHeight;
  var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); renderer.setSize(W, H); host.prepend(renderer.domElement);
  var scene = new THREE.Scene(), cam = new THREE.PerspectiveCamera(40, W / H, .1, 100); cam.position.z = 6.2;
  var group = new THREE.Group(); scene.add(group);

  /* fibonacci sphere points */
  var N = 2600, pos = new Float32Array(N * 3), col = new Float32Array(N * 3), cA = new THREE.Color("#7c8cff"), cB = new THREE.Color("#d4177e"), cG = new THREE.Color("#f7d83a");
  for (var i = 0; i < N; i++) {
    var y = 1 - (i / (N - 1)) * 2, r = Math.sqrt(1 - y * y), th = Math.PI * (3 - Math.sqrt(5)) * i;
    var x = Math.cos(th) * r, z = Math.sin(th) * r;
    pos.set([x * 1.7, y * 1.7, z * 1.7], i * 3);
    var land = (Math.sin(x * 5.1 + 1.3) * Math.cos(y * 4.2) + Math.sin(z * 6.3 - y * 2.1)) > .35;
    var c = land ? cG : cA.clone().lerp(cB, (y + 1) / 2);
    col.set([c.r, c.g, c.b], i * 3);
  }
  var g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(pos, 3)); g.setAttribute("color", new THREE.BufferAttribute(col, 3));
  var pts = new THREE.Points(g, new THREE.PointsMaterial({ size: .035, vertexColors: true, transparent: true, opacity: .95 }));
  group.add(pts);

  /* glow core + rings */
  var core = new THREE.Mesh(new THREE.SphereGeometry(1.62, 48, 48), new THREE.MeshBasicMaterial({ color: "#1a1580", transparent: true, opacity: .55 }));
  group.add(core);
  function ring(rad, color, tilt) {
    var m = new THREE.Mesh(new THREE.TorusGeometry(rad, .006, 8, 200), new THREE.MeshBasicMaterial({ color: color, transparent: true, opacity: .7 }));
    m.rotation.x = tilt; scene.add(m); return m;
  }
  var r1 = ring(2.15, "#f7d83a", 1.2), r2 = ring(2.45, "#d4177e", 1.9);

  /* arcs between random points (online connections) */
  var arcs = [];
  function rnd() { var u = Math.random() * 2 - 1, a = Math.random() * 6.283, s = Math.sqrt(1 - u * u); return new THREE.Vector3(s * Math.cos(a), u, s * Math.sin(a)).multiplyScalar(1.7); }
  for (var k = 0; k < 9; k++) {
    var a = rnd(), b = rnd(), mid = a.clone().add(b).multiplyScalar(.5).normalize().multiplyScalar(2.5 + Math.random() * .6);
    var curve = new THREE.QuadraticBezierCurve3(a, mid, b), geo = new THREE.BufferGeometry().setFromPoints(curve.getPoints(60));
    var line = new THREE.Line(geo, new THREE.LineBasicMaterial({ color: k % 2 ? "#f7d83a" : "#ff5aa8", transparent: true, opacity: .75 }));
    geo.setDrawRange(0, 0); group.add(line); arcs.push({ geo: geo, off: Math.random() * 120 });
  }

  var mx = 0, my = 0;
  window.addEventListener("pointermove", function (e) { mx = (e.clientX / window.innerWidth - .5); my = (e.clientY / window.innerHeight - .5); }, { passive: true });
  window.addEventListener("resize", function () { W = host.clientWidth; H = host.clientHeight; renderer.setSize(W, H); cam.aspect = W / H; cam.updateProjectionMatrix(); });

  var t = 0, vis = true, running = false;
  new IntersectionObserver(function (es) { vis = es[0].isIntersecting; if (vis && !running && !reduce) { running = true; requestAnimationFrame(loop); } }).observe(host);
  function loop() {
    running = vis && !reduce;
    t += 1;
    group.rotation.y += reduce ? 0 : .0026;
    group.rotation.x += ((my * .4) - group.rotation.x) * .04;
    group.rotation.z += ((-mx * .2) - group.rotation.z) * .04;
    r1.rotation.z += .002; r2.rotation.z -= .0015;
    arcs.forEach(function (a) { var p = ((t + a.off) % 180) / 120; a.geo.setDrawRange(0, Math.floor(Math.min(1, p) * 61)); });
    renderer.render(scene, cam);
    if (vis && !reduce) requestAnimationFrame(loop);
  }
  if (reduce) arcs.forEach(function (a) { a.geo.setDrawRange(0, 61); });
  running = true; loop();
};
