"""Turn the slide-6 poster picture into an embedded, playable video.

The ppt-master exporter has no native mp4 flag, so the video deck is produced
from the video-less export: the picture named ``Image 8`` (the slide-6 poster)
keeps its frame and poster, and gains a media relationship plus the
``a:videoFile`` / ``p14:media`` wiring PowerPoint needs to play an mp4.
"""
import re
import sys
import zipfile
from pathlib import Path

NS_P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
NS_A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
NS_P14 = 'http://schemas.microsoft.com/office/powerpoint/2010/main'
NS_R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

VIDEO_REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/video'
MEDIA_REL = 'http://schemas.microsoft.com/office/2007/relationships/media'
PIC_NAME = 'Image 8'
VIDEO_PART = 'ppt/media/slide6_video.mp4'


def _relationship_ids(xml: str) -> set[int]:
    return {int(m) for m in re.findall(r'Id="rId(\d+)"', xml)}


def main(src: Path, dst: Path, video: Path) -> None:
    with zipfile.ZipFile(src) as z:
        parts = {name: z.read(name) for name in z.namelist()}

    rels_name = 'ppt/slides/_rels/slide6.xml.rels'
    rels = parts[rels_name].decode('utf-8')
    used = _relationship_ids(rels)
    video_rid = f'rId{max(used) + 1}'
    media_rid = f'rId{max(used) + 2}'
    parts[VIDEO_PART] = video.read_bytes()
    parts[rels_name] = rels.replace(
        '</Relationships>',
        f'<Relationship Id="{media_rid}" Type="{MEDIA_REL}" '
        f'Target="../media/slide6_video.mp4"/>'
        f'<Relationship Id="{video_rid}" Type="{VIDEO_REL}" '
        f'Target="../media/slide6_video.mp4"/></Relationships>',
    ).encode('utf-8')

    xml = parts['ppt/slides/slide6.xml'].decode('utf-8')
    pic = re.search(
        rf'<p:pic>(?:(?!</p:pic>).)*?name="{re.escape(PIC_NAME)}"'
        rf'(?:(?!</p:pic>).)*?</p:pic>',
        xml, re.S,
    )
    if pic is None:
        raise RuntimeError(f'picture {PIC_NAME!r} not found in slide6.xml')
    patched = pic.group(0)
    patched = patched.replace(
        '<p:cNvPr id="8" name="Image 8" />',
        '<p:cNvPr id="8" name="Image 8" descr="Видео: нейросети мозга">'
        f'<a:hlinkClick r:id="" action="ppaction://media"/>'
        f'</p:cNvPr>',
    )
    patched = patched.replace('<p:nvPr />', (
        f'<p:nvPr><a:videoFile r:link="{video_rid}"/><p:extLst>'
        f'<p:ext uri="{{DAA4B4D4-6D71-4841-9C94-3DE7FCFB9230}}">'
        f'<p14:media xmlns:p14="{NS_P14}" xmlns:r="{NS_R}" r:embed="{media_rid}"/>'
        f'</p:ext></p:extLst></p:nvPr>'
    ))
    xml = xml.replace(pic.group(0), patched)
    parts['ppt/slides/slide6.xml'] = xml.encode('utf-8')

    content_types = parts['[Content_Types].xml'].decode('utf-8')
    if 'Extension="mp4"' not in content_types:
        content_types = content_types.replace(
            '<Default Extension="mp3"',
            '<Default Extension="mp4" ContentType="video/mp4"/><Default Extension="mp3"',
            1,
        )
    parts['[Content_Types].xml'] = content_types.encode('utf-8')

    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as out:
        for name, data in parts.items():
            out.writestr(name, data)
    print(f'Embedded slide-6 video -> {dst} ({video_rid}/{media_rid})')


if __name__ == '__main__':
    proj = Path(__file__).resolve().parents[1]
    root = proj.parents[2]
    main(
        Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'Konceptsiya_schastya_bez_video.pptx',
        Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'Konceptsiya_schastya.pptx',
        Path(sys.argv[3]) if len(sys.argv) > 3 else proj / 'media' / 'brain_neurons.mp4',
    )
