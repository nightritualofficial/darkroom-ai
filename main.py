from story_engine import generate_story
from audio_engine import generate_tts
from thumbnail_engine import generate_thumbnail
from video_engine import create_video
from analytics_engine import analyze_category

import random
import json

def load_categories():
    with open("categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_prompt():
    categories = load_categories()
    category = random.choice(categories["horror"])
    return f"Write a short horror story about: {category}"

def main():
    print("🟣 DARKROOM-AI PIPELINE BAŞLIYOR")

    # Hikâye üretimi
    prompt = generate_prompt()
    print(f"📌 Seçilen tema: {prompt}")

    story = generate_story(prompt)
    print(f"✍️ Hikaye oluşturuldu ({len(story)} karakter)")

    # Ses oluşturma
    audio_path = generate_tts(story)
    print(f"🔊 Ses dosyası hazır: {audio_path}")

    # Thumbnail / görsel
    image_prompt = f"Horror scene: {prompt}"
    thumbnail_path = generate_thumbnail(image_prompt)
    print(f"🖼 Thumbnail üretildi: {thumbnail_path}")

    # Video oluştur
    video_path = create_video(thumbnail_path, audio_path)
    print(f"🎬 Video oluşturuldu: {video_path}")

    print("✅ PIPELINE BAŞARIYLA TAMAMLANDI")

if __name__ == "__main__":
    main()
