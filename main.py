import requests
import json
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = "7972927579:AAGc7yetmrwqV7RvfDgkQQCM3t2HSjC4xj4"
CHAT_ID = "5824295830"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

@app.route("/", methods=["GET"])
def home():
    return "Ultimate Power Bot is Running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    try:
        pair = data.get("pair", "UNKNOWN")
        action = data.get("action", "BUY")
        entry = data.get("entry", "0.0000")
        sl = data.get("sl", "0.0000")
        tp1 = data.get("tp1", "0.0000")
        confidence = data.get("confidence", "N/A")
        strategy = data.get("strategy", "Unknown Strategy")

        message = f"""🚨 *Sinyal Trading Terdeteksi*

📌 *Pair*: `{pair}`
🟢 *Action*: *{action}*
🎯 *Entry*: `{entry}`
🛡 *Stop Loss*: `{sl}`
🎯 *Take Profit*: `{tp1}`
🧠 *Confidence*: `{confidence}`
📚 *Strategi*: _{strategy}_

⚠️ *Analisis lengkap* hanya untuk member premium.
"""
        send_telegram_message(message)
        return {"status": "sent"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
