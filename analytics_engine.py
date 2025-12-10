# analytics_engine.py — Darkroom AI Comment Analyzer
# Bu sürüm YouTube API henüz eklenmediği için simüle analiz yapar.
# Uploader tamamlandığında gerçek veriye bağlanacak şekilde tasarlanmıştır.

import random

def analyze_comments(video_id):
    """
    Yorumları analiz eder.
    Şu anda simüle edildiği için rastgele bir analiz döndürür.
    Uploader tamamlandığında gerçek YouTube API'sine bağlanacak.
    """

    print(f"📊 Yorumlar analiz ediliyor (video: {video_id})...")

    fake_comments = [
        "Part 2 pls!!",
        "This was terrifying omg",
        "More like this!",
        "DROP PART 2 NOW",
        "Amazing work bro",
        "Part2??",
        "make a series plsss"
    ]

    return fake_comments


def should_generate_part2(video_id):
    """
    Yorumlarda 'part 2' isteği varsa true döner.
    Şu anda fake veri ile çalışır.
    """

    comments = analyze_comments(video_id)

    part2_count = sum("part" in c.lower() and "2" in c.lower() for c in comments)

    print(f"🔎 'Part 2' tespit edilen yorum sayısı: {part2_count}")

    # En az 2 kişi istemişse ertesi gün Part 2 planlanır
    return part2_count >= 2
