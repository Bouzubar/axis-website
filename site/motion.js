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

// 15 Oct, Abdullah: home scrolls like turning pages. When a scroll comes to rest between two sections,
// the page eases on to the whole next section in the direction it was going (or back, if it barely moved)
// and stays there until the next swipe. Inside a section taller than the screen it scrolls freely.
// A fast scroll is never stopped mid-way: it settles on the nearest section where it comes to rest.
(function () {
  if (!document.body.classList.contains('home') || !document.querySelector('.seg')) return;
  var secs0 = [].slice.call(document.querySelectorAll('.seg > section'));
  if (matchMedia('(hover: none) and (pointer: coarse)').matches) {
    // Touch: the browser snaps (CSS). Mark each section's top, and the bottom of a long one; a short
    // strip (the numbers) rides with the page above.
    function marks() {
      var room = innerHeight - (document.querySelector('header.nav') || { offsetHeight: 0 }).offsetHeight;
      secs0.forEach(function (s, i) {
        [].slice.call(s.querySelectorAll(':scope > .snap-s, :scope > .snap-e')).forEach(function (m) { m.remove(); });
        if (i && s.offsetHeight < innerHeight * 0.45) return;
        // A section that fits is its own stop (bands clip their overflow, so marks inside them would not count).
        s.classList.toggle('snap-a', s.offsetHeight <= room + 2);
        if (s.offsetHeight <= room + 2) return;
        ['snap-s', 'snap-e'].forEach(function (c) { var m = document.createElement('i'); m.className = c; m.setAttribute('aria-hidden', 'true'); s.appendChild(m); });
      });
    }
    // A short or gentle swipe that the browser would spring back still turns one page in its direction.
    function stopsT() {
      var h = (document.querySelector('header.nav') || { offsetHeight: 0 }).offsetHeight, vh = innerHeight,
        max = document.documentElement.scrollHeight - vh, out = [0, max];
      document.querySelectorAll('.home .seg > section.snap-a, .home .snap-s, .home .snap-e').forEach(function (el) {
        var r = el.getBoundingClientRect(), y = el.classList.contains('snap-e') ? r.bottom + scrollY - vh : r.top + scrollY - h;
        if (el.classList.contains('h-hero')) y = 0;
        out.push(Math.max(0, Math.min(max, Math.round(y))));
      });
      return out.sort(function (a, b) { return a - b; });
    }
    var ty = 0, sy = 0, dy = 0, tt = 0;
    addEventListener('touchstart', function (e) { ty = e.touches[0].clientY; sy = scrollY; dy = 0; clearTimeout(tt); }, { passive: true });
    addEventListener('touchmove', function (e) { dy = ty - e.touches[0].clientY; }, { passive: true });
    addEventListener('touchend', function () {
      if (Math.abs(dy) < 40) return;
      var d = dy, check = function () {
        if (Math.abs(scrollY - sy) > 6) return;              // the browser already turned the page
        var list = stopsT(), to = d > 0 ? list.filter(function (p) { return p > sy + 6; })[0] : list.filter(function (p) { return p < sy - 6; }).pop();
        if (to != null) scrollTo({ top: to, behavior: 'smooth' });
      };
      tt = setTimeout(check, 450);
    }, { passive: true });
    marks(); document.documentElement.classList.add('snapon'); var rz = 0, w0 = innerWidth;   // the address bar hiding changes the height only: keep the marks
    addEventListener('resize', function () { if (innerWidth === w0) return; w0 = innerWidth; clearTimeout(rz); rz = setTimeout(marks, 200); });
    return;
  }
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var nav = document.querySelector('header.nav'), secs = [].slice.call(document.querySelectorAll('.seg > section'));
  var from = scrollY, idle = 0, touching = false, anim = 0, t0 = 0, moved = 0;
  function navh() { return nav ? nav.offsetHeight : 0; }
  function stops() {
    var h = navh(), vh = innerHeight, max = document.documentElement.scrollHeight - vh, out = [0, max];
    secs.forEach(function (s, i) {
      var r = s.getBoundingClientRect(), top = r.top + scrollY;
      if (i && r.height > vh * 0.45) out.push(top - h);   // a short strip (the numbers) rides with the page above
      if (r.height > vh - h + 2) out.push(top + r.height - vh);   // the end of a long section is a page too
    });
    return out.map(function (y) { return Math.max(0, Math.min(max, Math.round(y))); })
      .sort(function (a, b) { return a - b; }).filter(function (y, i, a) { return !i || y - a[i - 1] > 8; });
  }
  function inside(y) {   // resting inside a long section, with nothing else on screen: leave it be
    var h = navh(), vh = innerHeight;
    return secs.some(function (s) { var r = s.getBoundingClientRect(), top = r.top + scrollY;
      return top - h < y - 2 && top + r.height > y + vh + 2; });
  }
  function stop() { if (anim) { cancelAnimationFrame(anim); anim = 0; } }
  function go(to) {
    var a = scrollY, d = to - a, T = Math.min(900, 420 + Math.abs(d) * 0.45), s = performance.now();
    if (Math.abs(d) < 2) { from = scrollY; return; }
    stop();
    (function step(n) {
      var k = Math.min(1, (n - s) / T), e = k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
      scrollTo({ top: a + d * e, behavior: 'instant' });
      if (k < 1) anim = requestAnimationFrame(step); else { anim = 0; from = scrollY; }
    })(s);
  }
  function settle() {
    if (touching || anim) return;
    var y = scrollY, d = y - from, list = stops(), vh = innerHeight;
    if (list.indexOf(Math.round(y)) > -1 || inside(y)) { from = y; return; }
    var dt = performance.now() - t0, fast = Math.abs(d) > vh * 1.2 || Math.abs(d) / Math.max(dt, 1) > 3;
    var down = list.filter(function (p) { return p > y; })[0], up = list.filter(function (p) { return p < y; }).pop();
    if (down == null) down = up; if (up == null) up = down;
    var near = (y - up) < (down - y) ? up : down, to;
    if (fast || Math.abs(d) < 24) to = near;          // a fling settles where it is; a nudge falls back
    else to = d > 0 ? down : up;                      // otherwise turn the page the way it was going
    go(to);
  }
  addEventListener('scroll', function () {
    if (anim) return;
    if (!idle) t0 = performance.now();
    clearTimeout(idle); idle = setTimeout(function () { idle = 0; settle(); }, 140);
  }, { passive: true });
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) {
    addEventListener(ev, function () { if (anim) { stop(); from = scrollY; } }, { passive: true });
  });
  addEventListener('touchstart', function () { touching = true; }, { passive: true });
  addEventListener('touchend', function () { touching = false; clearTimeout(idle); idle = setTimeout(function () { idle = 0; settle(); }, 160); }, { passive: true });
  addEventListener('hashchange', function () { from = scrollY; });
})();
