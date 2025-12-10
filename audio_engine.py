# audio_engine.py — Darkroom AI TTS Engine

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tts(text, mode):
    """Hikayeyi OpenAI TTS kullanarak sese çevirir."""

    # Mode'a göre dosya adı
    audio_path = "audio_output.wav"

    try:
        print("🎤 TTS oluşturuluyor...")

        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",        # doğal, net, tüyler ürperten ses
            input=text
        )

        # Ses dosyasını yaz
        with open(audio_path, "wb") as f:
            f.write(response.read())

        return audio_path

    except Exception as e:
        print("TTS Error:", e)

        # Yedek ses (pipeline çökmesin)
        with open(audio_path, "wb") as f:
            f.write(b"")

        return audio_path
