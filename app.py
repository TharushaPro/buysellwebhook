import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Your Telegram Bot Token and Chat ID
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

# Send message to Telegram function
def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    print(response.text)  # Log the response from Telegram API

@app.route("/buy", methods=["POST"])
def buy_signal():
    # Get the JSON data from TradingView
    signal_data = request.json
    signal = signal_data.get("signal")
    price = signal_data.get("price")
    coin = signal_data.get("coin")
    
    if signal and price and coin:
        # Create a message to send to Telegram
        message = f"Signal received: {signal} for {coin} at price {price}"
        
        # Send the message to Telegram
        send_telegram_notification(message)
        
        # Handle your trading logic here (e.g., place order on Binance)
        
        return jsonify({"status": "success", "message": "Signal received"})
    else:
        return jsonify({"status": "error", "message": "Invalid data received"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
