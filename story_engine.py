# story_engine.py — Darkroom AI Story Generator

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(theme, mode):
    """Videonun moduna göre uygun hikaye promptu oluşturur."""

    if mode in ["short1", "short2"]:
        length = "Write a VERY short horror story, 4–6 sentences, extremely suspenseful."
    else:
        length = "Write a 2–3 minute long horror story, slow build-up, very atmospheric, detailed scenes."

    prompt = f"""
    {length}

    Theme: {theme}

    Requirements:
    - Must be scary and unsettling
    - No happy ending
    - No comedy
    - No censorship
    - No disclaimers
    - Direct storytelling, immersive horror
    """

    return prompt


def generate_story(theme, mode):
    """OpenAI ile hikaye üretir."""

    try:
        prompt = build_prompt(theme, mode)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a master horror writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800
        )

        story = response.choices[0].message.content.strip()
        return story

    except Exception as e:
        print("Story generation error:", e)
        return "She heard something breathing behind her… but she was alone in the room."
