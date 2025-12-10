import os
import json
import time
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ---------------------------
#  YOUTUBE AUTH SYSTEM
# ---------------------------
def load_credentials():
    """
    Loads OAuth2 credentials from GitHub Secrets.
    """
    client_id = os.getenv("YT_CLIENT_ID")
    client_secret = os.getenv("YT_CLIENT_SECRET")
    refresh_token = os.getenv("YT_REFRESH_TOKEN")

    if not client_id or not client_secret or not refresh_token:
        raise Exception("❌ Missing YouTube OAuth credentials! Add them in GitHub Secrets.")

    creds_data = {
        "token": None,  # not required
        "refresh_token": refresh_token,
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": client_id,
        "client_secret": client_secret,
        "scopes": ["https://www.googleapis.com/auth/youtube.upload"]
    }

    creds = Credentials.from_authorized_user_info(creds_data)

    # Refresh access token
    request = google.auth.transport.requests.Request()
    creds.refresh(request)

    return creds


# ---------------------------
#  UPLOAD FUNCTION
# ---------------------------
def upload_to_youtube(video_path, title, description, tags, category_id="24", is_short=False, thumbnail_path=None):
    """
    Uploads a video or short to YouTube.
    """

    creds = load_credentials()
    youtube = build("youtube", "v3", credentials=creds)

    # Shorts requirement: Must be < 60 seconds
    if is_short:
        print("📱 Uploading as YouTube Short...")
    else:
        print("📺 Uploading as YouTube full video...")

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    print("📤 Uploading video...")

    upload_request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = upload_request.next_chunk()
        if status:
            print(f"⬆️ Upload Progress: {int(status.progress() * 100)}%")

    print("🎉 Video uploaded successfully!")
    print("🔗 Video ID:", response["id"])

    video_id = response["id"]

    # Upload thumbnail if provided
    if thumbnail_path and os.path.exists(thumbnail_path):
        print("🖼️ Uploading thumbnail...")
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumbnail_path)
        ).execute()
        print("✅ Thumbnail uploaded.")

    return video_id


# ---------------------------
#  ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    """
    This script is called by video_engine.py and short generators.
    Example call:
    python youtube_uploader.py "output.mp4" "My Title" "Description here" "tag1,tag2" "thumbnail.jpg" "short"
    """

    import sys

    video_path = sys.argv[1]
    title = sys.argv[2]
    description = sys.argv[3]
    tags = sys.argv[4].split(",")
    thumbnail = sys.argv[5] if sys.argv[5] != "None" else None
    is_short = sys.argv[6].lower() == "short"

    upload_to_youtube(
        video_path=video_path,
        title=title,
        description=description,
        tags=tags,
        is_short=is_short,
        thumbnail_path=thumbnail
    )# placeholder for youtube_uploader.py
