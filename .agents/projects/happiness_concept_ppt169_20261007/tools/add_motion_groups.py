"""Split selected SVG blocks into direct-root groups for per-click animation.

Rewrites ``svg_output/*.svg`` in place. Elements already drawn on the page are
re-parented into new *direct-root* groups (siblings of the current top-level
groups) so the exporter can animate each block on its own and Morph-pair a
carrier across adjacent slides. Geometry and paint are untouched.
"""
from pathlib import Path
from xml.etree import ElementTree as ET

PROJ = Path(__file__).resolve().parents[1]
SVG = PROJ / 'svg_output'
SVGNS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVGNS)


def _tag(elem: ET.Element) -> str:
    return elem.tag.rsplit('}', 1)[-1]


def _find_group(root: ET.Element, gid: str) -> ET.Element:
    for child in list(root):
        if _tag(child) == 'g' and child.get('id') == gid:
            return child
    raise KeyError(gid)


def _insert_after(root: ET.Element, anchor: ET.Element, node: ET.Element) -> None:
    root.insert(list(root).index(anchor) + 1, node)


def _new_group(gid: str, bounds: str, role: str | None = None) -> ET.Element:
    attrs = {'id': gid, 'data-pptx-bounds': bounds}
    if role:
        attrs['data-pptx-role'] = role
    return ET.Element(f'{{{SVGNS}}}g', attrs)


def _carve(root, source_gid, specs, after_gid, role=None):
    """Move child slices of *source_gid* into new root groups after *after_gid*."""
    after = _find_group(root, after_gid)
    src = _find_group(root, source_gid)
    children = list(src)
    for gid, bounds, a, b in specs:
        group = _new_group(gid, bounds, role)
        for elem in children[a:b]:
            src.remove(elem)
            group.append(elem)
        _insert_after(root, after, group)
        after = group
    if len(src) == 0:
        root.remove(src)


def _extract(root, source_gid, predicate, new_gid, bounds, after_gid, role=None):
    src = _find_group(root, source_gid)
    moved = [e for e in list(src) if predicate(e)]
    group = _new_group(new_gid, bounds, role)
    for elem in moved:
        src.remove(elem)
        group.append(elem)
    _insert_after(root, _find_group(root, after_gid), group)


def main() -> None:
    # 04_science: swb -> 3 blocks; approaches -> 4 cards
    root = ET.parse(SVG / '04_science.svg').getroot()
    _carve(root, 'swb', [
        ('swb-left', '80 175 340 195', 0, 4),
        ('swb-mid', '450 168 380 210', 4, 9),
        ('swb-right', '860 175 340 195', 9, 13),
    ], after_gid='title')
    _carve(root, 'approaches', [
        ('appr-1', '80 400 272 118', 0, 3),
        ('appr-2', '367 400 272 118', 3, 6),
        ('appr-3', '654 400 272 118', 6, 9),
        ('appr-4', '941 400 272 118', 9, 12),
    ], after_gid='swb-right')
    ET.ElementTree(root).write(SVG / '04_science.svg', encoding='utf-8', xml_declaration=True)

    # 13_recommendations: recs -> 6 cards
    root = ET.parse(SVG / '13_recommendations.svg').getroot()
    _carve(root, 'recs', [
        ('rec-1', '80 180 360 215', 0, 4),
        ('rec-2', '460 180 360 215', 4, 8),
        ('rec-3', '840 180 360 215', 8, 12),
        ('rec-4', '80 415 360 215', 12, 16),
        ('rec-5', '460 415 360 215', 16, 20),
        ('rec-6', '840 415 360 215', 20, 24),
    ], after_gid='title')
    ET.ElementTree(root).write(SVG / '13_recommendations.svg', encoding='utf-8', xml_declaration=True)

    # 08_formula: donut -> 3 sectors + center (wedges overlap by design)
    root = ET.parse(SVG / '08_formula.svg').getroot()
    _carve(root, 'donut', [
        ('donut-seg1', '180 222 150 300', 0, 1),
        ('donut-seg2', '241 250 89 272', 1, 2),
        ('donut-seg3', '241 222 89 73', 2, 3),
        ('donut-center', '205 338 250 78', 3, 5),
    ], after_gid='title', role='decoration')
    ET.ElementTree(root).write(SVG / '08_formula.svg', encoding='utf-8', xml_declaration=True)

    # 10_easterlin / 11_education: pull the data polyline + accent circle out
    root = ET.parse(SVG / '10_easterlin.svg').getroot()
    _extract(root, 'chart', lambda e: _tag(e) == 'polyline',
             'chart-line', '150 278 650 222', 'chart', role='decoration')
    _extract(root, 'chart', lambda e: _tag(e) == 'circle',
             'chart-mark', '579 291 22 22', 'chart-line', role='decoration')
    ET.ElementTree(root).write(SVG / '10_easterlin.svg', encoding='utf-8', xml_declaration=True)

    root = ET.parse(SVG / '11_education.svg').getroot()
    _extract(root, 'chart', lambda e: _tag(e) == 'polyline',
             'chart-line', '180 300 560 200', 'chart', role='decoration')
    _extract(root, 'chart', lambda e: _tag(e) == 'circle',
             'chart-mark', '409 489 22 22', 'chart-line', role='decoration')
    ET.ElementTree(root).write(SVG / '11_education.svg', encoding='utf-8', xml_declaration=True)

    print('motion groups created')


if __name__ == '__main__':
    main()
