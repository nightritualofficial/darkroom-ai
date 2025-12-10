import os
from story_engine import generate_story
from audio_engine import generate_audio
from thumbnail_engine import generate_thumbnail
from video_engine import generate_video
import json, random

def load_categories():
    with open("categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def select_random_theme():
    categories = load_categories()
    all_items = [item for category in categories.values() for item in category]
    return random.choice(all_items)

def pipeline(mode="short1"):
    print("\n🔥 DARKROOM-AI PIPELINE BAŞLIYOR 🔥")

    theme = select_random_theme()
    print("🎭 Seçilen tema:", theme)

    story = generate_story(theme, mode)
    print("📜 Hikaye oluşturuldu.\n")

    audio_path = generate_audio(story)
    print("🔊 Ses hazır:", audio_path)

    img_prompt = theme
    thumbnail_path = generate_thumbnail(img_prompt)
    print("🖼 Thumbnail:", thumbnail_path)

    video_path = generate_video(audio_path, thumbnail_path)
    print("🎬 Video hazır:", video_path)

    print("\n🎉 PIPELINE TAMAMLANDI! 🎉")
    return video_path

if __name__ == "__main__":
    pipeline()
