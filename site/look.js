/* Men / Women photos. The build fills in the map; each image carries data-cover or data-series.
   No choice yet: the page keeps the mixed set it was built with. */
(function () {
  var M = {"c":{"ankle-foot-pain":{"m":"covers/ankle-foot-pain.jpg","f":"covers/f/ankle-foot-pain.jpg","d":"m"},"anterior-pelvic-tilt":{"m":"covers/anterior-pelvic-tilt.jpg","f":"covers/f/anterior-pelvic-tilt.jpg","d":"f"},"elbow-wrist-pain":{"m":"covers/elbow-wrist-pain.jpg","f":"covers/f/elbow-wrist-pain.jpg","d":"m"},"hip-groin-pain":{"m":"covers/hip-groin-pain.jpg","f":"covers/f/hip-groin-pain.jpg","d":"f"},"knee-pain":{"m":"covers/knee-pain.jpg","f":"covers/f/knee-pain.jpg","d":"m"},"lateral-pelvic-tilt":{"m":"covers/lateral-pelvic-tilt.jpg","f":"covers/f/lateral-pelvic-tilt.jpg","d":"f"},"lower-back-pain":{"m":"covers/lower-back-pain.jpg","f":"covers/f/lower-back-pain.jpg","d":"m"},"neck-pain":{"m":"covers/neck-pain.jpg","f":"covers/f/neck-pain.jpg","d":"f"},"shoulder-pain":{"m":"covers/shoulder-pain.jpg","f":"covers/f/shoulder-pain.jpg","d":"m"},"foundation-strength":{"m":"covers/foundation-strength.jpg","f":"covers/f/foundation-strength.jpg","d":"m"},"athletic-development":{"m":"covers/athletic-development.jpg","f":"covers/f/athletic-development.jpg","d":"f"},"multidirectional-base":{"m":"covers/multidirectional-base.jpg","f":"covers/f/multidirectional-base.jpg","d":"m"},"multidirectional-build":{"m":"covers/multidirectional-build.jpg","f":"covers/f/multidirectional-build.jpg","d":"f"},"multidirectional-compete":{"m":"covers/multidirectional-compete.jpg","f":"covers/f/multidirectional-compete.jpg","d":"m"},"multidirectional-restore":{"m":"covers/multidirectional-restore.jpg","f":"covers/f/multidirectional-restore.jpg","d":"f"},"rotational-base":{"m":"covers/rotational-base.jpg","f":"covers/f/rotational-base.jpg","d":"m"},"rotational-build":{"m":"covers/rotational-build.jpg","f":"covers/f/rotational-build.jpg","d":"f"},"rotational-compete":{"m":"covers/rotational-compete.jpg","f":"covers/f/rotational-compete.jpg","d":"m"},"rotational-restore":{"m":"covers/rotational-restore.jpg","f":"covers/f/rotational-restore.jpg","d":"f"},"grappling-base":{"m":"covers/grappling-base.jpg","f":"covers/f/grappling-base.jpg","d":"m"},"grappling-build":{"m":"covers/grappling-build.jpg","f":"covers/f/grappling-build.jpg","d":"f"},"grappling-compete":{"m":"covers/grappling-compete.jpg","f":"covers/f/grappling-compete.jpg","d":"m"},"grappling-restore":{"m":"covers/grappling-restore.jpg","f":"covers/f/grappling-restore.jpg","d":"f"},"striking-base":{"m":"covers/striking-base.jpg","f":"covers/f/striking-base.jpg","d":"m"},"striking-build":{"m":"covers/striking-build.jpg","f":"covers/f/striking-build.jpg","d":"f"},"striking-compete":{"m":"covers/striking-compete.jpg","f":"covers/f/striking-compete.jpg","d":"m"},"striking-restore":{"m":"covers/striking-restore.jpg","f":"covers/f/striking-restore.jpg","d":"f"},"linear-speed-base":{"m":"covers/linear-speed-base.jpg","f":"covers/f/linear-speed-base.jpg","d":"m"},"linear-speed-build":{"m":"covers/linear-speed-build.jpg","f":"covers/f/linear-speed-build.jpg","d":"f"},"linear-speed-compete":{"m":"covers/linear-speed-compete.jpg","f":"covers/f/linear-speed-compete.jpg","d":"m"},"linear-speed-restore":{"m":"covers/linear-speed-restore.jpg","f":"covers/f/linear-speed-restore.jpg","d":"f"},"endurance-base":{"m":"covers/endurance-base.jpg","f":"covers/f/endurance-base.jpg","d":"m"},"endurance-build":{"m":"covers/endurance-build.jpg","f":"covers/f/endurance-build.jpg","d":"f"},"endurance-compete":{"m":"covers/endurance-compete.jpg","f":"covers/f/endurance-compete.jpg","d":"m"},"endurance-restore":{"m":"covers/endurance-restore.jpg","f":"covers/f/endurance-restore.jpg","d":"f"},"full-body":{"m":"covers/full-body.jpg","f":"covers/f/full-body.jpg","d":"m"},"upper-lower":{"m":"covers/upper-lower.jpg","f":"covers/f/upper-lower.jpg","d":"f"},"ppl-upper-lower":{"m":"covers/ppl-upper-lower.jpg","f":"covers/f/ppl-upper-lower.jpg","d":"m"},"body-part":{"m":"covers/body-part.jpg","f":"covers/f/body-part.jpg","d":"f"},"push-pull-legs":{"m":"covers/push-pull-legs.jpg","f":"covers/f/push-pull-legs.jpg","d":"m"},"glute-emphasis-4day":{"f":"covers/glute-emphasis-4day.jpg","d":"f"},"glute-emphasis-3day":{"f":"covers/glute-emphasis-3day.jpg","d":"f"},"acl-reconstruction":{"m":"covers/acl-reconstruction.jpg","f":"covers/f/acl-reconstruction.jpg","d":"f"},"shoulder-dislocation":{"m":"covers/shoulder-dislocation.jpg","f":"covers/f/shoulder-dislocation.jpg","d":"m"},"hamstring-strain":{"m":"covers/hamstring-strain.jpg","f":"covers/f/hamstring-strain.jpg","d":"f"}},"s":{"corrective":{"p":"series_corrective.jpg","m":"covers/knee-pain.jpg","d":"p","f":"covers/f/knee-pain.jpg"},"fundamentals":{"p":"series_fundamentals.jpg","m":"covers/foundation-strength.jpg","d":"p","f":"covers/f/foundation-strength.jpg"},"performance":{"p":"series_performance.jpg","m":"covers/linear-speed-build.jpg","d":"p","f":"covers/f/linear-speed-build.jpg"},"physique":{"p":"series_physique.jpg","m":"covers/full-body.jpg","d":"p","f":"covers/f/full-body.jpg"},"return":{"p":"series_return.jpg","m":"covers/acl-reconstruction.jpg","d":"p","f":"covers/f/acl-reconstruction.jpg"}},"h":{"home":{"d":"p","p":"hero/home","m":"hero/home_m","f":"hero/home_f"},"science":{"d":"p","p":"hero/science","m":"hero/science","f":"hero/science_f"},"physique":{"d":"p","p":"hero/physique","m":"hero/physique","f":"hero/physique_f"},"squat":{"d":"p","p":"hero/squat","m":"hero/squat_m","f":"hero/squat_f"},"performance":{"d":"p","p":"hero/performance","m":"hero/performance_m","f":"hero/performance"}}};
  var base = (document.currentScript && document.currentScript.src || '').replace(/look\.js(\?.*)?$/, '') + 'img/';
  var KEY = 'axis-look', v = null;
  try { v = localStorage.getItem(KEY); } catch (e) {}
  if (v !== 'm' && v !== 'f') v = null;
  function pick(e) { return e ? (v && e[v]) || e[e.d] : null; }
  window.axisCover = function (slug) { var p = pick(M.c[slug]); return p ? 'img/' + p : 'img/covers/' + slug + '.jpg'; };
  function apply() {
    if (v) {
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
    v = b.getAttribute('data-look');
    try { localStorage.setItem(KEY, v); } catch (err) {}
    apply();
  });
  apply();
})();
