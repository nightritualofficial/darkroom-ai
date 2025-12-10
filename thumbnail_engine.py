# thumbnail_engine.py – Darkroom AI Thumbnail Generator
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_thumbnail(prompt, output_path="thumbnail.png"):
    """Thumbnail image generator."""

    try:
        response = client.images.generate(
            model="gpt-4o-mini",   # gpt-image-1 yerine mini model
            prompt=prompt,
            size="1024x1024"
        )

        image_base64 = response.data[0].b64_json

        # Kaydet
        import base64
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_base64))

        return output_path

    except Exception as e:
        print("Thumbnail generation error:", e)
        return None
