(function () {
  var root = document.documentElement;
  root.classList.add('js');
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function ready(fn) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn);
    else fn();
  }

  ready(function () {
    // Top bar turns solid after scrolling past the top.
    var bar = document.querySelector('.bar');
    function onScroll() { bar.classList.toggle('scrolled', window.scrollY > 24); }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Reveal on scroll.
    var items = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && !still) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
      items.forEach(function (el) { io.observe(el); });
    } else {
      items.forEach(function (el) { el.classList.add('in'); });
    }

    // Capabilities carousel: autoplay, arrows, dots, swipe (native scroll-snap).
    var car = document.querySelector('.carousel');
    if (car) {
      var track = car.querySelector('.track');
      var slides = car.querySelectorAll('.slide');
      var dots = car.querySelectorAll('.dot');
      var DUR = 6000, cur = -1, timer = null, hover = false, visible = false;
      car.style.setProperty('--dur', DUR + 'ms');
      if (still) car.classList.add('still');

      function mark(i) {
        if (i === cur) return;
        cur = i;
        dots.forEach(function (d, k) {
          d.classList.remove('on');
          if (k === i) { void d.offsetWidth; d.classList.add('on'); }
          d.setAttribute('aria-current', k === i ? 'true' : 'false');
        });
      }
      function go(i) {
        i = (i + slides.length) % slides.length;
        track.scrollTo({ left: slides[i].offsetLeft, behavior: still ? 'auto' : 'smooth' });
        mark(i);
        restart();
      }
      function nearest() {
        var x = track.scrollLeft, best = 0, bd = Infinity;
        slides.forEach(function (s, k) { var d = Math.abs(s.offsetLeft - x); if (d < bd) { bd = d; best = k; } });
        return best;
      }
      function stop() { clearTimeout(timer); timer = null; }
      function restart() {
        stop();
        var on = !still && !hover && visible && !document.hidden;
        car.classList.toggle('paused', !on);
        if (on) timer = setTimeout(function () { go(cur + 1); }, DUR);
      }

      car.querySelector('.prev').addEventListener('click', function () { go(cur - 1); });
      car.querySelector('.next').addEventListener('click', function () { go(cur + 1); });
      dots.forEach(function (d, k) { d.addEventListener('click', function () { go(k); }); });
      track.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); go(cur + 1); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); go(cur - 1); }
      });
      var settle;
      track.addEventListener('scroll', function () {
        clearTimeout(settle);
        settle = setTimeout(function () { var n = nearest(); if (n !== cur) { mark(n); restart(); } }, 120);
      }, { passive: true });
      car.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') { hover = true; restart(); } });
      car.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') { hover = false; restart(); } });
      car.addEventListener('focusin', function () { hover = true; restart(); });
      car.addEventListener('focusout', function () { hover = false; restart(); });
      document.addEventListener('visibilitychange', restart);
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) { visible = es[0].isIntersecting; restart(); }, { threshold: 0.4 }).observe(car);
      } else { visible = true; }
      mark(0);
      restart();
    }

    // Starfield: twinkling stars with a slow drift and pointer parallax.
    var canvas = document.getElementById('sky');
    if (!canvas || !canvas.getContext) return;
    var ctx = canvas.getContext('2d');
    var stars = [], w = 0, h = 0, dpr = 1, px = 0, py = 0, tx = 0, ty = 0;

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = canvas.clientWidth; h = canvas.clientHeight;
      canvas.width = w * dpr; canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.round(w * h / 2600);
      stars = [];
      for (var i = 0; i < n; i++) {
        var z = Math.random();
        stars.push({
          x: Math.random() * w, y: Math.random() * h, z: z,
          r: 0.3 + z * 1.2, a: 0.25 + Math.random() * 0.75,
          s: 0.5 + Math.random() * 2, p: Math.random() * Math.PI * 2,
          warm: Math.random() < 0.08
        });
      }
    }

    function draw(t) {
      ctx.clearRect(0, 0, w, h);
      px += (tx - px) * 0.05; py += (ty - py) * 0.05;
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        var x = (s.x + t * 0.004 * s.z + px * s.z * 18) % w;
        if (x < 0) x += w;
        var y = s.y + py * s.z * 18;
        var tw = still ? s.a : s.a * (0.6 + 0.4 * Math.sin(t * 0.001 * s.s + s.p));
        ctx.beginPath();
        ctx.arc(x, y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.warm ? 'rgba(232,207,134,' + tw + ')' : 'rgba(226,232,245,' + tw + ')';
        ctx.fill();
      }
      if (!still) requestAnimationFrame(draw);
    }

    window.addEventListener('resize', resize);
    window.addEventListener('pointermove', function (ev) {
      tx = ev.clientX / window.innerWidth - 0.5;
      ty = ev.clientY / window.innerHeight - 0.5;
    }, { passive: true });
    resize();
    requestAnimationFrame(draw);
  });
})();
