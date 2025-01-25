import requests
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Replace with your actual Telegram Bot token and chat ID
telegram_token = 'your_telegram_bot_token'
chat_id = 'your_chat_id'

# Telegram API URL
telegram_api_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

# Function to send Telegram notification
def send_telegram_notification(message):
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    try:
        response = requests.post(telegram_api_url, data=payload)
        print(response.json())  # Print the response for debugging
        if response.status_code == 200:
            print("Telegram notification sent successfully!")
        else:
            print(f"Failed to send Telegram notification, status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")

@app.route('/buy', methods=['POST'])
def buy_signal():
    try:
        # Get JSON data from the incoming POST request
        data = request.get_json()

        # Check if the 'signal' is present in the request
        if 'signal' in data and 'price' in data and 'coin' in data:
            signal = data['signal']
            price = data['price']
            coin = data['coin']
            print(f"Received signal: {data}")  # For debugging

            # Send a Telegram message with the signal info
            message = f"Signal: {signal} \nCoin: {coin} \nPrice: {price}"
            send_telegram_notification(message)

            # Return a success response
            return jsonify({"status": "success", "message": "Signal received and notification sent"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid data received"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error processing request: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
