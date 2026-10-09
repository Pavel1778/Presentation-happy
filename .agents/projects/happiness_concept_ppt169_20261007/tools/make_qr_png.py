"""Rasterise the slide-15 QR SVG into a lossless PNG for embedding.

The QR source is an SVG; PowerPoint renders a picture whose blip points at an
SVG part inconsistently, so the deck embeds a plain PNG instead. Regenerate the
PNG after editing ``images/qr_sources.svg`` and keep the module quiet enough
(high DPI, no JPEG) that the code still decodes.
"""
from pathlib import Path

import cairosvg

PROJ = Path(__file__).resolve().parents[1]


def main() -> None:
    src = PROJ / 'images' / 'qr_sources.svg'
    dst = PROJ / 'images' / 'qr_sources.png'
    cairosvg.svg2png(
        url=str(src), write_to=str(dst),
        output_width=1080, output_height=1080, background_color='white',
    )
    print(f'{src.name} -> {dst.name} (1080x1080, lossless)')


if __name__ == '__main__':
    main()
