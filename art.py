"""Animated SVG illustrations, one per capability. All drawn in a 320x160 box.

Colors come from CSS classes in style.css (.a-line, .a-dot, .a-hot, ...), so the
art follows the brand palette. Motion is CSS/SMIL and is disabled under
prefers-reduced-motion.
"""
import math
import random

W, H = 320, 160


def _svg(body):
    return f'<svg class="art" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{body}</svg>'


def ai():
    """Neural network: three layers, signals travelling along the edges."""
    layers = [[40, 80, 120], [30, 63, 97, 130], [55, 105]]
    xs = [80, 160, 240]
    out, k = [], 0
    for li in range(2):
        for y1 in layers[li]:
            for y2 in layers[li + 1]:
                x1, x2 = xs[li], xs[li + 1]
                out.append(f'<line class="a-line" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
                if k % 3 == 0:
                    out.append(
                        f'<circle class="a-pulse" r="2.2"><animateMotion dur="{2.2 + (k % 5) * .35:.2f}s" '
                        f'begin="{(k * .23) % 2:.2f}s" repeatCount="indefinite" path="M{x1},{y1} L{x2},{y2}"/></circle>'
                    )
                k += 1
    for li, ys in enumerate(layers):
        for j, y in enumerate(ys):
            cls = "a-hot" if li == 2 and j == 0 else "a-dot"
            out.append(f'<circle class="{cls} a-breathe" style="--d:{(li + j) * .3:.1f}s" cx="{xs[li]}" cy="{y}" r="6"/>')
    return _svg("".join(out))


def decision():
    """Search tree: many branches explored, one optimal path lit in bronze."""
    rnd = random.Random(7)
    out, best = [], []
    levels = [(160, 22)]
    nodes = [[(160, 22)]]
    for depth in range(1, 4):
        row = []
        for (px, py) in nodes[-1]:
            n = 3 if depth < 3 else 2
            spread = 90 / depth
            for i in range(n):
                x = px + (i - (n - 1) / 2) * spread
                y = 22 + depth * 38
                row.append((x, y))
                out.append(f'<line class="a-line" x1="{px:.1f}" y1="{py}" x2="{x:.1f}" y2="{y}"/>')
        nodes.append(row)
    # optimal path: pick a fixed chain
    path = [(160, 22)]
    for depth in range(1, 4):
        px, _ = path[-1]
        cands = [p for p in nodes[depth] if abs(p[0] - px) < 95 / depth]
        path.append(cands[len(cands) // 2 + (1 if depth == 2 else 0)] if len(cands) > 1 else cands[0])
    d = "M" + " L".join(f"{x:.1f},{y}" for x, y in path)
    for row in nodes:
        for (x, y) in row:
            out.append(f'<circle class="a-dot" cx="{x:.1f}" cy="{y}" r="{4.5 if y < 30 else 3.2}"/>')
    out.append(f'<path class="a-best" d="{d}"/>')
    for i, (x, y) in enumerate(path):
        out.append(f'<circle class="a-hot a-breathe" style="--d:{i * .25:.2f}s" cx="{x:.1f}" cy="{y}" r="5"/>')
    return _svg("".join(out))


def local():
    """A chip with a glowing die; data flows in and out along the traces."""
    out = []
    cx, cy = 160, 80
    for side in range(4):
        for i in range(5):
            o = -32 + i * 16
            if side == 0:   a, b = (cx + o, cy - 38), (cx + o, 6)
            elif side == 1: a, b = (cx + o, cy + 38), (cx + o, 154)
            elif side == 2: a, b = (cx - 38, cy + o * .8), (40, cy + o * .8)
            else:           a, b = (cx + 38, cy + o * .8), (280, cy + o * .8)
            out.append(f'<line class="a-line" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>')
            if (side + i) % 2 == 0:
                out.append(
                    f'<circle class="a-pulse" r="2"><animateMotion dur="{1.8 + i * .3:.1f}s" begin="{(side * .4 + i * .2):.1f}s" '
                    f'repeatCount="indefinite" path="M{b[0]:.1f},{b[1]:.1f} L{a[0]:.1f},{a[1]:.1f}"/></circle>'
                )
    out.append(f'<rect class="a-chip" x="{cx - 38}" y="{cy - 38}" width="76" height="76" rx="8"/>')
    out.append(f'<rect class="a-die a-breathe" x="{cx - 20}" y="{cy - 20}" width="40" height="40" rx="4"/>')
    out.append(f'<text class="a-label" x="{cx}" y="{cy + 4}" text-anchor="middle">LLM</text>')
    return _svg("".join(out))


def signal():
    """Noisy raw signal on the left becomes a clean spectrum on the right."""
    rnd = random.Random(3)
    pts = []
    for i in range(0, 141, 3):
        y = 80 + 26 * math.sin(i / 9) * math.cos(i / 23) + rnd.uniform(-14, 14)
        pts.append(f"{20 + i},{y:.1f}")
    out = [f'<polyline class="a-raw" points="{" ".join(pts)}"/>']
    out.append('<path class="a-arrow" d="M168 80 h18 m-6 -6 l6 6 l-6 6"/>')
    heights = [18, 34, 70, 104, 62, 30, 46, 88, 40, 20, 12]
    for i, h in enumerate(heights):
        x = 200 + i * 10
        cls = "a-bar-hot" if h > 85 else "a-bar"
        out.append(f'<rect class="{cls} a-grow" style="--d:{i * .12:.2f}s" x="{x}" y="{140 - h}" width="6" height="{h}" rx="1.5"/>')
    out.append('<line class="a-axis" x1="196" y1="141" x2="312" y2="141"/>')
    return _svg("".join(out))


def hpc():
    """A grid of compute nodes lighting up in waves."""
    out = []
    cols, rows = 9, 4
    for r in range(rows):
        for c in range(cols):
            x, y = 40 + c * 30, 32 + r * 32
            if c < cols - 1:
                out.append(f'<line class="a-line" x1="{x}" y1="{y}" x2="{x + 30}" y2="{y}"/>')
            if r < rows - 1:
                out.append(f'<line class="a-line" x1="{x}" y1="{y}" x2="{x}" y2="{y + 32}"/>')
    for r in range(rows):
        for c in range(cols):
            x, y = 40 + c * 30, 32 + r * 32
            out.append(f'<rect class="a-node a-wave" style="--d:{(c + r) * .18:.2f}s" x="{x - 7}" y="{y - 7}" width="14" height="14" rx="3"/>')
    return _svg("".join(out))


def space():
    """Earth's limb, an orbit, a satellite passing over a ground station."""
    out = [
        '<circle class="a-planet" cx="160" cy="420" r="300"/>',
        '<ellipse class="a-orbit" cx="160" cy="175" rx="190" ry="120"/>',
    ]
    rnd = random.Random(11)
    for _ in range(26):
        out.append(f'<circle class="a-star" cx="{rnd.uniform(0, W):.0f}" cy="{rnd.uniform(0, 100):.0f}" r="{rnd.uniform(.5, 1.3):.1f}"/>')
    # ground station
    out.append('<path class="a-dish" d="M150 124 q10 -14 20 0 z M160 124 v8"/>')
    out.append('<path class="a-beam" d="M160 118 L130 70 M160 118 L190 70"/>')
    # satellite on the orbit
    out.append(
        '<g class="a-sat"><rect x="-5" y="-4" width="10" height="8" rx="1.5"/>'
        '<rect class="a-panel" x="-19" y="-2.5" width="12" height="5"/><rect class="a-panel" x="7" y="-2.5" width="12" height="5"/>'
        '<animateMotion dur="12s" repeatCount="indefinite" rotate="auto" '
        'path="M-30,175 A190,120 0 0 1 350,175"/></g>'
    )
    return _svg("".join(out))


ART = {"ai": ai, "decision": decision, "local": local, "signal": signal, "hpc": hpc, "space": space}
