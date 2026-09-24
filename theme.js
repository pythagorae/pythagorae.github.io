(function () {
  var root = document.documentElement;

  function effective() {
    return root.getAttribute('data-theme') || 'dark';
  }

  function setLabel() {
    var b = document.querySelector('.theme');
    var es = root.lang === 'es';
    if (b) b.textContent = effective() === 'dark' ? (es ? 'Claro' : 'Light') : (es ? 'Oscuro' : 'Dark');
  }

  window.toggleTheme = function () {
    var next = effective() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
    setLabel();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setLabel);
  } else {
    setLabel();
  }
})();
