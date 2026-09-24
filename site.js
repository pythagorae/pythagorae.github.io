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

    // Capabilities carousel: transform-based, so page scrolling can never desync it.
    var car = document.querySelector('.carousel');
    if (car) {
      var vp = car.querySelector('.viewport');
      var track = car.querySelector('.track');
      var slides = car.querySelectorAll('.slide');
      var dots = car.querySelectorAll('.dot');
      var N = slides.length, DUR = 6000, cur = 0, timer = null;
      var hover = false, kbFocus = false, visible = false;
      car.style.setProperty('--dur', DUR + 'ms');
      if (still) car.classList.add('still');

      function render(offsetPx) {
        track.style.transform = 'translateX(calc(' + (-100 * cur) + '% + ' + (offsetPx || 0) + 'px))';
      }
      function markDots() {
        dots.forEach(function (d, k) {
          d.classList.remove('on');
          d.setAttribute('aria-current', k === cur ? 'true' : 'false');
        });
        void car.offsetWidth; // restart the progress fill
        dots[cur].classList.add('on');
        slides.forEach(function (s, k) { s.setAttribute('aria-hidden', k === cur ? 'false' : 'true'); });
      }
      function stop() { clearTimeout(timer); timer = null; }
      function restart() {
        stop();
        var on = !still && !hover && !kbFocus && visible && !document.hidden;
        car.classList.toggle('paused', !on);
        if (on) timer = setTimeout(function () { go(cur + 1); }, DUR);
      }
      function go(i) {
        cur = ((i % N) + N) % N;
        render(0);
        markDots();
        restart();
      }

      car.querySelector('.prev').addEventListener('click', function () { go(cur - 1); });
      car.querySelector('.next').addEventListener('click', function () { go(cur + 1); });
      dots.forEach(function (d, k) { d.addEventListener('click', function () { go(k); }); });
      vp.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); go(cur + 1); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); go(cur - 1); }
      });

      // Swipe / drag. touch-action: pan-y keeps vertical page scrolling native.
      var sx = 0, sy = 0, dx = 0, dragging = false, decided = false, horizontal = false, pid = null;
      vp.addEventListener('pointerdown', function (e) {
        if (e.pointerType === 'mouse' && e.button !== 0) return;
        dragging = true; decided = false; horizontal = false; dx = 0;
        sx = e.clientX; sy = e.clientY; pid = e.pointerId;
      });
      vp.addEventListener('pointermove', function (e) {
        if (!dragging || e.pointerId !== pid) return;
        var mx = e.clientX - sx, my = e.clientY - sy;
        if (!decided && (Math.abs(mx) > 6 || Math.abs(my) > 6)) {
          decided = true; horizontal = Math.abs(mx) > Math.abs(my);
          if (horizontal) { track.classList.add('dragging'); try { vp.setPointerCapture(pid); } catch (err) {} stop(); }
          else { dragging = false; }
        }
        if (horizontal) { dx = mx; render(dx); }
      });
      function endDrag() {
        if (!dragging) return;
        dragging = false;
        track.classList.remove('dragging');
        if (!horizontal) return;
        var w = vp.clientWidth || 1;
        if (dx < -Math.min(60, w * .15)) go(cur + 1);
        else if (dx > Math.min(60, w * .15)) go(cur - 1);
        else go(cur);
      }
      vp.addEventListener('pointerup', endDrag);
      vp.addEventListener('pointercancel', endDrag);
      vp.addEventListener('lostpointercapture', endDrag);
      vp.addEventListener('click', function (e) { if (horizontal && Math.abs(dx) > 6) { e.preventDefault(); e.stopPropagation(); } }, true);

      // Pause only while someone is actually engaged with it.
      car.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') { hover = true; restart(); } });
      car.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') { hover = false; restart(); } });
      car.addEventListener('focusin', function (e) {
        var kb = false; try { kb = e.target.matches(':focus-visible'); } catch (err) {}
        if (kb) { kbFocus = true; restart(); }
      });
      car.addEventListener('focusout', function () { if (kbFocus) { kbFocus = false; restart(); } });
      document.addEventListener('visibilitychange', restart);
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) { visible = es[0].isIntersecting; restart(); }, { threshold: 0.35 }).observe(car);
      } else { visible = true; }
      go(0);
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
