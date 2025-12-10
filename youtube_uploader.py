# youtube_uploader.py — Darkroom AI YouTube Upload System
# Tamamen yenilenmiş, GitHub Actions ile uyumlu

import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def authenticate_youtube():
    """GitHub Actions ortamında OAuth refresh token ile otomatik Google bağlantısı."""

    creds = Credentials(
        None,
        refresh_token=os.getenv("YT_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("YT_CLIENT_ID"),
        client_secret=os.getenv("YT_CLIENT_SECRET")
    )

    return build("youtube", "v3", credentials=creds)


def upload_video(video_path, title, description, tags, thumbnail_path=None):
    """YouTube'a video yükler."""

    youtube = authenticate_youtube()

    print("📤 Video YouTube'a yükleniyor...")

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "24"  # Entertainment
        },
        "status": {"privacyStatus": "public"}
    }

    media = MediaFileUpload(video_path, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()

    print("✅ Video Yüklendi! Video ID:", response["id"])

    if thumbnail_path:
        upload_thumbnail(youtube, response["id"], thumbnail_path)

    return response["id"]


def upload_thumbnail(youtube, video_id, thumbnail_path):
    """Videoya özel thumbnail yükler."""

    print("🖼️ Thumbnail yükleniyor...")

    youtube.thumbnails().set(
        videoId=video_id,
        media_body=thumbnail_path
    ).execute()

    print("✅ Thumbnail başarıyla yüklendi!")
