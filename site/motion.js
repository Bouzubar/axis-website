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
    // Home: sections carry the dimmed photo, so only their contents move and fade.
    var blocks = [].slice.call(document.querySelectorAll('main > section, main > article, main > .marquee, main > .mq, .pp-body > section, .seg > section > *'));
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

  // Sports marquee: a pause button (it would otherwise move forever).
  [].forEach.call(document.querySelectorAll('.mq-pause'), function (b) {
    b.addEventListener('click', function () {
      var on = b.getAttribute('aria-pressed') !== 'true';
      b.setAttribute('aria-pressed', on);
      b.previousElementSibling.classList.toggle('paused', on);
      b.textContent = on ? b.dataset.play : b.dataset.pause;
    });
  });

  // Buy: Instagram links can't carry text, so copy a ready message (program + price) to paste in the chat.
  var ar0 = document.documentElement.dir === 'rtl';
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-msg]');
    if (!a) return;
    try { navigator.clipboard && navigator.clipboard.writeText(a.dataset.msg); } catch (err) {}
    var t = document.querySelector('.toast') || document.body.appendChild(document.createElement('div'));
    t.className = 'toast'; t.setAttribute('role', 'status');
    t.textContent = ar0 ? 'نسخنا رسالتك. الصقها في محادثة إنستغرام.' : 'Message copied. Paste it in the Instagram chat.';
    t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('on'); }, 4000);
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
      pv.setAttribute('aria-disabled', i === 0); nx.setAttribute('aria-disabled', i === items.length - 1);
    }
    function go(k) {
      var it = items[Math.max(0, Math.min(items.length - 1, k))];
      var dx = it.getBoundingClientRect().left - box.getBoundingClientRect().left - (box.clientWidth - it.offsetWidth) / 2;
      box.scrollBy({ left: dx, behavior: still ? 'auto' : 'smooth' });
    }
    // aria-disabled (not disabled) so keyboard focus stays on the button at either end.
    pv.addEventListener('click', function () { if (pv.getAttribute('aria-disabled') !== 'true') go(current() - 1); });
    nx.addEventListener('click', function () { if (nx.getAttribute('aria-disabled') !== 'true') go(current() + 1); });
    box.addEventListener('scroll', function () { requestAnimationFrame(paint); }, { passive: true });
    addEventListener('resize', function () { cur = -1; paint(); });
    paint();
  });
})();

// Home photos sit just below the header (and the preview note while it is on screen).
(function () {
  var nav = document.querySelector('header.nav'), root = document.documentElement;
  if (!nav || !document.querySelector('.seg')) return;
  var last = -1, busy = false;
  function set() {
    busy = false;
    var b = Math.max(0, Math.round(nav.getBoundingClientRect().bottom));
    if (b !== last) { last = b; root.style.setProperty('--bgtop', b + 'px'); }
    root.style.setProperty('--navh', nav.offsetHeight + 'px');
  }
  function ask() { if (!busy) { busy = true; requestAnimationFrame(set); } }
  addEventListener('scroll', ask, { passive: true });
  addEventListener('resize', ask);
  set();
})();

// 15 Oct, Abdullah: the home page scrolls freely. Only the big title photos (the bands) pull the page in:
// when a scroll comes to rest just short of a band it eases on to show the whole band, and when it comes to
// rest just past one it eases back. Scrolling away from a band is never pulled back.
(function () {
  if (!document.querySelector('.seg .band')) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var nav = document.querySelector('header.nav'), bands = [].slice.call(document.querySelectorAll('.seg .band'));
  var last = scrollY, dir = 0, idle = 0, touching = false, anim = 0;
  function stop() { if (anim) { cancelAnimationFrame(anim); anim = 0; } }
  function go(to) {
    var a = scrollY, d = to - a, T = 380 + Math.min(320, Math.abs(d) * 0.6), s = performance.now();
    (function step(n) {
      var k = Math.min(1, (n - s) / T), e = 1 - Math.pow(1 - k, 3);
      scrollTo({ top: a + d * e, behavior: 'instant' });
      anim = k < 1 ? requestAnimationFrame(step) : 0;
    })(s);
  }
  function settle() {
    if (touching || anim || !dir) return;
    var h = nav ? nav.offsetHeight : 0, zone = innerHeight * 0.28;
    for (var i = 0; i < bands.length; i++) {
      var off = bands[i].getBoundingClientRect().top - h;   // how far the band's top is from where it should sit
      if (Math.abs(off) < 2) return;
      if ((dir > 0 && off > 0 && off < zone) || (dir < 0 && off < 0 && -off < zone * 0.6)) { go(scrollY + off); return; }
    }
  }
  addEventListener('scroll', function () {
    if (anim) return;
    var y = scrollY; if (y !== last) dir = y > last ? 1 : -1; last = y;
    clearTimeout(idle); idle = setTimeout(settle, 160);
  }, { passive: true });
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) { addEventListener(ev, stop, { passive: true }); });
  addEventListener('touchstart', function () { touching = true; }, { passive: true });
  addEventListener('touchend', function () { touching = false; clearTimeout(idle); idle = setTimeout(settle, 220); }, { passive: true });
})();
