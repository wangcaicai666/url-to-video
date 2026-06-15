#!/usr/bin/env python3
"""Render a video from a script, narration audio, and optional visuals.

Usage:
    python render_video.py --script script.md --audio narration.wav --out video.mp4

This is a skeleton. It shells out to ffmpeg with a placeholder background.
Swap in real visuals / slides for production use.
"""
import argparse
import shutil
import subprocess
import sys


def render(script: str, audio: str, out: str, background: str | None) -> int:
    if shutil.which("ffmpeg") is None:
        print("error: ffmpeg not found on PATH", file=sys.stderr)
        return 1

    # Placeholder: a solid color background sized for the narration length.
    bg_source = (
        ["-i", background]
        if background
        else ["-f", "lavfi", "-i", "color=c=black:s=1280x720"]
    )
    cmd = [
        "ffmpeg", "-y",
        *bg_source,
        "-i", audio,
        "-shortest",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        out,
    ]
    print("running:", " ".join(cmd), file=sys.stderr)
    return subprocess.call(cmd)


def main(argv) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--script", required=True)
    p.add_argument("--audio", required=True)
    p.add_argument("--out", default="video.mp4")
    p.add_argument("--background", default=None, help="optional image/video bg")
    args = p.parse_args(argv[1:])
    return render(args.script, args.audio, args.out, args.background)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
