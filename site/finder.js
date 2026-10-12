// AXIS Program Finder: questions, then a recommended plan. Data comes from #fd-data (built by finder.py).
(function () {
  var D = JSON.parse(document.getElementById('fd-data').textContent);
  var root = document.getElementById('finder');
  var $ = function (s) { return root.querySelector(s); };
  var A = {}, hist = [];

  function steps() {
    var s = ['goal', 'pain'];
    if (A.goal === 'sport') s.push('sport', 'season');
    if (A.goal === 'muscle') s.push('days', 'focus');
    s.push('exp');
    return s;
  }

  function options(key) {
    var o = D[key][1];
    if (key === 'pain' && A.goal === 'pain') o = o.filter(function (x) { return x[0] !== 'none'; });
    if (key === 'focus') o = o.filter(function (x) {
      if (x[0] === 'glutes') return A.days === '3' || A.days === '4';
      if (x[0] === 'split') return A.days === '5';
      return true;
    });
    return o;
  }

  function show(key) {
    var s = steps(), i = s.indexOf(key);
    var opts = options(key);
    if (opts.length === 1) { A[key] = opts[0][0]; return next(key); }
    $('.fd-intro').hidden = true; $('.fd-res').hidden = true; $('.fd-q').hidden = false;
    $('.fd-count').textContent = D.step + ' ' + (i + 1) + ' ' + D.of + ' ' + s.length;
    $('.fd-title').textContent = D[key][0];
    var hint = $('.fd-hint'); hint.hidden = key !== 'pain'; hint.textContent = D.pain_hint;
    var box = $('.fd-opts'); box.innerHTML = '';
    opts.forEach(function (o) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'fd-opt' + (A[key] === o[0] ? ' on' : ''); b.textContent = o[1];
      b.onclick = function () { A[key] = o[0]; hist.push(key); next(key); };
      box.appendChild(b);
    });
    $('.fd-back').hidden = hist.length === 0;
    root.scrollIntoView({ block: 'start' });
  }

  function next(key) {
    var s = steps(), i = s.indexOf(key);
    if (i + 1 < s.length) show(s[i + 1]); else result();
  }

  function label(key) {
    var f = D[key][1].filter(function (x) { return x[0] === A[key]; })[0];
    return f ? f[1] : '';
  }

  function fill(str, map) { return str.replace(/\{(\w+)\}/g, function (_, k) { return map[k] || ''; }); }

  function mainPick() {
    var W = D.why;
    if (A.goal === 'sport') {
      return { slug: A.sport.replace('_', '-') + '-' + A.season,
               why: fill(W.perf, { sport: D.sport_txt[A.sport], season: D.season_txt[A.season] }) };
    }
    if (A.goal === 'muscle') {
      var d = A.days, f = A.focus, slug, extra = '';
      if (d === '3') slug = f === 'glutes' ? 'glute-emphasis-3day' : 'full-body';
      else if (d === '4') slug = f === 'glutes' ? 'glute-emphasis-4day' : 'upper-lower';
      else if (d === '5') slug = f === 'split' ? 'body-part' : 'ppl-upper-lower';
      else if (A.exp === 'adv') slug = 'push-pull-legs';
      else { slug = 'ppl-upper-lower'; extra = ' ' + W.phys_adv; d = '5'; }
      return { slug: slug, why: fill(W.phys, { days: d, focus: D.focus_txt[f] || '' }) + extra };
    }
    if (A.exp === 'new') return { slug: 'foundation-strength', why: W.foundation };
    return { slug: 'athletic-development', why: W.athletic };
  }

  function plan() {
    var out = [];
    if (A.pain && A.pain !== 'none') {
      out.push({ slug: A.pain, why: D.progs[A.pain].series === 'return' ? D.why.rts : fill(D.why.corrective, { area: D.area_txt[A.pain] }) });
    }
    var m = mainPick();
    if (A.exp === 'new' && m.slug !== 'foundation-strength') out.push({ slug: 'foundation-strength', why: D.why.foundation });
    out.push(m);
    return out;
  }

  function card(step, i) {
    var p = D.progs[step.slug];
    var lead = i === 0 ? D.first : D.then;
    return '<article class="fd-card"><div class="fd-img"><img data-cover="' + step.slug + '" src="' + D.prefix + (window.axisCover ? window.axisCover(step.slug) : 'img/covers/' + step.slug + '.jpg') + '" alt="" loading="lazy"></div>' +
      '<div class="fd-body"><div class="mono gold">' + (i + 1) + ' · ' + lead + '</div><h3>' + p.name + '</h3>' +
      '<div class="mono dim">' + p.wl + ' · ' + p.price + ' ' + D.kd + '</div>' +
      '<p>' + step.why + '</p><a class="link" href="' + D.base + step.slug + '/index.html">' + D.view + ' <span class="arr">→</span></a></div></article>';
  }

  function result() {
    $('.fd-q').hidden = true; $('.fd-res').hidden = false;
    var keys = steps();
    $('.fd-chips').innerHTML = keys.map(function (k) { return '<li>' + label(k) + '</li>'; }).join('');
    var pl = plan();
    $('.fd-cards').innerHTML = pl.map(card).join('');
    var extra = '';
    var corr = pl.some(function (x) { return D.progs[x.slug].series === 'corrective'; });
    var twelve = pl.some(function (x) { return D.progs[x.slug].weeks === 12; });
    var big = pl.filter(function (x) { return D.progs[x.slug].weeks === 12; }).pop();
    if (corr && big) extra += '<p class="fd-bundle">' + D.bundle + ' <span class="price">' + D.progs[big.slug].combo + '</span></p>';
    var last = D.progs[pl[pl.length - 1].slug];
    if (last.series === 'performance') {
      var fam = last.family.replace('_', '-');
      extra += '<div class="fd-year"><h3>' + D.year + '</h3><p class="dim">' + D.year_p + '</p><ol>' +
        ['base', 'build', 'compete', 'restore'].map(function (b) {
          var s = fam + '-' + b;
          return '<li class="' + (b === last.block ? 'on' : '') + '"><a href="' + D.base + s + '/index.html">' + D.block[b] + '</a></li>';
        }).join('') + '</ol></div>';
    }
    $('.fd-extra').innerHTML = extra;
    root.scrollIntoView({ block: 'start' });
  }

  $('.fd-start').onclick = function () { show('goal'); };
  $('.fd-back').onclick = function () { var k = hist.pop(); if (k) show(k); };
  $('.fd-restart').onclick = function () { A = {}; hist = []; show('goal'); };

  // The homepage tiles link here with ?goal=pain|general|sport|muscle: skip straight past question 1.
  var g = (location.search.match(/[?&]goal=(\w+)/) || [])[1];
  if (g && D.goal[1].some(function (x) { return x[0] === g; })) { A.goal = g; hist.push('goal'); next('goal'); }
})();
