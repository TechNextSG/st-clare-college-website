/* St. Clare College - quiet, professional interactions. No libraries. */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.classList.add("js");
  window.addEventListener("load", function () { root.classList.add("loaded"); });
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }

  /* header shadow on scroll */
  var head = d.querySelector(".head");
  function onScroll() { if (head) head.classList.toggle("scrolled", window.scrollY > 10); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* mobile menu: focus in, outside inert, Esc closes, Tab wraps */
  var mb = d.querySelector(".menu-btn"), nav = d.getElementById("nav");
  if (mb && nav) {
    var outside = $$("main, footer, .util, .brand, .skip");
    function setMenu(open) {
      d.body.classList.toggle("menu-open", open);
      mb.setAttribute("aria-expanded", open);
      mb.querySelector("span").textContent = open ? "Close" : "Menu";
      d.body.style.overflow = open ? "hidden" : "";
      outside.forEach(function (el) { open ? el.setAttribute("inert", "") : el.removeAttribute("inert"); });
      if (open) setTimeout(function () { var a = nav.querySelector("a"); if (a) a.focus(); }, 50);
    }
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
    window.addEventListener("resize", function () { if (window.innerWidth > 1080 && d.body.classList.contains("menu-open")) setMenu(false); });
  }

  /* tabs */
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
    fromHash(); window.addEventListener("hashchange", fromHash);
  });

  /* quiet reveals */
  var rv = $$(".rv");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { rootMargin: "0px 0px -6% 0px" });
    rv.forEach(function (el) { io.observe(el); });
    setTimeout(function () { rv.forEach(function (el) { el.classList.add("in"); }); }, 6000); /* failsafe */
  } else rv.forEach(function (el) { el.classList.add("in"); });

  /* contact form -> email draft */
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
