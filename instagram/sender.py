import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")

class InstagramSender:
    def send_message(self, text: str, user_id: str):
        url = f"https://graph.facebook.com/v21.0/me/messages"

        payload = {
            "recipient": {"id": user_id},
            "message": {"text": text}
        }

        params = {
            "access_token": ACCESS_TOKEN
        }

        requests.post(url, json=payload, params=params)
