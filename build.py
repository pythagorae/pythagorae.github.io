#!/usr/bin/env python3
"""Generate index.html (English, default) and es/index.html (Spanish) from one template.

Edit the copy in T below, then run: python3 build.py
"""
from pathlib import Path

from art import ART

ROOT = Path(__file__).parent


T = {
    "en": {
        "path": "index.html",
        "url": "https://pythagorae.com/",
        "title": "Pythagorae — Engineering for hard, complex systems",
        "desc": "Pythagorae — software, artificial intelligence, high-performance computing and space-systems engineering. Córdoba, Argentina.",
        "nav": ["Capabilities", "Team", "Contact"],
        "other": ("/es/", "es", "ES"),
        "eyebrow": "Pythagorae S.A.S. &middot; C&oacute;rdoba, Argentina",
        "h1": 'Engineering for <span class="grad">hard, complex systems.</span>',
        "lede": "Artificial intelligence, high-performance computing and space systems &mdash; from raw data to production systems.",
        "cta1": "Talk to us",
        "cta2": "Our capabilities",
        "statement": "We build software that turns raw, complex data into something you can trust.",
        "principles": [
            ("First principles", "We understand the whole system before we change it &mdash; physics, data and code."),
            ("Built to be correct", "Mission-critical habits: tested, measured, verified before it ships."),
            ("End to end", "From sensor to model to production &mdash; one team."),
        ],
        "cap_h": "Capabilities",
        "caps": [
            ("ai", "Artificial intelligence &amp; machine learning", "Model development, training and evaluation; reinforcement learning; integration of large language models into real systems."),
            ("decision", "Optimal solvers for AI", "Extending language models with search, planning, optimization engines and imperfect-information solvers &mdash; so AI agents reach optimal decisions, not just plausible ones."),
            ("local", "Local &amp; sovereign LLM inference", "Open language models on your own hardware, or on infrastructure we manage for you &mdash; served with an open-source stack you can audit, so privacy is verifiable, not promised. GPU sizing, quantization, fine-tuning. Your data never leaves your jurisdiction."),
            ("signal", "Signal &amp; data processing", "High-volume sensor and telemetry data &mdash; from raw streams and undocumented formats to calibrated, usable products."),
            ("hpc", "High-performance &amp; distributed systems", "GPU and HPC computing, cloud and on-premise infrastructure, reliable systems in production."),
            ("space", "Space &amp; ground systems", "Software for satellite, ground-segment and scientific systems, where correctness is not optional."),
        ],
        "team_h": "Team",
        "team_sub": "The people behind the work.",
        "team": [
            ("felipe", "Felipe", "Satellite systems &middot; radar &middot; distributed systems &middot; AI"),
            ("ismael", "Ismael", "Search &middot; planning &middot; reinforcement learning"),
            ("agustin", "Agust&iacute;n", "Game theory &middot; imperfect-information solvers"),
        ],
        "contact_h": "Have a hard problem?",
        "contact_p": "Tell us about it. We reply to every message.",
        "contact_btn": "founder@pythagorae.com",
        "legal": "Pythagorae S.A.S. &middot; CUIT 30-71960531-8 &middot; Villa Carlos Paz, C&oacute;rdoba, Argentina",
    },
    "es": {
        "path": "es/index.html",
        "url": "https://pythagorae.com/es/",
        "title": "Pythagorae — Ingeniería para sistemas complejos",
        "desc": "Pythagorae — ingeniería de software, inteligencia artificial, cómputo de alto rendimiento y sistemas espaciales. Córdoba, Argentina.",
        "nav": ["Capacidades", "Equipo", "Contacto"],
        "other": ("/", "en", "EN"),
        "eyebrow": "Pythagorae S.A.S. &middot; C&oacute;rdoba, Argentina",
        "h1": 'Ingenier&iacute;a para <span class="grad">sistemas dif&iacute;ciles y complejos.</span>',
        "lede": "Inteligencia artificial, c&oacute;mputo de alto rendimiento y sistemas espaciales &mdash; de los datos crudos a sistemas en producci&oacute;n.",
        "cta1": "Hablemos",
        "cta2": "Nuestras capacidades",
        "statement": "Construimos software que convierte datos crudos y complejos en algo en lo que se puede confiar.",
        "principles": [
            ("Primeros principios", "Entendemos el sistema completo antes de cambiarlo &mdash; f&iacute;sica, datos y c&oacute;digo."),
            ("Hecho para ser correcto", "H&aacute;bitos de misi&oacute;n cr&iacute;tica: probado, medido y verificado antes de entregarse."),
            ("De punta a punta", "Del sensor al modelo y a producci&oacute;n &mdash; un solo equipo."),
        ],
        "cap_h": "Capacidades",
        "caps": [
            ("ai", "Inteligencia artificial y aprendizaje autom&aacute;tico", "Desarrollo, entrenamiento y evaluaci&oacute;n de modelos; aprendizaje por refuerzo; integraci&oacute;n de modelos de lenguaje en sistemas reales."),
            ("decision", "Solvers &oacute;ptimos para IA", "Extendemos modelos de lenguaje con b&uacute;squeda, planificaci&oacute;n, motores de optimizaci&oacute;n y solvers de informaci&oacute;n imperfecta &mdash; para que los agentes de IA lleguen a decisiones &oacute;ptimas, no solo plausibles."),
            ("local", "Inferencia de LLM local y soberana", "Modelos de lenguaje abiertos en tu propio hardware, o en infraestructura que gestionamos para vos &mdash; servidos con un stack de c&oacute;digo abierto que pod&eacute;s auditar: la privacidad se verifica, no se promete. Dimensionamiento de GPU, cuantizaci&oacute;n, fine-tuning. Tus datos no salen de tu jurisdicci&oacute;n."),
            ("signal", "Procesamiento de se&ntilde;ales y datos", "Datos de sensores y telemetr&iacute;a en gran volumen &mdash; de flujos crudos y formatos sin documentar a productos calibrados y utilizables."),
            ("hpc", "Sistemas distribuidos y de alto rendimiento", "C&oacute;mputo en GPU y HPC, infraestructura en la nube y propia, sistemas confiables en producci&oacute;n."),
            ("space", "Sistemas espaciales y de segmento terreno", "Software para sistemas satelitales, de segmento terreno y cient&iacute;ficos, donde la correcci&oacute;n no es opcional."),
        ],
        "team_h": "Equipo",
        "team_sub": "Las personas detr&aacute;s del trabajo.",
        "team": [
            ("felipe", "Felipe", "Sistemas satelitales &middot; radar &middot; sistemas distribuidos &middot; IA"),
            ("ismael", "Ismael", "B&uacute;squeda &middot; planificaci&oacute;n &middot; aprendizaje por refuerzo"),
            ("agustin", "Agust&iacute;n", "Teor&iacute;a de juegos &middot; solvers de informaci&oacute;n imperfecta"),
        ],
        "contact_h": "&iquest;Ten&eacute;s un problema dif&iacute;cil?",
        "contact_p": "Contanos. Respondemos todos los mensajes.",
        "contact_btn": "founder@pythagorae.com",
        "legal": "Pythagorae S.A.S. &middot; CUIT 30-71960531-8 &middot; Villa Carlos Paz, C&oacute;rdoba, Argentina",
    },
}

# Tetractys: 4 rows (1,2,3,4 nodes) on a triangular lattice, apex = the monad (bronze).
S, H = 70, 60.6
NODES = [(200 + (i - r / 2) * S, 60 + r * H * 1.25) for r in range(4) for i in range(r + 1)]
def _edges():
    idx, k = {}, 0
    for r in range(4):
        for i in range(r + 1):
            idx[(r, i)] = k; k += 1
    out = []
    for (r, i), a in idx.items():
        for nb in ((r, i + 1), (r + 1, i), (r + 1, i + 1)):
            if nb in idx:
                out.append((a, idx[nb]))
    return out
EDGES = _edges()


def tetractys_svg():
    lines = "".join(
        f'<line class="edge" style="--d:{n * 0.07:.2f}s" x1="{NODES[a][0]:.1f}" y1="{NODES[a][1]:.1f}" x2="{NODES[b][0]:.1f}" y2="{NODES[b][1]:.1f}"/>'
        for n, (a, b) in enumerate(EDGES)
    )
    dots = "".join(
        f'<circle class="node{" monad" if k == 0 else ""}" style="--d:{0.4 + k * 0.09:.2f}s" cx="{x:.1f}" cy="{y:.1f}" r="{13 if k == 0 else 11}"/>'
        for k, (x, y) in enumerate(NODES)
    )
    return (
        '<svg class="tetractys" viewBox="0 0 400 360" aria-hidden="true">'
        f'<g class="edges">{lines}</g><g class="nodes">{dots}</g></svg>'
    )



def page(lang, t):
    other_href, other_lang, other_label = t["other"]
    home = "/" if lang == "en" else "/es/"
    caps = "".join(
        f'''
        <article class="card reveal" style="--i:{n}">
          <div class="card-art">{ART[key]()}</div>
          <div class="card-body">
          <span class="num">0{n + 1}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
          </div>
        </article>''' for n, (key, title, desc) in enumerate(t["caps"])
    )
    principles = "".join(
        f'<div class="principle reveal" style="--i:{n}"><h3>{h}</h3><p>{p}</p></div>'
        for n, (h, p) in enumerate(t["principles"])
    )
    team = "".join(
        f'''
        <figure class="person reveal" style="--i:{n}">
          <div class="photo"><img src="/assets/team/{slug}.jpg" alt="{name}" width="400" height="400" loading="lazy"></div>
          <figcaption><strong>{name}</strong><span>{role}</span></figcaption>
        </figure>''' for n, (slug, name, role) in enumerate(t["team"])
    )
    n1, n2, n3 = t["nav"]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta name="theme-color" content="#060c1c">
<meta property="og:title" content="Pythagorae">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:image" content="https://pythagorae.com/assets/og.png">
<meta property="og:url" content="{t["url"]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="https://pythagorae.com/">
<link rel="alternate" hreflang="es" href="https://pythagorae.com/es/">
<link rel="alternate" hreflang="x-default" href="https://pythagorae.com/">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v=9">
<script defer src="/site.js?v=8"></script>
</head>
<body>

<header class="bar">
  <div class="wrap bar-in">
    <a class="brand" href="{home}" aria-label="Pythagorae"><img src="/assets/lockup-horizontal-cream.svg" alt="Pythagorae" height="22"></a>
    <nav>
      <a href="#capabilities">{n1}</a>
      <a href="#team">{n2}</a>
      <a href="#contact">{n3}</a>
      <a class="lang" href="{other_href}" hreflang="{other_lang}" lang="{other_lang}">{other_label}</a>
    </nav>
  </div>
</header>

<section class="hero">
  <canvas id="sky" aria-hidden="true"></canvas>
  <div class="milky" aria-hidden="true"></div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="lede">{t["lede"]}</p>
      <div class="ctas">
        <a class="btn primary" href="#contact">{t["cta1"]}</a>
        <a class="btn ghost" href="#capabilities">{t["cta2"]} <span aria-hidden="true">&darr;</span></a>
      </div>
    </div>
    <div class="hero-art">{tetractys_svg()}</div>
  </div>
</section>

<section class="statement">
  <div class="wrap">
    <blockquote class="reveal">{t["statement"]}</blockquote>
    <div class="principles">{principles}</div>
  </div>
</section>

<section id="capabilities" class="section">
  <div class="wrap">
    <header class="section-head reveal"><h2>{t["cap_h"]}</h2></header>
    <div class="grid">{caps}
    </div>
  </div>
</section>

<section id="team" class="section alt">
  <div class="wrap">
    <header class="section-head reveal"><h2>{t["team_h"]}</h2><p>{t["team_sub"]}</p></header>
    <div class="team">{team}
    </div>
  </div>
</section>

<section id="contact" class="contact">
  <div class="wrap reveal">
    <h2>{t["contact_h"]}</h2>
    <p>{t["contact_p"]}</p>
    <a class="btn primary big" href="mailto:founder@pythagorae.com">{t["contact_btn"]}</a>
  </div>
</section>

<footer class="foot">
  <div class="wrap foot-in">
    <ul class="social">
      <li><a href="https://github.com/pythagorae" target="_blank" rel="noopener">GitHub</a></li>
      <li><a href="https://huggingface.co/pythagorae" target="_blank" rel="noopener">Hugging Face</a></li>
      <li><a href="https://www.linkedin.com/company/pythagorae" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://x.com/pythagorae_ai" target="_blank" rel="noopener">X</a></li>
      <li><a href="https://www.youtube.com/@pythagorae" target="_blank" rel="noopener">YouTube</a></li>
    </ul>
    <p class="legal">{t["legal"]}</p>
  </div>
</footer>

</body>
</html>
'''


if __name__ == "__main__":
    for lang, t in T.items():
        out = ROOT / t["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, t), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
