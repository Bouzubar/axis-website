// AXIS sign-up forms (free guide, coaching waiting list). No backend: each form posts to a Google Form,
// whose responses land in a Google Sheet. Config comes from data/site.json via the form's data-cfg.
(function () {
  document.querySelectorAll('form.gsignup').forEach(function (f) {
    var m = f.querySelector('.wl-msg'), c = JSON.parse(f.dataset.cfg);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = {};
      new FormData(f).forEach(function (v, k) { d[k] = String(v).trim(); });
      d.source = f.dataset.source;
      d.lang = document.documentElement.lang;
      var done = function () { f.classList.add('sent'); m.innerHTML = c.ok; };
      if (c.form) {
        var b = new URLSearchParams();
        Object.keys(c.entries).forEach(function (k) { if (c.entries[k] && d[k]) b.append('entry.' + c.entries[k], d[k]); });
        // Google Forms sends no CORS headers, so the reply is opaque: a network failure is the only error we can see.
        fetch('https://docs.google.com/forms/d/e/' + c.form + '/formResponse', { method: 'POST', mode: 'no-cors', body: b })
          .then(done, function () { m.textContent = c.err; });
      } else {
        var txt = [d.source, d.name, d.email, d.goal].filter(Boolean).join(String.fromCharCode(10));
        var go = function () { done(); m.insertAdjacentHTML('beforeend', '<span class="dim"> ' + c.copy + '</span>'); window.open(c.ig, '_blank'); };
        if (navigator.clipboard) navigator.clipboard.writeText(txt).then(go, go); else go();
      }
    });
  });
})();
