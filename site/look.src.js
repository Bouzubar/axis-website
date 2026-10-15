/* Men / Women photos. The build fills in the map; each image carries data-cover or data-series.
   No choice (or the chosen button clicked again): the mixed set of men and women. */
(function () {
  var M = /*MAP*/{};
  var base = (document.currentScript && document.currentScript.src || '').replace(/look\.js(\?.*)?$/, '') + 'img/';
  var KEY = 'axis-look', v = null;
  try { v = localStorage.getItem(KEY); } catch (e) {}
  if (v !== 'm' && v !== 'f') v = null;
  function pick(e) { return e ? (v && e[v]) || e[e.d] : null; }
  window.axisCover = function (slug) { var p = pick(M.c[slug]); return p ? 'img/' + p : 'img/covers/' + slug + '.jpg'; };
  function apply() {
    {
      [].forEach.call(document.querySelectorAll('img[data-cover],img[data-series]'), function (i) {
        var c = i.getAttribute('data-cover'), p = pick(c ? M.c[c] : M.s[i.getAttribute('data-series')]);
        if (p && i.src !== base + p) i.src = base + p;
      });
      [].forEach.call(document.querySelectorAll('picture[data-hero]'), function (pic) {
        var p = pick(M.h[pic.getAttribute('data-hero')]), img = pic.querySelector('img'), src = pic.querySelector('source');
        if (!p || !img) return;
        if (src) src.srcset = base + p + '_ph.jpg';
        if (img.src !== base + p + '.jpg') img.src = base + p + '.jpg';
      });
    }
    [].forEach.call(document.querySelectorAll('.look button'), function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-look') === v));
    });
  }
  window.axisLook = apply;
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.look button');
    if (!b) return;
    // clicking the selected button again turns it off (Abdullah, 15 Oct)
    v = b.getAttribute('data-look') === v ? null : b.getAttribute('data-look');
    try { v ? localStorage.setItem(KEY, v) : localStorage.removeItem(KEY); } catch (err) {}
    apply();
  });
  apply();
})();
