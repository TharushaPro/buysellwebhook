import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Telegram Bot Token and Chat ID (replace with your own)
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

# Telegram API URL
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'

def send_telegram_message(message):
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def handle_signal():
    data = request.json
    signal = data.get('signal')
    symbol = data.get('symbol')
    price = data.get('price')
    
    if signal and symbol and price:
        # Create message based on the signal
        message = f"Signal: {signal}\nSymbol: {symbol}\nPrice: {price}"
        send_telegram_message(message)
        return jsonify({'status': 'success', 'message': 'Signal sent to Telegram'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
