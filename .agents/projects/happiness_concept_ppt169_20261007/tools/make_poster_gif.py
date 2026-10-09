"""Build the slide-6 animated poster GIF from the brain-neurons video.

The mp4 in ``media/`` is not tracked in the repository, so this recreates both
the animated GIF the SVG points at (``images/brain_neurons.gif``) and the static
fallback poster (``images/p06_video_poster.jpg``). Needs opencv-python and PIL.
"""
from pathlib import Path

import cv2
from PIL import Image

FPS_OUT = 8
GIF_SIZE = (320, 230)
POSTER_SIZE = (960, 540)


def main() -> None:
    proj = Path(__file__).resolve().parents[1]
    src = proj / 'media' / 'brain_neurons.mp4'
    cap = cv2.VideoCapture(str(src))
    fps = cap.get(cv2.CAP_PROP_FPS)
    step = max(1, round(fps / FPS_OUT))
    frames = []
    i = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if i % step == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(
                Image.fromarray(frame)
                .resize(GIF_SIZE, Image.LANCZOS)
                .convert('P', palette=Image.ADAPTIVE, colors=24)
            )
        i += 1
    cap.release()

    frame_ms = int(round(1000 * step / fps))
    frames[0].save(
        proj / 'images' / 'brain_neurons.gif', save_all=True,
        append_images=frames[1:], duration=frame_ms, loop=0,
        optimize=True, disposal=2,
    )
    frames[0].convert('RGB').resize(POSTER_SIZE, Image.LANCZOS).save(
        proj / 'images' / 'p06_video_poster.jpg', quality=88,
    )
    print(f'{len(frames)} frames @ {frame_ms} ms -> images/brain_neurons.gif + poster')


if __name__ == '__main__':
    main()
