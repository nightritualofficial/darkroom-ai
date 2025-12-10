# thumbnail_engine.py – Darkroom AI Thumbnail (fallback)

import os

# Repo köküne koyacağımız sabit görsel
FALLBACK_THUMBNAIL = "default_thumbnail.png"


def generate_thumbnail(prompt, output_path="thumbnail.png"):
    """
    Şimdilik OpenAI image API kullanmıyoruz (kuruluş doğrulaması istiyor).
    Onun yerine repo kökündeki default_thumbnail.png dosyasını kullanıyoruz.
    """
    if os.path.exists(FALLBACK_THUMBNAIL):
        print("🖼 Thumbnail için yedek görsel kullanılıyor:", FALLBACK_THUMBNAIL)
        return FALLBACK_THUMBNAIL
    else:
        print("❌ default_thumbnail.png bulunamadı, thumbnail olmadan devam edilecek.")
        return None
