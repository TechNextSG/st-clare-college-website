(function () {
  "use strict";
  var d = document, toast = d.querySelector(".toast"), tT;
  function say(t) { toast.textContent = t; toast.classList.add("on"); clearTimeout(tT); tT = setTimeout(function () { toast.classList.remove("on"); }, 1800); }
  function copyText(t) { return navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject(); }
  d.querySelectorAll("[data-copy]").forEach(function (b) { b.addEventListener("click", function () { var v = b.getAttribute("data-copy"); copyText(v).then(function () { say("Copied " + v.toUpperCase()); }, function () { say(v.toUpperCase()); }); }); });
  d.querySelectorAll("[data-copy-el]").forEach(function (b) { b.addEventListener("click", function () { copyText(d.getElementById(b.getAttribute("data-copy-el")).textContent).then(function () { say("Boilerplate copied"); }); }); });
  d.querySelectorAll("[data-copy-html]").forEach(function (b) {
    b.addEventListener("click", function () {
      var html = d.getElementById(b.getAttribute("data-copy-html")).innerHTML;
      if (navigator.clipboard && window.ClipboardItem) navigator.clipboard.write([new ClipboardItem({ "text/html": new Blob([html], { type: "text/html" }), "text/plain": new Blob([html], { type: "text/plain" }) })]).then(function () { say("Signature copied: paste it into Gmail"); });
      else copyText(html).then(function () { say("Signature HTML copied"); });
    });
  });
  var tt = d.getElementById("tt"), out = d.querySelector(".tt-out");
  if (tt) tt.addEventListener("input", function () { out.textContent = tt.value || "Become a Clarean"; });
  var dlg = d.querySelector("dialog.lb");
  d.querySelectorAll("[data-full]").forEach(function (b) { b.addEventListener("click", function () { dlg.querySelector("img").src = b.getAttribute("data-full"); dlg.querySelector("img").alt = b.getAttribute("aria-label"); dlg.showModal(); }); });
  dlg.querySelector(".x").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  /* reveal + active nav */
  var els = d.querySelectorAll(".sw, .lg, .rule-card, .el, .mat, .vcard, .photos figure, .font");
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    els.forEach(function (e) { e.classList.add("rv"); });
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { rootMargin: "0px 0px -6% 0px" });
    els.forEach(function (e) { io.observe(e); });
    setTimeout(function () { els.forEach(function (e) { e.classList.add("in"); }); }, 5000);
  }
  var links = d.querySelectorAll(".top nav a");
  var so = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); }); }); }, { rootMargin: "-45% 0px -50% 0px" });
  d.querySelectorAll("main section[id]").forEach(function (s) { so.observe(s); });
})();
