# audio_engine.py — Darkroom AI TTS Engine

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_audio(text, output_path="audio_output.wav"):
    """Ucuz model ile TTS üretimi."""
    try:
        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        )

        with open(output_path, "wb") as f:
            f.write(response.read())

        return output_path

    except Exception as e:
        print("audio generation error:", e)
        return None
