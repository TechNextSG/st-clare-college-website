/* St. Clare College - lite YouTube embeds and image lightbox. */
(function () {
  "use strict";
  document.querySelectorAll(".yt[data-id]").forEach(function (box) {
    var b = box.querySelector("button"); if (!b) return;
    b.addEventListener("click", function () {
      var f = document.createElement("iframe"), st = box.getAttribute("data-start");
      f.src = "https://www.youtube-nocookie.com/embed/" + box.getAttribute("data-id") + "?autoplay=1&rel=0" + (st ? "&start=" + st : "");
      f.title = b.getAttribute("aria-label") || "Video";
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      box.innerHTML = ""; box.appendChild(f);
    });
  });
  var full = document.querySelectorAll("[data-full]");
  if (!full.length) return;
  var dlg = document.createElement("dialog"); dlg.className = "lb"; dlg.setAttribute("aria-label", "Image viewer");
  dlg.innerHTML = '<button class="x" type="button" aria-label="Close image">&times;</button><img alt=""><p></p>';
  document.body.appendChild(dlg);
  dlg.querySelector(".x").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  full.forEach(function (b) {
    b.addEventListener("click", function () {
      var im = dlg.querySelector("img"), cap = b.getAttribute("data-cap") || "";
      im.src = b.getAttribute("data-full"); im.alt = cap; dlg.querySelector("p").textContent = cap;
      if (dlg.showModal) dlg.showModal(); else window.open(b.getAttribute("data-full"));
    });
  });
})();
