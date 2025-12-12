from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_message(text: str) -> str:
    prompt = f"""
    Классифицируй сообщение по категориям:
    - greeting
    - faq
    - objection
    - closing

    Сообщение: "{text}"

    Ответь одним словом.
    """

    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return result.choices[0].message.content.strip()
