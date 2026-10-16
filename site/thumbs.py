"""Program cover thumbnails framed on the athlete (Abdullah, 15 Oct: list photos were cutting off the
sport and the movement). Finds the lit figure on the dark cover and crops a 4:5 frame around it."""
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).parent
SRC, DST = ROOT / "img" / "covers", ROOT / "img" / "thumbs"
W, H = 640, 800


def pct(vals, q):
    v = sorted(vals)
    return v[min(len(v) - 1, int(len(v) * q / 100))]


def frame(im):
    g = im.convert("L").resize((180, 240)).filter(ImageFilter.GaussianBlur(3))
    px = list(g.get_flattened_data()) if hasattr(g, 'get_flattened_data') else list(g.getdata())
    thr = max(38, pct(px, 88))
    ys = [i // 180 for i, v in enumerate(px) if v > thr]
    xs = [i % 180 for i, v in enumerate(px) if v > thr]
    if len(xs) < 20:
        return (0, 0, im.width, im.height)
    # trim stray light (rim glows, overlay lines) at the edges of the lit mass
    y0, y1 = pct(ys, 2), pct(ys, 99.5); x0, x1 = pct(xs, 3), pct(xs, 97)
    y0 -= (y1 - y0) * 0.16                                  # heads are often darker than the lit body
    sx, sy = im.width / 180, im.height / 240
    x0, x1, y0, y1 = x0 * sx, x1 * sx, y0 * sy, y1 * sy
    bw, bh = (x1 - x0) * 1.25, (y1 - y0) * 1.18           # breathing room around the figure
    h = max(bh, bw * H / W, im.height * 0.62)               # never zoom in past ~1.6x
    h = min(h, im.height); w = h * W / H
    if w > im.width:
        w = im.width; h = w * H / W
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    l = min(max(cx - w / 2, 0), im.width - w); t = min(max(cy - h / 2, 0), im.height - h)
    return (int(l), int(t), int(l + w), int(t + h))


def build(force=False):
    n = 0
    for f in SRC.rglob("*.jpg"):
        out = DST / f.relative_to(SRC)
        if not force and out.exists() and out.stat().st_mtime >= f.stat().st_mtime:
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(f).convert("RGB")
        im.crop(frame(im)).resize((W, H), Image.LANCZOS).save(out, quality=80, optimize=True, progressive=True)
        n += 1
    return n


if __name__ == "__main__":
    print(build(force=True), "thumbnails")
