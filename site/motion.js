// AXIS site motion: scroll reveals, counters, the block chart drawing itself, scroll progress
// and a soft glow that follows the pointer on the finder tiles. Everything is skipped for
// people who ask for reduced motion; without JavaScript every element is simply visible.
(function () {
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Inner pages get the same gentle reveal on their blocks without per-page markup.
  if (!document.body.classList.contains('home'))
    document.querySelectorAll('.pp-sec, .prog, .offer, .pchart-card, .yearstrip, .fam, .card').forEach(function (el) { el.classList.add('rv'); });
  var els = document.querySelectorAll('.rv, .h-title, .chartcard, [data-count]');
  function count(el) {
    var end = +el.dataset.count, t0 = null;
    if (still) { el.textContent = end; return; }
    function step(t) {
      t0 = t0 || t;
      var k = Math.min(1, (t - t0) / 1100), e = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(end * e);
      if (k < 1) requestAnimationFrame(step);
    }
    el.textContent = '0';
    requestAnimationFrame(step);
  }
  if (!('IntersectionObserver' in window) || still) {
    els.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        if (e.target.dataset.count) count(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }
  var bar = document.querySelector('.progress');
  if (bar && !still) {
    var tick = false;
    addEventListener('scroll', function () {
      if (tick) return; tick = true;
      requestAnimationFrame(function () {
        var d = document.documentElement, m = d.scrollHeight - d.clientHeight;
        bar.style.transform = 'scaleX(' + (m > 0 ? d.scrollTop / m : 0) + ')';
        tick = false;
      });
    }, { passive: true });
  }
  // Scroll-linked handover between sections (Abdullah, 11 Oct): each block fades in rising from
  // below as it enters, and fades out moving up as it leaves. Tied directly to scroll position,
  // so it moves exactly with the finger. Skipped on the finder, where content changes in place.
  if (!still && !document.getElementById('finder')) {
    var blocks = [].slice.call(document.querySelectorAll('main > section, main > article, main > .marquee, .pp-body > section'));
    var busy = false, D = 70;
    function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
    function frame() {
      var vh = innerHeight, zone = vh * 0.42;
      for (var i = 0; i < blocks.length; i++) {
        var el = blocks[i], r = el.getBoundingClientRect();
        if (r.bottom < -40 || r.top > vh + 40) { el.style.opacity = 0; continue; }
        var pin = clamp((vh - r.top) / zone), pout = clamp(r.bottom / zone);
        var y = (1 - pin) * D - (1 - pout) * D, v = Math.min(pin, pout);
        el.style.opacity = (0.08 + 0.92 * v).toFixed(3);
        el.style.transform = v > 0.999 ? '' : 'translate3d(0,' + y.toFixed(1) + 'px,0) scale(' + (0.97 + 0.03 * v).toFixed(4) + ')';
      }
      busy = false;
    }
    function ask() { if (!busy) { busy = true; requestAnimationFrame(frame); } }
    blocks.forEach(function (el) { el.classList.add('sx'); });
    addEventListener('scroll', ask, { passive: true });
    addEventListener('resize', ask);
    frame();
  }
  if (!still) document.querySelectorAll('.tile').forEach(function (t) {
    t.addEventListener('pointermove', function (e) {
      var r = t.getBoundingClientRect();
      t.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      t.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  // Phone carousels (series cards, sample pages): one card per swipe, with dots, a count and
  // next/previous buttons underneath so it is obvious there is more. Hidden above 600px by CSS.
  var ar = document.documentElement.dir === 'rtl';
  [].forEach.call(document.querySelectorAll('.scroll, .phones'), function (box) {
    var items = [].slice.call(box.children);
    if (items.length < 2) return;
    var nav = document.createElement('div');
    nav.className = 'cnav';
    nav.innerHTML = '<div class="hint"><span class="dots">' + items.map(function () { return '<i></i>'; }).join('') +
      '</span><span class="n"></span></div><div class="btns">' +
      '<button type="button" class="pv" aria-label="' + (ar ? 'السابق' : 'Previous') + '"><span>←</span></button>' +
      '<button type="button" class="nx" aria-label="' + (ar ? 'التالي' : 'Next') + '"><span>→</span></button></div>';
    box.parentNode.insertBefore(nav, box.nextSibling);
    var dots = nav.querySelectorAll('.dots i'), n = nav.querySelector('.n'), pv = nav.querySelector('.pv'), nx = nav.querySelector('.nx');
    var cur = -1;
    function current() {
      var mid = box.getBoundingClientRect().left + box.clientWidth / 2, best = 0, d = 1e9;
      items.forEach(function (it, i) { var r = it.getBoundingClientRect(), x = Math.abs(r.left + r.width / 2 - mid); if (x < d) { d = x; best = i; } });
      return best;
    }
    function paint() {
      var i = current();
      if (i === cur) return;
      cur = i;
      [].forEach.call(dots, function (dt, k) { dt.classList.toggle('on', k === i); });
      n.innerHTML = '<span dir="ltr">' + (i + 1) + ' / ' + items.length + '</span> · ' + (ar ? 'اسحب' : 'Swipe');
      pv.disabled = i === 0; nx.disabled = i === items.length - 1;
    }
    function go(k) {
      var it = items[Math.max(0, Math.min(items.length - 1, k))];
      var dx = it.getBoundingClientRect().left - box.getBoundingClientRect().left - (box.clientWidth - it.offsetWidth) / 2;
      box.scrollBy({ left: dx, behavior: still ? 'auto' : 'smooth' });
    }
    pv.addEventListener('click', function () { go(current() - 1); });
    nx.addEventListener('click', function () { go(current() + 1); });
    box.addEventListener('scroll', function () { requestAnimationFrame(paint); }, { passive: true });
    addEventListener('resize', function () { cur = -1; paint(); });
    paint();
  });
})();
