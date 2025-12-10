# thumbnail_engine.py – Darkroom AI Thumbnail Generator
import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_thumbnail(prompt, output_path="thumbnail.png"):
    """Thumbnail image generator using gpt-image-1-mini."""

    try:
        response = client.images.generate(
            model="gpt-image-1-mini",
            prompt=prompt,
            size="1024x1024"
        )

        image_base64 = response.data[0].b64_json

        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_base64))

        return output_path

    except Exception as e:
        print("Thumbnail generation error:", e)
        return None
