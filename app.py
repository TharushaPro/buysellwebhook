import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ensure Heroku uses the correct port
port = int(os.environ.get("PORT", 5000))

# Home route to check if the server is working
@app.route('/')
def home():
    return "Hello World"

# Route to handle TradingView signals (POST /buy)
@app.route('/buy', methods=['POST'])
def buy():
    try:
        data = request.get_json()  # Get the JSON payload from TradingView
        
        if not data:
            return jsonify({"error": "No data received"}), 400

        # Log the incoming data for debugging
        print(f"Received signal: {json.dumps(data, indent=4)}")
        
        # Extract the signal from TradingView (for now, we just print it)
        signal = data.get('signal')
        if signal:
            # Handle buy/sell logic here based on the signal
            return jsonify({"message": f"Signal received: {signal}"}), 200
        else:
            return jsonify({"error": "Signal not found in data"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
