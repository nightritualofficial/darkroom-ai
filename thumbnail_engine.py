# thumbnail_engine.py — Darkroom AI Thumbnail Generator

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_thumbnail(prompt, output_path="thumbnail.png"):
    """Ucuz model ile 1024x1024 thumbnail üretimi."""
    try:
        response = client.images.generate(
            model="gpt-image-1",
            size="1024x1024",
            prompt=f"dark, cinematic horror thumbnail: {prompt}"
        )

        image_bytes = response.data[0].b64_json
        import base64
        img = base64.b64decode(image_bytes)

        with open(output_path, "wb") as f:
            f.write(img)

        return output_path

    except Exception as e:
        print("thumbnail error:", e)
        return None
