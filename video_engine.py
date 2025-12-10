# video_engine.py — Darkroom AI Video Builder

import os
import subprocess

def generate_video(audio_path, image_path, output_path="video.mp4"):
    """Audio + thumbnail ile video oluşturur."""

    if not os.path.exists(audio_path):
        print("audio file missing")
        return None

    if not os.path.exists(image_path):
        print("image file missing")
        return None

    try:
        cmd = [
            "ffmpeg", "-loop", "1",
            "-i", image_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            output_path,
            "-y"
        ]

        subprocess.run(cmd, check=True)

        return output_path

    except Exception as e:
        print("video generation error:", e)
        return None
