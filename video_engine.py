# video_engine.py — Darkroom AI Video Generator

import os
import subprocess
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_background_image(prompt, out_path="bg.png"):
    """OpenAI Image ile atmosferik bir korku görseli üretir."""
    try:
        print("🖼 Arka plan görseli üretiliyor...")

        response = client.images.generate(
            model="gpt-image-1",
            prompt=f"Dark horror atmosphere, cinematic, extremely detailed, {prompt}",
            size="1024x576"
        )

        image_bytes = response.data[0].b64_json
        import base64
        img = base64.b64decode(image_bytes)

        with open(out_path, "wb") as f:
            f.write(img)

        return out_path

    except Exception as e:
        print("Image generation failed:", e)
        return None


def generate_video(story, audio_path, mode):
    """FFmpeg ile ses + arka plan görüntüsü birleştirerek video oluşturur."""

    # Süre ayarı
    if mode == "long":
        duration = 150   # ~2.5 dakika
    else:
        duration = 20    # short videolar için 15–30 s

    bg_path = "background.png"
    final_video = "final_video.mp4"

    # Arka plan görüntüsünü yarat
    generate_background_image(story[:100], bg_path)

    print("🎬 Video oluşturuluyor...")

    try:
        # 1) Görselden duran video yarat
        subprocess.run([
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", bg_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-t", str(duration),
            "-pix_fmt", "yuv420p",
            "-shortest",
            final_video
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        return final_video

    except Exception as e:
        print("Video generation error:", e)
        return None
