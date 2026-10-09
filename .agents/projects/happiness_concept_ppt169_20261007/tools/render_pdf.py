"""Render the deck SVG pages to a print PDF.

Recipe: cairosvg ``svg2pdf`` keeps text as vector but cannot resolve the
relative raster paths from here.  So each raster ``href`` is swapped for a tiny
8x8 placeholder before rasterising, then ``Page.replace_image`` puts the real
(downscaled, JPEG) photo back into the already-placed frame.  Result: a small
PDF with selectable vector text and real photos.
"""
import base64
import io
import re
import sys
from pathlib import Path

import cairosvg
import pymupdf
from PIL import Image

MAX_W, MAX_H = 1280, 720
RASTER_EXT = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.svg'}


def _load_raster(path: Path) -> bytes:
    if path.suffix.lower() == '.svg':
        # Nested SVG (the slide-15 QR); cairosvg cannot draw it in place, so
        # rasterise at high DPI to keep it scannable in print.
        png = cairosvg.svg2png(url=str(path), output_width=1080, output_height=1080)
        im = Image.open(io.BytesIO(png))
    else:
        im = Image.open(path)
    if im.mode in {'P', 'LA', 'RGBA'}:
        rgba = im.convert('RGBA')
        bg = Image.new('RGB', rgba.size, (255, 255, 255))
        bg.paste(rgba, mask=rgba.split()[-1])
        im = bg
    else:
        im = im.convert('RGB')
    im.thumbnail((MAX_W, MAX_H))
    buf = io.BytesIO()
    if path.suffix.lower() == '.svg':
        # JPEG artefacts break QR decoding, keep the QR lossless PNG.
        im.save(buf, 'PNG', optimize=True)
    else:
        im.save(buf, 'JPEG', quality=80, optimize=True)
    return buf.getvalue()


def render_page(svg_path: Path, out_pdf: Path) -> None:
    base = svg_path.parent
    svg = svg_path.read_text(encoding='utf-8')

    placeholder = Image.new('RGB', (8, 8), (200, 200, 200))
    buf = io.BytesIO()
    placeholder.save(buf, 'PNG')
    placeholder_uri = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()

    rasters: list[Path] = []

    def repl(match: 're.Match[str]') -> str:
        href = match.group(1)
        if href.startswith('data:'):
            return match.group(0)
        path = (base / href).resolve()
        if path.suffix.lower() in RASTER_EXT:
            rasters.append(path)
            return f'href="{placeholder_uri}"'
        return match.group(0)

    svg = re.sub(r'href="([^"]+)"', repl, svg)
    tmp = out_pdf.with_suffix('.page.svg')
    tmp.write_text(svg, encoding='utf-8')
    try:
        cairosvg.svg2pdf(url=str(tmp), write_to=str(out_pdf))
    finally:
        tmp.unlink(missing_ok=True)

    doc = pymupdf.open(out_pdf)
    images = doc[0].get_images(full=True)
    if len(images) != len(rasters):
        raise RuntimeError(
            f'{svg_path.name}: {len(images)} embedded rasters vs '
            f'{len(rasters)} source rasters'
        )
    for info, source in zip(images, rasters):
        doc[0].replace_image(info[0], stream=_load_raster(source))
    tmp_pdf = out_pdf.with_suffix('.tmp.pdf')
    doc.save(str(tmp_pdf), deflate=True, garbage=4)
    doc.close()
    tmp_pdf.replace(out_pdf)


def main(project: Path, out: Path) -> None:
    pages = sorted((project / 'svg_output').glob('*.svg'))
    parts_dir = project / 'validation' / '_pdf_pages'
    parts_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open()
    for index, svg in enumerate(pages, 1):
        page_pdf = parts_dir / f'page{index:02d}.pdf'
        render_page(svg, page_pdf)
        single = pymupdf.open(page_pdf)
        doc.insert_pdf(single)
        single.close()
        print(f'[{index}/{len(pages)}] {svg.name}')
    doc.save(str(out), deflate=True, garbage=4)
    print(f'PDF: {out} pages={doc.page_count} size={out.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    proj = Path(__file__).resolve().parents[1]
    root = proj.parents[2]
    main(
        Path(sys.argv[1]) if len(sys.argv) > 1 else proj,
        Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'Konceptsiya_schastya.pdf',
    )
