/* St. Clare Assistant: answers questions from this website's own content (assets/kb.json).
   Runs in the browser: no server, no AI API, nothing sent anywhere. */
(function () {
  "use strict";
  var d = document, w = window, kb = null, open = false, busy = false;
  var reduce = w.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var SYN = { enrol: "enroll", enrolment: "enrollment", tuition: "fees", fee: "fees", magkano: "fees", tor: "transcript", shs: "senior high", hm: "hospitality",
              cs: "computer science", polsci: "political science", saan: "where", kailan: "when", kinder: "kindergarten", reqs: "requirements", req: "requirements" };
  var STOP = { the: 1, a: 1, an: 1, is: 1, are: 1, do: 1, does: 1, i: 1, you: 1, to: 1, of: 1, in: 1, for: 1, and: 1, can: 1, what: 1, how: 1, my: 1, me: 1, at: 1, on: 1, st: 1, clare: 1, college: 0, please: 1, po: 1, ba: 0 };

  function norm(s) { return (" " + s.toLowerCase().replace(/[’']/g, "").replace(/[^a-z0-9&+\- ]+/g, " ").replace(/\s+/g, " ") + " ").replace(/ (\w+) /g, function (m, t) { return " " + (SYN[t] || t) + " "; }); }

  function score(q, it) {
    var s = 0, toks = q.trim().split(" ").filter(function (t) { return t.length > 1 && !STOP[t]; });
    it.k.forEach(function (k) {
      var kk = " " + k + " ";
      if (q.indexOf(kk) > -1) s += k.indexOf(" ") > -1 ? 3 + k.split(" ").length : 2.2;
      else if (k.length > 4 && q.indexOf(k) > -1) s += 1.2;
    });
    toks.forEach(function (t) { if (t.length > 3 && it.q.toLowerCase().indexOf(t) > -1) s += .6; });
    return s * (it.w || 1);
  }

  function answer(text) {
    var q = norm(text), ranked = kb.intents.map(function (it) { return { it: it, s: score(q, it) }; })
      .filter(function (r) { return r.s > 0; }).sort(function (a, b) { return b.s - a.s; });
    if (!ranked.length || ranked[0].s < 1.8) {
      var pg = kb.pages.filter(function (p) { return q.indexOf(" " + p[1].toLowerCase() + " ") > -1; });
      return { a: kb.fallback, l: pg.map(function (p) { return [p[0], p[1]]; }), more: kb.suggest.slice(0, 3) };
    }
    var top = ranked[0].it, more = ranked.slice(1, 4).filter(function (r) { return r.s >= ranked[0].s * .5; }).map(function (r) { return r.it.q; });
    return { a: top.a, l: top.l, more: more };
  }

  /* ---------- UI ---------- */
  var CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="bub" d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><circle class="dt d1" cx="8.5" cy="12" r=".9" fill="currentColor"/><circle class="dt d2" cx="12" cy="12" r=".9" fill="currentColor"/><circle class="dt d3" cx="15.5" cy="12" r=".9" fill="currentColor"/></svg>';
  var root = d.createElement("div"); root.className = "sca";
  root.innerHTML =
    '<button class="sca-launch" type="button" aria-expanded="false" aria-controls="sca-panel">' + CHAT + '<span>Ask St. Clare</span></button>' +
    '<section class="sca-panel" id="sca-panel" role="dialog" aria-modal="false" aria-labelledby="sca-title" hidden>' +
      '<header><img src="img/seal-128.webp" alt="" width="40" height="40"><div><b id="sca-title">St. Clare Assistant</b><small>Answers from this website</small></div>' +
      '<button class="sca-x" type="button" aria-label="Close the assistant"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></header>' +
      '<div class="sca-log" role="log" aria-live="polite"></div>' +
      '<div class="sca-chips" aria-label="Suggested questions"></div>' +
      '<form class="sca-form"><label class="sr-only" for="sca-in">Type your question</label><input id="sca-in" autocomplete="off" maxlength="200" placeholder="Ask about enrollment, programmes, fees..."><button type="submit" aria-label="Send"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg></button></form>' +
      '<p class="sca-note">Answers come from stclareonline.com content on this site. For fees and dates, call (02) 8232-4483.</p>' +
    "</section>";
  d.body.appendChild(root);
  var btn = root.querySelector(".sca-launch"), panel = root.querySelector(".sca-panel"), log = root.querySelector(".sca-log"),
      chips = root.querySelector(".sca-chips"), form = root.querySelector(".sca-form"), input = root.querySelector("#sca-in");

  function esc(s) { var t = d.createElement("div"); t.textContent = s; return t.innerHTML; }
  function scrollLog() { log.scrollTop = log.scrollHeight; }
  function bubble(html, who) {
    var m = d.createElement("div"); m.className = "sca-msg " + who; m.innerHTML = html; log.appendChild(m);
    if (who === "bot" && m.offsetHeight > log.clientHeight * .6) log.scrollTop = m.offsetTop - 12; else scrollLog();
    return m;
  }
  function setChips(list) {
    chips.innerHTML = "";
    (list || []).forEach(function (q) { var b = d.createElement("button"); b.type = "button"; b.textContent = q; b.addEventListener("click", function () { ask(q); }); chips.appendChild(b); });
  }
  function reply(r) {
    var links = (r.l || []).map(function (l) { var ext = /^https?:/.test(l[0]); return '<a class="sca-link" href="' + esc(l[0]) + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + ">" + esc(l[1]) + " &rarr;</a>"; }).join("");
    bubble(r.a + (links ? '<div class="sca-links">' + links + "</div>" : ""), "bot");
    setChips(r.more && r.more.length ? r.more : kb.suggest.slice(0, 3));
  }
  function ask(text) {
    text = (text || "").trim(); if (!text || busy || !kb) return;
    busy = true; bubble(esc(text), "me"); setChips([]);
    var typing = bubble('<span class="sca-typing"><i></i><i></i><i></i></span>', "bot typing");
    setTimeout(function () { typing.remove(); reply(answer(text)); busy = false; }, reduce ? 50 : 520 + Math.min(700, text.length * 12));
  }
  function load(cb) {
    if (kb) return cb();
    fetch("assets/kb.json?v=" + (root.getAttribute("data-v") || "1")).then(function (r) { return r.json(); }).then(function (j) { kb = j; cb(); })
      .catch(function () { bubble("Sorry, the assistant couldn't load. Please call (02) 8232-4483 or email stclarecollege.ph@gmail.com.", "bot"); });
  }
  function toggle(on) {
    open = on; panel.hidden = !on; btn.setAttribute("aria-expanded", on); root.classList.toggle("open", on);
    if (on) load(function () {
      if (!log.children.length) { bubble("Hi! I'm the St. Clare Assistant. Ask me about programmes, enrollment, requirements, student services or how to reach the college.", "bot"); setChips(kb.suggest); }
      setTimeout(function () { input.focus(); }, 60);
    }); else btn.focus();
  }
  btn.addEventListener("click", function () { toggle(!open); });
  root.querySelector(".sca-x").addEventListener("click", function () { toggle(false); });
  d.addEventListener("keydown", function (e) { if (open && e.key === "Escape") toggle(false); });
  form.addEventListener("submit", function (e) { e.preventDefault(); var v = input.value; input.value = ""; ask(v); });
  /* nudge once per visit after a few seconds */
  setTimeout(function () { if (!open) root.classList.add("nudge"); setTimeout(function () { root.classList.remove("nudge"); }, 4000); }, 6000);
})();
