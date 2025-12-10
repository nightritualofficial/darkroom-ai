# analytics_engine.py — Darkroom AI Analytics

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_comments(comments):
    """Yorumlara göre hangi tema daha iyi performans veriyor."""
    try:
        text = "\n".join(comments)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Analyze horror video comments and determine interest themes."},
                {"role": "user", "content": text}
            ],
            max_tokens=200
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("analytics error:", e)
        return "analysis unavailable"
