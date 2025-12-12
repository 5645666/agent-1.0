from flask import Flask, request
from core.agent import Agent
from instagram.sender import InstagramSender
import os
from dotenv import load_dotenv

load_dotenv()

VERIFY_TOKEN = os.getenv("IG_VERIFY_TOKEN")

app = Flask(__name__)
agent = Agent()
sender = InstagramSender()

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge
    
    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    for entry in data.get("entry", []):
        for messaging in entry.get("messaging", []):
            sender_id = messaging["sender"]["id"]
            message_text = messaging["message"]["text"]

            response = agent.handle_message(message_text)
            sender.send_message(response, user_id=sender_id)

    return "ok", 200
