# main.py — Darkroom AI Orchestrator
# Bu dosya bütün pipeline'ı baştan sona yönetir.

import argparse
import random
import json
import time

from story_engine import generate_story
from audio_engine import generate_tts
from video_engine import generate_video
from thumbnail_engine import generate_thumbnail
from analytics_engine import analyze_comments, should_generate_part2
# uploader'ı en son ekleyeceğiz
# from youtube_uploader import upload_video

def load_categories():
    """Kategori listesini yükler."""
    with open("categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def choose_random_theme(mode):
    """Short1/Short2/Long videoya göre uygun tema seçer."""
    cats = load_categories()

    if mode in ["short1", "short2"]:
        themes = cats["short_themes"]
    else:
        themes = cats["long_themes"]

    return random.choice(themes)

def orchestrate(mode):
    print(f"\n🚀 DARKROOM-AI PIPELINE BAŞLIYOR ({mode})")
    print("-" * 60)

    # 1) Tema seç
    theme = choose_random_theme(mode)
    print(f"🎭 Seçilen tema: {theme}")

    # 2) Hikaye üret
    story = generate_story(theme, mode)
    print(f"📜 Hikaye oluşturuldu ({len(story)} karakter)\n")

    # 3) Ses üret
    audio_path = generate_tts(story, mode)
    print(f"🎤 Ses dosyası hazır: {audio_path}")

    # 4) Video üret
    final_video = generate_video(story, audio_path, mode)
    print(f"🎬 Video hazır: {final_video}")

    # 5) Thumbnail üret
    thumbnail_path = generate_thumbnail(story)
    print(f"🖼 Thumbnail üretildi: {thumbnail_path}")

    # 6) Upload — EN SON EKLENECEK
    print("⏳ Upload aşaması en son bağlanacak...")
    # upload_result = upload_video(final_video, thumbnail_path, story)
    # print(f"📤 Video YouTube'a yüklendi: {upload_result}")

    # 7) Analytics kontrolü (Part 2 kontrol)
    # if upload_result:
    #     video_id = upload_result["video_id"]
    #     print("👁‍🗨 Yorumlar analiz ediliyor...")
    #     if should_generate_part2(video_id):
    #         print("🔥 Part 2 yarın üretilecek.")
    #     else:
    #         print("ℹ️ Part 2 gerekmiyor.")

    print("\n✅ PIPELINE BAŞARIYLA TAMAMLANDI")
    print("-" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="short1",
                        help="short1 | short2 | long")
    args = parser.parse_args()

    orchestrate(args.mode)
