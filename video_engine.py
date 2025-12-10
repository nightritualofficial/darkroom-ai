# video_engine.py – Darkroom AI Video Builder

import os
import subprocess
import time

def generate_video(audio_path, image_path, output_path=None):
    """Audio + image ile video oluşturur."""

    if not os.path.exists(audio_path):
        print("❌ Audio dosyası yok!")
        return None

    if not os.path.exists(image_path):
        print("❌ Thumbnail dosyası yok!")
        return None

    # Benzersiz video adı
    if output_path is None:
        ts = int(time.time())
        output_path = f"output_video_{ts}.mp4"

    try:
        cmd = [
            "ffmpeg",
            "-y",
            "-loop", "1",
            "-i", image_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            output_path
        ]

        print("▶️ FFmpeg çalışıyor...")
        subprocess.run(cmd, check=True)
        print("✅ Video üretildi:", output_path)

        return output_path

    except Exception as e:
        print("❌ Video generation error:", e)
        return None
