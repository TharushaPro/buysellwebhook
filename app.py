import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Webhook is up and running!"

@app.route('/buy', methods=['POST'])
def buy_signal():
    try:
        data = request.get_json()
        # Here, you can extract and handle your buy signal data
        print(f"Buy signal received: {data}")
        return jsonify({"status": "success", "message": "Buy signal received"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/sell', methods=['POST'])
def sell_signal():
    try:
        data = request.get_json()
        # Here, you can extract and handle your sell signal data
        print(f"Sell signal received: {data}")
        return jsonify({"status": "success", "message": "Sell signal received"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    # Use the PORT provided by Heroku or default to 5000
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
