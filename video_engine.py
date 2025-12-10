name: Run Daily Video

on:
  workflow_dispatch:
  schedule:
    - cron: "0 */6 * * *"

jobs:
  run-video:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install Requirements
        run: pip install -r requirements.txt

      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Generate Daily Video
        run: python3 main.py

      - name: Upload to YouTube
        env:
          YT_CLIENT_SECRET: ${{ secrets.YT_CLIENT_SECRET }}
          YT_TOKEN: ${{ secrets.YT_TOKEN }}
        run: |
          python3 youtube_uploader.py
