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

    // Cards: glow follows the pointer.
    document.querySelectorAll('.card').forEach(function (card) {
      card.addEventListener('pointermove', function (ev) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (ev.clientX - r.left) + 'px');
        card.style.setProperty('--my', (ev.clientY - r.top) + 'px');
      });
    });

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
