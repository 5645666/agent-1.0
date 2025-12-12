from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(user_text: str, scenario: dict) -> str:
    prompt = f"""
    Ты — ИИ-консультант Instagram магазина.
    Сценарий: {scenario}

    Сообщение пользователя: {user_text}

    Ответь вежливо, продающе, коротко.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
