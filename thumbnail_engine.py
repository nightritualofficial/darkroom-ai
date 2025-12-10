# thumbnail_engine.py — Darkroom AI Thumbnail Generator

import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_thumbnail_prompt(story):
    """Hikayeden atmosfer çıkarıp AI için güçlü bir thumbnail promptu oluşturur."""

    return f"""
    Ultra detailed cinematic horror thumbnail.
    Dark atmosphere, suspense, danger.
    Inspired by the story: {story[:200]}
    Moody lighting, shadows, high contrast.
    YouTube 16:9 format.
    """


def generate_thumbnail(story, out_path="thumbnail.png"):
    """OpenAI Image ile thumbnail oluşturur."""

    prompt = build_thumbnail_prompt(story)

    print("🖼 Thumbnail oluşturuluyor...")

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1280x720"
        )

        img_b64 = response.data[0].b64_json
        img_bytes = base64.b64decode(img_b64)

        with open(out_path, "wb") as f:
            f.write(img_bytes)

        return out_path

    except Exception as e:
        print("Thumbnail creation failed:", e)

        # Yedek boş dosya
        with open(out_path, "wb") as f:
            f.write(b"")

        return out_path
