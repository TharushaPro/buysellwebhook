import os
import json
import requests
from flask import Flask, request

app = Flask(__name__)

# Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()

@app.route("/buy", methods=["POST"])
def buy():
    data = request.get_json()

    if data is None or 'signal' not in data:
        return "Invalid data", 400

    signal = data['signal']
    price = data['price']
    coin = data['coin']

    # Handle the signal (e.g., perform trading actions)
    message = f"Received signal: {signal} at price: {price} for {coin}"
    send_telegram_message(message)

    return "Signal received", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
